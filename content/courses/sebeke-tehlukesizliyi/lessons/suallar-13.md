+++
title = "Virtuallaşdırmanın əsasları və təhlükəsizliyi"
unit = "suallar"
order = 13
summary = "Mühazirənin nəzarət sualları, situasiya tapşırıqları, konspektin situasiyaları və ehtimal olunan əlavə suallar, imtahana hazır cavablarla."
updated = 2026-11-09

[[source]]
title = "Mühazirə 13: Virtuallaşdırmanın əsasları və təhlükəsizliyi"
note = "Elmar Cabbarov, 2026–2027"

[[source]]
title = "Midterm konspekti, Mövzu 13"
note = "Elmar Cabbarov"
+++

İmtahan yazılı və açıq suallarla keçir. Hər sualı əvvəl öz sözlərinlə cavablandır, sonra cavaba bax. Situasiya cavablarında ardıcıllıq: aktiv, pozulan xassə, səbəb, tədbir, yoxlama.

## Nəzarət sualları

:::reveal Virtuallaşdırma fiziki resursla qonağın gördüyü resurs arasında hansı əlaqəni qurur?
- Virtuallaşdırma (virtualization) fiziki hesablama resursunu proqramlara məntiqi resurs kimi təqdim edir və istifadəsini idarə edir.
- Qonaq fiziki serverin quruluşunu deyil, ona ayrılmış virtual prosessoru, yaddaşı, diski və şəbəkə interfeysini görür.
- Təqdimatı hipervizor (hypervisor) təbəqəsi yaradır və bir fiziki qurğudan bir neçə mühitin istifadəsini əlaqələndirir.
- Paylaşma səmərəlilik verir, ayırma isə bir mühitin digərinə icazəsiz təsirini məhdudlaşdırır; ikisi birlikdə düşünülməlidir.
:::

:::reveal İnkapsulyasiya, izolyasiya, uyğunluq və avadanlıqdan nisbi müstəqilliyin sərhədləri nədir?
- **İnkapsulyasiya:** VM konfiqurasiya, disk və vəziyyət faylları ilə təsvir olunur; amma disk faylı təkbaşına kifayət etmir (şifrələmə açarı, virtual firmware, əlavə disklər). RAM vəziyyəti saxlanmayıbsa, işləyən proseslər davam etmir.
- **İzolyasiya:** birbaşa icazəsiz çıxışı məhdudlaşdırır; ortaq host, hipervizor, disk və prosessor riskləri qalır, tam təcrid yoxdur.
- **Uyğunluq:** standart virtual qurğular hesabına; prosessor arxitekturası, sürücü, proqram və lisenziya ilə məhduddur.
- **Avadanlıqdan nisbi müstəqillik:** x86 qonağı fərqli arxitekturaya köçürmək eyni iş deyil; birbaşa verilmiş GPU və ya şəbəkə qurğusu daşınmanı məhdudlaşdırır.
- Xüsusiyyətlər zəmanət kimi yox, şərtlər daxilində başa düşülür.
:::

:::reveal Birinci və ikinci tip hipervizorlar necə fərqlənir? Hyper-V və KVM-in təsnifatını əsaslandırın.
- **Birinci tip (bare metal):** avadanlıq üzərində nəzarəti özü qurur, altında ümumi təyinatlı host ƏS yoxdur (ESXi, Xen). **İkinci tip (hosted):** host ƏS üzərində proqram kimi işləyir (VirtualBox, VMware Workstation).
- **Hyper-V** birinci tipdir: hipervizor avadanlığın üzərindədir, Windows isə idarəedici kök bölmədə işləyir; Windows mühiti görünməsi ikinci tip etmir.
- **KVM** Linux nüvəsinə virtuallaşdırma funksiyası əlavə edir və birinci tip kimi təsnif olunur; QEMU istifadəçi məkanında virtual qurğuları tamamlayır.
- Proxmox VE ayrıca hipervizor deyil, KVM və konteynerləri idarə edən platformadır; ekranda adi ƏS görünməsi təsnifat üçün kifayət etmir.
- Birinci tip avtomatik təhlükəsiz, ikinci tip avtomatik zəif deyil; müqayisə hücum səthinə, idarəetmə hüquqlarına və təsir dairəsinə əsaslanır.
:::

:::reveal Tam virtuallaşdırma ilə aparat dəstəkli virtuallaşdırma niyə bir yerdə işləyə bilər?
- Tam virtuallaşdırma qonağa yetərli virtual aparat interfeysi verir, qonağın dəyişdirilməsi tələb olunmur. Bu, **qonağın gördüyü interfeys** haqqındadır.
- Aparat dəstəyi (Intel VT-x, AMD-V) isə **prosessorun qonaq icrasına necə nəzarət etdiyi** haqqındadır.
- Tarixən problemli təlimatlar ikili çevirmə (binary translation) ilə dəyişdirilirdi; aparat dəstəyi bu işi prosessora verir, qonaq yenə tam virtuallaşdırılmış mühit görür.
- Deməli, bunlar bir-birini istisna edən siniflər deyil, fərqli suallara cavabdır.
:::

