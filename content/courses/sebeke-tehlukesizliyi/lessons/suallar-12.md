+++
title = "SIEM və istifadəçi davranışlarının təhlili (UEBA)"
unit = "suallar"
order = 12
summary = "Mövzu üzrə bütün nəzarət sualları və situasiya tapşırıqları cavabları ilə: mühazirənin 20 sualı, 7 situasiyası, konspektin 3 situasiyası və ehtimal olunan əlavə suallar."
updated = 2026-11-09

[[source]]
title = "Mühazirə 12: SIEM və istifadəçi davranışlarının təhlili (UEBA)"
note = "Elmar Cabbarov, 2026–2027"

[[source]]
title = "Midterm konspekti, Mövzu 12"
note = "Elmar Cabbarov"
+++

İmtahan yazılı açıq suallardır; cavabı əvvəlcə özün yaz, sonra aç. Universitet situasiyalarındakı vaxt, say və ballar şərtidir.

## Nəzarət sualları

:::reveal SIM və SEM SIEM-də necə birləşir?
- **SIM** (Security Information Management): uzunmüddətli saxlama, axtarış, hesabat.
- **SEM** (Security Event Management): real vaxt monitorinq, korrelyasiya, xəbərdarlıq.
- SIEM ikisini bir sistemdə birləşdirir: toplayır, vahid formaya gətirir, əlaqələndirir, xəbərdarlıq yaradır və araşdırma üçün saxlayır.
- Termini 2005-ci ildə Gartner analitikləri işlədib.
:::

:::reveal Hadisə, xəbərdarlıq və insident arasında fərq nədir?
- **Hadisə (event):** sistemdə baş verən və qeydə alınan fəaliyyət (hesaba giriş); log qeydi onu təsvir edən saxlanılmış sətirdir.
- **Xəbərdarlıq (alert):** aşkarlama məntiqinin araşdırılmalı saydığı nəticə (10 dəqiqədə 20 uğursuz giriş); TP və ya FP ola bilər.
- **İnsident (incident):** təhlükəsizliyi pozan və ya real təhdid edən hadisə (oğurlanmış hesabla məlumatın çıxarılması).
- Hadisə → xəbərdarlıq → (təsdiqlənərsə) insident; hər xəbərdarlıq insident deyil.
:::

:::reveal Normallaşdırma nə üçün lazımdır?
- Fərqli mənbələr eyni şeyi fərqli adlandırır: firewall `src`, Windows `IpAddress`, VPN `client_ip`.
- Normallaşdırma onları vahid sahəyə (`source.ip`) gətirir, bir qayda bütün mənbələri əhatə edir.
- ECS və OCSF bu məqsədlə yaradılıb; onlar ötürmə protokolu deyil, sahə adı və məna sxemidir.
- Düzgün ayrışdırılmayan log korrelyasiyaya düşmür: mərhələdə səhv növbətini korlayır.
:::

:::reveal Hadisənin baş vermə və SIEM-ə çatma vaxtı niyə ayrıca saxlanılır?
- Bunlar fərqli anlayışlardır (məsələn, hadisə 10:00, SIEM-də indeks 10:07).
- Fərq mənbə, ötürmə kanalı, növbə və indeksləmə problemini göstərir.
- Gecikmə korrelyasiyanı pozur: 5 dəqiqəlik pəncərə gec gələn hadisəni buraxa bilər. Ardıcıllıq hadisə vaxtına (event time) görə qiymətləndirilir.
- Vaxt NTP ilə sinxron olmalı, UTC-də saxlanmalı, ilkin qurşaq qorunmalıdır.
:::

:::reveal Yanlış mənfi nəticə niyə yanlış müsbətdən təhlükəlidir?
- **FN:** hücum var, SIEM susub; heç kim xəbər tutmur, hücum davam edir.
- **FP:** hücum yoxdur, xəbərdarlıq var; analitikin vaxtını alır, amma hücumu gizlətmir.
- Çox FP xəbərdarlıq yorğunluğu yaradır və dolayı yolla FN-ə aparır; yenə də FN-in zərəri birbaşadır.
- Qaydanı söndürmək FP-ni sıfırlayır, FN-ni artırır.
:::

