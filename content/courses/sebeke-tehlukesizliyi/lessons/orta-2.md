+++
title = "Kibertəhlükəsizlik təhdidləri; təhdid məlumatları və analitikası"
unit = "orta"
order = 2
summary = "Hər anlayış izahla: aktivlər və risk, aktorlar və APT, hücum növləri, sosial mühəndislik, şəbəkə və veb hücumları, zəifliklərin prioritetləşdirilməsi, standartlar, təhdid kəşfiyyatı, həyat dövrü, IoC/TTP, OSINT, STIX/TAXII/TLP/MISP."
updated = 2026-11-09

[[source]]
title = "Mühazirə 2: Kibertəhlükəsizlik təhdidləri; təhdid məlumatları və analitikası"
note = "Elmar Cabbarov, 2026–2027"
+++

Mövzunun iki hissəsi var: təhdidlərin xəritəsi (kim, niyə, hansı üsulla hücum edir) və təhdid kəşfiyyatı (bu biliyi müdafiəyə çevirmək). Universitet (LMS, tələbə bazası, kitabxana, yataqxana Wi-Fi-si) nümunələri şərti tədris nümunəsidir.

## Nəyi qoruyuruq: sistem, informasiya və risk

İnformasiya sistemi aparat və proqramla yanaşı insanları, iş qaydalarını və məlumatın özünü də əhatə edir. LMS (Learning Management System) yalnız veb server deyil: hesab, qiymətləndirmə qaydası, baza, ehtiyat nüsxə və nəticəni təsdiqləyən əməkdaş eyni prosesdir. Aktiv (asset) təşkilat üçün dəyəri olan resursdur; dəyər qiymətlə ölçülmür: qiymət cədvəlinin kiçik faylı serverdən həssas ola bilər. Hər aktiv üçün sahib, məqsəd, həssaslıq, asılılıq və bərpa tələbi müəyyən edilir. Analitik məlumatın düzgünlüyünü, aktuallığını, dolğunluğunu və suala uyğunluğunu ayrıca yoxlayır.

**Xassələr.** Məxfilik (confidentiality), tamlıq (integrity) və əlçatanlıq (availability) CIA üçlüyüdür. Bütöv model bunlara autentiklik, hesabatlılıq (accountability: əməliyyatı subyektə bağlamaq; ortaq admin hesabı bunu zəiflədir), imtinanın qarşısının alınması (non-repudiation: mənşə və ya qəbula dair yoxlanıla bilən sübut; "təxirəsalınmazlıq" deyil), etibarlılıq və fiziki təhlükəsizliyi də əlavə edir.

| Anlayış | Mənası | Nümunə (keçmiş əməkdaşın açıq qalmış VPN hesabı) |
| --- | --- | --- |
| Təhdid (threat) | Arzuolunmaz nəticəyə səbəb ola bilən şərait və ya hadisə | Hesabdan məlumat oğurlamaq istəyən tərəf |
| Zəiflik (vulnerability) | İstifadə oluna bilən boşluq | Hesabın vaxtında bağlanmaması |
| Hücum (attack) | Boşluqdan qəsdən istifadə cəhdi | Oğurlanmış parolla giriş cəhdi |
| Risk | Ehtimal və nəticənin ağırlığı ilə bağlı qeyri-müəyyənlik | Məlumat yayılması, qeydiyyatın dayanması |
| İnsident | Təhlükəsizliyi pozan hadisə | Tələbə bazasının ixracı |

Risk bəzən ehtimal × zərər kimi hesablanır: ehtimal 0,1, zərər 50 000 manat, gözlənilən illik itki 5 000 manat. Bu, zəmanətli proqnoz deyil; fərziyyələr açıq yazılmalıdır.

## Təhdid aktorları və APT

Təhdid aktoru (threat actor) zərərli fəaliyyət göstərən şəxs, qrup və ya təşkilatdır; təhdid mənbəyi daha geniş anlayışdır (yanğın, enerji kəsilməsi, səhv). Disk nasazlığı əlçatanlıq insidentidir, amma hücum deyil. Aktorlar yaşa və təhsilə görə ayrılmır; etik haker icazə ilə sınaq aparır.

