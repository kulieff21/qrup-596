+++
title = "Girişə nəzarət prinsipləri və modelləri; identifikasiya və giriş idarəetməsi (IAM)"
unit = "uzun"
order = 3
summary = "Tam mühazirə: giriş qərarının qurulması, AAA, autentifikasiya faktorları, FIDO2, parol siyasəti, DAC/MAC/RBAC/ABAC, formal modellər, IAM həyat dövrü, SSO, LDAP, SAML, Kerberos, OAuth/OIDC, PAM, sıfır etimad, kimlik hücumları və PDCA."
updated = 2026-11-09

[[source]]
title = "Mühazirə 3: Girişə nəzarət prinsipləri və modelləri; identifikasiya və giriş idarəetməsi (IAM)"
note = "Elmar Cabbarov, 2026–2027"
+++

Girişə nəzarət dörd sualın cavabıdır: sistemə kim girir, onun kim olduğunu necə yoxlayırıq, içəridə nəyə icazəsi var və etdiklərini kim yazır. Mövzunun məqsədi universitet informasiya sistemində kimin hansı resursa, hansı əməliyyat üçün və hansı şərtlərlə daxil olduğunu əsaslandıra bilməkdir. Mövzu giriş siyasətindən başlayır, autentifikasiya və modellərdən keçir, IAM, federasiya protokolları və hücumlarla bitir. Universitetin adları, hesabları və rəqəmləri şərti tədris nümunəsidir.

:::note Bu mövzudan sonra bacarmalısan
- İdentifikasiya, autentifikasiya, avtorizasiya və hesabatlılığı ayırmağı.
- DAC, MAC, RBAC və ABAC modellərindən situasiyaya uyğun olanı seçməyi.
- Bell–LaPadula və Biba qaydalarını tətbiq etməyi; MFA və parol siyasətini müasir tələblərlə qurmağı.
- Hesabın yaradılmasından bağlanmasına qədər yoxlanılan IAM prosesi qurmağı.
:::

## Təhlükəsizlik siyasətindən giriş qərarına

### Model nəyi təsvir edir

Girişə nəzarət (access control) subyektin obyekt üzərində əməliyyat aparmasına icazə verən və ya onu rədd edən qaydalar və mexanizmlərdir.

- **Subyekt** sorğunu başladan aktiv tərəfdir: insanın adından işləyən proses, xidmət hesabı və ya avtomatlaşdırılmış agent.
- **Obyekt** qorunan resursdur: tələbə bazasındakı sətir, LMS kursu, fayl, API funksiyası, printer.
- **Əməliyyat**: oxuma, yazma, silmə, icra, təsdiq, paylaşma.

:::exam Giriş obyekti ≠ əlçatanlıq
"Giriş obyekti" (access object) anlayışı CIA-dakı əlçatanlıqla (availability) qarışdırılmamalıdır. Mühazirənin köhnə slaydındakı "əlçatanlığın həcmi" termini əslində giriş obyektidir.
:::

Üç səviyyə ayrılır:

| Səviyyə | Nədir | Nümunə |
| --- | --- | --- |
| Təhlükəsizlik siyasəti | Universitetin qəbul etdiyi məzmunlu tələb | Tələbə öz qiymətini görə bilər, dəyişə bilməz |
| Təhlükəsizlik modeli | Siyasətin dəqiq, təhlilə yararlı təsviri | İstifadəçi, kurs və əməliyyat arasındakı əlaqə |
| Mexanizm | Modelin proqramda və sistemdə icrası | LMS hər sorğuda əlaqəni yoxlayır |

Firewall-un bağlantını buraxması LMS daxilindəki qiymət sətirinə icazə demək deyil.

Yaxşı modelin xassələri:

- **Abstraktlıq**: proqramın hər detalını təkrarlamır, yalnız təhlükəsizlik üçün lazım olan əlaqələri saxlayır.
- **Sadəlik**: yoxlamanı və düzgün tətbiqi asanlaşdırır.
- **Adekvatlıq**: real risklər təsvirə daxildir. Model yalnız işçiləri nəzərə alırsa, tələbələrin, məzunların və podratçıların girişi izahsız qalır.
- Rahat interfeys ayrı meyardır; modelin riyazi sadəliyi ilə eyniləşdirilmir.

Formal təsvirdə sistemin vəziyyəti istifadəçilər, obyektlər, hüquqlar və aktiv sessiyalar çoxluğudur. Keçid hesabın yaradılması, rolun verilməsi, sənədin etiketinin dəyişdirilməsidir. Başlanğıc vəziyyət təhlükəsizdirsə və hər icazəli keçid qorunan xassəni saxlayırsa, xassə sonrakı vəziyyətlərdə də qalır. Bu yalnız modelin fərziyyələri daxilində doğrudur: proqram zəifliyi və ya modelə daxil edilməyən ehtiyat nüsxə kanalı sübutdan kənarda qala bilər.

### İstinad monitoru və giriş matrisi

İstinad monitoru (reference monitor), başqa adla giriş dispetçeri, subyektlə obyekt arasındakı sorğunu siyasətə görə yoxlayan abstrakt mexanizmdir. Üç tələbi var:

1. Hər qorunan müraciət ondan keçməlidir (yan keçmək mümkün olmamalıdır).
2. Subyekt onu dəyişdirə (saxtalaşdıra) bilməməlidir.
3. Düzgünlüyü yoxlanacaq qədər sadə (kiçik) olmalıdır.

Portalda menyudakı düyməni gizlətmək bu tələbi ödəmir: tələbə birbaşa API ünvanına sorğu göndərəndə server yenə icazəni yoxlamalıdır.

:::exam Dispetçer tələbi
Köhnə slaydda dispetçerin yoxlama aparması "qeyri-mümkün" yazılıb; düzgünü əksinədir: dispetçeri **yan keçmək** qeyri-mümkün olmalıdır.
:::

Giriş matrisi sətirlərdə subyektləri, sütunlarda obyektləri, xanalarda hüquqları göstərir (R oxuma, W yazma, X icra; boş xana açıq icazənin olmadığını bildirir).

| Subyekt | Qiymət jurnalı | Təqaüd siyahısı | Ehtiyat nüsxə skripti |
| --- | --- | --- | --- |
| Aysel, kurs üzrə məsul | R, W | Hüquq yoxdur | Hüquq yoxdur |
| Murad, maliyyə əməkdaşı | R | R, W | Hüquq yoxdur |
| backup-svc xidməti | R | R | X |
| Tələbə hesabı | Yalnız öz sətri üçün R | Yalnız öz sətri üçün R | Hüquq yoxdur |

Matrisin çox xanası boşdur, ona görə iki formada saxlanır:

- **ACL (access control list, sütun)**: hər obyekt üçün icazəli subyektlər və əməliyyatlar.
- **Səlahiyyət siyahısı (capability list, sətir)**: subyekt hansı obyektlərə nə edə bilər. Həqiqi capability mexanizmində hüququ təmsil edən istinad saxtalaşdırılmadan qorunur; istifadəçi profilində resurs adlarını yazmaq bu qorumanı yaratmır.

:::figure
src = "m03-1.png"
alt = "Giriş qərarının qurulması: subyektin sorğusu icra nöqtəsi PEP-ə gedir, PEP qərarı qərar nöqtəsi PDP-dən alır; PDP siyasəti PAP-dan, atributları PIP-dən götürür; icazəli əməliyyat obyektə çatır."
caption = "Şəkil 1. Giriş sorğusunun siyasətə və atributlara görə yoxlanması."
:::

### Qərarı məhdudlaşdıran prinsiplər

- **Minimal səlahiyyət (least privilege)**: iş üçün lazım olan ən az hüquq, lazım olan resurslarda və müddətdə. Kitabxana əməkdaşı borc qeydini yeniləməlidir, bütün tələbələrin maliyyə məlumatlarını ixrac etməməlidir.
- **Bilmək zərurəti (need-to-know)** məlumatın məzmununa aiddir: fakültə rəhbərinin yüksək vəzifəsi başqa fakültənin tibbi sənədlərini oxumaq üçün əsas deyil.
- **Vəzifələrin bölgüsü (separation of duties, SoD)** ziddiyyətli səlahiyyətləri ayırır: təqaüd ödənişini hazırlayan onu təkbaşına təsdiqləməməlidir.
  - **Statik** bölgü iki ziddiyyətli rolun eyni şəxsə verilməsini qadağan edir.
  - **Dinamik** bölgü hər iki rolu olan şəxsin eyni əməliyyatda həm hazırlayan, həm təsdiqləyən olmasına mane olur. Kiçik kafedrada çevikdir, amma əməliyyat tarixçəsinin düzgün yoxlanmasını tələb edir.

| Prinsip | Sistemdə tələb | Universitetdə yoxlama |
| --- | --- | --- |
| Susmaya görə rədd (default deny) | Açıq icazə yoxdursa sorğu rədd edilir | Rolsuz hesab qiymət API-sini aça bilmir |
| Tam vasitəçilik (complete mediation) | Hər qorunan əməliyyatda hüquq yoxlanır; keşdəki köhnə icazəyə güvənilmir | Kurs nömrəsini dəyişmək başqa jurnalı açmır |
| Minimal səlahiyyət | Hüquq işin sərhədini aşmır | Kitabxana hesabı tələbə bazasını dəyişmir |
| Vəzifələrin bölgüsü | Ziddiyyətli əməliyyatlar ayrılır | Ödənişi hazırlayan özü təsdiqləmir |
| Nasazlıqda bağlı qalma (fail-secure) | Qərar mexanizmi işləmirsə qorunan giriş açılmır | Siyasət xidməti dayananda ixrac rədd edilir |

Fail-secure yüksək əlçatanlığı ləğv etmir: ehtiyat siyasət xidməti, nəzarətli keş və fövqəladə prosedur qurula bilər; keşdəki qərarın müddəti və ləğv siqnalı məlum olmalıdır. Yanğında təxliyə qapısının açılması insan təhlükəsizliyinə yönəlmiş **fail-safe** davranışıdır (4-cü mövzu); rəqəmsal bazanın hamıya açılması ilə eyniləşdirilmir.

## İdentifikasiya, autentifikasiya, avtorizasiya və uçot

- **İdentifikasiya (identification)**: subyektin özünü hansı identifikatorla təqdim etməsi.
- **Autentifikasiya (authentication)**: iddianın autentifikator vasitəsilə yoxlanması.
- **Avtorizasiya (authorization)**: yoxlanmış subyektin konkret əməliyyata hüququnun müəyyən edilməsi.
- **Fəaliyyətin uçotu (accounting)**: istifadə və əməliyyatlar barədə qeydlər. Son üç funksiya birlikdə **AAA** adlanır.
- **Hesabatlılıq (accountability)**: qeydlərin və təşkilati məsuliyyətin köməyi ilə hərəkətin kimə aid olduğunu əsaslandırmaq imkanı.

