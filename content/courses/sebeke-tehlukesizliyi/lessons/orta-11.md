+++
title = "Son qurğuların təhlükəsizliyi və sistemlərin mühafizəsinin gücləndirilməsi"
unit = "orta"
order = 11
summary = "Hər anlayış 1–3 cümlə ilə: son qurğu və hücum səthi, EPP/EDR/XDR/MDR, hardening, yamaqlar, Secure Boot/TPM/şifrələmə, Windows və Linux bazası, mobil cihazlar, loglar, insident, şəbəkə avadanlığı, IoT, Zero Trust və ölçmə."
updated = 2026-11-09

[[source]]
title = "Mühazirə 11: Son qurğuların təhlükəsizliyi və sistemlərin mühafizəsinin gücləndirilməsi"
note = "Elmar Cabbarov, 2026–2027"
+++

Hücumların çoxu son qurğuda başlayır: noutbukda, laboratoriya kompüterində, telefonda. Mövzu bu cihazları qoruyan texnologiyaları və hücum səthini kiçildən gücləndirmə prosesini əhatə edir. Universitet nümunələri şərti tədris nümunəsidir.

## Son qurğu və hücum səthi

Son qurğu (endpoint) məlumatı qəbul edən, emal edən və ya saxlayan cihazdır: iş stansiyası, noutbuk, smartfon, planşet, server, həmçinin printer, kamera, ağıllı lövhə və ölçü cihazı kimi Internet of Things (IoT) cihazları. Hamısına antivirus qurmaq mümkün deyil, ona görə tərif məhsulun dəstəklədiyi siyahı ilə məhdudlaşmır. Müdafiə cihazı, məlumatı və onun giriş imkanlarını (brauzer sessiyası, tokenlər, qoşulmuş resurslar) əhatə edir. Üç xassə: məxfilik (icazəsiz oxu), tamlıq (icazəsiz dəyişmə), əlçatanlıq (vaxtında istifadə). Şantaj proqramı bir neçəsini pozur: məlumatı həm oğurlayır, həm şifrələyir.

Hücum səthi (attack surface) müdaxilə üçün istifadə oluna bilən bütün giriş imkanlarıdır: açıq portlar, xidmətlər, proqramlar, makrolar, brauzer əlavələri, USB, lokal admin hesabı, uzaqdan yardım agenti. İnternetdən əlçatmaz cihazın səthi sıfır deyil: USB, qonşu kompüter, fiziki giriş qalır. Sistemin mühafizəsinin gücləndirilməsi (system hardening) lazımsız imkanları azaltmaq, zəif sazlamaları dəyişmək və nəzarətləri **yoxlamaq** prosesidir. Risk ehtimalı və zərəri birlikdə qiymətləndirir: kitabxana terminalı ilə tələbə bazasının admin kompüteri eyni ƏS-də olsa da, riskləri fərqlidir.

| Qurğu | Başlıca risk | Tədbir |
| --- | --- | --- |
| Kafedra noutbuku | Oğurlanma, sessiya itkisi | Disk şifrələməsi, MFA, EDR |
| Tələbə laboratoriyası | İcazəsiz icra, ortaq hesab | Adi hesablar, tətbiq nəzarəti |
| LMS serveri | Xidmət zəifliyi | Yamaq, xidmət hesabı, bərpa |
| Kitabxana terminalı | Əvvəlki sessiya | Məhdud rejim, sessiya təmizlənməsi |
| Printer | Yaddaşda sənəd, açıq idarəetmə | Ayrıca zona, yenilənmə |
| Ölçü cihazı | Köhnə proqram | İzolyasiya, vasitəçi kompüter |

## Təhdidlər və hücumun inkişafı

Zərərli proqram (malware) icazəsiz işləyən proqramdır: virus fayllara qoşulur, soxulcan şəbəkədə yayılır, troyan faydalı görünür; şantaj proqramı (ransomware) şifrələyir və ya yaymaqla hədələyir; məlumat oğurlayan proqram parol və sessiya toplayır. Eyni proqram bir neçə funksiya daşıya bilər. Fişinq (phishing) istifadəçini aldadaraq fayl açdırır, parol alır və ya əməliyyat təsdiqlədir (məsələn, makro aktivləşdirən saxta sənəd); proqram istifadəçinin hüquqları ilə işləyir. Oğurlanmış hesabda fayl olmaya bilər: parol, sessiya kukisi və ya token istifadə olunur. Çoxamilli autentifikasiya (MFA) parol itkisinə əlavə maneədir, amma sessiya oğurluğunu tam həll etmir.

