+++
title = "Virtuallaşdırmanın əsasları və təhlükəsizliyi"
unit = "qisa"
order = 13
summary = "Mühazirənin skeleti: hər anlayış bir-iki cümlə ilə, mühazirənin ardıcıllığında."
updated = 2026-11-09

[[source]]
title = "Mühazirə 13: Virtuallaşdırmanın əsasları və təhlükəsizliyi"
note = "Elmar Cabbarov, 2026–2027"
+++

Virtuallaşdırma (virtualization) fiziki resursu proqramlara məntiqi resurs kimi təqdim edir: paylaşma səmərəlilik, ayırma isə mühitlər arasında məhdudlaşdırma verir. Universitet nümunələri şərtidir: məsələn, LMS xidməti bir Linux VM-də, tələbə bazası başqa VM-də işləyir, hər ikisi eyni fiziki serverdədir, amma ayrı disk, hesab və şəbəkə siyasətinə malikdir. Mövzunun məqsədi: fiziki resurs ilə virtual təqdimat arasındakı əlaqəni izah etmək, hipervizor və üsulları ayırmaq, VM ilə konteyner üçün etibar sərhədini göstərmək, snapshot ilə ehtiyat nüsxəni fərqləndirmək, idarəetmə girişini məhdudlaşdırmaq və nasazlığı ardıcıl təcrid etməkdir.

## Virtuallaşdırma nədir

| Anlayış | Nədir |
| --- | --- |
| Virtual maşın (virtual machine, VM) | Öz ƏS və tətbiqləri olan məntiqi kompüter; fiziki kompüter host, VM-in ƏS-i qonaq ƏS |
| Hipervizor (hypervisor), VMM (virtual machine monitor) | Qonaqlara resurs ayıran və aparat əməliyyatlarına nəzarət edən təbəqə |
| Konsolidasiya (consolidation) | Tətbiqləri daha az hostda toplamaq; qənaət faizi universal deyil, host çökəndə hamısı dayanır |
| HA (high availability) | Nasaz hostun VM-i başqa hostda yenidən başlayır; ayrıca sazlanır |
| Obyektlər | VM, konteyner (container), virtual şəbəkə, saxlama (storage virtualization), verilənlər (data virtualization) |

Yaddaşın virtual ünvanlanması saxlama virtuallaşdırılması deyil; VM daxilində baza işləməsi verilənlərin virtuallaşdırılması deyil.

Dörd xüsusiyyət şərtlidir: inkapsulyasiya (encapsulation, VM fayllarla təsvir olunur, amma disk faylı təkbaşına kifayət etmir), izolyasiya (isolation, tam təcrid yoxdur, ortaq host riskləri qalır), uyğunluq (compatibility, arxitektura və lisenziya məhdudlaşdırır), avadanlıqdan nisbi müstəqillik (birbaşa GPU daşınmanı məhdudlaşdırır).

## Hipervizorlar

- **Birinci tip (type 1, bare metal):** avadanlıq üzərində; VMware ESXi, Xen, Hyper-V (Windows kök bölmədir), KVM (Linux nüvəsinə əlavə, QEMU qurğuları tamamlayır).
- **İkinci tip (type 2, hosted):** host ƏS üzərində; VirtualBox, VMware Workstation.
- **Proxmox:** KVM və konteynerləri idarə edən platforma, ayrıca hipervizor deyil.
- **VDI (virtual desktop infrastructure):** iş masası data mərkəzindəki VM-dədir; riskləri ekran görüntüsü, hesab oğurluğu, bufer/USB.

:::exam Tələ
Birinci tip avtomatik təhlükəsiz, ikinci tip avtomatik zəif deyil. İdarəetmə kompüteri məcburi deyil. Müqayisə hücum səthinə, idarəetmə hüquqlarına və təsir dairəsinə əsaslanır.
:::

## Üsullar və imtiyazlar