| Mərhələ | Sual | LMS nümunəsi |
| --- | --- | --- |
| İdentifikasiya | Hansı hesabı təqdim edirsən? | İstifadəçi aysel@unec.example yazır |
| Autentifikasiya | Həmin hesabı idarə etdiyini necə sübut edirsən? | FIDO2 açarı sorğunu imzalayır |
| Avtorizasiya | Bu jurnal üzərində nə edə bilərsən? | Yalnız təyin olunduğu kursa bal yaza bilir |
| Fəaliyyətin uçotu | Hansı əməliyyat baş verdi? | Kim, hansı balı, nə vaxt dəyişdi, nəticə nə oldu |

:::exam Tələ: autentifikasiya ≠ avtorizasiya
Autentifikasiya kimliyi yoxlayır, avtorizasiya icazəni. Dekanlıq əməkdaşı düzgün parol və MFA ilə daxil olub (autentifikasiya uğurludur), amma başqa fakültənin tələbəsinin şəxsi işini aça bilirsə, bu avtorizasiya problemidir. READ, WRITE, EXECUTE autentifikasiya növləri deyil, giriş əməliyyatlarıdır, yəni avtorizasiyaya aiddir (köhnə slaydda səhv verilib).
:::

Autentifikasiya hesabın arxasında mütləq gözlənilən insanın oturduğunu sübut etmir: paylaşılan parol, oğurlanmış sessiya və açıq qalmış terminal bu əlaqəni zəiflədir. Kafedranın hamısı bir hesabdan istifadə edirsə, jurnal hadisəni göstərir, lakin şəxsi etibarlı ayırmır; buna görə fərdi hesab, ekran kilidi və sessiya qorunması uçotun keyfiyyətinə də təsir edir.

**İlkin şəxsiyyət yoxlaması (identity proofing)** autentifikasiyadan əvvəl gəlir: universitet qəbul sənədlərini və ya əmək müqaviləsini yoxlayıb şəxsi hesabla əlaqələndirir, sonra autentifikator bağlayır. Hesab səhv şəxsə bağlanıbsa, güclü MFA həmin səhv əlaqəni qoruyacaq. Eyni adlı iki tələbə ad-soyadla yox, daxili sabit identifikatorla fərqləndirilir; poçt ünvanı dəyişə bildiyi üçün əsas əlaqə yalnız ona bağlanmır.

**NIST SP 800-63-4** 2025-ci ilin iyulunda yekunlaşıb və SP 800-63-3 seriyasını əvəz edir. Üç ayrı təminat səviyyəsi var: **IAL** (şəxsiyyətin ilkin yoxlanması), **AAL** (autentifikasiya), **FAL** (federasiya). Yüksək AAL avtomatik yüksək şəxsiyyət yoxlaması demək deyil. Anonim kitabxana axtarışı ilə diplomun elektron təsdiqi üçün eyni səviyyə seçilmir; tələb riskə və yanlış girişin nəticəsinə görə əsaslandırılır.

### AAA şəbəkə girişində: RADIUS və TACACS+

- Yataqxana Wi-Fi şəbəkəsində giriş nöqtəsi autentifikasiya sorğusunu mərkəzi **RADIUS** xidmətinə göndərib qərarı ala bilər. Uçot qurulubsa, avadanlıq sessiyanın başlanması, aralıq vəziyyəti və bitməsi barədə uçot sorğularını RADIUS uçot serverinə göndərir, server qəbulu təsdiqləyir.
- Şəbəkə avadanlığının inzibati girişində **TACACS+** autentifikasiya, avtorizasiya və uçotu ayırmaq üçün işlədilir.
- Protokolun adını yazmaq təhlükəsiz kanal demək deyil: müştəri–server etimadı, sirrlər və nəqliyyat qoruması ayrıca yoxlanır. **Blast-RADIUS** (CVE-2024-3596) köhnə təhlükəsizlik fərziyyələrinə arxalanmağın riskini göstərir; reallaşdırmanın düzəlişləri və tövsiyə etdiyi qoruma parametrləri yoxlanmalıdır.

Uçot qeydi uğurlu girişlə məhdudlaşmır: rolun verilməsi, MFA vasitəsinin dəyişməsi, hesabın bərpası və rədd edilmiş ixrac da yazılır. **Audit** qeydlərin oxunmasından genişdir: siyasətə, prosesə və sübutlara meyarlar üzrə sistemli qiymət verilir (məsələn, hesabın bağlanma qaydası ilə faktiki bağlanma vaxtının müqayisəsi). Loqların analizi auditin yalnız bir hissəsidir.

## Autentifikasiya faktorları və fişinqə davamlı giriş

### Faktorların birləşdirilməsi

| Faktor | Nümunə | Zəif cəhət |
| --- | --- | --- |
| Bildiyin şey (knowledge) | Parol, PIN, gizli sual | Oğurlanır, təxmin edilir, fişinqlə alınır |
| Sahib olduğun şey (possession) | Telefon, smart kart, FIDO2 açarı (YubiKey) | İtir, oğurlanır; SMS kodu SIM-swap ilə ələ keçir |
| Özünə məxsus olan (inherence) | Barmaq izi, üz, iris, səs | Dəyişdirilə bilmir: sızsa, yeni barmaq izi olmur |
| Əlavə kontekst | Yer (IP, GPS), vaxt, davranış (yazı ritmi) | Faktor sayılmır, risk qiymətləndirməsi üçündür |

Cihazda (token, smart kart) saxlanan kriptoqrafik açar **sahiblik** faktorudur; onun rəqəmsal olması onu bilik faktoruna çevirmir.

**MFA (multi-factor authentication)** fərqli kateqoriyalardan ən azı iki faktor tələb edir. Parol və gizli sual iki addımdır, amma ikisi də "bildiyin şey"dir, deməli MFA deyil. Smart kart və PIN sahiblik və bilik faktorlarını birləşdirir. Yalnız seriya nömrəsini oxudan universitet kartı kriptoqrafik smart kartla eyni sayılmır.

| Üsul | Nəyi sübut edir | Məhdudiyyət |
| --- | --- | --- |
| Parol | Sirrə bələdlik | Fişinq, təkrar istifadə, oflayn təxmin |
| SMS ilə birdəfəlik kod | Telefon nömrəsi kanalına giriş | SIM dəyişdirmə, kodun real vaxtda ötürülməsi |
| TOTP tətbiqi | Vaxta bağlı sirri saxlayan vasitəyə giriş | Kod saxta sayta yazıla bilər |
| Push təsdiqi | Qeydiyyatlı cihazda razılıq | Bildiriş yorğunluğu, aldadıcı təsdiq |
| FIDO2 açarı / passkey | Domenlə bağlı açarın idarəsi | Son qurğu və bərpa prosesi ayrıca qorunmalıdır |

Güc sırası: SMS < autentifikator tətbiqi (TOTP) < push (rəqəm uyğunlaşdırması ilə) < FIDO2/WebAuthn açarları və passkey-lər. TOTP eyni sirr və vaxt intervalından birdəfəlik kod yaradır; kodun ömrünün qısalığı real vaxtda oğurlanmasını dayandırmır. Rəqəm uyğunlaşdırması təsadüfi təsdiqi azaldır, amma push-u FIDO2 səviyyəsinə çıxarmır. Üsul pilləsinə yox, konkret hücumda hansı sübutun qorunduğuna baxılır.

### Biometrik uyğunlaşdırma

Biometrik sistem barmaq izini və ya üzü əvvəl qeydiyyatdan keçmiş şablonla müqayisə edir; tam eynilik yox, oxşarlıq həddi axtarır.

| Əmsal | Mənası | Tip və təsir |
| --- | --- | --- |
| **FAR** (false acceptance rate) | Aid olmayan şəxsin səhvən qəbulu | II tip xəta, təhlükəsizlik üçün daha təhlükəli |
| **FRR** (false rejection rate) | İcazəli şəxsin səhvən rədd edilməsi | I tip xəta, istifadəçini əsəbiləşdirir |
| **CER / EER** | FAR = FRR olan iş nöqtəsi | Fərqli sistemləri müqayisə üçün: nə qədər aşağıdırsa, sistem bir o qədər dəqiqdir |

Hədd sərtləşdikdə FAR azalır, FRR artır. Kitabxana girişində aşağı FAR istənilirsə, yaş barmaq və zəif işıq daha çox qanuni istifadəçini dayandıra bilər. EER laboratoriya müqayisəsi üçündür; real yerləşdirmədə istifadəçi qrupu, sensor və saxta biometrik nümunənin aşkarlanması da yoxlanır. Başqa tədqiqatın əmsalı yataqxana girişinin gözlənilən nəticəsi sayılmır.

Biometrik əlamət parol kimi dəyişdirilmir və adətən sirr deyil. NIST yanaşmasında biometrika ayrıca autentifikator deyil, fiziki autentifikatorun aktivləşdirilməsi ilə işlədilir: telefonda barmaq izi passkey-in şəxsi açarını açır, serverə barmaq izi göndərilmir. Alternativ giriş və əlçatanlıq əvvəlcədən nəzərə alınır; sensor işləməyəndə yardım masası şəxsiyyəti yoxlamadan hesab açmamalıdır.

:::note Köhnə fikir
Mühazirədəki "biometrika bahadır, yalnız yüksək təhlükəsizlikli təşkilatlarda işlədilir" fikri köhnəlib: bu gün hər smartfonda barmaq izi və üz tanıma var.
:::

### FIDO2 və passkey necə işləyir

**FIDO2** veb autentifikasiyası üçün **WebAuthn**, xarici autentifikatorlarla əlaqə üçün **CTAP** texnologiyalarını birləşdirir. **Passkey** parolsuz girişdə işlənən açıq açarlı FIDO kimlik məlumatıdır.

1. **Qeydiyyat**: autentifikator xidmət üçün açar cütü yaradır; server açıq açarı və kimlik identifikatorunu saxlayır, şəxsi açar autentifikatorda qalır və serverə göndərilmir.
2. **Sorğu**: login.unec.example təsadüfi sorğu dəyəri (challenge) göndərir.
3. **İmza**: autentifikator istifadəçinin iştirakını (tələb olunursa yerli PIN və ya biometrika) təsdiqləyir, domenlə əlaqəli məlumatı və sorğunu imzalayır.
4. **Yoxlama**: server imzanı açıq açarla, challenge-in təzəliyini və mənşəyi yoxlayır. Saxta login-yardim.example həqiqi xidmət üçün imza ala bilmir: fişinqə davamlılıq **domen bağlanmasından** gəlir.