Digər təhdidlər: yamanmamış zəifliklər, təhlükəli konfiqurasiya (standart parol, lazımsız xidmət), itmiş cihaz, təchizat zənciri (etibarsız quraşdırma paketi). Gündəlik işin admin hüququ ilə görülməsi hamısının ziyanını artırır.

Hücum zənciri: ilkin giriş, kəşfiyyat, qalıcı giriş, səlahiyyət artırma, yan keçid, məlumatın çıxarılması və ya xidmətin dayandırılması (şərti ardıcıllıq). Eyni admin parolu yan keçidi asanlaşdırır. Çoxqatlı nəzarət (poçt filtri, tətbiq nəzarəti, EDR, firewall, ehtiyat nüsxə) bir maneə düşəndə növbətinin işləməsi üçündür; hamısının bir admin hesabı ilə söndürülməsi qatları zəiflədir. Əməkdaş şübhəli sənədi dərhal bildirməlidir; cəza qorxusu bildirişi gecikdirir.

## EPP, EDR, XDR və MDR

- **EPP** (Endpoint Protection Platform) zərərli icranı qurğuda önləyir; antivirus onun əsasıdır (imza, evristika, davranış analizi). Hamısını tutmur.
- **EDR** (Endpoint Detection and Response) proses, fayl, reyestr, şəbəkə və yaddaş telemetriyası toplayır, proses ağacını göstərir, prosesi dayandırır, faylı karantinə alır, cihazı təcrid edir. Analitik və sazlama tələb edir; telemetriya tam surət deyil.
- **XDR** (Extended Detection and Response) qurğu, poçt, kimlik, şəbəkə və bulud siqnallarını əlaqələndirir; çox vaxt bir istehsalçının ekosisteminə bağlıdır, "tam inteqrasiya" zəmanəti yoxdur.
- **MDR** (Managed Detection and Response) xidmət modelidir: xarici komanda xəbərdarlıqları izləyir və razılaşdırılmış cavabı verir; təcrid səlahiyyəti və gecə əlaqəsi müqavilədə yazılır.

:::exam
Antivirus **faylı**, EDR cihazdakı **bütün davranışı**, XDR **bir neçə mənbəni** (son qurğu + poçt + şəbəkə + bulud + kimlik) görür. Antivirus bloklayır və karantinə alır; EDR zənciri aşkarlayır və təcrid edir. MDR texnologiya deyil, xidmətdir.
:::

Nümunə: sənəd tətbiqi skript interpretatorunu başladır, o xarici ünvana qoşulur. EPP faylı tanımaya bilər, EDR proses ağacını göstərir, XDR eyni məktubun başqalarına çatdığını tapır, MDR cihazı təcrid edir. Qanuni statistik paket də skript işlədə bilər; ona görə proses adına görə bütün laboratoriyanı bloklamaq olmaz. Yanlış müsbət qanuni işi şübhəli sayır, yanlış mənfi hücumu buraxır. Agentin quraşdırılması işlədiyini sübut etmir: sensorun son əlaqəsi, siyasət versiyası və sınaq xəbərdarlığının çatması yoxlanır; geniş istisnalar audit olunur.

## Hardening prosesi

:::tip Hardening-in 4 əsası
Uçot, minimal səlahiyyət, minimal funksionallıq (lazımsız proqram, xidmət, port, protokol, məsələn SMBv1 və Telnet söndürülür), baza konfiqurasiyası.
:::

**Uçot:** sahib, funksiya, zona, ƏS, proqramlar, dəstək, məlumat sinfi, şəbəkə zonası (VLAN), nəzarət vəziyyəti. Mənbələr (skan, agent, satınalma, port məlumatı) tutuşdurulur. Uçotda olmayan cihaz qorunmayan cihaz sayılır; aşkarlananda əvvəl sahibi və funksiyası müəyyən edilir, sonra idarəetməyə daxil edilir və ya məhdud şəbəkəyə keçirilir.

**Baza konfiqurasiyası (security baseline)** cihaz qrupu üçün təsdiqlənmiş minimum sazlamadır; noutbuk, terminal və server üçün ayrı hazırlanır.

