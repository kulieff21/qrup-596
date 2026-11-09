+++
title = "Son qurğuların təhlükəsizliyi və sistemlərin mühafizəsinin gücləndirilməsi"
unit = "qisa"
order = 11
summary = "Mühazirənin bütün anlayışları bir sətirlə: son qurğu, EPP/EDR/XDR/MDR, hardening, yamaqlar, Secure Boot/TPM/şifrələmə, Windows və Linux, mobil cihazlar, loglar, şəbəkə avadanlığı, IoT, Zero Trust."
updated = 2026-11-09

[[source]]
title = "Mühazirə 11: Son qurğuların təhlükəsizliyi və sistemlərin mühafizəsinin gücləndirilməsi"
note = "Elmar Cabbarov, 2026–2027"
+++

Hücumların çoxu son qurğuda başlayır. Bu mövzu cihazları qoruyan texnologiyaları və hücum səthini kiçildən gücləndirmə prosesini sadalayır. Nümunələr şərti universitet nümunəsidir. Hər sətir bir anlayışdır; dərinlik üçün orta və uzun versiyalara baxın.

## Son qurğu və hücum səthi

| Anlayış | Nədir |
| --- | --- |
| Son qurğu (endpoint) | Məlumatı qəbul, emal və ya saxlayan cihaz: noutbuk, telefon, server, printer, kamera. |
| Internet of Things (IoT) | Sensor, kamera, ağıllı lövhə kimi cihazlar; antivirus qurmaq çətindir. |
| Hücum səthi (attack surface) | Hücumçunun istifadə edə biləcəyi bütün giriş nöqtələri: portlar, xidmətlər, proqramlar, admin hesabı, USB. |
| Hardening (system hardening) | Lazımsız imkanları azaltmaq, zəif sazlamanı düzəltmək, nəzarəti yoxlamaq. |
| Risk | Hücum ehtimalı və zərərin birləşməsi; cihaz funksiyası və məlumatın həssaslığı ilə bağlıdır. |

Üç xassə: məxfilik (icazəsiz oxu), tamlıq (icazəsiz dəyişmə), əlçatanlıq (vaxtında istifadə). İnternetə çıxışsız cihazın da hücum səthi var (USB, qonşu kompüter, fiziki giriş). Cihaz ələ keçəndə diskdəki sənədlərlə yanaşı brauzer sessiyası və qoşulmuş resurslar da hədəf olur: oğurlanmış noutbukun diski qorunsa da, onun LMS və ya poçt sessiyası ayrıca ləğv edilməlidir. Risk cihazın funksiyasından asılıdır: kitabxana terminalı ilə tələbə bazasının admin kompüteri eyni ƏS-də olsa da, riskləri fərqlidir. Hər qurğu üçün uyğun tədbir fərqlidir: noutbukda disk şifrələməsi və MFA, laboratoriyada adi hesab və tətbiq nəzarəti, serverdə yamaq və xidmət hesabı, printerdə ayrıca zona, ölçü cihazında izolyasiya.

## Təhdidlər

- **Zərərli proqram (malware):** virus, soxulcan, troyan; şantaj proqramı (ransomware) şifrələyir və ya yaymaqla hədələyir.
- **Fişinq (phishing):** istifadəçini aldadıb fayl açdırır və ya parol alır; proqram istifadəçinin hüquqları ilə işləyir.
- **Oğurlanmış hesab:** parol, kuki və ya token; MFA kömək edir, sessiya oğurluğunu tam həll etmir.
- **Digər:** yamanmamış zəiflik, təhlükəli konfiqurasiya (standart parol), itmiş cihaz, təchizat zənciri.
- **Hücum zənciri:** ilkin giriş, kəşfiyyat, qalıcı giriş, səlahiyyət artırma, yan keçid, məlumat çıxarma; müdafiə çoxqatlıdır və hadisəni dərhal bildirmək vacibdir.

## EPP, EDR, XDR, MDR