:::reveal 4625, 4624, 4688, 4732 və 1102 hadisələri nəyi göstərir?
- **4625:** uğursuz giriş (kobud güc, parol püskürtməsi).
- **4624:** uğurlu giriş (Logon Type 3 şəbəkə, 10 RDP); MFA keçdiyini sübut etmir.
- **4688:** yeni proses yaradıldı; komanda sətri audit siyasəti ilə açılır, defolt yazılmır.
- **4732:** qrupa üzv əlavə edildi, imtiyaz artımı (Subject edən, MemberSid əlavə olunan).
- **1102:** audit jurnalı təmizləndi, izlərin silinməsi.
:::

:::reveal Hədd və ardıcıllıq korrelyasiyası nə ilə fərqlənir?
- **Hədd əsaslı:** pəncərədə hadisə sayı həddi keçir (10 dəqiqədə 20 uğursuz giriş).
- **Ardıcıllıq:** hadisələr müəyyən sıra ilə baş verir (uğursuz girişlər, sonra uğurlu giriş, yeni cihaz, həssas resurs).
- Hədd sayır, ardıcıllıq sıranı və hadisələr arasındakı məsafəni yoxlayır.
- Hər ikisi hesab, IP, vaxt üzrə əlaqə qurur; pəncərə sərhədi və gecikmə hər ikisinə təsir edir.
:::

:::reveal Parol püskürtməsini aşkar etmək üçün niyə fərqli hesablar sayılır?
- Püskürtmədə bir parol çoxlu hesaba sınanır, hər hesaba yalnız 1–2 cəhd düşür.
- Hesab üzrə hədd qaydası (10 uğursuz giriş) işləmir, çünki say həddən aşağıdır.
- Mənbə IP üzrə **fərqli hesabların sayı** (dcount/dc) götürülür: məsələn 10 dəqiqədə cəhd > 20 və hesab > 10.
- MITRE ATT&CK T1110.003; brute force isə T1110.001.
:::

:::reveal UBA və UEBA arasında fərq nədir?
- **UBA** yalnız istifadəçiləri, **UEBA** həm də cihazları, serverləri, tətbiqləri və xidmət hesablarını izləyir.
- UEBA əlavə tutur: yoluxmuş server, sui-istifadə olunan xidmət hesabı.
- Fərq alqoritmdə yox, izlənən obyektlərin dairəsindədir; maşın öyrənməsini UBA da işlədir.
- Hər ikisi baza profili qurur: öz tarixçəsi, oxşar qrup, təşkilat ortalaması.
:::

:::reveal z-balı nə göstərir? Anomaliya niyə insident deyil?
- z = (x − μ) / σ: dəyərin ortadan neçə standart kənarlaşma uzaqda olduğunu göstərir. μ = 200, σ = 50, x = 500 → z = 6.
- Z-balı standartlaşdırılmış məsafədir; nadirlik ehtimalı çıxarmaq normal paylanma fərziyyəsi tələb edir (dövrilik, sıfır dispersiya, əyri paylanma yanıldır).
- Anomaliya risk deyil: imtahan həftəsi, konfrans, gecə iş qanuni ola bilər. Model diqqəti yönəldir, qərarı analitik verir.
- Risk balı anomaliyanı kontekstlə (təhdid, həssaslıq) birləşdirir.
:::

:::reveal SIEM ilə SOAR arasında fərq nədir?
- **SIEM:** toplayır, normallaşdırır, əlaqələndirir, xəbərdarlıq yaradır (aşkarlama).
- **SOAR:** playbook-larla araşdırma və cavabı avtomatlaşdırır (zənginləşdirmə, bilet, məhdudlaşdırma); əsas vəzifəsi iş axınıdır.
- Hesab bloklama kimi yüksək təsirli addımlar analitikin təsdiqi, həddi və geri qaytarma planı ilə icra olunur.
- Əlaqəli: EDR (qurğu səviyyəsi), XDR (bir neçə qat), UEBA (SIEM modulu), SOC (komanda).
:::