| Mənbə | Nədir | Qeyd |
| --- | --- | --- |
| CIS Benchmarks | Məhsul və buraxılış üzrə təhlükəsiz sazlama | Sərt profil iş proqramına təsir edə bilər |
| STIG (DISA) | Texniki tələb və yoxlama qaydaları | ABŞ müdafiə mühiti üçündür, avtomatik hüquqi tələb deyil |
| CIS Controls | Təşkilat üzrə tədbirlər (məs., cihaz uçotu) | Benchmarks məhsul səviyyəsidir |
| ISO/IEC 27001 və 27002 | İdarəetmə sistemi və tədbirlər rəhbərliyi | 27002-də 93 tədbir, dörd mövzu |

Ardıcıllıq: funksiyanı öyrən, baza seç, fərqi ölç, sına, tətbiq et, izlə. Sınaq yalnız giriş ekranı deyil, dərs proqramı, çap və şəbəkəni də əhatə edir.

![figure](m11-1.png)

Konfiqurasiyanın bazadan yayınması (configuration drift) zamanla yaranır (genişlənmiş firewall qaydası, quraşdırıcının açdığı xidmət). Group Policy, Intune və Ansible siyasəti yayır və fərqi tapır. İstisna yazılı olmalıdır: cihazlar, tələb, risk, kompensasiyaedici tədbir, məsul şəxs, bitmə tarixi; bütün fakültə üçün nəzarəti söndürmək əsaslandırılmır.

## Minimum səlahiyyət və hesablar

Minimum səlahiyyət (least privilege) iş üçün lazım olan hüquqları verməkdir. Gündəlik hesab inzibati hesabdan ayrılır. İmtiyaz müddətli verilə bilər: ehtiyac anında səlahiyyət (just-in-time privilege); iş bitəndə geri alınır. Windows UAC pəncərəsi ayrıca hesabı əvəz etmir.

LAPS (Local Administrator Password Solution) hər Windows cihazında unikal lokal admin parolu yaradır, dövri dəyişir və Active Directory və ya Entra ID-də saxlayır; oxuma hüququ məhdud və audit olunan olmalıdır. Ortaq parol yan keçidi asanlaşdırır. LAPS domen admin parolunu idarə etmir və oxucu hesab ələ keçsə, çox cihaz risk altına düşür.

| Hesab | Verilməməli hüquq |
| --- | --- |
| Tələbə | Lokal administrator |
| Laborant | Domen üzrə tam idarə |
| LMS xidmət hesabı | İnteraktiv gündəlik giriş |
| Şəbəkə administratoru | Adi poçtda imtiyazlı sessiya (bastion və AAA qeydləri) |
| Fövqəladə | Nəzarətsiz daimi istifadə |

İşçi ayrılanda hesab bağlanır, qrup üzvlüyü və açarlar yoxlanır; artıq hüququ geri almaq prosesə daxildir.

## Yamaqlar və dəstək müddəti

Yamaq (patch) zəifliyi aradan qaldıran dəyişiklikdir; ƏS-dən başqa brauzer, VPN müştərisi, drayver və firmware-ə də aiddir. NIST SP 800-40 Rev. 4 bunu planlı profilaktik texniki xidmət kimi görür.

:::steps Yamaq idarəsinin beş mərhələsi
[[step]]
title = "Aşkarla"
body = "Bildiriş, versiya və skan tutuşdurulur; cihaz həqiqətən təsirlənirmi?"

[[step]]
title = "Prioritet ver"
body = "KEV, CVSS, əlçatanlıq, məlumatın həssaslığı və mövcud tədbirlər."

[[step]]
title = "Sına"
body = "Təmsilçi pilot qrupda iş proqramı və geri qaytarma yolu."

[[step]]
title = "Mərhələli quraşdır"
body = "Pilotdan sonra digər qruplar, yenidən başlatma planlanır."

[[step]]
title = "Yoxla"
body = "Versiya, faktiki quraşdırma və xidmət təsdiqlənir. Göndərmək quraşdırmaq deyil."
:::

CVSS texniki ağırlığı göstərir, təşkilat riskini yox. CISA KEV kataloqu real istismarı məlum zəiflikləri verir; kataloqda olmamaq istismarsızlıq sübutu deyil. EPSS gələcək istismar ehtimalıdır və faktiki istismarla qarışdırılmamalıdır. Nümunə: İnternetə açıq VPN şlüzündə aktiv istismar olunan CVSS 7,5 zəiflik daxili kompüterdəki CVSS 9,8-dən əvvəl yamanır. Yamaq qoyula bilməyən sistem üçün kompensasiyaedici tədbir: seqmentasiya, xidməti söndürmək, əlavə monitorinq.

