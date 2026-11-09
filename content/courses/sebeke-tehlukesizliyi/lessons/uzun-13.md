+++
title = "Virtuallaşdırmanın əsasları və təhlükəsizliyi"
unit = "uzun"
order = 13
summary = "Tam mühazirə: virtuallaşdırma obyektləri, hipervizorlar, virtual resurslar və şəbəkələr, snapshot və köçürmə, klaster, konteynerlər, təhdidlər, sərtləşdirmə və diaqnostika."
updated = 2026-11-09

[[source]]
title = "Mühazirə 13: Virtuallaşdırmanın əsasları və təhlükəsizliyi"
note = "Elmar Cabbarov, 2026–2027"
+++

Virtuallaşdırma (virtualization) fiziki hesablama resursunu proqramlara məntiqi resurs kimi təqdim etmək və istifadəsini idarə etmək üsuludur. Proqram fiziki serverin bütün quruluşunu bilmir; ona ayrılmış virtual prosessoru, yaddaşı, diski və şəbəkə interfeysini görür. Bu təqdimatı yaradan proqram təbəqəsi eyni fiziki qurğudan bir neçə mühitin istifadəsini əlaqələndirir. Resursların **paylaşılması** və mühitlərin **ayrılması** birlikdə düşünülməlidir: paylaşma səmərəlilik verir, ayırma isə bir mühitin digərinə icazəsiz təsirini məhdudlaşdırır.

Mühazirənin ardıcıllığı: anlayış və obyektlər, hipervizorlar, virtuallaşdırma üsulları, resurslar, virtual şəbəkələr, həyat dövrü (şablon, snapshot, köçürmə), klaster və bərpa, konteynerlər, təhdidlər, sərtləşdirmə, konteyner təhlükəsizliyi, diaqnostika. Universitet topologiyası, VLAN nömrələri, GiB hesabları şərti tədris nümunəsidir.

## Virtuallaşdırma nədir

Virtual maşın (virtual machine, VM) öz əməliyyat sistemi və tətbiqləri olan məntiqi kompüterdir. Fiziki kompüter **host**, VM daxilindəki əməliyyat sistemi **qonaq** əməliyyat sistemi adlanır. Hipervizor (hypervisor), yaxud virtual maşın monitoru (virtual machine monitor, VMM), qonaqlara resurs ayırır və aparat üzərindəki əməliyyatlarını nəzarətdə saxlayır. Misal: universitetin `lms.unec.example` xidməti bir Linux VM-də, tələbə bazası başqa VM-də işləyə bilər. Hər ikisi eyni fiziki serverdə olsa da, ayrı disklərə, hesablara və şəbəkə siyasətlərinə malikdir.

:::note Sadə dillə
Ənənəvi yanaşmada hər tətbiq ayrı serverdə işləyirdi və serverlərin çoxu gücünün kiçik hissəsini istifadə edirdi. Virtuallaşdırmada bir güclü server çoxlu VM daşıyır. Üstünlüyü: yer, enerji, soyutma qənaəti. Qiyməti: bütün yumurtalar bir səbətdədir.
:::

### Nə üçün ayrı serverlər birləşdirilir

Hər tətbiq üçün ayrıca fiziki server idarəni sadələşdirə bilər, amma tətbiqlərin pik yükü eyni vaxta düşmədikdə resursun bir hissəsi boş qalır. Konsolidasiya (consolidation) həmin işləri daha az fiziki hostda toplamaqdır. Kafedranın daxili saytı əsasən gündüz, kitabxananın kataloqu semestr ərzində, LMS isə imtahan günlərində çox işlənir; bu fərqlər ölçülərsə, ortaq resurs hovuzu ayrı serverlərdən qənaətli ola bilər. Qənaət faizi universal deyil: lisenziya, saxlama, elektrik, ehtiyat tutum və əmək xərcləri ayrıca hesablanır.

Şərti nümunə: üç tətbiqə üç fiziki server ayrılıb, yaddaşın böyük hissəsi boşdur. Onları bir hostda üç VM kimi yerləşdirmək yer və elektrik xərcini azaldır, amma həmin host sıradan çıxanda üç xidmət birlikdə dayanır. İki host və bərpa mexanizmi xərci artırır, dayanma riskini azaldır. Düzgün sual yalnız "neçə server azalır" deyil, "qalan serverlər hansı nasazlıq yükünü daşıyır" sualıdır.

| Fayda | Mexanizm | Universitetdə yoxlanmalı şərt |
| --- | --- | --- |
| Konsolidasiya | Bir hostda bir neçə ayrı VM | İmtahan vaxtı CPU, yaddaş və disk ehtiyatı qalırmı? |
| Sürətli yerləşdirmə | Hazır şablondan VM yaradılır | Şablon yamanıbmı, fərdi kimlik yaradılırmı? |
| İdarənin sadələşməsi | Mərkəzi inventar və avtomatlaşdırma | Dəyişikliyi edən hesab və təsdiq qeydə alınırmı? |
| Yüksək əlçatanlıq | Nasaz hostun VM-i başqa hostda başlanır | Klaster, saxlama və ehtiyat tutum sazlanıbmı? |
| Tədris mühitinin ayrılması | Hər qrupa ayrıca VM və şəbəkə | Laboratoriyanın inzibati şəbəkəyə yolu bağlanıbmı? |

Konspektdəki dörd fayda: konsolidasiya, etibarlılıq (VM başqa hostda başladıla bilər, **HA sazlanıbsa**), klasterləşmə (hostlar ortaq hovuz yaradır, yük balanslaşdırılır), asan idarə (şablondan dəqiqələrlə VM, klonlama, snapshot).

### Virtuallaşdırma obyektləri

Virtuallaşdırma bütün kompüterə, ayrı resursa və ya tətbiqin məlumatı görmə üsuluna aid ola bilər. Eyni söz işlədilsə də, bu texnologiyaların etibar sərhədləri fərqlidir.

| Obyekt | Təqdim edilən görünüş | Universitet nümunəsi |
| --- | --- | --- |
| Virtual maşın (server virtuallaşdırılması) | Öz nüvəsi olan kompüter | Tələbə uçotu üçün ayrıca server |
| Konteyner (ƏS səviyyəsi) | Ayrılmış proses və fayl mühiti | Kitabxana axtarış xidmətinin tətbiqi |
| Virtual şəbəkə | Məntiqi portlar, seqmentlər, marşrutlar | Laboratoriya ilə inzibati zonanın ayrılması |
| Saxlama resursu (storage virtualization) | Fiziki disklərdən ayrılmış məntiqi həcm | LMS disklərinin ortaq massivdə saxlanması |
| Verilənlər (data virtualization) | Mənbələr üzərində vahid sorğu görünüşü | Tələbə uçotu ilə kitabxana məlumatının əlaqələndirilməsi |

:::warning Üç qarışdırılan anlayış
Operativ yaddaşın virtual ünvanlanması ilə saxlama virtuallaşdırılması fərqlidir: birincidə proses ünvanları yaddaş səhifələrinə, ikincidə fiziki disklər məntiqi həcmlərə çevrilir. Tələbə bazasının VM daxilində işləməsi özlüyündə verilənlərin virtuallaşdırılması deyil: bazanın yerləşdiyi kompüterin virtual olması ilə bir neçə bazaya vahid sorğu interfeysi qurmaq ayrı məsələlərdir.
:::

### VM-in dörd xüsusiyyəti və sərhədləri

Dörd xüsusiyyət müəllimin slaydından gəlir, amma **şərtlidir**; hər birini zəmanət kimi yox, hansı şərtlərdə işlədiyi ilə əzbərləmək lazımdır.

| Xüsusiyyət | Mənası | Sərhəd |
| --- | --- | --- |
| İnkapsulyasiya (encapsulation) | VM konfiqurasiya, virtual disk və vəziyyət faylları ilə təsvir olunur; köçürmək olur | Yalnız disk faylı həmişə kifayət etmir: şifrələmə açarı, virtual firmware parametrləri, əlavə disklər də lazım ola bilər. İşləyən VM-in RAM vəziyyəti saxlanmayıbsa, söndürülmüş disk nüsxəsindən proseslər davam etmir |
| İzolyasiya (isolation) | Bir VM-in başqa VM-in yaddaşına və resurslarına birbaşa icazəsiz çıxışı məhdudlaşır | LMS tətbiqinin çökməsi adətən bazanın ƏS-ni çökdürmür; amma ortaq host, hipervizor, disk və prosessor riskləri qalır |
| Uyğunluq (compatibility) | Standart virtual qurğular qonağın müxtəlif hostlarda işləməsini asanlaşdırır | Prosessor arxitekturası, sürücü, proqram və lisenziya şərtləri ilə məhduddur |
| Avadanlıqdan nisbi müstəqillik | VM-in fiziki server modelinə bağlılığı azalır | Intel əsaslı hostlar arasında daşınma x86 qonağı fərqli arxitekturaya köçürməklə eyni deyil; birbaşa verilmiş GPU və ya şəbəkə qurğusu daşınmanı məhdudlaşdırır |

## Hipervizorların arxitekturası

### Birinci tip və ikinci tip

Birinci tip hipervizor (type 1, bare metal) avadanlıq üzərində virtuallaşdırma nəzarətini özü qurur; altında ayrıca ümumi təyinatlı host ƏS yoxdur. Nümunələr: VMware ESXi, Xen. İkinci tip hipervizor (type 2, hosted) əvvəlcədən işləyən ümumi təyinatlı host ƏS üzərində proqram kimi yerləşir; nümunələr: VirtualBox, VMware Workstation. Burada qonağa xidmət yolu host ƏS-in sürücülərindən və xidmətlərindən də asılıdır.

:::figure
src = "m13-1.png"
alt = "Sol tərəfdə birinci tip: fiziki avadanlıq, üstündə hipervizor (ESXi, Hyper-V, KVM), üstündə VM-lər. Sağda ikinci tip: fiziki avadanlıq, host əməliyyat sistemi, hipervizor (VirtualBox, Workstation), VM-lər."
caption = "Birinci və ikinci tip hipervizorların məntiqi qatları."
:::

Üç dəqiqləşdirmə:

- Birinci tip üçün ayrıca idarəetmə kompüteri **məcburi deyil**. Konsol başqa serverdə, ayrıca VM-də və ya məhsulun öz vasitələri ilə işləyə bilər; idarəetməni ayrı etibar zonasına çıxarmaq təhlükəsizlik seçimidir. Hipervizoru mütləq mikronüvə saymaq da düzgün deyil.
- **Hyper-V** birinci tipdir: hipervizor avadanlığın üzərindədir, Windows isə idarəedici kök bölmədə işləyir. Windows mühiti görünməsi onu ikinci tip etmir.
- **KVM** Linux nüvəsinə virtuallaşdırma funksiyası əlavə edir və birinci tip kimi təsnif olunur; **QEMU** kimi istifadəçi məkanı komponentləri virtual qurğuların təqdimatını tamamlayır. **Proxmox VE** KVM və konteynerləri idarə edən platformadır, ayrıca hipervizor mexanizmi deyil. Ekranda adi ƏS görünməsi təsnifat üçün kifayət etmir.

