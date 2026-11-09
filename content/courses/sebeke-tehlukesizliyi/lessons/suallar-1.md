+++
title = "Şəbəkə təhlükəsizliyinin əsasları: CIA və DAD triadası"
unit = "suallar"
order = 1
summary = "Mövzu 1 üzrə imtahan sualları: mühazirənin bütün nəzarət sualları, situasiya tapşırıqları, konspektdən situasiyalar və ehtimal olunan əlavə suallar, hazır cavablarla."
updated = 2026-11-09

[[source]]
title = "Mühazirə 1: Şəbəkə təhlükəsizliyinin əsasları: CIA və DAD triadası"
note = "Elmar Cabbarov, 2026–2027"

[[source]]
title = "Midterm konspekti, Mövzu 1"
note = "Elmar Cabbarov"
+++

Əvvəl sualı öz sözlərinlə cavablandır, sonra cavaba bax. Situasiya suallarında ardıcıllıq: **aktiv → pozulan xassə (CIA) və nəticə (DAD) → səbəb → tədbir → yoxlama**. Universitet nümunələri şərti tədris nümunəsidir.

## Nəzarət sualları

:::reveal Verilənlər, informasiya və bilik eyni universitet nümunəsində necə fərqlənir?
- **Verilənlər:** formal təsvir, `student_id=142, score=85`.
- **İnformasiya:** rəqəmlərin müəyyən fənnin yekun nəticəsi olduğu məlum olanda alınan məna.
- **Bilik:** təqaüdün hesablanması qaydasını bilən əməkdaşın bu nəticəni digər fənlərlə əlaqələndirib qərar verməsi.
- Təhlükəsizlik rəqəmləri və kontekstini birlikdə qorumalıdır: bal dəyişməsə də başqa tələbənin identifikatoruna bağlanarsa, nəticə yanlışdır.
:::

:::reveal İnformasiyanın dolğunluğu ilə təhlükəsizlik tamlığı arasında hansı fərq var?
- **Dolğunluq** keyfiyyət xassəsidir: qərar üçün lazım olan hissələrin olması.
- **Təhlükəsizlik tamlığı** icazəsiz və ya təsadüfi dəyişiklikdən qorunmadır.
- Adları olmayan siyahı ilkin olaraq belə hazırlanıbsa, keyfiyyət qüsurudur; hücumçu adları silibsə, tamlıq pozuntusudur.
- Araşdırma üçün ilkin vəziyyət və icazəli dəyişiklik qaydası bilinməlidir.
:::

:::reveal Kodlaşdırma, sıxılma və şifrələmə niyə eyni qorumanı vermir?
- Kodlaşdırma (UTF-8, Base64) məzmunu başqa formaya çevirir; üsulu bilən hər kəs ilkin məzmunu bərpa edir.
- Sıxılma özlüyündə məxfiliyi qorumur.
- Yalnız şifrələmə məzmunu açarla qoruyur.
- Nümunə: tələbə siyahısını Base64 ilə məktuba əlavə etmək onu məxfi etmir.
:::

:::reveal Açıq universitet məlumatı üçün CIA-nın hansı xassələri tələb olunur?
- **Tamlıq və əlçatanlıq.** Məlumat açıqdır, oxu məxfiliyi tələb olunmur.
- Tamlıq: saxta imtahan tarixi və ya dəyişdirilmiş cədvəl ziyan verir.
- Əlçatanlıq: sayt dayansa xidmət pozulur.
- Dərc hüququ və məzmun tamlığı qorunur.
:::

:::reveal HTTPS ilə qorunan tətbiqdə başqa tələbənin sənədinin görünməsi hansı çatışmazlıqdır?
- Çatışmayan tədbir **obyekt səviyyəsində avtorizasiyadır**.
- Server yalnız giriş faktını yoxlayıb identifikatorun kimə aid olduğunu yoxlamır.
- HTTPS ötürmə kanalını qoruyur, alıcının biznes hüququnu müəyyən etmir.
- Pozulan xassə məxfilik, DAD nəticəsi ifşadır. Sorğudakı identifikatorun dəyişdirilə bilməsi özlüyündə zəiflik deyil, icazənin yoxlanmaması zəiflikdir.
:::

