+++
title = "Virtuallaşdırmanın əsasları və təhlükəsizliyi"
unit = "orta"
order = 13
summary = "Hər anlayış 1–3 cümlə ilə: hipervizorlar, resurslar, virtual şəbəkələr, snapshot və bərpa, konteynerlər, təhdidlər, sərtləşdirmə və diaqnostika."
updated = 2026-11-09

[[source]]
title = "Mühazirə 13: Virtuallaşdırmanın əsasları və təhlükəsizliyi"
note = "Elmar Cabbarov, 2026–2027"
+++

Virtuallaşdırma (virtualization) fiziki hesablama resursunu proqramlara məntiqi resurs kimi təqdim edir. Paylaşma səmərəlilik verir, ayırma isə bir mühitin digərinə icazəsiz təsirini məhdudlaşdırır; ikisi birlikdə düşünülür. Universitet topologiyası, VLAN nömrələri və GiB hesabları şərti tədris nümunəsidir.

## Virtuallaşdırma nədir

Virtual maşın (virtual machine, VM) öz əməliyyat sistemi və tətbiqləri olan məntiqi kompüterdir. Fiziki kompüter host, VM-in ƏS-i qonaq ƏS adlanır. Hipervizor (hypervisor), yəni virtual maşın monitoru (virtual machine monitor, VMM), qonaqlara resurs ayırır və aparat üzərindəki əməliyyatlarını nəzarətdə saxlayır.

Konsolidasiya (consolidation) tətbiqləri daha az fiziki hostda toplayır: pik yükləri eyni vaxta düşməyən xidmətlər (kafedra saytı gündüz, LMS imtahan günü) ortaq hovuzdan qənaət edir. Qənaət faizi universal deyil. Tələ: üç VM bir hostda olsa, host çökəndə üçü birlikdə dayanır; yüksək əlçatanlıq (high availability, HA) və ehtiyat tutum ayrıca xərcdir. Digər faydalar: şablondan sürətli yerləşdirmə, mərkəzi idarə, klasterləşmə, tədris mühitinin ayrılması.

Virtuallaşdırılan obyektlər (etibar sərhədləri fərqlidir):

| Obyekt | Görünüş |
| --- | --- |
| Virtual maşın | Öz nüvəsi olan kompüter |
| Konteyner (container) | Ayrılmış proses və fayl mühiti |
| Virtual şəbəkə | Məntiqi portlar, seqmentlər, marşrutlar |
| Saxlama (storage virtualization) | Fiziki disklərdən məntiqi həcm |
| Verilənlər (data virtualization) | Mənbələr üzərində vahid sorğu görünüşü |

:::warning Qarışdırma
Yaddaşın virtual ünvanlanması ilə saxlama virtuallaşdırılması fərqlidir. VM daxilində baza işləməsi verilənlərin virtuallaşdırılması deyil.
:::

VM-in dörd xüsusiyyəti şərtlidir:

- **İnkapsulyasiya (encapsulation):** VM fayllarla təsvir olunur və köçürülür; amma disk faylı təkbaşına çox vaxt kifayət etmir (şifrələmə açarı, virtual firmware, əlavə disklər, RAM vəziyyəti).
- **İzolyasiya (isolation):** bir VM digərinin yaddaşına birbaşa çıxa bilmir; ortaq host, hipervizor, disk və prosessor riskləri qalır, yəni tam təcrid yoxdur.
- **Uyğunluq (compatibility):** standart virtual qurğular, amma prosessor arxitekturası, sürücü və lisenziya ilə məhduddur.
- **Avadanlıqdan nisbi müstəqillik:** birbaşa verilmiş GPU və ya şəbəkə qurğusu daşınmanı məhdudlaşdırır.

## Hipervizorların arxitekturası

Birinci tip (type 1, bare metal) hipervizor avadanlıq üzərində nəzarəti özü qurur: VMware ESXi, Xen. İkinci tip (type 2, hosted) adi host ƏS üzərində proqram kimi işləyir: VirtualBox, VMware Workstation. Hyper-V birinci tipdir (Windows kök bölmədir). KVM Linux nüvəsinə virtuallaşdırma əlavə edir, birinci tip kimi təsnif olunur, QEMU virtual qurğuları tamamlayır. Proxmox VE KVM və konteynerləri idarə edən platformadır, ayrıca hipervizor deyil.

