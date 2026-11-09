+++
title = "Şəbəkə təhlükəsizliyinin əsasları: CIA və DAD triadası"
unit = "uzun"
order = 1
summary = "Tam mühazirə: informasiya və verilənlər, CIA və DAD, autentiklik və Parker heksadı, AAA, təhdid–zəiflik–risk, riskə cavab, layihələndirmə prinsipləri, təsnifat, OSI/TCP/IP, Equifax–Stuxnet–WannaCry və tələblərin yoxlanması."
updated = 2026-11-09

[[source]]
title = "Mühazirə 1: Şəbəkə təhlükəsizliyinin əsasları: CIA və DAD triadası"
note = "Elmar Cabbarov, 2026–2027"
+++

Bu mövzu bütün kursun lüğətidir. Sonrakı mövzularda hər hücumu və hər müdafiə vasitəsini bu üç hərfə bağlayacağıq: hansı xassəni pozur, hansını qoruyur. Mühazirədəki universitet topologiyası, adlar, ünvanlar, hesablar və rəqəmlər **şərti tədris nümunəsidir**, real universitetin faktiki göstəricisi deyil.

:::note Bu mövzudan sonra bacarmalısan
- aktiv, zəiflik, təhdid, risk, insident və nəzarət sözlərini qarışdırmadan işlətməyi;
- istənilən hadisəni oxuyub CIA-nın hansı komponentinin pozulduğunu və hadisənin DAD-ın hansı ünsürünə uyğun gəldiyini deməyi;
- autentiklik və inkaredilməzlik üçün hansı sübutun tələb olunduğunu izah etməyi;
- AAA üzrə giriş qərarını təhlil etməyi;
- riski ehtimal və təsir üzrə qiymətləndirib dörd cavab strategiyasından birini seçməyi;
- şəbəkənin müxtəlif səviyyələri üçün uyğun tədbirlər seçməyi.
:::

## İnformasiya, verilənlər və bilik

### Mənanın yaranması və təqdimat formaları

**İnformasiya** hadisə, obyekt və proses haqqında məna daşıyan məlumatdır. **Verilənlər** (*data*) həmin məlumatın saxlanma, emal və ötürmə üçün formal təsviridir. **Bilik** (*knowledge*) informasiyadan əlaqələri anlamaq və qərar vermək üçün istifadə etməyə imkan verən qaydalar və təcrübədir. Sərhəd kontekstdən asılıdır: bazadakı rəqəm özü ilə bütün mənanı daşımır, sütunun adı, ölçü vahidi və aid olduğu şəxs bilinməlidir.

:::example Verilənlərdən biliyə
Bazada `student_id=142, score=85` yazılıb (şərti nümunə). Bu, formal **verilənlərdir**. Rəqəmlərin müəyyən fənnin yekun nəticəsini bildirdiyi məlum olanda **informasiya** alınır. Təqaüdün hesablanması qaydasını bilən əməkdaş bu nəticəni digər fənlərlə əlaqələndirib qərar verirsə, bu **biliyin** işidir. Təhlükəsizlik həm rəqəmləri, həm kontekstini qorumalıdır: bal dəyişməsə də başqa tələbənin identifikatoruna bağlanarsa, nəticə yanlışdır.
:::

İnformasiya mətn, səs, qrafika və video formasında təqdim olunur. **Analoq** təqdimatda fiziki kəmiyyət fasiləsiz dəyişə bilər, **rəqəmsal** təqdimat diskret simvollar və kodlarla işləyir; auditoriyadakı danışıq mikrofonla rəqəmsallaşdırılanda seçmə və kodlaşdırma aparılır. Səs yazısı, transkript və imzalanmış protokol eyni hadisəni təsvir etsə də fərqli təhlükəsizlik tələblərinə malikdir.

**Kodlaşdırma ilə şifrələmə fərqlidir.** UTF-8 mətn simvollarını baytlara çevirir, Base64 ikilik məlumatı mətn simvolları ilə təqdim edir; bu üsulları bilən hər kəs ilkin məzmunu bərpa edə bilər. Şifrələmə məzmunu açarla qoruyur. Kafedranın tələbə siyahısını Base64 formasında məktuba əlavə etməsi siyahını məxfi etmir; faylın sıxılması da özlüyündə məxfiliyi qorumur.

Hesabi (bal), mətn (ad) və məntiqi (qeydiyyat aktivdir/deyil) verilənlər gündəlik işlənir. Proqramlaşdırmadakı göstərici (pointer) yaddaş obyektinə istinaddır; onu bütün informasiya sistemləri üçün ayrıca məzmun növü saymaq düzgün deyil. Tipin səhv seçilməsi təhlükəsizlik problemi yarada bilər: bal sahəsində mətn qəbul edən tətbiq gözlənilməyən girişləri düzgün emal etməyə bilər.

### Keyfiyyət xassələri və tarixi kontekst

İnformasiyanın faydası onun düzgün anlaşılmasından və qərara uyğunluğundan asılıdır. Keyfiyyət xassələri təhlükəsizlik xassələri ilə əlaqəlidir, onları əvəz etmir. Dəyişdirilmədən qorunan köhnə dərs cədvəli tamlığını saxlayıb, tələbəyə isə səhv istiqamət verə bilər; doğru məlumatın gec çatması da tədris prosesini poza bilər.

| Xassə | Mənası | Universitet nümunəsi |
| --- | --- | --- |
| Düzgünlük | Məzmunun real vəziyyətə uyğunluğu | Auditoriya nömrəsi faktiki dərs yeri ilə uyğun gəlir |
| Dolğunluq | Qərar üçün lazım olan hissələrin olması | Cədvəldə fənn, tarix və auditoriya göstərilir |
| Aktuallıq | Məlumatın aid olduğu vaxt üçün qüvvədə olması | İmtahanın dəyişmiş vaxtı portalda görünür |
| Aydınlıq | İstifadəçinin məzmunu düzgün anlaması | Tarixin hansı semestrə aid olduğu yazılır |
| Faydalılıq və qiymətlilik | Məlumatın konkret məqsədə xidmət etməsi | Kitabxana istifadəsi hesabatı fond seçiminə kömək edir |
| Təhlükəsizlik tamlığı | İcazəsiz və ya təsadüfi dəyişiklikdən qorunma | Təsdiqlənmiş cədvələ nəzarətsiz düzəliş edilmir |

:::warning Dolğunluq ilə təhlükəsizlik tamlığı
Bütün tələbələrin adı olmayan siyahı natamamdır. Siyahı başlanğıcdan belə hazırlanıbsa, bu, **keyfiyyət qüsuru** ola bilər. Hücumçu adları silibsə, artıq **tamlıq pozuntusudur**. Təhlükəsizlik araşdırması ilkin vəziyyəti və icazəli dəyişiklik qaydasını bilmədən düzgün nəticəyə gələ bilməz.
:::

İnformasiyanın qeydiyyatı və yayılması tarixən yazı, çap, elektrik rabitəsi və kompüter şəbəkələri ilə genişlənib. Bu mərhələləri "informasiya inqilabları" adlandıran təsnifatlar var, lakin bölgü vahid elmi standart deyil. Avropada Qutenberqin XV əsrdə çap texnologiyasını inkişaf etdirməsi biliyin çoxaldılmasını asanlaşdırdı; teleqraf, telefon və radio məsafədən əlaqəni dəyişdi; ARPANET-in 1969-cu ildə işə başlaması şəbəkələşmənin tanınmış mərhələsidir. Elektrikin kəşfini bir şəxsin 1834-cü ildəki işi ilə bağlamaq düzgün deyil.

Bu tarix təhlükəsizlik baxımından da oxunmalıdır. Əlyazmanın oğurlanması bir nüsxəyə təsir edə bilərdi; rəqəmsal sənəd mənbədən silinmədən köçürülür və çoxsaylı ünvanlara yayılır. Rəqəmsal daşıyıcı daimi deyil: avadanlıq köhnəlir, format dəstəyi itir, açarlar unudulur. Uzunmüddətli saxlama yoxlama, miqrasiya və ehtiyat nüsxə tələb edir.

## İnformasiya təhlükəsizliyinin əhatəsi

**İnformasiya təhlükəsizliyi** (*information security*) informasiyanın məxfiliyini, tamlığını və əlçatanlığını qoruyan idarəetmə vəziyyəti və fəaliyyətləridir. İnformasiyanın mühafizəsi bu məqsədlərə xidmət edən konkret tədbirlərin toplusudur. **Şəbəkə təhlükəsizliyi** (*network security*) rabitə infrastrukturunu, əlaqələri və şəbəkə üzərindən xidmətləri qoruyur. **Kibertəhlükəsizlik** (*cybersecurity*) rəqəmsal sistemlərə və onların qarşılıqlı əlaqələrinə yönəlir. Kağız tələbə işi və bağlı şkaf informasiya təhlükəsizliyinə aiddir, lakin şəbəkə trafiki deyil.

**Aktiv** (*asset*) təşkilat üçün dəyəri olan resursdur. Universitetdə aktiv yalnız server deyil: tələbə bazası, qiymət jurnalı, diplom reyestri, şəbəkə avadanlığı, əməkdaşların təcrübəsi və xidmətə etimad da qorunmalı dəyər daşıyır. Serverin qiyməti ilə oradakı məlumatın itkisinin təsiri eyni deyil: ucuz diskdəki yeganə dissertasiya nüsxəsi bahalı ehtiyat serverdən daha böyük akademik itki yarada bilər.

Təhlükəsizlik məqsədi aktivin xidmət etdiyi işdən çıxarılır. Universitetin işi tələbənin təhsil alması, qiymətləndirilməsi və nəticəsinin düzgün rəsmiləşdirilməsidir. Portalı hamı üçün bağlamaq bəzi hücum yollarını azaldar, amma həmin işi də dayandırar. Məqsəd resursu mümkün qədər bağlamaq yox, **icazəli istifadəyə uyğun qorumaqdır**; icazənin kimə, hansı məlumat üçün, hansı müddətdə verildiyi aydın olmalıdır.

| Səviyyə | Qorunan maraq | Universitetlə əlaqə |
| --- | --- | --- |
| Şəxs | Fərdi məlumat və qanuni informasiya almaq imkanı | Tələbə öz nəticəsini görür, başqasının tibbi sənədini görmür |
| Təşkilat | Tədris və inzibati xidmətlərin düzgün işləməsi | LMS, maliyyə sistemi və diplom reyestri qorunur |
| Cəmiyyət | Etibarlı informasiya və xidmətlərə inam | Diplomun həqiqiliyini yoxlamaq mümkün olur |
| Dövlət | Kritik xidmətlər və informasiya infrastrukturunun qorunması | Dövlət sistemləri ilə əlaqələrdə müəyyən edilmiş tələblər tətbiq olunur |

Tədbirlər **inzibati** (kimin qərar verdiyini və qaydanı müəyyən edir), **texniki** (giriş nəzarəti, şifrələmə, audit mexanizmi) və **fiziki** (daşıyıcını və avadanlığı qoruyur) ola bilər. Server otağının açarı hamıda varsa, güclü parol kifayət etmir; istifadəçinin vəzifəsi dəyişəndə icazəsi yenilənmirsə, yaxşı firewall artıq hüququ aradan qaldırmır.

İnformasiya-kommunikasiya texnologiyaları (İKT) təhsil və iqtisadiyyatda məsafədən xidmətləri genişləndirir. Elektron dövlət xidmətində istifadəçi məlumatın qorunacağına və nəticənin doğru olacağına etibar etməlidir. Ona görə təhlükəsizlik tələbi **xidmətin layihəsindən başlamalıdır**: sonradan alınmış təhlükəsizlik məhsulu aydın olmayan məsuliyyət bölgüsünü düzəltmir.