:::reveal Paravirtual sürücü hansı işi sadələşdirir və hansı uyğunluq problemi yarada bilər?
- Paravirtual sürücü (məsələn Linux-da virtio disk və şəbəkə) qurğunun mürəkkəb fiziki modelini təqlid etmək əvəzinə hipervizorla sadələşdirilmiş qarşılıqlı əlaqə qurur və CPU xərcini azalda bilər.
- Sürücü qonaqda mövcud deyilsə, sistem açılış diskini görməyə bilər.
- Disk nəzarətçisini dəyişməzdən əvvəl sürücü quraşdırılır, geri qayıtma yolu hazırlanır, sınaq VM-i üzərində açılış yoxlanır.
- Paravirtuallaşdırma sürət vasitəsidir; sürücünün və hipervizorun təhlükəsizliyi ayrıca qorunur.
:::

:::reveal Ring 0 ilə VMX non-root rejimi arasında münasibət nədir? Ring −1 ifadəsi necə başa düşülməlidir?
- Ring 0 nüvənin imtiyaz halqasıdır, tətbiq ring 3-dədir. VMX root və non-root rejimləri isə Intel VT-x-in ayrıca rejimləridir və ring nömrəsinin davamı deyil.
- Qonaq nüvəsi VMX non-root rejimində ring 0-da işləyə bilər; hipervizor root rejimində idarəni saxlayır.
- Ring −1 bəzi mətnlərdə hipervizora verilən şərti addır, x86-nın rəsmi halqası deyil.
- Nəzarət tələb edən hadisədə VM çıxışı (VM exit) baş verir; hipervizor yoxlayır və qonağı davam etdirir.
:::

:::reveal vCPU sayı niyə ayrılmış fiziki nüvə sayı ilə eyni deyil?
- vCPU qonağın gördüyü icra vahididir; hipervizor onu fiziki prosessorun məntiqi icra vahidlərinə planlaşdırır.
- Bağlama və rezerv siyasəti yoxdursa, vahidlər zamanla başqa VM-lərlə bölüşülür; aparat axınları da iki müstəqil nüvə qədər məhsuldarlıq vermir.
- Overcommit (şərti nümunə: 24 nüvəyə 4 × 8 = 32 vCPU) qadağan deyil, amma hamı eyni vaxtda işləyəndə növbə yaranır; qonaqda CPU aşağı görünsə gözləmə (CPU ready, steal time) yüksək ola bilər.
- Rezerv əlçatanlığı qoruyur, limit yuxarı həddi qoyur, pay rəqabətdə üstünlük verir.
:::

:::reveal Yaddaşın həddən artıq təyini və balloon mexanizmi bazanın gecikməsinə necə təsir edə bilər?
- Balloon sürücüsü qonaq daxilində səhifələr ayırıb saxlayır, hipervizor həmin səhifələrin fiziki yaddaşını başqa VM-lərə verir.
- Qonaqda istifadə edilə bilən yaddaş azalır: keş boşaldılır və ya səhifələr diskə çıxarılır.
- Disk RAM-dan ləng olduğundan nəticə uzun fasilələrdir; bazanın keş səhifələri diskə dəyişəndə hər sorğu gecikir.
- Ona görə yaddaşın artıq təyini bəzən CPU-dan daha sərt problem yaradır; yaddaş rezervi və real işçi dəst ölçülür.
:::

:::reveal Saxlama virtuallaşdırılması, virtual yaddaş və verilənlərin virtuallaşdırılması necə ayrılır?
- **Saxlama virtuallaşdırılması:** fiziki disklər məntiqi həcmlərə çevrilir.
- **Virtual yaddaş (ünvanlama):** proses ünvanları yaddaş səhifələrinə çevrilir (RAM ilə bağlıdır, diskdən abstraksiya deyil).
- **Verilənlərin virtuallaşdırılması (data virtualization):** vasitəçi qat ayrı mənbələrə vahid sorğu görünüşü verir; əsas təhlükəsizlik məsələsi səlahiyyətlərin uyğunlaşdırılması və zaman uyğunsuzluğudur.
- Bazanın VM daxilində işləməsi verilənlərin virtuallaşdırılması deyil.
:::

