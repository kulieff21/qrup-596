+++
title = "Təhlükəsizlik tədbirləri və şəbəkə təhlükəsizliyi protokolları"
unit = "uzun"
order = 4
summary = "Tam mühazirə: tədbirlərin təsnifatı, fiziki və inzibati tədbirlər, açıq mətn protokollarının əvəzləri, SSH, e-poçt, IPsec və 802.1X, TLS/SSL ilə sertifikatlar, DNS hücumları və DNSSEC."
updated = 2026-11-09

[[source]]
title = "Mühazirə 4: Təhlükəsizlik tədbirləri və şəbəkə təhlükəsizliyi protokolları"
note = "Elmar Cabbarov, 2026–2027"
+++

Bu mövzu iki sualı birləşdirir: riski azaltmaq üçün hansı tədbirlər var və onları necə təsnif etmək lazımdır; şəbəkədə məlumatı qoruyan protokollar (SSH, TLS, IPsec, DNSSEC) nəyi qoruyur və nəyi qorumur. Dörd hissədir: tədbirlər, şəbəkə protokolları, TLS/SSL, DNS təhlükəsizliyi. Universitet topologiyası, adlar və rəqəmlər şərti tədris nümunəsidir.

:::note Bu mövzudan sonra bacarmalısan
- İstənilən tədbiri növünə (fiziki, inzibati, texniki) və funksiyasına (qarşısını alan, aşkarlayan və s.) görə təsnif etməyi.
- Siyasət, standart, prosedur və təlimatı fərqləndirməyi.
- Təhlükəsiz olmayan protokolu əvəzi ilə dəyişməyi; SSH, TLS, DNSSEC-in nəyi qoruduğunu və nəyi qorumadığını deməyi.
- TLS 1.2 ilə 1.3 əl sıxmasını müqayisə etməyi; sertifikat zəncirinin və DNSSEC etibar zəncirinin yoxlanmasını göstərməyi.
:::

## Təhlükəsizlik tədbirləri

### Əsas anlayışlar

Təhlükəsizlik tədbiri (nəzarət, *control*) riski aradan qaldırmaq, azaltmaq, aşkar etmək və ya hadisədən sonra bərpanı təmin etmək üçün görülən təşkilati, texniki və ya fiziki addımdır. Qapı kilidi də, parol siyasəti də, firewall qaydası da tədbirdir: forma fərqlidir, məqsəd eynidir, riski təşkilatın qəbul edə biləcəyi səviyyəyə endirmək.

| Anlayış | İzah | Nümunə |
| --- | --- | --- |
| Aktiv | Təşkilat üçün dəyəri olan informasiya, sistem, xidmət, avadanlıq | Tələbə qiymətləri bazası |
| Təhdid | Aktivə zərər vura biləcək hadisə və ya subyekt | Qiymətləri dəyişmək istəyən tələbə |
| Zəiflik | Təhdidin istifadə edə biləcəyi çatışmazlıq | LMS-də yamaqlanmamış boşluq |
| Risk | Təhdidin baş vermə ehtimalı ilə təsirinin birləşməsi | Qiymətlərin saxtalaşdırılması riski |
| Tədbir | Riski azaldan addım | Yamaq, MFA, dəyişiklik jurnalı |
| Qalıq risk | Tədbirlərdən sonra qalan risk | Rəhbərlik tərəfindən yazılı qəbul edilir |

Risk yalnız "mənfi hadisənin ehtimalı" deyil: ehtimal aşağı, təsir çox böyük ola bilər (yanğın: ehtimal az, server otağı üçün təsir ağır). Ona görə risk həmişə iki ölçü ilə qiymətləndirilir.

:::exam
Bir köhnə slaydda risk yalnız "mənfi təsirlərin yaranma ehtimalı" kimi verilib. Düzgün tərif: ehtimal ilə təsirin birləşməsi.
:::

**Keyfiyyət üsulu:** ehtimal və təsir 1–5 şkalası ilə qiymətləndirilir; ehtimal 3, təsir 5 olarsa risk 15 balla "yüksək" zonaya düşür. **Kəmiyyət üsulu** pulla hesablayır:

- SLE (Single Loss Expectancy): bir hadisənin ziyanı.
- ARO (Annualized Rate of Occurrence): hadisənin ildə gözlənilən sayı.
- ALE (Annualized Loss Expectancy): illik gözlənilən itki, **ALE = SLE × ARO**.

:::example Hesablama nümunəsi (rəqəmlər şərtidir)
Fidyə proqramı hadisəsinin universitetə ziyanı 20 000 manat, ehtimalı iki ildə bir dəfə (ARO = 0,5). ALE = 20 000 × 0,5 = 10 000 manat. EDR həlli ildə 4000 manata başa gəlir və ARO-nu 0,1-ə endirir: yeni ALE = 2000 manat. Tədbirin illik faydası: 10 000 − 2000 − 4000 = **4000 manat**.
:::

Riskə dörd cür cavab verilir: **azaltmaq** (tədbir görmək), **ötürmək** (kiber sığorta, xidmət müqaviləsi), **qaçmaq** (riskli xidməti bağlamaq), **qəbul etmək** (rəhbərlik qərarı ilə). "Riskə göz yummaq" siyahıda yoxdur: qəbul etmək yazılı və məsuliyyətli qərardır.

### Tədbirlərin təsnifatı

Hər tədbirə iki sual verilir: nədir (növü) və nə edir (funksiyası). Bu iki ox bir-birindən asılı deyil. Kamera fiziki tədbirdir, əsasən aşkarlayır, görünən yerdə asılıbsa çəkindirir də. Situasiya suallarında hər iki oxu adlandırmaq cavabı tam edir.

| Növ | Qarşısını alan | Aşkarlayan | Düzəldən | Çəkindirən |
| --- | --- | --- | --- | --- |
| Fiziki | Kilid, turniket, mantrap | CCTV, hərəkət sensoru, su sızma sensoru | Yanğınsöndürmə sistemi | "Kamera ilə izlənir" lövhəsi, mühafizəçi |
| İnzibati | Təhlükəsizlik siyasəti, işə qəbulda yoxlama, təlim | Hüquqların dövri yoxlanması, audit | İnsidentə cavab planı | İntizam tənbehləri qaydası |
| Texniki | Firewall, MFA, şifrələmə | IDS, SIEM, antivirus skanı | Yamaq, faylın karantinə alınması | Giriş ekranında xəbərdarlıq mətni |

Üç əlavə funksiya:

- **Bərpaedici** (recovery): xidməti qaytarır, məs. ehtiyat nüsxədən bərpa, ehtiyat data mərkəzi.
- **Kompensasiyaedici** (compensating): əsas tədbir mümkün olmayanda yerini tutur, məs. yamaq qoyula bilməyən köhnə cihazı ayrıca seqmentə çıxarmaq.
- **Yönləndirici** (directive): nə etməli olduğunu deyir, məs. "USB yaddaş qadağandır" qaydası.

### Çoxsəviyyəli müdafiə və tədbir seçimi

Heç bir tədbir səhvsiz deyil. Çoxsəviyyəli müdafiədə (*defense in depth*) tədbirlər soğan kimi ardıcıl qatlardır; hücumçu bir qatı keçsə, növbəti qat onu dayandırır, ləngidir və ya aşkarlayır. Fişinq məktubu poçt süzgəcindən keçsə, təlim görmüş işçi bildirir; o da olmasa, EDR zərərli prosesi tutur; o da olmasa, seqmentasiya yayılmanı məhdudlaşdırır. Qatlar: məlumat, siyasət və təlim, fiziki mühafizə, şəbəkə (firewall, seqmentlər), host (EDR, yamaq), şifrələmə.

Tədbir riskə görə seçilir: aktivin dəyəri, ehtimal olunan ziyan, qanun və müqavilə tələbləri, tədbirin xərci və istifadəçiyə təsiri. "Ən bahalı məhsulu alaq" məqbul deyil. Xərc ilə qarşısı alınan itki eyni müddət üzrə müqayisə olunur: illik ALE ilə birdəfəlik alış qiymətini yan-yana qoymaq düzgün deyil. Tədbirdən sonra qalan qalıq risk rəhbərlik tərəfindən qəbul edilməlidir.

| Tədbir | Effektivlik göstəricisi |
| --- | --- |
| Yamaq idarəetməsi | Kritik yamaqların neçə gün ərzində quraşdırıldığı |
| Təlim | Fişinq sınağında keçidi açanların və bildirənlərin faizi |
| Giriş baxışı | Vaxtında ləğv olunan hesabların faizi |
| Ehtiyat nüsxə | Uğurlu bərpa sınaqlarının sayı, faktiki bərpa müddəti |
| Temperatur sensoru | Xəbərdarlığın növbətçiyə çatma vaxtı, kalibrləmə tarixi |

### Fiziki tədbirlər

Serverə, kabelə, ehtiyat diskə fiziki çatan adam rəqəmsal müdafiənin böyük hissəsindən yan keçir: diski çıxarıb aparmaq üçün firewall-dan keçmək lazım deyil. Fiziki müdafiə də qat-qat qurulur.

![figure](m04-1.png)

Perimetr, qəbul və qonaq zonası, daxili zonalar, server otağı, rack, aktiv.

### Girişə nəzarət vasitələri

| Vasitə | Üstünlüyü | Məhdudiyyəti |
| --- | --- | --- |
| Mexaniki kilid | Sadə və ucuz | Açarın surəti çıxarıla bilir, jurnal yoxdur |
| Elektron kart | İcazə tez dəyişir, jurnal saxlanılır | Başqasına verilə və klonlana bilər |
| PIN | Rahat | Paylaşıla və müşahidə edilə bilər |
| Biometrika | Şəxslə güclü əlaqəli | Məxfilik, səhv uyğunlaşma, dəyişdirilə bilməməsi |
| Turniket, mantrap | Bir kartla iki nəfərin keçməsini azaldır | Qiymət, yer, təxliyə tələbləri |
| Videomüşahidə | Hadisəni göstərir, sübut yaradır | Monitorinq və saxlanma tələb edir |