| Meyar | Birinci tip | İkinci tip |
| --- | --- | --- |
| Yerləşmə | Avadanlıq üzərində | Host ƏS üzərində |
| İstifadə | Klaster, istehsalat, VDI | Laboratoriya, test, tədris |
| Təhlükəsizlik | İdarəetmə və yamaqlar | Host ƏS də qorunur |

:::exam Tələ
Birinci tip avtomatik təhlükəsiz, ikinci tip avtomatik zəif deyil: internetə açıq yamanmamış ESXi yenilənmiş laboratoriya noutbukundan riskli ola bilər. Performans da mütləq deyil. Birinci tip üçün ayrıca idarəetmə kompüteri məcburi deyil, bu təhlükəsizlik seçimidir.
:::

Virtual iş masası infrastrukturu (virtual desktop infrastructure, VDI) iş masasını məlumat mərkəzindəki VM-də saxlayır, istifadəçi uzaq görüntü ilə qoşulur. Riskləri: ekran görüntüsü, hesab oğurluğu, bufer/USB yönləndirilməsi, sessiya kəsiləndə itən iş.

## Virtuallaşdırma üsulları və imtiyazlar

- **Tam virtuallaşdırma (full virtualization):** qonağa tam virtual aparat interfeysi verilir, dəyişdirilməsi tələb olunmur. Tarixən problemli təlimatlar ikili çevirmə (binary translation) ilə dəyişdirilirdi. Aparat dəstəyi ilə birlikdə də işləyə bilər, bunlar bir-birini istisna etmir.
- **Emulyasiya (emulation):** başqa maşının davranışını proqramla təqlid edir (QEMU); uyğunluğu genişləndirir, performansa xərc qoyur.
- **Paravirtuallaşdırma (paravirtualization):** qonaq virtual olduğunu bilir və hipervizora hypercall göndərir. Paravirtual sürücülər (virtio) tam virtual VM-də də işləyir; qonaqda sürücü yoxdursa açılış diski görünməyə bilər.
- **Aparat dəstəyi:** Intel VT-x, AMD-V. İmtiyaz halqaları (protection rings): tətbiq ring 3, nüvə ring 0. Intel-də VMX root və non-root rejimləri ring nömrəsinin davamı deyil; ring −1 şərti addır, rəsmi halqa deyil. Nəzarət tələb edən hadisədə VM çıxışı (VM exit) baş verir, hipervizor yoxlayıb qonağı davam etdirir; adi hesablama birbaşa CPU-da gedir.
- **IOMMU** (Intel VT-d, AMD-Vi) qurğuların birbaşa yaddaş girişini ünvan çevirməsi ilə məhdudlaşdırır; VT-x/AMD-V ilə eyni deyil. İç-içə virtuallaşdırma (nested virtualization) VM daxilində hipervizor işlətməyə imkan verir, hücum səthi və performans ayrıca qiymətləndirilir.

## Virtual resurslar

**Prosessor.** Virtual prosessor (virtual CPU, vCPU) qonağın gördüyü icra vahididir; 8 vCPU 8 müstəsna nüvə demək deyil. Resursların artıq təyini (overcommit) virtual cəminin fiziki tutumu keçməsidir: hamı eyni vaxtda işləyəndə növbə yaranır, qonaqda CPU aşağı görünsə də gözləmə yüksək ola bilər (CPU ready, steal time). Rezerv (reservation) əlçatanlığı qoruyur, limit (limit) yuxarı həddi qoyur, pay (share) rəqabətdə üstünlük verir.

**Yaddaş.** Qonaq virtual ünvanı qonağın fiziki ünvanına, hipervizor hostun fiziki yaddaşına çevirir; Intel EPT və AMD NPT bunu sürətləndirir. Balloon sürücüsü qonaqdan səhifə alıb fiziki yaddaşı başqa VM-lərə verir; təzyiq davam edərsə səhifələmə diskə düşür və baza sorğuları ləngiyir. NUMA-da çox böyük VM uzaq yaddaşa müraciət edə bilər.

**Disk.** Virtual disk blok qurğusu kimi görünür; hovuza NFS və iSCSI ilə çatmaq olar, saxlama şəbəkəsinin gecikməsi qonaqda disk gecikməsi kimi görünür. Qalın ayrılmada (thick provisioning) həcm əvvəlcədən rezerv edilir; nazik ayrılmada (thin provisioning) yazıldıqca tutulur, ona görə görünən cəm fiziki hovuzu keçə bilər (800 GiB görünür, 500 GiB hovuz). RAID disk nasazlığına dözür, amma silinməni və şifrələnməni geri qaytarmır; əsas VM və nüsxələr eyni massivdədirsə, hücumçu hər ikisini poza bilər.