:::reveal MTTD və MTTR nədir?
- **MTTD:** hücumun başlanğıcından aşkarlanmaya qədər orta vaxt.
- **MTTR:** aşkarlanmadan aradan qaldırılmaya (bərpaya) qədər orta vaxt.
- Nümunə: gecikmələr 8, 12, 25 dəq → MTTD = 45 / 3 = 15 dəq; 30, 50, 100 dəq → MTTR = 180 / 3 = 60 dəq.
- Tərif açıq yazılır (MTTR ilk cavaba qədər də ola bilər); orta vaxt gecikmiş kritik işi gizlədir, median və yuxarı persentillər də verilir.
:::

:::reveal Sabit və sürüşən pəncərə sərhəddəki hücumu necə fərqli görür?
- **Sabit (tumbling):** vaxtı üst-üstə düşməyən hissələrə bölür (09:50–10:00, 10:00–10:10).
- **Sürüşən (sliding):** hər qiymətləndirmə anından əvvəlki intervalı götürür.
- 09:58-də 12, 10:03-də 12 cəhd: sabit pəncərələrin heç birində >20 yoxdur; 10:03-də bitən 10 dəqiqəlik sürüşən pəncərə 24 cəhd görür.
- Xərci: sürüşən daha çox vəziyyət saxlayır və hadisələri təkrar qiymətləndirir.
:::

:::reveal ECS və OCSF hansı problemi həll edir, nəyi həll etmir?
- **Həll edir:** sahə adlarını və mənalarını vahidləşdirir (ECS sahə sxemi; OCSF hadisə sinifləri, kateqoriyalar, atributlar), bir qayda bütün mənbələrdə işləyir.
- **Həll etmir:** ötürmə protokolu deyil (syslog ilə gələn hadisə onlara uyğunlaşdırılır); yalnız ad dəyişmək semantik uyğunluğu qorumur.
- Dəyişməz şəxs identifikatorunu əvəz etmir (ali, UNEC\ali, ali@kampus.example eyni hesab ola bilər).
- Atribut yolu və enum dəyərləri sxem versiyasına görə yoxlanır.
:::

:::reveal WORM ilə heş zəncirinin verdiyi zəmanətlər necə fərqlənir?
- **WORM:** müddət ərzində obyektin dəyişdirilməsini və silinməsini **məhdudlaşdırır** (qarşısını alır); sadə «yalnız oxu» icazəsi WORM deyil, admin onu geri dəyişir.
- **Heş zənciri:** H_i = SHA-256(H_(i−1) || qeyd_i); sonradan dəyişikliyi **aşkarlayır**, silməni qarşısını almır.
- Hücumçu bütün arxivi və ilk etibar nöqtəsini dəyişə bilirsə, zənciri yenidən hesablayar: son heşlər ayrıca, imzalanmış manifestdə saxlanır.
- Heş mənbənin əvvəlcə doğru yazdığını sübut etmir. Sınaqda SIEM admininin arxivi təkbaşına silə bilmədiyi təsdiqlənməlidir.
:::

:::reveal Isolation Forest nəticəsi niyə hücum etiketi sayılmır?
- Üsul təsadüfi bölünmələrlə çoxluqdan uzaq nöqtəni daha az bölünmə ilə ayırır; çıxış **anomaliya göstəricisidir**, sinif etiketi deyil.
- Kənar müşahidə sadəcə nadirdir (yeni layihə, mövsüm, arxivləşdirmə); hücum faktı analitik yoxlama ilə təsdiqlənir.
- Kənar müşahidə payı parametri məlum hücum faizi deyil.
- Analitikə hansı xüsusiyyətlərin şəxsin və qrupun tarixçəsindən fərqləndiyi göstərilməlidir.
:::