- **Sinxronlaşdırılan passkey** bir neçə cihazda işləyir; **cihazla məhdud açar** həmin autentifikatorda qalır. Bərpa, açarın çıxarılması və təminat səviyyələri eyni deyil.
- PIN və ya biometrik yoxlamanın tələbi siyasətdə göstərilməlidir: sadəcə açara toxunmaq hər quruluşda ikinci faktor deyil.
- İmtiyazlı hesablara daha sərt autentifikator tələbi qoyula, adi LMS girişində başqa risk seçimi edilə bilər.

:::warning Fişinqə davamlı ≠ hər şeyə davamlı
Fişinqə davamlı autentifikasiya oğurlanmış sessiyanı, yoluxmuş kompüteri və zəif hesab bərpasını aradan qaldırmır. Yardım masası yalnız telefon zənginə əsasən MFA vasitəsini dəyişirsə, hücumçu ən güclü mərhələni bərpa yolu ilə keçə bilər.
:::

## Parol siyasəti və parolların saxlanması

### NIST tələblərinin praktik mənası

| Məsələ | Köhnə yanaşma (mühazirədə də var) | NIST SP 800-63B-4 (2025) |
| --- | --- | --- |
| Uzunluq | Minimum 8 simvol | Yalnız parolla girişdə minimum **15**; MFA tərkibində minimum **8**; ən azı **64** simvolluq parolların qəbulu tövsiyə olunur |
| Tərkib | Böyük hərf, rəqəm, xüsusi simvol məcburiyyəti | Tələb edilməməlidir: insanlar "Parol1!" kimi proqnozlaşdırıla bilən parollar seçir |
| Dəyişmə | Hər 30–90 gündən bir məcburi | Müntəzəm məcburi dəyişmə yoxdur; yalnız sızma sübutu olanda |
| Qadağan siyahısı | — | Sızmış və tez işlənən parollar yoxlanır (məs. universitet adı ilə qurulmuş zəif parol rədd edilir) |
| Rahatlıq | — | Parol meneceri və avtomatik doldurma; yapışdırmaya (paste) icazə |
| Onlayn təxmin | — | Uğursuz cəhdlər məhdudlaşdırılır (hesab və mənbə üzrə risk nəzarəti) |

Məqsəd insanı qısa və proqnozlaşdırılan şablona məcbur etməməkdir. Qadağan siyahısının yoxlanması açıq parolun naməlum xidmətə göndərilməsi demək deyil: lokal siyahı və ya parolun məxfiliyini qoruyan üsul işlədilir. Giriş xətası hesabın mövcudluğunu açıqlamamalıdır, amma eyni mətn kifayət etmir: vaxt fərqi və bərpa səhifəsinin davranışı da hesabların sadalanmasına imkan verə bilər.

Sərt kilidlənmə hücumçuya tələbələri imtahandan əvvəl sistemdən kənarda saxlamaq imkanı verə bilər; artan gecikmə, mənbələr üzrə məhdudiyyət və təhlükəsiz bərpa birlikdə planlaşdırılır. Yataqxana Wi-Fi-də çox istifadəçi eyni xarici IP-dən çıxır, ona görə yalnız IP-yə görə bloklama qanuni istifadəçiləri də dayandırar. CAPTCHA köməkçi tədbirdir, oğurlanmış parolu etibarsız etmir.

### Salt, heş və oflayn hücum

Server parolu geri açılan şifrələmə ilə yox, parol üçün nəzərdə tutulmuş törətmə funksiyası ilə saxlamalıdır (Argon2, bcrypt, scrypt, PBKDF2).

1. Qeydiyyatda hər parol üçün təsadüfi, ayrıca **duz (salt)** yaradılır.
2. Funksiya parolu, duzu və xərc parametrlərini qəbul edib yoxlama dəyəri yaradır.
3. Bazada duz, parametrlər və nəticə saxlanır.
4. Girişdə daxil edilən parol həmin parametrlərlə hesablanıb müqayisə edilir.

Duz sirr deyil. Eyni parolu seçmiş iki tələbənin nəticələrinin fərqlənməsinə və hazır cədvəllərin təkrar istifadəsinin çətinləşməsinə xidmət edir. Duz zəif parolu gücləndirmir: bazanı oğurlayan hücumçu hər hesab üçün təxminləri yenə sınaya bilər. Yavaş və yaddaş tələb edən funksiya bu oflayn sınağın xərcini artırır; adi SHA-256 isə sürətli olduğu üçün parol saxlamaq üçün çatışmazdır.

**Argon2id** yaddaş və hesablama xərcini sazlamağa imkan verir. **bcrypt** geniş reallaşdırmalarda 72 bayt giriş məhdudiyyətinə malikdir; uzun parolu səssiz kəsmək olmaz. Funksiya seçimi, normativ tələblər və platforma dəstəyi birlikdə qiymətləndirilir; Argon2id seçmək avtomatik NIST uyğunluğu demək deyil. Nümunə argon2-cffi kitabxanasının API-sidir; parametrlər kitabxananın profilindəndir, istehsalatda serverin yükü ölçülməlidir:

```python
ph = PasswordHasher()
stored = ph.hash(password)           # parol kodda və jurnalda yazılmır
try:
    ph.verify(stored, entered_password)
except VerifyMismatchError:
    deny_login()
else:
    if ph.check_needs_rehash(stored):
        update_hash(ph.hash(entered_password))
    allow_login()
```

Texniki xəta (baza və ya kitabxana dayanması) icazəyə çevrilməməlidir; heş yalnız hesab uğurla yoxlanandan sonra yenilənir. **Pepper** bazadan ayrı qorunan əlavə sirrdir, bəzi arxitekturalarda faydalıdır, itirilməsi və dəyişdirilməsi üçün plan tələb edir. Ehtiyat nüsxədəki köhnə heşlər də həssasdır: əsas bazanı sərtləşdirib nüsxələri açıq saxlamaq oflayn hücumu asanlaşdırır.

## Diskresion və mandatlı girişə nəzarət

### Sahibin qərar verdiyi DAC

**Diskresion girişə nəzarətdə (discretionary access control, DAC)** resursun sahibi çərçivə daxilində hüquq verir və geri götürür. Kafedra əməkdaşı yaratdığı sənədi həmkarına paylaşır; əməliyyat sistemi sahiblik və ACL mexanizmləri ilə icra edir. Subyekt və obyekt sabit identifikatorla tanınmalıdır ki, adın dəyişməsi hüququ təsadüfən başqa hesaba keçirməsin.

Linux-da faylda r, w, x oxuma, yazma, icra deməkdir. Qovluqda fərqlənir: r adları siyahılamaq, x qovluqdan keçmək və məlum ada müraciət etmək, w digər şərtlərlə birlikdə qeydləri dəyişmək. Faylı silmək çox vaxt faylın öz yazma hüququndan yox, qovluğun hüquqlarından asılıdır. Laboratoriya nümunəsi (sahib sənəd üçün yazır, qrup oxuyur, digərləri qapalıdır):

```bash
chgrp kafedra /srv/kafedra/cedvel.txt
chmod 640 /srv/kafedra/cedvel.txt
ls -l /srv/kafedra/cedvel.txt
getfacl /srv/kafedra/cedvel.txt
```

Əlavə ACL qeydləri və ACL maskası varsa, effektiv hüquq yalnız üç rəqəmlə izah olunmaya bilər; üst qovluqlardan keçid hüququ da lazımdır, proses başqa imtiyazlarla işləyirsə, faktiki giriş fərqlənə bilər. DAC-ın zəifliyi: sahib səhvən hamıya aça bilər; oxuma icazəsi olan şəxs məzmunu başqa yerə köçürə bilər.

### Mərkəzi siyasətin tətbiq etdiyi MAC

**Mandatlı girişə nəzarətdə (mandatory access control, MAC)** resurs sahibi mərkəzi siyasəti zəiflədə bilmir. Klassik çoxsəviyyəli formada obyektin məxfilik etiketi ilə subyektin buraxılış və cari işləmə səviyyəsi müqayisə olunur. Məhdud tədqiqat sənədlərini paylaşma düyməsi ilə hamıya açmağın qarşısını alır.

- MAC xətti səviyyələrlə məhdudlaşmır: **SELinux** tip əsaslı siyasətlərdən, **AppArmor** tətbiq profillərindən istifadə edir. LMS prosesi ələ keçirilsə də, düzgün siyasət onun ehtiyat nüsxə açarlarını oxumasını dayandıra bilər. Tətbiqin daxilində başqa tələbənin qiymətini görmək səhvini isə düzəltmir.
- DAC və MAC birlikdə işləyə bilər: birinin icazəsi digərinin qadağasını aradan qaldırmır.
- MAC tam statik deyil; etiket və siyasət dəyişiklikləri nəzarətli keçidlər olmalıdır. Çətinlik: düzgün etiketləmə, istisnalar, əməliyyat yükü (sərt və idarəsi çətindir). Rəddi aradan qaldırmaq üçün siyasəti söndürmək qorumanı ləğv edir.

| Vəziyyət | DAC baxışı | MAC baxışı |
| --- | --- | --- |
| Sahib həmkarına oxuma verir | ACL dəyişməsi giriş verə bilər | Mərkəzi etiket qaydası da ödənməlidir |
| Sahib sənədi hamıya açır | Sistem icazə verə bilər | Siyasət aşağı səviyyəyə açmanı rədd edə bilər |
| LMS prosesi başqa qovluğa gedir | Proses hesabının hüququ yoxlanır | Tətbiqin tipi və ya profili də yoxlanır |
| Etiket səhv seçilib | Etiket əsas qərar deyil | Yanlış etiket yanlış girişə səbəb olur |

## Rol, atribut və qayda əsasında avtorizasiya

### RBAC və sessiyada aktiv rollar

**Rol əsaslı girişə nəzarət (role-based access control, RBAC)** hüquqları şəxslərə yox, iş funksiyalarına bağlayır. Rol təşkilati funksiyadır, icazə obyekt və əməliyyat cütüdür; rolun adı özlüyündə qeyri-məhdud hüquq demək deyil.