**Verilənlər.** Verilənlərin virtuallaşdırılmasında (data virtualization) vasitəçi qat mənbələri vahid görünüşdə birləşdirir; əsas risk səlahiyyətlərin uyğunlaşdırılmasıdır (mənbədəki sətir/sütun məhdudiyyətləri qorunmalıdır) və zaman uyğunsuzluğudur.

## Virtual şəbəkələr

Virtual şəbəkə interfeysi (virtual network interface card, vNIC) VM-i virtual kommutatora (virtual switch, vSwitch) bağlayır; fiziki şəbəkəyə çıxış uplink ilədir. Eyni hostdakı VM-lər arasında trafik uplink-ə çıxmır, ona görə yalnız uplink-dəki IDS və firewall onu görmür: virtual firewall, mikroseqmentasiya (microsegmentation) və ya host sensoru lazımdır.

:::figure
src = "m13-2.png"
alt = "VM-lər vNIC ilə vSwitch-ə, oradan uplink və trunk ilə fiziki kommutatora, VLAN-lar arasında isə firewall-a qoşulur."
caption = "Virtual portlardan fiziki şəbəkəyə gedən yol."
:::

VLAN məntiqi Ethernet seqmentidir; IEEE 802.1Q etiketi çərçivənin VLAN-ını göstərir. Access port bir VLAN-ın etiketsiz, trunk icazəli VLAN-ların etiketli trafikini daşıyır. VLAN şifrələmə deyil: VLAN-lar arası qaydasız marşrut varsa fərqli ad qorumur. Şərti plan: VLAN 10 hipervizor idarəetməsi, 20 LMS tətbiqləri, 30 bazalar, 40 ehtiyat nüsxə, 50 laboratoriya.

| Rejim | Əlaqə | Risk |
| --- | --- | --- |
| Körpü (bridged) | Fiziki seqmentlə, real kompüter kimi | VM kampus şəbəkəsinə çıxır |
| NAT | Host IP-si arxasından çıxış | Çıxış hücumları və sızma |
| Host-only | Host və həmin VM-lər | Hosta hücum |
| Daxili (internal network) | Yalnız seçilmiş VM-lər | İkinci interfeys, hipervizor zəifliyi; zərərli proqram təhlili üçün ən uyğun |

Şərq–qərb trafiki (east-west traffic) VM və xidmətlər arasındadır, şimal–cənub trafiki (north-south traffic) mühitə girib-çıxandır. Mikroseqmentasiya qaydaları tətbiqin roluna qədər daraldır; eyni VLAN-da olmaq etibar səbəbi deyil. Virtual portda MAC dəyişməsi, saxta trafik və promiscuous rejim siyasətlə idarə olunur; trafik güzgüləndikdə şəxsi məlumat səbəbi ilə sensor qeydlərinə giriş məhdudlaşdırılır.

## Həyat dövrü: şablon, snapshot, köçürmə

Şablon (template) təkrar VM üçün baza təsviridir; klon (clone) onun nüsxəsidir (tam klon öz diskinə malikdir, əlaqəli klon baza diskdən asılıdır). Şablonda real data, SSH açarı, ortaq parol qalmır; ilk açılışda kimlik fərdiləşdirilir (Windows-da Sysprep, Linux-da cloud-init). Şablon söndürülmüş halda da köhnəlir, ayrıca yamaq dövrünə girir.

Snapshot (snapshot) müəyyən vəziyyətə qayıtmaq nöqtəsidir: yazılar ayrıca fərq qatına gedir, baza diskdən asılıdır. Yeniləmədən əvvəl qısa müddət üçündür; baza ayrı VM-dədirsə tək VM-i geri çevirmək uyğunsuzluq yaradır, köhnə snapshot sızmış parolu qaytarır, uzun zəncir performansı düşürür, faylını əllə silmək VM-i poza bilər. Qəza uyğunluğu (crash consistency) qəfil enerji kəsilməsinə bənzəyir; tətbiq uyğunluğu (application consistency) buferləri və tranzaksiyaları nəzərə alır (Windows VSS və s., bazada istehsalçının üsulu).