| Meyar | Birinci tip | İkinci tip |
| --- | --- | --- |
| Yerləşmə | Nəzarət avadanlıq üzərindədir | Ümumi təyinatlı host ƏS üzərində |
| Asılılıqlar | Hipervizor, sürücülər, idarəetmə bölmələri | Bunlara host ƏS və xidmətləri əlavə olunur |
| Tipik istifadə | Server klasteri, istehsalat, VDI | Fərdi laboratoriya, test, tədris |
| Performans | Sazlamadan və yükdən asılıdır | Aparat dəstəyi ilə yüksək ola bilər |
| Təhlükəsizlik qərarı | İdarəetmə və yamaqlar ayrıca qiymətləndirilir | Host ƏS-in qorunması da tələb olunur |

:::exam Tələ: "birinci tip təhlükəsiz, ikinci tip zəifdir"
Birinci tip avtomatik təhlükəsiz, ikinci tip avtomatik zəif deyil. İnternetə açılmış, yamanmamış ESXi idarəetməsi tələbənin yenilənmiş və ayrılmış laboratoriya noutbukundan daha böyük risk ola bilər. Müqayisə hücum səthinə, idarəetmə hüquqlarına və nasazlığın təsir dairəsinə əsaslanır. Performans üçün də mütləq hökm yoxdur: disk növü və yaddaş çatışmazlığı tip fərqindən çox gecikmə yarada bilər. (Konspektin "Tip 1 yüksək, Tip 2 aşağı performans, kiçik/böyük hücum səthi" cədvəli sadələşdirmədir; mühazirəyə görə hər ikisi şərtlidir.)
:::

### Virtual iş masası infrastrukturu

Virtual iş masası infrastrukturu (virtual desktop infrastructure, VDI) istifadəçinin iş masasını məlumat mərkəzindəki VM-də saxlayır; istifadəçi son qurğudan uzaq görüntü protokolu ilə qoşulur. Bağlantı brokeri autentifikasiyadan sonra uyğun iş masasını seçib sessiyanı yönəldir. **Davamlı** iş masasında dəyişikliklər qalır; **davamlı olmayan** hovuzda sessiya bitəndən sonra maşın təmiz şablondan yenidən yaradıla bilər.

Statistik proqramlar VDI hovuzunda saxlanıla bilər, tələbə evdən qoşulur. Ekran görüntüsünün çəkilməsi və giriş hesabının oğurlanması riski qalır; bufer, lokal disk və USB yönləndirilməsi məhdudlaşdırılır, layihələrin saxlanacağı yer əvvəlcədən müəyyən edilir. Sessiya kəsiləndə saxlanmamış iş itə bilər: sessiyanın bərpası ilə tətbiqin məlumat saxlaması ayrıca yoxlanır.

## Virtuallaşdırma üsulları və prosessorun imtiyazları

### Tam virtuallaşdırma və emulyasiya

Tam virtuallaşdırma (full virtualization) qonaq ƏS-ə işləmək üçün yetərli virtual aparat interfeysi verir; qonağın xüsusi dəyişdirilməsi tələb olunmur. Tarixi proqram yanaşmalarında imtiyazlı əməliyyatlar tutulub hipervizora ötürülür, problemli təlimatlar ikili çevirmə (binary translation) ilə dəyişdirilirdi. Aparat dəstəyindən istifadə edən sistem də tam virtuallaşdırma təqdim edə bilər: **tam virtuallaşdırma ilə aparat dəstəyi bir-birini istisna etmir**.

Emulyasiya (emulation) başqa maşının davranışını proqramla təqlid edir. QEMU fərqli arxitekturanın təlimatlarını proqramla icra edə bilir; uyğun aparat və KVM ilə isə qonağın çox təlimatını birbaşa prosessorda işlədir. x86 tətbiqini x86 VM-də işlətmək ilə onu fərqli arxitekturada emulyasiya etmək eyni performans modelinə malik deyil: emulyasiya uyğunluğu genişləndirir, təlimat çevrilməsi isə əlavə xərc yaradır.

### Paravirtuallaşdırma

Paravirtuallaşdırmada (paravirtualization) qonaq mühitin virtual olduğunu nəzərə alan interfeysdən istifadə edir və xüsusi çağırışla (hypercall) hipervizordan əməliyyat istəyir. Tam paravirtual qonaqda ƏS-in uyğunlaşdırılması tələb oluna bilər. Paravirtual **sürücülər** isə tam virtual maşında da işləyə bilər: məsələn, Linux VM-də virtio disk və şəbəkə sürücüləri qurğunun mürəkkəb fiziki modelini təqlid etmək əvəzinə sadələşdirilmiş qarşılıqlı əlaqə qurur.

LMS faylları üçün disk əməliyyatları çoxdursa, paravirtual sürücü CPU xərcini azalda bilər. Sürücü qonaqda yoxdursa, sistem açılış diskini görməyə bilər. Disk nəzarətçisini dəyişməzdən əvvəl sürücü quraşdırılır, geri qayıtma yolu hazırlanır, sınaq VM-i üzərində açılış yoxlanır. Paravirtuallaşdırma sürət vasitəsidir; sürücünün və hipervizorun təhlükəsizliyi ayrıca qorunur.

### Intel VT-x, AMD-V və halqalar

x86-da imtiyaz halqaları (protection rings) əməliyyatların səlahiyyət səviyyəsini ayırır. Adətən tətbiq ring 3-də, ƏS nüvəsi ring 0-da işləyir; ring 1 və 2 mövcuddur, amma ümumi təyinatlı sistemlər onları çox vaxt işlətmir. Nüvə avadanlığa ən geniş əmrləri verə bildiyindən, bir neçə nüvəni eyni maşında təhlükəsiz işlətmək üçün əlavə nəzarət gərəkdir.

Intel VT-x və AMD-V prosessora qonaq icrasını nəzarətdə saxlamaq imkanları əlavə edir. Intel terminologiyasında VMX root və VMX non-root rejimləri var. Bu rejimlər ring nömrəsinin davamı deyil: qonaq nüvəsi non-root rejimdə ring 0-da işləyə bilər. Bəzi mətnlər hipervizoru şərti olaraq **ring −1** adlandırır; bu, x86-nın rəsmi halqa nömrəsi deyil. AMD uyğun nəzarəti öz SVM mexanizmləri ilə qurur.

Qonaq adi hesablamaları birbaşa prosessorda icra edir. Nəzarət tələb edən hadisədə VM çıxışı (VM exit) baş verir, idarə hipervizora keçir; hipervizor əməliyyatı yoxlayır, virtual nəticəni hazırlayır və qonağı davam etdirir. "Hər təlimat proqramla təqlid edilir" təsviri düzgün deyil (köhnə təsvirdir). LMS-də hesablamanın çoxu birbaşa CPU-da getsə də, virtual qurğu ilə tez-tez qarşılıqlı əlaqə əlavə keçidlər yaradır.

| Anlayış | Cavab verdiyi sual | Məhdudiyyət |
| --- | --- | --- |
| Tam virtuallaşdırma | Qonağa tam maşın interfeysi verilirmi? | Arxitektura və virtual qurğu uyğunluğu qalır |
| Paravirtuallaşdırma | Qonaq hipervizor interfeysini tanıyırmı? | Uyğun nüvə və ya sürücü tələb oluna bilər |
| Aparat dəstəyi | Prosessor qonaq nəzarətini necə asanlaşdırır? | Firmware sazlaması və proqram dəstəyi lazımdır |
| Emulyasiya | Başqa aparatın davranışı necə təqlid edilir? | Təlimat çevirməsi performansı məhdudlaşdıra bilər |

Intel VT-d və AMD-Vi (giriş-çıxış yaddaş idarəetməsi) VT-x və AMD-V ilə eyni funksiya deyil. IOMMU qurğuların birbaşa yaddaş girişini məhdudlaşdırmaq üçün ünvan çevirməsi edir. GPU hesablama VM-inə birbaşa verilirsə, IOMMU qrupları və qurğu ayrılması yoxlanır; prosessor virtuallaşdırmasının açıq olması qurğunun təhlükəsiz ötürülməsini həll etmir. İç-içə virtuallaşdırma (nested virtualization) VM daxilində başqa hipervizor işlətməyə imkan verir; dəstək, performans və hücum səthi ayrıca qiymətləndirilir.

## Virtual resursların işləmə qaydası

### vCPU və planlaşdırma

Virtual prosessor (virtual CPU, vCPU) qonağın gördüyü icra vahididir; hipervizor onun işini fiziki prosessorun məntiqi icra vahidlərinə planlaşdırır. Səkkiz vCPU vermək səkkiz fiziki nüvəni daimi və müstəsna ayırmaq deyil: bağlama və rezerv siyasəti yoxdursa, vahidlər zamanla başqa VM-lərlə bölüşülür. Eyni nüvədəki aparat axınları iki müstəqil nüvə qədər məhsuldarlıq vermir.

Resursların artıq təyini (overcommit) ayrılmış virtual resursların cəminin fiziki tutumu keçməsidir. Şərti nümunə: hostda SMT söndürülüb, 24 fiziki nüvə 24 məntiqi icra vahidi verir; dörd VM-in hərəsinə 8 vCPU ayrılıb, cəmi 32 vCPU. Bu qadağan deyil, amma bütün VM-lər eyni vaxtda CPU istəyəndə növbə yaranır. Qonaqda CPU istifadəsi aşağı görünsə də vCPU-nun gözləməsi böyük ola bilər; CPU ready və ya steal time göstəriciləri bunu araşdırmağa kömək edir.

Daha çox vCPU vermək həmişə çıxış yolu deyil: az axınlı tətbiqdə əlavə vCPU boş qalır, böyük VM-in planlaşdırılması çətinləşir. Əvvəl gecikmə, növbə, fiziki CPU istifadəsi və paralellik ölçülür. Üç idarəetmə vasitəsi: **rezerv (reservation)** resursun əlçatanlığını qoruyur, **limit (limit)** yuxarı həddi qoyur, **pay (share)** rəqabətdə üstünlüyü müəyyən edir. Hər birinin mənası platformada yoxlanır.

### Operativ yaddaş və ünvan çevirməsi

Qonaqdakı proses virtual ünvan görür; qonaq ƏS bunu qonağın fiziki ünvanına çevirir, hipervizor onu hostun fiziki yaddaşı ilə əlaqələndirir. Intel EPT və AMD NPT (ikinci səviyyəli səhifə cədvəli) bu çevirməni aparatla sürətləndirir. Bu xəritə düzgün qorunmasa, bir VM başqasının məlumatını oxuya bilər.

Dinamik geri almada balloon sürücüsü qonaq daxilində səhifələr ayırıb saxlayır; hipervizor həmin səhifələrin fiziki yaddaşını geri alıb başqa VM-lərə verə bilir. Tətbiqin iş yükü azalmır: qonaqda istifadə olunan yaddaş azalır, keş boşalır və ya səhifələr diskə çıxarılır. Disk RAM-dan ləng olduğundan nəticə uzun fasilələrdir. İmtahan bazasında yaddaşın həddən artıq təyini CPU-dan daha sərt problem yarada bilər: keş səhifələri diskə dəyişəndə hər sorğu gecikir.