| Aktor | Motiv | İmkan |
| --- | --- | --- |
| Həvəskar (skript-kiddi) | Maraq, nüfuz | Aşağı, hazır alətlər |
| Haktivist | Siyasi, ideoloji | Aşağı–orta, DDoS, sayt dəyişdirmə |
| Cinayətkar qrup | Pul | Orta–yüksək, ransomware, BEC |
| Dövlət dəstəkli | Casusluq, sabotaj | Çox yüksək, uzunmüddətli |
| Daxili pozucu (insider) | Pul, narazılıq, səhlənkarlıq | Qanuni giriş |
| Kommersiya rəqibi | İqtisadi üstünlük | Orta, sənaye casusluğu |

Fidyə proqramının xidmət kimi satılması (Ransomware-as-a-Service, RaaS) modelində proqramı yazan, ilkin giriş satan və məlumat çıxaran tərəflər ayrı ola bilər. Motiv davranışdan çıxarılan fərziyyədir: siyasi şüar mütləq haktivist demək deyil, xarici IP dövlət mənsubiyyəti sübutu deyil. Atributlaşdırma (attribution) fəaliyyəti konkret aktora bağlamaqdır və alternativ izahların yoxlanmasını tələb edir.

İnkişaf etmiş davamlı təhdid (Advanced Persistent Threat, APT) uzun müddət fəaliyyət göstərən, imkanlarını uyğunlaşdıran və girişini saxlayan rəqibdir. APT dövlət mənsubiyyəti demək deyil və hər mərhələdə zero-day tələb etmir: oğurlanmış parol və standart idarəetmə aləti də kifayət edə bilər. Cavab yalnız domeni bloklamaq deyil: ələ keçirilmiş hesab, sessiya və açarlar araşdırılır, məxfi seqment ayrılır, imtiyazlı girişə ayrıca nəzarət qoyulur.

## Hücumların təsnifatı və hücum səthi

ITU-T X.800: **passiv** hücumlar (məzmunun ələ keçirilməsi, trafik analizi) məlumatı dəyişmir, aşkarlamaq çətindir; şifrələmə trafik analizini tam aradan qaldırmır. **Aktiv** hücumlar: başqasının kimliyinə bürünmə (masquerade), təkrar göndərmə (replay), mesajın dəyişdirilməsi, xidmətdən imtina. Replay-a qarşı birdəfəlik dəyər, vaxt məhdudiyyəti və sessiya nəzarəti kömək edir.

| Təsir forması | Pozulan xassə | Qeyd |
| --- | --- | --- |
| Kəsmə (interruption) | Əlçatanlıq | Adətən aktiv |
| Ələ keçirmə (interception) | Məxfilik | Passiv ola bilər |
| Dəyişdirmə (modification) | Tamlıq | Aktiv |
| Saxtalaşdırma (fabrication) | Autentiklik | Aktiv |

:::exam
Dördlüyü bütövlükdə "aktiv hücum" adlandırmaq səhvdir, çünki ələ keçirmə passivdir. Təsirə görə bölgü (hansı xassə) ilə fəaliyyətə görə bölgü (passiv/aktiv) ayrı suallardır.
:::

Hücum vektoru (attack vector) rəqibin hədəfə çatdığı yoldur. Hücum səthi (attack surface) bütün giriş nöqtələridir: açıq VPN, LMS, poçt, USB, bulud API açarı, server otağı qapısı. Etibar sərhədi fərqli güvən fərziyyəli zonaları ayırır; autentifikasiya keçən istifadəçiyə hər şeyə etibar verilmir. Vektor təhlili: aktiv, ona çatan interfeyslər, yoxlamalar, girişdən sonrakı keçidlər.

## Sosial mühəndislik və hesab hücumları

Sosial mühəndislik (social engineering) insanın etibarından, tələskənliyindən və ya qaydanı yanlış anlamasından istifadədir. İnsan həmişə ən zəif halqa deyil: işçi fişinqi ilk aşkar edən də ola bilər, zəif layihələndirilmiş parol bərpası isə təcrübəli işçini də aldadır.

| Forma | Mexanizm |
| --- | --- |
| Fişinq (phishing) | Kütləvi saxta məktub |
| Hədəfli fişinq (spear phishing) | Şəxsə uyğunlaşdırılmış |
| Whaling | Rəhbərlərə yönəlmiş |
| Vişinq (vishing) / smişinq (smishing) / quishing | Telefon / SMS / QR kod |
| BEC (Business Email Compromise) | Real poçtdan ödəniş və ya rekvizit dəyişmə tələbi |
| Pretexting | Uydurma rol və ssenari |
| Tailgating | Səlahiyyətli şəxslə qapıdan keçmə |
| Baiting | Cəlbedici yem (tapılmış USB) |