Biometrik sistemlərdə iki səhv növü var: **FAR** (False Acceptance Rate), yad şəxsin qəbulu; **FRR** (False Rejection Rate), icazəli şəxsin rədd edilməsi. Həssaslığı artırdıqca FAR azalır, FRR artır. İki əyrinin kəsişdiyi nöqtə **CER** (Crossover Error Rate) sistemləri müqayisə etmək üçündür. Barmaq izi oğurlansa parol kimi dəyişdirilmir, ona görə biometrika adətən ikinci faktordur.

**Mantrap** (şlüz) iki qapı arasında kiçik otaqdır: ikinci qapı yalnız birinci bağlananda açılır. **Tailgating** (icazəli şəxsin ardınca icazəsiz keçmək) qarşısı qapıların qarşılıqlı bloklanması, sensor və ya mühafizəçi ilə bir nəfərlik keçid ilə alınır. Tailgating sosial davranışdan istifadə edir (nəzakətlə qapını açıq saxlamaq), ona görə işçilərin maarifləndirilməsi də lazımdır.

Ziyarətçi əvvəlcədən qeydiyyata alınır, şəxsiyyəti yoxlanır, nişan daşıyır, həssas zonada müşayiət olunur. Kart və açarın həyat dövrü (verilmə, dəyişiklik, dövri baxış, itki, ləğv) sənədləşdirilir; itirilmiş kart dərhal deaktiv edilir, son istifadə cəhdləri jurnaldan yoxlanır.

### Server otağı və avadanlıq

Server otağı pəncərəsiz, su borularından uzaq, ayrıca kilidlənən yerdədir. Minimum imtiyaz burada da işləyir (tələbə işlərini aparan əməkdaş girməməlidir); vəzifələr ayrılığına görə icazəni istəyən, təsdiqləyən və jurnalı yoxlayan fərqli şəxslərdir.

| Sahə | Tələb | Yoxlama sübutu |
| --- | --- | --- |
| Giriş | Rol əsaslı elektron giriş və jurnal | Aktiv kart siyahısı, aylıq jurnal baxışı |
| Rack-lər | Kilid, etiketləmə, kabel idarəetməsi | Fiziki baxış, inventar |
| Daşıyıcılar | Kilidli saxlanc, təhlükəsiz utilizasiya | Təhvil aktı, məhv etmə sertifikatı |
| Konsollar | Avtomatik kilidlənmə | Konfiqurasiya yoxlaması |
| Ehtiyat nüsxələr | Əsas sahədən ayrı, təhlükəsiz məkan | Bərpa testi, yerləşmə jurnalı |

Təmiz masa və təmiz ekran qaydası: məxfi sənəd masada qalmır, çap materialı printerdən vaxtında götürülür, iş yerini tərk edəndə ekran kilidlənir. Köhnə disklər silinmədən atılmır: təhlükəsiz silmə, kriptoqrafik silmə (şifrələmə açarını məhv etmək) və ya fiziki məhv. Kamera və biometrik sistemlər qanuni məqsəd, məhdud saxlanma müddəti və şəffaf məlumatlandırma ilə işlədilir.

### Ətraf mühit və fasiləsizlik

Ətraf mühit təhdidləri bilərəkdən hücum etmir, amma xidməti dayandıra bilir; əsas təsir əlçatanlığadır.

- **Temperatur:** yüksəldikcə avadanlıq söndürülür və ömrü qısalır. ASHRAE data mərkəzləri üçün 18–27 °C tövsiyə edir.
- **Rütubət:** çox aşağıda statik elektrik, çox yüksəkdə kondensasiya və korroziya. Sensorlar monitorinqə bağlanır, hədd aşılanda xəbərdarlıq növbətçiyə çatır.
- **Yanğın:** qarşısının alınması, erkən aşkarlama, xəbərdarlıq, təxliyə, söndürmə. Su elektron avadanlığa ziyan vurur, ona görə server otaqlarında qaz əsaslı sistemlər (FK-5-1-12, inert qaz qarışıqları) və ya boru sistemi işə düşməzdən əvvəl quru qalan pre-action sistemləri seçilir. Qaz boşalmazdan əvvəl insanları xəbərdar edən siqnal olmalıdır.
- **Su:** server otağı boru xətlərinin altına qoyulmur, kritik nöqtələrdə su sızma sensorları, avadanlıq birbaşa döşəməyə qoyulmur.

:::tip Yadda saxla: fail-safe və fail-secure
Fiziki təhlükəsizlikdə birinci prioritet insan həyatıdır. Yanğın zamanı elektron qapı insanları içəridə kilidləməməlidir (**fail-safe**). Server otağının qapısı isə adi elektrik kəsintisində açıq qalmamalıdır (**fail-secure**). Balans layihə mərhələsində qurulur, çıxış tərəfi həmişə əl ilə açılır.
:::

| Komponent | Funksiya | İdarəetmə tələbi |
| --- | --- | --- |
| UPS | Qısa kəsintidə enerji verir, gərginliyi sabitləşdirir, düzgün söndürməyə vaxt yaradır | Batareya testi, yük hesabı |
| Generator | Uzun kəsintidə enerji | Yanacaq, avtomatik keçid, dövri sınaq |
| Soyutma | Temperaturu iş diapazonunda saxlayır | N+1 ehtiyat, sensor nəzarəti |
| Torpaqlama | Elektrik təhlükəsini azaldır (gərginlik sıçrayışından qoruma) | Peşəkar yoxlama |

Artıqlıq (*redundancy*) N+1 modeli ilə qurulur: lazım olandan bir əlavə komponent. İki eyni kondisioner eyni elektrik xəttinə qoşulubsa real artıqlıq yoxdur, tək nasazlıq nöqtəsi qalıb.

Fasiləsizlik iki göstəricilə planlaşdırılır: **RTO** (Recovery Time Objective), xidmətin nə müddətə bərpa olunmalı olduğu; **RPO** (Recovery Point Objective), nə qədər məlumat itkisinin qəbul edildiyi. LMS üçün RTO 4 saat, RPO 1 saatdırsa, ehtiyat nüsxə ən azı saatda bir alınmalı, sistem 4 saata qalxmalıdır. **3-2-1 qaydası:** üç nüsxə, iki fərqli daşıyıcı, biri başqa yerdə. Fidyə proqramlarına qarşı nüsxələrdən biri dəyişdirilə bilməyən (immutable) və ya şəbəkədən ayrı olmalıdır. Sınaqdan keçməyən nüsxə plan sayılmır, ümid sayılır.

### İnzibati tədbirlər

İnzibati tədbirlər kimin nəyə cavabdeh olduğunu, nəyin qadağan olduğunu, hadisədə kimin nə edəcəyini müəyyən edir; texniki tədbir bu qərarları sistemdə icra edir.

### Sənədlər iyerarxiyası

![figure](m04-2.png)

| Sənəd | Nəyə cavab verir | Nümunə |
| --- | --- | --- |
| Siyasət | Nə və niyə? Rəhbərlik təsdiqləyir, məcburidir | "Bütün uzaqdan girişlər MFA ilə qorunmalıdır." |
| Standart | Hansı minimum tələblərlə? Məcburidir | "MFA üçün yalnız FIDO2 və ya autentifikator tətbiqi." |
| Prosedur | Addım-addım necə və kim edir? | "Yeni işçiyə MFA qoşmaq üçün 7 addım." |
| Təlimat (guideline) | Tövsiyə, məcburi deyil | "Parol menecerindən istifadə tövsiyə olunur." |

Siyasətə məhsul adı və tez dəyişən texniki parametr yazılmır, əks halda sənəd köhnəlir; belə detallar standart və prosedurlarda saxlanır.

### Siyasətin hazırlanması

1. Məqsəd, qanuni və müqavilə tələbləri müəyyən edilir.
2. Əhatə dairəsi, aktivlər, istifadəçilər, istisnalar yazılır.
3. Terminlər və məsul rollar göstərilir.
4. Tələblər konkret, ölçülə bilən, icra oluna bilən yazılır.
5. Pozuntu, istisna və eskalasiya prosesi müəyyən edilir.
6. Hüquq, insan resursları, İT və biznes sahibləri ilə razılaşdırılır.
7. Səlahiyyətli rəhbər təsdiqləyir, əməkdaşlara çatdırılır.
8. Tətbiq üçün standart, prosedur, təlim və texniki tədbirlər hazırlanır.
9. Effektivlik ölçülür, sənəd dövri yenilənir.

Yaxşı siyasətin sahibi, versiyası, qüvvəyə minmə və növbəti baxış tarixi olur. İstisna yalnız risk qiymətləndirməsi ilə və müddətli verilir.

Əsas siyasətlər: məqbul istifadə (AUP), girişə nəzarət, məlumatın təsnifatı, uzaqdan iş, insidentlərin idarəsi, ehtiyat nüsxə, tədarükçü təhlükəsizliyi, dəyişikliklərin idarəsi. Personal tədbirləri: işə qəbulda yoxlama, məxfilik müqaviləsi (NDA), təlim, vəzifə dəyişəndə və işdən çıxanda hüquqların götürülməsi (joiner, mover, leaver prosesi). Vəzifələr ayrılığı və məcburi məzuniyyət fırıldaqçılığı çətinləşdirir.

### Standartların aktual versiyaları

Ədəbiyyatda ISO/IEC 17799 və ya 27002-nin köhnə 11 bölməli strukturuna hələ rast gəlinir. Aktual olanlar:

| Sənəd | Məzmun |
| --- | --- |
| ISO/IEC 27001:2022 | İnformasiya təhlükəsizliyi idarəetmə sisteminin (İTİS) tələbləri, sertifikatlaşma buna görə |
| ISO/IEC 27002:2022 | 93 nəzarət, 4 mövzuda: təşkilati (37), insan (8), fiziki (14), texnoloji (34) |
| ISO/IEC 27005:2022 | Risklərin idarəsi üzrə rəhbərlik (proqram aləti deyil) |
| NIST CSF 2.0 (2024) | Altı funksiya: Govern, Identify, Protect, Detect, Respond, Recover |
| NIST SP 800-53 Rev. 5 | Geniş nəzarətlər kataloqu |
| CIS Controls v8.1 | Prioritetləşdirilmiş praktiki tədbirlər |
| NIST SP 800-61 Rev. 3 (2025) | İnsidentlərə cavab tövsiyələri |

### Texniki tədbirlər

| İstiqamət | Tədbirlər | Məqsəd |
| --- | --- | --- |
| Kimlik və giriş | IAM, MFA, RBAC, PAM | Girişi kimliyə və rola bağlamaq |
| Məlumatın qorunması | Şifrələmə, DLP, açar idarəetməsi | Məxfilik və bütövlük |
| Şəbəkə | Firewall, seqmentləşdirmə, IDS/IPS, NAC | Trafikin məhdudlaşdırılması və izlənməsi |
| Son nöqtə | EDR, antivirus, tətbiq nəzarəti, sərtləşdirmə | Cihaz riskinin azaldılması |
| Zəiflik idarəetməsi | Skan, yamaq, konfiqurasiya yoxlaması | Məlum boşluqların azaldılması |
| Monitorinq | Jurnallar, SIEM, zaman sinxronizasiyası | Aşkarlama və araşdırma |
| Fasiləsizlik | Ehtiyat nüsxə, replikasiya, bərpa testi | Xidmətin bərpası |

Təhlükəsiz başlanğıc mövqeyi **default deny**: icazə verilməyən hər şey bağlıdır. İcazələr rol və konkret iş ehtiyacına görə verilir, yüksək səlahiyyətlər müddətli olur.

Autentifikasiya kimliyi təsdiqləyir, avtorizasiya həmin şəxsin nə edə biləcəyini müəyyən edir. Çoxfaktorlu autentifikasiya fərqli kateqoriyaları birləşdirir: bilik (parol), sahiblik (telefon, açar), biometrik xüsusiyyət. **İki parol MFA deyil**, çünki ikisi də eyni kateqoriyadandır. MFA parol oğurluğunu ciddi azaldır, amma fişinq proksiləri sessiya tokenini oğurlaya bilir, bildiriş bombardmanı istifadəçini təsdiqləməyə məcbur edə bilir. FIDO2 açarları domenə bağlı olduğu üçün fişinqə davamlıdır.

Şifrələmə məxfiliyi qoruyur, amma açar zəif saxlanırsa dəyəri itir: açarın yaradılması, saxlanması, rotasiyası, ehtiyatı, ləğvi və məhvi müəyyən edilməlidir. Zəifliklərin prioritetini sayı deyil, aktivin kritikliyi və istismar ehtimalı müəyyən edir. Jurnal və SIEM mövzusu 12-ci, seqmentasiya və IDS/IPS 6-cı mühazirədə ətraflı izah olunur.

### Birləşdirilmiş nümunə: tələbə informasiya sistemi

Sistem şəxsi məlumat, qiymət və ödəniş məlumatını emal edir, İnternetdən əlçatandır, baza ayrıca server zonasındadır.

| Risk sahəsi | Fiziki | İnzibati | Texniki |
| --- | --- | --- | --- |
| Server otağı | Kart, kamera, rack kilidi | Giriş siyahısının aylıq baxışı | Giriş hadisələrinin SIEM-ə ötürülməsi |
| İstifadəçi hesabı | İş yerində ekran məxfiliyi | Hesab həyat dövrü və təlim | MFA, RBAC, risk əsaslı giriş |
| Məlumat bazası | Ehtiyat daşıyıcının kilidli saxlanması | Təsnifat və saxlanma siyasəti | Şifrələmə, DLP, audit jurnalı |
| Şəbəkə | Kabel və cihaz otağının qorunması | Dəyişiklik proseduru | WAF, firewall, seqmentləşdirmə, TLS |
| Fasiləsizlik | UPS, generator, yanğın və su sensoru | BCP/DR planı və məşq | Ehtiyat nüsxə və bərpa testi |

Gecə server otağına uğursuz kart cəhdi, ardınca inzibati hesaba çoxsaylı uğursuz giriş qeydə alınır. Kamera, kart sistemi və SIEM vaxt baxımından əlaqələndirilir, növbətçi prosedura uyğun hərəkət edir. Fiziki siqnal texniki siqnalı gücləndirir; üç qat olmasaydı iki hadisə arasında əlaqə görünməzdi.

## Şəbəkə təhlükəsizliyi protokolları

### Protokollar və təhdidlər

İlk protokollar bir-birini tanıyan təşkilatlar üçün yaradılıb. Telnet, FTP, HTTP hər şeyi, parollar daxil, açıq mətnlə ötürür; trafiki dinləyən oxuya bilir. İki yol var: köhnə protokolu şifrəli əvəzi ilə dəyişmək və ya onu qorunan kanalın içinə salmaq.

| OSI səviyyəsi | Protokollar | Tipik hücum | Qorunma |
| --- | --- | --- | --- |
| 2, kanal | Ethernet, ARP, VLAN | MAC seli, ARP saxtalaşdırması, VLAN hopping | Port security, DAI, 802.1X, MACsec |
| 3, şəbəkə | IP, ICMP, BGP | IP saxtalaşdırması, marşrut oğurluğu | Ingress filtering (BCP 38), IPsec, RPKI |
| 4, nəqliyyat | TCP, UDP | SYN seli, port skanı | SYN cookies, firewall, sürət məhdudiyyəti |
| 5–6, sessiya və təqdimat | TLS | Versiya endirmə, MITM | TLS 1.2/1.3, sertifikat yoxlaması |
| 7, tətbiq | HTTP, DNS, SMTP, SSH | Saxtalaşdırma, inyeksiya, parol oğurluğu | HTTPS, DNSSEC, SPF/DKIM/DMARC, SSH |

Ethernet MAC ünvanı 48 bitdir (64 yox). ARP IPv4 ünvanını MAC ünvanına çevirir (əksinə yox) və autentifikasiyası yoxdur, ARP saxtalaşdırması buna görə mümkündür. TCP-nin üç addımlı əl sıxması (SYN, SYN-ACK, ACK) **etibarlı** bağlantı qurur, təhlükəsiz yox: nə şifrələmə, nə autentifikasiya. Port nömrəsi də təhlükəsizlik sərhədi deyil, TCP 443-dən zərərli trafik də keçir.

:::exam
Tələ: 7-ci səviyyə tətbiq (Application), 6-cı təqdimat (Presentation). "İnvaziv qoruma" termini yoxdur, söhbət intrusion prevention (IPS) haqqındadır. IPv6 IPsec-i dəstəkləyir, amma trafik avtomatik şifrələnmir.
:::

### Açıq mətn protokolları və əvəzləri

| Köhnə protokol | Təhlükəsiz əvəzi | Qeyd |
| --- | --- | --- |
| Telnet (TCP 23) | SSH (TCP 22) | Şifrəli idarəetmə, açarla autentifikasiya; ilk qoşulmada host açarı yoxlanır |
| HTTP (TCP 80) | HTTPS (TCP 443) | HTTP + TLS; məxfilik, tamlıq, sertifikatla server autentifikasiyası; HSTS |
| FTP (TCP 20/21) | SFTP (TCP 22), FTPS (explicit 21, implicit 990) | SFTP SSH üzərində, FTPS TLS üzərində; fərqli protokollardır. Explicit: 21-də AUTH TLS |
| SNMP v1/v2c (UDP 161) | SNMPv3 | v1/v2c-də community string açıq gedir |
| DNS (53) | DNSSEC; DoT (853), DoH (443) | DNSSEC şifrələmir, DoT və DoH şifrələyir |
| LDAP (TCP 389) | LDAPS (TCP 636), StartTLS | Kataloq sorğuları və parollar şifrələnir |
| POP3 (110), IMAP (143) | POP3S (995), IMAPS (993) | Poçt qəbulu |
| SMTP (25) | Serverlərarası: TCP 25 + STARTTLS; müştəridən göndərmə: TCP 587 + məcburi STARTTLS və ya TCP 465 + Implicit TLS | Bağlantı qorunur, məktub ucdan uca şifrələnmir |
| NTP (UDP 123) | NTS (RFC 8915) | Vaxtın saxtalaşdırılmasının qarşısı |

:::example Yataqxana kommutatoru
Administrator kommutatoru Telnet ilə idarə edir. Eyni seqmentdəki tələbə ARP saxtalaşdırması ilə trafiki öz üzərindən keçirir, Wireshark-da telnet süzgəci ilə "Follow TCP Stream" seçib administrator parolunu oxuyur. SSH-a keçidlə həmin ekranda yalnız şifrəli baytlar görünür.
:::

### SSH

SSH (Secure Shell, RFC 4251–4254) uzaqdan idarəetmə, fayl ötürülməsi və tunelləmə üçün şifrəli kanaldır, TCP 22 üzərində, üç qatdan ibarətdir:

- **Nəqliyyat qatı:** serveri autentifikasiya edir, açar razılaşdırır, şifrələyir.
- **Autentifikasiya qatı:** istifadəçini yoxlayır.
- **Bağlantı qatı:** bir bağlantıda bir neçə müstəqil kanal; sessiyalar ayrıca kanallarda.