Şərti hesab: hostun 128 GiB RAM-ından hipervizora 16 GiB ayrılır, VM-lərə 112 GiB qalır. Dörd VM-in hərəsinə 24 GiB verilsə cəmi 96 GiB təyin olunur, 16 GiB ehtiyat qalır. Bu hesab real işçi dəstini ölçmür, yalnız tutum sərhədidir. NUMA quruluşunda yaddaşın prosessora yaxınlığı gecikməyə təsir edir; çox böyük VM ayrı NUMA düyünlərinə yayılarsa uzaq yaddaş müraciətləri artar.

### Disklər və saxlama hovuzu

Virtual disk qonağa blok qurğusu kimi görünür; arxada fayl, məntiqi həcm və ya xüsusi saxlama sistemi ola bilər. Bir neçə host eyni hovuza şəbəkə ilə çata bilər (NFS, iSCSI). Saxlama şəbəkəsinin gecikməsi qonaqda disk gecikməsi kimi görünür, ona görə ləng bazanı yalnız qonaq ƏS-dən araşdırmaq kifayət etmir.

Qalın ayrılmada (thick provisioning) həcm əvvəlcədən rezerv edilir (sıfırlama davranışı məhsuldan asılıdır). Nazik ayrılmada (thin provisioning) fiziki yer yazıldıqca tutulur. Şərti hovuz 500 GiB-dir, dörd VM-ə hərəsinə 200 GiB görünən disk verilib: görünən cəm 800 GiB, faktiki istifadə 300 GiB ola bilər. Boş görünən qonaq diskləri hovuzun dolmayacağına zəmanət vermir; snapshot və ehtiyat nüsxə üçün də yer lazımdır.

| Resurs | Şübhə yaradan əlamət | Yoxlanacaq göstərici | İlkin addım |
| --- | --- | --- | --- |
| CPU | İmtahan səhifəsi fasilələrlə açılır | İcra gözləməsi, host yükü | Yüklərin eyni vaxta düşməsini yoxlamaq |
| RAM | Baza sorğuları birdən ləngiyir | Balloon, swap, işçi dəst | Yaddaş rezervini və real tələbi ölçmək |
| Disk | Yazı əməliyyatları gözləyir | Gecikmə, növbə, boş yer | Hovuz və snapshot artımını yoxlamaq |
| Şəbəkə | Paket itkisi, dəyişən sürət | Port sayğacları, uplink yükü | VM-dən fiziki porta qədər yolu izləmək |

RAID disk nasazlığına dözümlülük verə bilər, amma silinmiş faylı və ya şifrələnmiş bazanı geri qaytarmır; replikasiya və ehtiyat nüsxə ayrıca mexanizmlərdir. Massivdə həm əsas VM diskləri, həm bütün ehtiyat nüsxələr saxlanırsa, massivə çıxış əldə edən hücumçu hər ikisini poza bilər. Məntiqi həcm ayrılması ayrıca təhlükəsizlik sərhədi yaratmaya bilər.

### Verilənlərin vahid görünüşü

Verilənlərin virtuallaşdırılmasında (data virtualization) vasitəçi qat sorğunu uyğun mənbələrə yönəldir və nəticəni vahid məntiqi görünüşdə təqdim edir. Kitabxana borcu, fakültə və qeydiyyat statusu ayrı sistemlərdədirsə, hesabat xidməti onları vahid sorğu ilə bağlaya bilər. Məlumatı daimi bir bazaya köçürmək məcburi deyil; keş və aralıq nəticələr saxlanıla bilər, bu qatın nə saxladığı sənədləşdirilir.

Əsas təhlükəsizlik məsələsi **səlahiyyətlərin uyğunlaşdırılmasıdır**: kitabxana işçisinin borcu görməsi bütün akademik qeydləri oxumasına əsas vermir; mənbədəki sətir və sütun məhdudiyyətləri vahid görünüşdə də qorunmalıdır. Ayrı bazalar eyni anın vəziyyətini qaytarmaya bilər (zaman uyğunsuzluğu). Hesabat xidməti mənbənin icazələrini geniş hesabla keçirsə, rahat sorğu interfeysi məxfilik pozuntusuna çevrilir.

:::note Köhnə slaydlarla fərq: yaddaş sözü
Slayddakı "virtual yaddaş fiziki disklərdən və RAID-dən abstraksiyadır" cümləsində söhbət yaddaş qurğularının virtuallaşdırılmasından (storage virtualization) gedir, ƏS-dəki "virtual yaddaş" anlayışından yox. "Verilənlər bazası" bəndi isə verilənlərin virtuallaşdırılmasıdır (data virtualization).
:::

## Virtual şəbəkələr və trafik sərhədləri

### vSwitch üzərindən paket necə keçir

Virtual şəbəkə interfeysi (virtual network interface card, vNIC) VM-i virtual kommutatora (virtual switch, vSwitch) bağlayır. vSwitch portlar arasında Ethernet çərçivələri ötürür; fiziki şəbəkəyə çıxış uplink ilə olur. Eyni hostda, eyni məntiqi seqmentdəki iki VM arasında trafik fiziki kommutatora çıxmadan ötürülə bilər, buna görə yalnız fiziki uplink üzərindəki IDS və firewall onu görmür. Sensorun yeri real paket yoluna uyğun seçilməlidir; hostdakı şərq–qərb trafikini görmək üçün virtual firewall, mikroseqmentasiya (məsələn VMware NSX) və ya hostda sensor lazımdır.

Şərti topologiya: LMS tətbiqi 10.20.0.10 (VLAN 20), bazası 10.30.0.20 (VLAN 30). Sorğu VLAN-lar arasında firewall və ya nəzarət olunan marşrutlaşdırıcıdan keçir; hər iki VM eyni hostda olsa da bu məntiqi keçid qalır. Eyni VLAN daxilindəki VM-ləri ayırmaq üçün ayrıca paylanmış firewall qaydası və ya başqa nəzarət lazımdır.

:::figure
src = "m13-2.png"
alt = "LMS VM (VLAN 20), Baza VM (VLAN 30), Admin VM (VLAN 10) vNIC ilə vSwitch-ə qoşulur; vSwitch uplink vasitəsilə fiziki kommutatora (trunk) çıxır; kommutator VLAN-lar arasında firewall ilə əlaqəlidir."
caption = "Virtual portlardan fiziki şəbəkəyə və VLAN-lar arasındakı firewall-a gedən yol."
:::

VLAN məntiqi Ethernet seqmentidir; IEEE 802.1Q etiketi çərçivənin hansı VLAN-a aid olduğunu göstərir. Access port adətən bir VLAN-ın etiketsiz trafikini, trunk icazəli VLAN-ların etiketli trafikini daşıyır. Etiketləmə yeri qonaq, port qrupu və ya fiziki port ola bilər; eyni paketi iki dəfə etiketləmək və ya gözlənilən etiketi silmək əlaqəni poza bilər. **VLAN şifrələmə deyil**; VLAN-lar arasında qaydasız marşrutlaşdırma varsa, adların fərqli olması trafiki qorumur.

| VLAN | Alt şəbəkə | Təyinat | İcazə prinsipi |
| --- | --- | --- | --- |
| 10 | 10.10.10.0/24 | Hipervizor idarəetməsi | Yalnız idarə olunan admin keçidindən |
| 20 | 10.20.0.0/24 | LMS tətbiqləri | Tərs proksidən tələb olunan bağlantılar |
| 30 | 10.30.0.0/24 | Tələbə və LMS bazaları | Yalnız uyğun tətbiq xidmətlərindən |
| 40 | 10.40.0.0/24 | Ehtiyat nüsxə infrastrukturu | Ayrı hesablarla məhdud axınlar |
| 50 | 10.50.0.0/24 | Tədris laboratoriyası | İnzibati zonalara standart qadağa |

### Bridged, NAT, host-only və daxili şəbəkə

Körpü rejimində (bridged) VM fiziki yerli şəbəkənin iştirakçısı olur və ayrıca IP ala bilər, şəbəkədə real kompüter kimi görünür. NAT rejimində VM çıxış trafikini ünvan çevirməsi ilə göndərir (host IP-si arxasında); xaricdən başlanan bağlantı üçün ayrıca yönləndirmə lazım ola bilər. NAT çıxan zərərli trafiki qadağan etmir: yataqxana Wi-Fi şəbəkəsindən NAT arxasındakı yoluxmuş VM internetdəki xidmətlərə hücum edə bilər.

Host-only şəbəkəsi hostu və seçilmiş VM-ləri birləşdirir; host hücum səthində qalır. Daxili şəbəkə (internal network) yalnız seçilmiş VM-lər arasında bağlantı qurur; host və fiziki uplink üzv olmur. Amma ayrı VM-də marşrutlaşdırma və ya ikinci interfeys açılarsa, daxili şəbəkədən də çıxış yarana bilər: rejimin adı seçildikdən sonra faktiki interfeyslər və marşrutlar yoxlanır.

| Rejim | Kimlə əlaqə | Əsas risk | Uyğun nümunə |
| --- | --- | --- | --- |
| Bridged | Fiziki seqmentdəki qurğularla | VM kampus şəbəkəsinə birbaşa çıxır | Nəzarət olunan test serveri |
| NAT | İcazəli çıxış, yönləndirilən giriş | Çıxış hücumları, məlumat sızması | Adi proqram laboratoriyası |
| Host-only | Host və həmin şəbəkədəki VM-lər | Hosta hücum, səhv marşrutlaşdırma | Hostla fayl ötürən ayrılmış laboratoriya |
| Daxili | Yalnız seçilmiş VM-lər | İkinci interfeys, hipervizor zəifliyi | Təcrid edilmiş zərərli proqram təhlili |

:::exam Konspektin təhlükəsizlik reytinqi
Bridged: zərərli proqram analizi üçün **təhlükəlidir** (VM universitet şəbəkəsinə çıxır). NAT: orta (İnternet çıxışı var). Host-only: host-a hücum riski qalır. Daxili şəbəkə: zərərli proqram laboratoriyası üçün **ən uyğunu**.
:::

### Şərq–qərb trafikinə nəzarət

Şərq–qərb trafiki (east-west traffic) xidmətlər və VM-lər arasındakı əlaqədir; şimal–cənub trafiki (north-south traffic) mühitə daxil olan və oradan çıxan əlaqələrdir. Mikroseqmentasiya (microsegmentation) qaydaları tətbiqin roluna qədər daraldır: LMS-in veb qatı yalnız tətbiq qatına, tətbiq qatı isə bazanın tələb etdiyi xidmətə çatır. Eyni VLAN-da yerləşmə avtomatik etibar səbəbi deyil.

Virtual portda mənbə MAC ünvanının dəyişməsi, saxta trafik ötürülməsi və promiscuous rejim üçün siyasət müəyyən edilir. Promiscuous rejim sensor üçün lazım ola bilər, adi tələbə VM-i üçün əsaslandırılmalıdır. Hər portda kor-koranə qadağa da həll deyil: bəzi şəbəkə cihazları və klaster həlləri xüsusi davranış tələb edir; istisna konkret VM-ə verilir, sahibi və səbəbi yazılır. Trafik güzgülənəndə paketlərdə tələbələrin şəxsi məlumatı ola bilər, ona görə sensor qeydlərinə giriş məhdudlaşdırılır.

## VM-in həyat dövrü və vəziyyətinin daşınması

### Şablon və klon