BEC-də zərərli əlavə lazım deyil; real hesabdan gələn məktub poçt yoxlamasından keçə bilər. Rekvizit dəyişikliyi əvvəldən qeydə alınmış kanalla və ikinci şəxslə təsdiqlənir. Deepfake səs və video rəhbəri təqlid edə bilər: tanış üz ödəniş səlahiyyəti deyil. Təlimdə işçi səhvi gizlətmədən bildirə bilməlidir.

| Parol hücumu | Mexanizm |
| --- | --- |
| Brute force | Çoxlu kombinasiya |
| Lüğət hücumu | Ehtimallı söz və variantlar |
| Password spraying | Az parol, çoxlu hesab |
| Credential stuffing | Başqa xidmətdən sızmış cütlər |

Püskürtməni hesab üzrə hədd tutmur (bir mənbədən 60 hesaba birər uğursuz giriş); mənbə üzrə fərqli hesablar da sayılmalıdır. Yalnız IP həddi ortaq NAT-ı bloklaya bilər. MFA (Multi-Factor Authentication) fərqli faktor kateqoriyalarını birləşdirir (bilik, sahiblik, insanın özü); parol və PIN eyni kateqoriyadır. MFA yorğunluğu təkrar bildirişlə təsdiq qoparır; aralıq proksi sessiya tokenini oğurlaya bilər. FIDO2/WebAuthn fişinqə daha davamlıdır. NIST SP 800-63-4 (2025) uzun unikal parol, sızmış parolların yoxlanması və cəhd limitini önə çəkir; pozuntu olmadan məcburi dövri dəyişiklik zəmanət deyil.

## Şəbəkə hücumları və xidmətdən imtina

- **Sniffing**: paketlərin dinlənməsi; kommutatorlu şəbəkədə görünürlük bağlantı yerindən asılıdır.
- **Spoofing**: IP (cavab almaq və TCP sessiyası mümkün olmaya bilər), ARP (yerli seqmentdə yanlış IP–MAC), DNS cavabının saxtalaşdırılması. Hamısını "IP dəyişmək" kimi izah etmək mexanizmi gizlədir.
- **MITM (Man-in-the-Middle, on-path)**: iki tərəf arasına girib rabitəni izləmək və dəyişmək; məsələn, saxta Wi-Fi nöqtəsi. Düzgün TLS yoxlaması qoruyur, amma istifadəçi sertifikat xəbərdarlığını keçərsə zəifləyir.

TLS bağlantısı veb xidmətin təhlükəsiz olduğunu göstərmir: hücumçu öz domeni üçün etibarlı sertifikat ala bilər, kilid işarəsi domenin universitetə aid olduğunu təsdiqləmir. Tədbirlər: TLS, seqmentləşdirmə və ARP yoxlaması, idarə olunan Wi-Fi profili, giriş/çıxış ünvan süzgəci, etibarlı resolver və DNSSEC (məzmunu şifrələmir).

Xidmətdən imtina (Denial of Service, DoS) xidməti əlçatmaz edir; Distributed Denial of Service (DDoS) çoxlu mənbədən gəlir (botnet və ya əks etdirmə). Hücum həcm (kanal dolur), protokol vəziyyəti (sessiya cədvəli tükənir) və ya tətbiq səviyyəsində (az trafiklə bahalı sorğu) olur. Əks etdirmədə (reflection) sorğu qurbanın saxta ünvanı ilə üçüncü tərəfə gedir; cavab sorğudan böyükdürsə gücləndirmə (amplification) yaranır (100 baytlıq sorğuya 2 000 baytlıq cavab: nisbət 20; protokola görə dəyişir).

:::reveal Xarici kanal 1 Gbit/s, hücum axını 3 Gbit/s olduqda kampus firewall-ı niyə kömək etmir?
Kanal firewall-a çatmamış operatorun xəttində dolur; qanuni sorğuların bir hissəsi orada itir. Süzmə operator və ya yuxarı şəbəkə səviyyəsində aparılmalıdır. Hazırlıq: operatorla əlaqə, trafik təmizləmə, tətbiqdə sürət limiti, keş, WAF qaydaları. Bir IP-yə sərt limit ortaq çıxışdakı qanuni tələbələri kəsə bilər; CAPTCHA bütün protokol hücumlarını dayandırmır.
:::

