+++
title = "Bulud hesablamalarının əsasları və bulud təhlükəsizliyi"
unit = "suallar"
order = 14
summary = "Mühazirənin nəzarət sualları, situasiya tapşırıqları, konspektdən situasiyalar və ehtimal olunan əlavə suallar hazır cavablarla; imtahanda yazılı cavab üçün."
updated = 2026-11-09

[[source]]
title = "Mühazirə 14: Bulud hesablamalarının əsasları və bulud təhlükəsizliyi"
note = "Elmar Cabbarov, 2026–2027"

[[source]]
title = "Midterm konspekti, Mövzu 14"
note = "Elmar Cabbarov"
+++

Əvvəl suala özün cavab yaz, sonra cavaba bax. Situasiya cavabının ümumi quruluşu: aktiv, pozulan xassə, səbəb, tədbir, yoxlama.

## Nəzarət sualları

:::reveal NIST SP 800-145-in beş xüsusiyyəti adi server icarəsindən nə ilə fərqlənir?
- Beş xüsusiyyət: tələb üzrə özünəxidmət, geniş şəbəkə girişi, resursların hovuzlaşdırılması (multi-tenancy), sürətli elastiklik, ölçülən xidmət.
- Adi icarədə server sabitdir, sifariş provayder müdaxiləsi ilə gedir, tutum tələbə görə avtomatik artıb azalmır, istifadə ölçülmür.
- Başqasının server otağında sabit icarə avtomatik bulud sayılmır; statik sayt da beş xüsusiyyətin hamısını daşımaya bilər.
- Özünəxidmət təsdiqsizlik demək deyil: kvota və təsdiqlənmiş obrazlar təyin edilə bilər, sifariş sərhəd daxilində avtomatik emal olunur.
:::

:::reveal Elastiklik, şaquli miqyaslanma və üfüqi miqyaslanma arasında hansı əlaqə var?
- Elastiklik (elasticity) tələb artanda genişlənmə, azalanda daralmadır; miqyaslanma (scalability) sistemin artan yükü qarşılamaq qabiliyyətidir.
- Şaquli miqyaslanma: LMS daha böyük virtual maşına keçirilir. Üfüqi: bir neçə tətbiq nüsxəsinə bölünür.
- Elastiklik bu miqyaslanma üsullarını tələbə görə (çox vaxt avtomatik) artırıb azaltmaqdır.
- Hər ikisində baza kilidlənmələri və ümumi fayl saxlancı dar boğaz ola bilər; tətbiqi çoxaltmaq bazanın səhv layihəsini düzəltmir.
:::

:::reveal İctimai bulud ilə ictimai açılmış saxlanc niyə fərqli anlayışlardır?
- İctimai bulud yerləşdirmə modelidir: provayderin xidməti hamıya təklif olunur, amma hər müştərinin resursları məntiqi ayrılır.
- İctimai saxlanc isə ayrıca konfiqurasiya qərarıdır: bucket-in hamıya oxunmasına icazə verilməsi.
- Təhlükəsizlik modelin adından yox, izolyasiyadan, icazələrdən, konfiqurasiyadan və nəzarətdən asılıdır.
- Qarışdırmaq səhv risk qiymətləndirməsinə gətirir.
:::

:::reveal Özəl buludu üçüncü tərəfin idarə etməsi onun modelini dəyişirmi?
- Xeyr. Özəl buludu müəyyən edən yalnız bir təşkilatın istifadəsidir, idarə edənin kim olması yox.
- Üçüncü tərəf operator ola bilər, infrastruktur universitetdən kənarda yerləşə bilər.
- Dəyişən şey idarəetmə məsələsidir: tutum, yeniləmə və operatorun məsuliyyəti; "özəl" ad təhlükəsizlik vermir (yamaq gecikirsə, nüsxə yoxlanmırsa).
:::

