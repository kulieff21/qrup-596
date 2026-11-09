+++
title = "Kibertəhlükəsizlik təhdidləri; təhdid məlumatları və analitikası"
unit = "qisa"
order = 2
summary = "Mühazirənin skeleti: hər anlayış bir-iki cümlə ilə, mühazirənin sırasında. Aktorlar, hücumlar, zəifliklər, standartlar, təhdid kəşfiyyatı, IoC/TTP, STIX/TAXII/TLP/MISP."
updated = 2026-11-09

[[source]]
title = "Mühazirə 2: Kibertəhlükəsizlik təhdidləri; təhdid məlumatları və analitikası"
note = "Elmar Cabbarov, 2026–2027"
+++

Mövzu iki hissədir: təhdidlərin xəritəsi (kim, niyə, hansı üsulla) və təhdid kəşfiyyatı (bu biliyi müdafiəyə çevirmək). Universitet nümunələri şərti tədris nümunəsidir.

## Nəyi qoruyuruq

| Anlayış | Nədir |
| --- | --- |
| LMS (Learning Management System) | Tədrisin idarə edilməsi sistemi; hesab, qayda, baza, nüsxə və insanlar birlikdə sistemdir |
| Aktiv (asset) | Təşkilat üçün dəyəri olan resurs; dəyər qiymətlə ölçülmür |
| Məxfilik (confidentiality) | İcazəsiz tərəfə açılmama |
| Tamlıq (integrity) | İcazəsiz dəyişikliyə qarşı qorunma |
| Əlçatanlıq (availability) | Lazım olanda resursdan istifadə; bu üçlük CIA-dır |
| Hesabatlılıq (accountability) | Əməliyyatı konkret subyektə bağlamaq imkanı |
| İmtinanın qarşısı (non-repudiation) | Mənşə və ya qəbula dair yoxlanıla bilən sübut |
| Təhdid (threat) | Zərər verə bilən şərait və ya hadisə |
| Zəiflik (vulnerability) | İstifadə oluna bilən boşluq |
| Hücum (attack) | Boşluqdan qəsdən istifadə cəhdi |
| Risk | Ehtimal və nəticənin ağırlığı ilə bağlı qeyri-müəyyənlik |
| İnsident | Təhlükəsizliyi pozan hadisə |

Aktiv üçün sahib, məqsəd, həssaslıq, asılılıq və bərpa tələbi müəyyən edilir. Ehtimal × zərər hesabı (0,1 × 50 000 manat = 5 000 manat illik itki) zəmanətli proqnoz deyil.

## Təhdid aktorları və APT

Təhdid aktoru (threat actor) zərərli fəaliyyət göstərən şəxs və ya qrupdur; təhdid mənbəyi yanğın və səhvi də əhatə edir. Etik haker icazə ilə sınaq aparır.

| Aktor | Motiv |
| --- | --- |
| Həvəskar (skript-kiddi) | Maraq, nüfuz |
| Haktivist | Siyasi mesaj |
| Cinayətkar qrup | Pul; fidyə proqramı xidmət kimi satılır: Ransomware-as-a-Service (RaaS) |
| Dövlət dəstəkli qrup | Casusluq, sabotaj |
| Daxili pozucu (insider) | Pul, narazılıq, səhlənkarlıq |
| Kommersiya rəqibi | İqtisadi üstünlük |

Motiv davranışdan çıxarılan fərziyyədir: siyasi şüar mütləq haktivist, xarici IP dövlət sübutu deyil; atributlaşdırma (attribution) fəaliyyəti aktora bağlamaqdır və sübut tələb edir. İnkişaf etmiş davamlı təhdid (Advanced Persistent Threat, APT) uzun müddət gizli qalıb uyğunlaşan rəqibdir; dövlət demək deyil və zero-day tələb etmir (oğurlanmış parol da kifayət edə bilər). Cavab: ələ keçirilən hesab, sessiya və açarlar araşdırılır, məxfi seqment ayrılır.

## Hücumların təsnifatı