SSH CA tələb etmir, server öz host açarını təqdim edir. İlk qoşulmada istifadəçi açarın barmaq izini təsdiqləyir, o known_hosts faylına yazılır. Bu model **TOFU** (Trust On First Use): ilk qoşulmada ortada hücumçu varsa onun açarı qəbul edilə bilər, ona görə barmaq izi başqa kanalla yoxlanır. Sonrakı qoşulmada açar dəyişibsə SSH xəbərdarlıq verir və ona ciddi yanaşmaq lazımdır. Böyük şəbəkələrdə öz CA ilə SSH sertifikatları problemi aradan qaldırır.

İstifadəçi autentifikasiyasında parol əvəzinə açar cütü: gizli açar istifadəçidə, açıq açar serverdə authorized_keys faylında. Müştəri sessiya identifikatorunu və sorğu sahələrini gizli açarla imzalayır, server icazəni və imzanı yoxlayır. Parol şəbəkəyə çıxmır, kobud güc mənasını itirir.

```bash
# Açar yaratmaq və serverə yükləmək
ssh-keygen -t ed25519 -C "admin@universitet.example"
ssh-copy-id admin@10.10.80.20

# /etc/ssh/sshd_config
PermitRootLogin no
PasswordAuthentication no
KbdInteractiveAuthentication no
AuthenticationMethods publickey
PubkeyAuthentication yes
AllowGroups it-admin
MaxAuthTries 3
AllowTcpForwarding no
```

Tunelləmə həm faydalı, həm risklidir: `ssh -L` yerli portu uzaq xidmətə yönəldir, `ssh -D` SOCKS proksi yaradır. İşçi bu yolla firewall qaydalarından yan keçə bilir, ona görə lazım olmayan serverlərdə `AllowTcpForwarding no` (SSH-ın daxili yönləndirməsini söndürür). Shell girişi olan istifadəçinin ayrıca proksi qaldırması üçün shell imkanları və şəbəkə çıxışı da nəzarətdə saxlanmalıdır. Agent yönləndirməsi (`ssh -A`) ehtiyatla işlədilir: ələ keçirilmiş aralıq server agentdən istifadə edə bilər.

SSH proqramı da yenilənməlidir. 2024-də aşkarlanan **regreSSHion** (CVE-2024-6387) glibc əsaslı Linux-da OpenSSH serverində autentifikasiyasız kod icrası verirdi. Həmin il **XZ Utils** kitabxanasına yerləşdirilmiş arxa qapı (CVE-2024-3094) SSH serverini hədəfləyirdi və təsadüfən aşkar edildi.

### E-poçtun qorunması

SMTP 1980-ci illərdə yaradılıb, göndərənin kimliyini yoxlamır: hər kəs "From" sahəsinə rektor@universitet.example yaza bilər. STARTTLS bunu həll etmir. Saxta göndəriciyə qarşı üç mexanizm:

![figure](m04-3.png)

| Mexanizm | Nə yoxlayır | DNS qeydi |
| --- | --- | --- |
| SPF (RFC 7208) | Göndərən IP domenin icazə verdiyi serverlərdəndirmi | TXT, domen üzərində |
| DKIM (RFC 6376) | Rəqəmsal imza doğrudurmu, yolda dəyişdirilibmi | TXT, selector._domainkey |
| DMARC (RFC 9989, əvvəl RFC 7489) | SPF və ya DKIM nəticəsi "From" domeni ilə uyğun gəlirmi, uğursuzluqda nə edilsin | TXT, _dmarc |

```text
universitet.example.                  TXT "v=spf1 ip4:203.0.113.25 -all"
s1._domainkey.universitet.example.    TXT "v=DKIM1; k=rsa; p=MIIBIjAN..."
_dmarc.universitet.example.           TXT "v=DMARC1; p=reject; rua=mailto:dmarc@universitet.example"
```

SPF zərfdəki domeni yoxlayır, istifadəçinin gördüyü "From" sahəsini yox. DMARC bu boşluğu uyğunluq (alignment) tələbi ilə bağlayır və siyasət seçimi verir: **none** (yalnız hesabat), **quarantine** (spam qovluğu), **reject** (rədd). Yeni domenlərdə none ilə başlanır, hesabatlar öyrənilir, sonra sərtləşdirilir. Serverlər arasında STARTTLS-in endirilməsinin qarşısını MTA-STS (RFC 8461) alır. Ucdan uca məxfilik üçün S/MIME və ya PGP lazımdır.

### SNMP və NTP

SNMP şəbəkə cihazlarının monitorinqi üçündür: sorğular UDP 161, trap mesajları UDP 162. v1/v2c-də kimlik açıq mətn "community string"dir, standart public/private dəyərlər tez-tez dəyişdirilmir. SNMPv3 (RFC 3414) üç səviyyə verir: **noAuthNoPriv, authNoPriv, authPriv**; sonuncu həm autentifikasiya, həm şifrələmə verir və seçilməlidir. SNMP yalnız idarəetmə şəbəkəsindən əlçatan olmalıdır.

NTP UDP 123-də vaxtı sinxronlaşdırır. Vaxtın saxtalaşdırılması Kerberos biletlərinə, sertifikat yoxlamasına, SIEM korrelyasiyasına təsir edir. NTS (Network Time Security, RFC 8915) NTP-yə kriptoqrafik autentifikasiya əlavə edir. Köhnə NTP serverlərinin monlist əmri (CVE-2013-5211) gücləndirmə hücumları üçün geniş istifadə olunub.

### IPsec, 802.1X və RADIUS

| Meyar | IPsec | TLS | SSH |
| --- | --- | --- | --- |
| Səviyyə | Şəbəkə (3) | Nəqliyyatla tətbiq arası | Tətbiq |
| Nəyi qoruyur | Bütün IP trafikini | Tətbiq bağlantısını | Uzaqdan sessiya və fayl ötürməsini |
| Kimlik | Sertifikat, PSK, EAP | X.509 sertifikat | Host açarı, istifadəçi açarı |
| Tipik istifadə | Saytdan sayta VPN | Veb, API, poçt | Server və cihaz idarəetməsi |

**IPsec** komponentləri (AH, ESP, IKE/IKEv2, SA, nəqliyyat və tunel rejimləri) 7-ci mövzunun VPN hissəsində ətraflı izah olunur. Qısaca: IKE tərəfləri yoxlayır və açarları razılaşdırır (SA); AH yalnız tamlıq və mənbə autentifikasiyası verir, şifrələmir, NAT ilə uyuşmur; ESP şifrələmə və tamlıq verir, praktikada demək olar həmişə ESP işlədilir; nəqliyyat rejimi yalnız faydalı yükü (host–host), tunel rejimi bütün paketi yeni paketə qoyur (şlüz–şlüz VPN).

**IEEE 802.1X** port əsaslı girişə nəzarətdir: kompüter kabelə və ya Wi-Fi-a qoşulanda autentifikasiyadan keçənə qədər buraxılmır. Üç rol: istifadəçi cihazı (supplicant), kommutator və ya giriş nöqtəsi (authenticator), RADIUS serveri (authentication server). 802.1X **trafiki şifrələmir**, girişi idarə edir. **NAC** (Network Access Control) cihazın vəziyyətini də yoxlayır (antivirus aktivdirmi, yamaqlar varmı) və uyğun gəlməyəni karantin VLAN-ına göndərir.

RADIUS UDP 1812 (autentifikasiya) və 1813 (uçot) işlədir. Şəbəkə cihazlarına inzibati giriş üçün **TACACS+** (TCP 49) istifadə olunur, çünki hər əmri ayrıca avtorizasiya edə bilir. 2024-də aşkarlanan **Blast-RADIUS** (CVE-2024-3596) UDP üzərindəki RADIUS-un MD5 əsaslı cavab yoxlamasındakı zəiflikdən istifadə edir; qorunma: Message-Authenticator atributunu məcburi etmək və RADIUS-u TLS üzərinə keçirmək.

### Təhlükəsiz uzaqdan idarəetmə

- İdarəetmə portları (SSH, RDP, veb panellər) İnternetə birbaşa açılmır.
- Administrator əvvəl VPN ilə idarəetmə zonasına girir, sonra nəzarətli jump host vasitəsilə serverə keçir.
- İnzibati hesablar fərdidir, MFA məcburidir, ortaq "admin" hesabı yoxdur.
- İcazə mənbə şəbəkəsi və vaxtla məhdudlaşdırılır, müvəqqəti hüquqlar iş bitəndə ləğv olunur.
- Sessiyalar jurnala yazılır, yüksək riskli əmrlər izlənir; PAM parolları anbarda saxlayıb sessiyanı qeydə ala bilir.
- İdarəetmə kompüterləri gündəlik poçt və veb üçün işlədilmir.

Cihazlar üçün ayrıca idarəetmə VLAN-ı, kritik yerlərdə əsas şəbəkədən ayrı kanal (out-of-band): əsas şəbəkə hücum altındakı administrator yenə də çata bilir.

## TLS/SSL protokolları və rəqəmsal sertifikatlar

### TLS nədir

TLS (Transport Layer Security) iki tətbiq arasında etibarsız şəbəkə üzərindən qorunan kanal qurur; HTTPS, qorunan poçt protokolları, bir çox VPN və API-lər onun üzərindədir. Üç xidmət:

- **Məxfilik:** məlumat yolda oxunmur.
- **Tamlıq:** dəyişdirilmə aşkar edilir.
- **Autentifikasiya:** adətən server sertifikatla kimliyini sübut edir. **mTLS**-də müştəri də sertifikat təqdim edir.

![figure](m04-4.png)

TLS tətbiq protokolu ilə TCP arasında yerləşir, OSI-yə dəqiq sığmır, adətən 5–6-cı səviyyələrə aid edilir. İki qat: **əl sıxma protokolu** tərəfləri tanıdır və açarları razılaşdırır; **record protokolu** məlumatı bölüb şifrələyir və tamlığını qoruyur.