## CIA triadası

CIA məxfilik (*confidentiality*), tamlıq (*integrity*) və əlçatanlıq (*availability*) sözlərinin ingiliscə baş hərflərindən yaranır. Bu üç xassə təhlükəsizlik məqsədlərini ayırmağa kömək edir; onlar məhsul adları deyil. Eyni texniki tədbir bir neçə məqsədə xidmət edə bilər, bir məqsəd isə bir neçə tədbir tələb edə bilər. Azərbaycan dilli ədəbiyyatda hər birinin bir neçə adı var, imtahanda hamısını tanımaq lazımdır.

| Xassə | Başqa adları | Mənası | Pozulma | Qoruyan vasitələr |
| --- | --- | --- | --- | --- |
| Məxfilik (confidentiality) | konfidensiallıq | Məlumatı yalnız icazəsi olan görür | Sızma, dinləmə, səhv adresə göndərilmiş e-poçt | Şifrələmə, girişə nəzarət, MFA, təsnifat |
| Tamlıq (integrity) | bütövlük | Məlumat icazəsiz dəyişdirilməyib, mənbəyi doğrudur | Bank köçürməsində məbləğin dəyişdirilməsi, saytın üzünün dəyişdirilməsi (defacement) | Heş (SHA-256), rəqəmsal imza, HMAC, versiya nəzarəti, dəyişiklik logları |
| Əlçatanlıq (availability) | əlyetənlik | İcazəli istifadəçi məlumatı lazım olanda ala bilir | DDoS, ransomware, elektrik kəsintisi, disk qəzası | Ehtiyat nüsxə, RAID, klaster, UPS, DDoS qoruması |

:::tip Hansı vasitə hansı xassəni qoruyur
Şifrələmə → **məxfilik**. Heş və imza → **tamlıq**. Ehtiyat nüsxə və artıqlıq (*redundancy*) → **əlçatanlıq**. Heş məlumatı gizlətmir, yalnız dəyişib-dəyişmədiyini göstərir. Şifrələmə isə dəyişikliyi özü-özlüyündə aşkarlamır (buna görə müasir protokollar AES-GCM kimi autentifikasiyalı şifrələmə işlədir).
:::

### Məxfilik və icazəli açıqlama

Məxfilik məlumatın yalnız **icazəli subyektlərə** açıqlanmasıdır. Subyekt insan, xidmət hesabı və ya proqram ola bilər. Məxfilik "məlumatı heç kimə verməmək" demək deyil: tələbənin nəticəsini onun özünə göstərmək icazəli açıqlamadır, eyni nəticəni bütün yataqxana şəbəkəsinə açmaq pozuntudur. Sərhədi məlumatın sahibi, qanuni tələblər və universitetin siyasəti müəyyən edir.

Pozuntu sızma, trafikin dinlənilməsi, səhv ünvana məktub və ya açıq paylaşım ilə baş verə bilər. Tələbə bazasının internetdən əlçatmaz olması sızmayacağına zəmanət vermir: daxili əməkdaş icazəsindən artıq ixrac edə, xidmət hesabının açarı oğurlana, ehtiyat nüsxə açıq qovluğa düşə bilər. Buna görə məxfilik məlumatın **bütün nüsxələrinə və ötürmə yollarına** aid edilir.

Şifrələmə oxumaq üçün açar tələb edir. Ötürülən məlumat TLS kimi qorunan kanalla daşına, diskdəki məlumat ayrıca şifrələnə bilər. Disk şifrələməsi oğurlanmış daşıyıcını qoruyur; işləyən serverdə artıq avtorizasiya almış tətbiqin məlumatı oxumasını dayandırmır. Açar eyni açıq qovluqda saxlanırsa, şifrələmənin faydası kəskin azalır; açarların saxlanması, ehtiyatlanması və ləğvi ayrıca planlaşdırılmalıdır.

:::example HTTPS var, amma sızma var
LMS-də tələbə daxil olduqdan sonra `GET /api/results/142` sorğusu verir (identifikator şərtidir). Server yalnız giriş faktını yoxlayıb həmin identifikatorun kimə aid olduğunu yoxlamırsa, başqa tələbənin nəticəsi görünə bilər. **HTTPS bu xətanı düzəltmir**: məlumat qorunan kanalla icazəsiz şəxsə çatır. Çatışmayan tədbir **obyekt səviyyəsində avtorizasiyadır**. Sorğudakı identifikatorun dəyişdirilə bilməsi özlüyündə zəiflik deyil; icazənin yoxlanmaması zəiflikdir.
:::

:::warning Məxfilik fərdi həyatın toxunulmazlığı deyil
Universitet məlumatı sızdırmadan da lazımsız şəxsi məlumat toplaya və onu bəyan edilmiş məqsəddən kənar işlədə bilər. Belə halda texniki məxfilik tədbirləri olsa da, fərdi məlumatların işlənməsi problemi qalır.
:::

### Tamlıq və etibarlı dəyişiklik

Tamlıq məlumatın icazəsiz və ya **təsadüfi** dəyişdirilmədən qorunmasıdır; silinmə, yanlış obyektə bağlanma və icazəsiz əvəzləmə də tamlığa aiddir. Qiymət jurnalında düzəliş mümkündür, amma düzəlişi kim edə bilər, nə əsasla edir və əvvəlki qiymət necə saxlanır sualları cavablandırılmalıdır. Məqsəd dəyişməzlik deyil, **nəzarət edilən dəyişikliyədir**.

Kriptoqrafik **heş** (*hash*) dəyişən ölçülü məlumatdan sabit ölçülü xülasə çıxarır. SHA-256 faylın dəyişib-dəyişmədiyini yoxlamaq üçün işlədilə bilər: etibarlı ilkin xülasə ilə sonrakı xülasə fərqlidirsə, baytlar dəyişib. Heş məzmunu gizlətmir və faylın doğru məlumat daşıdığını sübut etmir. Hücumçu həm faylı, həm yanındakı heş faylını dəyişə bilirsə, adi müqayisə hücumu aşkar etməyə bilər.

Aşağıdakı əmrlər yerli laboratoriyadakı şərti `qiymetler.csv` faylı üçündür: birinci əmr başlanğıc xülasəni saxlayır, ikinci sonrakı vəziyyəti müqayisə edir. Etalon faylın **ayrıca qorunması** bu nümunənin əsas şərtidir.

```bash
sha256sum qiymetler.csv > qiymetler.sha256
sha256sum -c qiymetler.sha256
```

**HMAC** (açarlı mesaj autentifikasiya kodu) xülasəni gizli açarla bağlayır; açarsız hücumçu etibarlı kod yarada bilməməlidir. Lakin açarı paylaşan hər tərəf kod yarada bildiyinə görə HMAC konkret şəxsin müəllifliyini **üçüncü tərəfə sübut etmək üçün uyğun deyil**. **Rəqəmsal imza** (*digital signature*) şəxsi açarla yaradılır və uyğun açıq açarla yoxlanır; imzanın kimə aid olduğu isə açarın etibarlı kimliklə əlaqəsinə söykənir.

Tamlıq yalnız kriptoqrafiya məsələsi deyil. Verilənlər bazasında xarici açarlar əlaqəsiz qiymət sətirlərini, tranzaksiya isə yarımçıq yeniləmələri məhdudlaşdıra bilər. Tətbiq balın icazəli intervalda olmasını yoxlayır, rol nəzarəti həmin balı kimin dəyişəcəyini müəyyən edir. İmza səhv daxil edilmiş qiyməti həqiqətə çevirmir: iş prosesinin düzgünlüyü, girişin yoxlanması və dəyişiklik tarixçəsi birlikdə qurulmalıdır.

### Əlçatanlıq və bərpa qabiliyyəti

Əlçatanlıq icazəli istifadəçinin tələb olunan xidməti **münasib vaxt ərzində** ala bilməsidir. Serverin elektrikə qoşulması kifayət deyil: ad həlli, şəbəkə yolu, identifikasiya xidməti, tətbiq və baza işləməlidir. İmtahanın son dəqiqəsində cavab verməyən LMS texniki baxımdan işlək proses saxlasa da istifadəçi üçün əlçatan deyil. Tələb xidmətin cavab müddəti və iş vaxtı ilə konkretləşdirilir.

Paylanmış xidmətdən imtina hücumu (*distributed denial of service*, DDoS) çoxsaylı mənbə ilə kanalın, bağlantı cədvəlinin və ya tətbiq resursunun tükənməsinə səbəb ola bilər. Hamı üçün eyni sürət həddi kifayət etmir: yataqxananın çoxlu tələbəsi bir çıxış IP-si paylaşa bilər, mənbə IP-yə görə sərt bloklama onların hamısını imtahandan uzaqlaşdıra bilər. **Müdafiə tədbirinin öz təsiri də yoxlanmalıdır.**

| Vasitə | Nə üçündür | Sərhədi |
| --- | --- | --- |
| Ehtiyat nüsxə (backup) | İtirilmiş vəziyyəti bərpa etmək | Ayrı saxlanan, dəyişdirilməsi məhdud, bərpası yoxlanmış nüsxə lazımdır |
| Artıqlıq (redundancy) | Komponent sıradan çıxanda xidmətin davamı | Eyni asılılığın sıradan çıxması bütün nüsxələri dayandıra bilər |
| RAID | Müəyyən disk nasazlıqlarına qarşı dayanıqlıq | Ehtiyat nüsxənin əvəzi deyil: icazəli hesab faylı siləndə silinmə massivdə də görünür |
| Replikasiya | Məlumatın başqa serverdə nüsxəsi | Zərərli dəyişikliyi də digər serverə ötürə bilər |

**RTO** (*recovery time objective*, bərpa vaxtı hədəfi) xidmətin nə qədər müddətdə bərpa edilməli olduğunu, **RPO** (*recovery point objective*, bərpa nöqtəsi hədəfi) qəbul edilən məlumat itkisini zamanla ifadə edir. Şərti olaraq RTO iki saat, RPO on beş dəqiqədirsə, xidmət iki saatda qayıtmalı və itki əvvəlki on beş dəqiqədən artıq olmamalıdır. Bu rəqəmləri satıcı deyil, **prosesin sahibi** əsaslandırır; imtahan cavabları üçün on beş dəqiqəlik itki də qəbul edilməyə bilər.

| Xassə | Universitetdə tələb | Tədbir | Tədbirin sərhədi |
| --- | --- | --- | --- |
| Məxfilik | Tələbə yalnız öz şəxsi işini görür | Obyekt üzrə icazə və şifrələmə | Oğurlanmış sessiya icazəli istifadəçini təqlid edə bilər |
| Tamlıq | Qiymət əsaslandırılmış qaydada dəyişir | Rol nəzarəti, təsdiq və audit | Yanlış ilkin qiymət ayrıca yoxlanmalıdır |
| Əlçatanlıq | İmtahan cavabı vaxtında qəbul edilir | Tutum planı, ehtiyat xidmət və bərpa | Eyni asılılığın sıradan çıxması bütün nüsxələri dayandıra bilər |

### Xassələr arasında balans