:::reveal Hibrid bulud ilə çoxbuludlu istifadəni universitet nümunəsində müqayisə edin.
- Hibrid: müstəqil qalan iki və ya daha çox bulud, məlumat və tətbiqin daşınmasına imkan verən texnologiya ilə əlaqələndirilir. Nümunə: özəl buluddakı LMS imtahan vaxtı ictimai buludda əlavə tətbiq nüsxələri işlədir.
- Çoxbuludlu (multi-cloud): sadəcə bir neçə provayderdən istifadə. Nümunə: poçt bir provayderdə, hesablama digərində.
- Çoxbuludlu NIST-in beşinci yerləşdirmə modeli deyil; yerli server ilə SaaS abunəsinin yanaşı olması hibrid sayılmır.
- Çoxbuludlu kimlik, audit və bacarıq tələbini artırır; iki buludda eyni tətbiq yalnız məlumat, açar və bərpa asılılıqları da ayrıldıqda kömək edir.
:::

:::reveal IaaS, PaaS və SaaS-da əməliyyat sistemi, tətbiq və hesablar üzrə məsuliyyəti ayırın.
- IaaS: qonaq əməliyyat sistemi, tətbiq və hesablar universitetdə; provayder avadanlıq və virtuallaşdırmada.
- PaaS: ƏS və icra mühiti yamaqları provayderdə; tətbiq kodu, konfiqurasiya və hesablar universitetdə.
- SaaS: ƏS və əsas tətbiq provayderdə; hesablar, MFA, rollar, paylaşma və məlumat universitetdə.
- Bütün modellərdə məlumatın təsnifatı və hesablar müştəridədir.
:::

:::reveal İdarəetmə müstəvisinin ələ keçirilməsi tətbiq hesabının ələ keçirilməsindən nə ilə fərqlənir?
- İdarəetmə müstəvisi (control plane) resursları yaradan və dəyişən interfeysdir (panel, API); məlumat müstəvisi (data plane) tətbiqin gündəlik məlumat əməliyyatıdır.
- Oğurlanmış idarəetmə hesabı ilə hücumçu LMS-in giriş səhifəsinə toxunmadan bütün bazanı silə bilər.
- Tətbiq hesabı yalnız tətbiqin icazə verdiyi əməliyyatlara imkan verir.
- Panel və API eyni səlahiyyətlərin yoludur; məhdudiyyət xidmətin avtorizasiya siyasətində olmalıdır.
:::

:::reveal Rolun icazə siyasəti ilə etibar siyasəti hansı suallara cavab verir?
- İcazə siyasəti: rol hansı əməliyyatı hansı resursda edə bilər (məsələn, yalnız `s3:GetObject` ilə `assignments/*`).
- Etibar siyasəti: hansı kimliklər və hansı şərtlərlə rolu qəbul edə bilər.
- Dar icazəli rolu hər kəs qəbul edə bilirsə, qoruma natamamdır.
- Tam effektiv icazə digər siyasətlərə, təşkilat məhdudiyyətlərinə və açar siyasətinə də bağlıdır; açıq rədd (explicit deny) icazəni üstələyə bilər.
:::

:::reveal MFA oğurlanmış sessiya və xidmət tokeni riskini niyə tam aradan qaldırmır?
- MFA girişdə amilləri yoxlayır; giriş bitəndən sonra oğurlanmış sessiya tokeni MFA-nı yan keçir.
- Xidmət tokeni və açar insan girişi deyil, MFA ilə qorunmur; müvəqqəti token də müddəti bitənədək təhlükəlidir.
- Çarələr: fişinqə davamlı MFA (FIDO2, passkey), cihaz vəziyyəti, qısa sessiya, riskli girişdə yenidən təsdiq, xidmətlər üçün qısaömürlü iş yükü kimliyi və dar etibar əlaqəsi.
:::

:::reveal Şifrəli saxlancın anonim oxunmasına icazə verilsə, şifrələmə hansı problemi həll etmir?
- Yanlış avtorizasiyanı: saxlanarkən şifrələmə yalnız diskin və ya surətin icazəsiz əldə edilməsindən qoruyur.
- Səlahiyyətli xidmət (burada anonim girişə icazə verilmiş saxlanc) məlumatı açıb verir.
- Eyni qayda artıq rol hüququna aiddir: LMS roluna bütün sənədləri oxumaq hüququ verilibsə, server tərəfli şifrələmə onu daraltmır.
- Düzgün tədbir: ictimai girişin bloklanması, dar icazə, anonim sorğunun rədd sınağı.
:::