| Üsul | Məqsəd | Zəiflik |
| --- | --- | --- |
| Snapshot | Qısa geri qayıtma | Eyni yaddaşda, disk itsə itir |
| Klon | Test, tədris | Köhnə sirlər köçür |
| Replikasiya (replication) | Tez bərpa, RTO-nu azaldır | Silinməni və şifrələnməni də köçürür |
| Ehtiyat nüsxə (backup) | Silinmə, ransomware, fəlakət | Bərpa sınağı olmalıdır |

:::exam Tələ
Snapshot ehtiyat nüsxə deyil. İşləyən VM fayllarını adi kopyalamaq uyğunsuz nüsxə verə bilər: VM söndürülür və ya hipervizorun ehtiyatlama interfeysi işlədilir.
:::

:::steps İşlək köçürmə (live migration), pre-copy
[[step]]
title = "İlkin surət"
body = "Yaddaşın ilkin surəti ötürülür, VM işləyir."

[[step]]
title = "Dəyişmiş səhifələr"
body = "İşləmə zamanı dəyişən səhifələr təkrar göndərilir."

[[step]]
title = "Qısa dayandırma və davam"
body = "Qalan vəziyyət qısa dayandırma ilə ötürülür, qonaq hədəfdə davam edir."
:::

Köçürmə sıfır fasilə zəmanəti deyil; yaddaş çox sürətlə dəyişirsə uzanır, nasaz hostdan RAM köçürülmür. Kanalda açıq yaddaş və açarlar ola bilər: kanal ayrılır, autentifikasiya və şifrələmə aktiv edilir. Hədəfdə VLAN, firewall və saxlama siyasətləri qorunmalıdır, hostların CPU və virtual qurğu uyğunluğu yoxlanır.

## Klaster, HA və bərpa

Klaster hostları əlaqələndirir, HA nasaz hostun VM-lərini başqa hostda yenidən başladır (qonaq və tətbiq təkrar açılır, RAM-da saxlanmamış data itə bilər). N+1 planında bir host itəndən sonra kritik yükün sığması hesablanır: üç hostda 336 GiB tutumdan biri itəndə 224 GiB qalır, 240 GiB tələbatı ödəmir. Ayırma qaydası (anti-affinity) replikaları fərqli hostlara yayır; ortaq elektrik, kommutator, massiv yenə ortaq risk qalır. Kvorum və fencing parçalanmış qrupların eyni məlumatı zidd dəyişməsini önləyir.

RTO (recovery time objective) xidmətin qaytarılma müddətidir, RPO (recovery point objective) qəbul edilən məlumat itkisidir. RPO 15 dəqiqə olan bazaya gecəlik nüsxə kifayət etmir. 3-2-1 qaydası: 3 nüsxə, 2 daşıyıcı, 1 başqa yerdə, ən azı biri oflayn və ya dəyişdirilə bilməyən; ehtiyatlama hesabı admin hesabından ayrı olur, açarların bərpası da sınanır. Bərpa testi ayrılmış şəbəkədə aparılır (ünvan toqquşması olmasın), əvvəl bütövlük, sonra xidmət funksiyası yoxlanır.

## Konteynerlər

Konteyner tətbiqi və asılılıqlarını ayrı proses mühitində işlədir, host nüvəsini paylaşır; VM-in öz nüvəsi var. Konteyner təsviri (image) tətbiq və kitabxanalardan ibarətdir, davamlı məlumat ayrıca həcmdə (volume) saxlanır. Sürətli başlanma dərhal hazırlıq demək deyil. Windows/macOS-da Linux konteyner alətləri çox vaxt Linux VM işlədir.

| Meyar | VM | Konteyner |
| --- | --- | --- |
| Nüvə | Hər qonağın öz nüvəsi | Paylaşılır |
| Sərhəd | Virtual aparat, hipervizor | Nüvə mexanizmləri |
| Qalıq risk | Escape, rəqabət | Ortaq nüvə zəifliyi, geniş səlahiyyət |

Ad fəzası (namespace) prosesə ayrılmış görünüş verir (PID, mount, network, user); nəzarət qrupları (control groups, cgroups) CPU və yaddaşı hesablayıb məhdudlaşdırır. Biri görünüşü ayırır, o biri resursu məhdudlaşdırır; ikisi bütün təhlükəsizliyi həll etmir. Kubernetes ad fəzası Linux network namespace-dən fərqli olaraq API obyektlərini qruplaşdırır. Etibarsız kod üçün adi konteyner tam təcrid sayılmır, ayrıca VM seçilir.