:::reveal Eyni hostdakı VM-lərin trafiki hansı halda fiziki IDS-dən keçməyə bilər?
- Eyni hostda, eyni məntiqi seqmentdəki iki VM arasındakı trafik vSwitch-də ötürülür və uplink-ə çıxmır.
- Yalnız fiziki uplink üzərindəki IDS və firewall belə trafiki görmür.
- Çarə: sensorun real paket yoluna uyğun yerləşdirilməsi, virtual firewall, mikroseqmentasiya (məsələn VMware NSX) və ya hostda sensor.
- Eyni VLAN daxilindəki VM-ləri ayırmaq üçün ayrıca paylanmış firewall qaydası lazımdır.
:::

:::reveal Bridged, NAT, host-only və daxili şəbəkə rejimlərini risklərinə görə müqayisə edin.
| Rejim | Əlaqə | Risk |
| --- | --- | --- |
| Bridged | Fiziki seqmentdəki qurğularla, real kompüter kimi | VM kampus şəbəkəsinə birbaşa çıxır |
| NAT | Çıxış ünvan çevirməsi ilə | Çıxış hücumları və məlumat sızması (zərərli trafiki qadağan etmir) |
| Host-only | Host və həmin şəbəkədəki VM-lər | Hosta hücum, səhv marşrutlaşdırma |
| Daxili | Yalnız seçilmiş VM-lər | İkinci interfeys və hipervizor zəifliyi |

Zərərli proqram təhlili üçün ən uyğunu daxili şəbəkədir, amma faktiki interfeyslər və marşrutlar yoxlanır.
:::

:::reveal Snapshot, klon, replikasiya və müstəqil ehtiyat nüsxə hansı məqsədlərlə seçilir?
- **Snapshot:** yeniləmədən əvvəl qısa müddətli geri qayıtma; baza diskdən və platformadan asılıdır.
- **Klon:** test və tədris mühiti; köhnə sirlər və kimliklər köçə bilər.
- **Replikasiya:** dayanmadan sonra tez bərpa; səhvi və şifrələnməni də köçürür.
- **Ehtiyat nüsxə:** silinmə, ransomware və fəlakətdən bərpa; ayrı giriş və bərpa sınağı tələb edir.
- Eyni hovuzda qalan snapshot müstəqil ehtiyat nüsxə sayılmaz.
:::

:::reveal Live migration üçün yaddaş, disk, şəbəkə və CPU uyğunluğu niyə birlikdə yoxlanır?
- Pre-copy: yaddaşın ilkin surəti ötürülür, dəyişən səhifələr təkrar göndərilir, qısa dayandırma ilə qalan vəziyyət köçür, qonaq hədəfdə davam edir.
- Saxlama ortaq deyilsə disk də köçürülməlidir; hostların prosessor və virtual qurğu uyğunluğu tələb olunur.
- Yaddaş çox sürətlə dəyişirsə köçürmə uzanır; live migration sıfır fasilə zəmanəti deyil.
- Hədəfdə VLAN, firewall və saxlama siyasətləri qorunmalıdır; kanal ayrılır, autentifikasiya və şifrələmə aktiv edilir.
:::

:::reveal HA klasterinin olması hansı səbəblərdən xidmətin fasiləsizliyinə zəmanət vermir?
- HA VM-i başqa hostda yenidən başladır: qonaq ƏS və tətbiq təkrar açılır, fasilə qalır, RAM-dakı saxlanmamış məlumat itə bilər.
- Ehtiyat tutum yoxdursa, yer çatmır (336 GiB tutumda biri itəndə 224 GiB qalır).
- Replikalar eyni hostdadırsa (anti-affinity yoxdur) və ya eyni elektrik, kommutator, massivə bağlıdırsa, ortaq risk qalır.
- Kvorum və fencing düzgün sazlanmalıdır; HA resurs yaratmır.
:::

:::reveal RPO və RTO universitetin ehtiyatlama siyasətini necə dəyişir?
- RTO xidmətin qaytarılma müddətini, RPO qəbul edilən məlumat itkisini bildirir.
- RPO 15 dəqiqə, RTO 1 saat olan bazaya gecəlik nüsxə kifayət etmir: tranzaksiya jurnalları və ya replikasiya lazımdır.
- RTO-ya VM-in açılması ilə yanaşı bazanın yoxlanması və istifadəçi girişi də daxildir.
- Hər xidmətin hədəfi fərqlidir (LMS materialları RPO 4 saat/RTO 2 saat, kafedra saytı 24/8 saat); bərpa ayrılmış şəbəkədə sınanır.
- 3-2-1 qaydası və oflayn/dəyişdirilə bilməyən nüsxə tətbiq olunur.
:::

:::reveal Konteynerin namespaces və cgroups mexanizmləri hansı ayrı məsələləri həll edir?
- **Namespace** prosesə resursların ayrılmış görünüşünü verir (PID, mount, network, user).
- **cgroups** CPU, yaddaş və digər resurs istifadəsini hesablayır və məhdudlaşdırır.
- Biri görünüşü ayırır, digəri resurs istifadəsinə nəzarət edir; heç biri bütün təhlükəsizliyi həll etmir.
- Yaddaş limiti yoxdursa bir proqram başqalarının yaddaşını tükədə bilər; limit varsa aşan proses dayandırıla bilər.
:::