| Anlayış | Nədir |
| --- | --- |
| Tam virtuallaşdırma (full virtualization) | Qonağa tam virtual aparat interfeysi, dəyişiklik lazım deyil; ikili çevirmə (binary translation) tarixi üsuldur |
| Emulyasiya (emulation) | Başqa maşını proqramla təqlid edir (QEMU), yavaşdır |
| Paravirtuallaşdırma (paravirtualization) | Qonaq hypercall ilə hipervizordan istəyir; virtio sürücüləri |
| Intel VT-x, AMD-V | Prosessorun qonaq nəzarəti; VMX root/non-root ring nömrəsinin davamı deyil, ring −1 şərti addır |
| İmtiyaz halqaları (protection rings) | Tətbiq ring 3, nüvə ring 0 |
| VM çıxışı (VM exit) | Nəzarət tələb edən hadisədə idarə hipervizora keçir |
| IOMMU (VT-d, AMD-Vi) | Qurğuların birbaşa yaddaş girişini məhdudlaşdırır |
| İç-içə virtuallaşdırma (nested virtualization) | VM daxilində hipervizor |

Tam virtuallaşdırma və aparat dəstəyi bir-birini istisna etmir.

## Virtual resurslar

| Anlayış | Nədir |
| --- | --- |
| Virtual CPU (vCPU) | Qonağın icra vahidi; müstəsna nüvə deyil |
| Overcommit | Virtual cəmin fiziki tutumu keçməsi; hamı işləyəndə CPU gözləməsi artır |
| Reservation, limit, share | Rezerv əlçatanlığı qoruyur, limit yuxarı həddir, pay rəqabətdə üstünlük verir |
| Balloon, EPT/NPT, NUMA | Balloon yaddaşı geri alır, EPT/NPT ünvan çevirməsini sürətləndirir, NUMA-da uzaq yaddaş gecikdirir |
| NFS, iSCSI | Hovuza şəbəkə ilə çatma yolları |
| Thick provisioning | Həcm əvvəlcədən rezerv olunur |
| Thin provisioning | Yazıldıqca tutulur; hovuz dola bilər |
| RAID | Disk nasazlığına dözür, silinməyə qarşı qoruma deyil |
| Data virtualization | Vahid sorğu görünüşü; əsas risk səlahiyyət uyğunlaşdırılmasıdır |

## Virtual şəbəkələr

- **vNIC** (virtual network interface card) VM-i **vSwitch**-ə (virtual switch) qoşur, çıxış **uplink** ilədir. Eyni hostdakı trafik uplink-ə çıxmır, fiziki IDS və firewall görmür; virtual firewall, mikroseqmentasiya (microsegmentation) və ya host sensoru lazımdır.
- **VLAN** məntiqi seqmentdir, IEEE 802.1Q etiketi aid olduğu VLAN-ı göstərir; access port bir VLAN, **trunk** icazəli VLAN-ları daşıyır. VLAN şifrələmə deyil.
- **Rejimlər:** bridged (VM kampus şəbəkəsinə çıxır, zərərli proqram analizi üçün təhlükəli), NAT (host IP-si arxasından, çıxış hücumları), host-only (hosta hücum riski), internal network (daxili, zərərli proqram laboratoriyası üçün ən uyğun).
- **East-west traffic** VM-lər arasında, **north-south traffic** mühitə girib-çıxan; promiscuous rejim və MAC dəyişməsi siyasətlə idarə olunur.

## Həyat dövrü

| Anlayış | Nədir |
| --- | --- |
| Template, clone | Şablon baza təsvirdir; klon nüsxədir (tam və ya əlaqəli); Sysprep və cloud-init kimliyi fərdiləşdirir |
| Snapshot | Qısa geri qayıtma nöqtəsi, baza diskdən asılı; ehtiyat nüsxə deyil |
| Crash consistency, application consistency | Qəfil enerji kəsilməsi kimi tutulma, uyğun olaraq tranzaksiyaları nəzərə alan tutulma (VSS) |
| Replikasiya (replication) | Başqa yerə davamlı surət; RTO-nu azaldır, səhvi və şifrələnməni də köçürür |
| Backup (ehtiyat nüsxə) | Ayrı yerdə müstəqil nüsxə |
| Live migration | İşləyən VM-in köçürülməsi, pre-copy: yaddaş surəti, dəyişənlər, qısa dayandırma; sıfır fasilə zəmanəti deyil |