Windows 10-un ümumi dəstəyi 14 oktyabr 2025-də bitib; uyğun cihazlar üçün Extended Security Updates (ESU) 14 oktyabr 2028-ə qədər yenilənmə verə bilər, amma bu avtomatik deyil. Dəstəksiz sistemdə antivirus çatışmayan yamağı əvəz etmir: cihaz ayrıca zonaya keçirilir, İnternet çıxışı məhdudlaşdırılır, müddətli istisna təsdiqlənir, əvəzləmə planı hazırlanır.

## Secure Boot, TPM və disk şifrələməsi

![figure](m11-3.png)

- **UEFI Secure Boot** yükləmə komponentlərinin imzasını yoxlayır; yalnız imzalı yükləyici və nüvə işə düşür (bootkit-ə qarşı). İşləmə vaxtındakı hücumları dayandırmır, imzalı kod qüsursuz demək deyil.
- **TPM** (Trusted Platform Module) açarları qoruyan və yükləmə ölçmələrini saxlayan modul (ayrı çip, inteqrə və ya firmware). Ölçülən yüklənmə (measured boot) ölçmələri PCR registrlərinə yazır; bloklamır, sübut verir.
- Disk açarı TPM-ə bağlıdırsa və yükləmə zənciri dəyişibsə, açar verilmir və bərpa açarı lazımdır; qanuni firmware yenilənməsi də bunu tetikləyə bilər.
- **BitLocker** (Windows) və **LUKS** (Linux, cryptsetup) söndürülmüş cihaz oğurlananda məlumatı qoruyur. İşləyən və ya yuxu rejimində cihazda açarlar yaddaşda qalır; ekran kilidi bunu təmin etmir. TPM + PIN daha sərt fiziki qoruma verir, amma dəstək tələb edir.

:::exam
"Disk şifrələnib, narahatlığa əsas yoxdur" yuxu rejimindəki açıq sessiya üçün səhvdir: sessiya, token və sertifikatlar ləğv edilir, uzaqdan kilid və ya silmə verilir, bərpa açarının yeri yoxlanır. Gələcək üçün hibernasiya, qısa kilid müddəti, TPM + PIN.
:::

Bərpa açarı qorunan mərkəzi yerdə (Entra ID, AD) saxlanır, açıq faylda yox. LUKS başlığının ehtiyatı həssasdır: köhnə nüsxə əvvəlki açar yuvalarını saxlaya bilər. Ehtiyat nüsxənin bərpası sınanmalıdır.

## Tətbiq, firewall və USB

Tətbiq icrasına nəzarət (application allowlisting) yalnız təsdiqlənmiş proqramı işlədir (AppLocker və WDAC, yəni App Control for Business); qayda imzaya, heşə və ya yola bağlanır. İmza yenilənməyə uyğunlaşır, heş dəqiqdir amma hər dəyişiklikdə dəyişir, yol sadədir amma yazıla bilən kataloqda zəifdir. Əvvəl audit rejimi, sonra bloklama. Proqram yazan tələbə üçün ayrıca virtual mühit. İcazəli proqram da sui-istifadə oluna bilər, ona görə EDR ilə tamamlanır.

Qurğu firewall-u (host firewall) cihazın gələn və çıxan bağlantılarını süzür və eyni VLAN-dakı yoluxmuş qonşudan qoruyur. DLP (Data Loss Prevention) həssas məlumatın USB-yə, poçta, buluda və çapa çıxmasını məhdudlaşdırır; təsnifat və etiketdən asılıdır. USB cihaz klaviatura və ya adapter kimi görünə bilər; qadağa, yalnız oxuma və cihaz sinfi məhdudiyyəti ayrı siyasətlərdir; AutoRun söndürmək saxta klaviaturanı dayandırmır. Seriya nömrəsi güclü kimlik sübutu deyil.

## Windows və Linux bazası