Şablon (template) təkrar VM yaratmaq üçün baza təsviridir. Klon (clone) mövcud təsvirin ayrıca VM kimi nüsxəsidir. **Tam klon** öz virtual diskinə malikdir; **əlaqəli klon** baza diskdən asılı olub fərqləri ayrıca saxlayır. Əlaqəli klon yerə qənaət edir, amma baza disk itərsə ondan asılı qonaqlar da işləməyə bilər.

Etibarlı şablonun mənbəyi, versiyası, yamaq tarixi və sahibi məlumdur. Şablonda tələbə bazasının real nüsxəsi, şəxsi SSH açarı və ya ümumi administrator parolu saxlanmır. İlk açılışda host adı, maşın kimliyi, SSH host açarları və xidmət sirləri fərdiləşdirilir; Windows üçün Sysprep, Linux-da cloud-init bunu avtomatlaşdıra bilər. Kimlik yenilənməsi domen üzvlüyünü və tətbiq qeydiyyatını da nəzərə almalıdır.

Şablon söndürülmüş vəziyyətdə də köhnəlir: altı ay sonrakı klon köhnə paketlərlə başlayır. Şablon ayrıca yamaq dövrünə daxil edilir, nəzarətli qurma prosesindən yenidən alınır və sınaqdan keçirilir. İstifadədən çıxmış VM-in silinməsi ilə disk nüsxələrinin, snapshot-ların və ehtiyat nüsxələrin saxlanma müddəti eyni qərar deyil; hər biri inventarda izlənir.

### Snapshot necə işləyir

Snapshot (snapshot) VM-in müəyyən andakı vəziyyətinə qayıtmaq üçün nöqtədir. Disk snapshot-ında sonrakı yazılar çox vaxt ayrıca **fərq qatına** yönəlir (bəzi saxlama sistemləri başqa mexanizm işlədir); oxuma zamanı dəyişmiş blok fərq qatından, qalanı baza diskdən alınır. Məhsul dəstəkləyirsə RAM və qurğu vəziyyəti də saxlanıla bilər; nələri əhatə etdiyi yoxlanır.

:::figure
src = "m13-3.png"
alt = "Baza disk, fərq qatı 1, fərq qatı 2 və cari yazılar zənciri; hər qat əvvəlkinə bağlıdır. Aşağıda ayrıca ehtiyat nüsxə sahəsi: başqa saxlanc və dəyişdirilə bilməyən nüsxə."
caption = "Snapshot-un baza diskdən asılılığı və ayrıca ehtiyat nüsxə sahəsi."
:::

LMS paketini yeniləməzdən əvvəl qısa müddətli snapshot geri qayıtmanı asanlaşdırır. Amma yeniləmədən sonra tələbələrin təqdim etdiyi işlər varsa, geriyə dönüş onları da silə bilər. Baza başqa VM-dədirsə, yalnız tətbiq VM-ini geri çevirmək versiya və məlumat uyğunsuzluğu yaradır; qərarda xidmətin bütün asılılıqları nəzərə alınır. Köhnə snapshot-a dönüş sızmış parolu yenidən aktiv edə və sertifikat vəziyyətini köhnəldə bilər.

Qəza uyğunluğu (crash consistency) diskin qəfil enerji kəsilməsinə bənzər vəziyyətdə tutulmasıdır. Tətbiq uyğunluğu (application consistency) üçün tətbiqin buferləri və tranzaksiyaları nəzərə alınır, uyğun dondurma və ya baza mexanizmi işlədilir. Windows VSS və Linux-da fayl sistemini müvəqqəti dondurma kömək edə bilər, amma fayl sisteminin uyğunluğu bazanın tranzaksiya uyğunluğuna bərabər deyil: baza üçün istehsalçının dəstəklədiyi ehtiyatlama üsulu seçilir.

Uzun snapshot zənciri əlavə disk müraciətləri və yer təzyiqi yaradır. Silinmə bəzi sistemlərdə fərq bloklarının birləşdirilməsini tələb edir, buna da vaxt və boş yer lazımdır. Hovuz dolanda ilk addım təsadüfi fayl silmək deyil: hansı zəncirin hansı VM-ə aid olduğu müəyyən edilir, platformanın birləşdirmə yolu seçilir. Snapshot faylını fayl menecerindən silmək VM-in bütövlüyünü poza bilər.

| Üsul | Nə saxlayır | Əsas istifadə | Məhdudiyyət |
| --- | --- | --- | --- |
| Snapshot | Müəyyən andakı vəziyyətə keçid məlumatı (eyni yaddaşda) | Qısa müddətli geri qayıtma | Baza diskdən və platformadan asılıdır; disk/host itsə snapshot da itir; uzun saxlansa performans düşür |
| Klon | VM-in ayrıca və ya bazadan asılı nüsxəsi | Test və tədris mühiti | Köhnə sirlər və kimliklər köçə bilər |
| Replikasiya | Başqa yerdə yenilənən davamlı surət | Dayanmadan sonra tez bərpa (RTO-nu azaldır) | Səhv və şifrələnmə də köçür (silinmiş/şifrələnmiş məlumatı dərhal surətləyir) |
| Ehtiyat nüsxə (backup) | Ayrı yerdə saxlanan müstəqil, idarə olunan nüsxə | Silinmə, ransomware, fəlakətdən bərpa | Ayrı giriş və bərpa sınağı tələb edir; bərpa testi edilməyibsə işləyəcəyi bilinmir |

:::tip Yadda saxla: snapshot ehtiyat nüsxə deyil
Snapshot ehtiyatlama proqramının iş axınında istifadə oluna bilər, amma eyni saxlama hovuzunda qalan snapshot müstəqil ehtiyat nüsxə sayılmaz. Disk və ya host itəndə snapshot da itir.
:::

:::exam Tələ: işləyən VM-in fayllarını kopyalamaq
"Tam ehtiyat nüsxə üçün sadəcə faylları kopyalamaq kifayətdir" yanlışdır. İşləyən VM-in fayllarını adi kopyalama əmri ilə götürmək uyğunsuz (corrupted) nüsxə verə bilər: bloklar kopyalanarkən dəyişir. Ya VM nəzarətlə söndürülür, ya da hipervizorun/platformanın ehtiyatlama interfeysi işlədilir.
:::

### İşlək VM-in köçürülməsi

İşlək köçürmə (live migration) VM-in icra vəziyyətini bir hostdan digərinə ötürür. Tipik əvvəlcədən köçürmə (pre-copy) üsulu:

:::steps Pre-copy live migration
[[step]]
title = "İlkin surət"
body = "Yaddaşın ilkin surəti hədəf hosta ötürülür, VM işləməyə davam edir."

[[step]]
title = "Dəyişmiş səhifələr"
body = "İşləmə zamanı dəyişmiş yaddaş səhifələri təkrar göndərilir."

[[step]]
title = "Qısa dayandırma"
body = "Sonda qısa dayandırma ilə qalan vəziyyət ötürülür."

[[step]]
title = "Hədəfdə davam"
body = "Qonaq hədəf hostda işini davam etdirir."
:::

Saxlama ortaq deyilsə disk də uyğun üsulla daşınır; hostların prosessor və virtual qurğu uyğunluğu yoxlanır. İmtahan vaxtı LMS yaddaş səhifələrini çox sürətlə dəyişirsə, köçürmə uzun çəkə bilər: dəyişmə sürəti ayrılmış şəbəkə ötürməsinə yaxınlaşanda təkrar nüsxələmə çətinləşir. Bəzi sistemlər başqa alqoritmlər təklif edir, amma fasiləsizliyin dərəcəsi məhsul və yükdən asılıdır. **Live migration sıfır fasilə zəmanəti deyil**; host artıq sıradan çıxıbsa, oradakı RAM vəziyyətini köçürə bilməz.

Köçürmə kanalında bazanın açıq yaddaşı və açarlar ola bilər: kanal ayrılır, tərəflər autentifikasiya olunur, dəstəklənən şifrələmə aktiv edilir (VM şifrələnsə də kanalın avtomatik şifrələndiyi qəbul edilmir). Hədəf hostda əvvəlki VLAN, firewall və saxlama siyasətləri qorunmalıdır; əks halda texniki uğurlu köçürmə əlçatmazlıq və ya daha açıq şəbəkə mövqeyi ilə bitir.

## Klaster, yüksək əlçatanlıq və bərpa

Klaster bir neçə hostun əlaqələndirilmiş idarəsidir; resurs hovuzu yerləşdirməni, yük balansını və bəzi nasazlıqlardan bərpanı asanlaşdırır. Yüksək əlçatanlıq (high availability, HA) host nasazlığından sonra VM-i başqa hostda yenidən başlada bilər. Qonaq ƏS və tətbiq təkrar açıldığından fasilə qalır, RAM-dakı saxlanmamış məlumat itə bilər. Replikası olan tətbiq və ya xüsusi nasazlığa dözümlülük mexanizmi daha az fasilə verə bilər, amma ayrıca qurulur.

### Ehtiyat tutum və ortaq nasazlıq sahəsi

Şərti klaster: üç host, hərəsində 128 GiB RAM-dan 16 GiB platformaya ayrılıb; VM-lərə ümumi tutum 3 × 112 = 336 GiB. Tələbat 240 GiB olarsa normalda yer çatır. Bir host itəndə qalan tutum 224 GiB olur: 16 GiB çatışmır. Klasterin mövcudluğu bu hesabı dəyişmir. N+1 planında bir host itəndən sonra kritik yükün qalan hostlara sığması əvvəlcədən yoxlanır; CPU, disk və şəbəkə də hesablanır.

LMS-in iki replikası eyni hostdadırsa, host nasazlığı hər ikisini dayandırır; ayrı hostlarda saxlamaq üçün ayırma qaydaları (anti-affinity) verilir. İki host eyni elektrik xəttinə, kommutatora və massivə bağlıdırsa, ortaq risk qalır. Kvorum və nasaz düyünün yazma hüququnu kəsən fencing mexanizmi parçalanmış qrupların eyni məlumatı zidd şəkildə dəyişməsinin qarşısını almağa kömək edir; bu parametrlər təxminlə dəyişdirilmir.

Yük azalanda VM-ləri az hostda toplamaq enerji qənaəti verir, amma söndürülmüş hostu açmaq vaxt aparır və ehtiyat tutum azalır; gecə ehtiyatlaması, səhər VDI giriş dalğası və texniki xidmət nəzərə alınır, siyasət qəza bərpası ilə birlikdə sınanır.

### RTO, RPO və bərpa sınağı

Bərpa vaxtı hədəfi (recovery time objective, RTO) xidmətin hansı müddətdə qaytarılmalı olduğunu, bərpa nöqtəsi hədəfi (recovery point objective, RPO) nə qədər son məlumatın itirilməsinin qəbul edildiyini göstərir. Şərti: tələbə bazasının RPO-su 15 dəqiqə, RTO-su 1 saatdırsa, gecəlik nüsxə birinci hədəfə uyğun gəlmir; tranzaksiya jurnallarının tez saxlanması və ya replikasiya lazımdır. RTO-ya VM-in açılması ilə yanaşı bazanın yoxlanması və istifadəçi girişinin bərpası da daxildir.