Xassələr arasındakı seçim iş məqsədi ilə aparılır. Hər səhifədə MFA soruşmaq girişə mane ola, amma oğurlanmış sessiyanın bəzi risklərini həll etməyə bilər. Daha düzgün seçim həssas əməliyyat zamanı əlavə yoxlama, sessiyanın məhdud müddəti və oğurlanma siqnallarına reaksiya ola bilər. Resursların hamısına eyni qoruma səviyyəsi vermək büdcəni yanlış istiqamətə yönəldir.

| Sistem | Ən kritik xassə | Səbəb |
| --- | --- | --- |
| Tələbələrin şəxsi işləri (pasport, tibbi arayış, ünvan) | Məxfilik | Sızma geri qaytarılmır, fərdi məlumatlar qanunla qorunur |
| Elektron qiymət jurnalı, diplom reyestri | Tamlıq | Bir balın dəyişməsi təqaüdə, diploma, universitetin nüfuzuna təsir edir |
| İmtahan günü onlayn test sistemi | Əlçatanlıq | Sistem 20 dəqiqə dayansa minlərlə tələbənin imtahanı pozulur |
| Xəbər saytı, dərs cədvəli (açıq) | Tamlıq, əlçatanlıq | Məxfilik tələb olunmur; amma saxta imtahan tarixi yazılsa və ya sayt dayansa ziyan var |

## DAD triadası və hücumların nəticələri

DAD informasiya təhlükəsizliyinə **pozuntu tərəfindən** baxır: ifşa (*disclosure*), dəyişdirmə (*alteration*) və məhv etmə (*destruction*). Bəzi mənbələr sonuncu D-ni xidmətdən imtina (*denial*) kimi genişləndirir; bu iki anlayışın fərqi var, çünki məlumatı məhv etmədən də xidmətə girişi dayandırmaq mümkündür. **CIA qorunan xassəni, DAD ona qarşı baş verən nəticəni adlandırır**; hadisəni təhlil edəndə hər ikisi göstərilir.

:::tip Situasiya sualında hansı termin
"Nə baş verdi?" soruşulanda **DAD** termini, "nə pozuldu?" soruşulanda **CIA** termini ilə cavab verirsən.
:::

:::figure
src = "m01-1.png"
alt = "CIA xassələri, universitet nümunələri və DAD nəticələri üç sıra ilə bağlanır."
caption = "Qorunan CIA xassələrinin DAD nəticələri ilə uyğunluğu."
:::

**İfşa** məlumatın icazəsiz şəxsə məlum olmasıdır; tələbə sənədlərinin açıq paylaşım keçidi ilə göndərilməsi qəsd olmadan da ifşa yarada bilər. **Dəyişdirmə** bazadakı balın, ödəniş rekvizitinin və ya şəbəkə konfiqurasiyasının icazəsiz dəyişməsidir. **Məhv etmə** faylın silinməsi və ya istifadə üçün yararsız vəziyyətə salınmasıdır. DDoS isə məlumatı olduğu kimi saxlayıb ona müraciəti mümkünsüz edə bilər.

| Ssenari | Pozulan CIA xassəsi | DAD nəticəsi | Araşdırılan əsas fakt |
| --- | --- | --- | --- |
| Qəbul sənədləri açıq qovluqdadır | Məxfilik | İfşa | Kimin giriş əldə etdiyi və nə oxuduğu |
| İmtahan balı icazəsiz dəyişir | Tamlıq | Dəyişdirmə | Əvvəlki qiymət, hesab və əsaslandırma |
| Şəbəkə kanalı DDoS ilə dolur | Əlçatanlıq | Xidmətdən imtina | Kanal, bağlantı və tətbiq yükü |
| Administrator bazanı səhvən silir | Tamlıq və əlçatanlıq | Məhv etmə | Silinmənin əhatəsi və bərpa nöqtəsi |
| Saxta DNS cavabı portalı əvəz edir | DNS məlumatının tamlığı; sonrakı sızmada məxfilik | Dəyişdirmə, mümkün ifşa | İstifadəçinin hansı serverə çatdığı |
| Fayllar oğurlanır, sonra şifrələnir | Məxfilik, tamlıq və əlçatanlıq | İfşa, dəyişdirmə və imtina | Çıxarılan məlumat və bərpa imkanı |

:::note Sadə dillə: real nümunələr
**İfşa:** qəbul komissiyasının bulud qovluğu "linki olan hər kəs" üçün açıq qalır. **Dəyişdirmə:** saxta e-poçtla tədarükçü adından bank rekvizitlərinin dəyişdirilməsi (BEC fırıldağı). **Məhv/imtina:** ransomware fayl serverini şifrələyir.
:::

Bir hücumun bir neçə xassəni pozması təhlilin normal nəticəsidir. Fidiyə proqramı (*ransomware*) faylları icazəsiz şifrələyəndə baytlar dəyişir və istifadəçi faylı aça bilmir: **tamlıq və əlçatanlıq** təsirlənir. Əvvəlcədən məlumat çıxarılması da sübut olunarsa, **məxfilik pozuntusu** əlavə edilir. Şifrələnmiş fayl görmək məlumatın oğurlandığını sübut etmir; ifşa barədə qərar çıxış trafiki, fayl oxuma qeydləri və digər sübutlara söykənməlidir.

:::exam Tələ: bir hücum bir neçə xassəni poza bilər
Müasir ransomware əvvəlcə faylları oğurlayır (ifşa → məxfilik), sonra şifrələyir (məhv/inkar → əlçatanlıq; faylların icazəsiz dəyişdirilməsi tamlığı da pozur). Buna **ikiqat qəsb (double extortion)** deyilir. Sualda "hansı xassələr pozuldu" deyə cəm halında soruşulursa, **hamısını sadala**.
:::

Şərti nümunədə dekanlığın fayl serverində əmrlər açılmır: ransomware ola bilər, amma disk xətası, yanlış icazə və açar itkisi də eyni əlaməti yaradır. **Əlaməti səbəblə qarışdırmaq yanlış cavab tədbirinə gətirir**: nasaz diskdə nəzarətsiz bərpa cəhdi qalan məlumatı da itirə bilər.

Tədbir də pozulan xassəyə uyğun seçilir. Ehtiyat nüsxə xidmətin və məlumatın bərpasına kömək edir, artıq baş vermiş ifşanı geri almır. Parolun dəyişdirilməsi aktiv sessiyaları avtomatik ləğv etməyə bilər. Şəbəkə bloklaması hücum kanalını kəsə bilər, bazada edilmiş dəyişikliyi düzəltmir. İnsident üzrə üç sual verilir: davam edən zərər necə dayandırılır, düzgün vəziyyət necə tapılır, təkrarlanma yolu necə bağlanır?

## CIA-dan kənar təhlükəsizlik xassələri

### Autentiklik, inkaredilməzlik və hesabatlılıq

**Autentiklik** (*authenticity*) mənbənin və ya obyektin iddia edilənə uyğun olmasıdır; məsələn, qəbul məktubunun həqiqətən universitetdən gəldiyini yoxlamaq. Məktubun mətni dəyişməyibsə də saxta mənbədən yarana bilər: **dəyişiklik aşkarlanmaması mənbənin doğruluğuna bərabər deyil**. Rəqəmsal sertifikat, imza və etibarlı açar əlaqəsi mənbənin yoxlanmasına kömək edir.

**Autentifikasiya** (*authentication*) isə kimlik iddiasının yoxlanması prosesidir. İstifadəçi autentifikasiya edilə bilər, sənədin autentikliyi ayrıca yoxlanar: tələbə hesabı ilə daxil olub saxta arayış yükləyibsə, giriş yoxlaması sənədi həqiqi etmir. Eyni qayda server sertifikatına aiddir: sertifikat domenlə əlaqəni yoxlamağa kömək edir, saytdakı bütün məzmunun akademik doğruluğunu təsdiqləmir.

**İnkaredilməzlik** (*non-repudiation*) əməliyyatın mənşəyini və ya çatdırılmasını sonradan inkar etməyə qarşı sübut yaradan xassədir; mənası "təxirə salınmamaq" deyil. Diplom əlavəsinin rəqəmsal imzası, etibarlı vaxt möhürü və imza açarının qorunması müəlliflik iddiasını əsaslandıra bilər. İmza insanın heç vaxt etiraz edə bilməyəcəyi demək deyil: açarın oğurlanması, sertifikatın qüvvəsi və imza anındakı şərait mübahisədə yoxlanır.

**Hesabatlılıq** (*accountability*) fəaliyyətin məsul subyektlə əlaqələndirilə bilməsidir. Kafedra əməkdaşları bir dekanlıq hesabını paylaşırsa, qeyddə hesab görünür, konkret icraçı bilinmir. Fərdi hesablar, təsdiq qaydası və dəyişdirilmədən qorunan audit qeydləri bu boşluğu azaldır. Hesabatlılıq məsuliyyətin avtomatik hüquqi sübutu deyil: hesab oğurlana bilər, əlaqə başqa dəlillərlə də yoxlanmalıdır.

| Xassə | Cavab verdiyi sual | Uyğun vasitə | Tək vasitənin çatışmazlığı |
| --- | --- | --- | --- |
| Autentiklik | Mənbə iddia edilən mənbədirmi? | İmza və sertifikat yoxlaması | Etibarsız açar əlaqəsi yanlış etimad yaradır |
| İnkaredilməzlik | Mənşə barədə sonradan hansı sübut var? | Rəqəmsal imza, vaxt sübutu və qeyd zənciri | Açarın kimdə olduğu araşdırılmalıdır |
| Hesabatlılıq | Əməliyyatı hansı subyekt edib? | Fərdi hesab və qorunan audit | Paylaşılan və oğurlanmış hesab əlaqəni zəiflədir |

Şərti nümunədə qiymət düzəlişinə fakültə əməkdaşı elektron təsdiq verir. Bazada sadəcə `approved=true` saxlamaq **zəif sübutdur**: bazaya yazan proqram bunu dəyişə bilər. Təsdiqin aid olduğu sənəd versiyası, təsdiqləyən hesab, vaxt və qərarın əsası birlikdə saxlanmalıdır. Güclü müəlliflik sübutu tələb edilirsə, məhz həmin versiya imzalanır; imza sonradan dəyişən canlı səhifəyə deyil, konkret məzmuna bağlanır.

### Parker heksadı

Donn Parkerin altı xassəli modeli, **Parker heksadı** (*Parkerian hexad*), CIA-ya **sahiblik və nəzarət** (*possession or control*), **autentiklik** və **faydalılıq** (*utility*) əlavə edir. Bu model CIA-nın səhv olduğunu demir, bəzi itkiləri daha dəqiq adlandırmağa imkan verir. Xassələr təhlildə kəsişə bilər; hər hadisəni yalnız bir xanaya salmaq tələb olunmur.

| Xassə | Qorunan məna | Nümunə |
| --- | --- | --- |
| Məxfilik | İcazəsiz açıqlamanın qarşısı alınır | Şəxsi iş yalnız səlahiyyətli əməkdaşa açılır |
| Sahiblik və nəzarət | Resurs üzərində idarəetmə itirilmir | Şifrəli arxiv diski oğurlananda nəzarət itir |
| Tamlıq | Məzmun nəzarətsiz dəyişmir | Diplom reyestrinin sətri icazəsiz əvəzlənmir |
| Autentiklik | Mənbə və obyekt həqiqidir | Arayışın universitetin imzasını daşıdığı yoxlanır |
| Əlçatanlıq | Resurs lazım olanda əldə edilir | Elektron kataloq sorğuya cavab verir |
| Faydalılıq | Əldə edilən resurs məqsəd üçün işlənə bilir | Arxiv faylı dəstəklənən formatda açılır |