:::reveal Kubernetes ad fəzası, Linux network namespace və NetworkPolicy necə fərqlənir?
- **Kubernetes ad fəzası** API obyektlərini məntiqi qruplaşdırır, təkbaşına şəbəkə sərhədi yaratmır.
- **Linux network namespace** prosesin interfeys və marşrutlarını ayırır.
- **NetworkPolicy** seçilmiş Pod-lara icazə verilən trafik istiqamətlərini bildirir; tətbiq edən şəbəkə plaqini lazımdır.
- Nümunə: lms-db Pod-ları yalnız lms-api Pod-larından TCP 5432 qəbul edir; icazələr birləşir, çıxışı bu qayda məhdudlaşdırmır.
:::

:::reveal VM escape, hyperjacking və oğurlanmış idarəetmə hesabı ilə hücumun yollarını ayırın.
- **VM escape:** qonaqdakı kod sərhədi keçib host/hipervizor kontekstində icra qazanır (zəiflik tələb olunur).
- **Oğurlanmış idarəetmə hesabı:** hücumçu qanuni səlahiyyətlə VM konsolu açır, disk qoşur, snapshot çıxarır, VM silir; zəiflik lazım deyil, ayrıca audit gərəkdir.
- **Hyperjacking:** hipervizorun ələ keçirilməsi və ya gizli zərərli hipervizor; daha aşağı etibar qatından qonaqların gördüyü vəziyyət idarə olunur, tək VM-i yenidən qurmaq kifayət etmir.
:::

:::reveal VENOM, ESXiArgs və CVE-2025-22224 zənciri hansı fərqli təhlükəsizlik dərslərini verir?
- **VENOM (CVE-2015-3456):** QEMU virtual disket nəzarətçisində yaddaş daşması; köhnə virtual periferiya da hücum səthidir.
- **ESXiArgs (2023):** yamanmamış, əlçatan ESXi-yə ransomware (OpenSLP, CVE-2021-21974); idarəetməni internetdən ayırmaq və yamaqları gecikdirməmək; CISA/FBI bərpa təlimatı müstəqil ehtiyat nüsxəni əvəz etmir.
- **CVE-2025-22224/22225/22226 (2025, mart):** VMX-də yaddaş pozuntusu, VMX-dən hipervizora ixtiyari yazma, məlumat açıqlanması; CISA kataloqunda, 22225 ransomware ilə (2026). Seqmentasiya + yamaq birlikdə.
:::

:::reveal Spekulyativ icra yan kanallarına qarşı niyə bir neçə qat üzrə tədbir tələb olunur?
- Yan kanal icazəli məlumatı birbaşa oxumur, vaxt və keş davranışından nəticə çıxarır.
- Spectre (proqnozlaşdırılan icra yolları) və Meltdown (imtiyaz yoxlaması ilə keçici icra) eyni zəiflik deyil.
- Təsir prosessor modelindən, variantdan, host və qonaq yamaqlarından asılıdır: firmware/mikrokod, hipervizor və nüvə tədbirləri birlikdə lazım ola bilər.
- Yüksək məxfilikdə fiziki ayrılma seçilir; tək sazlamanı söndürmək hamısını bağlamır, performans təsiri ölçülür.
:::

:::reveal NIST SP 800-125 və NIST SP 800-190 hansı fərqli mühitləri əhatə edir?
- **SP 800-125** (2011), *Security for Full Virtualization Technologies*: tam virtuallaşdırma, yəni hipervizor mühiti.
- **SP 800-190** (2017), *Application Container Security Guide*: konteyner təhlükəsizliyi (təsvir, reyestr, orkestrasiya, konteyner, host qatları).
- Biri digərini əvəz etmir; sənədin yaşı etibar sərhədlərini ləğv etmir, amma məhsul sazlaması aktual təlimatla tamamlanır.
:::

:::reveal VM konsoldan işləyir, şəbəkədən açılmırsa, hansı ardıcıllıqla fərziyyələri yoxlamaq lazımdır?
1. Əhatə və son dəyişiklik; müqayisə nöqtəsi.
2. Fiziki yol (kabel, port, uplink).
3. Virtual bağlantı (vNIC, port qrupu).
4. IP, maska, şlüz, DHCP.
5. VLAN və marşrut (trunk siyahısı, etiket).
6. TCP/UDP və firewall; xidmətin dinlədiyi ünvan.
7. DNS, TLS və tətbiq.
8. Resurs təzyiqi və qeydlər.
9. Bir fərziyyə bir dəyişiklik ilə yoxlanır, təsdiqlənir, sənədləşdirilir.
:::