| Xidmət | RPO | RTO | Yoxlanacaq nəticə |
| --- | --- | --- | --- |
| Tələbə bazası | 15 dəqiqə | 1 saat | Son tranzaksiyalar və tətbiq bağlantısı |
| LMS materialları | 4 saat | 2 saat | Fayllar, icazələr, kursların açılması |
| Kafedra saytı | 24 saat | 8 saat | Məzmun, sertifikat, domen sazlaması |
| Tədris VM-ləri | Şablondan başlanma | 1 iş günü | Fərdi kimlik və laboratoriya şəbəkəsi |

3-2-1 qaydası: **3** nüsxə, **2** fərqli daşıyıcı növündə, **1** nüsxə başqa yerdə; ransomware riskinə görə ən azı biri oflayn və ya dəyişdirilməsi məhdud (immutable). Ehtiyatlama hesabı hipervizor administratoru ilə eyni geniş hüquqlu hesab olmamalıdır. Şifrələnmiş nüsxənin açarı itərsə nüsxənin sağlamlığı kifayət etmir: açarların bərpası da sınağa daxildir.

Bərpa testi istehsalatdan ayrılmış şəbəkədə aparılır: köhnə bazanı eyni IP və domen kimliyi ilə kampus şəbəkəsinə qoşmaq ünvan toqquşması və yanlış məktub göndərişi yaradır. Əvvəl nüsxənin bütövlüyü, sonra xidmətin funksiyası yoxlanır: şərti tələbə hesabı ilə giriş, fənn məlumatının oxunması, icazəsiz sorğunun rədd edilməsi. Yalnız VM-in açıldığına baxmaq xidmətin bərpasını göstərmir.

:::exam Tələ: HA, güzgü, "10%" və "50–60%"
HA resurs yaratmır, mövcud resursda yenidən başlanmanı idarə edir; "güzgü nüsxəsi" təkbaşına fasiləsizlik vermir, HA və ya replikasiya ayrıca sazlanmalıdır. "Serverlərin orta yükü 10%-dən çox deyil", "xərclər 50–60% azalır" rəqəmlərinin mənbəyi və ili göstərilməyib: universal fakt kimi əzbərlənməz.
:::

## Konteynerlər və tətbiqlərin idarəsi

### Konteynerin VM-dən fərqi

Konteyner (container) tətbiqi və asılılıqlarını ayrılmış proses mühitində işlədir. Adi Linux konteynerləri host nüvəsini **paylaşır**, hərəsinin ayrıca qonaq nüvəsi yoxdur; VM isə öz ƏS nüvəsinə malikdir. Konteyner təsvirində (image) tətbiq, kitabxanalar və fayl sistemi qatları saxlanır; işləyən konteyner ona icra vəziyyəti və adətən yazılan qat əlavə edir. Davamlı məlumat konteynerin ömründən asılı olmasın deyə ayrıca həcmdə (volume) saxlanır.

Kitabxananın axtarış tətbiqi konteynerdə yenidən başlaya bilər, amma tələbə sifarişləri ayrıca bazada qalmalıdır; fayllar yalnız yazılan qatda saxlansa, konteyner dəyişdiriləndə itir. Konteyner tez başlayır və az resurs istəyir, amma böyük təsvirin endirilməsi, tətbiqin başlanması və bazaya bağlantı vaxt aparır: sürətli proses başlanması xidmətin dərhal hazır olması demək deyil.

:::figure
src = "m13-4.png"
alt = "Solda iki VM: hər birində tətbiq və ayrıca qonaq nüvəsi, altında hipervizor və avadanlıq. Sağda üç konteyner ortaq host nüvəsi (namespaces, cgroups) üzərində, altında avadanlıq."
caption = "Ayrı qonaq nüvələri olan VM-lər və host nüvəsini paylaşan konteynerlər."
:::

Linux konteynerini Linux nüvəsi işlədir. Windows və ya macOS-da Linux konteyner alətləri çox vaxt arada Linux VM işlədir, ona görə eyni konteynerin istənilən nüvədə dəyişmədən işləyəcəyi qəbul edilmir. Konteynerlər VM daxilində də yerləşə bilər: universitet müxtəlif etibar səviyyəli fakültələri ayrı VM-lərdə, hər fakültənin xidmətlərini həmin VM-də konteynerlərdə ayıra bilər.

| Meyar | Virtual maşın | Adi Linux konteyneri |
| --- | --- | --- |
| Nüvə | Hər qonağın öz nüvəsi | Host nüvəsi paylaşılır |
| Ayırma sərhədi | Virtual aparat və hipervizor | Nüvə mexanizmləri və icra mühiti |
| Paketləmə | ƏS, tətbiqlər, virtual disklər | Tətbiq və istifadəçi məkanı asılılıqları |
| Yeniləmə | Qonaq və hipervizor ayrıca yamanır | Təsvir yenidən qurulur, host da yamanır |
| Tədris istifadəsi | Fərqli ƏS və nüvə sınaqları | Eyni nüvə ailəsində tətbiq laboratoriyası |
| Qalıq risk | Escape, ortaq host, resurs rəqabəti | Ortaq nüvə zəifliyi, geniş səlahiyyətlər |

:::note Sadə dillə
VM avadanlığı, konteyner əməliyyat sistemini virtuallaşdırır. VM-də güclü izolyasiya, amma ağırdır; konteyner yüngüldür və saniyələrlə başlayır, amma nüvə ortaqdır, nüvə zəifliyi bütün konteynerlərə təsir edə bilər.
:::

### Namespaces və cgroups

Linux ad fəzası (namespace) prosesə resursların ayrılmış görünüşünü verir: PID ad fəzasında proseslər ayrı nömrələnir, mount ad fəzasında qoşulmuş fayl sistemləri, network ad fəzasında interfeyslər və marşrutlar fərqlənir. User ad fəzası konteynerdəki istifadəçi identifikatorunu hostda başqa identifikatora xəritələyə bilər; imkanın mövcudluğu onun konkret mühitdə aktiv olduğu demək deyil.

Nəzarət qrupları (control groups, cgroups) proseslərin CPU, yaddaş və digər resurs istifadəsini hesablayır və məhdudlaşdırır. **Namespace görünüşü ayırır, cgroups resurs istifadəsinə nəzarət edir**; heç biri təkbaşına bütün təhlükəsizliyi həll etmir. Şəbəkə ad fəzasındakı konteynerin başqa konteynerə çıxışı marşrut və firewall qaydası ilə açıq qala bilər. Kubernetes ad fəzası isə Linux network namespace-dən fərqli olaraq API obyektlərini məntiqi qruplaşdırır.

Tələbə kodunu işlədən xidmətdə yaddaş limiti yoxdursa, bir proqram digər konteynerlərin yaddaşını tükədə bilər; limit varsa, limiti aşan proses dayandırıla bilər və tətbiq bunu düzgün emal etməlidir. Etibarsız tələbə kodunu adi konteynerə qoyub tam təcrid saymaq olmaz: riskdən asılı olaraq ayrıca VM, daha sərt icra mühiti, çıxış məhdudiyyəti və birdəfəlik işçi düyün seçilir.

:::exam Tələ: namespace şəbəkəni ayırmır
Namespace təkbaşına şəbəkəni ayırmır; NetworkPolicy lazımdır. Konspektdə konteynerə xas risklər: imicdə köhnə/zəif paketlər və naməlum mənbədən imic; `--privileged` rejimi, host qovluqlarının qoşulması, root kimi işləmə; imicə yazılmış parollar və API açarları.
:::

### Docker və Kubernetes-in əsasları

Docker təsvirin qurulması, saxlanması və konteynerin başladılması üçün alətlər verir. Reyestr (registry) təsvirləri saxlayır; etiket (tag) ada bənzər göstəricidir və başqa təsvirə keçirilə bilər. Məzmun heşi ilə digest konkret təsviri müəyyən edir; heş bütövlüyü yoxlamağa kömək edir, amma etibarlı müəllifdən gəldiyini sübut etmir: mənbə və imza siyasəti ayrıca yoxlanır. Dockerfile təsvirin necə qurulduğunu təsvir edir, özü işləyən konteyner deyil.

Kubernetes konteynerləşdirilmiş tətbiqlərin yerləşdirilməsini və istənən vəziyyətini idarə edir.

| Komponent | Rolu |
| --- | --- |
| Pod | Ən kiçik yerləşdirmə vahidi; bir və ya bir neçə konteyner, ortaq şəbəkə mühiti və bəzi ortaq həcmlər |
| Deployment | Nəzarətçi: replika sayını və yenilənməni idarə edir |
| Service | Dəyişən Pod ünvanlarının qarşısında sabit xidmət görünüşü |
| Ingress | Xaricdən HTTP trafikinə yol (uyğun nəzarətçi tələb olunur) |
| API server | İdarəetmə müstəvisində sorğuları qəbul edir |
| Planlaşdırıcı | Pod üçün düyün seçir |
| Nəzarətçilər | Faktiki vəziyyəti istənənlə tutuşdurur |
| etcd | Klasterin vəziyyətini saxlayır |
| kubelet və icra mühiti (runtime) | İşçi düyündə Pod-ların işləməsini təşkil edir |

Kubernetes hipervizor deyil və hər Pod üçün ayrıca VM yaratmır; idarəetmə API-sinə geniş hüquq qazanan hesab bütün tətbiqlərə təsir edir. LMS-in üç replikası istənilsə, Pod dayananda nəzarətçi əvəzini yaradır; amma bütün replikalar eyni fiziki hostdakı düyünlərdədirsə, host nasazlığı yenə ümumi dayanmadır. Readiness yoxlaması trafik qəbul etməyə hazırlığı, liveness yoxlaması yenidən başlatma ehtiyacını qiymətləndirir; yanlış liveness yoxlaması bazanın müvəqqəti ləngiməsində bütün tətbiqləri ardıcıl yenidən başladıb vəziyyəti ağırlaşdıra bilər.

## Təhdidlər və məlum zəifliklər

### Etibar sərhədinin keçilməsi

VM-dən çıxış (VM escape) qonaqdakı kodun nəzərdə tutulan sərhədi keçib host və ya hipervizor kontekstində icra qazanmasıdır. Yol virtual qurğu modelindəki yaddaş xətasından, ortaq inteqrasiya xidmətindən və ya başqa zəiflikdən keçə bilər. Qonaq daxilində administrator olmaq host administratoru olmaq deyil; escape məhz bu sərhədin pozulmasıdır.

**İdarəetmə hesabının oğurlanması** başqa yoldur: hücumçu paneldə qanuni səlahiyyətlərlə VM konsolunu aça, disk qoşa, snapshot çıxara və VM-ləri silə bilər; escape zəifliyi lazım deyil. Yalnız qonaqlardakı antivirusu izləyən universitet hipervizor səviyyəsində disk şifrələnməsini və ya ixracını gec görər: idarəetmə əməliyyatlarının ayrıca auditi tələb olunur.

Hipervizorun ələ keçirilməsi və ya gizli zərərli hipervizorun yerləşdirilməsi **hyperjacking** adlanır; VM daxilindəki adi zərərli proqramdan fərqlidir. Hücumçu daha aşağı etibar qatında qonaqların gördüyü vəziyyəti idarə edə bilər. Təsdiqsiz açılış komponenti aşkarlanarsa, tək VM-i yenidən qurmaq kifayət deyil: firmware, açılış zənciri və hipervizorun etibarlı mənbədən yenidən qurulması qiymətləndirilir.