Formal işarələmə: **U** istifadəçilər, **R** rollar, **P** icazələr, **SE** sessiyalar. **UA** (istifadəçi–rol) və **PA** (rol–icazə) təyinatları **çoxun çoxadır** (birin çoxa deyil, köhnə slaydda səhv yazılıb): istifadəçinin bir neçə rolu, rolun çox istifadəçisi, icazənin bir neçə rolu ola bilər. **RH** rol iyerarxiyasıdır. Sessiyada istifadəçi ona təyin edilmiş rolların altçoxluğunu aktivləşdirir.

- Nümunə: Nigar həm tədqiqatçı, həm kafedra katibidir; adi tədqiqat sessiyasında katibin təsdiq hüququnu aktivləşdirməyə ehtiyac yoxdur. Bütün rolları avtomatik birləşdirmək minimal səlahiyyətə uyğun olmaya bilər.
- İyerarxiyada böyük vəzifə aşağı rolların icazələrini miras alması məcburi deyil: rektorun tələbənin tibbi sənədini dəyişməsi iyerarxiyadan çıxan düzgün nəticə deyil.
- Üstünlük: kadr dəyişikliyi asandır (gedən roldan çıxarılır, yeni əməkdaş daxil edilir). Rol anlayışı PostgreSQL və bəzi OS mexanizmlərində də var. Active Directory qrupu vasitə ola bilər, lakin çox qrup düzgün rol layihəsinin sübutu deyil.
- Çətinlik: **rol çoxalması (role explosion)**: hər fakültə, kurs, tarix və cihaz üçün ayrı rol. İstisnalar birbaşa istifadəçiyə verildikcə roldan çıxarma bütün hüquqları silmir. Rolun sahibi, icazələri, uyğunluq şərti və baxış müddəti sənədləşdirilir.

### ABAC və siyasət arxitekturası

**Atribut əsaslı girişə nəzarətdə (attribute-based access control, ABAC)** qərar subyektin, obyektin, əməliyyatın və mühitin atributlarından hesablanır: kafedra və status, kursun məxfilik səviyyəsi, cihazın idarə olunması, vaxt. Rol da atributlardan biri ola bilər; RBAC və ABAC mütləq alternativ deyil.

| Funksiya | Ad | Nümunə |
| --- | --- | --- |
| Siyasətin idarə olunduğu nöqtə | **PAP** | Siyasət saxlanılır |
| Qərarın hesablandığı nöqtə | **PDP** | Atributlarla qərar çıxarır |
| Qərarın icra olunduğu nöqtə | **PEP** | LMS API-si |
| Atribut mənbəyi | **PIP** | Dərs yükü sistemi (kurs əlaqəsi), cihaz idarəetməsi (cihaz vəziyyəti) |

Bunlar məntiqi funksiyalardır, hər biri üçün ayrı server lazım deyil. Şərti qiymət dəyişmə siyasəti (konkret məhsul konfiqurasiyası deyil):

```text
permit = user.status == "active" and "course-editor" in user.roles
     and resource.course in user.assigned_courses
     and action == "grade.update"
     and environment.exam_window_open and device.managed
```

Atributlardan biri çatışmırsa, qorunan əməliyyat üçün icazə çıxarılmır. Aysel yalnız təyin olunan iki kursun jurnalını dəyişir; imtahan pəncərəsi bağlananda rol qalsa da əməliyyat rədd olunur. Cihaz vəziyyəti istifadəçinin göndərdiyi sərbəst JSON sahəsindən götürülə bilməz, əks halda hücumçu managed=true yazıb siyasəti keçər.

**Atributun təzəliyi** qərarın hissəsidir: işdən çıxan əməkdaş gecə yenilənən kataloqda gün ərzində aktiv görünə bilər. Hüquq dəyişməsi siqnalı, keş müddəti və mənbələr arasında ziddiyyətin həlli əvvəlcədən müəyyən edilir; qayda birləşdirmə üsulu (məs. rəddin üstünlüyü) ayrıca seçilib yoxlanır.

:::example RBAC və ABAC eyni tələbdə
"Müəllim yalnız öz dərs dediyi qrupların qiymətlərini, yalnız imtahan sessiyası ərzində və universitetin idarə olunan kompüterindən dəyişə bilər." RBAC ilə yalnız "müəllim" rolu verilir, qalan şərtlər çətin ifadə olunur. ABAC hamısını bir siyasətdə yazır: vəzifə=müəllim ∧ qrup∈dərs_dediyi_qruplar ∧ tarix∈sessiya ∧ cihaz=idarə olunan.
:::

### Qayda əsaslı nəzarət

**Qayda əsaslı nəzarət (rule-based access control)** vaxt, mənbə, protokol və başqa şərtlər üzrə əvvəlcədən yazılmış qaydalarla qərar verir (hamıya eyni tətbiq olunan qaydalar): firewall ACL-i, "iş saatından kənar inzibati giriş qadağandır". ABAC da qaydalarla işləyə bilər, ona görə sərhəd həmişə sərt deyil; əsas fərq qərarın hansı məlumatdan və məntiqdən çıxmasıdır. Zəif cəhət: fərdi istisnalar çətindir.

| Model | Qərarın əsası | Nümunə | Əsas uğursuzluq |
| --- | --- | --- | --- |
| DAC | Sahibin verdiyi hüquq | Kafedra sənədinin paylaşılması (Windows/Linux fayl icazələri, Google Drive "paylaş") | Səhv paylaşma |
| MAC | Mərkəzi məcburi siyasət | Məhdud tədqiqat sənədi etiketi; hərbi sistemlər, SELinux, AppArmor | Yanlış etiket, sərt istisnalar |
| RBAC | İş funksiyasının rolu | Kitabxanaçıya borc qeydini yeniləmək; AD qrupları, ERP | Rol çoxalması, hüquq yığılması |
| ABAC | Etibarlı atributlar | Öz kursu, açıq sessiya, idarə olunan cihaz; bulud IAM, Zero Trust | Köhnə və ya saxta atribut |
| Qayda əsaslı | Şərtlər və qayda sırası | İdarəetmə şəbəkəsindən giriş; firewall ACL | Geniş istisna, səhv sıra |

## Məxfilik və tamlığın formal modelləri

### Bell–LaPadula və informasiya axını

**Bell–LaPadula (BLP)** məxfiliyi qoruyan formal modeldir: yüksək məxfilikli məlumat icazəsiz aşağı səviyyəyə axmamalıdır. İlk hesabatlar **1973**-də təqdim olunub, yekun təsvir **1975**-də dərc edilib (1975 yox, 1973 ilk təqdimatdır). Model tamlıq və əlçatanlıq barədə təminat vermir. Səviyyələr: Açıq < Məxfi < Çox məxfi.

| Xassə | Qayda | Məna |
| --- | --- | --- |
| Sadə təhlükəsizlik (ss) | **No read up** | Öz səviyyəndən yuxarını oxuya bilməzsən |
| Ulduz (\*) | **No write down** | Öz səviyyəndən aşağı obyektə yaza bilməzsən; yoxsa "məxfi" istifadəçi sirri "açıq" fayla köçürərdi |
| Diskresion (ds) | Giriş matrisi | Matris də uyğun icazə verməlidir |

:::exam Ulduz qaydasının düzgün oxunuşu
"Subyekt məxfi olmayan məlumatdan yaza bilməz" yanlışdır; düzgünü: subyekt özündən aşağı səviyyəli obyektə yaza bilməz.
:::

Nümunə: məxfi səviyyədə işləyən tədqiqatçı çox məxfi layihəni oxuya bilməz, məxfi hesabatı uyğun ACL olduqda oxuya bilər, hesabatdan hissəni açıq elana yaza bilməz. Yuxarıya yalnız əlavə edən (geri oxumayan) əməliyyat mümkün ola bilər; oxuma-yazma birlikdə olan redaktədə hər iki qayda ödənməlidir.

- **Təhlükəsizlik qəfəsi (security lattice)**: səviyyə kateqoriyalar çoxluğu ilə birlikdədir; subyektin dərəcəsi kifayət etməli və bütün lazım olan kateqoriyaları əhatə etməlidir. "Məxfi, layihə-A" buraxılışı "Məxfi, layihə-B" sənədinə giriş vermir (bilməyin zərurəti).
- Səviyyənin aşağı salınması adi istifadəçinin əməliyyatı deyil; ayrıca səlahiyyətli yoxlama və məxfiliyin götürülməsi proseduru (etibarlı keçid) qurulur. Səviyyə istənilən anda dəyişsə, oxunmuş sirri aşağıya yazmaq üçün yol açılar.
- **Gizli kanal (covert channel)**: nəzərdə tutulmayan müşahidə olunan davranışla (resurs məşğulluğu, cavab vaxtı) bit ötürmə. Modeldən zərərli proqramın heç vaxt məlumat oğurlaya bilməyəcəyi çıxmır; ekran fotosu, yanlış etiketlənmiş nüsxə və kompromitasiya olunmuş etibarlı komponent də risklərdir. "BLP-yə uyğun sistemdə virus məlumat oğurlaya bilməz" iddiası şişirdilib.

### Biba və etibarsız məlumatın təsiri

**Biba (1977)** tamlığa yönəlir: aşağı etibarlı mənbə yüksək etibarlı məlumatı pozmamalıdır. Sərt variant: **no read down** və **no write up**. Biba məxfilik yox, tamlıq modelidir; BLP-nin güzgü əksidir. Məxfilik və tamlıq səviyyələri ayrı xassələrdir.

Nümunə: rəsmi qiymət bazası yüksək tamlıqdadır, tələbənin yüklədiyi cədvəl aşağı. Yüksək etibarlı xidmət cədvəli yoxlamadan oxuyub bazaya tətbiq edərsə, etibarsız giriş rəsmi nəticəyə təsir edir. Real sistem bunu yoxlama və təsdiq edən etibarlı çevirmə ilə həll edir; sərt qaydanı keçidsiz bütün iş axınına tətbiq etmək məlumat qəbulunu çətinləşdirər. Aşağı tamlıqlı proses yüksək tamlıqlı prosesi öz adından təhlükəli işə məcbur etməməlidir.

**Windows Mandatory Integrity Control** aşağı tamlıqlı prosesin yuxarı səviyyəli obyektə yazmasını məhdudlaşdıran əlaqəli ideyadan istifadə edir (brauzer aşağı səviyyədə işləyib sistem fayllarına yaza bilmir); bu, Biba qaydalarının tam reallaşdırılması deyil.