:::reveal SHA-256 xülasəsinin etalonunu niyə ayrıca qorumaq lazımdır?
- Heş yalnız etibarlı ilkin xülasə ilə müqayisədə mənalıdır.
- Hücumçu həm faylı, həm yanındakı heş faylını dəyişə bilirsə, adi müqayisə hücumu aşkar etmir.
- Etalon ayrıca nəzarətə alınır və ya etibarlı açarla imzalanır.
- Heş məzmunu gizlətmir və faylın doğru məlumat daşıdığını sübut etmir.
:::

:::reveal HMAC ilə rəqəmsal imzanın üçüncü tərəfə sübut verməsində hansı fərq var?
- **HMAC** xülasəni gizli açarla bağlayır; açarı paylaşan hər tərəf kod yarada bilir, ona görə konkret şəxsin müəllifliyini üçüncü tərəfə sübut etmir.
- **Rəqəmsal imza** şəxsi açarla yaradılır, uyğun açıq açarla yoxlanır.
- İmzanın kimə aid olduğu açarın etibarlı kimliklə əlaqəsinə söykənir.
- İmza səhv daxil edilmiş qiyməti həqiqətə çevirmir.
:::

:::reveal RAID, replikasiya və ehtiyat nüsxə hansı itkilərə qarşı fərqli işləyir?
- **RAID:** müəyyən disk nasazlıqlarına qarşı dayanıqlıq; ehtiyat nüsxənin əvəzi deyil, icazəli hesabın silməsi massivdə də görünür.
- **Replikasiya:** başqa serverdə nüsxə; zərərli dəyişikliyi də ötürür.
- **Ehtiyat nüsxə:** itirilmiş vəziyyətin bərpası; ayrı saxlanan, dəyişdirilməsi məhdud, bərpası yoxlanmış olmalıdır.
- **Artıqlıq** komponent sıradan çıxanda xidmətin davamıdır; eyni asılılıq hamısını dayandıra bilər.
:::

:::reveal RTO və RPO-nu imtahan cavablarının qəbulu üçün necə əsaslandırmaq olar?
- **RTO** xidmətin bərpa müddəti, **RPO** qəbul edilən məlumat itkisinin zaman həddidir.
- Şərti: RTO 2 saat, RPO 15 dəqiqə: xidmət iki saatda qayıtmalı, itki son 15 dəqiqədən çox olmamalıdır.
- Rəqəmləri satıcı deyil, **prosesin sahibi** əsaslandırır.
- İmtahan cavabları üçün 15 dəqiqəlik itki də qəbul edilməyə bilər; ona görə hədlər proses sahibi ilə razılaşdırılır.
:::

:::reveal DAD-da məhv etmə ilə xidmətdən imtina niyə tam eyni deyil?
- Məhv etmə faylın silinməsi və ya yararsız vəziyyətə salınmasıdır.
- İmtina (denial) xidmətə girişin dayandırılmasıdır; məlumat olduğu kimi qala bilər (DDoS).
- Hər ikisi əlçatanlığı pozur, amma səbəb və bərpa yolu fərqlidir.
- CIA qorunan xassəni, DAD baş verən nəticəni adlandırır.
:::

:::reveal Ransomware aşkar ediləndə məxfilik pozuntusu barədə hansı sübutlar axtarılır?
- Şifrələnmiş fayl görmək oğurluğu sübut etmir.
- Axtarılır: **çıxış trafiki**, **fayl oxuma qeydləri** və digər sübutlar.
- Əvvəlcədən məlumat çıxarılması sübut olunarsa, məxfilik pozuntusu (ifşa) əlavə edilir; şifrələmə tamlığı və əlçatanlığı pozur.
- Bu, ikiqat qəsbdir (double extortion).
:::

:::reveal Autentiklik, autentifikasiya, inkaredilməzlik və hesabatlılıq necə fərqlənir?
- **Autentiklik:** mənbənin və ya obyektin iddia edilənə uyğunluğu (imza, sertifikat).
- **Autentifikasiya:** kimlik iddiasının yoxlanması prosesi.
- **İnkaredilməzlik:** mənşəyi və ya çatdırılmanı sonradan inkar etməyə qarşı sübut (rəqəmsal imza, vaxt möhürü); "təxirə salınmamaq" deyil.
- **Hesabatlılıq:** əməliyyatın məsul subyektə bağlana bilməsi (fərdi hesab, qorunan audit).
- Paylaşılan və ya oğurlanmış hesab hesabatlılığı zəiflədir; açarın oğurlanması inkaredilməzliyə təsir edir.
:::