:::exam Tələ
Snapshot ehtiyat nüsxə deyil; işləyən VM fayllarını adi kopyalamaq uyğunsuz nüsxə verə bilər.
:::

## Klaster və bərpa

- **Klaster** hostları birləşdirir; **N+1** bir host itəndən sonra yükün sığmasını tələb edir (336 GiB tutum, biri itəndə 224 GiB, 240 GiB tələbat çatmır).
- **Anti-affinity** replikaları fərqli hostlara yayır; **fencing** və kvorum parçalanmış qrupun zidd yazmasını önləyir.
- **RTO** (recovery time objective) bərpa müddəti, **RPO** (recovery point objective) qəbul edilən itki; RPO 15 dəqiqə olan bazaya gecəlik nüsxə kifayət etmir.
- **3-2-1:** 3 nüsxə, 2 daşıyıcı, 1 başqa yerdə, biri oflayn və ya dəyişdirilə bilməyən. Bərpa ayrılmış şəbəkədə sınanır.

## Konteynerlər

| Anlayış | Nədir |
| --- | --- |
| Konteyner | Host nüvəsini paylaşan proses mühiti; VM-in öz nüvəsi var |
| Image, volume | Təsvir tətbiq və kitabxanalardır; davamlı data ayrıca həcmdədir |
| Namespace, control groups (cgroups) | Birincisi görünüşü ayırır, ikincisi CPU/yaddaşı məhdudlaşdırır; təkbaşına kifayət deyil |
| Docker, Dockerfile | Təsvir qurma və başlatma aləti, qurma reseptidir |
| Registry, tag, digest | Reyestr saxlayır, etiket dəyişə bilir, digest konkret təsviri göstərir |
| Kubernetes, Pod | Orkestrasiya; Pod ən kiçik vahid |
| Deployment, Service, Ingress | Replikalar, sabit ünvan, xarici HTTP girişi |
| API server, planlaşdırıcı, nəzarətçilər | İdarəetmə müstəvisi: API sorğuları qəbul edir, planlaşdırıcı Pod üçün düyün seçir, nəzarətçilər faktiki vəziyyəti istənənlə tutuşdurur; API-yə geniş hüquq bütün tətbiqlərə təsir edir |
| etcd, kubelet, runtime | Vəziyyət saxlama, işçi düyün agenti, konteyner icra mühiti |
| Readiness, liveness | Hazırlıq və yenidən başlatma yoxlaması |

Namespace təkbaşına şəbəkəni ayırmır, NetworkPolicy lazımdır; etibarsız kod üçün adi konteyner kifayət deyil.

## Təhdidlər

| Təhdid | Nədir / tədbir |
| --- | --- |
| VM escape | Qonaqdan hosta çıxış; yamaq, lazımsız qurğuları söndürmək |
| Management plane ələ keçirilməsi | Admin paneli ilə VM silmək, disk ixracı (ESXi ransomware); ayrıca VLAN, MFA, RBAC, audit |
| VM sprawl | Nəzarətsiz yaranmış unudulmuş VM-lər; inventar |
| Köhnə imic və şablon | Hər klon eyni zəifliyi daşıyır; sirlər imicdən çıxarılır |
| Snapshot sızması | Disk və RAM nüsxəsi oğurlanır |
| Noisy neighbour | Qonşu resursu sıxışdırır; limit və rezerv |
| Side channel | Ortaq CPU keşi; yamaqlar |
| Ortaq nasazlıq sahəsi | Host çöküşü hamını dayandırır; HA |
| Hyperjacking | Hipervizorun ələ keçirilməsi; tək VM-i yenidən qurmaq kifayət deyil |
| Spectre, Meltdown | 2018 spekulyativ icra yan kanalları; eyni zəiflik deyil |
| VENOM | QEMU disket nəzarətçisi daşması (CVE-2015-3456) |
| ESXiArgs | 2023 ESXi ransomware, OpenSLP (CVE-2021-21974); CISA bərpa təlimatı nüsxəni əvəz etmir |
| CVE-2025-22224, CVE-2025-22225, CVE-2025-22226 | VMX yaddaş pozuntusu, hipervizora ixtiyari yazma, məlumat açıqlanması; ayrılma yamağı əvəz etmir |