- **EPP** (Endpoint Protection Platform): zərərli icranı qurğuda önləyir; antivirus onun əsasıdır (imza, evristika, davranış).
- **EDR** (Endpoint Detection and Response): davranış telemetriyası toplayır, zənciri aşkarlayır, prosesi dayandırır, cihazı təcrid edir.
- **XDR** (Extended Detection and Response): qurğu, poçt, şəbəkə, bulud və kimliyi əlaqələndirir.
- **MDR** (Managed Detection and Response): xarici komandanın izləmə və cavab xidməti.

:::exam
Antivirus faylı, EDR cihazdakı bütün davranışı, XDR bir neçə mənbəni görür; MDR texnologiya deyil, xidmətdir.
:::

## Hardening prosesi

Dörd əsas: **uçot** (uçotda olmayan cihaz qorunmayan sayılır), **minimal səlahiyyət**, **minimal funksionallıq** (SMBv1 və Telnet kimi lazımsız protokol söndürülür), **baza konfiqurasiyası**.

| Anlayış | Nədir |
| --- | --- |
| Security baseline | Cihaz qrupu üçün təsdiqlənmiş minimum sazlama. |
| CIS Benchmarks | Məhsul üzrə təhlükəsiz sazlama tövsiyələri; CIS Controls təşkilat səviyyəsindədir. |
| STIG | DISA-nın texniki tələb və yoxlama qaydaları; avtomatik hüquqi tələb deyil. |
| ISO/IEC 27001 və 27002 | İdarəetmə sistemi və tədbirlər rəhbərliyi. |
| Configuration drift | Konfiqurasiyanın zamanla bazadan uzaqlaşması; Group Policy, Intune, Ansible ilə izlənir. |
| İstisna | Yazılı, müddətli, məsul şəxsli, kompensasiyaedici tədbirli. |

## Minimum səlahiyyət

Hesab sərhədləri: tələbəyə lokal administrator, laborantın domen üzrə tam idarə, xidmət hesabına interaktiv giriş verilmir; fövqəladə hesab nəzarətsiz daimi istifadəyə çevrilməməlidir.

- **Minimum səlahiyyət (least privilege):** yalnız iş üçün lazım olan hüquq; gündəlik və admin hesabı ayrılır.
- **Ehtiyac anında səlahiyyət (just-in-time privilege):** imtiyaz müddətli verilir, iş bitəndə geri alınır; Windows UAC bunu əvəz etmir.
- **LAPS** (Local Administrator Password Solution): hər cihazda unikal lokal admin parolu, Active Directory və ya Entra ID-də saxlanır; ortaq parolu aradan qaldırır, oxuma hüququ qorunmalıdır.
- Ayrılan işçinin hesabı bağlanır, qrup üzvlüyü və açarları yoxlanır; artıq hüququ geri almaq prosesə daxildir.

## Yamaqlar və dəstək

Yamaq (patch) zəifliyi aradan qaldırır; ƏS-dən başqa brauzer, VPN müştərisi, drayver və firmware də daxildir. NIST SP 800-40 Rev. 4 bunu planlı profilaktik xidmət sayır.

Beş mərhələ: **aşkarla, prioritet ver, sına (pilot qrup), mərhələli quraşdır, yoxla.** Göndərmək quraşdırmaq demək deyil, ona görə yoxlama vacibdir.

- **CVSS** texniki ağırlıqdır; **KEV** (CISA-nın Known Exploited Vulnerabilities kataloqu) real istismarı göstərir; **EPSS** gələcək istismar ehtimalıdır, faktiki istismar deyil.
- İnternetə açıq VPN şlüzündə aktiv istismar olunan zəiflik daxili kompüterdəki daha yüksək CVSS-dən əvvəl yamanır.
- Yamaq qoyula bilməyəndə: seqmentasiya, xidməti söndürmək, əlavə monitorinq.
- Windows 10-un ümumi dəstəyi 14 oktyabr 2025-də bitib; **ESU** (Extended Security Updates) 14 oktyabr 2028-ə qədər ödənişli yenilənmə verə bilər. Dəstəksiz sistemdə antivirus yamağı əvəz etmir.

## Secure Boot, TPM, şifrələmə