Şifrəli diskin oğurlanmasında **nəzarət itkisi qətidir**, məxfilik itkisi isə açarın qorunmasından asılıdır. Diskdəki məlumatın ayrıca nüsxəsi varsa, universitet istifadəni davam etdirə bilər. Başqa nümunədə dissertasiya arxivi serverdədir və endirilir, lakin yeganə deşifrləmə açarı itirilib: baytlar əldə edilə bilsə də məzmun yararsızdır. Əməliyyat baxımından əlçatanlıq da təsirlənir, heksad isə **faydalılıq itkisini** ayrıca göstərir.

Konspektə görə heksadı yalnız **tanımaq** kifayətdir.

## AAA: kimlik, icazə və fəaliyyətin uçotu

### Üç ayrı qərar

AAA autentifikasiya, avtorizasiya (*authorization*) və fəaliyyətin uçotu (*accounting*) modelidir. Birinci mərhələ kimlik iddiasını yoxlayır, ikinci həmin subyektin konkret əmələ icazəsini müəyyən edir, üçüncü resurs istifadəsi və əməliyyatlar barədə qeydlər yaradır. Uçot qeydləri auditə xidmət edə bilər, amma hər uçot qeydi tam audit sübutu deyil; hansı sahələrin saxlandığı ayrıca müəyyən edilir.

Şəbəkədə bu model yataqxana Wi-Fi girişində, administratorun avadanlığa qoşulmasında və LMS-də işləyir. Wi-Fi istifadəçisinin hesabı tanınandan sonra ona tələbə şəbəkəsi verilə bilər; bu, onun tələbə bazasına yazmaq hüququ aldığı demək deyil. **Şəbəkə girişi ilə tətbiq icazəsi ayrı qərarlardır**, hər qərarın aid olduğu resurs və etibar sərhədi göstərilməlidir.

:::figure
src = "m01-2.png"
alt = "Giriş sorğusu autentifikasiya, avtorizasiya və LMS obyektindən keçir; hər iki mərhələ uçota yazılır."
caption = "LMS-də kimlik yoxlaması, obyekt üzrə icazə qərarı və audit qeydi."
:::

| Mərhələ | Sual | LMS nümunəsi | Tipik səhv |
| --- | --- | --- | --- |
| Autentifikasiya | Kim olduğunu necə sübut edir? | Hesab və çoxamilli yoxlama | Girişin uğurlu olmasını bütün hüquqlara bərabər saymaq |
| Avtorizasiya | Bu obyekt üzərində bu əmələ icazəsi varmı? | Yalnız öz qrupunun qiymətini dəyişir | İcazəni yalnız interfeysdə gizlətmək |
| Fəaliyyətin uçotu | Nə, nə vaxt və hansı nəticə ilə edildi? | Köhnə və sonrakı bal, hesab və sorğu identifikatoru | Parolu qeydə yazmaq, dəyişiklik tarixçəsini saxlamamaq |

**Çoxamilli autentifikasiya** (*multi-factor authentication*, MFA) müxtəlif kateqoriyadan amilləri birləşdirir: **bilinən sirr, sahib olunan vasitə və biometrik xüsusiyyət**. İki fərqli parol eyni kateqoriyadandır və MFA sayılmır. MFA-nın keyfiyyəti üsuldan asılıdır: fişinqə davamlı açar əsaslı üsulla istifadəçinin aldadılıb kod ötürə bildiyi üsul eyni müdafiəni vermir. Hesabın bərpası zəifdirsə, hücumçu əsas giriş yoxlamasını keçmədən hesabı ala bilər.

Autentifikasiyadan sonra tətbiq adətən **sessiya** yaradır. Sessiya identifikatoru oğurlandıqda hücumçu artıq yoxlanmış kimliyin davamını təqlid edə bilər. Buna görə sessiya müddəti, çıxışda ləğv, cihaz və risk siqnalları, həssas əməliyyatda təkrar yoxlama lazımdır. Parolun dəyişməsi ilə bütün tokenlərin avtomatik ləğv olunması fərziyyə kimi qəbul edilmir, tətbiqin faktiki davranışı yoxlanır.

### Rollar, atributlar və audit

**Rol əsaslı giriş nəzarəti** (*role-based access control*, RBAC) icazələri vəzifə rollarına bağlayır: tələbə, tədris əməkdaşı, sistem administratoru. **Atribut əsaslı giriş nəzarəti** (*attribute-based access control*, ABAC) qərara əlavə kontekst daxil edir: fənnə təyinat, semestr, cihazın vəziyyəti, əməliyyatın vaxtı. Sadəcə tədris əməkdaşı olmaq bütün fənlərin nəticəsini dəyişmək hüququ verməməlidir; rol və atribut birlikdə də işlənə bilər.

İcazə **serverdə, hər uyğun sorğu üçün** yoxlanır. Düyməni ekrandan gizlətmək kifayət deyil, istifadəçi sorğunu başqa vasitə ilə göndərə bilər. Uzunömürlü tokendə köhnə rol qalırsa, kadr sistemindəki dəyişiklik dərhal tətbiqə çatmaya bilər. Hüququn verilməsi qədər **vaxtında götürülməsi** də təhlükəsizlik tələbidir.

Aşağıdakı JSON şərti audit nümunəsidir (hesablar, identifikatorlar, vaxt və qiymətlər tədris üçün seçilib; real formatda ayrıca strukturlaşdırılmış hadisə ola bilər):

```json
{"time":"2026-11-08T08:10:00Z","actor":"staff.leyla","action":"grade.update",
 "student_id":142,"course":"NETSEC","old":74,"new":81,"result":"allow","request_id":"r-28"}
```

Bu qeyd dəyişiklik barədə iz verir, amma əməliyyatın qanuni olduğunu özü sübut etmir: düzəlişin təsdiq sənədi və hesabın kimə aid olduğu yoxlanmalıdır. Qeydlər girişə nəzarətlə qorunur, vaxt mənbələri uyğunlaşdırılır, həssas sistemdən ayrıca saxlanır. **Parollar, sessiya sirləri və tam şəxsiyyət sənədləri auditə yazılmır.** Audit anbarının özü də məxfilik və tamlıq tələbi olan aktivdir.

## Təhdidlər, zəifliklər və insidentlər

### Anlayışlar arasındakı səbəb əlaqəsi

| Termin | Mənası |
| --- | --- |
| Təhdid (threat) | Aktivə zərər vura biləcək potensial hadisə və ya şərait. Təhdid mənbəyi onu doğuran subyekt və ya səbəbdir (hücumçu, amma daşqın da) |
| Zəiflik (vulnerability) | Sistemin və ya prosesin zərər üçün istifadə oluna bilən çatışmazlığı |
| Risk (risk) | Həmin şəraitdə baş verə biləcək zərərin ehtimalı və təsiri ilə bağlıdır |
| Hücum (attack) | Təhlükəsizliyi pozmağa yönəlmiş qəsdli cəhd |
| Eksploit (exploit) | Zəiflikdən istifadə üsulu və ya kodu |
| Hadisə (event) | Sistemdə baş verən müşahidə edilə bilən fakt |
| Təhlükəsizlik insidenti (security incident) | Təhlükəsizliyi pozan və ya ona real təhlükə yaradan, cavab tələb edən hadisə və ya hadisələr toplusu |

Texniki nasazlıq əməliyyat insidenti ola bilər; təhlükəsizliklə əlaqəsi ayrıca qiymətləndirilir.

:::note Sadə dillə: konspekt cümlələri
"Server yamanmayıb" **zəiflikdir**, "kimsə bu zəiflikdən istifadə edə bilər" **təhdiddir**, "bu baş versə müştəri bazası sızar və şirkət cərimə ödəyər" isə **riskdir**. Universitetdə: elektron qiymət jurnalı **aktivdir**, müəllimlərin "123456" kimi parolları **zəiflikdir**, öz balını qaldırmaq istəyən tələbə **təhdiddir**, "tələbənin müəllim hesabına girib balı dəyişməsi ehtimalı və nəticəsi" **riskdir**, balın həqiqətən dəyişdirilməsi **insidentdir**, müəllim hesablarında MFA isə **nəzarət tədbiridir** (texniki, inzibati və ya fiziki).
:::

| Termin | Şərti universitet nümunəsi | Qarışdırılmamalı fikir |
| --- | --- | --- |
| Aktiv | Qəbul sənədləri bazası | Aktiv onun server qiyməti ilə məhdudlaşmır |
| Təhdid mənbəyi | Sənədləri oğurlamaq istəyən xarici şəxs | Mənbə ilə zəiflik eyni deyil |
| Zəiflik | İxrac interfeysində icazə yoxlaması yoxdur | Açıq portun özü həmişə zəiflik deyil |
| Hücum | Şəxs icazəsiz ixrac sorğusu göndərir | Uğursuz cəhd də hücum ola bilər |
| Risk | Sənədlərin sızması və hüquqi, əməliyyat zərəri ehtimalı | Risk yalnız proqram xətasının adı deyil |
| Hadisə | Server sorğunu və cavabı qeydə alır | Hər qeyd insident deyil |
| İnsident | İcazəsiz ixrac təsdiqlənir | İnsident qərarı tək xəbərdarlıq sayına bağlanmır |
| Tədbir (control) | Obyekt üzrə icazə, ixrac məhdudiyyəti və audit | Məhsulun alınması tədbirin işlədiyini sübut etmir |

:::exam Tələ: hər hadisə insident deyil
Gündə milyonlarla hadisə (log yazısı) yaranır, onlardan yalnız bir qismi insidentə çevrilir. Bu fərq SIEM mövzusunda (12-ci mövzu) yenə qarşıya çıxacaq.
:::

Zəiflik təhdidin özü deyil. Yanğın ehtimalı server otağında kabel qüsuru olmasa da mövcuddur; yanğın aşkarlayıcısının olmaması isə nəticəni ağırlaşdıra bilər. Xidmətin internetə açılması iş üçün zəruri ola bilər; onun yoxlanılmamış versiyası, zəif konfiqurasiyası və ya həddən artıq hüququ ayrıca zəifliklərdir. **Hər açıq xidməti zəiflik adlandırmaq prioritetləşdirməni korlayır.**

:::figure
src = "m01-3.png"
alt = "Zəiflik, təhdid fəaliyyəti, hadisə və zərər zənciri; tədbirlər və qalıq risk altda."
caption = "Zəiflikdən zərərə gedən risk ssenarisi və tədbirlərdən sonra qalan risk."
:::

### Təhdidlərin təsnifatı

Təhdidlər bir neçə müstəqil meyarla təsnif edilir. Yataqxana istifadəçisinin qəsdən saxta giriş səhifəsi yayması insan mənşəli, qəsdli və aktiv fəaliyyətdir; administratorun marşrut qaydasını səhv silməsi insan mənşəli, amma qəsdsizdir. Avadanlıq nasazlığını həmişə təbii fəlakət kateqoriyasına salmaq dəqiq deyil, texniki səbəbləri ayrıca göstərmək faydalıdır.