| Xidmət | Port | Qeyd |
| --- | --- | --- |
| HTTPS | TCP 443 | HTTP/3 UDP 443-də QUIC işlədir, içində TLS 1.3 var |
| SMTPS (Implicit TLS) | TCP 465 | Poçt göndərilməsi |
| SMTP Submission + STARTTLS | TCP 587 | Açıq başlayır, sonra TLS-ə keçir |
| IMAPS | TCP 993 | Poçt qəbulu |
| POP3S | TCP 995 | Poçt qəbulu |
| LDAPS | TCP 636 | Kataloq xidməti |
| FTPS | TCP 990 (implicit), TCP 21 (explicit) | SFTP isə SSH üzərində başqa protokoldur |
| DoT (DNS over TLS) | TCP 853 | DNS sorğularının məxfiliyi |
| Syslog over TLS | TCP 6514 | Logların SIEM-ə qorunan ötürülməsi |

UDP tətbiqləri üçün DTLS (Datagram TLS) var; son versiyası DTLS 1.3 (RFC 9147) TLS 1.3-ün UDP variantıdır, VoIP, WebRTC və bəzi VPN-lər işlədir.

### SSL-dən TLS 1.3-ə

SSL Netscape-in 1990-cı illərdə hazırladığı protokoldur; standartlaşdırma IETF-ə keçdi və ad TLS oldu. "SSL sertifikatı" ifadəsi hələ işlədilir, amma sertifikatlar TLS ilə işləyir. SSL-in heç bir versiyası təhlükəsiz deyil.

| Versiya | İl | Status | Əsas qeyd |
| --- | --- | --- | --- |
| SSL 2.0 | 1995 | Qadağandır (RFC 6176) | Əl sıxması qorunmur, zəif şifrlər |
| SSL 3.0 | 1996 | Qadağandır (RFC 7568) | POODLE hücumu |
| TLS 1.0 | 1999 | Köhnəlib (RFC 8996) | BEAST, MD5 və SHA-1 asılılığı |
| TLS 1.1 | 2006 | Köhnəlib (RFC 8996) | BEAST-ə düzəliş, müasir AEAD şifrləri yoxdur |
| TLS 1.2 | 2008 | Qəbul edilir | Düzgün sazlananda təhlükəsiz; köhnə seçimləri də dəstəklədiyi üçün sazlama vacibdir |
| TLS 1.3 | 2018 | Tövsiyə olunur | RFC 8446, 2026-cı ilin iyulunda RFC 9846 ilə yeniləndi; köhnə alqoritmlər çıxarılıb |

### Kriptoqrafik tikinti blokları

Asimmetrik kriptoqrafiya sürətli deyil, ona görə yalnız tərəflərin tanınması və açarın razılaşdırılması üçündür; məlumat sürətli simmetrik alqoritmlə şifrələnir.

| Vəzifə | Müasir seçim | Köhnə və zəif |
| --- | --- | --- |
| Açar mübadiləsi | ECDHE (X25519, P-256), X25519MLKEM768 | Statik RSA, statik DH, DH 1024 bit |
| Autentifikasiya (imza) | ECDSA, RSA-PSS, Ed25519 | RSA-PKCS#1 v1.5 (MD5 və SHA-1 ilə) |
| Simmetrik şifrələmə | AES-GCM, ChaCha20-Poly1305 | RC4, 3DES, AES-CBC |
| Heş və açar törətmə | SHA-256, SHA-384, HKDF | MD5, SHA-1 |

### Şifr dəstinin oxunması

TLS 1.2-də ad bütün alqoritmləri göstərir:

```text
TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256
    |     |         |           |
    |     |         |           +-- PRF üçün heş (SHA-256)
    |     |         +-------------- simmetrik şifr və rejim (AES-128 GCM)
    |     +------------------------ server imzası (RSA sertifikat)
    +------------------------------ açar mübadiləsi (ECDHE)
```

TLS 1.3-də ad qısalıb, çünki açar mübadiləsi və imza ayrıca razılaşdırılır. İlkin spesifikasiya beş dəst müəyyən edib, sonra əlavələr yaranıb. Geniş işlənən üçü: TLS_AES_128_GCM_SHA256, TLS_AES_256_GCM_SHA384, TLS_CHACHA20_POLY1305_SHA256.

### Ortaq sirr açıq kanalda necə yaranır

Tərəflər görüşməyib, kanalı hamı dinləyir, amma sonda ortaq sirr var: bunu **Diffie-Hellman** mümkün edir. İdeya kiçik ədədlərlə (real sistemdə yüzlərlə bit, TLS-də elliptik əyri variantı):

```text
Açıq parametrlər:   p = 23,  g = 5
Müştəri gizli a = 6:  A = 5^6  mod 23 = 8    (A göndərilir)
Server  gizli b = 15: B = 5^15 mod 23 = 19   (B göndərilir)
Müştəri: 19^6 mod 23 = 2
Server:   8^15 mod 23 = 2
```

Dinləyən 23, 5, 8 və 19-u görür; 2-ni tapmaq diskret loqarifm məsələsidir, böyük ədədlərdə praktiki mümkün deyil. Amma Diffie-Hellman "mən kiminlə danışıram?" sualına cavab vermir: ortadakı hücumçu hər iki tərəflə ayrıca sirr qura bilər. Bunu serverin sertifikatla imzası həll edir: server açıq dəyərini gizli açarı ilə imzalayır, müştəri sertifikatdakı açıq açarla yoxlayır.

### İrəli məxfilik (forward secrecy)

Statik RSA-da müştəri 48 baytlıq premaster_secret yaradıb serverin açıq RSA açarı ilə şifrələyirdi; trafik açarları ondan və Hello təsadüfi dəyərlərindən törədilirdi. Hücumçu trafiki illərlə yazıb sonra serverin gizli açarını oğurlayanda köhnə bütün sessiyaları açırdı.

ECDHE-də hər sessiyaya müvəqqəti açar yaradılır və sonra silinir: 2024-də yazılmış trafik 2026-da serverin gizli açarı oğurlansa belə açılmır. Bu xassə **irəli məxfilik**dir. TLS 1.3-də statik RSA çıxarılıb. (EC)DHE ilə qurulan 1-RTT trafik açarları irəli məxfilik verir; yalnız PSK işlədən psk_ke rejimi və 0-RTT məlumatı vermir.

### Əl sıxması

![figure](m04-5.png)

### TLS 1.2

ClientHello: müştəri versiyanı, şifr dəstlərini, təsadüfi ədədi və SNI ilə hədəf domeni göndərir. Server ServerHello ilə seçimini bildirir, sertifikatını və ECDHE açıq dəyərini imzalanmış şəkildə (ServerKeyExchange) göndərir. Müştəri sertifikatı yoxlayır, öz açıq dəyərini göndərir. Hər iki tərəf ortaq sirri hesablayır, ChangeCipherSpec ilə şifrəli rejimə keçir, Finished ilə əl sıxmasının dəyişdirilmədiyini təsdiqləyir. **İki dövr (2-RTT)**, sertifikat açıq ötürülür.

### TLS 1.3

Bir dövr (**1-RTT**). Müştəri əvvəlcədən ən çox işlənən qrup üçün key_share göndərir, server ilk cavabla ortaq sirri hesablayır. ServerHello-dan sonrakı hər şey, sertifikat daxil, şifrələnir.

İki mesajı qarışdırmaq olmaz: **CertificateVerify** serverin sertifikatdakı açarın gizli hissəsinə sahib olduğunu sübut edir (əl sıxması tarixçəsinin heşini imzalayır); **Finished** HMAC kodudur, iki tərəfin eyni açarları və eyni tarixçəni gördüyünü təsdiqləyir. key_share qrupu uyğun deyilsə server HelloRetryRequest göndərir və bir dövr əlavə olunur.

| Meyar | TLS 1.2 | TLS 1.3 |
| --- | --- | --- |
| Əl sıxması | 2-RTT | 1-RTT (0-RTT seçimi ilə) |
| Sertifikat | Açıq | Şifrəli |
| İrəli məxfilik | Yalnız ECDHE/DHE seçiləndə | (EC)DHE ilə 1-RTT-də var; PSK-only və 0-RTT məlumatında yoxdur |
| Statik RSA, RC4, 3DES, CBC | Mümkündür | Çıxarılıb |
| Sıxılma, yenidən danışıq | Var | Çıxarılıb |
| Şifr dəsti | Onlarla variant | İlkin spesifikasiyada beş |
| Açar törətmə | PRF | HKDF |

:::steps TLS 1.3 əl sıxmasının addımları
[[step]]
title = "ClientHello + key_share"
body = "Müştəri versiya, şifr dəstləri, SNI və ən çox işlənən qrup üçün açıq dəyər göndərir."

[[step]]
title = "ServerHello + key_share"
body = "Server seçimini və öz açıq dəyərini göndərir; hər iki tərəf ortaq sirri hesablayır. Bundan sonrası şifrəlidir."

[[step]]
title = "Certificate, CertificateVerify, Finished"
body = "Server sertifikatı, əl sıxması heşinin imzasını və HMAC Finished mesajını göndərir."

[[step]]
title = "Müştəri Finished"
body = "Müştəri öz Finished mesajını göndərir, şifrəli tətbiq məlumatı başlayır."
:::

**0-RTT** təkrar qoşulan müştəriyə ilk mesajla məlumat göndərməyə imkan verir, lakin təkrar göndərmə (replay) hücumuna açıqdır: hücumçu paketi yenidən göndərib əməliyyatı ikinci dəfə icra etdirə bilər. Ona görə yalnız vəziyyəti dəyişməyən sorğular (adi GET) üçündür; ödəniş və ya qiymət dəyişdirmə üçün söndürülür.

### X.509 sertifikatının sahələri