## Situasiya tapşırıqları

**Situasiya 1.** Universitetin zərərli proqram laboratoriyasında VirtualBox VM-i bridged rejimdədir, ortaq bufer və host qovluğu açıqdır. Laboratoriya işi real tələbə sənədləri saxlanan noutbukda aparılır. Hansı sərhədlər pozula bilər?

:::reveal Cavab
- **Pozulan sərhədlər:** VM kampus şəbəkəsinə birbaşa trafik göndərə bilər; ortaq qovluq və bufer hosta əlavə keçid yaradır.
- **Tədbir:** iş ayrıca, real məlumatsız laboratoriya qurğusunda aparılır; daxili virtual şəbəkə, lazım olduqda simulyasiya xidməti seçilir.
- Ortaq inteqrasiya imkanları bağlanır, hipervizor yamanır, iş bitəndə təmiz vəziyyət qaytarılır.
- Daxili şəbəkə də escape riskini aradan qaldırmır, ona görə hostun ayrılması qalır.
:::

**Situasiya 2.** Tələbə bazasının gündəlik snapshot-ları əsas VM ilə eyni massivdədir. Şərti ransomware hadisəsində hipervizor idarəetməsi ələ keçirilib və bütün bu fayllar silinib. Komanda niyə əvvəlki günə qayıda bilmir?

:::reveal Cavab
- **Səbəb:** bərpa nöqtələri eyni nasazlıq və giriş sahəsində qalıb; müstəqil, başqa yerdə saxlanan və silinməsi ayrıca məhdudlaşdırılan ehtiyat nüsxə yoxdur.
- Snapshot qısa geri qayıtma nöqtəsidir, ayrıca qorunan ehtiyatlama deyil.
- **Tədbir:** bərpa siyasəti tətbiq uyğunluğunu, açarları, RPO və RTO-nu, ayrılmış şəbəkədə sınağı əhatə etməlidir.
- İdarəetmə hesablarının və sirlərin bərpası da tələb olunur.
:::

**Situasiya 3.** Şərti klasterdə iki hostun hər biri VM-lərə 112 GiB RAM verə bilir. LMS və digər kritik VM-lər birlikdə 160 GiB tələb edir. Bir host dayananda HA bütün VM-ləri başlada bilmir. Hansı hesab əvvəlcədən aparılmalı idi?

:::reveal Cavab
- **Hesab:** bir host itəndən sonrakı tutum 112 GiB-dir, tələb 160 GiB; 48 GiB çatışmır. N+1 planı normal vəziyyətin 224 GiB cəminə əsaslana bilməz.
- **Tədbir:** kritik VM-lərin yaddaş tələbi təhlükəsiz şəkildə 112 GiB-ə endirilməli və ya bir host itəndən sonra ən azı 160 GiB qalacaq qədər tutum artırılmalıdır.
- Yalnız qeyri-kritik VM-ləri dayandırmaq 48 GiB çatışmazlığını aradan qaldırmır.
- CPU, disk və şəbəkə ehtiyatı ayrıca ölçülür; HA resurs yaratmır, mövcud resursda yenidən başlanmanı idarə edir.
:::

**Situasiya 4.** Kafedranın Kubernetes ad fəzasında tələbəyə Pod yaratmaq hüququ verilib. O, host qovluğunu qoşan imtiyazlı Pod təsviri təqdim edir. Administrator ad fəzası ayrı olduğu üçün təhlükə görmür. Hansı tədbirlər çatışmır?

:::reveal Cavab
- Ad fəzası bu parametrləri özlüyündə qadağan etmir.
- **Çatışan tədbirlər:** RBAC, Pod qəbul siyasəti (Pod Security Admission), host qovluğu və imtiyazlı rejim məhdudiyyətləri.
- Tətbiq root olmayan istifadəçi, azaldılmış capabilities və uyğun seccomp profili ilə işləməlidir.
- Şəbəkə çıxışı ayrıca siyasətlə məhdudlaşdırılır.
- Etibarsız tələbə kodu üçün ayrıca işçi mühit və ya VM səviyyəsində ayrılma qiymətləndirilir; adi konteyner sərhədi kifayət sayılmır.
:::

**Situasiya 5.** Kitabxananın test VM-ləri şablondan çoxaldılıb və hamısında eyni SSH host açarı, ortaq xidmət parolu var. Bir test maşınının diski tələbə qrupuna verilib. Hadisə yalnız həmin VM-ə aiddirmi?