İmtahan vaxtı trafik artımı ilə hücumu ayırmaq üçün hesabların normal autentifikasiyası, müxtəlif kurslara baxış, eyni bahalı yola təkrar sorğular və uğursuz nəticələrə baxılır.

## Veb, zərərli proqram və təchizat zənciri

| Hücum | Mexanizm | Tədbir |
| --- | --- | --- |
| SQL injection | Giriş SQL sorğusunun məntiqinə qarışır | Parametrli sorğu, məhdud baza hüququ |
| XSS (Cross-Site Scripting) | Etibarsız məzmun brauzerdə icra olunur | Kontekstə uyğun kodlaşdırma; HttpOnly tam həll deyil |
| CSRF (Cross-Site Request Forgery) | Brauzer sessiyası başqa saytın sorğusu üçün istifadə olunur | CSRF tokeni, SameSite |
| Giriş nəzarətinin pozulması | Obyektə icazə serverdə yoxlanmır | Hər sorğuda hüquq yoxlaması |
| SSRF (Server-Side Request Forgery) | Sorğunu server göndərir | Çıxışı və ünvanları məhdudlaşdırmaq |
| Fayl yükləmə | Yüklənmiş fayl icra olunur | İcradan ayrı saxlama, tip və ölçü yoxlaması |

CSRF-də sui-istifadə obyekti brauzerin sessiyası, SSRF-də serverin şəbəkə çıxışıdır. Obyekt identifikatorunu dəyişib başqasının sənədini açmaq autentifikasiya yox, avtorizasiya problemidir (OWASP Top 10:2025, A01 Broken Access Control).

Virus daşıyıcı fayla bağlı yayılır; soxulcan (worm) şəbəkə ilə özü yayılır; Troyan (Trojan) faydalı proqram görüntüsü altında zərər verir; casus proqram məlumat toplayır, açarbasma qeydedicisi simvolları izləyir. Kateqoriyalar kəsişə bilər. Fidyə proqramı (ransomware) şifrələməklə və məlumatı yaymaqla hədələməklə ödəniş tələb edir; ehtiyat nüsxə məxfilik pozuntusunu geri qaytarmır, əsas admin hesabına bağlı nüsxə də silinə bilər.

Təchizat zənciri hücumunda (supply chain attack) etibarlı təchizatçı, asılılıq, qurma prosesi və ya yeniləmə kanalı vasitə olur; rəqəmsal imza zərərsizlik zəmanəti deyil (OWASP A03 Software Supply Chain Failures; konspektdə SolarWinds 2020, 3CX 2023). Müdafiə: asılılıq inventarı, proqram komponentləri siyahısı (Software Bill of Materials, SBOM), təsdiqlənmiş mənbələr, mərhələli yeniləmə. SBOM komponentin mövcudluğunu göstərir, funksiyanın istismar oluna bildiyini yox.

## Zəifliklər və düzəliş prioriteti

- **CVE** (Common Vulnerabilities and Exposures): ictimai zəifliyə identifikator (CVE-2021-44228, Log4Shell). Balı və ya universitetdə istismarı bildirmir; hər zəifliyin CVE-si olmur.
- **CWE** (Common Weakness Enumeration): zəiflik **növü** (CWE-89, SQL injection); bir CWE-yə çoxlu CVE uyğun gəlir. CVE düzəlişi izləməyə, CWE səbəbi öyrənməyə kömək edir.
- **Zero-day**: sərhədi mənbələrdə fərqlidir (istehsalçı bilmir / istismar zamanı düzəliş yoxdur); hesabatda dəqiq vəziyyət yazılır. Çoxdan düzəldilmiş zəifliyi yeniləməyən universitet üçün zero-day demək olmaz.
- **CVSS v4.0** (Common Vulnerability Scoring System): texniki ciddilik, 0–10. Qruplar: əsas (Base), təhdid (Threat), mühit (Environmental), əlavə (Supplemental; yekun bala təsir etmir). CVSS-B, BT, BE, BTE hansı qrupların daxil olduğunu göstərir.
- **EPSS** (Exploit Prediction Scoring System): yaxın 30 gündə istismar müşahidəsi ehtimalı; 0,20 = 20 faiz, bu universitetin sındırılma ehtimalı deyil; persentil nisbi sıralamadır.
- **KEV** (Known Exploited Vulnerabilities, CISA): real istismar kataloqu; siyahıda olmaq güclü siqnaldır, olmamaq zəmanət deyil.