Sertifikat domen adını açıq açarla bağlayan, Sertifikat Mərkəzinin (CA) imzaladığı sənəddir. Sahələr: subyekt, buraxan CA, etibarlılıq tarixləri, açıq açar, Subject Alternative Name (SAN), açarın məqsədi, CA imzası. Brauzerlər domeni Common Name-dən yox, SAN-dan yoxlayır. CA sertifikatında basicConstraints CA:TRUE, adi server sertifikatında CA:FALSE olur; yoxlanmasa istənilən server sertifikatı başqalarını imzalaya bilərdi. keyUsage və EKU (serverAuth) açarın hansı iş üçün olduğunu məhdudlaşdırır.

| Növ | CA nəyi yoxlayır | Harada işlənir |
| --- | --- | --- |
| DV | Yalnız domen üzərində nəzarəti | Əksər saytlar, Let's Encrypt |
| OV | Domen və təşkilatın mövcudluğu | Korporativ saytlar |
| EV | Təşkilatın ətraflı hüquqi yoxlanışı | Bəzi maliyyə qurumları |

Kilid saytın dürüst olduğunu bildirmir: fişinq saytı da pulsuz DV ala bilir. Kilid yalnız kanalın qorunduğunu göstərir. Chrome 77-də (2019) EV göstəricisi ünvan sətrindən səhifə məlumatları bölməsinə keçirildi.

### Zəncirin yoxlanması

![figure](m04-6.png)

Brauzer serverdən sertifikatı və aralıq sertifikatları alır, yoxlayır: zəncir etibar anbarındakı kökdə bitirmi, imzalar düzgündürmü, tarix keçibmi, domen SAN-da varmı, ləğv olunubmu. Kök CA-nın gizli açarı oflayn saxlanır, gündəlik sertifikatları aralıq CA imzalayır; aralıq CA sındırılsa kök onu ləğv edə bilir.

### Ləğv

- **CRL** (Certificate Revocation List): CA-nın dövri yayımladığı ləğv siyahısı.
- **OCSP:** real vaxt sorğusu, amma istifadəçinin hansı sayta girdiyini CA-ya açır.
- **OCSP stapling:** server CA-dan aldığı təsdiqi öz cavabına əlavə edir.

Let's Encrypt 2025-də OCSP xidmətini dayandırıb CRL-ə keçib; sənayedə qısa ömürlü sertifikatlara üstünlük verilir.

### Qısa müddətli sertifikatlar

CA/Browser Forum SC-081v3 qərarı (aprel 2025) ictimai TLS sertifikatlarının maksimum müddətini azaldır: 15 mart 2026-dan 200 gün, 15 mart 2027-dən 100 gün, 15 mart 2029-dan 47 gün. Əllə yeniləmə real deyil; yeniləmə ACME (RFC 8555) ilə avtomatlaşdırılır.

:::example Portal sertifikatı bitdi
Sessiya imtahanı gecəsi LMS-ə girmək olmur: hücum deyil, inventar problemidir. Həll: ACME avtomatlaşdırması, sertifikatların inventarı, bitməyə 30 gün qalmış monitorinq.
:::

### Brauzer xətaları

| Chrome xətası | Səbəb | İlk addım |
| --- | --- | --- |
| NET::ERR_CERT_DATE_INVALID | Müddət bitib və ya cihaz saatı səhvdir | Tarixi və sertifikatı yoxlamaq |
| NET::ERR_CERT_COMMON_NAME_INVALID | Domen SAN siyahısında yoxdur | Sertifikatı düzgün domenə buraxmaq |
| NET::ERR_CERT_AUTHORITY_INVALID | Zəncir etibarlı kökə çatmır, aralıq sertifikat yoxdur, özünü imzalayıb, TLS yoxlaması gedir | Tam zənciri qurmaq, CA-nı yoxlamaq |
| NET::ERR_CERT_REVOKED | Sertifikat ləğv olunub | Yeni sertifikat buraxmaq |
| ERR_SSL_VERSION_OR_CIPHER_MISMATCH | Ortaq versiya və ya şifr yoxdur | Server konfiqurasiyasına baxmaq |

Hər xəbərdarlıq MITM əlaməti ola bilər. Kampus Wi-Fi-ında birdən bütün saytlar ERR_CERT_AUTHORITY_INVALID verirsə istifadəçi keçməməli, İT xidmətinə xəbər verməlidir.

### Qarşılıqlı TLS (mTLS)

mTLS-də server CertificateRequest göndərir, müştəri də sertifikat təqdim edib gizli açarı ilə imza atır: parolsuz, oğurlanması çətin kimlik. İstifadə: xidmətlərarası rabitə, SIEM agentinin kolektora qoşulması, korporativ VPN, Wi-Fi-da EAP-TLS. Çətinlik: çoxlu müştəri sertifikatının buraxılması, yenilənməsi, ləğvi üçün daxili PKI.

### Şəffaflıq jurnalları və DigiNotar dərsi

2011-də Hollandiyanın **DigiNotar** CA-sı sındırıldı, hücumçular *.google.com üçün saxta sertifikat buraxdı; əsasən İrandakı istifadəçilərə qarşı MITM üçün işlədildi. DigiNotar həmin il müflis oldu. Dərs: bütün sistem hər CA-nın səhvsiz işləməsindən asılıdır. **Certificate Transparency** (RFC 6962) cavabdır: sertifikatlar açıq, yalnız əlavə oluna bilən jurnallara yazılır, domen sahibi öz domeni üçün buraxılanları izləyir.

### Məşhur hücumlar

| Ad | İl | Nədən istifadə edir | Qorunma |
| --- | --- | --- | --- |
| SSL stripping | 2009 | HTTPS-ə keçid anında istifadəçini HTTP-də saxlayır | HSTS |
| BEAST | 2011 | TLS 1.0-da CBC-nin proqnozlaşdırıla bilən IV-si | TLS 1.2+, AEAD |
| CRIME | 2012 | TLS sıxılması sirrin uzunluğunu açır | Sıxılmanı söndürmək |
| Heartbleed | 2014 | OpenSSL 1.0.1–1.0.1f Heartbeat səhvi, CVE-2014-0160; sorğu başına 64 KB-a qədər server yaddaşı | OpenSSL yeniləmə, açarları və sertifikatları dəyişmək |
| POODLE | 2014 | SSL 3.0 padding zəifliyi | SSL 3.0-ı söndürmək |
| FREAK, Logjam | 2015 | Köhnə "export" zəif şifrlərinə endirmə | Zəif şifrləri çıxarmaq, güclü DH |
| DROWN | 2016 | Eyni açarı işlədən SSLv2 serveri TLS-i də zəiflədir | SSLv2-ni hər yerdə söndürmək |
| ROBOT | 2017 | RSA padding oracle | Statik RSA-nı söndürmək |

Heartbleed protokolun deyil, proqram səhvi idi: OpenSSL sorğudakı uzunluğu yoxlamırdı; gizli açarlar, parollar, sessiya məlumatları sızırdı. Düzəlişdən sonra açarlar da dəyişdirilməli idi, çünki artıq oğurlanmış ola bilərdi.

### Sessiyanın bərpası

Hər bağlantıda tam əl sıxması bahalıdır. TLS 1.2-də sessiya ID və sessiya biletləri, TLS 1.3-də PSK əsaslı bərpa. Bilet şifrələnmiş sessiya vəziyyəti və ya server bazasına istinad ola bilər. Biletin açarı sızsa TLS 1.2 bilet bərpası, TLS 1.3 psk_ke trafiki və 0-RTT təhlükəyə düşür; psk_dhe_ke ilə qurulan 1-RTT trafik təzə (EC)DHE sayəsində irəli məxfiliyi saxlayır. Bilet açarları tez-tez dəyişdirilir.

### TLS nəyi qorumur

TLS tətbiqin özünü qorumur: SQL inyeksiyası, XSS, zəif parol HTTPS üzərindən də işləyir; məlumat serverdə və müştəridə açıqdır. ClientHello-da iki oxşar uzantı: SNI domeni, ALPN tətbiq protokolunu (h2, http/1.1) seçir. QUIC TLS 1.3-ün əl sıxmasını və açar törətməsini işlədir, TLS record qatını yox, paketləri özü qoruyur.

Metaməlumat qalır: IP ünvanları, vaxt və həcm, TLS 1.3-də belə ClientHello-dakı SNI. RFC 9849 (2026) ilə standartlaşmış **ECH** (Encrypted Client Hello) ClientHello-nun həssas hissəsini serverin açıq açarı ilə şifrələyir.

### HSTS

İstifadəçi portal.universitet.example yazanda brauzer çox vaxt əvvəl HTTP ilə gedir, server HTTPS-ə yönləndirir. Açıq Wi-Fi-dakı hücumçu bu ilk açıq sorğunu tutub istifadəçini HTTP-də saxlaya bilər (SSL stripping). HSTS (RFC 6797) başlığı brauzerə "bu sayta yalnız HTTPS ilə gəl" deyir. İlk ziyarət problemi üçün domen brauzerlərin əvvəlcədən yüklənmiş HSTS siyahısına əlavə edilə bilir.

### Kvant təhlükəsi

"Harvest now, decrypt later": hücumçu bu gün şifrəli trafiki yazıb gələcəkdə kvant kompüteri ilə aça bilər. NIST 2024-də ML-KEM-i FIPS 203 kimi standartlaşdırdı. Brauzerlər və böyük xidmətlər klassik X25519 ilə ML-KEM-768-i birləşdirən hibrid mübadiləni (X25519MLKEM768) işlədir.

### Düzgün konfiqurasiya və yoxlama

```nginx
ssl_protocols TLSv1.2 TLSv1.3;
ssl_prefer_server_ciphers off;
ssl_session_tickets off;
add_header Strict-Transport-Security "max-age=63072000" always;
```

Yoxlama əmrləri: birincisi TLS 1.3 bağlantısını, ikincisi TLS 1.0-ı sınayır (uğursuzluğun serverin rədd etməsindən, yoxsa müştərinin yerli OpenSSL siyasətindən olduğu ayrılmalıdır), üçüncüsü tarixləri və SAN-ı göstərir, dördüncüsü server tərəfində versiya və şifrləri sadalayır.