Docker təsvirləri qurur və konteyneri başladır; reyestr (registry) təsvirləri saxlayır, etiket (tag) başqa təsvirə keçirilə bilər, digest konkret təsviri müəyyən edir (bütövlüyü yoxlayır, müəllifi sübut etmir). Dockerfile təsvirin qurulma reseptidir. Kubernetes istənən vəziyyəti idarə edir: Pod ən kiçik vahiddir, Deployment replikaları idarə edir, Service sabit ünvan verir, Ingress xarici HTTP-yə yol açır; API server, planlaşdırıcı, nəzarətçilər və etcd idarəetmə müstəvisidir, işçi düyündə kubelet və icra mühiti (runtime) işləyir. Readiness hazırlığı, liveness yenidən başlatma ehtiyacını yoxlayır; yanlış liveness vəziyyəti ağırlaşdıra bilər.

## Təhdidlər və məlum zəifliklər

| Təhdid | Mahiyyət | İlkin müdafiə |
| --- | --- | --- |
| VM escape | Qonaqdan hipervizora/hosta çıxış | Yamaq, lazımsız qurğuları (USB, ortaq qovluq, bufer) söndürmək |
| İdarəetmə müstəvisinin (management plane) ələ keçirilməsi | Admin hesabı ilə VM silmək, disk ixracı, ESXi-yə ransomware | Ayrıca VLAN, MFA, RBAC, audit |
| VM sprawl | Unudulmuş, yamanmayan VM-lər | İnventar, sahib, son tarix |
| Köhnə imic/şablon | Hər klon eyni zəifliyi daşıyır | Yenilənən şablon, sirsiz imic |
| Snapshot sızması | Disk və RAM nüsxəsi oğurlanır | Giriş məhdudiyyəti, şifrələmə |
| Resurs rəqabəti | Səs-küylü qonşu (noisy neighbour) | Limit, rezerv |
| Yan kanal (side channel) | Ortaq CPU keşi | Mikrokod və hipervizor yamaqları |
| Ortaq nasazlıq sahəsi | Host çöküşü | HA, yayılma, ehtiyat tutum |

Hyperjacking hipervizorun ələ keçirilməsi və ya gizli hipervizor yerləşdirilməsidir; tək VM-i yenidən qurmaq kifayət etmir, firmware və açılış zənciri də yoxlanır. Spectre və Meltdown (2018) spekulyativ icra yan kanallarıdır: eyni zəiflik deyil, təsir prosessor və yamaqlardan asılıdır, tək sazlama hamısını bağlamır.

- **VENOM (CVE-2015-3456):** QEMU virtual disket nəzarətçisində yaddaş daşması; köhnə virtual periferiya da hücum səthidir.
- **ESXiArgs (2023):** yamanmamış, əlçatan ESXi-yə ransomware, OpenSLP (CVE-2021-21974) ilə əlaqələndirilib; CISA bərpa təlimatı müstəqil nüsxəni əvəz etmir.
- **CVE-2025-22224/22225/22226 (2025):** VMX-də yaddaş pozuntusu, ESXi-də VMX-dən hipervizora ixtiyari yazma, məlumat açıqlanması; CISA kataloqundadır. İdarəetmə VLAN-ı kifayət deyil, hipervizor yamanmalıdır.

## Sərtləşdirmə

NIST SP 800-125 (2011) tam virtuallaşdırmanı, NIST SP 800-190 konteynerləri əhatə edir; biri digərinin əvəzi deyil. Hipervizor minimal quraşdırılır: köhnə qurğu, USB, ortaq bufer və qovluq bağlanır; Secure Boot dəstəklənirsə işlədilir. Yamaq firmware, mikrokod, hipervizor, idarəetmə serveri, qonaq alətləri və qonaq ƏS-ni əhatə edir; sınaq hostundan başlanır, riskli zəiflikdə sürətləndirilir. Dəstəkdən çıxmış qonaq ƏS ayrıca risk: Windows 10 adi dəstəyi 14 oktyabr 2025-də bitib, ESU avtomatik deyil.

İdarəetmə müstəvisi tələbə şəbəkələrindən ayrılır, internetə açılmır; admin VPN ilə keçid hostu (jump host) üzərindən girir. Şəbəkə ayrılması hesab nəzarətini əvəz etmir: fərdi hesab, çoxamilli autentifikasiya (MFA) və rol əsaslı giriş nəzarəti (RBAC). Rollar bölünür (operator VM yaradır, amma baza diskini ixrac edə bilmir). Qeydə alınır: giriş, rol dəyişikliyi, VM yaradılması, snapshot, disk ixracı; qeydlər hostdan kənara göndərilir. SIEM yalnız uğursuz girişi sayırsa, qanuni hesabla disk ixracını qaçırar. İnsident şübhəsində restart RAM sübutunu itirə bilər; NIST SP 800-61 Rev. 3 cavab planı üçündür.