| Orta səviyyəli subyektin əməliyyatı | Bell–LaPadula | Sərt Biba |
| --- | --- | --- |
| Yuxarı səviyyəni oxumaq | Qadağandır | Mümkündür |
| Aşağı səviyyəni oxumaq | Mümkündür | Qadağandır |
| Yuxarı səviyyəyə yalnız yazmaq | Mümkündür | Qadağandır |
| Aşağı səviyyəyə yalnız yazmaq | Qadağandır | Mümkündür |
| Eyni səviyyədə oxumaq və yazmaq | Digər icazələr varsa mümkündür | Digər icazələr varsa mümkündür |

:::figure
src = "m03-2.png"
alt = "Solda Bell–LaPadula: məxfi subyekt Açıq səviyyədən oxuya, Çox məxfi səviyyəyə yaza bilər; sağda sərt Biba: orta tamlıqlı subyekt yüksək tamlıqdan oxuya, aşağı tamlığa yaza bilər."
caption = "Şəkil 2. Məxfilik və tamlıq qaydalarının orta səviyyəli subyekt üçün müqayisəsi."
:::

:::tip Yadda saxla
BLP sirrin aşağı **sızmasını** önləyir (yuxarı oxuma yox, aşağı yazma yox). Biba etibarsızın yuxarı **çirkləndirməsini** önləyir (aşağı oxuma yox, yuxarı yazma yox). Biba BLP-nin güzgü əksidir.
:::

### HRU və hüququn sızması problemi

**Harrison–Ruzzo–Ullman (HRU)** modelinin 1976-cı il məqaləsi giriş matrisinin dinamik dəyişməsini araşdırır: subyekt və obyekt yaradan, hüquq əlavə edən və silən əmrlər. Təhlükəsizlik sualı (**safety problemi**, hüququn sızması): verilmiş başlanğıc vəziyyətdən əmrlər ardıcıllığı ilə müəyyən hüquq əvvəl olmadığı xanaya keçə bilərmi? HRU yalnız məxfilik etiketi modeli kimi təqdim edilmir.

Nümunə: kafedra sənədinin sahibi paylaşma hüququnu assistentə verir, assistent başqa hesaba ötürür. Son hesabın ilkin siyahıda olmaması təhlükəsizliyə zəmanət deyil; keçidlər ardıcıllığına baxılır. Ümumi HRU sistemləri üçün təhlükəsizliyin qərarlaşdırılması **həllolunmazdır**. Bu, praktik sistemlərin yoxlanmasının mümkünsüzlüyü demək deyil: məhdud qaydalar, qadağan edilmiş ötürmə və konkret vəziyyətlərin təhlili ilə yoxlanılan sərhəd qurulur.

## Əməliyyatın düzgünlüyü və maraq toqquşması

### Clark–Wilson modeli

**Clark–Wilson** kommersiya iş axınlarında tamlığı düzgün əməliyyatlarla qoruyur (bank əməliyyatlarının məntiqi): istifadəçi məlumatı birbaşa dəyişmir, yalnız sertifikatlaşdırılmış proqramlarla; vəzifələr bölünür, hər əməliyyat audit olunur.

| Anlayış | Məna | Nümunə |
| --- | --- | --- |
| **CDI** (constrained data items) | Qaydalı dəyişən qorunan məlumat | Rəsmi bal, təqaüd ödənişi |
| **UDI** | Məhdudlaşdırılmayan, yoxlanmamış giriş | Tələbənin müraciət faylı |
| **TP** (transformation procedures) | Təsdiqlənmiş çevirmə proseduru | Əsas və təsdiqlə bal düzəlişi |
| **IVP** (integrity verification procedure) | Tamlığı yoxlama proseduru | Ödəniş cəmi ilə uçot qalığının uyğunluğu |
| Vəzifələrin bölgüsü | Səlahiyyətlərin ayrılması | Tərtib edən və təsdiqləyən ayrı şəxslərdir |

İstifadəçi, prosedur və məlumat arasında icazəli əlaqələr qurulur. Qiymət dəyişikliyi funksiyası (TP) balın icazəli intervalda olmasını, kursun uyğunluğunu, dəyişmə əsasını və təsdiqi yoxlayır. Bazaya birbaşa UPDATE hüququ bu yoxlamaları keçirsə, tətbiqdəki düzgün axın kifayət etmir: baza imtiyazları da sərhədi saxlamalıdır. Təsdiqlənmiş prosedurun özü səhv ola bilər: sınaq, uyğun məlumata bağlama, audit, təsdiqləyənlə istifadəçinin ayrılması. Yarımçıq tranzaksiya (məbləğ çıxılıb, tələbə hesabına yazılmayıb) biznes tamlığı pozuntusudur.

### Brewer–Nash modeli

**Brewer–Nash (Çin səddi, Chinese Wall)** əvvəlki girişlərdən asılı dinamik maraq toqquşmasını məhdudlaşdırır. Məlumat təşkilatlara aid dəstlərə, rəqib təşkilatlar maraq toqquşması siniflərinə bölünür. Şəxs bir şirkətin məxfi məlumatını açandan sonra eyni sinifdəki rəqibin məlumatına giriş məhdudlaşır; fərqli sinifdəki məlumatlara giriş qala bilər. İcazə keçmiş hərəkətlərdən asılıdır.

- Nümunə: rəqib müəssisələr üçün məxfi layihə aparan tədqiqat məsləhətçisi (və ya iki rəqib şirkətin tenderində ekspert müəllim) birinin sənədini açandan sonra digərininkinə giriş hüququnu itirir.
- Model bütün təklifləri müqayisə etməli olan adi tender qiymətləndirməsinə kor-koranə tətbiq edilməməlidir; əks halda qayda işi mümkünsüz edər.
- Yalnız oxuma məhdudlaşdırılmır: bir müştəridən oxunan sirrin başqasının yazıla bilən sahəsinə daşınması da bağlanır (yazma qaydaları). Şəxsləndirmədən təmizlənmiş açıq məlumat ayrıca idarə olunur.
- Giriş tarixçəsi silinərsə və ya şəxs ikinci hesab açarsa, dinamik sərhəd pozulur; kimliklərin əlaqələndirilməsi vacibdir.

:::note Köhnə slaydlarla fərq
Konspektdə qeyd olunan düzəlişlər: giriş obyekti əlçatanlıq deyil; BLP ilk dəfə 1973-də təqdim olunub; ulduz qaydası "özündən aşağı obyektə yazmaq" kimi oxunur; BLP virusdan qorumur (gizli kanallar qalır); Biba tamlıq modelidir; RBAC əlaqələri çoxun çoxadır (UA, PA, RH); istinad monitorunu yan keçmək qeyri-mümkün olmalıdır; cihazda saxlanan açar "sahib olduğun şey"dir; audit logların analizindən genişdir; 95/46/EC direktivi 2018-dən GDPR ilə əvəz olunub.
:::

## IAM həyat dövrü və hüquqların yoxlanması

### Gələn, vəzifəsi dəyişən və gedən istifadəçi

**IAM (identity and access management)** hesabları, autentifikatorları və hüquqları təşkilati hadisələrlə əlaqələndirən proseslər və texnologiyalardır: istifadəçinin işə girdiyi gündən çıxdığı günə qədər. Başlanğıc mənbə etibarlı olmalıdır (əməkdaş üçün kadr sistemi, tələbə üçün qeydiyyat sistemi). Bir şəxs həm əməkdaş, həm magistrant ola bilər: biri bitəndə digərinin hüququ təsadüfən silinməməli, bitənin hüquqları da saxlanmamalıdır.

- **Joiner (gələn)**: şəxs yoxlanır, sabit identifikator yaradılır, rol təsdiqlənir, autentifikator təhlükəsiz bağlanır, minimum hüquq verilir. Hesab açmaq hər sistemdə hesabın yarandığı demək deyil: LMS, kitabxana və poçta hüquqların çatdırılması (**provisioning**) ayrıca nəticə yoxlaması tələb edir; xəta zamanı təkrar cəhd ikinci hesab yaratmamalıdır.
- **Mover (keçən)**: köhnə və tələb olunan hüquqların fərqi hesablanır, köhnələr götürülür, yenilər verilir. Unudulsa, **hüquq yığılması (privilege creep)** yaranır. Köhnə işin təhvili üçün qısa keçid lazımdırsa, istisnanın sahibi və bitmə vaxtı yazılır.
- **Leaver (gedən)**: qüvvəyə minmə anında giriş dayandırılır (hesab, VPN, kart, aktiv sessiyalar, refresh token-lər, API açarları, üçüncü tərəf xidmətləri). Hesabı silmək ilk addım olmaya bilər: sənəd sahibliyi, audit əlaqələri və saxlama öhdəlikləri qorunur, giriş bloklanır. Lokal tətbiq kataloqla gec sinxronlaşırsa, mərkəzi bloklama bütün girişi dərhal kəsmir.

| Hadisə | Əməliyyat | Yoxlanılan nəticə |
| --- | --- | --- |
| Joiner | Təsdiqlənmiş rolu vermək | LMS və kitabxanada faktiki minimum hüquq var |
| Mover | Köhnə hüquqları götürmək | Birbaşa və miras hüquqların fərqi yoxlanıb |
| Leaver | Girişi və sessiyaları bağlamaq | Bütün əlaqəli sistemlərdə giriş sınağı rədd edilir |
| Müvəqqəti giriş | Bitmə vaxtı təyin etmək | Vaxt bitəndə hüquq həqiqətən silinib |
| Bərpa | Şəxsi yenidən yoxlamaq | Köhnə autentifikator və sessiyalar idarə olunub |

:::figure
src = "m03-3.png"
alt = "IAM həyat dövrü: qeydiyyat (şəxs yoxlanır), hüquq verilməsi (minimum səlahiyyət), dövri yoxlama (ehtiyac təsdiqlənir), girişin bağlanması (sessiyalar ləğv edilir); status dəyişəndə köhnə hüquqlar çıxarılıb hüquq verilməsinə qayıdılır."
caption = "Şəkil 3. Kimlik hadisəsindən hüququn verilməsinə, yoxlanmasına və ləğvinə qədər həyat dövrü."
:::

### Hüquqların dövri nəzərdən keçirilməsi

**Access review**: resurs sahibi mövcud hüquqları iş ehtiyacı ilə müqayisə edib saxlayır və ya ləğv edir. Baxış birbaşa təyinatları, iç-içə qrupları, rol iyerarxiyasını, paylaşma keçidlərini və tətbiq daxilində verilmiş hüquqları əhatə etməlidir (kafedra müdiri yalnız qrupu təsdiqləyib qrupun maliyyə ixracına çıxışını görmürsə, sübut zəifdir). Tezlik riskə görə seçilir; şərti universitet siyasəti (standartın tələbi deyil): imtiyazlı hüquqlara **hər ay**, digərlərinə **hər semestr**. Qərar verən hesabın sahibini, hüququn əsasını, son istifadəni və ziddiyyətli rolları görməlidir; son istifadə köməkçidir, nadir fövqəladə hüququn istifadə edilməməsi lazımsızlıq demək deyil.