:::exam
Yalnız CVSS-ə baxmaq səhvdir. Prioritet: real istismar olunurmu (KEV, EPSS), sistem İnternetə açıqdırmı, aktiv nə qədər kritikdir. "Ən böyük balı əvvəl yamaq" qaydası bunları itirir.
:::

Nümunə: uzaq giriş şlüzü (CVSS 8,1, KEV-də, İnternetə açıq) təcili düzəlir və kompromitasiya yoxlanır; təcrid edilmiş sınaq VM-i (9,8) izolyasiya yoxlanıb planlı düzəlir; tələbə bazası tətbiqi (6,5, daxildə istismar əlaməti) insident araşdırması və məhdudlaşdırma tələb edir. Təcili tədbir söndürmə, giriş daraltma, ayırma ola bilər. Yamaq artıq daxil olmuş hücumçunun sessiyasını və hesabını silmir. Düzəlişdən sonra kodun yeniləndiyi, yenidən başlatma və LMS axınları yoxlanır.

## Tədbirlər, siyasət və standartlar

Müdafiə hüquqi, təşkilati, prosedur və texniki tədbirləri birləşdirir. Hesab işə qəbulda verilir, vəzifə dəyişəndə yenilənir, çıxışda ləğv olunur; fiziki mühafizə və diskin təhlükəsiz atılması şəbəkədən yan keçən sızmanı bağlayır. İnsidentə cavab komandası (CERT və CSIRT) sübutu qoruyur, yayılmanı məhdudlaşdırır, bərpanı əlaqələndirir; rəhbərlik, hüquq və kommunikasiya əlaqələndiriciləri və xarici CERT/CSIRT kanalları əvvəlcədən təyin edilir.

İdentifikasiya özünü adlandırmaq, autentifikasiya yoxlamaq, avtorizasiya icazəni müəyyən etməkdir. Jurnallaşdırma yazmaq, audit yoxlamaqdır; parol və sessiya tokeni jurnala yazılmır. Firewall zonalar arası trafiki süzür; antivirus və EDR fayl və davranışı, poçt süzgəci spam və zərərli məzmunu yoxlayır; heç biri giriş nəzarəti və yeniləməni əvəz etmir. Şifrələmə simmetrik (eyni gizli açar) və asimmetrik (açıq/gizli açar) ola bilər; rəqəmsal imza mənşə və tamlığı yoxlayır, məxfilik vermir. Steqanoqrafiya (steganography) məlumatın mövcudluğunu gizlədir; "süni intellekt şifrələməsi" standart kateqoriya deyil.

Azərbaycanın informasiya, fərdi məlumatlar, informasiya əldə etmə, elektron imza qanunları istinad edilir; dövlət sirri, kommersiya sirri və biometrik informasiya qanunlarının tətbiqi məlumatdan asılıdır. Monitorinqin məqsədi, saxlanma müddəti və giriş səlahiyyəti yazılı müəyyən edilir; kəşfiyyat adı sərhədsiz şəxsi məlumat toplamağa icazə deyil.

| Sənəd | İstiqamət |
| --- | --- |
| ISO/IEC 27001:2022 | İnformasiya təhlükəsizliyinin idarəetmə sisteminə tələblər |
| ISO/IEC 27002:2022 | 93 tədbir, dörd mövzu qrupu |
| ISO/IEC 27005:2022 | Risk idarəsi |
| NIST CSF 2.0 (2024) | Govern, Identify, Protect, Detect, Respond, Recover |
| NIST SP 800-61 Rev. 3 (2025) | İnsidentə cavab və risk idarəsi |
| CIS Controls v8.1 | Prioritet tədbirlər |
| ISO/IEC 15408 | Məhsulun təhlükəsizlik qiymətləndirilməsi |