:::reveal Cavab
- **Xeyr:** ortaq parol digər klonların da riskə düşdüyünü göstərir.
- Sirr bütün aidiyyəti xidmətlərdə dəyişdirilir, girişlər araşdırılır, host açarları fərdiləşdirilir.
- Şablon düzəldilir və ilk açılışda kimlik yaratma prosesi qurulur.
- Köhnə nüsxələrin kimdə olduğu inventardan yoxlanır.
- Yalnız paylaşılan VM-i silmək sızmış məlumatı geri qaytarmır və digər klonların eyni parolunu dəyişmir.
:::

**Situasiya 6.** LMS yalnız live migration-dan sonra əlçatmaz olub. Konsol işləyir, IP ünvanı düzgündür, şlüzdən cavab gəlmir. Komanda DNS serverini dəyişməyi və bütün hostları yenidən başlatmağı təklif edir. İlk yoxlamalar necə seçilməlidir?

:::reveal Cavab
- Əvvəl vNIC, port qrupu, hədəf hostun VLAN və uplink konfiqurasiyası yoxlanır, qonşu həlli müşahidə edilir; sağlam hostla müqayisə fərqi daraldır.
- Şlüzün qonşu ünvanının həll olunmadığı və ya IP yolunun pozulduğu təsdiqlənərsə, DNS dəyişikliyi nasazlığı düzəltməz.
- Təkcə ping cavabının gəlməməsi yolun işləmədiyini sübut etmir: ICMP siyasətlə bloklana bilər.
- Təsdiqlənmiş səbəb bir dəyişiklik ilə düzəldilir, sonra şəbəkə, TLS və tətbiq əməliyyatı yoxlanır.
- Restart yalnız əsaslandırılmış ehtiyac və qorunmuş sübutla seçilir.
:::

**Situasiya 7.** Universitetin hesablama VM-ində böyük analiz başlanandan sonra tələbə bazası ləngiyib. Bazanın CPU istifadəsi aşağıdır, hostda isə disk növbəsi artıb. Bazaya daha çox vCPU ayırmaq təklif olunur. Bu qərar əsaslıdırmı?

:::reveal Cavab
- **Xeyr:** müşahidə saxlama rəqabətinə (noisy neighbour) uyğundur; əlavə vCPU disk növbəsini aradan qaldırmaya bilər.
- Analiz yükünün I/O istifadəsi, ortaq hovuzun gecikməsi və snapshot fəaliyyəti ölçülür.
- İşin vaxtı dəyişdirilə, I/O məhdudiyyəti və kritik bazaya uyğun rezerv tətbiq edilə bilər.
- Düzəlişdən sonra sorğu gecikməsi normal yüklə müqayisə edilir.
- Qonşunun qəsdən hücum edib-etmədiyi ayrıca araşdırılır.
:::

**Situasiya 8.** Təhlükəsizlik analitiki universitetin ESXi hostunda riskli versiya görür. Şəbəkə administratoru idarəetmə VLAN-ı ayrıldığı üçün CVE-2025-22224 və CVE-2025-22225 düzəlişlərini təxirə salmağı istəyir. Ayrılma kifayətdirmi?

:::reveal Cavab
- **Xeyr:** ayrılma idarəetmə interfeysinə şəbəkə girişini azaldır, amma qonaqdan başlayan zəiflik zəncirini bütövlükdə bağlamır.
- Təsirlənən versiya və ilkin şərtlər istehsalçı bildirişindən yoxlanır, prioritetli yamaq planı hazırlanır.
- Ehtiyatlama, uyğunluq və köçürmə imkanları təsdiqlənərək hostlar növbə ilə yenilənir.
- İstismar şübhəsi varsa, yalnız versiyanı yeniləmək kifayət deyil: hostun və idarəetmə hesablarının bütövlüyü araşdırılır.
:::

## Konspektdən situasiyalar

**Situasiya K1.** Kibertəhlükəsizlik dərsində tələbələr zərərli proqram nümunələrini VirtualBox-da analiz edir. VM "bridged" rejimdədir və host ilə ortaq qovluq açıqdır. Laborant deyir: "VM-dir, heç nə olmaz." Risklər nədir və laboratoriyanı necə qurmaq lazımdır?

:::reveal Cavab
- **Risklər:** bridged rejimdə VM universitet şəbəkəsində real kompüter kimi görünür, qurd tipli zərərli proqram digər kompüterlərə yayıla bilər; ortaq qovluq vasitəsilə zərərli fayl hosta keçə bilər; Tip 2 hipervizor host ƏS-in zəifliklərindən asılıdır.
- **Düzgün quruluş:** tam daxili şəbəkə (host-only istifadə olunarsa, hosta giriş firewall ilə məhdudlaşdırılır), lazım olsa simulyasiya olunmuş İnternet (məs. INetSim).
- Ortaq qovluq, bufer və USB söndürülür.
- İşdən əvvəl təmiz snapshot, işdən sonra ona qayıtma.
- Analiz kompüterləri ayrıca VLAN-da və real məlumatsız olur.
:::