Hesablama nümunəsi: 120 təyinatdan 18-i ləğv edilməli sayılıb, icra təsdiqində 12-si götürülüb; tamamlanma 12 / 18 ≈ **66,7 %**. Təsdiq düyməsi ilə faktiki silinmə ayrıdır; qalanlar üçün məsul şəxs və müddət təyin edilir. Baxışın faydası ləğv sayı ilə yox, artıq hüquqların vaxtında aradan qaldırılması ilə ölçülür.

**Xidmət hesabları** insan hesablarından fərqli idarə olunur: sahib, məqsəd və resurslar məlum olmalıdır. Şəxsi əməkdaş hesabı gecə inteqrasiya tapşırığında işlədilmir. Məhdud, mümkünsə qısaömürlü kimlik məlumatı seçilir; sirrlər kod deposunda saxlanmır. Sahib işdən çıxanda xidmətin sahibliyi ötürülür, sirrlərə çıxış və dəyişmə ehtiyacı yenidən qiymətləndirilir.

## SSO, kataloq xidməti və SAML federasiyası

### Vahid girişin sərhədləri

**SSO (single sign-on)** bir autentifikasiyadan sonra bir neçə xidmətə təkrar sirr verməmək deyir; rahatdır, amma SSO hesabı oğurlansa hamısı açılır, ona görə MFA mütləqdir. **Federasiya** ayrı sistemlərin kimlik barədə razılaşdırılmış etimad münasibətidir (format, açar və təminat səviyyəsi razılaşdırılır); SSO bir təşkilat daxilində də olur. **IdP (identity provider)** autentifikasiyanı aparır (Entra ID, Google), **SP (service provider)** nəticəni şərtlə qəbul edir.

- login.unec.example ilə girən istifadəçi LMS və elektron kitabxanaya keçə bilər, amma bu bütün resurslara hüquq vermir: kitabxana aktiv tələbə statusunu, LMS kurs qeydiyyatını ayrıca yoxlayır. IdP-nin kimliyi təsdiqləməsi yerli avtorizasiya səhvini düzəltmir.
- Mərkəzi hesabın ələ keçirilməsi çox xidmətə təsir edir: IdP-yə MFA, inzibati ayrılıq və etibarlı bərpa lazımdır.
- SSO sessiyası ilə tətbiq sessiyası ayrıdır: IdP-də çıxış LMS sessiyasını həmişə bağlamır, hesab bloklananda da belədir. Vahid çıxış, sessiya müddətləri və ləğv bildirişlərinin qəbulu sınanır; IdP dayananda davranış əvvəlcədən müəyyən edilir.

### LDAP nə edir

**LDAP (Lightweight Directory Access Protocol)** kataloqdakı obyektləri (istifadəçi, qrup, təşkilati vahid) axtarmaq və idarə etmək üçündür. Bind ilə autentifikasiya da qura bilər, amma SSO və ya federasiya protokolu deyil. **Active Directory** LDAP ilə yanaşı Kerberos və başqa xidmətləri birləşdirən kataloq və domen infrastrukturudur.

- LDAP adətən **TCP 389**: bağlantıda **StartTLS** ilə qorunan kanal qurula bilər. **LDAPS** adətən **TCP 636**-da başlanğıcdan TLS işlədir. 636-ya qoşulmaq kifayət etmir: sertifikatın etibar zənciri və server adı yoxlanmalıdır; sadə bind ilə parol ötürülürsə, kanal düzgün qorunmalıdır.
- Nümunə (StartTLS məcburi, -W parolu soruşur): `ldapsearch -x -ZZ -H ldap://directory.unec.example -D 'uid=lib-svc,ou=services,dc=unec,dc=example' -W -b 'ou=people,dc=unec,dc=example' '(uid=aysel)' uid mail`
- Xidmət hesabına bütün atributlar lazım deyil: kitabxanaya aktivlik statusu və identifikator kifayətdirsə, tibbi və kadr atributları verilmir.
- İstifadəçi girişini filtrə birbaşa birləşdirmək **LDAP injection** riskidir; filtr qaçırma funksiyası işlədilir. TLS bu məntiq səhvini aradan qaldırmır.

### SAML cavabının yolu

**SAML 2.0** XML əsaslı federasiya standartıdır (korporativ veb).

1. **Sorğu**: istifadəçi LMS-ə gəlir; LMS autentifikasiya sorğusu yaradıb onu IdP-yə yönəldir.
2. **Təsdiq**: IdP istifadəçini yoxlayır, kimlik və şərtlər barədə təsdiq (assertion) yaradır.
3. **Çatdırılma**: imzalanmış cavab brauzer vasitəsilə LMS-in əvvəlcədən müəyyən edilmiş qəbul ünvanına çatır.
4. **Sessiya**: LMS yoxlamadan sonra öz sessiyasını yaradır.

Yoxlama XML-də adı oxumaq deyil: **imza**, gözlənilən **issuer**, **audience**, **destination** və **recipient**, vaxt sərhədləri, sorğu ilə əlaqə və təkrar istifadə riski yoxlanır. Kitabxana üçün verilmiş assertion LMS-də qəbul edilmir. Etibar açarları metadata ilə idarə olunur, açar dəyişməsi planlı olmalıdır. İmza məzmunun dəyişmədiyini və etibarlı mənbədən gəldiyini yoxlayır, **gizlətmir**: məxfilik üçün qorunan nəqliyyat və lazım olsa assertion şifrələməsi. Lazımsız çox atribut göndərmək fərdi məlumat toplanmasına səbəb olur. Təhlükəsiz XML emalı və sınanmış kitabxana lazımdır; imzanı bir düyündə yoxlayıb adı başqa, yoxlanmamış düyündən götürmək kimliyi dəyişə bilər.

## Kerberos autentifikasiyası addım-addım

**Kerberos** parolu hər xidmətə göndərmədən **bilet (ticket)** ilə autentifikasiya edir (Windows domenlərində; vaxt sinxronizasiyası vacibdir). **KDC (key distribution center)** iki funksiyanı yerinə yetirir: **AS** (autentifikasiya xidməti) və **TGS** (bilet verən xidmət). **Realm** idarəetmə sahəsi, **principal** istifadəçi və ya xidmət kimliyidir. Axın ümumidir: ilkin autentifikasiya sertifikatla da qurula bilər. **TGT** bilet verən xidmətə müraciət üçün biletdir, fayl serverinə giriş bileti deyil.

:::steps Kerberos: bilet ardıcıllığı
[[step]]
title = "AS-REQ"
body = "Müştəri KDC-dən ilkin bilet istəyir. Tipik yoxlamada istifadəçi açarı ilə qorunan məlumat (məsələn vaxt nişanı) təqdim olunur; parol şəbəkədə açıq göndərilmir."

[[step]]
title = "AS-REP"
body = "Cavabda TGT və müştəri–TGS sessiya açarı üçün qorunan məlumat gəlir. TGT TGS-in uzunmüddətli açarı ilə qorunduğu üçün müştəri onun içini aça bilmir."

[[step]]
title = "TGS-REQ"
body = "Fayl xidmətinə girmək üçün müştəri TGT-ni, xidmət adını və müştəri–TGS sessiya açarı ilə qorunan autentifikatoru göndərir."

[[step]]
title = "TGS-REP"
body = "TGS TGT və autentifikatoru yoxlayır; xidmət bileti və müştəri–xidmət sessiya açarı qaytarır. Bilet xidmətin açarı ilə qorunur."

[[step]]
title = "AP-REQ"
body = "Müştəri xidmət biletini və yeni autentifikatoru fayl serverinə təqdim edir; xidmət öz açarı ilə bileti aça və autentifikatoru yoxlaya bilir."

[[step]]
title = "AP-REP"
body = "Qarşılıqlı autentifikasiya tələb olunanda xidmət cavab verir. Bundan sonra faylın ACL-i və digər siyasətlər avtorizasiyanı müəyyən edir."
:::

:::figure
src = "m03-4.png"
alt = "Kerberos ardıcıllığı: müştəri AS-REQ ilə KDC-nin AS hissəsinə, AS-REP ilə TGT alır; TGS-REQ ilə TGT və autentifikator göndərir, TGS-REP ilə xidmət bileti alır; AP-REQ ilə fayl xidmətinə bilet və autentifikator göndərir, AP-REP ilə qarşılıqlı yoxlama gəlir."
caption = "Şəkil 4. Kerberos-da ilkin biletin, xidmət biletinin və xidmətə təqdimatın ardıcıllığı."
:::

- TGT hər xidmətə istənilən hüquq vermir: bilet kimliyi daşıyır, resursun hüquqları ayrıca tətbiq olunur. Təqaüd cədvəlinə uğurlu autentifikasiya faylın dəyişdirilməsinə icazə demək deyil.
- **Vaxt** təzəlik və təkrar təqdimetməyə (replay) qarşı yoxlamada işlədilir; saatların fərqi həddi aşarsa, qanuni giriş pozulur. Vaxt xidməti qorunur, xidmət adları və DNS düzgün qurulur; təkrar təqdimetmə keşi də lazımdır, yalnız vaxt replay-i tam həll etmir.
- Laboratoriya əmrləri (MIT Kerberos): `kinit aysel@UNEC.EXAMPLE`, `klist`, `kvno host/files.unec.example`, `kdestroy`. kdestroy yalnız lokal biletləri silir; başqa cihazdakı və artıq yaranmış tətbiq sessiyalarını ləğv etmir.
- KDC kompromitasiyası realm üçün ağırdır: domen nəzarətçiləri adi tətbiq serverləri ilə eyni inzibati riskə qoyulmur. Xidmət açarı zəif paroldan törənibsə, bilet oflayn təxmin hədəfidir; qısa bilet müddəti zəif sirri gücləndirmir. Hesabın bloklanması əvvəl verilmiş biletlərin hər xidmətdə dərhal rədd olunmasına zəmanət deyil.

## OAuth 2.0, OpenID Connect və tokenlərin yoxlanması

### Delegasiya autentifikasiyadan nə ilə fərqlənir