ITU-T X.800: passiv hücum məzmunu ələ keçirir və trafik analizi aparır, dəyişmir; aktiv hücum bürünmə (masquerade), təkrar göndərmə (replay), dəyişdirmə və xidmətdən imtinadır. Təsirə görə: kəsmə (interruption, əlçatanlıq), ələ keçirmə (interception, məxfilik), dəyişdirmə (modification, tamlıq), saxtalaşdırma (fabrication, autentiklik). Dördlüyü "aktiv hücum" adlandırmaq səhvdir: ələ keçirmə passivdir. Təsirə görə bölgü hansı xassənin pozulduğunu, passiv/aktiv bölgü fəaliyyətin xarakterini göstərir; bir insidentdə bir neçə xassə pozula bilər. Şifrələmə trafik analizini tam aradan qaldırmır.

Hücum vektoru (attack vector) hədəfə gedən yoldur, hücum səthi (attack surface) bütün giriş nöqtələridir (VPN, LMS, poçt, USB, API açarı, server otağı).

## Sosial mühəndislik və hesab hücumları

Sosial mühəndislik (social engineering) insanın etibarından və tələskənliyindən istifadədir; insan həmişə ən zəif halqa deyil.

| Forma | Mexanizm |
| --- | --- |
| Fişinq (phishing) | Kütləvi saxta məktub |
| Spear phishing | Şəxsə uyğun |
| Whaling | Rəhbərə yönəlmiş |
| Vişinq (vishing), smişinq (smishing), quishing | Telefon, SMS, QR kod |
| BEC (Business Email Compromise) | Real poçtdan ödəniş və ya rekvizit dəyişmə tələbi |
| Pretexting | Uydurma rol və ssenari |
| Tailgating | Səlahiyyətli şəxslə qapıdan keçmə |
| Baiting | Cəlbedici yem (tapılmış USB) |

BEC-də zərərli əlavə lazım deyil, real hesabdan gələn məktub poçt yoxlamasından keçə bilər. Deepfake səs və video rəhbəri təqlid edə bilər; ödəniş ikinci şəxslə və əvvəlcədən qeydə alınmış kanalla təsdiqlənir.

- Brute force: çoxlu kombinasiya; lüğət hücumu: ehtimallı parollar.
- Password spraying: az parol, çoxlu hesab (hesab limiti tutmur; yalnız IP həddi ortaq NAT ünvanını bloklayıb hücumçunu buraxa bilər, ona görə mənbə üzrə fərqli hesablar da sayılır).
- Credential stuffing: başqa xidmətdən sızmış cütlər.
- MFA (Multi-Factor Authentication) müxtəlif faktor kateqoriyalarını birləşdirir; MFA yorğunluğu təkrar bildirişlə təsdiq qoparır; FIDO2/WebAuthn fişinqə davamlıdır. NIST SP 800-63-4 uzun unikal parol və sızmış parolların yoxlanmasını önə çəkir.

## Şəbəkə hücumları

- Sniffing: trafikin dinlənməsi.
- Spoofing: IP, ARP (yerli IP–MAC) və DNS saxtalaşdırması.
- MITM (Man-in-the-Middle): iki tərəf arasına girib rabitəni izləmək və dəyişmək (saxta Wi-Fi); tədbirlər: seqmentləşdirmə, ARP yoxlaması, idarə olunan profil; TLS yoxlaması qoruyur, amma kilid işarəsi domenin universitetə aid olduğunu göstərmir.
- DoS (Denial of Service) xidməti əlçatmaz edir; Distributed Denial of Service (DDoS) çoxlu mənbədəndir (botnet və ya əks etdirmə). Reflection sorğunu qurbanın saxta ünvanı ilə üçüncü tərəfə göndərir, cavab böyükdürsə gücləndirmə (amplification) olur. Kampus firewall-ı dolmuş xarici kanalı boşalda bilmir; operator, sürət limiti, keş, WAF və DNSSEC kimi tədbirlər işlədilir, CAPTCHA tam həll deyil.

## Veb, zərərli proqram və təchizat zənciri