| Meyar | Kateqoriyalar | Universitet nümunəsi |
| --- | --- | --- |
| Mənşə | Təbii, texniki və insanla bağlı | Daşqın, disk nasazlığı, hesabdan sui-istifadə |
| Niyyət | Qəsdli və qəsdsiz | Balın saxtalaşdırılması və səhv ixrac |
| Sərhədə münasibət | Daxili və xarici | İşçi hesabından sui-istifadə və kənar hücum |
| Təsir üsulu | Passiv və aktiv | Trafikin dinlənilməsi və saxta paket göndərilməsi |
| Hədəf xassə | Məxfilik, tamlıq və əlçatanlıq (yəni DAD) | Sızma, qiymət dəyişikliyi, xidmət kəsintisi |
| Ehtimal və təsir | Mühit üzrə qiymətləndirilən dərəcələr | Tez-tez baş verən qısa nasazlıq və nadir ağır qəza |
| Zərərin növü | Maddi, əməliyyat, hüquqi və nüfuzla bağlı | Bərpa xərci, imtahanın pozulması, etimad itkisi |

Konspekt əlavə edir: mənbəyə görə **təbii** və **süni**; yerləşməyə görə **daxili** (işçi, podratçı, keçmiş işçi) və **xarici** (hakerlər, cinayətkar qruplar, dövlət dəstəkli qruplar).

Daxili və xarici bölgü seçilmiş sərhəddən asılıdır. Podratçı universitetin əməkdaşı olmasa da imtiyazlı hesabla daxili resurslara giriş əldə edə bilər. Xarici hücumçunun fişinq vasitəsilə işçi hesabını alması avtomatik olaraq daxili aktor demək deyil. **İnsan amili, hesabın növü və hücumçunun mənsubiyyəti ayrı anlayışlardır.** Bu bölgülər üzrə mənbəsiz sabit faizlərdən istifadə etmək olmaz.

**Passiv hücum** məlumatı dəyişmədən müşahidə edir, ona görə izini tapmaq çətin ola bilər; yataqxana trafikinin dinlənilməsinə qarşı qorunan kanal və sertifikat yoxlaması tətbiq olunur. **Aktiv hücum** məlumatı dəyişir və ya resursu tükəndirir; ona qarşı da qabaqlayıcı tədbirlər var: giriş yoxlaması, sürət məhdudiyyəti və seqmentləşdirmə (*segmentation*). Aşkarlama və bərpa həm aktiv, həm passiv hücumun nəticələri üçün planlaşdırılır; bölgü tədbirləri bir-birindən tam ayırmır.

:::tip Yadda saxla (konspekt)
Passiv hücumla **əsasən qarşısını almaqla** (şifrələmə) mübarizə aparılır, çünki onu aşkarlamaq çətindir. Aktiv hücumla isə **aşkarlama və bərpa** ilə (IDS, loglar, ehtiyat nüsxə). Mühazirə bunu dəqiqləşdirir: aktiv hücuma qarşı da qabaqlayıcı tədbirlər var, aşkarlama və bərpa isə hər ikisi üçün lazımdır.
:::

## Riskin qiymətləndirilməsi və idarə edilməsi

### Risk ssenarisinin qurulması

Riskin idarəsi nə baş verə biləcəyini, universitetin hansı işi itirəcəyini və buna qarşı nə etməyin əsaslı olduğunu müəyyən edir. Əvvəl **qiymətləndirmənin sərhədi** seçilir (bütün universitet, tələbə bazası və ya yalnız imtahan cavablarının qəbulu), sonra aktivlər, asılılıqlar, təhdidlər və zəifliklər yazılır. Sərhəd bilinmirsə, eyni risk bir neçə dəfə sayıla, iki xidmət arasındakı boşluq nəzərdən qaça bilər.

Yaxşı risk cümləsi səbəbi nəticəyə bağlayır: *"İxrac interfeysində obyekt üzrə icazə yoxlanmadığı üçün tələbə hesabından başqa şəxslərin sənədləri çıxarıla və fərdi məlumat sızması baş verə bilər."* Burada zəiflik, mümkün fəaliyyət və zərər ayrıdır. "Kiberrisk yüksəkdir" cümləsi tədbir seçmək üçün az məlumat verir. Aktivin sahibi mümkün zərəri, texniki komanda ssenarinin baş vermə yolunu qiymətləndirir.

Sadə keyfiyyət qiymətləndirməsində **risk balı = ehtimal balı × təsir balı**; şərti olaraq hər biri 1-dən 5-ə qədər. Ehtimal "bu nə qədər tez-tez baş verə bilər", təsir "baş versə nə qədər ziyan olar" sualına cavabdır. Bu, dəqiq ehtimal hesabı deyil: üç bal iki baldan bir yarım dəfə böyük real ehtimalı bildirmir. Şkala prioritet seçməyə kömək edir; kateqoriyaların mənası əvvəlcədən yazılır, eyni hasilli iki ssenarinin cavabı fərqli ola bilər.

| Ssenari | Ehtimal | Təsir | Hasil | İlkin qərar |
| --- | --- | --- | --- | --- |
| Qəbul sənədlərinin icazəsiz ixracı | 4 | 5 | 20 | İxrac yolunu məhdudlaşdırmaq |
| Kitabxana kataloqunda qısa nasazlıq | 4 | 2 | 8 | Ucuz bərpa tədbirini qiymətləndirmək |
| Yeganə server otağında ağır yanğın | 1 | 5 | 5 | Ayrı məkanda bərpanı planlaşdırmaq |
| İmtahan zamanı identifikasiya xidmətinin dayanması | 3 | 5 | 15 | Asılılığı və ehtiyat rejimi yoxlamaq |

:::note Konspektdəki risk xəritəsi
Ehtimal və təsir 1–5 şkalasında xəritəyə qoyulur. **A** zonası: ehtimal da, təsir də yüksək, ilk növbədə azaldılır. **B**: nadir, amma dağıdıcı (məsələn zəlzələ), çox vaxt sığorta ilə ötürülür. **C**: tez-tez, amma xırda, çox vaxt qəbul edilir.
:::

Yanğın ssenarisinin hasilinin aşağı olması onu nəzərə almamağa əsas vermir: qəbul edilən maksimum itki, insan təhlükəsizliyi və hüquqi tələblər ayrıca məhdudiyyət yaradır. Ehtimalın qiymətləndirilməsində məlumat mənbəyi göstərilir (əvvəlki nasazlıqlar, arxitektura baxışı, test nəticələri, ekspert rəyi). Dəlil zəifdirsə, **qeyri-müəyyənlik də yazılır**; rəqəm qeyri-müəyyənliyi gizlətmək üçün işlədilmir.

**Kəmiyyət yanaşmasında** gözlənilən itki hesablana bilər. Şərti nümunə: bir kəsintinin orta zərəri 2 000 AZN, illik gözlənilən tezliyi üçdür, deməli illik gözlənilən itki 3 × 2 000 = 6 000 AZN. İllik 1 500 AZN-lik tədbirin tezliyi birə endirəcəyi əsaslandırılıbsa, qalan gözlənilən itki 2 000 AZN, tədbirlə birlikdə cəmi 3 500 AZN olar. Bu, müqayisə üçün faydalıdır, lakin nadir böyük itkiləri və pulla çətin ölçülən akademik zərəri tam əhatə etmir; fərziyyələrin doğruluğu qərardan sonra da izlənir.

### Riskə cavab və məsuliyyət

Riskə dörd əsas cavab var. Seçim avtomatik düsturla edilmir: universitet hansı nəticəni qəbul edə bilər, tədbir nə qədər iş yükü yaradır və hansı hüquqi öhdəlik qalır sualları birlikdə nəzərdən keçirilir.

| Strategiya | Mənası | Universitet nümunəsi və məhdudiyyət |
| --- | --- | --- |
| Azaltmaq (mitigate) | Ehtimalı və ya təsiri aşağı salmaq | MFA, ixrac nəzarəti və bərpa nüsxəsi; risk tam yox olmur |
| Yayınmaq (avoid) | Riski yaradan fəaliyyəti dayandırmaq | Lazımsız açıq fayl paylaşımını bağlamaq; alternativ iş prosesi lazımdır |
| Ötürmək və ya bölüşmək (transfer) | Maliyyə nəticəsinin və işin müəyyən hissəsini müqavilə ilə bölüşmək | Sığorta və xidmət müqaviləsi (kiber sığorta, autsorsinq); məlumat sahibinin məsuliyyəti avtomatik itmir |
| Qəbul etmək (accept) | Qalan riski səlahiyyətli qərarla saxlamaq | Az təsirli kataloq kəsintisi üçün sənədləşdirilmiş qərar; baxış tarixi olmalıdır |

Tədbirlərdən əvvəlki risk **ilkin risk**, tədbirlərdən sonra qalan hissə **qalıq risk** (*residual risk*) adlanır. Sıfır risk yoxdur; məqsəd riski təşkilatın qəbul edə biləcəyi səviyyəyə endirməkdir. Qalıq riskin sahibi müəyyən olmalıdır: texniki administratorun "belə qalacaq" deməsi rəhbərlik səviyyəsində qəbul qərarını əvəz etmir. Qərarda ssenari, tədbirlər, qalan təsir, məsul şəxs və təkrar baxış şərti yazılır. İmtahan sayının və xidmət yükünün artması əvvəlki qəbul qərarını yenidən qiymətləndirməyi tələb edə bilər.

**Risk reyestri** (*risk register*) qərarların yaddaşıdır: hər sətirdə aktiv, ssenari, qiymətləndirmə əsası, tədbir sahibi, son tarix və qalıq risk göstərilir. Universitet yalnız risk siyahısı hazırlayıb tədbirin işlədiyini yoxlamırsa, reyestr formal sənədə çevrilir. Ehtiyat nüsxə yazıldığı barədə hesabatın yanında **uğurlu bərpa sınağı**, ixrac nəzarətinin yanında icazəsiz sorğunun rədd edildiyini göstərən nəticə saxlanmalıdır.

## Təhlükəsizliyin layihələndirmə prinsipləri

### Minimum səlahiyyət və vəzifələrin ayrılması

**Minimum səlahiyyət** (*least privilege*) subyektə işi üçün lazım olan hüququ, lazım olan resursda və lazım olan müddətə verməkdir. Kitabxana əməkdaşının kataloq qeydini düzəltməsi üçün tələbə bazasının ehtiyat nüsxəsini silmək hüququ lazım deyil. Xidmət hesabına da eyni prinsip tətbiq olunur: LMS-in gündəlik baza hesabı bütün bazaları idarə edən hesab olmamalıdır. Hücumçu tətbiqi ələ keçirəndə zərər hesabın hüquqları ilə məhdudlaşır.

Prinsip ilkin quraşdırmadan sonra da işləməlidir: müvəqqəti layihə hüquqları bitmə tarixi ilə verilir, işdən ayrılan əməkdaşın hesabı ləğv edilir, köhnə qrup üzvlükləri nəzərdən keçirilir. Hüquq baxışında hesabın real işi və istifadə etdiyi resurslar tutuşdurulur; əks halda hüquqlar yığılır. İmtiyazlı əməliyyat üçün ayrıca hesab gündəlik poçt istifadəsi ilə inzibati işi ayırmağa kömək edir.

**Vəzifələrin ayrılması** (*separation of duties*) kritik əməliyyatın bütün mərhələlərini bir subyektin nəzarətində saxlamamağı tələb edir. Təqaüd ödənişində siyahını hazırlayan şəxs yekun bank faylını təkbaşına təsdiq etməməlidir; qiymət düzəlişində müraciət, təsdiq və icra rolları ayrılır. İki düymə əlavə etmək kifayət deyil: eyni hesab hər ikisini basa bilirsə, ayrılma yoxdur. Təsdiqləyən şəxs də nəyi təsdiqlədiyini görə bilməlidir.

### Dərinlik üzrə müdafiə və təhlükəsiz imtina