:::reveal Konseptin sürüşməsi ilə modelin zəhərlənməsi necə ayrılır?
- **Konseptin sürüşməsi (concept drift):** normal davranış təbii dəyişir (sessiya, onlayn dərslər, yeni sistem); yenilənməsə yanlış həyəcan artır.
- **Zəhərlənmə / low and slow:** model çox tez yenilənsə, hücumçu fəaliyyətini tədricən artıraraq normanı özünə uyğun dəyişir.
- Birincisi qanuni dəyişiklikdir, ikincisi qəsdən manipulyasiya; əlamət: bütöv qrup eyni vaxtda dəyişir (akademik təqvim) və ya tək hesab tədricən artır.
- Tədbir: nəzarətli yeniləmə, təsdiqlənmiş insident dövrlərini və etibarsız etiketləri təlimdən çıxarmaq, namizəd modeli kölgə rejimində yoxlamaq.
:::

:::reveal FPR ilə xəbərdarlıqların yanlış payı üçün məxrəclər nədir?
- **FPR = FP / (FP + TN):** məxrəc hücum olmayan bütün hallardır; TN məlum deyilsə hesablanmır.
- **Xəbərdarlıqların yanlış payı = FP / (TP + FP):** məxrəc bütün xəbərdarlıqlardır (1 − dəqiqlik).
- Nümunə: TP 20, FP 80 → yanlış pay 80%; TN = 920 olsa FPR = 80 / 1 000 = 8%.
- İki göstərici fərqli məxrəcə malikdir, qarışdırılmır.
:::

:::reveal Risk balında eyni sübutun təkrar sayılması necə məhdudlaşdırılır?
- «Yeni ölkə», «mümkünsüz səyahət», «nadir IP» eyni VPN girişindən yarana bilər; müstəqil sübut kimi toplansa bal şişər.
- Siqnallar əsas hadisə və səbəb qrupuna bağlanır; qrup üzrə **maksimum bal** və ya **limit** tətbiq olunur.
- DB ixracı ilə həmin fayla aid DLP xəbərdarlığı da eyni ötürməni təsvir edə bilər; fərqli mənbə müstəqil sübut demək deyil.
- Bal ehtimal deyil, prioritetdir; zamanla azalır.
:::

:::reveal SIEM tutumunda sıxılma, indeks, replika və ehtiyat necə hesablanır?
- Xam: 2000 EPS × 500 bayt = 1 MB/s → 86,4 GB/gün.
- Sıxılmadan sonra 0,5 + indeks 0,3: 86,4 × 0,8 = 69,12 GB/gün.
- Bir əsas + bir replika: × 2 = 138,24 GB/gün; 90 gün: 12 441,6 GB.
- +25% əməliyyat ehtiyatı: ≈ 15 552 GB ≈ 15,55 TB (onluq vahid).
- Replika ehtiyat nüsxə deyil; pik yük ortadan yüksək olur (8 000 EPS → 4 MB/s xam), imtahan pikini də sınamaq lazımdır.
:::

## Situasiya tapşırıqları

**Situasiya 1.** LMS administratorunun hesabına gecə 02:11-də VPN-dən 14 uğursuz giriş, 02:13-də isə yeni ölkədən uğurlu giriş qeydə alınıb. 02:21-də AD-də həmin hesab admin qrupuna əlavə olunub (4732), 02:34-də tələbə bazasından 2 GB ixrac olub, 02:41-də proksidə naməlum sayta böyük yükləmə görünüb. SIEM-də yalnız «uğursuz giriş» qaydası var və heç nə baş verməyib. Niyə? Qayda necə olmalıdır?

:::reveal Cavab
- **Aktiv:** LMS admin hesabı və tələbə bazası; pozulan: məxfilik, bütövlük (imtiyaz artımı).
- **Səbəb:** hər hadisə ayrılıqda zəif siqnaldır. Həddi və pəncərəsi verilmədiyindən 14 cəhdin niyə xəbərdarlıq yaratmadığını qəti demək olmaz: qaydanın şərtləri, aktivliyi, pəncərəyə düşmə, mənbənin toplanması və sahələrin düzgün ayrışdırılması yoxlanmalıdır.
- **Tədbir (qayda):** çoxmənbəli ardıcıllıq: eyni hesab üzrə uğursuz girişlərdən sonra yeni yerdən uğurlu giriş, 30 dəqiqə ərzində imtiyaz dəyişikliyi və böyük ixrac.
- **Cavab:** hesabı bağlamaq, sessiyaları kəsmək, qrupdan çıxarmaq, ixrac olunan məlumatı müəyyən etmək, hadisəni insident kimi rəsmiləşdirmək.
:::