**Situasiya K2.** Universitetin bir fiziki serveri çöküb və onun üzərindəki 8 VM (sayt, poçt, tələbə sistemi) 6 saat işləməyib. Rəhbərlik soruşur: "Bizə virtuallaşdırmanın etibarlılıq verdiyini demişdiniz?" Nə cavab verərdin?

:::reveal Cavab
- Virtuallaşdırma etibarlılıq üçün **imkan** verir, özü-özlüyündə zəmanət vermir; tək host ortaq nasazlıq sahəsidir.
- **Tələb olunanlar:** HA klaster (ən azı iki host, ortaq yaddaş və ya replikasiya), digər hostlarda ehtiyat tutum, kritik VM-lərin fərqli hostlara yayılması.
- RTO/RPO hədəflərinin müəyyən edilməsi və müntəzəm sınaq.
- Bu insident həmin tədbirlərin büdcəsini əsaslandırmaq üçün istifadə edilməlidir.
:::

**Situasiya K3.** İT komandası tələbə sisteminin bazasını gündəlik snapshot-larla "ehtiyatlayır", snapshot-lar eyni yaddaş massivindədir. Üstəlik yeni VM-lər bir il əvvəl hazırlanmış şablondan klonlanır, şablonda admin parolu yazılıb. Hansı problemləri görürsən?

:::reveal Cavab
- **Birincisi:** snapshot ehtiyat nüsxə deyil; massiv sıradan çıxsa və ya ransomware hipervizoru şifrələsə, snapshot-lar da itir. Ayrı yerdə, ayrıca idarə olunan, dəyişdirilə bilməyən ehtiyat nüsxələr (3-2-1) və bərpa testləri lazımdır.
- **İkincisi:** köhnə şablon bir illik yamaqları daşımır və içindəki parol bütün klonlarda eynidir: biri sızsa hamısı açılır.
- **Tədbir:** şablon müntəzəm yenilənir, sirlər imicdən çıxarılır, hər VM-də unikal parol (və ya mərkəzi sirr meneceri) olur.
:::

## Ehtimal olunan əlavə suallar

:::reveal Hipervizor (VMM) nədir və VM, host və qonaq ƏS anlayışları necə bağlıdır?
- Fiziki kompüter host, VM daxilindəki ƏS qonaq ƏS-dir. VM öz ƏS və tətbiqləri olan məntiqi kompüterdir.
- Hipervizor, yəni virtual maşın monitoru (VMM), qonaqlara resurs ayırır və aparat üzərindəki əməliyyatlarını nəzarətdə saxlayır.
- Müasir hipervizorlar bütün avadanlığı proqramla təqlid etmir, prosessorun aparat dəstəyindən (Intel VT-x, AMD-V) istifadə edir.
:::

:::reveal Virtual maşın ilə konteyneri müqayisə edin.
| Meyar | VM | Konteyner |
| --- | --- | --- |
| Nüvə | Hər qonağın öz nüvəsi | Host nüvəsi paylaşılır |
| Sərhəd | Virtual aparat və hipervizor | Nüvə mexanizmləri və icra mühiti |
| Paketləmə | ƏS, tətbiqlər, disklər | Tətbiq və asılılıqlar |
| Qalıq risk | Escape, ortaq host, resurs rəqabəti | Ortaq nüvə zəifliyi, geniş səlahiyyətlər |

VM avadanlığı, konteyner əməliyyat sistemini virtuallaşdırır. Konteynerlər VM daxilində də yerləşdirilə bilər: müxtəlif etibar səviyyəli fakültələr ayrı VM-lərdə, onların xidmətləri konteynerlərdə.
:::

:::reveal Snapshot ilə ehtiyat nüsxənin fərqini cədvəllə izah edin.
| | Snapshot | Replikasiya | Ehtiyat nüsxə |
| --- | --- | --- | --- |
| Nədir | VM-in müəyyən anda vəziyyəti, eyni yaddaşda | Başqa yerə davamlı surət | Ayrı yerdə müstəqil nüsxə |
| Nə üçün | Qısa geri qayıtma | Tez bərpa (RTO-nu azaldır) | Silinmə, ransomware, fəlakət |
| Zəiflik | Disk/host itsə itir; uzun saxlansa performans düşür | Şifrələnmiş/silinmiş məlumatı da surətləyir | Bərpa testi edilməyibsə işləyəcəyi bilinmir |

3-2-1: 3 nüsxə, 2 daşıyıcıda, 1-i başqa yerdə, biri immutable və ya oflayn.
:::