| Təhdid | Pozulan sərhəd | Universitet nümunəsi | İlkin müdafiə |
| --- | --- | --- | --- |
| VM escape | Qonaqdan hosta keçid | Tədris VM-indən hipervizor prosesinə çıxış | Yamaqlar, lazımsız qurğuların (USB, ortaq qovluq, bufer) çıxarılması |
| İdarəetmənin ələ keçirilməsi (management plane) | Admin hesabı və API | Oğurlanmış hesabla baza diskinin ixracı; ESXi-yə qarşı ransomware | Ayrıca VLAN, MFA, RBAC, auditlənən giriş, İnternetdən əlçatmazlıq |
| VM sprawl | Aktivlərin nəzarəti | Sahibi olmayan köhnə kafedra VM-i | İnventar, sahib və son istifadə tarixi, avtomatik təmizləmə |
| Köhnə imic və şablonlar | Təsvirin etibarı | Aylarla yenilənməyən, içində parol olan şablon; hər klon eyni zəifliyi daşıyır | Gücləndirilmiş, müntəzəm yenilənən şablon; sirlər imicdən çıxarılır |
| Snapshot sızması | Disk və yaddaş məxfiliyi | İmtahan bazasının RAM nüsxəsinin oğurlanması | Giriş məhdudiyyəti və şifrələmə |
| Resurs rəqabəti | Əlçatanlıq | Tələbə işi bütün disk növbəsini tutur (DoS) | Limit, rezerv, yerləşdirmə siyasəti |
| Yan kanal | Paylaşılan mikroarxitektura (ortaq CPU keşi) | Qonşu yükdən məxfi məlumat çıxarma | Mikrokod və hipervizor yamaqları, kritik VM-lərin ayrılması |
| Ortaq nasazlıq sahəsi | Əlçatanlıq | Bir host çökür, üzərindəki bütün VM-lər dayanır | HA klaster, kritik VM-ləri fərqli hostlara yaymaq, ehtiyat tutum |

### Nəzarətsiz artım, sızma və qonşu yük

VM-lərin nəzarətsiz artması (VM sprawl) yaratmanın silmə və uçotdan asan olmasından yaranır: sınaq üçün açılan VM unudulur, yamaq almır, köhnə hesab saxlayır. Söndürülmüş VM də diskində məlumat saxlayır və sonradan köhnə vəziyyətdə açıla bilər. İnventarda sahibi, məqsədi, məlumat sinfi və son istifadə tarixi olur; silmə qərarı ehtiyat nüsxə və qanuni saxlanma tələblərini nəzərə alır.

Snapshot sızmasında tətbiqin normal avtorizasiya yoxlaması keçilmir, çünki hücumçu artıq disk və ya RAM surətini alır. Yaddaş nüsxəsində sessiya nişanları və kriptoqrafik açarlar qala bilər; şifrəli diskdəki məlumat işləmə zamanı açıldığından RAM snapshot-ı ayrıca qorunur. Açar eyni əlçatan qovluqda saxlanırsa, fayl şifrələməsinin faydası azalır.

Səs-küylü qonşu (noisy neighbour) eyni hostdakı yükün ortaq resursları sıxışdırmasıdır; qəsdən DoS və ya adi hesablama işi ola bilər (məsələn böyük məlumat təhlili LMS-in disk gecikməsini artırır). Tək CPU limiti disk I/O rəqabətini həll etmir; resurslar ayrıca ölçülür. Səbəbi bilmədən qonşu VM-i söndürmək tədris işini poza bilər.

### Spectre və Meltdown

Yan kanal (side channel) icazəli məlumatı birbaşa oxumaq əvəzinə vaxt, keş davranışı və dolayı təsirlərdən nəticə çıxarır. 2018-ci ildə açıqlanan Spectre və Meltdown ailələri spekulyativ və keçici icranın təhlükəsizlik nəticələrini göstərdi. Spectre proqnozlaşdırılan icra yollarını manipulyasiya etməklə, Meltdown təsirlənən prosessorlarda imtiyaz yoxlaması ilə keçici icra arasındakı davranışla əlaqəlidir. Bunları eyni zəiflik və ya "hazır məlumat oxuma əmri" kimi təsvir etmək düzgün deyil.

Təsir prosessor modelindən, variantdan, host və qonaq yamaqlarından asılıdır; firmware və mikrokod yeniləməsi, hipervizor və nüvə tədbirləri birlikdə tələb oluna bilər. Etibarsız tələbə hesablamalarını məxfi tədqiqat bazası ilə eyni hostda saxlamaq ayrıca risk qərarıdır; yüksək məxfilikdə fiziki ayrılma və ya sərt planlaşdırma seçilə bilər. Bir sazlamanı söndürməklə bütün yan kanalların bağlandığı iddiası əsaslı deyil; tədbirlərin performans təsiri də ölçülür.

### VENOM, ESXiArgs və 2025-ci ilin ESXi zəiflikləri

| Hadisə | Mahiyyət | Dərs |
| --- | --- | --- |
| VENOM (CVE-2015-3456) | QEMU-nun virtual disket nəzarətçisi kodunda yaddaş daşması; qonaqda imkanlı hücumçu hostdakı QEMU prosesinin yaddaşına təsir edə bilərdi | Köhnə görünən virtual periferiya da hücum səthidir; disketdən istifadə olunmaması həssas qurğu modelinin çıxarıldığı demək deyil, düzəliş və faktiki mövcudluq yoxlanır |
| ESXiArgs (2023) | Yamanmamış, şəbəkədən əlçatan ESXi sistemlərinə qarşı ransomware kampaniyası; köhnə OpenSLP zəiflikləri, xüsusən CVE-2021-21974 ilə əlaqələndirildi | Hostun necə ələ keçirildiyi yalnız fayl uzantısından qəti müəyyən edilmir; CISA və FBI bərpa təlimatı yaysa da, bərpa vasitəsi müstəqil ehtiyat nüsxəni əvəz etmir; idarəetmə və köməkçi xidmətlər internetdən ayrılır, yamaq gecikdirilmir |
| CVE-2025-22224, -22225, -22226 (2025, mart) | CVE-2025-22224: qonaqdakı səlahiyyətdən VMX prosesində kod icrasına aparan yaddaş pozuntusu. CVE-2025-22225: ESXi-də VMX prosesindən hipervizor sərhədini keçməyə imkan verən ixtiyari yazma. CVE-2025-22226: məlumat açıqlanması, proses yaddaşından sızma | Fərqli, bir-biri ilə əlaqələndirilə bilən zəifliklərdir; hər sistemdə mütləq eyni üç addımlı hücum kimi öyrənilmir |

Bu CVE-lər CISA-nın məlum istismar olunan zəifliklər kataloqundadır; CISA 2026-cı ildə CVE-2025-22225 üçün ransomware istifadəsini də təsdiqləyib. Təsirlənən versiya, ilkin hüquq və düzəliş konkret məhsul bildirişindən götürülür. Şəbəkə seqmentasiyası qonaqdan başlayan zəncirin bütün mərhələlərini dayandırmaya bilər: idarəetmənin ayrılması ilə yanaşı hipervizorun yamanması da tələb olunur. İnsident şübhəsində VM-i başqa hosta köçürmək onun təmiz olduğunu sübut etmir.

## Hipervizor və idarəetmə müstəvisinin sərtləşdirilməsi

NIST SP 800-125, *Security for Full Virtualization Technologies* (2011), tam virtuallaşdırmanın təhlükəsizlik əsaslarını izah edir; yaşı etibar sərhədlərini ləğv etmir, amma konkret məhsul sazlaması aktual istehsalçı təlimatı ilə tamamlanır. NIST SP 800-190 konteyner təhlükəsizliyinə aiddir; onu hipervizor üzrə eyni təlimat saymaq olmaz. Universitet bu iki sahə üçün əlaqəli, amma ayrıca yoxlanan baza tələbləri yazır.

### Minimal host və nəzarətli dəyişiklik

Hipervizor yalnız tələb olunan funksiyalarla quraşdırılır: istifadə olunmayan xidmət, köhnə virtual qurğu, USB ötürülməsi, ortaq bufer və ortaq qovluq ehtiyac yoxdursa bağlanır; tədris üçün açılan istisna istehsalat şablonuna köçürülmür. Hostda gündəlik internet istifadəsi və aidiyyətsiz proqramlar hücum səthini artırır. Təhlükəsiz açılış (Secure Boot) və imza yoxlaması dəstəklənirsə təsdiqli komponentlərin yüklənməsi üçün istifadə olunur; işləmə vaxtındakı bütün zəiflikləri aradan qaldırmır.

Yamaq planı firmware, CPU mikrokodu, hipervizor, idarəetmə serveri, qonaq alətləri və qonaq ƏS-ni əhatə edir; bir qat digərini əvəz etmir. Ardıcıllıq: uyğunluq və ehtiyat nüsxə yoxlanır, sınaq hostu yenilənir, yük başqa hosta daşınır, növbə ilə tətbiq edilir, sonra versiya və funksiya təsdiqlənir. Riskli zəiflikdə adi texniki xidmət gününü gözləmək əvəzinə sürətləndirilmiş dəyişiklik prosesi işlədilir.

Dəstəkdən çıxmış qonaq ƏS ayrıca risk: Windows 10-un adi dəstəyi 14 oktyabr 2025-ci ildə bitib, biznes ESU proqramı 14 oktyabr 2028-ci ilədək yeniləmə verə bilər, amma bütün Windows 10 VM-ləri avtomatik ESU almır. VDI inventarında buraxılış, hüquq və yeniləmələrin faktiki gəlməsi yoxlanır; VM formatı köhnə ƏS zəifliklərini aradan qaldırmır.

### İdarəetməyə giriş

İdarəetmə müstəvisi (management plane) hipervizoru, mərkəzi konsolu, API-ni və kimlik sistemini əhatə edir. O, tələbə və qonaq Wi-Fi şəbəkələrindən ayrılır, internetə açılmır. Administrator idarə olunan iş stansiyasından VPN və ya qorunan girişlə keçid hostuna (jump host) daxil olur, sonra idarəetmə ünvanına çatır. Şəbəkə ayrılması hesaba etibarı əvəz etmir: fərdi hesab, çoxamilli autentifikasiya (MFA) və rol əsaslı giriş nəzarəti (RBAC) tələb olunur.

:::figure
src = "m13-5.png"
alt = "Admin (MFA) keçid hostuna (qeydiyyat), oradan idarəetmə VLAN-ındakı vCenter-ə qoşulur; vCenter üç hipervizoru idarə edir. Aşağıda ayrıca audit sahəsi: SIEM və dəyişdirilə bilməyən log."
caption = "İdarəetmə girişinin, hipervizorların və ayrıca audit sahəsinin əlaqəsi."
:::