**Dərinlik üzrə müdafiə** (*defense in depth*) bir tədbirin uğursuzluğunun bütün müdafiəni dağıtmamasıdır. İmtahan bazası şəbəkə seqmenti ilə ayrılır, tətbiqdə icazə yoxlanır, baza hesabının hüquqları məhdudlaşdırılır, dəyişikliklər auditə yazılır. Bu qatların işi fərqlidir: eyni yanlış icazə siyahısını üç yerdə təkrarlamaq müstəqil müdafiə yaratmaya bilər. **Ortaq açar, ortaq administrator və ortaq enerji mənbəyi gizli asılılıq** yaradır.

**Təhlükəsiz imtina** (*fail-secure*) nasazlıq zamanı qorunan resursa girişin nəzarətsiz açılmamasıdır. Qiymət dəyişdirmə xidməti icazə serverinə çata bilmirsə, dəyişiklik sorğusunu rədd etməlidir. Əvvəlcədən təsdiqlənmiş məhdud ehtiyat rejim ola bilər, amma ayrıca qaydaya və auditə bağlanır; xəta yarananda bütün istifadəçiləri administrator saymaq qəbuledilməzdir.

İnsan təhlükəsizliyinə xidmət edən **fail-safe** anlayışı ilə fərqi nəzərə alınır: yanğın çıxışı enerji kəsiləndə insanı içəridə saxlamamalıdır, lakin bu fiziki tələb qiymət bazasına nəzarətsiz giriş vermək tələbini yaratmır. Layihədə hansı təhlükənin üstün olduğu əvvəlcədən müəyyən edilir, istisna rejimlərin kimə xəbər verdiyi və nə vaxt bitdiyi yazılır.

| Prinsip | Düzgün tətbiq | Tez rast gəlinən qüsur |
| --- | --- | --- |
| Minimum səlahiyyət | LMS hesabı yalnız lazım olan cədvəllərə işləyir | Bütün tətbiqlərdə eyni inzibati hesab var |
| Vəzifələrin ayrılması | Qiymət düzəlişini ayrı səlahiyyətli şəxs təsdiqləyir | Hazırlayan öz müraciətini təsdiqləyir |
| Dərinlik üzrə müdafiə | Şəbəkə, tətbiq və baza ayrı yoxlama aparır | Bütün qatlar eyni geniş istisnaya əsaslanır |
| Təhlükəsiz imtina | İcazə yoxlanmırsa yazma rədd olunur | Xəta zamanı nəzarət söndürülür |
| Tam vasitəçilik (complete mediation) | Hər həssas əməliyyat üzrə icazə yoxlanır | Yalnız giriş səhifəsində yoxlama var |
| Hücum səthinin azaldılması (attack surface reduction) | İşlənməyən xidmət və hesablar bağlanır | Sınaq interfeysi əsas sistemdə açıq qalır |

### Sıfır etibar yanaşması

**Sıfır etibar** (*zero trust*) şəbəkədəki yerə və ya resursun universitetə məxsus olmasına əsasən avtomatik etimad verməyən yanaşmadır. NIST SP 800-207 bu yanaşmanı resurslara giriş qərarı ətrafında təsvir edir. Qərara istifadəçi kimliyi, cihaz vəziyyəti, resursun həssaslığı və sessiya konteksti daxil ola bilər. Daxili IP ünvanından gələn sorğu özlüyündə etibarlı sayılmır.

Kafedra noutbuku universitet Wi-Fi şəbəkəsindədir, bu fakt ona əməkhaqqı bazasına giriş vermir: istifadəçi uyğun rol daşımalı, cihaz müəyyən edilmiş vəziyyətə uyğun olmalı, sorğu icazəli əməliyyata aid olmalıdır. İcazə məhdud sessiya üçün verilir, risk dəyişəndə yenidən qiymətləndirilir.

Sıfır etibar bir məhsulun və ya VPN-in başqa adı deyil. Məlumat inventarı, kimlik idarəsi və xidmətlər arasındakı əlaqə bilinmirsə, yalnız giriş proksisi almaq yanaşmanı tamamlamır. Köhnə tətbiq cihaz kontekstini qəbul etmirsə, onun qarşısında nəzarət nöqtəsi və məhdud şəbəkə yolu qurula bilər, qalan boşluq risk kimi sənədləşdirilir. Mərhələli keçid üçün əvvəl **həssas xidmət və imtiyazlı giriş** seçmək əsaslıdır.

## Məlumatların təsnifatı və həyat dövrü

**Məlumatların təsnifatı** (*data classification*) məzmunu həssaslığına və iş tələbinə görə qruplaşdırır. Səviyyələrin adları təşkilatın siyasətindən asılıdır, universal dörd pillə yoxdur; aşağıdakı bölgü şərti universitet modelidir. Məxfilik etiketi əlçatanlıq və tamlıq tələblərini ayrıca qiymətləndirməyə mane olmamalıdır.

| Səviyyə | Nümunə | İcazəli istifadə | Qoruma qaydası |
| --- | --- | --- | --- |
| Açıq | Dərc olunmuş qəbul qaydası | Hamı oxuya bilər | Dərc hüququ və məzmun tamlığı qorunur |
| Daxili | Kafedranın işçi iclas planı | Müvafiq əməkdaşlar | Daxili paylaşım və giriş nəzarəti |
| Məxfi | Tələbə qiymətləri və şəxsi əlaqə məlumatları | Vəzifəsi üzrə ehtiyacı olanlar | Obyekt üzrə icazə, şifrələmə və audit |
| Ciddi məhdud | İmtahan sualları və imza açarları | Ayrıca təsdiqlənmiş dar qrup | Güclü giriş nəzarəti, ayrıca saxlama və əməliyyat təsdiqi |

**Məlumat sahibi** (*data owner*) istifadə məqsədini və qoruma tələbini müəyyən edir. **Texniki saxlayıcı** (*custodian*) bu tələbi sistemdə tətbiq edir: tədris hissəsi qiymət məlumatının kimə lazım olduğunu müəyyən edə, İT bölməsi icazəni qura bilər. İT administratorunun texniki çıxış imkanı məzmunu istənilən məqsədlə oxumaq hüququ demək deyil; saxlayıcının imtiyazlı əməliyyatları da nəzarətə alınır.

Təsnifat məlumat yarananda təyin edilir, sonrakı nüsxələrə və ixraclara daşınır. İmtahan sualı imtahandan əvvəl ciddi məhdud, rəsmi dərcdən sonra açıq ola bilər; fərdi qiymət məlumatı imtahan bitəndə avtomatik açıq olmur. Etiketin dəyişməsi səlahiyyətli qərar tələb edir. Dövlət sirri kimi hüquqi kateqoriyalar adi daxili etiketlə əvəz edilmir.

Məlumat üç vəziyyətdə olur: **sükunətdə** (*data at rest*, diskdə və ya arxivdə), **ötürülərkən** (*data in transit*, şəbəkə ilə daşınır) və **istifadədə** (*data in use*, işləyən prosesin yaddaşında emal edilir). Tələbə siyahısı serverdə şifrəli saxlanıb TLS ilə göndərilə bilər, lakin əməkdaşın ekranında və ixrac etdiyi faylda açıq görünür. Təhlükəsizlik yalnız ilk iki vəziyyətə baxsa, istifadə mərhələsi boş qalar.

| Mərhələ | Universitetdə görülən iş | Yoxlama sualı |
| --- | --- | --- |
| Toplama və yaratma | Lazım olan sahələr və məqsəd müəyyən edilir | Bu məlumat həqiqətən lazımdırmı? |
| Saxlama | Etiket, icazə və ehtiyat nüsxə qurulur | Bütün nüsxələr inventardadırmı? |
| İstifadə | Rol və obyekt üzrə icazə tətbiq edilir | Əməkdaş yalnız işi üçün lazım olan hissəni görürmü? |
| Ötürmə və paylaşma | Alıcı və kanal yoxlanır | Keçid sonradan başqasına açılırmı? |
| Arxivləşdirmə | Müddət, format və bərpa qaydası yazılır | Açar və oxuma vasitəsi qalacaqmı? |
| Silinmə | Əsas nüsxə və törəmə nüsxələr üzrə qayda işləyir | Ehtiyat nüsxələr üçün müddət necə tətbiq olunur? |

Sadəcə faylı silmək bütün daşıyıcılarda etibarlı məhv etmə deyil; saxlanma texnologiyası və daşıyıcının xüsusiyyəti nəzərə alınmalıdır. Şifrəli daşıyıcıda açarın məhvi uyğun şərtlərlə istifadə edilə bilər, lakin bütün açar nüsxələrinin nəzarətdə olması lazımdır. Arxiv müddətini məqsədsiz uzatmaq riskin əhatəsini böyüdür. Müddət bitəndə silinmə ilə hüquqi saxlanma tələblərinin toqquşması məlumat sahibi və hüquq xidməti ilə həll olunur.

## OSI və TCP/IP modellərinə təhlükəsizlik baxışı

### Səviyyələr və etibar sərhədləri

Açıq sistemlərin qarşılıqlı əlaqə modeli (*Open Systems Interconnection*, OSI) rabitə funksiyalarını **yeddi** səviyyəyə ayırır. TCP/IP modeli praktik internet protokollarını adətən **dörd** səviyyədə qruplaşdırır: kanal, internet, nəqliyyat və tətbiq. Bu bölgülər funksiyanı anlamaq üçündür; təhlükəsizlik vasitəsini mütləq yalnız bir səviyyəyə bağlamaq doğru deyil. TLS kimi protokolun funksiyaları OSI-nin yuxarı səviyyələri ilə əlaqələndirilə bilər, lakin real yığın həmin sərhədləri hər yerdə ayrıca modul kimi saxlamır.

Şərti nümunə: tələbə `lms.unec.example` ünvanına daxil olur; cihazın ünvanı 10.20.14.8, açıq xidmətin ünvanı 203.0.113.20 olsun. Tətbiq sorğusu TCP, IP və kanal başlıqları ilə daşına bilər; bu proses **kapsullaşdırma** (*encapsulation*) adlanır. Hər başlıq fərqli qərara xidmət edir: kanal qonşuya çatdırmanı, IP şəbəkələrarası yolu, nəqliyyat portu xidmətə yönəlməni dəstəkləyir. **Başlıqdakı ünvan istifadəçinin kimliyinin sübutu deyil.**

| OSI səviyyəsi | TCP/IP qarşılığı | Təhdid nümunəsi | Universitetdə tədbir |
| --- | --- | --- | --- |
| 7. Tətbiq | Tətbiq | İcazəsiz qiymət sorğusu, inyeksiya | Obyekt üzrə icazə və giriş yoxlaması |
| 6. Təqdimat | Tətbiq | Kodlaşdırmanın səhv emalı | Vahid format, ölçü və tip yoxlaması |
| 5. Sessiya | Tətbiq | Sessiya identifikatorunun oğurlanması | Token qorunması, müddət və ləğv |
| 4. Nəqliyyat | Nəqliyyat | Bağlantı resurslarının tükənməsi | Vəziyyət izləmə və bağlantı məhdudiyyəti |
| 3. Şəbəkə | İnternet | Saxta IP və yanlış marşrut | Giriş filtrləri, marşrut nəzarəti və IPsec |
| 2. Kanal | Kanal | ARP saxtalaşdırması, icazəsiz qoşulma | Port nəzarəti və uyğun kommutator müdafiəsi |
| 1. Fiziki | Kanal | Kabelin kəsilməsi, avadanlığın götürülməsi | Fiziki giriş və enerji qorunması |