:::reveal DEK, KEK, KMS və BYOK-un əlaqəsini izah edin.
- DEK (Data Encryption Key) məlumatı şifrələyir; KEK (Key Encryption Key) DEK-i qoruyur. Şifrəli DEK şifrəli obyektlə yanaşı saxlanır (envelope encryption).
- KMS açarların yaradılması, istifadə icazələri, auditi və həyat dövrünü verir.
- BYOK: müştəri açar materialını yaradıb xidmətə gətirir; mənşəyə və həyat dövrünə nəzarəti artırır.
- KEK-in qorunması çoxlu obyektin açılmasına təsir edir; BYOK provayderin məlumatı heç vaxt aça bilməməsi demək deyil. HSM açarları aparatda qoruyur, icazələri əvəz etmir.
:::

:::reveal Təhlükəsizlik qrupu, özəl endpoint və IAM niyə birlikdə qiymətləndirilir?
- Şəbəkə qaydası yalnız yolu açır; kimin nəyi edə biləcəyini IAM və tətbiq təyin edir.
- Açıq TCP 443-dən zəif API hücumu keçə bilər; PostgreSQL portunun yalnız tətbiq qrupuna açılması bazada güclü autentifikasiya və dar rol tələbini aradan qaldırmır.
- Özəl endpoint özəl yol verir, amma ələ keçirilmiş icazəli maşın həmin yoldan istifadə edə bilər.
- Biri digərinin boşluğunu örtmür; qrup istinadlarının əhatəsi dəyişiklik zamanı yoxlanır.
:::

:::reveal Konteyner obrazının imzası ilə zəiflik skanı nəyi ayrı-ayrılıqda yoxlayır?
- İmza obrazın mənşəyini və dəyişmədiyini yoxlayır, imzalayanın kodunun təhlükəsizliyini sübut etmir.
- Zəiflik skanı obrazdakı məlum zəiflikləri tapır, gələcək zəifliyə zəmanət vermir.
- Obraz kriptoqrafik heşə (digest) bağlanır, sonra icra zamanı proses, şəbəkə və fayl davranışı izlənir; saxlanılan obrazlar yenidən qiymətləndirilir.
:::

:::reveal Serverless funksiyada artıq rol və təkrar hadisə hansı nəticələr yarada bilər?
- Artıq rol (məsələn, bütün saxlancı oxumaq və silmək) bir zəifliyin təsirini artırır, kod zəifliyi və ya hadisə saxtalaşdırılması geniş səlahiyyətdən istifadəyə çevrilir.
- Təkrar hadisə eyni sənədi iki dəfə emal edə bilər; çarə idempotentlikdir (məsələn, nəticə obyekt versiyasına bağlanır).
- Digər risklər: müvəqqəti diskdə qalıq məlumat, cold start və icra limitləri imtahan vaxtı cavab müddətinə təsir edir.
:::

:::reveal CloudTrail idarəetmə hadisəsi ilə obyekt səviyyəli məlumat hadisəsinin fərqi nədir?
- İdarəetmə hadisəsi API və hesab fəaliyyətini göstərir (məsələn, saxlanc siyasətinin dəyişməsi, `PutBucketPolicy`).
- Obyekt səviyyəli data events konkret obyektin oxunuşunu göstərir və ayrıca seçilməlidir.
- Əvvəlcədən aktiv deyilsə, sonradan logu açmaq keçmişdə yazılmamış qeydi yaratmır.
- Tək əməliyyat adından saxlancın ictimai açıldığı nəticəsi çıxmır; tam qeyd, əvvəlki vəziyyət və ictimai giriş blokları araşdırılır.
:::