**Windows.** Dəstəklənən buraxılış və rol müəyyən edilir, sonra mərkəzi siyasətlə firewall, antivirus, şifrələmə, audit, ekran kilidi və admin qrupları sazlanır; SMBv1 və lazımsız uzaqdan giriş söndürülür (bütün SMB-ni düşünmədən yox). Yoxlama əmrləri: `Get-MpComputerStatus`, `Get-NetFirewallProfile`, `Get-BitLockerVolume`, `Confirm-SecureBootUEFI`, `Get-Tpm`, `Get-LocalGroupMember -SID 'S-1-5-32-544'`; nəticələr bazaya qarşı müqayisə olunur. Credential Guard bəzi giriş sirlərini qoruyur, tam zəmanət deyil. RDP yalnız idarəetmə şəbəkəsindən və adi hesablara verilmir.

**Linux.** Universal skript yoxdur; əvvəl buraxılış, rol, xidmətlər (`ss`, `systemctl`, `findmnt`, `sshd -T`). Açıq port zəiflik demək deyil. `127.0.0.1` lokal, `0.0.0.0` bütün IPv4 dinləməsidir; IPv6 ayrıca yoxlanır. `apt update` yalnız indeksi yeniləyir; yenilənmədən sonra köhnə nüvə qala bilər.

SSH üçün açar girişi, `PermitRootLogin no`, `PasswordAuthentication no`, `AllowUsers`, `X11Forwarding no`. Parol girişi yeni açarla giriş yoxlanmamış bağlanmır, mövcud sessiya və konsol saxlanır, `sshd -t` sintaksis, `sshd -T` effektiv sazlama verir. Firewall: UFW ilə `default deny incoming` və SSH-ni idarəetmə şəbəkəsinə məhdudlaşdırmaq; IPv6 ayrıca. Hüquqlar: `chmod 777` yox, `~/.ssh` üçün 700, `authorized_keys` üçün 600, sudo qaydası `visudo` ilə. SELinux və AppArmor məcburi giriş nəzarətidir: tətbiq işləməyəndə söndürmək əvəzinə rədd qeydi araşdırılır. `noexec` hər kod icrasını dayandırmır.

## Mobil cihazlar, MDM və BYOD

MDM (Mobile Device Management) qeydiyyatlı cihazda ekran kilidi, şifrələmə, tətbiq siyasəti və uzaqdan silmə tətbiq edir; UEM (Unified Endpoint Management) müxtəlif cihaz siniflərini bir idarəetmədə birləşdirir; MAM (Mobile Application Management) tətbiq və təşkilat məlumatına yönəlir. BYOD (Bring Your Own Device) cihazı şəxsin mülkiyyətində saxlayır: Android iş profili və ya tətbiq səviyyəli qoruma şəxsi və iş məlumatını ayırır. İtən cihazda seçici silmə yalnız universitet məlumatını silir; tam silmə şəxsi şəkilləri də itirə bilər, ona görə səlahiyyət əvvəlcədən müəyyən edilir. Uzaqdan silmə cihaz oflayn olanda gözləyir; konsolda əmrin yaranması silinmə demək deyil. Root/jailbreak aşkarlanması tam deyil. Qeydiyyatsız şəxsi cihaza (tələbə) yalnız məhdud veb giriş verilir; şəxsi telefonlar və idarə olunan kompüterlər ayrı zonada olur.

## Loglar, monitorinq və insident

Jurnal qeydi (log entry) baş vermiş hadisənin təsviridir; xəbərdarlıq qaydanın araşdırılmalı saydığı nəticədir; insident təhlükəsizliyi pozan vəziyyətdir. Saatlar sinxronlaşdırılır. Faydalı mənbələr: Windows Security 4624/4625 (giriş), 4688 (proses; komanda sətri ayrıca siyasət tələb edir), 4732 (qrupa üzv), 1102 (audit jurnalının təmizlənməsi), System 7045 (xidmət quraşdırılması); Linux-da journald və auditd; EDR və MDM qeydləri. auditd nəticəsinin boş olması hadisənin olmadığını sübut etmir. Sənəddən interpretator, ardınca xarici bağlantı və qoruma xidmətinin dayanması birlikdə ciddi siqnaldır. MITRE ATT&CK taksonomiyası araşdırmanı təşkil edir, özbaşına zərərli elan etmir.

Qeydlər qorunan kanalla mərkəzi SIEM-ə göndərilir (TLS üzərindən syslog), buferlənir, silinməkdən qorunur. Susan agent və uzun görünməyən noutbuk xəbərdarlıq yaratmalıdır.