**OAuth 2.0** tətbiqə istifadəçinin parolunu vermədən məhdud resursa giriş səlahiyyəti ötürən **avtorizasiya** çərçivəsidir ("bu tətbiq təqviminizi oxusun?"). Dörd rol: resurs sahibi istifadəçi, müştəri tətbiqi, avtorizasiya serveri, resurs serveri. Dərs planlaşdırma tətbiqi təqvimi oxuya bilər; bu, poçtu silmək və ya kimliyi təsdiqləmək hüququ deyil.

- **Giriş token-i (access token)** resurs serverinə təqdim edilir; oxuna bilən JWT və ya qeyri-şəffaf dəyər ola bilər (OAuth hər token-in JWT olmasını tələb etmir).
- **Səlahiyyət sahəsi (scope)** girişin sərhədidir; server konkret obyektin həmin istifadəçiyə aid olduğunu yenə yoxlamalıdır (calendar.read başqalarının təqvimini oxumaq üçün əsas deyil).
- **OpenID Connect (OIDC)** OAuth üzərində **autentifikasiya** qatıdır: openid scope-u ilə **kimlik token-i (ID token)** müştəriyə autentifikasiya iddiaları verir. ID token müştəri üçün, access token resurs serveri üçündür; birini digərinin yerinə qəbul etmək etimad sərhədini pozur. JWT-nin üç hissəsini açıb oxumaq yoxlamaq deyil: imza, issuer, audience və vaxt yoxlanır.
- SAML XML əsaslıdır, korporativ veb üçün; OIDC JSON/JWT əsaslıdır, müasir veb və mobil üçün.

### Avtorizasiya kodu və PKCE axını

Mobil tətbiq üçün avtorizasiya kodu axını **PKCE** ilə. PKCE kodun tutulmasına qarşı müştərinin başlanğıcda yaratdığı sirrlə son mübadiləni əlaqələndirir; müştəri autentifikasiyasının bütün variantlarını əvəz etmir. Server tətbiqində müştəri autentifikasiyası da olur; mobil tətbiqdə koda qoyulmuş daimi sirr etibarlı məxfi sirr sayılmır.

:::steps Avtorizasiya kodu + PKCE
[[step]]
title = "Hazırlıq"
body = "Tətbiq təsadüfi `code_verifier`, ondan `code_challenge`, sessiyaya bağlı `state`, OIDC üçün `nonce` yaradır. PKCE-də S256 üsulu seçilir."

[[step]]
title = "Yönləndirmə"
body = "İstifadəçi brauzer axını ilə avtorizasiya serverinə yönəlir; sorğuda qeydiyyatlı `client_id`, dəqiq uyğunlaşdırılan `redirect_uri`, scope-lar və challenge var."

[[step]]
title = "Kod"
body = "Autentifikasiya və razılıqdan sonra server qısaömürlü, birdəfəlik avtorizasiya kodunu qeydiyyatlı ünvana qaytarır. Tətbiq cavabın öz sessiyasına aid olduğunu yoxlayır."

[[step]]
title = "Token sorğusu"
body = "Tətbiq kodu və `code_verifier` dəyərini token ünvanına göndərir; server challenge uyğunluğunu, kodun müştəriyə və ünvana bağlılığını yoxlayır."

[[step]]
title = "Token-lər"
body = "Access token, OIDC-də ID token, siyasət imkan verirsə yeniləmə token-i (refresh token) verilir. Tətbiq ID token-i qəbul etməzdən əvvəl bütün yoxlamaları aparır."

[[step]]
title = "API"
body = "API access token-i auditoriya, etibarlı mənbə, müddət və səlahiyyət üzrə yoxlayır, sonra obyekt səviyyəsində yerli avtorizasiya tətbiq edir."
:::

`state` cavabı sessiya ilə əlaqələndirir və sorğunun saxtalaşdırılması riskini azaldır; `nonce` autentifikasiya sorğusu ilə ID token arasındakı əlaqəni yoxlayır; PKCE kodu müştəriyə bağlayır: üçü ayrı funksiyadır. Yönləndirmə ünvanının geniş şablonla qəbulu və ya açıq yönləndiriciyə bağlanması kodun başqa ünvana çatmasına səbəb ola bilər. Etibarlı kitabxanada da qeydiyyat və konfiqurasiya düzgün olmalıdır.

| Mexanizm | Əsas məqsəd | Əsas artefakt | Ayrıca qalan məsələ |
| --- | --- | --- | --- |
| LDAP | Kataloq sorğusu və idarəsi | Kataloq qeydi, bind nəticəsi | Veb federasiya |
| Kerberos | Bilet əsaslı autentifikasiya | TGT və xidmət bileti | Resursun əməliyyat hüququ |
| SAML 2.0 | Federativ kimlik təsdiqi | XML assertion | Yerli tətbiq avtorizasiyası |
| OAuth 2.0 | Məhdud girişin delegasiyası | Access token | Öz-özlüyündə kimlik təsdiqi |
| OIDC | OAuth üzərində autentifikasiya | ID token | API-də obyekt hüququ |

### Sessiya və token oğurlanmasına qarşı tədbirlər

- **Bearer token**: təqdim edən ondan istifadə edə bilir; sahiblik sübutu yoxdursa, surəti oğurlamaq kifayətdir. TLS ötürməni qoruyur, yoluxmuş cihazı və tətbiqin token-i loga yazmasını dayandırmır.
- **Refresh token** daha uzunmüddətli giriş verir: məhdud saxlanır, uyğun ssenaridə rotasiya və təkrar istifadə aşkarlanması tətbiq edilir. **RFC 9700** OAuth təhlükəsizliyi üçün yaxşı təcrübələri toplayır.
- Brauzer sessiya cookie-si: **Secure**, **HttpOnly**, uyğun **SameSite**. HttpOnly JavaScript-in cookie-ni oxumasını məhdudlaşdırır, lakin XSS olan səhifənin istifadəçi adından sorğu aparmasını tam dayandırmır; CSRF qoruması ayrıca lazımdır. Token-i URL parametrinə və ya diaqnostika jurnalına yazmaq sızma yaradır.
- **Müddət bitməsi ≠ ləğv**: imzası düzgün, müddəti bitməmiş JWT-ni lokal yoxlayan API hesabın az əvvəl bağlandığını bilməyə bilər. Qısa müddət, introspeksiya və ya ləğv məlumatının yayılması tətbiqin tələbinə görə seçilir. Məzunun kitabxana hüququ dayananda refresh token-lər, hazır access token-lərin qəbul müddəti və lokal sessiyalar nəzərə alınır.

## İmtiyazlı giriş və sıfır etimad

### PAM ilə idarəçi hüququnun məhdudlaşdırılması

**PAM (privileged access management)** yüksək təsirli hüquqların kimə, nə vaxt və hansı əsasla verildiyini nəzarətdə saxlayır: adi poçt hesabı ilə domen administratoru hesabı ayrılır; daimi inzibati üzvlük əvəzinə ehtiyac anında, məhdud müddətə (**just-in-time, JIT**) hüquq verilir; admin hesabları seyfdə saxlanır, sessiyalar yazılır. Əhatə də məhdudlaşdırılır: kitabxana xidmətini yenidən başlatmaq bütün serverin kök hüququnu tələb etməyə bilər.

Şərti prosedur: administrator sifariş açır, xidmət sahibi məqsədi təsdiqləyir, güclü autentifikasiyadan sonra yalnız konkret serverə **30 dəqiqəlik** giriş verilir; PAM vaxtı və əməliyyatları yazır, müddət bitəndə hüququ götürür (30 dəq nümunədir, universal tələb deyil). Sessiya yazısı məxfi məlumat göstərə bildiyi üçün ona çıxış da məhdudlaşdırılır.

PAM yalnız parol seyfi deyil: müvəqqəti kimlik məlumatları, komanda məhdudiyyəti, təsdiq və audit birlikdə. Seyfin administratoru həm sirri götürüb, həm izlərini silə bilməməlidir. PAM özü yüksək dəyərli hədəfdir: ehtiyatı və idarəetmə kanalı qorunmalıdır.

**Fövqəladə hesab (break-glass account)** əsas federasiya işləməyəndə bərpa üçündür: sirri ayrıca qorunur, istifadəsi dərhal xəbərdarlıq yaradır və sonradan araşdırılır. Hər gün işlətmək və ya MFA-nı keçmək üçün paylaşmaq mexanizmin məqsədini pozur; bərpa sınağı aparılmayıbsa, böhranda işləyəcəyinə sübut yoxdur.

### Sıfır etimadın giriş qərarına təsiri

**Sıfır etimad (zero trust)** şəbəkədə yerləşməyə və ya aktivin universitetə məxsus olmasına görə avtomatik etimad verməyən yanaşmadır; anlayışlar **NIST SP 800-207**-də. Qərar kimliyə, cihaz vəziyyətinə, resursun həssaslığına və əməliyyatın riskinə əsaslanır. Yataqxana Wi-Fi-nə qoşulmaq tələbə bazasının inzibati interfeysinə giriş üçün səbəb deyil.

- Tələbə şəxsi kompüterdən LMS materialını oxuya bilər; rəsmi qiymət dəyişikliyi təyin olunmuş əməkdaşdan və idarə olunan cihazdan tələb oluna bilər.
- VPN yalnız qorunan kanal qurur, bütün daxili resurslara avtomatik səlahiyyət yaratmamalıdır. Seqmentasiya və xidmət səviyyəsində avtorizasiya eyni siyasətin müxtəlif sərhədlərini qoruyur.
- **Davamlı qiymətləndirmə** hər paket üçün parol yazmaq deyil: sessiya və cihaz vəziyyəti seçilmiş hadisələrdə və müddətlərdə yenidən yoxlanır; cihaz idarəetmədən çıxsa, növbəti həssas əməliyyat rədd edilə bilər. Gecikmə, siyasət xidmətinin nasazlığı və köhnə tətbiqlərin məhdudiyyəti layihədə göstərilir. Sıfır etimad məhsul almaqla tamamlanmır; qərarların yoxlanılan qaydalarla qurulmasıdır.

## Kimliyə və girişə qarşı hücumlar

### Parol və sessiya hücumları