:::reveal CSPM, CWPP, CASB və CNAPP üçün ayrı universitet istifadəsi göstərin.
- CSPM: konfiqurasiya tələbə uyğundurmu? Açıq baza və söndürülmüş audit aşkarlanır.
- CWPP: iş yükünün özündə risk. LMS maşınında zəif paket və şübhəli proses tapılır.
- CASB: SaaS istifadəsi. Şəxsi SaaS hesabına sənəd ötürülməsi görünür.
- CNAPP: koddan icraya qədər əlaqələndirmə. Açıq tətbiq, zəif obraz və artıq rol birlikdə qiymətləndirilir.
:::

:::reveal Replikasiya nə üçün keçmiş sağlam vəziyyətə bərpa tələbini tam ödəmir?
- Replikasiya məlumatı başqa nüsxəyə çatdırır, o cümlədən səhv silinməni və zərərli dəyişikliyi.
- Ehtiyat nüsxə keçmiş sağlam vəziyyətə qayıtmaq üçün saxlanır.
- Replikasiya yüksək əlçatanlığa (komponent düşəndə xidmət davam etsin) xidmət edir; fəlakətdən bərpa və səhvdən qayıtmaq nüsxə tələb edir.
- Versiyalaşdırma da silinmə hüquqlarının qorunmasını tələb edir; nüsxələr ayrı hesabda və dəyişməz saxlanır.
:::

:::reveal RPO və RTO hədəflərini faktiki bərpa nəticələrindən necə ayırmaq olar?
- RPO və RTO əvvəl iş sahibi tərəfindən qoyulan hədəflərdir; RPO nə qədər məlumat itirilə bilər, RTO nə qədər müddət işləməmək olar.
- Faktiki nəticə bərpa sınağında və ya insidentdə ölçülür: son nüsxədən insidentə qədər itki pəncərəsi, insidentdən bərpaya qədər dayanma.
- Nümunə: son nüsxə 09:45, insident 10:00, bərpa 11:30 → itki 15, dayanma 90 dəqiqə; RPO 5 dəqiqədirsə, tələb ödənmir.
:::

:::reveal CSA CCM üzrə nəzarətin tətbiqini hansı sübutla yoxlamaq mümkündür?
- CCM v4.1 (yanvar 2026) 17 sahədə 207 nəzarət ehtiva edir; hər nəzarətə cavabdeh, tətbiq dairəsi və yoxlama sübutu bağlanır.
- Sübut nümunələri: rol matrisi və rədd edilmiş sınaq sorğusu, sınaq hadisəsinin SIEM-də tapılması, ölçülmüş bərpa sınağı, resurs reyestri və provayder sənədi, yoxlanmış ixrac və sınaq bərpası.
- Panelin yaşıl görünməsi və ya sertifikatın mövcudluğu universitetin öz konfiqurasiyasının düzgünlüyünü sübut etmir.
:::

:::reveal Region seçimi və sınaq ixracı çıxış strategiyasında hansı sualları cavablandırır?
- Region seçimi: məlumat harada saxlanır və emal olunur (ehtiyat nüsxə, log, analitika, alt emalçılar da); məlumat yerləşməsi (data residency) və suverenlik (data sovereignty) hüquqi sualları; yerli öhdəlik hüquq mütəxəssisi ilə.
- Sınaq ixracı: kurslar, qiymətlər, fayllar və əlaqələr hansı formatda çıxır, bütövlüyü və alternativdə bərpası yoxlanır.
- Çıxış strategiyası (exit strategy) müqavilə bitməmiş hazırlanır: ixracı kim təsdiq edir, açarlar necə qorunur, alternativ mühit nə vaxt hazır olur; sonra açarlar ləğv və silinmə sübutu alınır.
:::

## Situasiya tapşırıqları

**Situasiya 1.** Qəbul şöbəsi şəxsiyyət sənədlərini obyekt saxlancına yükləyib. Saxlancda şifrələmə aktivdir, amma anonim sorğu sənədi qaytarır. Şöbə şifrələmənin tələbə məlumatını qoruduğunu deyir. Risk və ilk addımlar nədir?