İnsidentə cavab NIST SP 800-61 Rev. 3 və NIST CSF 2.0 ilə əlaqələnir (Govern, Identify, Protect, Detect, Respond, Recover). Ardıcıllıq: təcrid və əhatə, sübutun qorunması (enerjini kəsmək yaddaşı itirə bilər), hesabların təhlükəsizləşdirilməsi, ilkin səbəbin aradan qaldırılması, təmiz mənbədən və ya yoxlanmış nüsxədən bərpa. Faylı silmək hesabı, planlı tapşırığı və oğurlanmış sessiyanı aradan qaldırmır. Ehtiyat nüsxə eyni hesabla silinə bilirsə, hücumçu hər ikisini məhv edir; ayrı səlahiyyət, oflayn və ya dəyişdirilməz saxlanma lazımdır. RPO qəbul edilən məlumat itkisi intervalı, RTO xidmətin bərpası üçün hədəf vaxtdır (şərti LMS: RPO dörd saat, RTO altı saat). Bərpa sınağı istifadəçi işini tamamlamalıdır: daxil ol, material aç, tapşırıq göndər.

## Aktiv şəbəkə avadanlığı

Aktiv avadanlıq enerji ilə siqnal yaradır, bərpa edir, çevirir və ya ötürməni idarə edir: kommutator, marşrutizator, giriş nöqtəsi (access point, AP), media çevirici, ötürücü modul; təkrarlayıcı və gücləndirici də aktivdir. Passiv komponent siqnalı yaratmadan ötürür: kabel, konnektor, passiv optik bölücü, patch panel. İdarə olunan PDU-nun şəbəkə interfeysi ayrıca qorunmalı aktiv sistemdir.

| Cihaz | Əsas tədbir |
| --- | --- |
| Kommutator | İstifadəsiz portları söndürmək, 802.1X, DHCP snooping, Dynamic ARP Inspection, BPDU Guard |
| Marşrutizator | IP şəbəkələri arasında yol seçir; ACL, təhlükəsiz idarəetmə; OSPF (daxili), BGP (avtonom sistemlər); NAT təhlükəsizlik siyasəti deyil |
| AP | WPA3-Enterprise, lazım olsa WPA2-Enterprise; EAP-TLS; server sertifikatını yoxlamaq; WPS söndürmək |
| SFP / SFP+ | Gigabit üçün SFP, 10 Gigabit üçün SFP+; standart, dalğa uzunluğu, lif uyğunluğu |
| PoE injektor | IEEE 802.3af/at/bt; güc büdcəsi |
| Çap serveri | Yamaq, ayrıca zona, saxlama müddəti |

Kommutator MAC öyrənir; naməlum unicast və broadcast VLAN daxilində yayılır. İdarəetmə planı ayrılır: SSH və HTTPS idarəetmə zonasından, Telnet və qorunmayan HTTP söndürülür; SNMP işlənirsə SNMPv3 seçilir (adı özü şifrələmə demək deyil); fərdi hesab və AAA qeydləri. RADIUS yamaq prosesinə daxildir (Blast-RADIUS CVE-2024-3596). Wi-Fi şifrələməsi son qurğunun zərərli proqramını həll etmir.

## Passiv komponentlər və fiziki mühafizə

UTP ekranlaşdırılmamış, STP ekranlı bükülmüş cütdür; ekranın faydası quraşdırma və torpaqlamadan asılıdır. Cat5e ilə düzgün 100 metrlik kanal 1000BASE-T üçün olur (patch kordlar daxil). Optik lif işığı nüvə və qabıq vasitəsilə ötürür; tək rejimli və çox rejimli növləri var. Optik lif itkisiz deyil (optik büdcə: məsələn, 8 dB büdcə, 5 dB itki, 3 dB ehtiyat), **dinlənə bilər** və şifrələməni əvəz etmir; elektromaqnit müdaxiləyə davamlılıq məxfilik demək deyil.

Konnektorlar: mis Ethernet-də RJ45 adlanan 8P8C; optikdə LC (kiçik), SC (itələmə), FC (yivli), ST (süngü), MT-RJ. RJ45 optik deyil. Adapter fərqli formaları qoşa bilər, dalğa uzunluğunu və rejimi çevirmir; UPC və APC qarışdırılmır. LIU qutusu lifləri sonlandırır; lif birləşmə korpusu (joint enclosure) birləşmələri qoruyur. Rəf: 19 düymlük montaj standartı, 1U = 44,45 mm; kilid, havalandırma, enerji və kabel yolu planlanır. Üz qapağı (face plate) divar jack-ını saxlayır; patch panel sonlandırmaları təşkil edir; krimper montaj alətidir.