| Hücum | Mexanizm |
| --- | --- |
| SQL injection | Giriş SQL məntiqinə qarışır; parametrli sorğu |
| XSS (Cross-Site Scripting) | Etibarsız məzmun brauzerdə icra olunur; kodlaşdırma, HttpOnly |
| CSRF (Cross-Site Request Forgery) | Brauzerin sessiyası sui-istifadə olunur; token, SameSite |
| Giriş nəzarətinin pozulması | Obyekt hüququ serverdə yoxlanmır (OWASP A01 Broken Access Control) |
| SSRF (Server-Side Request Forgery) | Sorğunu server göndərir |
| Fayl yükləmə | Yüklənmiş fayl icra olunur |

Obyekt identifikatorunu dəyişib başqasının sənədini açmaq avtorizasiya problemidir. Virus faylla yayılır, soxulcan (worm) şəbəkə ilə özü yayılır, Troyan (Trojan) faydalı proqram görüntüsü altında gizlənir. Fidyə proqramı (ransomware) şifrələyib ödəniş tələb edir; ehtiyat nüsxə sızmanı geri qaytarmır. Təchizat zənciri hücumu (supply chain attack) etibarlı təchizatçı və ya yeniləmə kanalı vasitəsilə gəlir; müdafiə proqram komponentləri siyahısıdır (Software Bill of Materials, SBOM).

## Zəifliklər və prioritet

- CVE (Common Vulnerabilities and Exposures): ictimai zəifliyin identifikatoru (CVE-2021-44228, Log4Shell).
- CWE (Common Weakness Enumeration): zəiflik növü (CWE-89, SQL injection).
- Zero-day: müdafiə hazır olmayan zəiflik; vəziyyət dəqiq yazılır, çoxdan düzəldilmiş zəifliyi zero-day adlandırmaq olmaz.
- CVSS (Common Vulnerability Scoring System) v4.0: texniki ciddilik, 0–10; qruplar Base, Threat, Environmental, Supplemental.
- EPSS (Exploit Prediction Scoring System): yaxın 30 gündə istismar ehtimalı (0,20 = 20 faiz; bu universitetin sındırılma ehtimalı deyil).
- KEV (Known Exploited Vulnerabilities): CISA-nın real istismar kataloqu; siyahıda olmamaq zəmanət deyil.

:::exam
Yalnız CVSS-ə baxmaq səhvdir. Prioritet: real istismar (KEV, EPSS), İnternetə açıqlıq, aktivin kritikliyi. İnternetə açıq 8,1 ballı KEV zəifliyi təcrid edilmiş 9,8 ballı VM-dən əvvəl düzəlir.
:::

## Tədbirlər, siyasət, standartlar

Tədbirlər hüquqi, təşkilati, prosedur və texnikidir. İnsidentə cavab komandası CERT/CSIRT adlanır. İdentifikasiya özünü adlandırmaq, autentifikasiya yoxlamaq, avtorizasiya icazə verməkdir; jurnallaşdırma yazır, audit yoxlayır. Firewall zonalar arası trafiki süzür; EDR (Endpoint Detection and Response) son qurğuda davranışı görür. Şifrələmə məzmunu oxunmaz edir; steqanoqrafiya (steganography) varlığı gizlədir; "süni intellekt şifrələməsi" standart deyil.

- ISO/IEC 27001:2022 idarəetmə sistemi, 27002:2022 tədbirlər (93, dörd qrup), 27005:2022 risk idarəsi, 15408 məhsul qiymətləndirməsi.
- NIST CSF 2.0 (Govern, Identify, Protect, Detect, Respond, Recover), NIST SP 800-61 Rev. 3 insidentə cavab, CIS Controls v8.1 prioritet tədbirlər.
- Narıncı kitab (Orange Book) 1985 Trusted Computer System Evaluation Criteria (TCSEC) tarixi sənədidir.
- Common Criteria (Ümumi meyarlar) funksional və zəmanət tələblərini ayırır; siniflər FAU, FIA, FRU, FCO, FPR, FDP, FPT, FCS, FMT, FTA, FTP.
- Siyasət üç səviyyəlidir (rəhbərlik, qaydalar, sazlamalar); prinsiplər: sadəlik, sistemlilik, dərinlik üzrə müdafiə, fasiləsizlik, düşünülmüş kafilik, uyğunlaşma, mexanizmin açıqlığı.