:::reveal Cavab
- **Pozulan xassə:** məxfilik; səlahiyyətsiz oxunuş mümkündür, çünki xidmət məlumatı açıb anonim istifadəçiyə verir (şifrələmə giriş nəzarəti deyil).
- **İlk addımlar:** ictimai giriş bağlanır; siyasətin əvvəlki vəziyyəti və mövcud qeydlər qorunur; hansı obyektin nə vaxt əlçatan olduğu araşdırılır.
- Obyekt oxunuşu qeydə alınmayıbsa, sızmanın tam həcmi barədə əsassız hökm verilmir.
- Məlumat sahibi və insident qrupu təsirə uyğun bildiriş prosedurunu müəyyən edir.
- **Yoxlama:** hesab səviyyəli blok və anonim oxunuşun rədd sınağı əlavə edilir.
:::

**Situasiya 2.** Universitet LMS-i virtual maşından idarə olunan platformaya keçirib. Tətbiq əlavəsində icazəsiz fayl oxunuşu tapılıb. Komanda platforma yeniləmələrinin provayderdə olduğunu əsas gətirir. Düzgün bölgü necədir?

:::reveal Cavab
- Platformanın ƏS və icra mühiti üzrə öhdəlikləri kodun və əlavənin təhlükəsizliyini avtomatik əhatə etmir; bu, universitetin tərəfidir.
- Universitet əlavəni düzəldir və ya müvəqqəti ayırır, məlumat təsirini araşdırır, yerləşdirməni təhlükəsizlik sınağından keçirir.
- Provayderin dəstək işi xidmət sərhədinə görə müəyyən olunur.
- Tətbiq rolunun daraldılması oxunuş zəifliyinin başqa saxlanca yayılmasını məhdudlaşdırır.
:::

**Situasiya 3.** Kafedranın açıq kod deposunda bulud açarı tapılıb. Açar deposundan silinib, lakin hesabda tanınmayan hesablama resursları görünür. Təkcə parolu dəyişmək yetərlidirmi?

:::reveal Cavab
- Xeyr. Sızmış açar ayrıca ləğv edilir və istifadəsi ilk mümkün vaxtdan araşdırılır; hesab parolunun dəyişməsi API açarını mütləq ləğv etmir.
- Yaradılmış resurslar, rollar, başqa açarlar və məlumat əməliyyatları yoxlanır, zərərli fəaliyyət dayandırılır.
- Sübut və xərc qeydləri qorunur.
- Gələcək üçün: statik açar əvəzinə qısaömürlü iş yükü kimliyi; depoda və qurma qeydlərində başqa sirlər axtarılır.
:::

**Situasiya 4.** Şərti imtahan sistemində RPO hədəfi 5 dəqiqə, RTO hədəfi 1 saatdır. Sınaqda saat 12:00-da dayanmış xidmət 12:40-da açılıb, son bərpa olunan qeyd 11:45-ə aiddir. Tələb ödənilibmi?

:::reveal Cavab
- **RTO:** dayanma 12:00 → 12:40 = 40 dəqiqə, hədəf 1 saatdır; ödənilib.
- **RPO:** məlumat itkisi pəncərəsi 11:45 → 12:00 = 15 dəqiqə, hədəf 5 dəqiqədir; aşılıb.
- Nüsxə və jurnal qorunması, replikasiya gecikməsi və faktiki bərpa nöqtəsi araşdırılır.
- Daha tez bərpa olunmaq itirilmiş yazıları geri qaytarmır; imtahan cavablarının alternativ qeydlə bərpası ayrıca qiymətləndirilir.
:::

**Situasiya 5.** Kitabxananın sənəd çevirmə funksiyası bütün universitet saxlancına oxuma və silmə hüququ ilə işləyir. CSPM ictimai saxlanc tapmadığı üçün sistemi uyğun sayıb. Risk qalıbmı?