PDU elektrik enerjisini paylayır, trafik yox; UPS elektrik kəsilməsində məhdud müddət enerji verir. İdarə olunan PDU-nun hesabı ələ keçsə, serverlər söndürülə bilər. Açıq auditoriya portu, səhv etiket və eyni kabel kanalından keçən iki ehtiyat bağlantı fiziki risklərdir.

## IoT və laboratoriya avadanlığı

Agent qəbul etməyən IoT cihazında nəzarət şəbəkə sərhədinə, hesab idarəsinə və firmware uçotuna keçir. Satınalmada dəstək müddəti, imzalı yenilənmə, standart parol, lokal idarəetmə və məlumatın hara getdiyi soruşulur. Tədbirlər: fərqli sirr, ayrıca zona, vasitəçi və qorunan tunel, kommutator səviyyəsində müşahidə, müddətli istisna və əvəzləmə, istifadədən çıxanda təmizləmə (zavod sıfırlaması etibarlı silmə sayılmır). Ölçü cihazı və köhnə idarəetmə kompüteri ayrıca VLAN-a qoyulur, nəticə təsdiqlənmiş vasitəçi ilə çıxarılır; ölçmənin bütövlüyü də yoxlanır. Aktiv zəiflik skanından əvvəl istehsalçı və laboratoriya məsulu ilə razılaşma lazımdır; passiv müşahidə uçot üçün daha münasibdir.

## Zero Trust və laboratoriya layihəsi

Zero Trust şəbəkə daxilində olmağı avtomatik etibar saymır; NIST SP 800-207 açıq yoxlama və ən az səlahiyyətə əsaslanan arxitekturadır. Giriş qərarına istifadəçi kimliyi, cihazın vəziyyəti və resursun həssaslığı daxildir; yenilənməmiş cihaza yalnız yenilənmə xidmətinə məhdud yol verilə bilər. Uyğunluq siqnalı təzə olmalıdır.

![figure](m11-4.png)

Şərti 40 kompüterlik laboratoriya: (1) proqram və cihaz uçotu; (2) bir neçə cihazda baza sınağı (adi hesab, təsdiqlənmiş paket, firewall, tətbiq nəzarəti, audit, EDR); (3) proqram yazan dərs üçün virtual mühit; (4) VLAN-dan yalnız LMS, DNS, vaxt, yenilənmə və fayl xidmətlərinə giriş; (5) USB siniflərə ayrılır; (6) zərərsiz sınaq hadisələri, bərpa sınağı. Təmiz obrazdan bərpa zamanı tələbə işləri əvvəl qorunan yerə köçürülür.

## Effektivliyin ölçülməsi

Göstərici məxrəci, ölçmə anı və istisnaları ilə verilir. Nümunə: uçotda 200 cihaz, vaxtında yamaqlanan 180 olsa pay 90 faizdir; skan daha 20 idarə olunmayan cihaz tapsa, 180/220 ≈ 81,8 faizdir. Göstəricilər: vaxtında yamaqlanma, idarə olunmayan cihaz, artıq administrator, sensor sağlamlığı (quraşdırma sayı ilə qarışdırılmır), cavab müddəti (orta yox, median və ən uzun), bərpa uğuru, baza uyğunluğu. Uyğunluq skanı sazlamanı, zəiflik skanı zəifliyi, nəzarət sınağı davranışı yoxlayır; bunlar eyni deyil. Sınaqlar səlahiyyətli mühitdə, razılaşdırılmış sərhəddə aparılır; problemli cihazı uçotdan çıxarmaq göstəricini yaxşılaşdırır, təhlükəsizliyi yox.

:::reveal Laboratoriyada tələbələr admin hüququ ilə işləyir və kriptomayner tapılıb. Əsas tədbirlər?
Admin hüququ götürülür (minimal səlahiyyət); proqramlar mərkəzdən və ya müvəqqəti icazə ilə quraşdırılır; allowlisting tanınmayan exe-ni bloklayır; eyni baza konfiqurasiyası və təmiz image; EDR aktivliyi yoxlanır; laboratoriya ayrıca VLAN-da; yoluxmuş kompüterlər sıfırdan qurulur.
:::