| Rol | İcazə verilən iş | Verilməyən hüquq | Audit mənbəyi |
| --- | --- | --- | --- |
| Laboratoriya operatoru | Öz hovuzunda VM yaratmaq və başlatmaq | Tələbə bazasının diskini ixrac etmək | VM əməliyyat jurnalı |
| Şəbəkə administratoru | Təsdiqlənmiş port qrupu və qayda dəyişikliyi | Bütün bazaların snapshot-ını oxumaq | Şəbəkə konfiqurasiya auditi |
| Ehtiyatlama operatoru | Müəyyən işləri və bərpanı idarə etmək | Bütün nüsxələrin qorunmasını ləğv etmək | Ehtiyatlama jurnalı |
| Təhlükəsizlik analitiki | Qeydləri və konfiqurasiyanı oxumaq | VM silmək və rol paylamaq | Oxuma və sorğu auditi |

Ən yüksək hüquqlar gündəlik istifadə hesabından ayrılır. Xidmət hesablarının hüquqları tələb olunan API əməliyyatlarına qədər daraldılır, sirləri təhlükəsiz saxlanır və dəyişdirilir. Fövqəladə giriş hesabı əsas kimlik xidməti dayananda kömək edir, amma istifadəsi xəbərdarlıq yaratmalıdır. Bütün bərpa mexanizmlərinin eyni virtual domen xidmətindən asılılığı girişin tam itirilməsinə səbəb ola bilər; qəza zamanı hosta necə daxil olunacağı əvvəlcədən sınanır.

### Audit və insidentə cavab

Qeydə alınır: uğurlu və uğursuz girişlər, rol dəyişiklikləri, VM yaradılması, snapshot, disk ixracı, konsol açılması, audit sazlamasının dəyişməsi. Saatlar sinxronlaşdırılır, qeydlər hostdan kənara göndərilir. Şərti audit sətirləri (konkret istehsalçı formatı deyil, hər sətrin əvvəlində 2026-11-08 tarixli vaxt damğası var):

```text
actor=lab-op action=snapshot.create target=lms-db result=denied src=10.10.10.25
actor=infra-admin action=disk.export target=lms-db result=success ticket=CHG-EXAMPLE
```

İkinci əməliyyat texniki olaraq uğurludur, amma dəyişiklik sifarişinin həqiqiliyi və hesabın davranışı yoxlanmalıdır. Snapshot və ixrac hüququ məxfi məlumatı oxuma hüququ qədər ciddi qiymətləndirilir. SIEM yalnız uğursuz girişləri sayırsa, qanuni hesabla disk çıxarılmasını qaçıra bilər; qaydalar aktiv və əməliyyat kontekstinə bağlanır.

Hostun ələ keçirilməsi şübhəsində zərəri məhdudlaşdırmaq, sübutu qorumaq və xidməti bərpa etmək arasında qərar verilir: kor-koranə restart RAM sübutunu itirə bilər, hostu işlək saxlamaq hücumun davamına yol aça bilər. NIST SP 800-61 Rev. 3 (2025) çərçivəsində məsul şəxslər və cavab addımları əvvəlcədən müəyyən edilir. Zərərli hostdan alınmış snapshot yeganə təmiz bərpa mənbəyi sayılmır; etibarlı təsvirlər, sirlərin dəyişdirilməsi və ayrılmış bərpa şəbəkəsi istifadə olunur.

## Konteyner təhlükəsizliyi

### Təsvirin hazırlanması və təchizat zənciri

NIST SP 800-190, *Application Container Security Guide* (2017), riskləri təsvir, reyestr, orkestrasiya, konteyner və host qatlarında ayırır. Təhlükəsizlik yalnız işə salma parametrindən asılı deyil: naməlum baza təsviri, qurma zamanı endirilmiş zərərli paket və ya oğurlanmış reyestr hesabı işləyən konteynerə qədər risk yaradır.

Təsvir minimal baza ilə qurulur, paket versiyaları nəzarətdə saxlanır, proqram komponentlərinin siyahısı (software bill of materials, SBOM) hazırlanır. Zəiflik skanı məlum problemi tapır, amma təmiz nəticə zərərli məntiqin və ya naməlum zəifliyin olmadığını sübut etmir. İmza yoxlaması təsvirin təsdiqli mənbədən gəldiyini yoxlayan siyasətə bağlanır; reyestrə yazma hüququ olan hesablar azaldılır, yerləşdirmə təsdiqlənmiş digest-ə bağlanır.

API açarını Dockerfile-da yazıb sonrakı qatda silmək etibarlı deyil: əvvəlki qatlarda qala bilər. Qurma sirləri üçün müvəqqəti sirr mexanizmi, işləmə zamanı ayrıca sirr xidməti seçilir; təsvirə real tələbə sənədləri və baza nüsxələri qoyulmur. Zəif paket tapılanda işləyən konteynerin içində əl ilə düzəliş etmək təkrarlana bilən nəticə vermir: təsvir düzəldilir, yenidən qurulur, nəzarətlə əvəz edilir.

### İşləmə səlahiyyətləri və nümunə

Konteynerdə root kimi işləmək hostda root olmaqla həmişə eyni deyil (user namespace xəritələnməsi və başqa məhdudiyyətlər fərq yaradır), amma artıq səlahiyyət zəifliyin təsirini böyüdür. `--privileged` rejimi, hostun kök qovluğunun qoşulması və Docker socket-in verilməsi ciddi əsaslandırma tələb edir: geniş hüquqlu Docker daemon-un socket-inə giriş çox vaxt host üzərində yüksək nəzarət verir.

Linux capabilities səlahiyyətləri kiçik hissələrə bölür: lazımsızlar çıxarılır, əlavə imtiyaz qazanma məhdudlaşdırılır, seccomp sistem çağırışlarını süzür; AppArmor və ya SELinux fayl və proses davranışını əlavə məhdudlaşdırır. Rootless icra host imtiyazlarını azaldır, amma nüvə zəifliklərini və tətbiq avtorizasiya səhvlərini aradan qaldırmır; nüvə yamaqları təsvirdən ayrı idarə olunur.

Şəbəkə tələb etməyən laboratoriya sınağı üçün şərti Docker əmri (UID 10001, yalnız `/tmp`-yə yazma əvvəlcədən yoxlanır; etiket tədris nümunəsidir, istehsalatda təsdiqlənmiş digest seçilir; limitlər şərtidir):

```bash
docker run --rm --name kitabxana-test \
  --user 10001:10001 --read-only \
  --tmpfs /tmp:rw,noexec,nosuid,size=64m \
  --cap-drop ALL --security-opt no-new-privileges=true \
  --pids-limit 128 --memory 256m --cpus 0.5 \
  --network none registry.unec.example/kitabxana:2026-11
```

Şəbəkə bağlanır, kök fayl sistemi oxuma rejimindədir, proses/yaddaş/CPU məhdudlaşır. Tətbiq bazaya qoşulmalıdırsa nümunə olduğu kimi uyğun gəlmir: ayrıca şəbəkə və yalnız lazım olan çıxışlar açılır. Oxuma rejimi məlumat oğurlamasını avtomatik dayandırmır: həssas məlumatı oxuyan proses icazəli çıxış kanalından onu göndərə bilər; tədbir tətbiqin həqiqi işi ilə yoxlanır.

### Kubernetes siyasətləri

Kubernetes-də RBAC tətbiq xidməti hesabına yalnız tələb olunan API hüquqlarını verir; token lazım deyilsə avtomatik qoşulması bağlanır. Pod Security Admission uyğun səviyyədə riskli Pod parametrlərini məhdudlaşdırır. Secret obyektində base64 kodlaşdırma **şifrələmə deyil**: saxlama zamanı şifrələmə, etcd girişləri və sirri oxuyan hesablar ayrıca qorunur. Ad fəzasının adı təkbaşına şəbəkə sərhədi yaratmır.

Şərti Pod-un əsas məhdudiyyətləri (xidmətə çıxış, davamlı məlumat, sağlamlıq yoxlamaları və nəzarətçi ayrıca hazırlanmalıdır):

```yaml
apiVersion: v1
kind: Pod
metadata: {name: kitabxana-demo, namespace: kitabxana}
spec:
  automountServiceAccountToken: false
  securityContext: {runAsNonRoot: true, runAsUser: 10001, seccompProfile: {type: RuntimeDefault}}
  containers:
    - name: app
      image: registry.unec.example/kitabxana:2026-11
      securityContext: {allowPrivilegeEscalation: false, readOnlyRootFilesystem: true, capabilities: {drop: ["ALL"]}}
      resources: {requests: {cpu: "100m", memory: "128Mi"}, limits: {cpu: "500m", memory: "256Mi"}}
      volumeMounts: [{name: temp, mountPath: /tmp}]
  volumes: [{name: temp, emptyDir: {sizeLimit: "64Mi"}}]
```

CPU request planlaşdırma üçün tələb, CPU limit yuxarı həddir (limitə çatma icranı ləngidir); yaddaş limitinin aşılması prosesin dayandırılmasına gətirə bilər. Dəyərlər məhsuldarlıq tövsiyəsi deyil. Bütün replikaların eyni anda limitə çatması yalnız replika sayını artırmaqla düzəlməyə bilər: düyündə fiziki tutum da qalmalıdır.

NetworkPolicy seçilmiş Pod-lara icazə verilən trafik istiqamətlərini bildirir; siyasəti tətbiq edən şəbəkə plaqini olmalıdır. Şərti qayda `lms` ad fəzasındakı `app: lms-db` Pod-larına yalnız həmin ad fəzasında `app: lms-api` Pod-larından TCP 5432 (nümunədə PostgreSQL) girişini açır:

```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: db-from-api
  namespace: lms
spec:
  podSelector:
    matchLabels:
      app: lms-db
  policyTypes: [Ingress]
  ingress:
    - from:
        - podSelector:
            matchLabels:
              app: lms-api
      ports:
        - protocol: TCP
          port: 5432
```

Bu qayda çıxış trafikini məhdudlaşdırmır və Pod-u seçən digər icazə siyasətlərini ləğv etmir: icazələr **birləşir**, digər siyasətin geniş giriş açıb-açmadığı yoxlanır. Bazanın autentifikasiyası və şifrələnmiş bağlantısı yenə lazımdır. Etiketi dəyişə bilən hesab siyasətin təsirinə müdaxilə edə bilər, ona görə RBAC ilə şəbəkə qaydaları birlikdə qiymətləndirilir; laboratoriya hesabına istənilən ad fəzasında Pod yaratmaq hüququ verilmir.

## Virtual və şəbəkə nasazlıqlarının diaqnostikası

### Müşahidədən fərziyyəyə

Diaqnostika problemin sərhədini ölçməklə başlayır: LMS hamı üçün açılmır, yalnız yataqxanada açılmır, yoxsa səhifə açılır, baza əməliyyatı dayanır? Başlanma vaxtı, təsirlənən xidmət, son dəyişiklik və normal işləyən müqayisə nöqtəsi qeyd olunur. Şikayət texniki nəticədən ayrılır: "internet yoxdur" DNS, autentifikasiya və ya tək tətbiq problemi ola bilər.

Sonra şəbəkə arxitekturası çəkilir: müştəri, access point və ya kabel portu, kommutator, marşrutlaşdırıcı, firewall, hipervizor uplink-i, vSwitch, vNIC, tətbiq. Aktiv qurğular trafiki emal edir, passiv kabel və konnektorlar daşıyır; virtual mühit passiv fiziki hissəni aradan qaldırmır. OSI-nin fiziki və kanal qatlarından IP, nəqliyyat və tətbiq qatlarına doğru yoxlama səhvin yerini daraldır; TCP/IP qatları ilə də eyni müşahidələr əlaqələndirilə bilər.