:::reveal Cavab
- Bəli: funksiyada kod zəifliyi və ya hadisə saxtalaşdırılması artıq səlahiyyətlərdən istifadəyə çevrilə bilər; ictimai giriş yoxlaması bu riski əhatə etmir.
- Rol yalnız çevriləcək prefiks, tələb olunan əməliyyat və düzgün hadisə mənbəyi ilə məhdudlaşdırılır.
- Təkrar hadisə, zərərli fayl, çıxış trafiki və audit sınaqları aparılır.
- İcra davranışı və kimlik riskinin müşahidəsi konfiqurasiya yoxlamasına əlavə edilir.
:::

**Situasiya 6.** LMS administratoru fişinqdən sonra hesabını itirib. İstehsalat və ehtiyat nüsxələr ayrı hesablardadır, amma eyni rol hər ikisini silə bilir. Hesabları ayırmaq nə üçün kifayət etməyib?

:::reveal Cavab
- İcazə və etibar sərhədi ayrılmayıb: ad baxımından ayrı hesablar eyni oğurlanmış kimlikdən asılı qalırsa, qoruma yoxdur.
- Rolun bərpa hesabına keçidi və silmə hüququ məhdudlaşdırılır.
- Dəyişməz saxlama, ayrıca fövqəladə giriş və qorunan açarlar yoxlanır.
- Oğurlanmış sessiyalar və yaradılmış əlavə kimliklər araşdırılır; sağlam nüsxə varsa, təcrid olunmuş mühitdə bərpa edilir.
- Gələcək üçün: insan girişində fişinqə davamlı MFA və imtiyazın məhdud müddətə verilməsi.
:::

**Situasiya 7.** Universitet SaaS LMS müqaviləsini bitirmək istəyir. Bütün faylları endirib, amma qiymətlərlə tələbə identifikatorları arasındakı əlaqə alternativ sistemdə açılmır. Çıxışın hansı hissəsi çatışmır?

:::reveal Cavab
- Texniki ixracın semantik tamlığı və alternativdə bərpa yoxlanmayıb: fayllar endirilib, əlaqələr isə yox.
- Kurs, tələbə, qiymət və fayl əlaqələri uyğun format və xəritələndirmə ilə çıxarılmalıdır.
- Nümunə kursda əlaqələr və icazələr yoxlanır, ziddiyyətlər həll edilir.
- Müqavilə bitməmiş dəstək və təkrar ixrac imkanı saxlanır.
- Mənbə məlumat yalnız uğurlu qəbul, tələb olunan saxlama və silmə qərarlarından sonra çıxarılır.
:::

## Konspektdən situasiyalar

**Situasiya 1.** Qəbul komissiyası abituriyentlərin sənədlərini ictimai buludda saxlayır. Jurnalist xəbər verir ki, bucket "public" olub və 3 000 pasport skanı axtarışda görünür. Komissiya deyir: "Bu, Amazon-un təhlükəsizlik problemidir." Haqlıdırmı?

:::reveal Cavab
- **Xeyr.** Ortaq məsuliyyət modelində bucket-in icazələri və konfiqurasiyası müştərinin, yəni universitetin məsuliyyətidir; provayder yalnız infrastrukturun təhlükəsizliyinə cavabdehdir.
- **Pozulan xassə:** məxfilik (Disclosure).
- **Dərhal:** ictimai girişi bağlamaq; əvvəlcədən aktiv edilmiş logları (CloudTrail data events, S3 server access logs) qoruyub hansı obyektlərə, nə vaxt və haradan müraciət edildiyini araşdırmaq (loglar aktiv deyildisə, bunu qeydə almaq); aidiyyəti orqanları və abituriyentləri xəbərdar etmək.
- **Gələcək üçün:** hesab səviyyəsində "Block Public Access", CSPM ilə avtomatik yoxlama, şifrələmə, minimal icazələr.
:::

**Situasiya 2.** Universitet qiymət sistemini öz serverindən əvvəlcə AWS EC2-yə (IaaS), sonra idarə olunan PaaS-a, nəhayət hazır SaaS məhsuluna keçirməyi planlaşdırır. Hər mərhələdə ƏS yamaqları, tətbiq kodunun təhlükəsizliyi və istifadəçi hesabları kimin məsuliyyətindədir?