1985-ci il Trusted Computer System Evaluation Criteria (TCSEC), "Narıncı kitab" (Orange Book), D, C, B, A bölgüləri ilə tarixi sənəddir; bütün standartların başlanğıcı və ya bugünkü universal sertifikat deyil. Common Criteria (Ümumi meyarlar) funksional tələbi (məhsul nə etməlidir) zəmanət tələbindən (niyə etibar edək) ayırır. Funksional siniflər: FAU audit, FIA identifikasiya/autentifikasiya, FRU resurs istifadəsi, FCO rabitədə imtinanın qarşısı, FPR məxfilik, FDP istifadəçi məlumatı, FPT təhlükəsizlik funksiyalarının mühafizəsi, FCS kriptoqrafik dəstək, FMT idarəetmə, FTA giriş, FTP etibarlı kanal. Qiymətləndirmə konkret məhsul və versiyaya aiddir.

Siyasət nəyin qorunduğunu, məsulları, qəbul edilən riski və yoxlamanı müəyyən edir (yuxarı: rəhbərlik məqsədləri; orta: LMS, poçt, uzaq giriş qaydaları; aşağı: sazlamalar və təlimatlar). Prinsiplər: sadəlik, sistemlilik, komplekslik və dərinlik üzrə müdafiə (qatlar eyni hesabdan idarə olunmamalı), fasiləsizlik, düşünülmüş kafilik (xərc, çətinlik, zərər müqayisəsi), uyğunlaşma, mexanizmin açıqlığı (alqoritm məlum olsa da açar gizli qalır).

## Təhdid kəşfiyyatı və qərarın səviyyəsi

Kibertəhdid kəşfiyyatı (Cyber Threat Intelligence, CTI) yoxlanmış, kontekstləşdirilmiş, qərara yarayan bilikdir. "Bu IP-dən bağlantı gəldi" müşahidədir; "bu bağlantı təsdiqlənmiş zərərli domenlə əlaqəlidir, serverdə naməlum proses başlayıb, ayırmaq araşdırılmalıdır" analitik nəticədir. Mənbə təkcə İnternet deyil: öz jurnallarımız, insident araşdırması, zərərli proqram analizi, tərəfdaş xəbərdarlığı (NIST SP 800-150); məqsəd yalnız önləmə deyil, aşkarlama və cavabdır.

| Səviyyə | Məzmun | Auditoriya |
| --- | --- | --- |
| Strateji | Uzunmüddətli trend, geosiyasət, risk | Rəhbərlik |
| Əməliyyat | Konkret kampaniya: kim, nə vaxt, kimə | CSIRT, təhdid ovçuları |
| Taktiki | TTP: taktika, texnika, prosedur | SOC rəhbəri, arxitektorlar |
| Texniki | IoC: IP, domen, URL, heş (tez köhnəlir) | SOC analitikləri, firewall, SIEM, EDR |

:::exam
Bəzi mənbələr (məs. CompTIA) IoC-ləri "taktiki" sayır. İmtahanda müəllimin bölgüsü: taktiki = TTP, texniki = IoC. Ən etibarlı açar auditoriyadır: rəhbər üçün strateji, maşına yüklənən texniki. İdarəetmənin strateji/taktiki/operativ səviyyələri ilə qarışdırma.
:::

## Kəşfiyyatın həyat dövrü

:::figure
src = "m02-1.png"
alt = "Kəşfiyyatın həyat dövrünün altı mərhələsi və əks-əlaqə oxu."
caption = "Əks-əlaqə tələblərin yenilənməsinə qayıdır."
:::

1. **Tələblər**: Priority Intelligence Requirement (PIR) qərar üçün çatışmayan biliyi ifadə edir ("bütün hücumları izləmək" tələb deyil; "semestr qeydiyyatında hesab ələ keçirilməsinin hansı yolları bizdə işləyər?" tələbdir).
2. **Toplama**: hər sual üçün mənbə (hesab oğurluğu: poçt şlüzü, identifikasiya platforması).
3. **Emal**: format, dublikat, vahid vaxt; domen, IP və URL eyni obyekt deyil. Eyni hesabatdan götürülən üç indikator üç müstəqil təsdiq deyil.
4. **Təhlil**: mənbənin etibarlılığı ilə məlumatın doğruluğu ayrı qiymətləndirilir; alternativ izahlar yoxlanır (DNS uyğunluğu sorğunu göstərir, yoluxmanı yox).
5. **Yayma**: alıcıya uyğun forma, müşahidə və hazırlanma vaxtı ayrı, TLP etiketi.
6. **Əks-əlaqə**: hansı qərar dəyişdi, yanlış müsbət oldumu; IP-yə görə kitabxana bloklanıbsa, müddət və bloklama prosesi düzəldilir.