:::reveal Virtual mühitin əsas təhlükəsizlik risklərini sadalayın və hər birinə tədbir göstərin.
- **VM escape:** yamaqlar, lazımsız virtual qurğuların (USB, ortaq qovluq, bufer) söndürülməsi.
- **İdarəetmə müstəvisinin ələ keçirilməsi:** ayrıca VLAN, MFA, RBAC, auditlənən giriş, internetdən əlçatmazlıq.
- **VM sprawl:** VM uçotu, sahib və müddət, avtomatik təmizləmə.
- **Köhnə imic və şablonlar:** yenilənən, gücləndirilmiş şablonlar; sirlərin imicdən çıxarılması.
- **Resurs rəqabəti:** limit və rezerv.
- **Yan kanallar:** mikrokod və hipervizor yamaqları, kritik VM-lərin ayrılması.
- **Ortaq nasazlıq sahəsi:** HA klaster, VM-ləri fərqli hostlara yaymaq, ehtiyat tutum.
:::

:::reveal "VM-lər bir-birindən tamamilə təcrid olunur" iddiası niyə yanlışdır?
- Hipervizor zəiflikləri (VM escape), resurs rəqabəti (noisy neighbour), yan kanallar (Spectre, Meltdown) və host nasazlığı bütün VM-lərə təsir edə bilər.
- Birbaşa icazəsiz çıxış məhdudlaşdırılır, amma ortaq host, hipervizor, disk və prosessor riskləri qalır.
:::

:::reveal Yaddaş (RAM) və disk üçün hesablama: overcommit və thin provisioning nümunələrini həll edin.
- **vCPU:** 24 fiziki nüvə (SMT söndürülüb), 4 VM × 8 vCPU = 32 vCPU. Qadağan deyil, amma hamı eyni vaxtda işləyəndə növbə yaranır.
- **RAM:** 128 GiB − 16 GiB (hipervizor) = 112 GiB; 4 × 24 = 96 GiB təyin olunub, 16 GiB ehtiyat qalır (tutum sərhədidir, real işçi dəsti ölçmür).
- **Thin provisioning:** hovuz 500 GiB, 4 × 200 = 800 GiB görünür, faktiki istifadə 300 GiB ola bilər; hovuzun dolmayacağına zəmanət yoxdur, snapshot və nüsxə üçün də yer lazımdır.
- **N+1:** 3 host × 112 = 336 GiB; tələbat 240 GiB sığır; bir host itəndə 224 GiB qalır, 16 GiB çatışmır.
:::

:::reveal VLAN nədir və niyə təhlükəsizlik sərhədi sayılmır?
- VLAN məntiqi Ethernet seqmentidir; IEEE 802.1Q etiketi çərçivənin hansı VLAN-a aid olduğunu göstərir. Access port bir VLAN-ın etiketsiz, trunk icazəli VLAN-ların etiketli trafikini daşıyır.
- VLAN şifrələmə deyil; VLAN-lar arasında qaydasız marşrutlaşdırma varsa fərqli adlar trafiki qorumur.
- Eyni VLAN-da yerləşmə etibar səbəbi deyil: mikroseqmentasiya və ya paylanmış firewall tətbiq olunur.
:::

:::reveal Konteyner təhlükəsizliyində təchizat zənciri və işləmə səlahiyyətləri üzrə əsas tədbirləri sadalayın.
- **Təsvir:** minimal baza, versiya nəzarəti, SBOM, zəiflik skanı (təmiz nəticə zərərsizlik sübutu deyil), imza və digest yoxlaması, reyestrə yazma hüququnun məhdudlaşdırılması.
- **Sirlər:** Dockerfile-da yazıb silmək etibarsızdır (qatlarda qalır); təsvirdə real data olmur; zəif paket təsvir yenidən qurularaq düzəldilir.
- **İşləmə:** `--privileged`, kök qovluq qoşulması və Docker socket-dən qaçınmaq, root olmayan istifadəçi, capabilities azaltmaq, seccomp, AppArmor/SELinux, rootless icra.
- **Kubernetes:** RBAC, Pod Security Admission, Secret-in şifrələnməsi (base64 şifrələmə deyil), NetworkPolicy.
:::

:::reveal İdarəetmə müstəvisini (management plane) necə sərtləşdirmək olar?
- Tələbə və qonaq şəbəkələrindən ayırmaq, internetə açmamaq; admin idarə olunan stansiyadan VPN və keçid hostu ilə girir.
- Fərdi hesab, MFA, RBAC; rolların bölgüsü (operator VM yaradır, baza diskini ixrac edə bilmir).
- Ən yüksək hüquqlar gündəlik hesabdan ayrılır, xidmət hesabları daraldılır, fövqəladə giriş hesabı xəbərdarlıq yaradır.
- Audit: giriş, rol dəyişikliyi, VM yaradılması, snapshot, disk ixracı, konsol; qeydlər hostdan kənara göndərilir, SIEM kontekstə bağlanır.
:::