## Konteyner təhlükəsizliyi

Təsvir minimal baza ilə qurulur, proqram komponentlərinin siyahısı (software bill of materials, SBOM) hazırlanır; zəiflik skanı təmiz olsa da məntiq zərərsiz sayılmaz; imza və digest ilə təsdiqli mənbə yoxlanır. Sirr Dockerfile-a yazılıb sonra silinməz (qatlarda qalır). Zəif paket konteynerdə əllə yox, təsvir yenidən qurularaq düzəldilir.

İşləmə: root olmayan istifadəçi, `--privileged`, kök qovluğun qoşulması və Docker socket ciddi əsaslandırma tələb edir. Linux capabilities azaldılır, seccomp sistem çağırışlarını süzür, AppArmor və SELinux davranışı məhdudlaşdırır, rootless icra imtiyazı azaldır, nüvə zəifliyini aradan qaldırmır. Şərti nümunə: `--cap-drop ALL`, `--read-only`, `--network none`, yaddaş, CPU və proses limitləri.

Kubernetes-də RBAC xidmət hesabına minimal hüquq verir; Pod Security Admission riskli Pod parametrlərini məhdudlaşdırır; Secret-də base64 şifrələmə deyil. NetworkPolicy seçilmiş Pod-lara icazəli trafiki bildirir (məsələn lms-db yalnız lms-api-dən TCP 5432); tətbiq edən plaqin lazımdır, icazələr birləşir, çıxışı özü məhdudlaşdırmır. Ad fəzası təkbaşına şəbəkə sərhədi deyil.

## Diaqnostika

Əvvəl sərhəd ölçülür (kimə, haradan, nə vaxtdan, son dəyişiklik, müqayisə nöqtəsi), şikayət texniki nəticədən ayrılır. Yol çəkilir: müştəri, kommutator, firewall, uplink, vSwitch, vNIC, tətbiq; OSI və TCP/IP qatları ilə aşağıdan yuxarı yoxlanır. Ardıcıllıq: əhatə, fiziki yol, virtual bağlantı, IP və DHCP, VLAN və marşrut, nəqliyyat və siyasət (TCP/UDP), DNS və tətbiq (TLS), resurs və qeydlər, bir fərziyyə bir dəyişiklik ilə təsdiq.

- Bir hostdakı bütün VM-lər təsirlənibsə uplink və vSwitch, yalnız biri isə vNIC, port qrupu və sürücü şübhəlidir. Live migration-dan sonra hədəfdə port qrupunun eyni VLAN-a bağlandığı, uplink-də VLAN siyahısı, MTU (kiçik paket keçməsi böyüyün keçəcəyini sübut etmir) yoxlanır.
- Alətlər: ip, ping, traceroute, ss, dig, curl, Windows-da ipconfig, tracert, netstat, Test-NetConnection. ping ICMP əlçatanlığını göstərir, veb xidməti yox; cavabsızlıq söndüyünü sübut etmir. ss/netstat dinləyən portu göstərir (127.0.0.1-ə bağlı xidmət şəbəkədən görünmür). Yanlış maska və DHCP toqquşması fasiləli nasazlıq yaradır.
- Jurnallar eyni zaman xəttində tutuşdurulur; nəzarətli təcridetmədə bir fərziyyə seçilir, bir dəyişən dəyişir. Bütün firewall-u söndürmək və ya klasteri restart etmək səbəbi gizlədir.

:::reveal Köçürmədən sonra LMS açılmır, konsol işləyir, şlüz cavab vermir. Nə yoxlanır?
Əvvəl əhatə (yalnız bu VM), sonra vNIC və port qrupu, hədəf hostun VLAN və trunk siyahısı. Nümunədə host B-nin trunk portunda VLAN 20 icazəli deyil: yalnız həmin siyahı düzəldilir, sonra şlüz, TCP 443, DNS və tələbə əməliyyatı yoxlanır. DNS dəyişmək və ya hamını restart etmək əsassızdır. Eskalasiya paketinə topologiya, versiyalar, vaxt, müşahidələr və rədd edilmiş fərziyyələr yazılır.
:::