```bash
openssl s_client -connect portal.universitet.example:443 -tls1_3
openssl s_client -connect portal.universitet.example:443 -tls1
echo | openssl s_client -connect portal.universitet.example:443 2>/dev/null \
  | openssl x509 -noout -dates -subject -ext subjectAltName
nmap --script ssl-enum-ciphers -p 443 portal.universitet.example
```

Wireshark-da əl sıxmasını `tls.handshake.type == 1` süzgəci ilə tapmaq olar (ClientHello-da SNI və şifr dəstləri görünür). İctimai saytlar üçün Qualys SSL Labs konfiqurasiyanı qiymətləndirir. NIST SP 800-52 Rev. 2 dövlət sistemləri üçün TLS 1.2 və 1.3 tələblərini müəyyən edir.

### Yoxlama siyahısı

- TLS 1.0, 1.1, SSLv2, SSLv3 söndürülüb.
- RC4, 3DES, CBC əsaslı, NULL və EXPORT şifrləri söndürülüb.
- Serverdə tam zəncir qurulub (aralıq sertifikat da verilir).
- HTTP-dən HTTPS-ə yönləndirmə və HSTS aktivdir.
- Yeniləmə ACME ilə avtomatlaşdırılıb, monitorinq var.
- Gizli açar 0600 icazələri ilə saxlanır, repozitoriyaya düşmür.
- Daxili trafik də (tətbiq və baza arası) TLS ilə qorunur.

## DNS təhlükəsizliyi və DNSSEC

### DNS necə işləyir

DNS domen adlarını IP-yə çevirir. Kompüter sorğunu rekursiv həllediciyə göndərir; keşdə yoxdursa həlledici iyerarxiya ilə aşağı gedir: kök serverlərdən TLD serverini, ondan domenin avtoritativ serverini öyrənir, A qeydini alır. Cavab TTL müddətinə keşlənir.

![figure](m04-7.png)

DNS şəbəkə iştirakçılarının bir-birini tanıdığı dövrdə layihələnib; cavablarda orijinallığı yoxlayan heç nə yoxdur. Sorğular adətən UDP 53-də açıq gedir. Həlledici cavabı qəbul edərkən yalnız sorğuya uyğunluğa baxır: 16 bitlik sorğu identifikatoru (TXID), mənbə portu, ad.

| Qeyd | Məzmun | Nümunə |
| --- | --- | --- |
| A | IPv4 ünvanı | 203.0.113.10 |
| AAAA | IPv6 ünvanı | 2001:db8::10 |
| CNAME | Başqa ada istinad | www → portal |
| MX | Poçt serveri | mx1.universitet.example |
| NS | Avtoritativ server | ns1.universitet.example |
| TXT | Mətn; SPF, DKIM, DMARC üçün | v=spf1 -all |
| PTR | IP-dən ada çevirmə | Qeydlərdə ad göstərmək üçün |
| SOA | Zonanın əsas parametrləri | Seriya nömrəsi, TTL dəyərləri |

Cavab böyük olanda və ya zona ötürülməsində (AXFR) TCP 53 işlədilir. EDNS(0) UDP cavabının ölçüsünü artırır və DNSSEC-in DO bayrağını daşıyır; ona görə firewall-da yalnız UDP 53-ü açıq saxlamaq DNSSEC-də nasazlıq yaradır.

### DNS hücumları

| Hücum | Mahiyyəti | Əsas qorunma |
| --- | --- | --- |
| Keşin zəhərlənməsi | Həlledicinin keşinə saxta qeyd yeridilir | Təsadüfi port və TXID, DNSSEC yoxlaması |
| DNS spoofing (LAN) | Yerli şəbəkədə qurbanın sorğusuna saxta cavab | DHCP snooping, DAI, DNSSEC, DoT/DoH |
| Domen ələ keçirilməsi | Registrator hesabı oğurlanır, NS qeydləri dəyişir | MFA, Registry Lock |
| DNS tunelləmə | Məlumat və ya C2 trafiki DNS sorğularında gizlədilir | DNS log analizi, çıxışı daxili həlledici ilə məhdudlaşdırma |
| DNS gücləndirmə (amplification) | Saxta mənbə IP ilə kiçik sorğu, böyük cavab qurbana gedir | Açıq həlledicini bağlamaq, RRL, BCP 38 |
| NXDOMAIN və ya subdomen seli | Mövcud olmayan adlarla yükləmə | Sürət məhdudlaşdırması, anycast |

### Kaminski hücumu

2008-də Den **Kaminski** (CVE-2008-1447) keş zəhərlənməsini ciddi təhlükəyə çevirən üsulu göstərdi. Həlledicilərin çoxu sabit mənbə portu işlədirdi, hücumçu yalnız 65 536 TXID variantından birini tapmalı idi. Əvvəllər saxta cavab uğursuz olanda eyni ad TTL bitənə qədər keşdə qalırdı və yeni cəhd gözləməli idi. Kaminski mövcud olmayan a1.universitet.example, a2.universitet.example adlarını sorğulayıb hər dəfə yeni yarış başlatdı; saxta cavaba bütöv domen üçün NS qeydi əlavə edirdi.

Təcili yamaqlar mənbə portunu təsadüfi etdi, axtarış sahəsi təxminən 2³² oldu. Bu yalnız ehtimalı azaldır, yolda olan hücumçuya qarşı işləmir. Əsaslı həll kriptoqrafik imzadır.

:::example Kampus keşinin zəhərlənməsi
Həlledicinin keşinə lms.universitet.example üçün hücumçunun IP-si yeridilib. Tələbə ünvanı düzgün yazır, saxta giriş səhifəsinə düşür, parolunu özü verir. TLS sertifikatı saxta saytı aşkar edə bilər, amma xəbərdarlıq keçilibsə və ya HTTP ilə gedilirsə hücum alınır.
:::

### DNSSEC nəyi qoruyur

DNSSEC (Domain Name System Security Extensions, RFC 4033–4035, indiki təsvir RFC 9364) qeydlərə rəqəmsal imza əlavə edir; həlledici cavabın domen sahibindən gəldiyini və dəyişdirilmədiyini yoxlayır.

| Verir | Vermir |
| --- | --- |
| Məlumatın mənşəyinin autentifikasiyası | Məxfilik: sorğu və cavablar açıq |
| Məlumatın tamlığı | DDoS-dan qorunma (əksinə, cavablar böyüyür) |
| Adın mövcud olmamasının sübutu | Registrator hesabının ələ keçirilməsindən qorunma |
| Keş zəhərlənməsi və saxtalaşdırmadan qorunma | Yoxlamayan həlledici qoruma vermir |

:::exam
Ən çox buraxılan səhv: "DNSSEC DNS-i şifrələyir". Yox: imza qoyur, yəni bütövlük və mənşə autentifikasiyası verir. Məxfilik üçün DoT və DoH.
:::

### DNSSEC qeyd tipləri

| Qeyd | Vəzifəsi |
| --- | --- |
| RRSIG | Qeydlər dəstinin (RRset) imzası; alqoritm, müddət və imzalayan açarın nişanını saxlayır |
| DNSKEY | Zonanın açıq açarı; flags 257 KSK, 256 ZSK |
| DS | Valideyn zonada, uşaq zonanın adətən KSK olan DNSKEY-inə istinad edir; digest DNSKEY sahibinin adı və məzmunundan hesablanır; zonalar arası etibar körpüsü |
| NSEC | Sıradakı mövcud adı göstərib aradakıların olmadığını sübut edir |
| NSEC3 | NSEC-in heşlənmiş variantı, adların siyahılanmasını çətinləşdirir (RFC 5155) |
| CDS, CDNSKEY | Uşaq zonanın yeni DS barədə valideynə avtomatik siqnalı |

Zonada adətən iki açar: **ZSK** (Zone Signing Key) qeydləri imzalayır, tez dəyişdirilir, qısa ola bilir; **KSK** (Key Signing Key) yalnız DNSKEY dəstini imzalayır, valideyndəki DS ona istinad edir. Beləliklə ZSK dəyişəndə valideyn zonaya müraciət lazım olmur. Bölgü məcburi deyil: bir açarla (CSK, Combined Signing Key) də imzalamaq olur.

Alqoritmlər: ən çox 13 (ECDSA P-256/SHA-256) və 8 (RSA/SHA-256), 15 (Ed25519) də işlənir; SHA-1 əsaslı 5 və 7 köhnəlib. ECDSA imzaları RSA-dan xeyli qısadır, cavablar kiçik qalır.

### Etibar zənciri

![figure](m04-8.png)

Yoxlayan həlledicidə (validating resolver) əvvəlcədən bir açar saxlanır: kök zonanın KSK-sı, **etibar lövbəri** (trust anchor). Yoxlama:

1. Həlledici kökün DNSKEY dəstini alır, KSK-nı etibar lövbəri ilə tutuşdurur, həmin açarla dəstin RRSIG imzasını yoxlayır. ZSK yalnız bundan sonra etibarlıdır.
2. Kökün ZSK-sı ilə example. üçün DS qeydinin imzasını yoxlayır.
3. example. zonasının DNSKEY dəstini alır, KSK-nı DS ilə tutuşdurur, dəstin imzasını həmin KSK ilə yoxlayır.
4. Eyni əməliyyatı universitet.example. üçün təkrarlayır.
5. Sonda A qeydinin RRSIG imzasını domen zonasının təsdiqlənmiş ZSK-sı ilə yoxlayır.

Dörd vəziyyət: zəncir tamdırsa **Secure** və həlledici AD bayrağı qoyur. Delegasiyada DS-in olmaması imzalı sübut olunubsa **Insecure** (cavab adi qaydada verilir). Etibar lövbəri olmayanda **Indeterminate** ola bilər. İmza səhvdirsə və ya vaxtı keçibsə **Bogus**: həlledici cavabı qaytarmır, SERVFAIL verir; domen sahibinin səhvi domeni yoxlayan həlledicilər üçün əlçatmaz edir.