**Situasiya 2.** Həftəlik 1200 xəbərdarlıq gəlir, analitik ikisini gözdən qaçırıb və hər ikisi real hücum olub. Araşdırma göstərir ki, xəbərdarlıqların 95%-i bir yedəkləmə tapşırığının yaratdığı yanlış müsbətdir. Nə etmək lazımdır?

:::reveal Cavab
- **Problem:** dəqiqlik çox aşağıdır, xəbərdarlıq yorğunluğu yaranıb (iki real hücum qaçıb).
- **Tədbir:** qayda yedəkləmə hesabı, vaxt və hədəf serveri kontekstinə görə **dar istisna** ilə tənzimlənir.
- Bütün hesabı qaydadan çıxarmaq olmaz: hücumçu həmin hesabdan sui-istifadə edə bilər.
- Xəbərdarlıqlar risk üzrə prioritetləşdirilir, təkrar işlər SOAR ilə avtomatlaşdırılır.
:::

**Situasiya 3.** UEBA Fərid müəllimin hesabı üçün yüksək risk balı verib: ilk dəfə İtaliyadan giriş, gecə saatları, çoxlu fayl yükləmə. Təhlükəsizlik işçisi hesabı dərhal bloklamaq istəyir. Düzgün yanaşma necədir?

:::reveal Cavab
- **Prinsip:** anomaliya insident deyil, əlavə yoxlama tələb edir.
- **Kontekst:** müəllim həmin vaxt ezamiyyətdədirmi, MFA keçibmi, cihaz tanınmışdırmı, faylların xarakteri, başqa siqnal varmı; müəllimlə ayrı kanaldan əlaqə.
- MFA nəticəsi, cihazın tanınması və ixracın qanuniliyi birlikdə qiymətləndirilir; təkcə naməlum cihaz və ya ixrac faktı bloklama üçün kifayət deyil.
- **Tədbir:** məlumat çatışmırsa riskə uyğun əlavə autentifikasiya və sessiya məhdudiyyəti; hesabın ələ keçirilməsi və ya davam edən icazəsiz ötürmə barədə güclü sübut olduqda hesab müvəqqəti bloklanır, sessiyalar kəsilir.
:::

**Situasiya 4.** Araşdırmada məlum olur ki, firewall qeydləri SIEM-ə 3 həftədir gəlmir, amma heç kim bunu görməyib. Hücum məhz həmin vaxtda baş verib. Hansı nəzarət çatışmır?

:::reveal Cavab
- **Çatışmayan:** mənbə sağlamlıq monitorinqi (susan mənbələrə nəzarət).
- Hər mənbə üçün gözlənilən həcm və «son hadisə vaxtı» izlənməli; **yoxluq korrelyasiyası** yazılmalıdır: mənbə N dəqiqədən çox susursa xəbərdarlıq gəlsin.
- Həmin dövrün qeydləri hələ saxlanılırsa, firewall-ın özündən bərpa edilib SIEM-ə yüklənməlidir.
:::

**Situasiya 5.** Universitet VPN-ində hadisə 10:00-da yaranıb, 10:07-də SIEM-ə çatıb. Beş dəqiqəlik qayda uğursuz girişdən sonrakı uğurlu girişi tutmayıb. Analitik ardıcıllıq intervalını dərhal otuz dəqiqəyə artırır. Bu həll düzgündürmü?