:::reveal Parker heksadında sahiblik itkisini məxfilik itkisindən ayıran nümunə hansıdır?
- Şifrəli arxiv diski oğurlananda **nəzarət (sahiblik) itkisi qətidir**.
- Məxfilik itkisi isə açarın qorunmasından asılıdır, avtomatik deyil.
- Ayrı nüsxə varsa, istifadə davam edir.
- Heksad: CIA + sahiblik və nəzarət, autentiklik, faydalılıq.
:::

:::reveal AAA mərhələlərinin hər biri LMS sorğusunda hansı qərara cavab verir?
- **Autentifikasiya:** kim olduğunu necə sübut edir (hesab, MFA).
- **Avtorizasiya:** bu obyekt üzərində bu əmələ icazəsi varmı (yalnız öz qrupunun qiyməti).
- **Uçot:** nə, nə vaxt, hansı nəticə ilə edildi (köhnə/yeni bal, hesab, sorğu identifikatoru).
- Tipik səhvlər: uğurlu girişi bütün hüquqlar saymaq, icazəni interfeysdə gizlətmək, parolu qeydə yazmaq.
:::

:::reveal Zəiflik, təhdid mənbəyi, risk və insidenti bir-birindən necə ayırmaq olar?
- **Zəiflik:** istifadə oluna bilən çatışmazlıq (ixracda icazə yoxdur).
- **Təhdid mənbəyi:** zərəri doğuran subyekt və ya səbəb (xarici şəxs, daşqın).
- **Risk:** zərərin ehtimalı və təsiri.
- **İnsident:** təhlükəsizliyi pozan, cavab tələb edən təsdiqlənmiş hadisə (icazəsiz ixrac təsdiqlənir).
- Hər hadisə (qeyd) insident deyil; mənbə ilə zəiflik eyni deyil.
:::

:::reveal Risk balının ehtimal balı ilə təsir balının hasili olması hansı məhdudiyyətə malikdir?
- Bu, dəqiq ehtimal hesabı deyil: 3 bal 2 baldan 1,5 dəfə böyük real ehtimal bildirmir.
- Şkala yalnız prioritet seçməyə kömək edir; kateqoriyaların mənası əvvəlcədən yazılmalıdır.
- Eyni hasilli iki ssenarinin cavabı fərqli ola bilər.
- Aşağı hasilli ssenari (yanğın 1×5 = 5) qəbul edilən maksimum itki, insan təhlükəsizliyi və hüquqi tələblərə görə nəzərə alınır; qeyri-müəyyənlik yazılır.
:::

:::reveal Riskin ötürülməsi universitetin hansı məsuliyyətlərini avtomatik aradan qaldırmır?
- Ötürmə maliyyə nəticəsinin və işin müəyyən hissəsini müqavilə ilə bölüşməkdir (sığorta, xidmət müqaviləsi).
- **Məlumat sahibinin məsuliyyəti avtomatik itmir.**
- Qalıq risk qalır və sahibi olmalıdır; koordinasiya universitetin öz sisteminə cavabdehliyini aradan qaldırmır.
:::

:::reveal Minimum səlahiyyətlə vəzifələrin ayrılması eyni prosesdə necə tətbiq olunur?
- Qiymət düzəlişində: **müraciət, təsdiq və icra** rolları ayrılır (vəzifələrin ayrılması).
- Hər rolun hesabı yalnız lazım olan cədvəllərə və lazım olan müddətə hüquq alır (minimum səlahiyyət).
- Eyni hesab hər ikisini basa bilirsə, ayrılma yoxdur.
- Hüquqlar bitmə tarixi ilə verilir, vaxtında götürülür; təsdiqləyən nəyi təsdiqlədiyini görə bilməlidir.
:::

:::reveal Fail-secure ilə insan təhlükəsizliyinə yönəlmiş fail-safe qərarı nə vaxt fərqlənir?
- **Fail-secure:** nasazlıqda qorunan resursa giriş nəzarətsiz açılmır (icazə serverinə çatılmırsa, yazma rədd edilir).
- **Fail-safe:** insan təhlükəsizliyi üstündür (yanğın çıxışı enerji kəsiləndə açıq qalır).
- Fiziki tələb qiymət bazasına nəzarətsiz giriş vermir; hansı təhlükənin üstün olduğu əvvəlcədən müəyyən edilir.
- İstisna rejimi qaydaya, müddətə və auditə bağlıdır.
:::