:::figure
src = "m01-4.png"
alt = "Cihaz, Wi-Fi, firewall, tərs proksi, LMS və baza: hər nöqtə başqa sualı yoxlayır."
caption = "Universitet xidmətinə gedən yol və ayrı nöqtələrdə aparılan təhlükəsizlik yoxlamaları."
wide = true
:::

OSI cədvəli hücumun bütün nəticəsini bir səviyyədə həbs etmir. ARP saxtalaşdırması kanal səviyyəsindən başlaya bilər, ardınca trafikin tutulması və saxta səhifə ilə parol oğurlanması baş verə bilər; tətbiqdə oğurlanmış hesabla qiymət dəyişməsi başqa səviyyədə görünər. Təhlildə **başlanğıc mexanizmi, müşahidə nöqtəsi və zərər** ayrı göstərilir. Şəbəkə sensoru tətbiqdəki bütün icazə qərarlarını görə bilməz.

### Protokollar və müdafiənin sərhədləri

**TCP** axının ardıcıllığını və itirilmiş hissələrin yenidən ötürülməsini dəstəkləyir, kriptoqrafik məxfilik və mənbə autentikliyi vermir. **UDP** də özlüyündə bu xassələri vermir; qoruma yuxarıdakı protokoldan asılıdır. **IP** paketi marşrutlaşdırır, mənbə ünvanının həqiqi istifadəçiyə aid olduğunu təsdiqləmir. Firewall-da IP-yə icazə vermək tətbiqdə tələbə kimliyini yoxlamağın əvəzi deyil.

**TLS** tətbiq məlumatının ötürülməsində məxfilik və tamlıq qoruması, sazlamadan asılı olaraq serverin və müştərinin autentifikasiyasını verir. Server sertifikatının etibar zənciri və ad uyğunluğu yoxlanmalıdır; sertifikat xətasını görməzliyə vurmaq saxta serverə qoşulma riskini artırır. TLS 1.3 üçün 2026-cı ilin iyulunda dərc edilmiş **RFC 9846** əsas sənəddir; əvvəlki mənbələr **RFC 8446**-ya istinad edir. TLS sessiyası istifadəçinin universitet daxilindəki vəzifəsini müəyyən etmir.

**IPsec** şəbəkə səviyyəsində qorunan rabitə qura bilər. Wi-Fi qoruması cihazla giriş nöqtəsi arasındakı hissəni qoruyur: tələbə qorunan Wi-Fi-a qoşulsa da tətbiqə qədər sonrakı yol ayrıca qorunmalıdır. **VPN** istifadəçini şəbəkəyə bağlayır, amma yoluxmuş noutbuku avtomatik təmizləmir. Bir hissədə qurulan qorumanın sərhədi bütün əlaqə ilə eyniləşdirilmir.

| Protokol və ya vasitə | Nəyi edir | Nəyi özlüyündə etmir |
| --- | --- | --- |
| DNS | Adı ünvana uyğunlaşdırır | Adi DNS cavabı məlumatı məxfi saxlamır |
| DNSSEC | DNS məlumatının mənşəyini və tamlığını yoxlamağa imkan verir | Sorğunu şifrələmir və saytın məzmununu qiymətləndirmir |
| TLS | Tətbiq əlaqəsini qoruyur | Obyekt üzrə biznes icazəsini müəyyən etmir |
| Firewall | Trafiki siyasətə uyğun buraxır və ya rədd edir | Hər qiymət dəyişikliyinin əsasını yoxlamır |
| VLAN | Kanal səviyyəsində məntiqi ayrılma yaradır | Marşrutlaşdırılan zonalararası trafiki avtomatik qadağan etmir |
| NAT | Ünvan çevrilməsi aparır | Giriş siyasəti və tətbiq nəzarətini əvəz etmir |

**Seqmentləşdirmə** universitet şəbəkəsini iş funksiyalarına görə ayırır: yataqxana Wi-Fi, kafedra cihazları, açıq xidmət zonası, məlumat bazası və idarəetmə şəbəkəsi fərqli sərhədlərdir. Zonalararası keçidi firewall qaydaları müəyyən edir. Bazanın VLAN-da olması təkbaşına kifayət etmir: tələbə şəbəkəsindən ona bütün trafik buraxılırsa, ayrılmanın faydası azalır. Qaydalar mənbə, hədəf, xidmət və iş əsasına görə yazılır.

DNS sorğuları ənənəvi olaraq UDP və TCP 53-dən, HTTPS çox vaxt TCP 443-dən istifadə edir; HTTP/3 isə QUIC üzərindən UDP ilə işləyə bilər. **Port nömrəsi tətbiqin kimliyini sübut etmir**: hücumçu icazəli portdan başqa məzmun ötürə bilər, tətbiq də qeyri-standart portda işləyə bilər. Qərar yalnız porta deyil, xidmət inventarına, kimliyə və əməliyyat kontekstinə bağlanır.

## Tanınmış hadisələrin CIA üzrə təhlili

### Equifax, 2017: məxfilik

2017-ci ildə **Equifax**-da fərdi məlumatların böyük həcmdə sızması məlum oldu. Hücum yolunda **Apache Struts** zəifliyi və yamağın vaxtında tətbiq edilməməsi vardı. Əsas təhlil istiqaməti **məxfiliyi**dir: sistem işləməyə davam etsə də məlumat icazəsiz çıxarılıb. Sızma xidmətin dayanmasını tələb etmir, buna görə yalnız serverin işləkliyini ölçmək məxfiliyə nəzarət deyil.

Universitetlə müqayisədə: açıq portal komponenti aktiv inventarında görünmürsə, yamaq qərarı icraya çatmaya bilər. Dərs inventar, yamaq məsuliyyəti və bazaya girişin məhdudlaşdırılmasıdır. **"Yamaq buraxılıb" faktı "universitetdə tətbiq edilib və yoxlanıb" faktından fərqlidir.** Sızmanın qarşısı üçün çıxış və kütləvi oxuma fəaliyyətinin görünməsi də lazımdır.

### Stuxnet: tamlıq

2010-cu ildə aşkar edilmiş **Stuxnet** sənaye idarəetmə sistemlərini hədəfləyən zərərli proqramdır. O, müəyyən idarəetmə mühitində proqram məntiqini dəyişə və operatorun gördüyü mənzərəni aldadıcı edə bilirdi. Tamlıq burada sənəd və baza sətrindən fiziki prosesin idarəetməsinə qədər uzanır: ekrandakı normal göstərici altdakı prosesin doğru işlədiyini sübut etmir.

Laboratoriyanın ventilyasiya və ya təcrübə avadanlığını idarə edən proqram üçün oxşar sual verilir: idarəetmə parametri icazəsiz dəyişsə, bunu müstəqil hansı ölçmə görəcək? Dərs idarəetmə məntiqinin yoxlanması, dəyişiklik təsdiqi və **müstəqil müşahidədir**. Stuxnet-i adi veb-sayt pozuntusu kimi təqdim etmək fiziki nəticə tərəfini itirər; bu nümunə hər universitet şəbəkəsinə eyni hücumun tətbiq ediləcəyi iddiası deyil.

### WannaCry, 2017: əlçatanlıq

**WannaCry** 2017-ci ilin mayında Windows sistemlərində yayılan və faylları şifrələyən ransomware idi. Yayılmada **SMB** zəifliklərindən istifadə olunurdu; Microsoft-un **MS17-010** təhlükəsizlik yeniləməsi hadisədən əvvəl dərc edilmişdi. Faylların açılmaması və xidmətlərin dayanması **əlçatanlıq** itkisini aydın göstərir; icazəsiz şifrələmə tamlığa da toxunur. Hadisəni izah etmək üçün sübutsuz məlumat oğurlanması iddiası əlavə edilməməlidir.

Universitet üçün dərs yamaq, lazımsız SMB əlaqələrinin bağlanması, seqmentləşdirmə və bərpa sınağıdır. Yataqxana cihazından inzibati fayl serverlərinə sərbəst keçid varsa, bir cihazın yoluxması daha geniş nəticə verə bilər. Təmiz və yoxlanmış ehtiyat nüsxə zərəri azalda bilər, lakin əvvəl hücumun davam edən yolu bağlanmalıdır.

| Hadisə | Əsas CIA baxışı | Universitet üçün yoxlama | Yanlış nəticə |
| --- | --- | --- | --- |
| Equifax, 2017 | Məxfilik | İnventar, yamaq və məlumat çıxışı | Portal işləyirsə sızma yoxdur |
| Stuxnet, 2010-cu ildə aşkarlanıb | Tamlıq | İdarəetmə dəyişiklikləri və müstəqil ölçmə | Normal ekran doğru prosesi sübut edir |
| WannaCry, 2017 | Əlçatanlıq, həmçinin tamlıq | Yayılma sərhədi və bərpa imkanı | Tək təhlükəsizlik məhsulu bütün zərəri dayandırır |

## İnformasiya əldə etmək hüququ və təhlükəsizliyin idarə edilməsi

### Açıqlıqla qorumanın uzlaşdırılması

İnformasiya əldə etmək hüququ ilə məxfilik tələbi birlikdə nəzərə alınmalıdır. Qəbul qaydasını açıq dərc etmək ilə tələbələrin fərdi sənədlərini açıq saxlamaq fərqli qərarlardır. İnformasiyanın qorunması bütün məlumatı gizlətmək üçün əsas deyil: açıq məlumatın düzgün və əlçatan yayımlanması da təhlükəsizlik məqsədidir. Məhdudiyyət hüquqi əsas və məlumatın xüsusiyyəti ilə bağlı olmalıdır.

Azərbaycanda bu mövzu üçün adları dəqiq olan hüquqi mənbələr: **"İnformasiya əldə etmək haqqında"**, **"Fərdi məlumatlar haqqında"**, **"İnformasiya, informasiyalaşdırma və informasiyanın mühafizəsi haqqında"** və **"Elektron imza və elektron sənəd haqqında"** qanunlardır. Mühazirədə onların bütün tətbiq şərtləri sadalanmır; konkret prosesdə məlumatın növü, tərəflərin statusu və qüvvədə olan hüquqi tələblər ayrıca yoxlanır. Xarici ölkənin istənilən qanununu bütün Azərbaycan universitetlərinə avtomatik tətbiq etmək düzgün deyil.

**İnformasiya sorğusu** məlumat almaq üçün müraciətdir. **İnformasiyanın açıqlanması** sorğu gözləmədən rəsmi resursda və ya başqa uyğun vasitə ilə yayılmasıdır. **İnformasiya xidməti** sorğu sahibinə məlumat çatdıran fəaliyyətdir. **Sənədləşdirilmiş informasiya** daşıyıcıda mətn, səs və ya təsvir kimi qeydə alınıb tanınmasına imkan verən rekvizitlər daşıyır. Elektron sənədin ünvanı və versiyası bilinmirsə, hansı məzmunun rəsmi cavab olduğu qarışa bilər.

**Fərdi məlumat** şəxsi birbaşa və ya dolayı tanımağa imkan verə bilər. Tələbənin adını silmək hər zaman anonimləşdirmə deyil: kiçik qrup, nadir təqaüd kateqoriyası və dəqiq tarix birlikdə şəxsi tanıda bilər. Kafedra hesabatında yalnız qrup və xüsusi sağlamlıq güzəşti göstərilibsə və qrupda həmin güzəştli bir nəfər varsa, adın olmaması şəxsin müəyyən edilməsini dayandırmaya bilər. Dərc qərarı **birləşmə riskini** də nəzərə almalıdır.