:::reveal Cavab
- **Xeyr:** gecikmə ilə hadisələr arasındakı şərt qarışdırılıb.
- Hadisə vaxtı üzrə **5 dəqiqəlik şərt saxlanır**, geriyə baxış intervalı isə gecikməni əhatə edəcək qədər genişləndirilir.
- Təkrar icrada deduplikasiya (xəbərdarlıq açarı) lazımdır.
- VPN ötürülməsi və NTP ayrıca yoxlanır; sadəcə intervalı böyütmək əlaqəsiz girişləri birləşdirə bilər.
:::

**Situasiya 6.** Kafedrada sessiya həftəsi endirmələr artıb. UEBA bütün əməkdaşları yüksək riskli göstərir və modeli həmin günün məlumatı ilə dərhal yeniləmək təklif olunur. Hansı yoxlamalar aparılmalıdır?

:::reveal Cavab
- Oxşar qrup, akademik təqvim, cihazlar və faylların təyinatı yoxlanır.
- Qrup üzrə qanuni mövsümi artım təsdiqlənərsə, **mövsümilik** modelə daxil edilir.
- Cari günü avtomatik norma saymaq olmaz: davam edən hücum da öyrənilə bilər (konseptin sürüşməsi, low and slow).
- Namizəd model kölgə rejimində yoxlanır, insident intervalları təlimdən çıxarılır.
:::

**Situasiya 7.** Kitabxana hesabı üçün yeni ölkə, nadir IP və mümkünsüz səyahət siqnalları birlikdə 90 bal yaradıb. Üçü də eyni VPN girişinə əsaslanır. Bu, üç müstəqil sübutdurmu?

:::reveal Cavab
- **Xeyr:** eyni giriş və coğrafi qiymətləndirmə üç dəfə sayılıb.
- Siqnallar əsas hadisə ilə əlaqələndirilir, eyni səbəb qrupu üzrə limit və ya maksimum bal seçilir.
- Cihaz, MFA, girişdən sonrakı fəaliyyət və VPN çıxışı ayrıca yoxlanır.
- 90 bal 90% hücum ehtimalı deyil: bal prioritetdir.
:::

## Konspektdən situasiyalar

**Situasiya 1.** Qış sessiyası həftəsində UEBA bir müəllim üçün yüksək risk balı verir: o, 3 gündə 2 GB fayl yükləyib (adi orta 150 MB). Analitik dərhal hesabı bloklamaq istəyir. Düzgün yanaşma nədir?

:::reveal Cavab
- **Prinsip:** anomaliya risk deyil, araşdırma səbəbidir.
- **Kontekst:** sessiya həftəsində oxşar qrupun (kafedra müəllimlərinin) yükləmələri də artıbmı (mövsümi davranış)? Fayllar müəllimin öz qruplarının imtahan işləridirmi? Giriş idarə olunan cihazdan, adi yerdən, MFA ilə olubmu? Fayllar təsdiqlənmiş universitet buludunda qalıb, yoxsa xarici xidmətə gedib?
- **Kontekst normaldırsa:** hadisə yanlış müsbət kimi bağlanır, model mövsümi davranışı nəzərə alacaq şəkildə sazlanır.
- **Şübhəli əlamət varsa** (xarici yükləmə, yeni cihaz): əvvəlcə yumşaq tədbir (təkrar MFA tələbi, sessiyanın kəsilməsi), lazım gəlsə bloklama.
:::

**Situasiya 2.** SIEM-də «5 dəqiqədə eyni hesabda 10 uğursuz giriş» qaydası var. Gecə ərzində 1 800 tələbə hesabının hər birinə bir IP-dən 2 dəfə «Yaz2026!» parolu ilə giriş cəhdi olub, qayda heç nə tutmayıb. Niyə və necə düzəltmək olar?

:::reveal Cavab
- **Səbəb:** password spraying: hər hesabda cəhd sayı həddən aşağıdır, hesab üzrə hədd qaydası işləmir.
- **Yeni qaydalar:** «bir mənbə IP-dən və ya ASN-dən qısa müddətdə N-dən çox fərqli hesaba uğursuz giriş» və «uğursuz girişlərdən sonra hər hansı hesabda uğurlu giriş» (ardıcıllıq).
- **Əlavə:** uğurlu girişləri yoxlamaq, həmin parolu qara siyahıya salmaq, MFA-sı olmayan hesabları tapmaq.
:::