:::reveal Sıfır etibar yanaşmasında daxili IP ünvanı niyə kifayət etmir?
- Sıfır etibar şəbəkədəki yerə görə avtomatik etimad vermir (NIST SP 800-207).
- Qərara istifadəçi kimliyi, cihaz vəziyyəti, resursun həssaslığı və sessiya konteksti daxildir.
- Kafedra noutbuku Wi-Fi-da olsa da əməkhaqqı bazasına giriş almır.
- İcazə məhdud sessiya üçün verilir, risk dəyişəndə yenidən qiymətləndirilir. Bu, VPN və ya bir məhsul deyil.
:::

:::reveal VLAN, NAT və firewall nə edir; hansı tələbləri ayrıca yoxlamaq lazımdır?
- **VLAN:** kanal səviyyəsində məntiqi ayrılma; marşrutlaşdırılan zonalararası trafiki avtomatik qadağan etmir.
- **NAT:** ünvan çevrilməsi; giriş siyasəti və tətbiq nəzarətini əvəz etmir.
- **Firewall:** trafiki siyasətə uyğun buraxır/rədd edir; hər qiymət dəyişikliyinin əsasını yoxlamır.
- Ayrıca yoxlanır: tətbiqdə obyekt icazəsi, mənbə–hədəf–xidmət üzrə qaydalar, kimlik və əməliyyat konteksti.
:::

:::reveal Equifax, Stuxnet və WannaCry hadisələrinin hər biri hansı yanlış təhlükəsizlik fərziyyəsini göstərir?
- **Equifax (məxfilik):** "portal işləyirsə sızma yoxdur" yanlışdır; zəiflik (Apache Struts) və yamaq inventardan, çıxış nəzarətindən asılıdır.
- **Stuxnet (tamlıq):** "normal ekran doğru prosesi sübut edir" yanlışdır; müstəqil ölçmə lazımdır.
- **WannaCry (əlçatanlıq, həmçinin tamlıq):** "tək təhlükəsizlik məhsulu bütün zərəri dayandırır" yanlışdır; yamaq (MS17-010), SMB-nin bağlanması, seqmentləşdirmə və bərpa sınağı lazımdır.
:::

## Situasiya tapşırıqları

**Situasiya 1.** Universitetin LMS-ində tələbə öz hesabı ilə daxil olur. Sorğudakı tələbə identifikatorunu dəyişəndə başqa şəxsin qiymət cədvəlini alır. Bağlantı HTTPS-dir və parol oğurlanmayıb. CIA, DAD və AAA üzrə problemi müəyyən edin.

:::reveal Cavab
- **Aktiv:** tələbə qiymət cədvəli. **Pozulan xassə:** məxfilik; **DAD:** ifşa.
- **AAA:** autentifikasiya işləyə bilər, çatışan mərhələ obyekt üzrə **avtorizasiyadır**.
- **Səbəb:** server sorğunu edən tələbənin həmin nəticəyə icazəsini yoxlamır; HTTPS yalnız kanalı qoruyur.
- **Tədbir:** hər sorğuda obyekt üzrə icazə yoxlaması.
- **Yoxlama:** sınaq hesabları ilə düzəliş yoxlanır, əvvəlki müraciətlər üzrə mümkün ifşanın əhatəsi araşdırılır. Qeydlərdə qiymət məzmununu təkrar toplamaq əvəzinə obyekt və qərar identifikatorları saxlanır.
:::

**Situasiya 2.** Kafedranın qiymət faylı və onun SHA-256 xülasəsi eyni yazıla bilən qovluqdadır. Mübahisəli qiymət tapılıb, amma cari faylın xülasəsi qovluqdakı etalonla uyğun gəlir. Bu uyğunluq tamlığı təsdiqləyirmi?

:::reveal Cavab
- **Xeyr.** Uyğunluq yalnız iki cari obyektin bir-birinə uyğun olduğunu göstərir.
- Hər ikisini dəyişmək imkanı varsa, etibarlı ilkin vəziyyət barədə sübut yoxdur.
- **Yoxlama:** faylın versiyaları, audit qeydləri və ayrıca qorunan nüsxə.
- **Tədbir:** etalon ayrı nəzarətə alınır və ya etibarlı açarla imzalanır.
- İlkin qiymətin faktiki doğruluğu akademik sənədlərlə yoxlanır; kriptoqrafik yoxlama bu qərarı əvəz etmir.
:::