Analitik məhsulun sahələri: sual və əhatə, müşahidə, qiymətləndirmə, etibar dərəcəsi, tədbir, vaxt və paylaşma. Etibar dərəcəsi ilə ehtimal ayrıdır: hadisə ehtimallı, amma mənbələr zəif ola bilər.

## IoC, IoA, TTP və davranış

- **IoC** (Indicator of Compromise): heş, domen, IP, reyestr yolu kimi texniki əlamət; uyğunluq araşdırmanın başlanğıcıdır, sındırılmanın sübutu deyil. Müşahidə tarixi, mənbə, etibar və yenidən baxılma vaxtı saxlanır.
- **IoA** (Indicator of Attack): davranış ardıcıllığı (ofis sənədindən skript, sonra xarici əlaqə); sərhədi platformalarda eyni deyil.
- **TTP** (Tactics, Techniques and Procedures): taktika məqsəd (ilkin giriş), texnika üsul (fişinq), prosedur konkret icra (saxta konfrans səhifəsi).

:::figure
src = "m02-2.png"
alt = "Ağrı piramidası: aşağıdan yuxarı heş, IP, domen, artefakt, alət, TTP."
caption = "Ağrı piramidası (D. Bianco, 2013)."
:::

Ağrı piramidası (Pyramid of Pain) göstərir ki, nə qədər yuxarıdakı əlamət bloklanırsa, hücumçu üçün dəyişmə bir o qədər "ağrılı" olur. Heşi bir baytla, IP-ni dəqiqələrlə dəyişmək olur; alətləri və TTP-ni dəyişmək bütün iş üsulunu dəyişmək deməkdir. Yuxarı pilləyə keçmək aşağıları ləğv etmir. Paylaşılan bulud IP-sinin bütövlükdə bloklanması kitabxananı da kəsə bilər; dar domen/URL qaydası və ya monitorinq daha uyğundur.

MITRE ATT&CK müşahidə olunan davranışı taktika (niyə) və texnika (necə) ilə təsvir edir: T1566 fişinq, T1078 etibarlı hesablar, T1110.003 parol püskürtməsi. Xəritədə rənglənmək aşkarlamanın işlədiyini sübut etmir; versiya saxlanmalıdır (v19 Defense Evasion-ı Stealth və Defense Impairment-ə ayırıb). Cyber Kill Chain (kəşfiyyat, silahlanma, çatdırılma, istismar, quraşdırma, idarəetmə, məqsədə çatma) hücumun harada kəsiləcəyini düşünmək üçündür; hər real hadisə bu sıra ilə getmir, ATT&CK də məcburi ardıcıllıq deyil.

## Mənbələr, OSINT və analitik səhvlər

Açıq mənbə kəşfiyyatı (Open-Source Intelligence, OSINT) ictimai əlçatan məlumatdır (hesabatlar, istehsalçı bildirişləri, sertifikat qeydləri, VirusTotal, AbuseIPDB); açıq olması düzgün olması demək deyil, lisenziya və şəxsi məlumat yoxlanır. Daxili jurnallar universitetə uyğunluğu göstərir; kommersiya məlumat axını (feed) keyfiyyəti obyekt sayı ilə ölçülmür; milli və sektor CERT/CSIRT-ləri, ISAC, tərəfdaşlar kontekst verir. Şübhəli saytı iş kompüterindən açmaq olmaz: əvvəl passiv mənbələr, aktiv yoxlama təcrid olunmuş mühitdə. Fayl reputasiya xidmətinə sənəd yükləmək paylaşmadır; yerli heş (`sha256sum`) məzmunu ötürmür.

| Qərəz | Mənası | Qarşı tədbir |
| --- | --- | --- |
| Təsdiqləmə (confirmation bias) | İlkin fikrə uyğun faktları seçmək | Zidd sübutu ayrıca yazmaq |
| Lövbərlənmə (anchoring) | İlk IP və ya qrup adına bağlanmaq | Hesab, cihaz, zaman əlaqələri |
| Əlçatanlıq (availability bias) | Son oxunan hadisəni hər insidentə tətbiq etmək | Əvvəl müşahidəni təsvir etmək |

Digər: avtomatlaşdırmaya etibar, seçmə qərəzi (yalnız EDR-li cihazlar). Alternativ fərziyyələr cədvəllə müqayisə olunur; bir güclü zidd sübut çox təsdiqləyicidən çox çəkir.