| Mexanizm | Nəyi qoruyur / nəyi qorumur |
| --- | --- |
| UEFI Secure Boot | Yalnız imzalı yükləyici və nüvə işləyir (bootkit-ə qarşı); işləmə vaxtındakı hücumlara qarşı yox. |
| TPM (Trusted Platform Module) | Açarları qoruyur, yükləmə ölçmələrini saxlayır. |
| Measured boot | Ölçmələri PCR registrlərinə yazır; bloklamır, sübut verir. |
| BitLocker, LUKS | Söndürülmüş cihaz oğurlananda məlumatı qoruyur. |
| Ekran kilidi | Diskin oxunmasını dayandırmır. |

Yuxu rejimində və ya işləyən cihazda açarlar yaddaşda qalır; TPM + PIN və hibernasiya bunu sərtləşdirir. Bərpa açarı mərkəzi qorunan yerdə saxlanır. Yükləmə zənciri dəyişəndə TPM açar vermir və bərpa açarı lazımdır.

## Tətbiq, firewall, DLP, USB

- **Application allowlisting:** yalnız təsdiqlənmiş proqram işləyir (AppLocker, WDAC); qayda imza, heş və ya yola görə; əvvəl audit rejimi.
- **Host firewall:** cihazın özündə gələn və gedən bağlantıları süzür, yoluxmuş qonşudan qoruyur.
- **DLP** (Data Loss Prevention): həssas məlumatın USB, poçt və buluda çıxmasını məhdudlaşdırır.
- **USB nəzarəti:** qadağa, yalnız oxuma və ya cihaz sinfi məhdudiyyəti; USB klaviatura kimi də görünə bilər.

## Windows və Linux

- **Windows:** mərkəzi siyasətlə firewall, antivirus, BitLocker, audit və admin qrupları; SMBv1 söndürülür; Credential Guard giriş sirlərini gücləndirir; RDP yalnız idarəetmə şəbəkəsindən. Yoxlama PowerShell əmrləri (`Get-MpComputerStatus`, `Get-BitLockerVolume`, `Get-Tpm`) yalnız oxuyur, düzəltmir; nəticə bazaya qarşı müqayisə olunur.
- **Linux:** universal skript yoxdur; əvvəl xidmət və portlara baxılır. SSH-də açar girişi, root girişi və parol girişi bağlanır (əvvəl yeni açarla giriş yoxlanır). UFW ilə `deny incoming` və SSH məhdudiyyəti; `chmod 777` yox; **SELinux** və **AppArmor** məcburi giriş nəzarətidir, söndürülmür.

## Mobil cihazlar

- **MDM** (Mobile Device Management): ekran kilidi, şifrələmə, tətbiq siyasəti, uzaqdan silmə.
- **UEM** (Unified Endpoint Management): müxtəlif cihaz siniflərini bir idarəetmədə birləşdirir.
- **MAM** (Mobile Application Management): tətbiq və təşkilat məlumatına yönəlir.
- **BYOD** (Bring Your Own Device): şəxsi cihaz; iş profili ilə ayrılır, itəndə seçici silmə şəxsi məlumata toxunmur.

## Loglar və insident

- **Jurnal qeydi (log entry)** hadisənin təsviri, **xəbərdarlıq** qaydanın nəticəsi, **insident** təhlükəsizliyi pozan vəziyyətdir.
- Windows Security 4624/4625 giriş, 4688 proses, 4732 qrupa üzv, 1102 audit təmizlənməsi; System 7045 xidmət; Linux-da journald və auditd.
- Qeydlər SIEM-ə TLS üzərindən syslog ilə gedir; susan agent xəbərdarlıq tələb edir; MITRE ATT&CK təsnifat verir.
- NIST SP 800-61 Rev. 3 və NIST CSF 2.0: təcrid, sübut, hesabların qorunması, səbəbin aradan qaldırılması, təmiz bərpa.
- **RPO** qəbul edilən məlumat itkisi intervalı, **RTO** bərpa üçün hədəf vaxtdır; bərpa istifadəçi işi ilə sınanır.

## Şəbəkə avadanlığı

Aktiv avadanlıq enerji ilə siqnalı yaradır, bərpa edir və ya idarə edir (təkrarlayıcı və gücləndirici də aktivdir); passiv komponent siqnalı yaratmadan ötürür.