| Addım | Yoxlanan sahə | Sual və müşahidə | Sonrakı qərar |
| --- | --- | --- | --- |
| 1 | Əhatə və dəyişiklik | Bir VM, bir host, yoxsa bütün kampus təsirlənib? | Müqayisə nöqtəsini seçmək |
| 2 | Fiziki yol | Kabel, port, enerji, uplink işləyirmi? | Link xətasını ayırmaq |
| 3 | Virtual bağlantı | vNIC qoşulubmu, port qrupu düzgündürmü? | VM ilə vSwitch arasını yoxlamaq |
| 4 | IP və DHCP | Ünvan, maska, şlüz, icarə düzgündürmü? | Ünvanlama səhvini düzəltmək |
| 5 | VLAN və marşrut | Etiket və icazəli trunk siyahısı uyğundurmu? | Paketin itən sərhədini tapmaq |
| 6 | Nəqliyyat və siyasət | Tələb olunan TCP və ya UDP axını keçir? | Firewall və xidmət dinləyicisini ayırmaq |
| 7 | DNS və tətbiq | Ad düzgün həll olunurmu, TLS və giriş işləyirmi? | Tətbiq asılılığını araşdırmaq |
| 8 | Resurs və qeydlər | CPU gözləməsi, disk və yaddaş təzyiqi varmı? | Şəbəkə kimi görünən resurs problemini tapmaq |
| 9 | Dəyişiklik və təsdiq | Bir fərziyyə bir dəyişiklik ilə yoxlanıbmı? | Nəticəni təsdiqləyib sənədləşdirmək |

### Fiziki və virtual yolu yoxlamaq

Port indikatoru və link vəziyyəti, kabelin oturması, optik modul, port səhv sayğacları və sürət razılaşması yoxlanır; normal kabel və ya portla nəzarətli müqayisə faydalıdır. Bütün klaster uplink-ini təsadüfən ayırmaq əhatəni böyüdər. Bir hostdakı bütün VM-lər təsirlənibsə ortaq uplink və vSwitch ehtimalı artır; yalnız bir VM təsirlənibsə vNIC-in qoşulu vəziyyəti, port qrupu və qonaq sürücüsü yoxlanır.

Live migration-dan sonra problem başlayıbsa, hədəf hostda eyni adlı port qrupunun eyni VLAN-a bağlandığı təsdiqlənir: adların bərabərliyi konfiqurasiyaların eyniliyi deyil. Uplink-də VLAN icazə siyahısı, qonaqda MTU və varsa overlay şəbəkəsinin əlavə başlıq tələbi araşdırılır. Kiçik paketlərin keçməsi böyük ötürmələrin keçəcəyini sübut etmir; MTU şübhəsində platformanın diaqnostika üsulu ilə yol boyu ölçü uyğunluğu yoxlanır.

### Ünvan, marşrut və xidmət yoxlaması

Şərti laboratoriya VM-i: 10.50.0.25/24, şlüz 10.50.0.1, DNS 10.50.0.53. Linux oxuma əmrləri (bəziləri ayrıca paket tələb edə bilər, çıxışlar mühitin faktiki ünvanları ilə şərh olunur):

```bash
ip -br link
ip -br address
ip route
ip route get 10.20.0.10
ip neigh
ping -c 3 10.50.0.1
traceroute 10.20.0.10
ss -lntup
dig @10.50.0.53 lms.unec.example A
```

Windows-da `ipconfig /all`, `route print`, `tracert`, `netstat -ano` və PowerShell-də `Test-NetConnection` uyğun suallara cavab verir. Məsələn, DNS-dən asılı olmadan şərti LMS ünvanında TCP 443 yoxlaması:

```powershell
Test-NetConnection 10.20.0.10 -Port 443
```

Maska ilə ünvanın məntiqi AND əməliyyatı alt şəbəkəni verir: 10.50.0.25 və 255.255.255.0 üçün şəbəkə 10.50.0.0/24-dür. VM-ə yanlış /16 maskası verilsə, bəzi uzaq ünvanları lokal hesab edib şlüzə göndərmək əvəzinə qonşu axtara bilər. DHCP hovuzu, icarə vaxtı, rezerv və statik ünvanların toqquşması yoxlanır; statik ünvanın DHCP hovuzundan nəzarətsiz götürülməsi fasiləli nasazlıq yaradır.

:::exam Alətlərin cavab verdiyi sual
`ping` cavabı ICMP əlçatanlığını göstərir, veb xidmətin işlədiyini yox; cavab gəlməməsi hostun söndüyünü sübut etmir (ICMP siyasətlə bloklana bilər). `traceroute`-da ulduzlar aralıq qurğunun cavab vermədiyini göstərə bilər, onun bütün trafiki atdığını yox. `ss` və `netstat` dinləyən portu və bağlantını göstərir; xidmət yalnız 127.0.0.1-ə bağlanıbsa şəbəkədən əlçatan olmaz. Konspektdə ping, traceroute, ipconfig, netstat şəbəkə əsaslarına aid alətlər kimi yalnız qısa xatırladılır.
:::

TLS ad yoxlamasını qoruyaraq DNS-i ayrıca sınamaq üçün şərti nümunə:

```bash
curl --connect-timeout 5 \
  --resolve lms.unec.example:443:10.20.0.10 \
  https://lms.unec.example/health
```

Ünvan məcburi seçilir, host adı və sertifikat yoxlaması qalır. Daxili sertifikat mərkəzi varsa etibarlı kök sertifikat qurulur; yoxlamanı söndürmək həll sayılmır. `/health` yalnız həmin son nöqtənin yoxladığı asılılıqları təsdiqləyir: tələbə hesabının avtorizasiyası və bazaya yazı ayrıca yoxlanır. VPN varsa tunel marşrutları, DNS seçimi və üst-üstə düşən lokal ünvan aralıqları da araşdırılır.

### Jurnallar və nəzarətli təcridetmə

Qonaq, hipervizor, firewall, fiziki kommutator, DHCP, DNS və tətbiq qeydləri eyni zaman xəttində tutuşdurulur. Linux nümunələri:

```bash
journalctl -b -p warning
journalctl -k -b
df -h
free -h
vmstat 1 5
```

Şərti hal: tətbiq jurnalında baza bağlantısı üçün timeout var, firewall rədd qeydi yoxdur, həmin vaxt hipervizorda saxlama gecikməsi artıb. Bu şəbəkə ehtimalını tam bağlamır, amma disk təzyiqini yoxlamağa əsas verir. Konteynerdə `kubectl describe pod`, `kubectl logs` və hadisələr başlanma xətasını, yaddaş limitinin aşılmasını və şəbəkə siyasətini ayırır; API-yə giriş yoxdursa işçi düyünün və idarəetmə müstəvisinin vəziyyəti ayrıca araşdırılır.

Nəzarətli təcridetmədə **bir fərziyyə** seçilir və **bir dəyişən** dəyişdirilir: eyni VLAN-dakı sağlam VM ilə müqayisə, test VM-i ilə port qrupu yoxlaması, icazə varsa dar filtrli paket müşahidəsi. Bütün firewall-u söndürmək və ya bütün klasteri restart etmək səbəbi gizlədə və məlumat itirə bilər; yenidən yükləmə lazımdırsa əvvəl qeydlər saxlanır, ehtiyatlama və təsir qiymətləndirilir, sonra planlı icra olunur. Firmware və proqram yeniləməsi təsadüfi cəhd kimi aparılmır.

### İşlənmiş diaqnostika nümunəsi

Şərti hadisə: LMS VM-i texniki xidmət üçün host A-dan host B-yə köçürülüb. VM işləyir, konsoldan giriş var, amma tələbələr saytı aça bilmir.

:::steps Host B-yə köçürmədən sonra LMS açılmır
[[step]]
title = "Əhatə"
body = "Yalnız bu VM təsirlənib; başqa hostdakı LMS test VM-i işləyir."

[[step]]
title = "Qonaq və şlüz"
body = "Ünvan və standart marşrut əvvəlki kimidir, şlüz üçün ARP sorğusu çıxır, cavab yoxdur. DNS dəyişmək və ya tətbiqi yenidən qurmaq üçün əsas yoxdur."

[[step]]
title = "Port qrupu və trunk"
body = "Port qrupunda VLAN 20 düzgündür, amma host B-nin fiziki trunk portunda VLAN 20 icazəli siyahıda yoxdur."

[[step]]
title = "Düzəliş, təsdiq, təkrarın qarşısı"
body = "Təsdiqlənmiş dəyişiklik yalnız həmin portun siyahısını düzəldir; şlüz cavabı, TCP 443, DNS ilə giriş və tələbə hesabının LMS əməliyyatı yoxlanır. Hostlar üzrə uyğunluq yoxlaması köçürmə proseduruna əlavə edilir."
:::

Problem yerli imkanlarla ayrılmırsa istehsalçının sənədi və texniki dəstək istifadə olunur. Eskalasiya paketində topologiya, versiyalar, vaxt aralığı, müşahidələr, dəyişikliklər və şəxsi məlumatdan təmizlənmiş qeydlər olur; hansı fərziyyənin hansı sübutla rədd edildiyi yazılır ki, ekspert eyni yoxlamaları təkrar etməsin. Nasazlığın aradan qalxması son addım deyil: düzəlişin təhlükəsizlik siyasətini pozmadığı və normal yükdə işlədiyi təsdiqlənir.

### Əlavə praktik işlər

Dörd laboratoriya tapşırığı: (1) iki alt şəbəkəni birləşdirən marşrutlaşdırıcı (ünvan, maska, standart marşrut, statik və DHCP variantı, OSI/TCP/IP qatları, marşrut cədvəli və iki istiqamətli yoxlama); (2) idarə olunan kommutatorda VLAN 20 və 30, son qurğu portları access, hipervizor uplink-i yalnız lazım olan VLAN-ları daşıyan trunk, VLAN-lar arasında yalnız təsdiqlənmiş marşrut və firewall qaydası; (3) TCP soket müştəri və serveri (əvvəl yalnız 127.0.0.1, mesaj sərhədi uzunluq prefiksi və ya ayırıcı ilə, TCP mesaj sərhədlərini saxlamır); (4) iki laboratoriya şəbəkəsi arasında VPN (tunel ünvanları, qarşı tərəfin kimlik yoxlaması, icazəli marşrutlar, tunel bağlanandan sonra girişin kəsilməsi).

## Köhnə slaydlarla fərq

:::note Köhnə slaydlarla fərq
Konspektin düzəlişləri (mühazirə ilə uyğun olanlar): VM-lər bir-birindən **tam təcrid olunmur** (hipervizor zəiflikləri, resurs rəqabəti, yan kanallar, host nasazlığı hamıya təsir edir). "Bütün avadanlıq təqlid edilir" köhnə təsvirdir, müasir virtuallaşdırma aparat dəstəyi ilə işləyir. "Bütün ƏS və proqramlarla uyğundur" şərtlidir (arxitektura, drayver, lisenziya). Tip 1 üçün ayrıca idarəetmə maşını məcburi deyil. İşləyən VM fayllarını kopyalamaq uyğunsuz nüsxə verə bilər.
:::