**Situasiya 3.** Universitetin fayl serverində ransomware aşkarlanıb. Şərti nümunədə çıxış qeydləri tələbələrin şəxsi işlərinin əvvəl kənara ötürüldüyünü göstərir. Təmiz ehtiyat nüsxə var. Rəhbərlik nüsxədən bərpanı tam həll sayır. Qalan problemlər hansılardır?

:::reveal Cavab
- **Pozulan xassələr:** ifşa məxfiliyi, icazəsiz şifrələmə tamlığı və əlçatanlığı pozub.
- Bərpa məlumatın işləkliyini qaytara bilər, **sızmış məlumatı geri almır**.
- **Tədbirlər:** davam edən hücum məhdudlaşdırılır, kompromitasiya edilmiş hesablar və sessiyalar araşdırılır, giriş yolu bağlanır.
- **Yoxlama:** nüsxənin təmizliyi və tamlığı, sübutların qorunması.
- İfşanın əhatəsi müəyyən edilir; aidiyyəti bildiriş qərarları hüquqi tələblər, məlumatın növü və təsdiqlənmiş prosedur üzrə verilir.
:::

**Situasiya 4.** Universitet kitabxanasının kataloqu üçün illik gözlənilən kəsinti itkisi şərti olaraq 3 000 AZN hesablanıb. Ehtiyat klasterin illik xərci şərti 40 000 AZN-dir. Kataloq diplom və imtahan xidmətləri üçün asılılıq deyil. Hansı risk cavabı əsaslıdır?

:::reveal Cavab
- Bu fərziyyələrlə klasteri gözlənilən itkiyə görə əsaslandırmaq çətindir (40 000 ≫ 3 000).
- **Cavab:** ucuz monitorinq və bərpa tədbirləri qiymətləndirilə, qalan risk səlahiyyətli rəhbər tərəfindən **qəbul** edilə bilər.
- Qərar hesabın əsasını, qəbul edilən kəsintini və baxış tarixini göstərməlidir.
- Nadir ağır itki, hüquqi tələb və ya gizli asılılıq varsa, hesab dəyişə bilər.
- Məbləğlər faktiki xərc deyil, qərar məntiqini göstərən şərti rəqəmlərdir.
:::

**Situasiya 5.** Tədris hissəsində bir əməkdaş qiymət düzəlişi yaradır və eyni hesabla onu təsdiqləyir. Auditdə hesab adı görünür. Hansı prinsip çatışmır və sadəcə MFA əlavə etmək problemi həll edərmi?

:::reveal Cavab
- **Çatışan prinsip:** vəzifələrin ayrılması.
- **MFA həll etmir:** hesabın həqiqi sahibini daha güclü yoxlamaq həmin şəxsin öz əməlini təsdiqləməsinin qarşısını almır.
- **Tədbir:** müraciət və təsdiq üçün ayrı səlahiyyətlər; eyni subyektin öz müraciətini təsdiqləməsi serverdə rədd edilir.
- **Yoxlama:** dəyişdirilən versiya, əsaslandırma və hər iki qərar auditlə bağlanır.
- Hesab paylaşılıbsa, fərdi hesablarla hesabatlılıq da bərpa edilməlidir.
:::

**Situasiya 6.** Yataqxananın qorunan Wi-Fi şəbəkəsinə qoşulan noutbukdan tələbə bazasının portuna əlaqə qurulur. Administrator daxili IP-ni kifayət qədər etibarlı sayır. Sıfır etibar və dərinlik üzrə müdafiə baxımından nə dəyişməlidir?

:::reveal Cavab
- Daxili şəbəkədə olmaq məlumat bazasına giriş hüququ yaratmır (sıfır etibar).
- Yataqxana ilə server zonası arasında əsaslandırılmamış yol bağlanır; baza yalnız lazım olan tətbiq hesablarını və mənbələri qəbul edir.
- Tətbiqdə istifadəçi və obyekt üzrə icazə ayrıca yoxlanır (dərinlik üzrə müdafiə: ayrı qatlar).
- İdarəetmə girişi fərqli nəzarətə alınır, cəhdlər izlənir.
- Wi-Fi şifrələməsi yerli rabitəni qoruyur; cihazın sağlamlığını və istifadəçinin bütün resurslara hüququnu sübut etmir.
:::