Sorğuda iki bayraq: **DO** DNSSEC qeydlərini də qaytarmağı, **CD** yoxlamanı söndürməyi xahiş edir. `dig +dnssec` özü yoxlamır (yoxlamanı həlledici aparır), `delv` yoxlamanı yerində edir.

```text
$ dig +dnssec A universitet.example
;; flags: qr rd ra ad; QUERY: 1, ANSWER: 2
universitet.example. 300 IN A     203.0.113.10
universitet.example. 300 IN RRSIG A 13 2 300 20261201000000 20261101000000 38421 universitet.example. kX3v...
$ dig DS example. +short
$ delv A universitet.example
```

RRSIG sətrində 13 alqoritmi, 2 domen adındakı etiketlərin sayını (universitet, example), 300 orijinal TTL-i, sonrakı iki tarix imzanın bitmə və başlama vaxtını, 38421 açar nişanını göstərir. `ad` bayrağı yoxlamanın uğurla getdiyini bildirir.

:::warning AD bayrağına nə qədər etibar
AD bayrağı son cihazla həlledici arasında heç nə ilə qorunmur. Kompüter ona yalnız həlledici etibarlıdırsa və kanal qorunursa (yerli həlledici, DoT və ya DoH) inana bilər.
:::

### Saxta cavab necə ifşa olunur

Hücumçu lms.universitet.example üçün saxta A 198.51.100.66 yeridir. İki variant:

- **RRSIG yoxdur:** həlledici zonanın imzalı olduğunu valideyndəki DS-dən bilir, RRSIG-in yoxluğunu pozuntu sayır, cavab Bogus.
- **Hücumçu RRSIG yaradır:** öz açarı ilə imzalayır, imza zonanın DNSKEY-i ilə uyğun gəlmir. Öz DNSKEY-ini göndərsə heşi example. zonasındakı DS-ə uyğun gəlmir; DS-i dəyişmək üçün example. açarı lazımdır, onu da kök təsdiqləyir, başında etibar lövbəri durur. Zəncirin heç yerində imza yarada bilmir.

**Replay:** köhnə, amma düzgün imzalı cavabı təkrar göndərmək başqa məsələdir; imzanın müddəti bitməyibsə həlledici qəbul edir. Ona görə RRSIG müddətləri qısa seçilir, adətən günlər və ya həftələr.

### DNSSEC və TLS PKI-sinin etibar modeli

| Meyar | TLS PKI | DNSSEC |
| --- | --- | --- |
| Etibar başlanğıcı | Brauzerdə yüzlərlə kök CA | Bir kök: DNS kök zonası |
| Kim imzalayır | İstənilən etibarlı CA hər domen üçün | Yalnız valideyn zona uşağı təsdiqləyir |
| Nəyi qoruyur | Əlaqə kanalını | DNS məlumatını |
| Sızma nəticəsi | Bir CA bütün internet üçün saxta sertifikat verə bilər | Zəiflik həmin zonanın aşağısı ilə məhdudlaşır |
| Harada yoxlanır | Müştəridə | Adətən həlledicidə |

### Mövcud olmayan adların sübutu

Həlledici "belə ad yoxdur" cavabını da yoxlaya bilməlidir, əks halda saxta NXDOMAIN ilə domen "yox edilərdi". NSEC qeydləri əvvəlcədən hazırlanır və sıralanmış siyahıda növbəti mövcud adı göstərir: `a.universitet.example NSEC lms.universitet.example` yəni a ilə lms arasında ad yoxdur.

Yan təsir **zona siyahılanması** (zone walking): NSEC zəncirini izləyən bütün adları öyrənir (vpn-test, db-backup kimi). NSEC3 adları heşləyir, amma lüğət hücumu qalır. Tam müdafiə üçün cavabı anında imzalayan "ağ yalanlar" (compact denial) üsulu. RFC 9276 NSEC3-də iterasiya sayını 0, salt-ı boş saxlamağı tövsiyə edir (böyük iterasiya həlledicini yükləyir).

İki mənfi cavab: **NXDOMAIN** adın ümumiyyətlə olmadığını, **NODATA** (kod NOERROR) ad olsa da istənilən tipdə qeydin olmadığını bildirir. Hər ikisi üçün ayrıca imzalı sübut verilir.

### Açarların idarəsi və kök KSK dəyişimi

Açarlar vaxtaşırı dəyişdirilir (key rollover); imzaların bitmə tarixi olduğundan imzalamanın avtomatik davam etməsi şərtdir. Ən tipik nasazlıq: vaxtında yenilənməmiş imza və ya uyğunsuz DS.

2010-un iyulunda kök zona imzalandı. İlk kök KSK dəyişimi 11 oktyabr 2018-də oldu. ICANN yeni KSK-2024 açarını (nişan 38696) 2025-də kök zonaya əlavə edib; cədvələ görə 11 oktyabr 2026-dan kök zonanı o imzalamalı, köhnə KSK-2017 11 yanvar 2027-də ləğv edilməlidir. Etibar lövbərini yeniləməyən həlledicilərdə ad həlli pozulur. Həlledicilər yeni kök açarı RFC 5011 ilə, saxlama müddətindən (hold-down, 30 gün) sonra qəbul edir. Həlledicinin saatı səhv olsa imzalar vaxtı keçmiş görünür.

30 sentyabr 2021-də **Slack** slack.com üçün DNSSEC-i işə salanda yaranan problem üzündən bəzi istifadəçilər xidmətə çata bilmədi. Geri qaytarmaq üçün DS-i silmək kifayət etmədi, keşlərdə köhnə məlumat TTL bitənə qədər qaldı.

ZSK dəyişimində **pre-publish**: yeni açar DNSKEY dəstinə əlavə olunur, keşlərin görməsi gözlənilir, imzalamaya keçilir, köhnə imzaların TTL-i bitəndən sonra köhnə açar silinir. KSK dəyişimində valideyndəki DS də dəyişdiyi üçün addımlar çoxdur. Keş TTL-ləri nəzərə alınmasa həlledicilər yeni imzanı köhnə açarla yoxlayıb uğursuz olur.

### Məhdudiyyətlər və əlaqəli texnologiyalar

DNSSEC cavabları böyükdür: gücləndirmə hücumları cazibədar olur, UDP fraqmentasiyası yaranır, TCP 53-ü bağlayan firewall-larda cavablar itir. Səhv DS domeni əlçatmaz edir.

| Texnologiya | Port | Nə qoruyur | Harada işləyir |
| --- | --- | --- | --- |
| DNSSEC | 53 | Bütövlük, mənşə | Zona və həlledici arasında, məlumat səviyyəsində |
| DoT (RFC 7858) | TCP 853 | Məxfilik, kanal | Müştəri ilə həlledici arasında |
| DoH (RFC 8484) | TCP 443 | Məxfilik, kanal | Müştəri ilə həlledici arasında, HTTPS içində |
| DoQ (RFC 9250) | UDP 853 | Məxfilik, kanal | Müştəri ilə həlledici arasında, QUIC üzərində |

Bunlar bir-birini əvəz etmir: DoH kanalı qoruyur, amma həlledici saxta cavab alıbsa onu şifrəli çatdıracaq; DNSSEC düzgünlüyü sübut edir, sorğunu gizlətmir. DoH təhlükəsizlik komandası üçün riskdir: brauzer sorğuları korporativ DNS-dən yan keçə bilir, süzgəclər və qeydlər kor qalır; korporativ şəbəkədə DoH daxili həlledici və ya siyasətlə idarə olunur.

**DANE** (RFC 6698) DNSSEC ilə qorunan TLSA qeydləri ilə TLS sertifikatını domenə bağlayır; poçt serverləri arası SMTP üçün işlənir.

### Qurulma addımları

1. Registrator və ya DNS provayderinin DNSSEC və DS qeydini dəstəkləməsi yoxlanır.
2. Açarlar yaradılır, alqoritm seçilir (tövsiyə: 13).
3. Zona imzalanır; Bind və PowerDNS-də inline signing imzaları avtomatik yeniləyir.
4. DS qeydi registrator vasitəsilə valideyn zonaya yerləşdirilir.
5. Yoxlama: dig +dnssec, delv, DNSViz, Verisign DNSSEC Analyzer.
6. Daxili həlledicidə yoxlama açılır: BIND-də `options { dnssec-validation auto; };`, Unbound-da `module-config: "validator iterator"` və `auto-trust-anchor-file: "/var/lib/unbound/root.key"`.
7. İmza bitmə tarixləri və DS uyğunluğu monitorinq edilir.
8. Geri qaytarma planı yazılır, TTL-lər nəzərə alınır.

:::note Köhnə slaydlarla fərq
Bir slaydda risk yalnız ehtimal kimi verilib (düzgünü: ehtimal və təsir). "İnvaziv qoruma" termini yoxdur: IPS nəzərdə tutulur. ISO/IEC 27005 proqram aləti deyil, rəhbər sənəddir. OSI-də 7 tətbiq, 6 təqdimatdır. MAC ünvanı 48 bitdir, ARP IPv4-ü MAC-a çevirir. TCP əl sıxması etibarlıdır, təhlükəsiz deyil. FC00::/7 unikal lokal ünvanlardır (ULA); CIDR sinifsiz domenlərarası marşrutlaşdırmadır, A/B/C sinifləri tarixi anlayışdır.
:::

## Təkrar kartları

:::flashcards
[[card]]
front = "ALE necə hesablanır?"
back = "**ALE = SLE × ARO.** İllik gözlənilən itki = bir hadisənin ziyanı × ildə gözlənilən say."

[[card]]
front = "DNSSEC nəyi vermir?"
back = "Məxfilik (şifrələmə), DDoS qorunması, registrator hesabının qorunması. Məxfilik üçün DoT/DoH."
:::