Sorğuya cavabda açıq hissə ilə məhdud hissə ayrılır: tədqiqatçı ümumi qəbul statistikasını istəyirsə, abituriyentlərin sənəd skanlarını göndərmək məqsədə uyğun deyil, kiçik qrupların detalları ayrıca qiymətləndirilir. Rəsmi kanal, versiya və məsul şəxs qeyd edilir.

### İdarəetmə, milli kontekst və ölçmə

Azərbaycanda 2003–2012-ci illəri əhatə edən İKT üzrə Milli Strategiya və "Azərbaycan 2020: gələcəyə baxış" İnkişaf Konsepsiyası rəqəmsal xidmətlərin genişlənməsinin tarixi sənədlərindəndir; onların müddətlərini hazırkı fəaliyyət proqramı kimi təqdim etmək olmaz. Universitet baxımından bu istiqamətlər elektron xidmət, informasiya əlçatanlığı, mütəxəssis hazırlığı və təhlükəsiz istifadəyə ehtiyacla əlaqələnir.

Milli səviyyədə koordinasiya, təhdid məlumatlarının toplanması və təhlili, maarifləndirmə və metodiki dəstək universitetin daxili təhlükəsizlik işindən fərqli funksiyalardır. Əvvəlki mənbələrdə Elektron Təhlükəsizlik Mərkəzi və Elektron Təhlükəsizlik Xidməti adları işlənir; **2 iyun 2026-cı il** dəyişikliklərindən sonra **Milli Kibertəhlükəsizlik Agentliyi** adı nəzərə alınmalıdır. Dövlət orqanlarının xüsusi rabitəsi və informasiya təhlükəsizliyi sahəsində **Xüsusi Rabitə və İnformasiya Təhlükəsizliyi Dövlət Xidməti** ayrıca qurumdur. Tarixi adlarla cari əlaqə planı qurmaq düzgün deyil.

Universitetin əlaqə planı aidiyyəti qurumu xidmətin statusuna və insidentin xarakterinə görə müəyyən edir; məqsəd kimə, hansı məlumatla və hansı kanalla müraciət ediləcəyini əvvəlcədən bilməkdir. Mübadilə üçün insidentin vaxtı, təsirlənən xidmət, faktlar və görülən tədbirlər hazırlanır; başqa tələbələrin məlumatı lazımsız yayılmır. **Koordinasiya universitetin öz sisteminə cavabdehliyini aradan qaldırmır.**

İdarəetmə üçün standartlar:

| Standart | Nə verir |
| --- | --- |
| ISO/IEC 27001:2022 | İnformasiya təhlükəsizliyi idarəetmə sisteminin tələbləri |
| ISO/IEC 27002:2022 | Tədbirlər üzrə rəhbərlik; 93 tədbir təşkilati, insan, fiziki və texnoloji mövzular üzrə qruplaşdırılır |
| ISO/IEC 27005:2022 | Riskin idarəsi |
| NIST CSF 2.0 (fevral 2024) | Altı funksiya: idarəetmə (Govern), müəyyənləşdirmə (Identify), qoruma (Protect), aşkarlama (Detect), cavab (Respond), bərpa (Recover) |
| NIST SP 800-61 Rev. 3 (aprel 2025) | İnsidentə cavabı CSF 2.0 çərçivəsi ilə əlaqələndirir |

Bu siyahı hər universitetin bütün tədbirləri eyni şəkildə tətbiq etməsi demək deyil: tətbiq sahəsi və risk əsası yazılmalıdır, sertifikat da hər insidentin mümkünsüzlüyünə zəmanət deyil. CSF funksiyaları **sərt ardıcıl mərhələlər deyil**: imtahan xidməti işləyərkən risk idarəsi, monitorinq və bərpa hazırlığı paralel davam edir.

Təhlükəsizlik səviyyəsini yalnız məhsul sayı və ya xəbərdarlıq həcmi ilə ölçmək olmaz. Daha mənalı göstəricilər: yamağı vaxtında yoxlanmış kritik xidmətlərin payı, icazə baxışının tamamlanması və bərpa sınağının nəticəsi. Milli indekslərdə də tərkib göstəriciləri və çəkilər bilinməlidir; mürəkkəb indeksdə bir sahənin yüksək balı başqa sahədəki zəifliyi gizlədə bilər. **Reytinqdə yer tutmaq konkret universitetin tələbə bazasının qorunduğunu sübut etmir.**

## Universitet xidməti üçün tələblərin hazırlanması və yoxlanması

### Tələbdən müşahidə edilən nəticəyə

Şərti olaraq universitet `imtahan.unec.example` xidmətini istifadəyə hazırlayır. Əvvəl iş prosesi təsvir edilir: tələbə kimliyini təsdiq edir, ona təyin edilmiş imtahanı açır, cavab göndərir və qəbul təsdiqi alır; tədris əməkdaşı nəticəni qiymətləndirir, səlahiyyətli komissiya əsaslandırılmış düzəlişi təsdiqləyir. Bu xəritə olmadan "portal təhlükəsiz olmalıdır" tələbi yoxlanıla bilmir. Hər keçiddə məlumat, subyekt və icazə müəyyən edilir.

- **Məxfilik tələbi:** tələbə başqa şəxsin cavabını və nəticəsini ala bilməməlidir.
- **Tamlıq tələbi:** qəbul edilmiş cavabın sonrakı dəyişiklikləri versiya və səlahiyyətlə əlaqələndirilməlidir.
- **Əlçatanlıq tələbi:** gözlənilən yük və qəbul edilən gecikmə proses sahibi ilə müəyyən edilməlidir.

Konkret hədlər şərti sınaq mühitində ölçülür; təsadüfi seçilmiş rəqəm universitetin real gücünü göstərmir. İmtahan zamanı identifikasiya xidmətinin dayanması da sınaq ssenarisinə daxil edilir.

| Məqsəd | Qeyri-dağıdıcı yoxlama | Qəbul meyarı |
| --- | --- | --- |
| Məxfilik | Sınaq tələbəsi başqa sınaq tələbəsinin obyektini istəyir | Server sorğunu rədd edir, həssas məzmun qaytarmır |
| Tamlıq | Təsdiqsiz rol qiymət düzəlişi göndərir | Əməl rədd edilir və cəhd auditə yazılır |
| Hesabatlılıq | Təsdiqli düzəlişin qeyd zənciri izlənir | Hesab, versiya, vaxt və qərarın əsası tapılır |
| Əlçatanlıq | Ayrılmış mühitdə razılaşdırılmış yük ölçülür | Proses sahibinin təsdiq etdiyi hədlər ödənir |
| Bərpa | Sınaq nüsxəsi təcrid olunmuş mühitə qaytarılır | Məzmun və xidmət razılaşdırılmış RTO və RPO-ya uyğundur |
| Hüququn götürülməsi | Rol ləğv ediləndən sonra əvvəlki sessiya yoxlanır | İmtiyaz müəyyən edilmiş müddətdə qüvvədən düşür |

Yerli Linux serverində aşağıdakı oxu əmrləri xidmət inventarını yoxlamağa kömək edir (imtiyazdan və konfiqurasiyadan asılı olaraq görünən məlumat fərqlənə bilər; əmrlər özlüyündə icazəsiz giriş və ya hücum sınağı aparmır):

```bash
ss -lntup
ip route show
systemctl --failed
```

`ss` dinləyən soketləri göstərir; tapılan hər port xidmət sahibinin siyahısı ilə tutuşdurulur: iş üçün lazımdırmı, hansı interfeysdə açıqdır, kimə məxsusdur? `ip route show` marşrutları göstərir, amma zonalararası firewall icazəsini tam təsvir etmir. `systemctl --failed` uğursuz vəziyyətdə olan bütün növ systemd vahidlərini göstərir; boş nəticə tətbiqin bütün funksiyalarının işlədiyinin sübutu deyil. **Texniki yoxlamanın nəyi gördüyü və nəyi görmədiyi nəticədə yazılır.**

### İnsident zamanı qərar vermək

:::steps İmtahan sistemində kütləvi səhv cavab: qərar ardıcıllığı
[[step]]
title = "Faktları topla"
body = "Hansı funksiya işləmir, nə vaxt başlayıb, neçə istifadəçiyə təsir edir, məlumat dəyişibmi? Sonra ehtimal edilən səbəblər ayrılır. Tək uğursuz giriş qeydi hücumu təsdiqləmir, lakin təsdiq gözləyərkən davam edən məlumat çıxışına göz yummaq da olmaz. Təcililik müşahidə edilən zərər və qeyri-müəyyənliklə əsaslandırılır."

[[step]]
title = "Zərəri məhdudlaşdır"
body = "Davam edən zərər dayandırılır, uyğun qeydlər və sistem vəziyyəti qorunur, təmiz mənbədən bərpa planı seçilir. Hücumçunun hesabını bağlamaqla kifayətlənilmir: aktiv sessiyalar, açarlar və başqa giriş yolları yoxlanır."

[[step]]
title = "Bərpa et və yoxla"
body = "Bərpadan sonra qəbul edilmiş cavablar, qiymətlərin versiyaları və istifadəçi hüquqları tutuşdurulur. Xidməti tez açmaq naminə sübutsuz qiymət bazasını doğru saymaq tamlıq problemini böyüdə bilər."

[[step]]
title = "Öyrən və yenilə"
body = "Risk reyestri və tələblər yenilənir. Təkmilləşdirmə konkret sahibi, son tarixi və yoxlama meyarı olan işə çevrilir."
:::

Nümunələr: bərpa sınağı məlumatın qaytarıldığını, amma **imza açarının olmadığını** göstəribsə, ilkin plan faydalılığı nəzərə almayıb. Hüququ alınmış əməkdaşın köhnə sessiyası işləyibsə, avtorizasiya dəyişikliyinin yayılma müddəti üçün tələb çatışmır. Bu əlaqə təhlükəsizlik anlayışlarını universitetin gündəlik qərarlarına bağlayır.

## Köhnə slaydlarla fərq

:::note Köhnə slaydlarla fərq
- **Non-repudiation** köhnə slaydda "təxirə salınmaz" tərcümə olunub. Düzgün qarşılığı **inkaredilməzlikdir**: əməliyyatın müəllifliyini sonradan inkar etməyə imkan verməyən sübutun olması.
- Slaydda təhdidlərin 80%-nin daxili, 20%-nin xarici olduğu yazılıb: 1990-cı illərdən qalma, mənbəsi olmayan rəqəmdir. Mühazirə də mənbəsiz sabit faizlərdən istifadəni rədd edir. İnsan faktoru daxili aktorla eyni şey deyil (xarici hücumçu da fişinqlə insan faktorundan istifadə edir); daxili təhdidin az rast gəlinməsi onun əhəmiyyətsiz olduğu demək deyil, çünki daxili şəxsin geniş giriş hüququ var.
- Slaydda adı keçən Rabitə və Yüksək Texnologiyalar Nazirliyi yanında Elektron Təhlükəsizlik Mərkəzi artıq bu adla yoxdur. 2018-dən sonra Elektron Təhlükəsizlik Xidməti, 2 iyun 2026-cı il fərmanı ilə isə onun əsasında Milli Kibertəhlükəsizlik Agentliyi (cert.az) yaradılıb. Dövlət orqanlarının şəbəkələri üzrə isə 2020-ci ildən ayrıca qurum olan Xüsusi Rabitə və İnformasiya Təhlükəsizliyi Dövlət Xidməti (cert.gov.az) cavabdehdir.
:::