**Situasiya 3.** Ardıcıllıq qaydası «uğursuz girişlərdən sonra 5 dəqiqə ərzində uğurlu giriş» axtarır. Məlum olur ki, VPN serverinin logları SIEM-ə 7 dəqiqə gecikmə ilə gəlir və qayda heç vaxt işləmir. Problem nədir?

:::reveal Cavab
- **Problem:** qayda yalnız son 5 dəqiqədə **qəbul olunmuş** logları axtarırsa, VPN-dən 7 dəqiqə gec gələn uğurlu giriş onu tetikləyən uğursuz girişlərlə eyni axtarışa düşmür.
- **Həll:** ardıcıllığı hadisə vaxtına (event time) görə qiymətləndirmək; gecikən hadisələr üçün ayrıca geriyə baxış pəncərəsi və ya gecikmə buferi qurmaq (hadisələr arasındakı 5 dəqiqəlik şərtlə qarışdırmamaq).
- VPN log ötürülməsini düzəltmək, bütün mənbələrdə NTP sinxronizasiyasını yoxlamaq, gecikən və susan mənbələr üçün ayrıca monitorinq qaydası yazmaq.
:::

## Ehtimal olunan əlavə suallar

:::reveal SIEM-in məlumat axınını mərhələlərlə izah edin.
- **Toplama** (agent, syslog, API, kolektor; TLS, bufer) → **ayrışdırma** (sahələr) → **normallaşdırma** (vahid sxem: ECS, OCSF) → **vaxtın sinxronlaşdırılması** (NTP, UTC) → **zənginləşdirmə** (rol, aktiv, IP ölkəsi, təhdid kəşfiyyatı) → **korrelyasiya və xəbərdarlıq** (qaydalar, UEBA) → **saxlama** (isti, ilıq, soyuq; dəyişməzlik).
- Hər mərhələdə səhv növbətini korlayır.
:::

:::reveal Dəqiqlik, tamlıq və FPR-i hesablayın: ayda 100 xəbərdarlıq, 20 TP, 80 FP, 5 qaçırılmış hücum.
- Dəqiqlik = TP / (TP + FP) = 20 / 100 = **20%**.
- Tamlıq = TP / (TP + FN) = 20 / (20 + 5) = **80%**.
- Xəbərdarlıqların yanlış payı = 80 / 100 = 80%.
- FPR = FP / (FP + TN); TN məlum deyilsə hesablanmır; TN = 920 olsa 80 / 1 000 = 8%.
- Nəticə: qayda hücumların çoxunu tutur, amma xəbərdarlıqların 80%-i boşdur; sazlama lazımdır. Dəqiqliyi artırmaq tamlığı azalda bilər.
:::

:::reveal Z-balını hesablayın: orta 200 MB, σ = 50 MB, bu gün 500 MB.
- z = (x − μ) / σ = (500 − 200) / 50 = **6**: normaldan 6 standart sapma uzaq.
- Bu çox nadir haldır, amma risk demək deyil: imtahan həftəsi ola bilər; risk balı anomaliyanı kontekstlə birləşdirir (R = 0,4A + 0,35K + 0,25S; A = 80, K = 60, S = 90 → 75,5).
- Slaydda qrafikdəki başqa rəqəmlərlə (40, 45, 38, 42, cari 100) qarışdırma; şəkildə ayrı nümunə: μ ≈ 202, σ ≈ 29, x = 650 → z ≈ 15.
:::

:::reveal Dörd əsas korrelyasiya növünü nümunə ilə izah edin.
- **Hədd:** bir hesabda 10 dəqiqədə ≥10 uğursuz giriş.
- **Ardıcıllıq:** 10 uğursuz giriş → 15 dəqiqə ərzində uğurlu giriş → yeni cihaz → qiymət bazasına müraciət.
- **Zaman:** müəllim hesabı gecə 03:00-da qiymətləri kütləvi dəyişir.
- **Kontekst əsaslı:** adi istifadəçi girişi, amma IP təhdid feed-indədir və hesab admin roludur.
- Mühazirədə əlavə: çoxmənbəli, təhdid kəşfiyyatı, yoxluq (absence), statistik/davranış.
:::