Süni intellekt qruplaşdırma, tərcümə, oxşar hesabat tapmaq və prioritetləşdirmə üçün faydalıdır, amma model mövcud olmayan CVE yarada bilər. Hesabatdakı mətn model üçün məlumatdır, təlimat deyil (prompt inyeksiyası). Öyrənmə məlumatının zəhərlənməsi və konseptin sürüşməsi (concept drift: imtahan mövsümündə gecə girişləri artır) yanlış nəticə verir. Yüksək təsirli qərarı analitik əsaslandırır.

## STIX, TAXII, TLP və MISP

**STIX 2.1** (Structured Threat Information Expression) məlumatın necə ifadə olunduğunu (indikator, kampaniya, zərərli proqram, əlaqə obyektləri), **TAXII 2.1** (Trusted Automated Exchange of Intelligence Information) onun HTTPS üzərindən necə ötürüldüyünü təsvir edir. STIX TAXII olmadan da ötürülə bilər; TAXII-dən almaq etibarlılığı təsdiqləmir. Silinmiş və ya geri çağırılmış indikator müdafiə vasitələrində qalmamalıdır. **MISP** açıq mənbəli paylaşma platformasıdır: hadisə (event), atribut, obyekt, taksonomiya, paylaşma qrupu; `to_ids` işarəsi avtomatik bloklama əmri deyil; MISP formatı STIX ilə eyni deyil.

Traffic Light Protocol (TLP 2.0) alıcının məlumatı kimə ötürə biləcəyini göstərir; hüquqi təsnifat və texniki giriş nəzarəti deyil.

| Etiket | Kimlə paylaşmaq olar |
| --- | --- |
| TLP:RED | Yalnız konkret alıcılar (görüşdə və ya yazışmada iştirak edənlər) |
| TLP:AMBER+STRICT | Yalnız öz təşkilatı daxilində, bilməli olanlar |
| TLP:AMBER | Təşkilat və müştərilər, bilməli olduqları qədər |
| TLP:GREEN | Öz icması daxilində (məs. AzScienceCERT icması), açıq yayım yox |
| TLP:CLEAR | Məhdudiyyət yoxdur (köhnə TLP:WHITE) |

TLP:AMBER+STRICT hesabatı mənbə adı silinib açıq kanalda yayıla bilməz; genişləndirmək üçün mənbənin icazəsi lazımdır.

## Universitetdə CTI işi

Böyük platformadan başlamaq lazım deyil: qorunan xidmətlər, sahibləri, prioritet suallar və mənbələr müəyyən edilir, sonra poçt şlüzü, SIEM (təhlükəsizlik məlumatı və hadisələrinin idarə edilməsi) və EDR-ə bağlanır. SOC xəbərdarlığı araşdırır, CSIRT insidenti əlaqələndirir. Qeydlərdə poçt keçidi, DNS sorğusu, uğurlu giriş və profil ixracı ardıcıl görünsə də, bu əlaqədir, səbəb sübutu deyil: məktub açılıb, yoxsa avtomatik yoxlanıb? Saat yaxınlığına görə istifadəçi günahlandırılmır. Təsdiq olunarsa: sessiyalar ləğv, parol və bərpa məlumatı yenilənir, poçt qaydaları və digər alıcılar yoxlanır.

Avtomatlaşdırma aşağı təsirli, geri çevrilə bilən işlərdən (zənginləşdirmə, dublikat, daxili axtarış) başlayır; domen bloklama və hesab bağlama üçün əvvəlcədən səlahiyyət və geri yol yazılır.

| Göstərici | Yanlış şərh riski |
| --- | --- |
| Tələbə uyğunluq | Məhsul sayını keyfiyyət saymaq |
| Tədbirə çevrilmə vaxtı | Yoxlanmamış sürətli bloklamanı uğur saymaq |
| İndikatorun aktuallığı | Çox indikator toplamaq |
| Xəbərdarlıq dəqiqliyi | Görünməyən hücumları saymamaq |
| Aşkarlama örtüyü | Xəritədə rənglənməni real sınaq saymaq |
| Qərara təsir | Hər dəyişiklik üçün CTI uğuru yazmaq |

Dəqiqlik: ayda 40 uyğunluğun 10-u təsdiqlənibsə 10/40 = 25 faiz; bu, hücumların dörddə birinin tapıldığı demək deyil.