**Situasiya 7.** Universitetin şifrəli arxiv diski oğurlanıb. Eyni məlumatın işlək nüsxəsi ayrı məkandadır, açarlar isə diskdən ayrı qorunur. Hansı itki qətidir, hansı pozuntu barədə əlavə sübut lazımdır?

:::reveal Cavab
- **Qəti itki:** Parker heksadı üzrə sahiblik və nəzarət.
- Ayrı nüsxə işləyirsə, xidmətin əlçatanlığı davam edə bilər.
- **Məxfilik itkisi** avtomatik təsdiqlənmir: şifrələmə, açarların vəziyyəti və diskdəki açıq qalıqlar araşdırılır.
- Diskin sonrakı taleyi bilinmədiyi üçün risk qeyd edilir; açar nüsxələrinin inventarı və insident proseduru yoxlanır.
- Şifrələmə oğurlanma faktını yox etmir, mümkün məzmun ifşasının qarşısını ala bilər.
:::

**Situasiya 8.** İmtahanın son saatında icazə xidməti dayanır. Proqramçı bütün sorğuları müvəqqəti buraxmağı təklif edir. Universitet xidmətin dayanmasını da qəbul etmək istəmir. Təhlükəsiz qərar necə hazırlanmalıdır?

:::reveal Cavab
- Bütün sorğuları açmaq **fail-secure** prinsipini pozar və qiymət, cavab və şəxsi məlumatlara nəzarətsiz giriş yaradar.
- Yazma və həssas oxu əməliyyatları üçün əvvəlcədən müəyyən edilmiş təhlükəsiz davranış tətbiq edilir.
- Məhdud ehtiyat rejim yalnız təsdiqlənmiş qaydalar, müddət və auditlə işləyə bilər.
- Tələbələr üçün vaxt uzadılması və rəsmi qəbul proseduru akademik qərarla müəyyən edilir.
- Sonra icazə xidmətinin artıqlığı, asılılıqları və nasazlıq sınaqları üzrə risk tədbiri hazırlanır.
:::

## Konspektdən situasiyalar

**Situasiya K1.** Universitetin qiymət sistemində bir tələbə müəllimin hesabına daxil olub öz imtahan balını 45-dən 85-ə qaldırır. Heç bir məlumat kənara çıxmayıb, sistem də dayanmayıb. CIA və DAD baxımından nə baş verib və hansı tədbir bunu tez aşkarlayardı?

:::reveal Cavab
- **Pozulan xassə:** tamlıq; **DAD:** dəyişdirmə (alteration).
- Hesaba icazəsiz giriş olduğuna görə **autentifikasiya da zəifdir**.
- **Aşkarlama:** qiymət dəyişikliklərinin audit loqu (kim, nə vaxt, köhnə və yeni dəyər) və dəyişiklikdən sonra müəllimə bildiriş.
- **Qarşısının alınması:** müəllim hesablarında MFA.
:::

**Situasiya K2.** Universitetin elektron kitabxana kataloqu hər ay təxminən bir dəfə 10 dəqiqəlik kəsinti yaşayır, tələbələr bir az gözləyir, ziyan cüzidir. Serveri tam ehtiyatlı klasterə keçirmək ildə 40 000 AZN, kəsintilərin illik ziyanı isə təxminən 3 000 AZN qiymətləndirilir. Hansı risk strategiyası məntiqlidir?

:::reveal Cavab
- Ehtimal yüksək, təsir aşağıdır, tədbirin dəyəri ziyandan dəfələrlə çoxdur.
- **Qəbul etmək (accept)** məntiqlidir: rəhbərlik (İT direktoru, prorektor) qərar verir və yazılı sənədləşdirir.
- Ucuz qismən tədbirlərlə (monitorinq, avtomatik yenidən başlatma) risk bir az azaldıla bilər; 40 000 AZN-lik klaster əsaslandırılmır.
- Eyni kəsinti imtahan sistemində olsaydı, təsir yüksək olardı və cavab **azaltmaq** olardı.
:::

**Situasiya K3.** Universitetin tədris hissəsinin şəbəkəsinə ransomware düşür. Hücumçular əvvəlcə 20 000 tələbənin şəxsi işini (pasport, ünvan, qiymətlər) öz serverlərinə köçürür, sonra serverləri şifrələyir və "ödəməsəniz, məlumatı yayacağıq" deyirlər. Hansı xassələr pozulub? Ehtiyat nüsxədən bərpa problemi tam həll edirmi?