## Təhdid kəşfiyyatı

Kibertəhdid kəşfiyyatı (Cyber Threat Intelligence, CTI) yoxlanmış, kontekstli, qərara yarayan bilikdir; xam məlumat hələ kəşfiyyat deyil. Mənbələr həm xarici, həm daxilidir (NIST SP 800-150).

| Səviyyə | Kimin üçün |
| --- | --- |
| Strateji | Rəhbərlik, risk və resurs qərarı |
| Əməliyyat | CSIRT; konkret kampaniya |
| Taktiki | SOC rəhbəri; TTP |
| Texniki | SOC, firewall, SIEM, EDR; IoC |

:::exam
İmtahanda: taktiki = TTP, texniki = IoC (CompTIA IoC-ləri taktiki sayır). Ən etibarlı açar auditoriyadır.
:::

## Həyat dövrü

Altı mərhələ: tələblər (Priority Intelligence Requirement, PIR: qərar üçün çatışmayan bilik), toplama (hər sual üçün mənbə), emal (format, dublikat, vahid vaxt; domen, IP və URL eyni obyekt deyil), təhlil, yayma (alıcıya uyğun forma və TLP etiketi), əks-əlaqə (hansı qərar dəyişdi); əks-əlaqə yeni tələblərə çevrilir. Təhlildə mənbənin etibarlılığı məlumatın doğruluğundan, etibar dərəcəsi ehtimaldan ayrılır.

## IoC, IoA, TTP, ATT&CK

- IoC (Indicator of Compromise): heş, domen, IP kimi texniki əlamət; uyğunluq sındırılma sübutu deyil.
- IoA (Indicator of Attack): davranış ardıcıllığı.
- TTP (Tactics, Techniques and Procedures): məqsəd, üsul, icra forması.
- Ağrı piramidası (Pyramid of Pain, Bianco): heş, IP, domen, artefakt, alət, TTP; nə qədər yuxarı bloklasan, hücumçuya bir o qədər baha başa gəlir.
- MITRE ATT&CK taktika və texnikalarla davranış bazasıdır (T1566 fişinq); Cyber Kill Chain mərhələli modeldir, hər hadisə bu sıra ilə getmir.

## Mənbələr, OSINT, qərəzlər

Açıq mənbə kəşfiyyatı (Open-Source Intelligence, OSINT) ictimai məlumatdan bilik çıxarır; mənbələr açıq hesabatlar, daxili jurnallar, kommersiya məlumat axını (feed), CERT, ISAC və tərəfdaşlardır. Qərəzlər: təsdiqləmə (confirmation bias), lövbərlənmə (anchoring), əlçatanlıq (availability bias). Süni intellekt köməkçidir, amma uydura bilər, zəhərlənə bilər, konseptin sürüşməsindən (concept drift) zəifləyir; qərarı analitik verir.

## STIX, TAXII, TLP, MISP

- STIX (Structured Threat Information Expression): məlumatın formatı.
- TAXII (Trusted Automated Exchange of Intelligence Information): ötürmə protokolu.
- MISP: açıq mənbəli paylaşma platforması; hadisə (event) və atributlarla işləyir.
- TLP (Traffic Light Protocol) 2.0: TLP:RED yalnız konkret alıcılar; TLP:AMBER+STRICT yalnız öz təşkilatı; TLP:AMBER təşkilat və müştərilər; TLP:GREEN icma; TLP:CLEAR məhdudiyyətsiz (köhnə TLP:WHITE).

## Universitetdə CTI

CTI poçt şlüzünə, SIEM-ə və EDR-ə bağlanır; SOC xəbərdarlığı araşdırır, CSIRT insidenti idarə edir. Avtomatlaşdırma geri çevrilə bilən işlərdən başlayır. Keyfiyyət indikator sayı ilə yox, tələbə uyğunluq, aktuallıq, dəqiqlik (10/40 = 25 faiz) və qərara təsirlə ölçülür.