- **Credential stuffing**: başqa xidmətdən sızmış istifadəçi–parol cütlərinin kütləvi sınanması; səbəb parolun təkrar istifadəsidir.
- **Parol püskürtməsi (password spraying)**: az sayda ehtimal olunan parolu çox hesaba sınamaq. Bir hesaba çox təxmin edən kobud gücdən fərqli olaraq hesab üzrə sərt həddən yayınır.
- Kitabxanada bir IP-dən çox hesaba uğursuz giriş hücum əlaməti ola bilər, lakin yataqxananın ümumi NAT çıxışı da eyni mənzərəni yaradır: hesabların sayı, cihaz xüsusiyyətləri, vaxt ardıcıllığı və uğurlu girişdən sonrakı fəaliyyət birlikdə araşdırılır. Fişinqə davamlı MFA və parol təkrarının azaldılması kömək edir; yalnız IP bloklamaq kifayət deyil.
- **Token oğurlanması**: hücumçu parolu bilmədən hazır sessiyadan istifadə edir. Jurnalda bir qanuni giriş, sonra başqa cihazdan eyni sessiya ilə ixrac görünə bilər. İnsident cavabı parolu dəyişməklə bitmir: sessiyalar və refresh token-lər ləğv edilir, cihaz araşdırılır, şübhəli tətbiq razılıqları və sonradan verilmiş hüquqlar yoxlanır.

### Pass-the-hash və Kerberoasting

**Pass-the-hash**: müəyyən NTLM ssenarilərində parolu tapmadan onun NT heşindən kimlik məlumatı kimi istifadə. Veb bazasındakı bcrypt heşinin parol əvəzinə işlədilməsi demək deyil. Hücumçu əvvəl son qurğuda sirrə çıxış qazanır, sonra başqa sistemə həmin hesabın adından keçir (laboratoriya kompüterində yüksək imtiyazlı hesab domenə qədər risk yaradır). Müdafiə: yüksək imtiyazlı hesabları aşağı etibarlı iş stansiyalarından ayırmaq, lokal administrator parollarını fərqləndirmək, NTLM istifadəsini azaltmaq, son qurğu sirrlərini qorumaq; parol uzunluğunu artırmaq artıq oğurlanmış heşi dayandırmır.

**Kerberoasting**: autentifikasiya olunmuş hücumçu xidmət principal adına (**SPN**) xidmət bileti alır və xidmət açarı ilə qorunan hissədə oflayn parol təxminləri aparır. Bilet istəmək qanuni funksiyadır; zəif xidmət hesabı parolu onu hücuma çevirir. Müdafiə: uzun, təsadüfi, idarə olunan sirr, uyğun mühitdə **gMSA**, lazımsız imtiyazın verilməməsi.

| Hücum | Mümkün müşahidə | Prioritet tədbir |
| --- | --- | --- |
| Credential stuffing | Çox hesab üzrə sızmış cütlərlə giriş | MFA, məhdudiyyət, sızmış parol yoxlaması |
| Parol püskürtməsi | Bir neçə təxminlə çox hədəf hesab | Hesablararası korrelyasiya |
| Pass-the-hash | Qeyri-adi NTLM və daxili keçid | Sirrin mənbəyini təmizləmək, imtiyazları ayırmaq |
| Kerberoasting | Qeyri-adi xidmət bileti sorğuları | Xidmət sirrlərini gücləndirmək, hüquqları azaltmaq |
| Token oğurlanması | Yeni kontekstdə hazır sessiya | Token və sessiyaları ləğv etmək, cihazı araşdırmaq |

Windows-da **4624** və **4625** uğurlu və uğursuz girişləri, **4768** TGT sorğusunu, **4769** xidmət bileti sorğusunu araşdırmağa kömək edir. Bir 4769 hadisəsi Kerberoasting-in sübutu deyil: audit siyasəti, jurnalın mənbəyi, şifrələmə növü, xidmətlərin sayı, sorğunu edən hesab və onun normal işi kontekst verir.

Jurnal nümunəsi (şərti, parol və tam token yoxdur): 08:10 `login` uğurlu, `user=u-1042`, `method=webauthn`, `session_id=s-208`; 08:12 `grade.export` `deny`, `reason=course_not_assigned`, eyni `session_id`. Birincidə autentifikasiya uğurludur, ikincidə avtorizasiya rəddidir; onları eyni uğursuz giriş sayğacında toplamaq mənanı gizlədər. Vaxt, sabit hesab identifikatoru, resurs, əməliyyat, nəticə və səbəb saxlanır; jurnallar uzaq qorunan mənbəyə göndərilir, saatlar sinxronlaşdırılır, giriş və saxlama müddəti məhdudlaşdırılır.

## Sınaq, audit və koordinasiya

### PDCA ilə giriş siyasətinin təkmilləşdirilməsi

**PDCA**: planlaşdırma (Plan), icra (Do), yoxlama (Check), təkmilləşdirmə (Act). Giriş modelinin əvəzi deyil, onun idarə olunma prosesidir. **ISO/IEC 27001:2022** informasiya təhlükəsizliyinin idarəetmə sistemi üçün tələblər verir; **ISO/IEC 27002:2022** 93 tədbiri dörd mövzuda qruplaşdırır. Standart hər istifadəçiyə hansı rolun veriləcəyini hazır müəyyən etmir.

| Mərhələ | Görülən iş | Sübut |
| --- | --- | --- |
| Plan | Qiymət dəyişikliyi üçün risk və siyasət seçilir | Rol xəritəsi, məsul şəxs, meyar |
| Do | MFA, rol və API yoxlaması qurulur | Konfiqurasiya və təsdiqlənmiş dəyişiklik |
| Check | İcazəli və qadağan sorğular sınanır | Test nəticələri və faktiki hüquq siyahısı |
| Act | Artıq hüquq və proses səhvi düzəldilir | Ləğv təsdiqi və təkrar yoxlama |

Şərti məqsəd: işdən ayrılan əməkdaşın kritik girişi qüvvəyə minmə vaxtından sonra **15 dəqiqə** ərzində bağlanır. Ölçmə kadr hadisəsinin vaxtından başlayır, IAM bildirişinin yaranmasından yox. Hədəfi keçən sistemdə gecikmənin mənbəyi tapılır (kadr qeydi gec gəlib, sinxronlaşma dayanıb, lokal sessiya qalıb). Orta göstərici ən uzun gecikmələri gizlədir, istisnalar da araşdırılır.

### Testbed və mənfi sınaqlar

**Sınaq mühiti (testbed)** mexanizmin davranışını təcrid olunmuş şəraitdə yoxlayan quruluşdur; BLP və Biba kimi xassəni formal müəyyən edən model deyil. Saxta tələbə məlumatları, test hesabları, ayrıca kataloq və tətbiq nüsxəsi işlədilir; fərqlər nəticəni istehsalatdan uzaqlaşdırmamalıdır.

- **Müsbət sınaq**: əməkdaş öz kursunu dəyişə bilir. **Mənfi sınaq**: başqa kursu dəyişə bilmir.
- **Sərhəd sınağı**: sessiyanın açılma və bağlanma anı, rolun ləğvindən sonrakı hazır sessiya, çatışmayan atribut, dayanmış siyasət xidməti.
- Obyekt identifikatorunu dəyişib başqa tələbənin qeydini açmaq cəhdi server səviyyəsində rədd edilməlidir; düymənin ekranda görünməməsi bu testin əvəzi deyil.
- Gözlənilən qərar sınaqdan əvvəl yazılır; test proqramın hazırda verdiyi nəticəni doğru sayırsa, səhvi təkrar edir. Giriş baxışı, jurnal və proses sənədi uyğun gəlməlidir.
- **Audit** formal sertifikatla məhdudlaşmır: hüququn əsasını və faktiki icrasını sübut edən təkrarlana bilən yoxlamadır.

### Təhlükəsizlik domenlərinin koordinasiyası

Multiagent şəbəkə təsvirində **agent** müəyyən təhlükəsizlik domeninin məsul xidmətini təmsil edir (mütləq süni intellekt deyil). **Formal** koordinasiya qayda, hadisə formatı və səlahiyyət bölgüsü ilə, **qeyri-formal** koordinasiya şəxsi əlaqələrlə gedir; kritik prosesi yalnız şəxsi tanışlığa bağlamaq davamlı deyil.

Dörd səviyyə: **ümumdövlət** (səlahiyyətli qurumlar arasında qaydalar və məlumat mübadiləsi), **korporativ** (universitetdə vahid siyasət), **lokal** (fakültə və İT bölmələri), **obyekt** (konkret LMS xidmətinin əməliyyatları). Bu mümkün təşkilati modeldir, bütün ölkələrdə eyni hüquqi struktur iddiası deyil.

Nümunə: oğurlanmış hesab xəbərdarlığını **SOC** alır, IAM hesabı və sessiyaları məhdudlaşdırır, LMS sahibi qiymət dəyişikliklərini yoxlayır, kadr/qeydiyyat xidməti şəxs əlaqəsini təsdiqləyir. Kənar koordinasiyada məlumat səlahiyyət və ehtiyac çərçivəsində ötürülür; hər tərəfin hansı siqnalı alacağı, nəyi dəyişə biləcəyi və nəticəni necə təsdiqləyəcəyi yazılır. Kimlik jurnallarını hamıya açmaq koordinasiya deyil.

### Məxfiliyin hüquqi çərçivələri

- **95/46/EC** direktivi 25 may 2018-dən tətbiq olunan **(EU) 2016/679 GDPR** ilə əvəz olunub.
- **2002/58/EC** direktivi elektron rabitə sektorunda fərdi məlumatların və məxfiliyin qorunmasını tənzimləyir.
- Avropa Şurası: **ETS 108** Konvensiyası və ona əlavə **ETS 181** Protokolu fərdi məlumatların qorunmasına aiddir; **ETS 185** (Budapeşt) Konvensiyası kibercinayətkarlıqla mübarizəni, o cümlədən kompüter məlumatlarının və sistemlərinin məxfiliyinə, tamlığına və əlçatanlığına qarşı əməlləri əhatə edir; **ETS 189** kompüter sistemləri vasitəsilə törədilən irqçi və ksenofob əməllərlə bağlı əlavə protokoldur.

Universitet tətbiq dairəsinə düşən tələbləri seçərkən kimlik atributlarının və audit qeydlərinin emal məqsədini, hüquqi əsasını, çıxışı və saxlanma müddətini nəzərə alır; sənədlərin fərqli məqsədləri düzgün ayrılmalıdır.

## Yadda saxlamaq üçün

:::reveal Hesab bağlanıb, amma LMS sessiyası açıqdır. Niyə leaver prosesi tamamlanmış sayılmır?
Mərkəzi bloklama ilə tətbiq sessiyasının ləğvi ayrıdır. Tamamlanma kataloq cavabı ilə deyil, hədəf tətbiqlərdə girişin faktiki rəddi ilə ölçülür; sessiyalar, refresh token-lər və API açarları ayrıca ləğv edilir.
:::