:::reveal Cavab
- **Məxfilik** pozulub (ifşa, məlumat oğurlanıb); şifrələmə **əlçatanlığı** pozub (məhv/imtina); icazəsiz dəyişdirmə **tamlığı** da pozub (dəyişdirmə). Bu, ikiqat qəsbdir.
- Təmiz nüsxədən bərpa tamlığı və əlçatanlığı qaytara bilər, **məxfiliyi qaytarmır**.
- **Tədbir:** insidentə cavab planı işə salınır, tələbələr və aidiyyəti dövlət orqanları xəbərdar edilir, sızmanın yolu tapılıb bağlanır.
- **Yoxlama:** ehtiyat nüsxənin hücumdan təsirlənmədiyi, zərərli proqram daşımadığı və bərpanın mümkün olduğu.
:::

## Ehtimal olunan əlavə suallar

:::reveal CIA triadasını izah edin: hər xassə, pozulma nümunəsi və qoruyan vasitə.
| Xassə | Mənası | Pozulma | Vasitə |
| --- | --- | --- | --- |
| Məxfilik | Yalnız icazəli subyekt görür | Sızma, dinləmə, səhv ünvana məktub | Şifrələmə, girişə nəzarət, MFA, təsnifat |
| Tamlıq | İcazəsiz/təsadüfi dəyişiklik yoxdur, mənbə doğrudur | Məbləğin dəyişməsi, defacement | Heş, imza, HMAC, versiya nəzarəti, loglar |
| Əlçatanlıq | İcazəli istifadəçi xidməti münasib vaxtda alır | DDoS, ransomware, elektrik kəsintisi, disk qəzası | Ehtiyat nüsxə, RAID, klaster, UPS, DDoS qoruması |

Xassələr bir-birinə mane ola bilər (hər səhifədə MFA əlçatanlığı ləngidir); hansının kritik olduğu sistemdən asılıdır: şəxsi işlər → məxfilik, qiymət jurnalı → tamlıq, imtahan günü test sistemi → əlçatanlıq.
:::

:::reveal CIA ilə DAD-ın fərqi nədir? Üç ünsürü uyğunlaşdırın.
- CIA **qorunan xassəni**, DAD ona qarşı **baş verən nəticəni** adlandırır; hadisə təhlilində hər ikisi göstərilir.
- Məxfilik ↔ **ifşa** (sızma, açıq qovluq); tamlıq ↔ **dəyişdirmə** (saxta bal, bank rekvizitləri); əlçatanlıq ↔ **məhv etmə / imtina** (silinmə, ransomware, DDoS).
- "Nə baş verdi?" → DAD, "nə pozuldu?" → CIA.
- Bir hücum bir neçə xassəni poza bilər (ransomware: ifşa, dəyişdirmə, imtina).
:::

:::reveal Aktiv, zəiflik, təhdid, risk, hadisə və insident terminlərini bir ssenaridə fərqləndirin.
- **Aktiv:** elektron qiymət jurnalı. **Zəiflik:** müəllimlərin "123456" parolu. **Təhdid:** balını qaldırmaq istəyən tələbə.
- **Risk:** hesaba girib balı dəyişmə ehtimalı və nəticəsi. **Hadisə:** log yazısı (hər hadisə insident deyil).
- **İnsident:** balın həqiqətən dəyişdirilməsi. **Tədbir (control):** müəllim hesablarında MFA.
- Eksploit zəiflikdən istifadə üsuludur; hücum qəsdli cəhddir.
:::

:::reveal Passiv və aktiv hücumu müqayisə edin.
- **Passiv:** məlumatı dəyişmədən müşahidə edir (dinləmə), izi tapmaq çətindir; qarşısı qorunan kanal və şifrələmə ilə alınır.
- **Aktiv:** məlumatı dəyişir, saxta paket göndərir və ya resursu tükədir; giriş yoxlaması, sürət məhdudiyyəti, seqmentləşdirmə, aşkarlama (IDS, loglar) və bərpa (ehtiyat nüsxə) tətbiq olunur.
- Konspekt: passiv hücuma qarşı əsasən qarşısını almaq, aktivə qarşı aşkarlama və bərpa; mühazirə dəqiqləşdirir ki, aktivə qarşı da qabaqlayıcı tədbirlər var, aşkarlama və bərpa hər ikisi üçün planlaşdırılır.
:::