| Cihaz | Əsas tədbir |
| --- | --- |
| Kommutator | Portlar söndürülür, VLAN, 802.1X, DHCP snooping, Dynamic ARP Inspection, BPDU Guard. |
| Marşrutizator | IP marşrutu; ACL; OSPF və BGP; NAT təhlükəsizlik siyasəti deyil. |
| Giriş nöqtəsi (access point, AP) | WPA3, lazım olsa WPA2-Enterprise, EAP-TLS. |
| İdarəetmə | SSH və HTTPS, Telnet yox; SNMP üçün SNMPv3; AAA qeydləri; RADIUS və Blast-RADIUS yamağı. |
| SFP və SFP+ | Gigabit üçün SFP, 10 Gigabit üçün SFP+. |
| PoE | Kabelə enerji verir. |
| PDU, UPS | PDU enerji paylayır, trafik yox; UPS müvəqqəti enerji verir. |

## Passiv komponentlər və fiziki mühafizə

- **UTP** ekransız, **STP** ekranlı bükülmüş cütdür; optik lif itkisizdir demək yanlışdır və **dinlənə bilər**, şifrələməni əvəz etmir.
- Konnektorlar: RJ45 (8P8C) mis, LC, SC, FC, ST, MT-RJ optikdir.
- Rəf: 19 düymlük standart, 1U = 44,45 mm; lif birləşmə korpusu (joint enclosure) birləşmələri qoruyur; üz qapağı (face plate) divar jack-ını saxlayır.
- Fiziki risklər: açıq auditoriya portu, səhv etiket, eyni kabel kanalından keçən iki ehtiyat bağlantı; kabel kanalı testi səhv sonlandırmanı üzə çıxarır.
- Optik büdcə: ümumi büdcə minus itki ehtiyatı verir (şərti nümunə: 8 dB − 5 dB = 3 dB ehtiyat). Cat5e ilə düzgün 100 metrlik kanal 1000BASE-T üçün yararlıdır.

## IoT və laboratoriya cihazları

Agent olmayanda nəzarət şəbəkəyə keçir: ayrıca VLAN, vasitəçi kompüter, fərqli parol, müddətli istisna və əvəzləmə, istifadədən çıxanda təmizləmə. Aktiv skandan əvvəl laboratoriya məsulu ilə razılaşılır.

## Situasiyalar üçün qısa xəritə

- **Laboratoriyada admin hüququ və kriptomayner:** admin hüququ götürülür, proqram mərkəzdən quraşdırılır, tətbiq nəzarəti, eyni baza və təmiz image, EDR yoxlanır, ayrıca VLAN, yoluxmuş kompüter sıfırdan qurulur.
- **Yuxu rejimində itən şifrəli noutbuk:** açar yaddaşdadır; uzaqdan kilid və ya silmə, parol və tokenlərin ləğvi, sertifikatların ləğvi, bərpa açarının yoxlanması; gələcəkdə hibernasiya, qısa kilid, TPM + PIN.
- **İstismar olunan kritik zəiflik, yamaq sınanmayıb:** kompensasiyaedici tədbir (virtual yamaq, funksiyanı söndürmək, girişi məhdudlaşdırmaq), istismar əlamətlərinin axtarışı, paralel sınaq, geri qaytarma planı, yazılı müddətli istisna.

## Zero Trust və ölçmə

- **Zero Trust:** şəbəkə daxili olmaq etibar deyil; NIST SP 800-207; qərar kimlik, cihaz vəziyyəti və resurs həssaslığına görə verilir.
- Şərti laboratoriya: uçot, pilot baza, adi hesab, tətbiq nəzarəti, EDR, ayrıca VLAN, USB siniflər, bərpa sınağı.
- Göstəricilər: yamaqlanma faizi (məxrəc əhatənin hamısıdır: 180/220 ≈ 81,8 faiz), idarə olunmayan cihaz, artıq admin, sensor sağlamlığı, cavab müddəti, bərpa uğuru, baza uyğunluğu. Quraşdırma sayı işləməyi sübut etmir.

:::warning
Qarışdırma: disk şifrələməsi ≠ sessiya qoruması; Secure Boot ≠ antivirus; yamağın göndərilməsi ≠ quraşdırılması; PDU ≠ trafik cihazı; optik lif ≠ dinlənməz.
:::