## Sərtləşdirmə

- **NIST** SP 800-125 (2011) tam virtuallaşdırma, SP 800-190 (2017) konteynerlər, SP 800-61 Rev. 3 (2025) insidentə cavab üçündür.
- Minimal host, Secure Boot, bütün qatların yamağı (firmware, mikrokod, hipervizor, alətlər, qonaq ƏS); Windows 10 adi dəstəyi 14 oktyabr 2025-də bitib.
- İdarəetmə müstəvisi ayrılır, VPN və keçid hostu (jump host), fərdi hesab, MFA, RBAC; rollar bölünür.
- Audit: giriş, snapshot, disk ixracı; **SIEM** qaydaları kontekstə bağlanır; insidentdə restart RAM sübutunu itirə bilər.

## Konteyner təhlükəsizliyi

- Təsvir minimal baza ilə qurulur, **SBOM** (software bill of materials) hazırlanır, imza və digest yoxlanır; sirr Dockerfile-da qalır, skan təmiz olsa belə zərərsizlik sübut deyil.
- `--privileged`, root, Docker socket qaçınılır; capabilities azaldılır, seccomp, AppArmor, SELinux, rootless icra.
- Kubernetes: RBAC, Pod Security Admission, Secret-də base64 şifrələmə deyil; NetworkPolicy yalnız lazımi trafikə icazə verir, icazələr birləşir.

## Diaqnostika

Ardıcıllıq: əhatə, fiziki yol, virtual bağlantı, IP və DHCP, VLAN və marşrut, TCP/UDP və siyasət, DNS və TLS, resurs və qeydlər, bir fərziyyə bir dəyişiklik ilə təsdiq. Alətlər: ping (ICMP), traceroute, ip, ss, dig, curl. Live migration-dan sonra hədəfdə VLAN, trunk siyahısı və MTU yoxlanır. Bütün firewall-u söndürmək və ya klasteri restart etmək səbəbi gizlədir.

## İmtahan üçün yadda saxla

- **Eyni hostda VM-lər arası trafik** fiziki IDS-dən keçməyə bilər: vSwitch daxilində qalır.
- **Daxili şəbəkə** də mütləq təhlükəsiz deyil: ikinci interfeys və ya marşrutlaşdırma çıxış yarada bilər, escape riski qalır.
- **HA resurs yaratmır**: mövcud tutumda yenidən başlanmanı idarə edir; ortaq elektrik, kommutator və massiv ortaq risk qalır.
- **Snapshot, replikasiya, ehtiyat nüsxə** üç ayrı alətdir: qısa geri qayıtma, tez bərpa, müstəqil bərpa.
- **Ayrılma yamağı əvəz etmir**: idarəetmə VLAN-ı CVE-2025-22224/22225 zəncirini tam bağlamır, hipervizor yamanmalıdır.
- **Konteyner təsviri** heş ilə bütövlüyü göstərir, etibarlı müəllifi sübut etmir; təmiz zəiflik skanı zərərsizlik sübutu deyil.
- **Ad fəzası**, Linux network namespace və NetworkPolicy üç ayrı anlayışdır; ad fəzası şəbəkə sərhədi yaratmır.
- **Qısa müddətli** snapshot yeniləmə üçündür; uzun zəncir yer və performans təzyiqi yaradır.
- **Konspektin düzəlişləri:** VM-lər tam təcrid olunmur, "bütün avadanlıq təqlid edilir" köhnə təsvirdir, "bütün ƏS ilə uyğundur" şərtlidir, 10% yük və 50–60% xərc rəqəmlərinin mənbəyi yoxdur, universal fakt kimi əzbərlənməz.