:::reveal Cavab
- **EC2 (IaaS):** ƏS yamaqları, tətbiq kodu və hesablar universitetdə; provayder avadanlıq və virtuallaşdırmada.
- **PaaS:** ƏS və runtime yamaqları provayderə keçir; tətbiq kodu, konfiqurasiya və hesablar universitetdə qalır.
- **SaaS:** ƏS və tətbiq kodu provayderdə; istifadəçi hesabları, MFA, rollar, məlumat və paylaşma parametrləri yenə universitetdə.
- Hər mərhələdə məlumatın təsnifatı və qorunması universitetin məsuliyyətidir.
:::

**Situasiya 3.** Hücumçu universitetin bulud admin hesabını fişinqlə ələ keçirir (MFA yox idi) və həm istehsalat serverlərini, həm də eyni hesabdakı bütün ehtiyat nüsxələri silir. Bu insidentdən hansı dərslər çıxmalıdır?

:::reveal Cavab
- Admin hesabında fişinqə davamlı MFA (FIDO2) olmalı idi.
- Admin hüquqları PAM və just-in-time ilə müvəqqəti verilməli idi.
- Ehtiyat nüsxələr ayrı hesabda, ayrı icazələrlə və immutable saxlanmalı idi ki, bir hesabın ələ keçirilməsi hər ikisini məhv etməsin.
- Audit logları ayrı yerə göndərilməli və silinmədən qorunmalı idi.
- Bərpa planı RTO/RPO hədəfləri ilə müntəzəm sınanmalı idi.
- 2014-cü ildə Code Spaces şirkəti oxşar hücumdan sonra bağlanıb.
:::

## Ehtimal olunan əlavə suallar

:::reveal Ortaq məsuliyyət modelini izah edin: "security of the cloud" ilə "security in the cloud" nədir?
- Ortaq məsuliyyət (shared responsibility) təhlükəsizlik işlərinin provayderlə müştəri arasında bölünməsidir.
- Buludun təhlükəsizliyi (security of the cloud): data mərkəzi, avadanlıq, hipervizor; provayderdədir.
- Buluddakı təhlükəsizlik (security in the cloud): məlumat, hesablar, icazələr, konfiqurasiya; model dəyişdikcə müştərinin payı dəyişir, məlumat və hesablar həmişə müştəridədir.
- Bulud insidentlərinin çoxu müştərinin səhv konfiqurasiyasından və oğurlanmış hesablardan baş verir.
:::

:::reveal Dörd yerləşdirmə modelini sadalayın və hər birinə universitet nümunəsi verin.
- İctimai: tələbə poçtu Microsoft 365-də, tədqiqat hesablamaları AWS-də.
- Özəl: universitetin OpenStack/Proxmox əsasında öz buludu (üçüncü tərəf də idarə edə bilər).
- İcma: bir neçə universitetin ortaq tədqiqat buludu.
- Hibrid: tələbələrin şəxsi işləri universitetin öz data mərkəzində, portalın veb hissəsi və imtahan dövrü əlavə tutumu ictimai buludda.
:::

:::reveal RPO və RTO-nu tərif edin və hesablama nümunəsi göstərin.
- RPO (Recovery Point Objective): qəbul edilə bilən maksimum məlumat itkisi pəncərəsi; gündə bir nüsxə olarsa, 24 saatlıq dəyişiklik itə bilər.
- RTO (Recovery Time Objective): xidmətin bərpasına qədər qəbul edilən maksimum vaxt.
- Nümunə: son nüsxə 09:45, insident 10:00, bərpa 11:30. İtki 10:00 − 09:45 = 15 dəqiqə, dayanma 11:30 − 10:00 = 90 dəqiqə.
- Bunlar nəticədir; RPO 5 dəqiqə, RTO 1 saatdırsa, hər iki hədəf pozulub.
:::

:::reveal Şifrələmə ilə giriş nəzarətinin fərqi nədir?
- Şifrələmə məlumatı diskdə, surətdə və ötürmədə qoruyur; giriş nəzarəti kimin nəyə daxil ola biləcəyini təyin edir.
- Səlahiyyətli xidmət məlumatı açıb verirsə, şifrələmə yanlış avtorizasiyanı dayandırmır.
- Açıq saxlancın şifrəli olması məxfiliyin qorunduğunu göstərmir.
- Ona görə təsnifat, IAM, ictimai girişin bloklanması və şifrələmə birlikdə işlədilir.
:::