:::reveal Riskin dörd cavab strategiyasını nümunələrlə izah edin.
- **Azaltmaq (mitigate):** ehtimalı və ya təsiri endirmək (MFA, yamaq, ehtiyat nüsxə).
- **Yayınmaq (avoid):** riski yaradan fəaliyyəti dayandırmaq (lazımsız açıq paylaşımı bağlamaq).
- **Ötürmək (transfer):** maliyyə nəticəsini müqavilə ilə bölüşmək (kiber sığorta, autsorsinq); məlumat sahibinin məsuliyyəti itmir.
- **Qəbul etmək (accept):** qalan riski səlahiyyətli yazılı qərarla saxlamaq, baxış tarixi ilə.
- Tədbirdən sonra qalan: **qalıq risk**; sıfır risk yoxdur.
:::

:::reveal Risk balını və illik gözlənilən itkini hesablayın (şərti nümunələr).
- **Risk balı = ehtimal × təsir:** qəbul sənədlərinin ixracı 4 × 5 = **20**; kataloq nasazlığı 4 × 2 = **8**; ağır yanğın 1 × 5 = **5**; identifikasiya xidmətinin dayanması 3 × 5 = **15**.
- **Kəmiyyət:** kəsintinin orta zərəri 2 000 AZN, illik tezlik 3 → illik gözlənilən itki 3 × 2 000 = **6 000 AZN**.
- 1 500 AZN-lik tədbir tezliyi 1-ə endirirsə: qalan itki 2 000 AZN + tədbir 1 500 AZN = **3 500 AZN**.
- Məhdudiyyət: nadir böyük və pulla ölçülməyən itkini tam əhatə etmir; fərziyyələr qərardan sonra da izlənir.
:::

:::reveal Təhlükəsizliyin layihələndirmə prinsiplərini sadalayın.
- **Minimum səlahiyyət** (least privilege), **vəzifələrin ayrılması**, **dərinlik üzrə müdafiə** (defense in depth), **təhlükəsiz imtina** (fail-secure), **tam vasitəçilik**, **hücum səthinin azaldılması**.
- Əlavə yanaşma: **sıfır etibar** (zero trust).
- Tipik qüsurlar: bütün tətbiqlərdə eyni inzibati hesab; hazırlayanın öz müraciətini təsdiqləməsi; bütün qatların eyni geniş istisnaya əsaslanması; xəta zamanı nəzarətin söndürülməsi; yalnız giriş səhifəsində yoxlama; sınaq interfeysinin açıq qalması.
:::

:::reveal Məlumatın üç vəziyyətini və həyat dövrünü izah edin.
- **Sükunətdə (data at rest):** diskdə, arxivdə. **Ötürülərkən (data in transit):** şəbəkədə. **İstifadədə (data in use):** işləyən prosesin yaddaşında, ekranda, ixrac faylında.
- Şifrəli saxlanıb TLS ilə göndərilən siyahı ekranda açıqdır; yalnız ilk ikisinə baxmaq kifayət deyil.
- **Həyat dövrü:** toplama və yaratma, saxlama, istifadə, ötürmə və paylaşma, arxivləşdirmə, silinmə.
- Təsnifat (açıq, daxili, məxfi, ciddi məhdud, şərti): sahib tələbi müəyyən edir, saxlayıcı tətbiq edir.
:::

:::reveal OSI səviyyələrini təhdid və tədbirlərlə izah edin.
- 7 Tətbiq: icazəsiz sorğu, inyeksiya → obyekt icazəsi. 6 Təqdimat: kodlaşdırma səhvi → format/tip yoxlaması. 5 Sessiya: sessiya oğurluğu → token qorunması, ləğv.
- 4 Nəqliyyat: bağlantı tükənməsi → vəziyyət izləmə. 3 Şəbəkə: saxta IP, yanlış marşrut → giriş filtrləri, IPsec. 2 Kanal: ARP saxtalaşdırması → port nəzarəti. 1 Fiziki: kabel kəsilməsi → fiziki giriş, enerji.
- TCP/IP dörd səviyyədir (kanal, internet, nəqliyyat, tətbiq).
- Hücum bir səviyyədə həbs olunmur; başlanğıc mexanizmi, müşahidə nöqtəsi və zərər ayrı göstərilir.
:::