:::reveal EDR, XDR, UEBA, SOAR və SOC-u SIEM ilə müqayisə edin.
- **EDR:** son qurğuda davranışı izləyib cavab verir; yalnız qurğu, amma daha dərin.
- **XDR:** bir neçə qatın telemetriyasını və cavabını birləşdirir; çox vaxt ekosistemə bağlıdır, açıq inteqrasiya da mümkündür.
- **UEBA:** davranış anomaliyası; SIEM-in modulu və ya məlumat qatı.
- **SOAR:** playbook ilə iş axını avtomatlaşdırması.
- **SOC:** texnologiya deyil, insanlar və proseslər (L1 triage, L2 dərin araşdırma, L3 təhdid ovu və yeni qaydalar).
:::

:::reveal Konseptin sürüşməsi nədir və iki təhlükəsi hansıdır?
- Normal davranış zamanla dəyişir (yeni semestr, vəzifə, onlayn dərslər).
- Model yavaş uyğunlaşsa yanlış həyəcan çoxalır.
- Çox tez uyğunlaşsa hücumçu fəaliyyətini tədricən artıraraq (low and slow) öz davranışını «normal» etdirir.
- Tədbir: nəzarətli baseline yeniləməsi, təsdiqlənmiş insident dövrlərini təlimdən çıxarmaq, böyük dəyişiklikləri planlı hadisələrlə tutuşdurmaq.
:::

:::reveal DLP növləri hansılardır?
- **Şəbəkə DLP:** hərəkətdə olan məlumat (poçt, veb yükləmə): tələbə siyahısı xarici poçta göndərilir.
- **Son qurğu DLP:** istifadədə olan məlumat (USB, çap, kopyalama): maaş cədvəli USB-yə köçürülür.
- **Saxlama/bulud DLP:** sükunətdə olan məlumat (fayl serverləri, SaaS): açıq qovluqda şəxsiyyət vəsiqələri.
- Üsullar: regex, rəqəmsal barmaq izi, etiketlər, maşın öyrənməsi; TLS yoxlaması olmadan şifrəli trafikdə məhduddur; əvvəl izləmə rejimi.
:::

:::reveal NIST SP 800-61 Rev. 3 ilə Rev. 2-nin fərqi nədir?
- Rev. 2-nin dörd mərhələsi: hazırlıq, aşkarlama və təhlil, məhdudlaşdırma/aradan qaldırma/bərpa, dərslər.
- Rev. 3 (aprel 2025) insidentə cavabı NIST CSF 2.0-ın altı funksiyası ilə əlaqələndirir: Govern, Identify, Protect, Detect, Respond, Recover.
- Əvvəlki nəşrin mərhələ sxemini Rev. 3-ün dəyişməz mərhələləri kimi vermək düzgün deyil.
- Jurnal idarəetməsi üçün NIST SP 800-92 (yeni versiya layihəsi 2023).
:::

:::reveal SIEM-in özünün qorunması və məxfilik üçün hansı tədbirlər görülür?
- İdarəetmə hesabları MFA və ən az səlahiyyətlə; qayda yazan, arxiv silən, sübut ixrac edən hüquqlar ayrılır; analitik baxışı audit olunur.
- Toplamada məqsəd və müddət siyasətdə yazılır, artıq məzmun (parol, token, tam sorğu) çıxarılır.
- Psevdonimləşdirmə; sadə heş anonimlik vermir, HMAC lüğət hücumunu çətinləşdirir.
- Log məzmunu etibarsızdır: hücumçu saxta sətir yaza bilər, strukturlaşdırılmış qeyd və qaçışlama lazımdır.
- UEBA balı avtomatik intizam qərarı deyil.
:::