:::reveal Bulud təhlükəsizliyinin dörd tədbir qrupunu sadalayın (kimlik, məlumat, şəbəkə, görünürlük).
- Kimlik və giriş: MFA, root/qlobal admin gündəlik işlənmir, minimal səlahiyyət (IAM, RBAC), SSO və federasiya, rollar və qısaömürlü tokenlər, sirlər seyfdə (Key Vault, Secrets Manager).
- Məlumat: saxlanarkən və ötürülərkən şifrələmə (TLS 1.2+), KMS/HSM, təsnifat, DLP, ictimai paylaşmanın defolt bağlanması.
- Şəbəkə: VPC/VNet seqmentasiyası, özəl endpoint, minimal portlar, WAF və DDoS qoruması, idarəetməyə məhdud giriş; Direct Connect/ExpressRoute defolt şifrəli deyil.
- Görünürlük: audit logları aktiv və SIEM-də, CSPM, CASB (kölgə İT), CWPP.
:::

:::reveal Capital One (2019) və Snowflake (2024) hadisələrindən hansı dərslər çıxır?
- Capital One: SSRF ilə müvəqqəti rol məlumatlarına çıxış və həmin səlahiyyətlərlə saxlanc məlumatlarının götürülməsi; hadisəni sadəcə açıq saxlanc kimi təsvir etmək dəqiq deyil. Dərs: tətbiqin sorğu imkanını daralt, rolu dar saxla, qeyri-adi istifadəni izlə; metadata xidməti qorunur (IMDSv2 kömək edir, universal həll deyil).
- Snowflake: Mandiant UNC5537 araşdırmasına görə oğurlanmış kimlik məlumatları və MFA ilə qorunmayan müştəri hesabları; platformanın özünün sındırılması deyil. Dərs: güclü MFA, iş yükü kimliyi, köhnə kimlik məlumatlarının ləğvi, qeyri-adi ixracın aşkarlanması.
- Ortaq dərs: müştəri tərəfində kimlik və səlahiyyət nəzarəti.
:::

:::reveal Kölgə İT (shadow IT) nədir və necə aşkarlanır?
- Universitetin təsdiqlənmiş reyestrinə düşməyən xidmət istifadəsidir (məsələn, kafedranın öz kartı ilə SaaS alması).
- Risk: məlumat sahibi, çıxış qaydası və hesabın təhvili unudulur.
- Aşkarlama: hesablaşma uçotu, kimlik sisteminin tətbiq icazələri, şəbəkə müşahidəsi; CASB də SaaS istifadəsinə nəzarət edir.
- Sonra məsul şəxs müəyyən edilir və məlumatın harada saxlandığı araşdırılır.
:::

:::reveal LMS-in buluda köçürülməsinin mərhələlərini və qəbul meyarlarını sadalayın.
- Əvvəl asılılıqlar siyahıya alınır; məlumat sahibi RPO/RTO və giriş tələblərini təsdiqləyir; əvvəlcə məhdud kursla sınaq aparılır.
- Mərhələlər: (1) təhlükəsiz baza mühiti: hesablar, federasiya, audit arxivi, şəbəkə, xərc nəzarəti, IaC şablonları; (2) şəxsiyyətsizləşdirilmiş məlumatla funksional, yük və mənfi təhlükəsizlik sınağı; (3) məlumatın sinxronlaşması, keçid pəncərəsi və geri dönüş şərti; (4) açılış və gücləndirilmiş müşahidə, köhnə mühitin yalnız qəbuldan sonra çıxarılması.
- Qəbul meyarları: icazə sərhədləri, saxlancın anonim açılmaması, admin MFA və müvəqqəti rol, audit qeydi, ölçülmüş bərpa, kursun ixracı və alternativdə bərpası.
:::
