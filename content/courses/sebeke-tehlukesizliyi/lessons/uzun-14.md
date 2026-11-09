+++
title = "Bulud hesablamalarının əsasları və bulud təhlükəsizliyi"
unit = "uzun"
order = 14
summary = "Mühazirənin tam variantı: NIST modeli, xidmət və yerləşdirmə modelləri, ortaq məsuliyyət, IAM, şifrələmə, şəbəkə, konteyner və serverless, audit, CSPM/CWPP/CASB/CNAPP, RPO/RTO, standartlar, iki insident və LMS-in köçürülməsi."
updated = 2026-11-09

[[source]]
title = "Mühazirə 14: Bulud hesablamalarının əsasları və bulud təhlükəsizliyi"
note = "Elmar Cabbarov, 2026–2027"
+++

Bulud təhlükəsizliyinin əsas fikri sadədir: serverlər başqasının data mərkəzindədir, amma məlumatın, hesabların və konfiqurasiyanın məsuliyyəti əsasən universitetdə qalır. Mühazirə bu fikri NIST tərifindən başlayıb universitet tədris idarəetmə sisteminin (Learning Management System, LMS) buluda köçürülməsinə qədər aparır. Təhlükəsizlik, bərpa, məlumatın yerləşməsi və xərc tələbləri birlikdə baxılır. Bütün universitet adları, həcmlər və hədəflər şərti tədris nümunəsidir.

:::note Sadə dillə
Universitetin poçtu Microsoft 365-də, dərs materialları Google Drive-da, tədqiqat hesablamaları AWS-dədir. Bulud serverləri başqasının data mərkəzindədir, amma məlumatın, hesabların və konfiqurasiyanın məsuliyyəti əsasən universitetin özündə qalır.
:::

:::tip Bu mövzudan sonra bacarmalısan
NIST-in bulud tərifini, beş əsas xüsusiyyəti, xidmət və yerləşdirmə modellərini izah etməyi; ortaq məsuliyyət modelində IaaS, PaaS, SaaS üçün kimin nəyə cavabdeh olduğunu deməyi; bulud insidentlərinin əsas səbəblərini (səhv konfiqurasiya, hesab oğurluğu) və tədbirləri sadalamağı. Mühazirənin məqsədi əlavə olaraq buludu adi hostinqdən fərqləndirmək, IAM siyasətini və şəbəkə qaydasını oxumaq, açıq saxlancın riskini qiymətləndirmək, şifrələmə ilə giriş nəzarətinin fərqini göstərmək və audit qeydlərinə əsasən araşdırma aparmaqdır.
:::

## Bulud hesablamaları nədir

Bulud hesablamaları (cloud computing) konfiqurasiya edilə bilən hesablama resurslarının (şəbəkə, server, yaddaş, tətbiq, xidmət) ortaq hovuzuna şəbəkə vasitəsilə, istənilən an, tələbə uyğun və minimal idarəetmə səyi ilə giriş modelidir. Resurslar provayderlə az qarşılıqlı əlaqə ilə sürətlə ayrılır və geri qaytarılır. NIST SP 800-145 beş əsas xüsusiyyəti, üç xidmət modelini və dörd yerləşdirmə modelini müəyyən edir.

Universitetin LMS üçün virtual maşın sifariş etməsi buluddan istifadənin yalnız bir formasıdır. Eyni universitet verilənlər bazasını idarə olunan xidmət kimi ala, sənədləri obyekt saxlancında saxlaya, poçtu hazır tətbiqdən istifadə etməklə işlədə bilər. Başqasının server otağında sabit server icarəsi avtomatik bulud sayılmır.

Tərifdə "şəbəkə üzərindən" deyilir, "İnternet üzərindən" yox. Universitetin daxili şəbəkəsindən əlçatan özəl bulud da tərifə uyğun ola bilər. Əksinə, İnternetdə açılan hər tətbiq bulud deyil: ayrıca serverdə işləyən statik kafedra saytı beş xüsusiyyətin hamısını daşımaya bilər.

### Beş əsas xüsusiyyət

| Xüsusiyyət | Mənası | Universitet nümunəsi |
| --- | --- | --- |
| Tələb üzrə özünəxidmət | Müştəri resursu provayder əməkdaşının hər sifarişə müdaxiləsi olmadan panel və ya API ilə özü ayırır | Laboratoriya rəhbəri paneldən sınaq mühiti yaradır |
| Geniş şəbəkə girişi | Xidmət standart mexanizmlərlə müxtəlif cihazlardan əlçatandır | Tələbə LMS-ə noutbukdan və telefondan daxil olur |
| Resursların hovuzlaşdırılması | Resurslar bir neçə müştəri arasında tələbə görə bölüşdürülür | Kitabxananın virtual maşını ortaq hesablama hovuzundadır |
| Sürətli elastiklik | Tutum tələbatla artırılır və azaldılır, bəzən avtomatik | İmtahan vaxtı tətbiq nüsxələri artır, sonra azalır |
| Ölçülən xidmət | İstifadə ölçülür, izlənir, hesabatlandırılır; ödəniş çox vaxt buna əsaslanır ("istifadə etdikcə ödə") | Kafedra hesablama saatlarını və saxlanc həcmini görür |

**Özünəxidmət** təşkilat daxilində təsdiq qaydasının olmaması demək deyil. Universitet laboratoriyaya büdcə və kvota ayıra, yalnız təsdiqlənmiş obrazlardan maşın yaratmağa icazə verə bilər. Fərq ondadır ki, təsdiqlənmiş sərhəd daxilində sifariş avtomatik emal olunur və fiziki avadanlığın alınmasını gözləmək lazım gəlmir.

**Hovuzlaşdırma** çoxicarəçiliyi (multi-tenancy) mümkün edir: bir fiziki infrastrukturdan bir neçə müştəri istifadə edir, onların kimlikləri, yaddaşı və şəbəkələri ayrılmalıdır. Məntiqi izolyasiyanı hipervizor (hypervisor), xidmətin avtorizasiyası və şəbəkə tədbirləri birlikdə qurur. Müştəri adətən diskin dəqiq rəfini seçmir, amma müqavilə və xidmət imkanları daxilində region seçə bilər.

**Elastiklik və miqyaslanma.** Elastiklik (elasticity) tələb artanda genişlənmə və azalanda daralmadır. Miqyaslanma (scalability) sistemin artan yükü qarşılamaq qabiliyyətidir. LMS daha böyük virtual maşına keçirilirsə, bu şaquli miqyaslanmadır; bir neçə tətbiq nüsxəsinə bölünürsə, üfüqi miqyaslanmadır.

**Ölçülən xidmət** həmişə ayrıca hesab-faktura demək deyil: özəl universitet buludu istifadənin fakültələr üzrə uçotunu apara bilər. Elastik resurslar sonsuz deyil: xidmət kvotaları, region tutumu, hesab məhdudiyyətləri və büdcə var.

### Buludun idarəetmə məntiqi

Resursları yaradan və dəyişən interfeyslər idarəetmə müstəvisinə (control plane), tətbiqin gündəlik məlumat əməliyyatları məlumat müstəvisinə (data plane) aiddir. Administratorun bazanı yaratması birinciyə, LMS-in həmin bazadan qiyməti oxuması ikinciyə nümunədir. Hücumçu LMS-in giriş səhifəsinə toxunmadan oğurlanmış idarəetmə hesabı ilə bütün bazanı silə bilər, buna görə fərq təhlükəsizliyə birbaşa təsir edir.

İdarəetmə paneli və proqramlaşdırma interfeysi (Application Programming Interface, API) eyni səlahiyyətlərin müxtəlif istifadə yollarıdır.

## Yerli infrastruktur, üstünlüklər və məhdudiyyətlər

Yerli infrastrukturda (on-premises) universitet server otağını, enerji ehtiyatını, avadanlığı və proqram qatlarını özü və ya müqaviləli tərəf vasitəsilə idarə edir. Bulud həmin işlərin bir hissəsini xidmət kimi verir. Buluda keçid İT komandasının ləğvi deyil, iş bölgüsünün dəyişməsidir.

:::example Sınaq mühiti
Kafedra LMS əlavəsini buraxmazdan əvvəl keyfiyyət yoxlaması (Quality Assurance, QA) aparmalıdır. Yerli mühitdə boş tutum varsa, sınaq maşını sürətlə yaranır; yoxdursa, satınalma və quraşdırma vaxt aparır. Buludda uyğun kvota daxilində eyni quruluş avtomatik yaradıla bilər. Sınaqda real tələbə bazasının surəti əvəzinə şəxsiyyətsizləşdirilmiş və ya sintetik məlumat seçilir, əks halda sürətli qurulan mühit məlumat sızması nöqtəsinə çevrilər.
:::

### Üstünlüklər hansı şərtlərdə alınır

- **Xərc.** Bulud ilkin kapital xərcinin bir hissəsini dəyişkən əməliyyat xərcinə çevirir; provayder avadanlıq alışını və tutumun istismarını çox müştəri arasında bölür. Qənaət üçün istifadə bitəndə resurs bağlanmalıdır: dayandırılmış virtual maşının diski və ayrılmış digər resurslar ödəniş yaratmağa davam edə bilər. Kvota və büdcə yenə planlaşdırılır.
- **Coğrafi əhatə.** Yerləşdirmə xaricdəki tələbələrə gecikməni azalda bilər, lakin məlumatları düşünülmədən hər regiona köçürməyə əsas vermir; məlumatın yerləşməsi, surətləri və dəstək girişi (ehtiyat nüsxə regionu daxil) əvvəlcədən razılaşdırılır.
- **İdarə olunan xidmət** avadanlıq və əməliyyat sistemi üzrə bəzi işləri azaldır. Tətbiq məntiqi, əlavələr, icazələr və məlumat keyfiyyəti universitetin işidir. Avtomatik yenilənmə inteqrasiyanın işləyəcəyinə zəmanət vermir; inteqrasiya sınaqları xidmət versiyası dəyişəndə də aparılır.

### Məhdudiyyətlər və cavab tədbirləri

| Məhdudiyyət | Universitetdə mümkün nəticə | Planlaşdırılan tədbir |
| --- | --- | --- |
| Əlaqə və xidmət fasiləsi | Yataqxanadan imtahana giriş dayanır | Ehtiyat rabitə, çoxzonalı quruluş, bərpa sınağı |
| Məxfilik riski | Sənədlər səhv paylaşılır | Təsnifat, minimal icazə, paylaşma nəzarəti |
| Hücum səthi | Panel, API və hesablar hədəflənir | MFA, təhlükəsiz kod, audit və cavab planı |
| Məhdud texniki nəzarət | SaaS bazasına birbaşa giriş mümkün deyil | İxrac imkanını və dəstəyi əvvəlcədən yoxlamaq |
| Provayderə bağlılıq | LMS məlumatını başqa xidmətə daşımaq çətinləşir | Portativ format, çıxış sınağı, müqavilə şərti |
| Dəyişkən xərc | Unudulmuş laboratoriya maşınları büdcəni aşır | Kvota, xərc xəbərdarlığı, resurs sahibi və bitmə tarixi |

### Xərc, xidmət səviyyəsi və nəzarət

Ümumi sahibolma xərcinə (Total Cost of Ownership, TCO) hesablama, saxlanc, trafik, lisenziya, dəstək, audit və əmək daxildir; təhlükəsizlik qeydlərinin saxlanması və məlumatın provayderdən çıxarılması da hesablanır. Buludun və ya özəl infrastrukturun həmişə daha ucuz olması barədə universal qayda yoxdur: sabit yük, mövcud avadanlıq və təcrübəli komanda bir seçimə, mövsümi yük və məhdud fiziki tutum digərinə üstünlük verə bilər.

:::example Şərti xərc hesabı
Laboratoriya üçün saatlıq resurs qiyməti 0,20 manat, istifadə ayda 100 saatdırsa, hesablama hissəsi 0,20 × 100 = 20 manat edir. Resurs unudulub 720 saat işləsə, 0,20 × 720 = 144 manat olar. Rəqəmlər real tarif deyil; saxlanc, trafik və vergilər hesabda yoxdur. Nümunə istifadəyə görə ödənişin öz-özünə qənaət yaratmadığını göstərir. Xərc xəbərdarlığı çox vaxt xərci dayandıran sərt limit deyil.
:::

Xidmət səviyyəsi razılaşması (Service Level Agreement, SLA) ölçülən əlçatanlığı, istisnaları və öhdəlik pozulanda tətbiq edilən şərtləri müəyyən edir. Xidmət krediti itirilmiş imtahanı bərpa etmir. Universitetin tələbəyə vədi provayderin bir komponent üçün vədindən fərqlənir: DNS, kimlik xidməti, rabitə və tətbiq də əlçatanlıq zəncirindədir.

## Buludun yerləşdirmə modelləri

Yerləşdirmə modeli infrastrukturu kimlərin istifadəsi üçün təşkil etdiyini göstərir və xidmət modelindən ayrıdır. İctimai buludda infrastruktur, platforma və hazır proqram xidməti də almaq olar; özəl buludun yalnız virtual maşınlardan ibarət olması da tələb deyil.

| Model | Tərif (NIST) | Universitet nümunəsi | İdarəetmə məsələsi |
| --- | --- | --- | --- |
| İctimai bulud (public cloud) | Provayderin infrastrukturu geniş ictimaiyyət üçün təklif olunur; hər müştərinin resursları məntiqi ayrılır | Tələbə poçtu Microsoft 365-də, tədqiqat hesablamaları AWS-də; LMS-in kommersiya provayderində yerləşməsi | Hesabların və resursların məntiqi ayrılması |
| Özəl bulud (private cloud) | Yalnız bir təşkilat üçün infrastruktur; universitetin özündə və ya üçüncü tərəfdə ola bilər | Universitet data mərkəzində OpenStack/Proxmox əsasında öz buludu | Tutum, yeniləmə və operatorun məsuliyyəti |
| İcma buludu (community cloud) | Ortaq maraqları və tələbləri olan təşkilatlar qrupu üçün | Bir neçə universitetin ortaq tədqiqat buludu | Üzvlük, məlumat sahibliyi, ortaq qaydalar |
| Hibrid bulud (hybrid cloud) | Müstəqil qalan iki və ya daha çox bulud infrastrukturunun, məlumat və tətbiqlərin onlar arasında daşınmasına imkan verən texnologiyalarla əlaqələndirilməsi | Tələbələrin şəxsi işləri universitetin öz data mərkəzində, portalın veb hissəsi və imtahan dövründəki əlavə tutum ictimai buludda | Sərhədlərarası kimlik, rabitə və bərpa |

### İctimai və özəl bulud

İctimai buludda xidmətin hamıya təklif olunması müştəri məlumatının hamıya açıq olması demək deyil. Şəxsi sənədlər orada da yalnız səlahiyyətli istifadəçilərə açılmalıdır. Təhlükəsizlik izolyasiya, icazələr, konfiqurasiya və nəzarətdən asılıdır. İctimai saxlanc ayrıca konfiqurasiya qərarıdır; bu iki anlayışı qarışdırmaq səhv risk qiymətləndirməsinə gətirir.

Özəl bulud bir təşkilat üçündür, lakin onu mütləq universitetin İT şöbəsi idarə etmir: üçüncü tərəf operator ola bilər, infrastruktur universitet ərazisindən kənarda yerləşə bilər. Fərqli fakültələr eyni özəl buludda ayrıca resurs qrupları işlədə bilər. Daha çox fərdiləşdirmə daha çox istismar işi yaradır. Özəl adlandırılan mühitdə yamaqlar gecikirsə və ehtiyat nüsxə yoxlanmırsa, adın özü təhlükəsizlik vermir.

Özəl bulud köhnə laboratoriya avadanlığına yaxınlıq və xüsusi inteqrasiya üçün uyğundur, lakin köhnə proqramın zəifliklərini aradan qaldırmır; hovuzu böyütmək əlavə avadanlıq və enerji tələb edir.

### İcma, hibrid və çoxbuludlu istifadə

**İcma buludunda** bir neçə universitet ortaq etik, təhlükəsizlik və tədqiqat tələbləri ilə resurs paylaşır. Xərc və ekspertiza bölüşdürülür, amma məlumatı kimin təsdiqi ilə silmək və üzv ayrıldıqda nə etmək qaydaları əvvəlcədən yazılır. İcma daxilində də ayrıca avtorizasiya sərhədləri var.

**Hibrid bulud** üçün bütün yerləşdirmə növlərini birləşdirmək tələb olunmur. NIST tərifində iki və ya daha çox müstəqil bulud arasında məlumat və tətbiqin daşınmasına imkan verən texnologiya nəzərdə tutulur. Özəl buluddakı LMS imtahan vaxtı ictimai buludda əlavə tətbiq nüsxələri işlədə bilər; bunun üçün sessiyalar, fayllar və baza əlaqəsi əvvəlcədən uyğunlaşdırılır. Sadəcə yerli serverlə bir SaaS abunəsinin yanaşı olması bu tərifi tam izah etmir. Hibrid rabitə ictimai İnternetdən, VPN-dən və ya xüsusi bağlantıdan keçə bilər; ötürmənin mütləq yavaş olduğu doğru deyil.

**Çoxbuludlu istifadə (multi-cloud)** bir neçə provayderin xidmətlərindən istifadədir və NIST-in beşinci yerləşdirmə modeli deyil. Poçt bir provayderdən, hesablama digərindən ala bilər. Asılılığı azalda bilər, amma kimlik, audit və bacarıq tələbini artırır; iki buludda eyni tətbiq yalnız məlumat, açar və bərpa asılılıqları da ayrıldıqda kömək edir.

:::warning Hibrid ilə çoxbuludlu eyni deyil
Hibrid: iki müstəqil bulud arasında məlumat və tətbiqin daşınmasını təmin edən texnologiya. Çoxbuludlu: sadəcə bir neçə provayderdən istifadə. Universitet nümunəsi: özəl bulud ilə ictimai bulud arasında imtahan dövründə tutum artımı hibriddir; poçtun bir provayderdə, hesablamanın digərində olması çoxbuludludur.
:::

:::note Köhnə slaydlarla fərq
Köhnə slaydlarda belə deyilirdi, düzgün variantlar isə bunlardır. "İctimai bulud açıq olduğuna görə daha az təhlükəsizdir": səhvdir, "ictimai" xidmətin hamıya təklif olunması deməkdir. Özəl bulud mütləq təşkilatın öz İT şöbəsində olmur, onu müəyyən edən yalnız bir təşkilatın istifadəsidir. Hibrid üç növün birləşməsi deyil, texnologiya ilə əlaqələndirilmiş iki və ya daha çox müstəqil buluddur; məlumat ötürülməsi mütləq yavaş və ya ictimai İnternetdən keçmir. "İctimai bulud özəldən bahadır" kimi universal sıralama yoxdur; "limitsiz resurs" da yoxdur, kvota və büdcə var. Buluda keçmək "bütün riskləri autsorsinq etmək" deyil, məsuliyyət müştəridə qalır. IaaS-ın tipik ödəniş modeli "istifadəçi başına" yox, resurs istifadəsinə görədir (instansiya saatı, yaddaş, trafik). Tərifdə "İnternet", yox "şəbəkə" deyilir.
:::

## Xidmət modelləri və ortaq məsuliyyət

**İnfrastruktur xidmət kimi (Infrastructure as a Service, IaaS)** hesablama, saxlanc və şəbəkə resursları verir. Universitet qonaq əməliyyat sistemini, tətbiqləri və onların sazlanmasını idarə edir. Nümunə: Amazon EC2, Azure Virtual Machines. İstifadəçi başına ödəniş IaaS-ın müəyyənedici əlaməti deyil; hesablama vaxtı, tutum və trafik işlədilir.

**Platforma xidmət kimi (Platform as a Service, PaaS)** tətbiqi yerləşdirmək üçün idarə olunan icra mühiti verir. Provayder infrastruktur və platformanın istismarını götürür; universitet tətbiq kodunu, asılılıqları, məlumatı və xidmət parametrlərini idarə edir. Nümunə: Azure App Service, Google App Engine, Heroku.

**Proqram təminatı xidmət kimi (Software as a Service, SaaS)** hazır tətbiq verir: Microsoft 365, Google Workspace. Universitet server koduna və əməliyyat sisteminə yamaq qurmur, amma hesabların həyat dövrünü, paylaşmanı, rolları və məlumat istifadəsini idarə edir.

| Meyar | IaaS | PaaS | SaaS |
| --- | --- | --- | --- |
| Alınan imkan | Virtual maşın, disk, şəbəkə | Tətbiq icra platforması | Hazır tətbiq funksiyaları |
| Universitetin əsas işi | Əməliyyat sistemi və bütün tətbiq qatı | Kod, asılılıqlar, konfiqurasiya | Hesablar, məlumat, istifadə qaydaları |
| Uyğun iş | Xüsusi quruluşlu laboratoriya serveri | Universitetin hazırladığı portal | Poçt və sənəd əməkdaşlığı |
| Çevikliyin sərhədi | Qonaq sistemdə geniş nəzarət | Platformanın dəstəklədiyi mühit | Provayderin verdiyi funksiyalar |
| Tipik xərc ölçüsü | Resurs vaxtı və həcmi | Plan, instansiya və istifadə | Abunə, istifadəçi və ya istifadə |

### Ortaq məsuliyyətin sərhədləri

Ortaq məsuliyyət (shared responsibility) təhlükəsizlik işlərinin provayderlə müştəri arasında bölünməsidir. Buludun fiziki və baza xidmət qatının təhlükəsizliyi (security of the cloud: data mərkəzi, avadanlıq, hipervizor) əsasən provayderdədir. Buludda qurulan sistemin təhlükəsizliyi (security in the cloud: məlumat, hesablar, icazələr, konfiqurasiya) seçilən modeldən asılı olaraq universitetin işidir. Müqavilə, xidmətin xüsusiyyətləri və idarə olunan əlavə komponentlər sərhədi dəyişə bilər. Ən sadə yığma sxem: on-premises hamısı müştəridə; IaaS-da fiziki data mərkəzindən virtuallaşdırmaya qədər provayderdə, əməliyyat sistemindən yuxarısı müştəridə; PaaS-da runtime və middleware də provayderə keçir; SaaS-da tətbiqin özü də provayderdədir. Məlumat və hesablar bütün modellərdə müştəridə qalır.

| İş sahəsi | IaaS | PaaS | SaaS |
| --- | --- | --- | --- |
| Fiziki bina, enerji, avadanlıq | Provayder | Provayder | Provayder |
| Hipervizor və əsas infrastruktur | Provayder | Provayder | Provayder |
| Qonaq əməliyyat sisteminin yamaqları | Universitet | Provayder | Provayder |
| İcra mühiti və platforma yamaqları | Universitet | Provayder, dəstək sərhədi üzrə | Provayder |
| Universitetin tətbiq kodu və əlavələri | Universitet | Universitet | Əsas tətbiq provayderdə, inteqrasiyalar universitetdə |
| Hesablar, rollar, MFA siyasəti | Universitet siyasəti, provayder mexanizmi | Universitet siyasəti, provayder mexanizmi | Universitet siyasəti, provayder mexanizmi |
| Məlumatın təsnifatı və qanuni istifadəsi | Universitet | Universitet | Universitet |
| Şifrələmənin texniki işi və sazlanması | Xidmətə görə bölünür | Xidmətə görə bölünür | Xidmətə görə bölünür |
| Audit və bərpa tələblərinin seçilməsi | Universitet, provayder imkanları ilə | Universitet, provayder imkanları ilə | Universitet, provayder imkanları ilə |

Cədvəl provayderin məlumatın qorunmasına görə heç bir öhdəliyi olmadığı demək deyil. Provayder öz xidmətinin izolyasiyasını və müqavilədəki tədbirləri işlətməlidir. Universitet isə məlumatı həmin xidmətə vermək qərarına, istifadə qaydalarına və öz konfiqurasiyasına cavabdehdir.

:::tip Yadda saxla: ortaq məsuliyyət
Provayder buludun təhlükəsizliyinə (security of the cloud), müştəri buluddakı təhlükəsizliyə (security in the cloud) cavabdehdir. IaaS-da qonaq ƏS-in yamaqları da müştəridədir. SaaS-da belə istifadəçi hesablarını, MFA-nı və paylaşma parametrlərini müştəri idarə edir. Bulud insidentlərinin çoxu provayderin sındırılmasından yox, müştərinin səhv konfiqurasiyasından və oğurlanmış hesablardan baş verir.
:::

### Bir LMS üçün üç fərqli seçim

LMS virtual maşında qurulursa, universitet əməliyyat sistemi, veb server, tətbiq və əlavələr üçün yamaq planı saxlayır. Eyni kod idarə olunan platformaya keçiriləndə baza əməliyyat sisteminin yamaqları provayderə keçir; kodun təhlükəli fayl yükləməsi və ya artıq icazəli baza hesabı yenə universitetin problemidir. Hazır LMS SaaS seçiləndə əsas proqramın yenilənməsi provayderdə olur, amma yanlış kurs rolu ilə bütün qiymətlərin görünməsi universitetin konfiqurasiya məsələsi qala bilər.

Bir həll daxilində modellər qarışa bilər: tətbiq IaaS-da, baza idarə olunan xidmətdə, poçt göndərişi başqa xidmətdə. Buna görə bütün sistemə bir dəfə IaaS etiketi yapışdırmaq məsuliyyəti izah etmir. Aktiv reyestrində hər komponentin sahibi, modeli, məlumatı və bərpa qaydası ayrıca göstərilir.

:::warning Ehtiyat nüsxə xidməti bərpa sübutu deyil
Müqavilədə ehtiyat nüsxə xidmətinin olması universitetin bərpanı yoxlamaq işini aradan qaldırmır. Provayder disk səviyyəsində bərpa verə bilər, universitetə isə müəyyən tələbənin səhv silinmiş tapşırığı lazım ola bilər. Bərpanın səviyyəsi və müddəti xidmət seçilməzdən əvvəl yoxlanır.
:::

## Buludda təhdid modeli və təhlükəsizlik sərhədləri

Təhdid modeli (threat model) qorunan aktivləri, etibar sərhədlərini, hücumçunun imkanlarını və mümkün zərəri əlaqələndirir. Universitet üçün aktiv yalnız virtual maşın deyil: tələbə bazası, imtahan sualları, idarəetmə tokeni, ehtiyat nüsxə və hesablaşma büdcəsi də aktivdir. Məxfilik pozula, qiymətlər dəyişdirilə, imtahan xidməti dayandırıla bilər.

LMS-ə sənəd yükləyən tələbəyə yalnız həmin kurs daxilində əməliyyat icazəsi verilir, tətbiqin saxlanc rolu isə faylları oxuyur və yazır. Bu iki kimliyi qarışdırmaq olmaz. Tətbiqdəki zəiflik hücumçuya rolun bütün səlahiyyətlərini işlətmək imkanı verə bilər; ona görə həm istifadəçinin əməliyyatı tətbiqdə yoxlanır, həm tətbiq rolunun təsir sahəsi dar saxlanır.

### Əsas risklər (konspekt xülasəsi)

| Risk | Nümunə |
| --- | --- |
| Səhv konfiqurasiya | Açıq S3 bucket, "linki olan hər kəs" paylaşması, İnternetə açıq verilənlər bazası, hər yerdən SSH-ə icazə verən security group |
| Hesabın ələ keçirilməsi | Admin hesabında MFA yoxdur; root hesabı gündəlik işlədilir |
| Sızmış açarlar | Tələbə layihəsində AWS açarı GitHub-a yüklənir, bir neçə dəqiqəyə botlar tapıb kriptomayner serverləri açır |
| Artıq icazələr | Xidmət hesabına "AdministratorAccess" verilib |
| Təhlükəsiz olmayan API-lər | Autentifikasiyasız və ya sürət məhdudiyyətsiz API |
| Məlumatın yeri və hüquqi tələblər | Fərdi məlumatların saxlandığı ölkə, çıxış planının olmaması, təminatçıya bağlılıq |
| Əlçatanlıq | Provayderin regional kəsintisi; bütün sistemlər bir zonadadır |

### Təhdiddən tədbirə

| Təhdid | Zəif quruluş | Birinci tədbir | Yoxlama sübutu |
| --- | --- | --- | --- |
| Hesabın ələ keçirilməsi | Admin hesabı yalnız parolla açılır | Fişinqə davamlı MFA və sessiya nəzarəti | Giriş siyasəti və sınaq qeydi |
| Məlumat sızması | Saxlanc anonim oxunuşa açıqdır | İctimai girişin qadağası | Siyasət və anonim sorğunun rəddi |
| İmtiyazdan sui-istifadə | LMS rolunda bütün resurslara icazə var | Resurs və əməliyyat üzrə dar siyasət | İcazə və rədd sınaqları |
| Məlumatın silinməsi | Eyni hesab bütün surətləri silir | Ayrı bərpa sərhədi və dəyişməz saxlama | Bərpa və silmə məhdudiyyəti sınağı |
| Xərclərin şişməsi | Kvotasız resurs yaratma hüququ | Kvota, təsdiq və xərc nəzarəti | Limit və xəbərdarlıq yoxlaması |

Konfiqurasiya xətası həmişə hücumla başlamır: qəbul şöbəsi sənəd paylaşmasını asanlaşdırmaq üçün anonim keçid aça bilər, hücumçu isə belə səhvdən sonradan istifadə edir. Təhlükəsiz başlanğıc parametrləri, avtomatik yoxlama və əməkdaşın işinə uyğun alternativ kanal xətanın ehtimalını azaldır.

Gizli İT (shadow IT) universitetin təsdiqlənmiş reyestrinə düşməyən xidmət istifadəsidir. Kafedra öz kartı ilə SaaS alanda məlumatın sahibi, çıxış qaydası və hesabın təhvil verilməsi unudula bilər. Aktivlərin aşkarlanması hesablaşma uçotu, kimlik sisteminin tətbiq icazələri və şəbəkə müşahidəsi ilə tamamlanır; aşkarlanan xidmət üçün məsul şəxs müəyyən edilir və məlumatın harada saxlandığı araşdırılır.

## Kimlik və girişin idarəsi

Kimlik və girişin idarəsi (Identity and Access Management, IAM) kimin hansı şərtlərlə hansı əməliyyatı edə biləcəyini müəyyən edir. Autentifikasiya kimliyi yoxlayır, avtorizasiya əməliyyata icazəni qiymətləndirir. Buludda kimlik insan hesabı, virtual maşının rolu, konteynerin xidmət hesabı və ya yerləşdirmə prosesinin tokeni ola bilər.

### Federasiya, rollar və minimal səlahiyyət

Universitet vahid girişdən (Single Sign-On, SSO) istifadə etdikdə əməkdaş ayrıca bulud parolu yaratmadan təşkilatın kimlik provayderi (Identity Provider, IdP) ilə daxil olur. Federasiya bir sistemdə təsdiqlənən kimliyin digərində qəbul edilməsidir; SAML və OpenID Connect bu məqsədlə işlədilir. Etibar konfiqurasiyası, tokenin ünvanlandığı xidmət və imzası yoxlanmalıdır. SSO öz-özünə doğru rol bölgüsü yaratmır.

Rol əsaslı giriş nəzarəti (Role-Based Access Control, RBAC) icazələri vəzifəyə bağlayır. Atribut əsaslı nəzarət (Attribute-Based Access Control, ABAC) şöbə, mühit, resurs etiketi və sessiya şərtlərindən istifadə edir. Kafedra əməkdaşının sınaq mühitini idarə etməsi istehsalat LMS-inə giriş verməməlidir. Etiketə əsaslanan siyasətdə etiketi dəyişmək hüququ da qorunur: istifadəçi resursa özbaşına uyğun etiket verə bilirsə, məhdudiyyətdən yan keçə bilər.

Minimal səlahiyyət (least privilege) vəzifənin tələb etdiyi ən dar icazədir. LMS-in tapşırıq oxuyan hissəsinə bütün saxlancı silmək hüququ lazım deyil. İcazə əməliyyat, resurs, mühit və vaxt üzrə daraldılır. Hansı kimliklərin hansı şərtlərlə rolu qəbul edə biləcəyini müəyyən edən etibar siyasəti də ayrıca yoxlanır: dar icazəli rolu hər kəs qəbul edə bilirsə, qoruma yenə natamamdır. Beləliklə, icazə siyasəti "rol nə edə bilər", etibar siyasəti "rolu kim qəbul edə bilər" sualına cavab verir.

Şərti unec-lms-example saxlancının yalnız assignments/ hissəsindəki obyektlərin oxunmasına icazə verən AWS IAM fraqmenti:

```json
{ "Version": "2012-10-17", "Statement": [{ "Effect": "Allow", "Action": "s3:GetObject", "Resource": "arn:aws:s3:::unec-lms-example/assignments/*" }] }
```

Bu, tam giriş modeli deyil: tətbiqin istifadəçi üzrə yoxlamaları, rolun etibar siyasəti və lazım olan digər əməliyyatlar ayrıca layihələndirilir. GetObject obyekt oxunuşudur; siyahılama və yazma verilməyib. Tam effektiv icazə yalnız bu sənədlə müəyyən olunmur: digər kimlik və resurs siyasətləri, təşkilat məhdudiyyətləri və açar siyasəti də qiymətləndirilir. AWS-də uyğun açıq rədd (explicit deny) icazəni üstələyə bilər. Sınaqda icazəli faylın oxunması ilə yanaşı, başqa prefiksin və silmə əməliyyatının rədd edilməsi də yoxlanır.

### İnsan hesabları və imtiyazlı giriş

Çoxfaktorlu autentifikasiya (Multi-Factor Authentication, MFA) fərqli amilləri birləşdirir. Administrator üçün FIDO2 təhlükəsizlik açarı və ya uyğun passkey kimi fişinqə davamlı üsullar üstün tutulur; SMS kodu və bildirişin kor-koranə təsdiqi eyni müqaviməti vermir. MFA olsa da, oğurlanmış sessiya tokeni risk yaradır, ona görə cihazın vəziyyəti, sessiyanın müddəti və riskli girişə yenidən təsdiq tələbi də nəzərdən keçirilir.

Əsas hesab (root account) və qlobal administrator gündəlik iş üçün işlədilmir. İmtiyazlı girişin idarəsi (Privileged Access Management, PAM) vasitəsilə səlahiyyət iş üçün və məhdud müddətə verilə bilər (just-in-time). Fövqəladə giriş hesabı ayrıca qorunur, istifadəsi xəbərdarlıq yaradır və bərpa prosedurunda yoxlanır. Əsas IdP dayananda bütün idarəetmə yollarının bağlanması da əlçatanlıq riskidir.

Ayrılan əməkdaşın hesabının bağlanması yalnız parol dəyişməsi ilə bitmir: bulud rolları, davam edən sessiyalar, API açarları və razılıq verilmiş tətbiqlər araşdırılır. Paylaşılan administrator hesabı fərdi hesabatlılığı zəiflədir.

### Xidmət kimlikləri, açarlar və sirlər

Tətbiqlərə uzunmüddətli statik açar əvəzinə iş yükü kimliyi (workload identity), idarə olunan kimlik və qısaömürlü token verilir. LMS öz roluna əsasən müvəqqəti kimlik məlumatı alır və açarı kodda ya diskdə saxlamaq ehtiyacı azalır. Müvəqqəti token də müddəti bitənədək təhlükəlidir.

Sirlər idarəetmə xidmətində, məsələn, AWS Secrets Manager və ya Azure Key Vault-da saxlanır. Bazanın parolu konteyner obrazına, Git deposuna və loga yazılmır. Açar sızıbsa, depodakı sətri silmək kifayət etmir: açar ləğv edilir, istifadəsi araşdırılır, artıq yaradılmış resurs və kimliklər yoxlanır.

:::figure
src = "m14-1.png"
alt = "Universitet kimliyindən (IdP, MFA) SAML/OIDC etibarı ilə qısa müddətli bulud roluna və yalnız lazım olan resursa keçid; rol ayrı audit hesabındakı audit axınına, oradan dəyişdirilə bilməyən saxlanca yazır."
caption = "Şəkil 1. Universitet kimliyindən məhdud bulud roluna keçid və ayrıca qorunan audit axını"
:::

## Məlumatların və açarların qorunması

Qorunma təsnifatla başlayır: dərs cədvəli ilə şəxsiyyət sənədinin surətinə eyni paylaşma qaydası tətbiq olunmur. Məlumatın sahibi hansı məqsədlə toplandığını, kimlərin görməli olduğunu və nə vaxt silinməli olduğunu müəyyən edir; təhlükəsizlik komandası bu qərarı saxlanc, IAM və audit parametrlərinə çevirir.

| Sinif | Nümunə | Giriş qaydası | Saxlama tədbiri |
| --- | --- | --- | --- |
| Açıq | Elan və dərc edilmiş dərs cədvəli | Təsdiqlənmiş ictimai oxunuş | Dəyişiklik icazəsi məhdud, nüsxə saxlanır |
| Daxili | Kafedranın iş sənədləri | Təşkilat hesabı və qrup | Xarici paylaşma nəzarətdədir |
| Məxfi | Tələbənin qiyməti və şəxsi işi | Vəzifə və konkret ehtiyac üzrə | Şifrələmə, audit, məhdud ixrac |
| Ciddi məhdud | İmtahan sualları və əsas sistem sirləri | Dar rol, güclü təsdiq | Ayrı açar və icazə sərhədi |

### Açıq obyekt saxlancı və yanlış paylaşma

Obyekt saxlancı (object storage) faylı obyekt kimi saxlayır; konteyner bəzi xidmətlərdə bucket adlanır. Obyektin adının çətin təxmin edilməsi giriş nəzarəti deyil. İctimai siyasət, girişə nəzarət siyahısı (Access Control List, ACL), SaaS paylaşma keçidi və müvəqqəti imzalı URL fərqli mexanizmlərdir və hər biri ayrıca yoxlanır. İmzalı keçidi alan şəxs müddəti və səlahiyyəti daxilində obyekti oxuya bilər; belə keçid loglarda və məktub yönləndirmələrində yayılmamalıdır.

Qəbul şöbəsinin sənədləri defolt olaraq özəl saxlanılır. İctimai girişin hesab səviyyəsində bloklanması təsadüfi açılmaya qarşı əlavə sərhəddir. Açıq dərs materialları üçün ayrıca saxlanc qarışmanı azaldır.

Şərti saxlanc üçün konfiqurasiyanı oxuyan AWS CLI əmrləri (dərsdə təhlil üçün; istehsalatda uyğun səlahiyyət və profil tələb olunur):

```bash
aws s3api get-public-access-block --bucket unec-lms-example
aws s3api get-bucket-policy-status --bucket unec-lms-example
aws s3api get-bucket-encryption --bucket unec-lms-example
```

Birinci əmr ictimai giriş bloklarının vəziyyətini, ikinci xidmətin siyasəti necə qiymətləndirdiyini, üçüncü şifrələmə parametrlərini göstərir. Heç biri təkbaşına bütün effektiv girişin sübutu deyil: hesab səviyyəli bloklar, obyekt ACL-ləri, digər hesabların icazələri və imzalı keçidlər də baxılır. Konfiqurasiya yoxlaması anonim oxunuşun və icazəsiz rolun rədd edilməsinə dair sınaqla tamamlanır.

### Şifrələmə və KMS

Ötürülən məlumat TLS ilə, saxlanan məlumat xidmətin disk, baza və ya obyekt şifrələməsi ilə qorunur. Uyğun konfiqurasiyada TLS 1.2 və TLS 1.3 işlədilə bilər. TLS 1.3 üçün iyul 2026 tarixli RFC 9846 əsas istinaddır; əvvəlki mənbələr RFC 8446-ya istinad edir.

Saxlanarkən şifrələmə diskin və ya surətin icazəsiz əldə edilməsinə qarşı tədbirdir. Səlahiyyətli xidmət məlumatı açıb verirsə, şifrələmə yanlış avtorizasiyanı dayandırmır. LMS roluna bütün tələbə sənədlərini oxumaq hüququ verilibsə, server tərəfli şifrələmə bu hüququ daraltmır; açıq saxlancın şifrəli olması da məxfiliyin qorunduğunu göstərmir.

Açar idarəetmə xidməti (Key Management Service, KMS) açar yaratma, istifadə icazələri, audit və həyat dövrü funksiyalarını verir. Zərf üsulu ilə şifrələmədə (envelope encryption) məlumat məlumat açarı (Data Encryption Key, DEK) ilə şifrələnir; DEK ayrıca açar şifrələmə açarı (Key Encryption Key, KEK) ilə qorunur. Şifrəli obyektlə yanaşı şifrəli DEK saxlanıla bilər. KEK-in qorunması çoxlu obyektin açılmasına təsir edir.

:::figure
src = "m14-2.png"
alt = "KMS-dəki əsas açar (heç vaxt çıxmır) məlumat açarı DEK-i şifrələyir; DEK açıq məlumatı tətbiqdə şifrələyir; saxlancda şifrəli DEK və şifrəli məlumat birlikdə durur."
caption = "Şəkil 2. Zərf üsulu ilə şifrələmədə məlumat açarının və KMS icazəsinin ayrılması"
:::

### BYOK, açarların həyat dövrü və DLP

Öz açarını gətirmə (Bring Your Own Key, BYOK) müştərinin yaratdığı açar materialını bulud xidmətinə gətirməsidir; açarın mənşəyinə və həyat dövrünə nəzarəti artıra bilər. Açarın provayder xidmətində işlədilməsi zamanı provayderin məlumatı texniki olaraq heç vaxt aça bilməməsi barədə ümumi nəticə çıxarmaq olmaz; xidmətin arxitekturası və etibar modeli ayrıca araşdırılır. Aparat təhlükəsizlik modulu (Hardware Security Module, HSM) da tətbiqin icazələrini əvəz etmir.

Açar idarəçisi ilə məlumat oxuyan rolun ayrılması vəzifələrin ayrılmasıdır. Açarın istifadəsi, rotasiyası, söndürülməsi, silinmə gözləməsi və bərpası sənədləşdirilir. Rotasiya köhnə ehtiyat nüsxənin açılmasına mane olmamalıdır. Açarın itməsi məlumatı silinmədən əlçatmaz edə bilər; kriptoqrafik silmədə bütün açar surətləri və saxlanmış açıq məlumat nəzərə alınır.

Məlumat sızmasının qarşısının alınması (Data Loss Prevention, DLP) həssas məzmunun icazəsiz ötürülməsini aşkarlayır və siyasətə görə bloklayır; məsələn, tələbə siyahısının şəxsi poçta göndərilməsini məhdudlaşdırır. Etiket, məzmun nümunəsi və sənəd izi birlikdə işlədilir. Səhv aşkarlama legitim işi dayandıra bilər, ona görə qayda əvvəlcə müşahidə rejimində sınanır; DLP ekran şəklini və bütün şifrəli kanalları mütləq görmür.

:::exam Şifrələmə giriş nəzarəti deyil
Saxlancda şifrələmə aktivdirsə və anonim sorğu sənədi qaytarırsa, risk qalır: xidmət məlumatı açıb anonim istifadəçiyə verir. Şifrələmə diski və surəti qoruyur, yanlış avtorizasiyanı yox.
:::

:::reveal DEK, KEK, KMS və BYOK bir-biri ilə necə əlaqəlidir?
Məlumat DEK ilə şifrələnir; DEK özü KEK ilə qorunur və şifrəli DEK şifrəli obyektlə yanaşı saxlanır. KEK KMS-də yaradılır, icazələri və auditi KMS verir. BYOK-da açar materialını müştəri yaradıb xidmətə gətirir. HSM açarların aparat səviyyəsində qorunmasıdır, amma tətbiqin icazələrini əvəz etmir.
:::

## Bulud şəbəkəsinin təhlükəsizliyi

Virtual özəl bulud (Virtual Private Cloud, VPC) və Azure terminologiyasında virtual şəbəkə (Virtual Network, VNet) məntiqi şəbəkə sərhədi yaradır. Alt şəbəkə, marşrut, təhlükəsizlik qaydası və xidmət endpoint-i birlikdə trafikin yolunu müəyyən edir. Alt şəbəkəyə özəl adı vermək onu qorumağa yetmir: ictimai IP, İnternetə marşrut və icazə qaydaları faktiki əlçatanlığı dəyişir.

LMS üçün giriş qatı, tətbiq qatı və baza ayrılır. İstifadəçi yalnız giriş qatına HTTPS ilə qoşulur. Tətbiq bazaya öz kimliyi və məhdud şəbəkə yolu ilə gedir; bazaya ictimai ünvan verilmir. İdarəetmə girişi təşkilatın qorunan giriş xidmətindən keçir.

### Təhlükəsizlik qrupları və qaydaların oxunması

Şəbəkə təhlükəsizlik qrupu (security group) resursa və ya interfeysə tətbiq olunan trafik qaydaları dəstidir. Termin və davranış provayderlər arasında fərqlənir. AWS security group vəziyyəti izləyir (stateful) və icazə qaydaları ilə işləyir, ayrıca rədd qaydası vermir. Azure NSG-də prioritetli icazə və rədd qaydaları var.

Şərti LMS trafik matrisi:

| Mənbə | Hədəf | Protokol və port | Əsaslandırma |
| --- | --- | --- | --- |
| İnternet istifadəçisi | Giriş balanslaşdırıcısı | TCP 443 | LMS-in HTTPS xidməti |
| Giriş qrupundakı resurs | Tətbiq qrupu | TCP 8443 | Şərti daxili HTTPS portu |
| Tətbiq qrupu | PostgreSQL bazası | TCP 5432 | Yalnız LMS baza bağlantısı |
| Qorunan idarəetmə xidməti | Tətbiq maşını | TCP 22 | Yalnız təsdiqlənmiş inzibatçılıq |
| Tətbiq qrupu | Özəl saxlanc endpoint-i | TCP 443 | Fayl xidməti ilə qorunan əlaqə |
| Digər mənbələr | Baza | Bütün portlar | İcazə verilməyən trafik buraxılmır |

Portun açılması tətbiq icazəsi deyil: TCP 443-dən verilən zəif API hücumu həmin şəbəkə qaydasından keçə bilər. PostgreSQL portunun yalnız tətbiq qrupuna açılması bazada güclü autentifikasiya və dar rol tələbini aradan qaldırmır. Qrup istinadının hansı resursları əhatə etdiyi dəyişiklik zamanı yoxlanır; sınaq serverini istehsalat qrupuna qoşmaq sərhədi genişləndirə bilər.

0.0.0.0/0 bütün IPv4 mənbələrini, ::/0 bütün IPv6 mənbələrini əhatə edir. Yalnız IPv4 qaydalarını sərtləşdirib IPv6 yolunu açıq saxlamaq səhvdir. İdarəetmə üçün şərti nümunə 192.0.2.40/32-dir; dinamik ünvanı rahatlaşdırmaq üçün bütün İnternetə giriş açılmır.

### Endpoint, WAF və çıxış trafiki

Özəl endpoint xidmətə özəl şəbəkə yolu verir, amma IAM siyasətini əvəz etmir: hücumçu icazəli maşını ələ keçirərsə, həmin yoldan istifadə edə bilər. Endpoint siyasəti, DNS və şəbəkə marşrutu birlikdə yoxlanır. NAT çıxış ünvanını dəyişir, öz-özünə tətbiq səviyyəsində məlumat sızmasını dayandırmır; tətbiqin çıxış trafiki tələb olunan xidmətlərlə məhdudlaşdırılır və müşahidə olunur.

Veb tətbiq firewall-u (Web Application Firewall, WAF) HTTP sorğularında qaydalara uyğun süzgəc aparır. Sürət məhdudiyyəti və provayderin DDoS müdafiəsi giriş qatını qorumağa kömək edir. Bunlar səhv biznes avtorizasiyasını həll etmir: tələbə başqa tələbənin tapşırığını düzgün görünən API sorğusu ilə oxuyursa, obyekt səviyyəli icazə tətbiqdə yoxlanmalıdır.

AWS Direct Connect və Azure ExpressRoute kimi xüsusi bağlantılar rabitə seçimi verir; onların defolt olaraq başdan-başa şifrəli olduğunu düşünmək olmaz. Məxfilik üçün qoruma TLS, IPsec və ya uyğun ayrıca imkanla qurulur.

:::figure
src = "m14-3.png"
alt = "İstifadəçi, CDN və WAF, yük balanslaşdırıcı, özəl alt şəbəkədə LMS tətbiqi və baza; LMS və baza ayrı hesablardakı audit qeydlərinə və dəyişməz ehtiyat nüsxəyə yazır."
caption = "Şəkil 3. LMS-in giriş, tətbiq və baza qatları; audit və ehtiyat nüsxə ayrıca hesablardadır"
wide = true
:::

## Konteyner, serverless və təchizat zəncirinin riskləri

Risk yalnız şəbəkə parametrindən ibarət deyil. Universitetin yazdığı kod, gətirdiyi kitabxana və yerləşdirdiyi obraz xidmətin təhlükəsizlik sərhədinə daxildir. İş yükünün (workload) forması dəyişəndə yamaq, müşahidə və kimlik üzrə məsuliyyət də dəyişir: eyni LMS əlavəsi virtual maşında, konteynerdə və funksiya kimi fərqli istismar qaydası tələb edə bilər.

### Konteynerlər və orkestrasiya

Konteyner tətbiqi asılılıqları ilə paketləyir və adətən hostun nüvəsini paylaşır; virtual maşında isə qonaq əməliyyat sistemi var. İmtiyazlı konteyner, host qovluqlarının yazma hüququ ilə qoşulması və idarəetmə soketinə giriş izolyasiyanı zəiflədə bilər. Tədbirlər: konteynerdə kök istifadəçi ilə işləməmək, lazımsız imkanları azaltmaq, fayl sistemini mümkün olduqda yalnız oxunan etmək.

Kubernetes kimi orkestrasiya sistemində idarəetmə API-si, xidmət hesabları, sirlər və şəbəkə siyasətləri ayrıca qorunur. Ad məkanı (namespace) təkbaşına güclü təhlükəsizlik sərhədi sayılmamalıdır. Şəbəkə siyasətinin təsiri şəbəkə əlavəsinin həmin funksiyanı dəstəkləməsindən asılıdır. İdarə olunan Kubernetes xidmətində provayder idarəetmə qatının müəyyən hissəsini idarə etsə də, işçi düyünlər, obrazlar və konfiqurasiya üzrə bölgü konkret xidmətə görə yoxlanır.

Kitabxananın axtarış xidməti konteynerdə işləyirsə, ona tələbə bazasının sirləri verilməməlidir. Əvvəl təsdiqlənmiş obraz kriptoqrafik heşi (digest) ilə seçilir, zəifliklər skan olunur, yerləşdirmə siyasəti yoxlanır; sonra icra zamanı proses, şəbəkə və fayl davranışı izlənir. Skanın uğurlu olması gələcəkdə zəiflik aşkarlanmayacağına zəmanət deyil. Konteyner təhlükəsizliyi üzrə NIST SP 800-190, virtuallaşdırma üzrə NIST SP 800-125 ayrıca mənbədir.

### Serverless funksiyalar

Serversiz hesablama (serverless computing) serverin yox olması deyil, server istismarının müştəridən gizlədilməsidir. Funksiya xidmət kimi (Function as a Service, FaaS) bunun bir formasıdır: sənəd yüklənəndə fayl yoxlama funksiyası işə düşə bilər. Provayder icra infrastrukturunu idarə edir; universitet kodu, asılılıqları, hadisə mənbəyini, rolunu və məlumat emalını qoruyur.

Təkrar gələn hadisə eyni sənədi iki dəfə emal edə bilər. İdempotentlik (idempotency) eyni əməliyyat təkrar ediləndə əlavə arzuolunmaz nəticənin yaranmamasıdır: məsələn, tapşırığın yoxlama nəticəsi obyekt versiyası ilə əlaqələndirilir ki, təkrar hadisə başqa faylın nəticəsini əvəz etməsin.

Funksiyanın roluna bütün saxlancı oxumaq hüququ vermək bir zəifliyin təsirini artırır. Müvəqqəti diskdə və yaddaşda əvvəlki sorğu məlumatı qala bilər; tələbə məlumatı qlobal dəyişəndə saxlanmır. Gec işə düşmə (cold start), icra limitləri və xidmət asılılıqları imtahan vaxtı cavab müddətinə təsir edə bilər; bu hədlər konkret platformada sınaqla ölçülür.

### Proqram təchizat zənciri

Proqram təchizat zənciri (software supply chain) mənbə kodundan istifadəçiyə çatan artefakta qədər kitabxana, qurma aləti, depo və yerləşdirmə prosesini əhatə edir. Kod düzgün olsa da, zərərli asılılıq və ya ələ keçirilmiş qurma hesabı nəticə artefaktını dəyişə bilər. Davamlı inteqrasiya və çatdırılma (Continuous Integration and Continuous Delivery, CI/CD) prosesinin səlahiyyəti buna görə istehsalat idarəetməsi qədər ciddi qorunur.

| Mərhələ | Risk | Tədbir |
| --- | --- | --- |
| Kod deposu | İcazəsiz dəyişiklik və sirr sızması | Fərdi hesab, dəyişiklik icmalı, sirr skanı |
| Asılılıqlar | Zərərli və ya zəif paket | Sabit versiya, kilid faylı, mənşə və zəiflik yoxlaması |
| Qurma prosesi | Oğurlanmış tokenlə artefaktın dəyişməsi | Təcrid edilmiş qurma, qısaömürlü kimlik |
| Obraz reyestri | Başqa obrazın eyni etiketlə verilməsi | Obrazın heşinə (digest) bağlama, imza və yazma icazəsinin daraldılması |
| Yerləşdirmə | Sınaq kodunun istehsalata nəzarətsiz keçməsi | Ayrı mühit, təsdiq və qəbul siyasəti |

Proqram komponentlərinin siyahısı (Software Bill of Materials, SBOM) hansı asılılığın harada olduğunu tapmağa kömək edir. İmza artefaktın mənşəyini və dəyişmədiyini yoxlamağa imkan verir, amma imzalayanın kodunun təhlükəsizliyini sübut etmir. Universitet imza yoxlamasını zəiflik skanı, icra nəzarəti və yeniləmə prosesi ilə birləşdirir. OWASP Top 10:2025-də A03 Software Supply Chain Failures bu sahəni ayrıca göstərir.

## Audit qeydləri, monitorinq və insidentə cavab

Virtual maşının sistem qeydləri idarəetmə API-sindən edilən dəyişiklikləri tam göstərmir; maşın dayandırılıbsa, içindəki agent də susur. Ona görə idarəetmə auditinin ayrıca mənbəyi var. Universitet hansı hesabın hansı resursu nə vaxt dəyişdirdiyini, hansı faylı oxuduğunu və tətbiqdə nə etdiyini fərqli qeydlərdən birləşdirir.

### Qeyd mənbələrinin fərqi

| Mənbə | Nəyi göstərir | Məhdudiyyəti |
| --- | --- | --- |
| AWS CloudTrail | Dəstəklənən API və hesab fəaliyyətləri | Obyekt səviyyəli data events ayrıca seçilməlidir |
| Azure Activity Log | İdarəetmə müstəvisində abunə fəaliyyətləri | Bütün tətbiq və məlumat oxunuşlarını əhatə etmir |
| Microsoft Entra giriş qeydləri | Kimlik girişləri və autentifikasiya nəticələri | Resursdakı sonrakı əməliyyatları göstərmir |
| Google Cloud Audit Logs | İdarəetmə və seçilən məlumat girişi qeydləri | Data Access sazlanması xidmət üzrə yoxlanır |
| Şəbəkə axın qeydləri | Mənbə, hədəf və trafik metadatası | Adətən paketin tam məzmunu yoxdur |
| LMS tətbiq qeydləri | Kurs, rol və istifadəçi əməliyyatı | Kodda audit yoxdursa, hadisə görünmür |
| Baza və saxlanc qeydləri | Seçilmiş sorğu və obyekt əməliyyatları | Aktivləşdirmə, xərc və saxlama tələbi var |

AWS CloudWatch metrik və log müşahidəsi üçün, AWS Config resurs konfiqurasiyası və uyğunluq qiymətləndirməsi üçün, Amazon Inspector dəstəklənən iş yüklərində zəifliklərin aşkarlanması üçün işlədilir; adları eyni təhlükəsizlik funksiyasını bildirmir. CloudTrail-də saxlanc siyasətinin dəyişməsi görünə bilər, ancaq konkret obyektin oxunuşunu araşdırmaq üçün uyğun məlumat hadisələri əvvəlcədən yazılmalıdır. Sonradan logu açmaq keçmişdə yazılmamış qeydi yaratmır.

### Şərti hadisənin oxunması

Tədris üçün qısaldılmış şərti CloudTrail üslublu qeyd (tarix, hesab, kimlik və saxlanc adı nümunədir):

```json
{ "eventTime": "2026-11-08T10:15:00Z", "eventSource": "s3.amazonaws.com", "eventName": "PutBucketPolicy", "sourceIPAddress": "198.51.100.24", "userIdentity": { "type": "AssumedRole", "accountId": "123456789012", "arn": "arn:aws:sts::123456789012:assumed-role/LmsOps/s1" }, "requestParameters": {"bucketName": "unec-lms-example"} }
```

Qeyd saxlanc siyasəti ilə bağlı API çağırışını göstərir. Təkcə əməliyyat adından saxlancın ictimai açıldığı nəticəsi çıxmır. Tam qeyddə nəticə və xəta sahələri, dəyişən siyasət, əvvəlki vəziyyət və həmin vaxt qüvvədə olan ictimai giriş blokları araşdırılır. Rol sessiyasının arxasındakı insan və ya yerləşdirmə prosesi tapılır, mənbə IP-nin universitetin təsdiqlənmiş çıxışı olub-olmaması yoxlanılır.

Təhlükəsizlik məlumatı və hadisələrinin idarəsi sistemi (Security Information and Event Management, SIEM) bu qeydi kimlik girişi, MFA nəticəsi və sonrakı obyekt əməliyyatları ilə əlaqələndirir. Siyasət dəyişikliyindən sonra geniş ixrac görülürsə, araşdırmanın prioriteti artır; planlı dəyişiklik ilə müqayisə aparılmadan avtomatik insident hökmü verilmir.

### Qeydlərin qorunması və cavab

Audit arxivi ayrıca hesabda və ya layihədə saxlanır; istehsalat administratorunun onu silmək hüququ məhdudlaşdırılır. Dəyişməz saxlama müddəti universitetin tələbinə uyğun qurulur. Başvermə və toplanma vaxtı ayrılır, saatlar sinxronlaşdırılır, toplamanın dayanması xəbərdarlıq yaradır; loglar həssas sahələr daşıya bilər, giriş və saxlama müddəti məhduddur.

İnsidentdə əvvəl yayılma və zərər dayandırılır, eyni vaxtda sübut qorunur. Oğurlanmış açar ləğv edilir, sessiya və etibar əlaqələri araşdırılır, zərərli rol və qaydalar təcrid olunur. Maşını dərhal silmək mümkün sübutu məhv edə bilər; uyğun surət və qeydlər qorunduqdan sonra təmiz mənbədən bərpa aparılır. Şəxsi məlumat təsiri müəyyən ediləndə bildiriş addımları universitetin hüquqi və təşkilati proseduruna görə seçilir. NIST SP 800-61 Rev. 3 (aprel 2025) cavab işini ümumi risk idarəetməsi ilə əlaqələndirir.

## CSPM, CWPP, CASB və CNAPP

Resursların sayı artdıqca əl ilə panel gəzmək kifayət etmir. Məhsul adını almazdan əvvəl universitet hansı resursların əhatə olunacağını, hansı məlumatın oxunacağını və vasitəyə hansı səlahiyyətin veriləcəyini müəyyən edir. Skanerə ehtiyacından artıq idarəetmə hüququ vermək ayrıca riskdir.

| Sinif | Əsas sual | Universitet nümunəsi | Praktik sərhəd |
| --- | --- | --- | --- |
| CSPM | Konfiqurasiya tələbə uyğundurmu? | Açıq baza və söndürülmüş audit aşkarlanır | Tətbiqin biznes məntiqini yoxlamır |
| CWPP | İş yükünün özündə risk varmı? | LMS maşınında zəif paket və şübhəli proses tapılır | Əhatə agent və platformadan asılıdır |
| CASB | Bulud tətbiqindən kim necə istifadə edir? | Şəxsi SaaS hesabına sənəd ötürülməsi görünür | Bütün tətbiq və kanalları eyni dərəcədə görmür |
| CNAPP | Koddan icraya qədər risklər necə əlaqələnir? | Açıq tətbiq, zəif obraz və artıq rol birlikdə qiymətləndirilir | Əhatə və funksiyalar məhsula görə dəyişir |

Bulud təhlükəsizlik vəziyyətinin idarəsi (Cloud Security Posture Management, CSPM) resursları siyahıya alır və qaydalara görə konfiqurasiyanı qiymətləndirir; baza İnternetə açıqdırsa və ya audit dayandırılıbsa, xəbərdarlıq verir (AWS Config, Defender for Cloud). İnfrastruktur kod kimi (Infrastructure as Code, IaC) şablonların yerləşdirmədən əvvəl yoxlanması səhvi erkən tutur; qurulmuş mühitin koddan yayınması (configuration drift) sonradan ayrıca aşkarlanır.

Bulud iş yüklərinin qorunması platforması (Cloud Workload Protection Platform, CWPP) maşın, konteyner və digər iş yüklərinin zəiflik və icra risklərinə baxır. Bulud giriş təhlükəsizliyi vasitəçisi (Cloud Access Security Broker, CASB) SaaS istifadəsini, paylaşmanı və məlumat ötürülməsini ("kölgə İT" daxil) müşahidə edir. API inteqrasiyası və trafik üzərindən nəzarətin görmə sahəsi fərqlidir.

Bulud əsaslı tətbiqlərin qorunması platforması (Cloud-Native Application Protection Platform, CNAPP) bir neçə nəzarəti əlaqələndirən məhsul sinfidir. CSPM, iş yükü qoruması və kimlik riskinin birlikdə təhlili prioritet seçimini yaxşılaşdırır: yalnız zəif paketə baxmaq əvəzinə həmin konteynerin İnternetdən əlçatan və məxfi saxlanca artıq icazəli olması nəzərə alınır.

Avtomatik düzəlişin təsiri qiymətləndirilir: açıq kitabxana kataloqunu yanlışlıqla bağlamaq legitim xidməti dayandıra bilər. Kritik şəxsi sənəd saxlancının anonim açılması isə sürətli müdaxilə tələb edə bilər. Qaydanın uğuru xəbərdarlıq sayı ilə yox, səhvin tapılması, vaxtında düzəlməsi və təkrarlanmaması ilə ölçülür.

## Əlçatanlıq, ehtiyat nüsxə və bərpa

Region coğrafi xidmət sahəsidir; əlçatanlıq zonası (Availability Zone, AZ) region daxilində nasazlıq təsirini ayırmaq üçün yerləşdirmə vahididir. İki virtual maşının olması onların ayrı nasazlıq sərhədlərində olması demək deyil; universitet maşınların, bazanın və faylların hansı zonalarda yerləşdiyini faktiki yoxlayır. Bulud AZ, regionlar, replikasiya və ehtiyat nüsxə verir, amma onları layihələndirmək müştərinin işidir.

### Replikasiya ilə ehtiyat nüsxənin fərqi

Yüksək əlçatanlıq (high availability) komponent sıradan çıxanda xidmətin işləməsini davam etdirməyə yönəlir. Fəlakətdən bərpa (disaster recovery) daha geniş nasazlıqdan sonra xidmətin qaytarılmasıdır. Replikasiya məlumatı başqa nüsxəyə çatdırır, lakin səhv silinməni və zərərli dəyişikliyi də çatdıra bilər. Ehtiyat nüsxə keçmiş sağlam vəziyyətə qayıtmaq üçün saxlanır. Versiyalaşdırmanın silinmə hüquqları da qorunmalıdır.

İmtahan bazasının bir zonada dayanmasına qarşı digər zonada hazır nüsxə seçilə bilər. Regionun itməsi ssenarisi üçün başqa region və ya uyğun bərpa mühiti lazım ola bilər; bu, replikasiya gecikməsi, xərc, məlumat yerləşməsi və operator bacarığı ilə birlikdə planlaşdırılır.

### RPO və RTO

Bərpa nöqtəsi hədəfi (Recovery Point Objective, RPO) itirilməsi qəbul edilən məlumatın zaman pəncərəsidir. Bərpa vaxtı hədəfi (Recovery Time Objective, RTO) xidmətin dayanmasından sonra qəbul edilən bərpa müddətidir. RPO disk həcmi, RTO provayderin dəstəyə cavab müddəti deyil. Hədəfi iş sahibi müəyyən edir, texniki komanda xərci qiymətləndirir. Qısa yaddaş qaydası: RPO nə qədər məlumat itir, RTO nə qədər müddət işləmir.

:::example Şərti hesab
Son istifadə edilə bilən nüsxə saat 09:45-dədir, insident 10:00-da baş verir, LMS 11:30-da bərpa olunur. Məlumat itkisi pəncərəsi 10:00 − 09:45 = 15 dəqiqə, xidmətin dayanması 11:30 − 10:00 = 90 dəqiqədir. Bunlar müşahidə olunan nəticələrdir; RPO və RTO əvvəl qoyulan hədəflərdir. Universitet RPO-nu 5 dəqiqə seçibsə, 15 dəqiqəlik nəticə tələbi ödəmir.
:::

:::figure
src = "m14-4.png"
alt = "Vaxt xətti: 09:45 son nüsxə, 10:00 insident, 11:30 LMS bərpa olunur; 09:45-dən 10:00-a qədər itki 15 dəqiqə, 10:00-dan 11:30-a qədər xidmətin dayanması 90 dəqiqə."
caption = "Şəkil 4. Şərti vaxt xəttində məlumat itkisi pəncərəsi və bərpa müddəti; hədəflər ayrıca müqayisə olunur"
:::

| Xidmət | RPO hədəfi | RTO hədəfi | Seçimə təsir |
| --- | --- | --- | --- |
| İmtahan cavablarının bazası | 5 dəqiqə | 1 saat | Tez-tez qeyd qorunması və hazır bərpa yolu |
| Dərs materiallarının saxlancı | 24 saat | 8 saat | Versiya və dövri ehtiyat nüsxə |
| Kitabxananın açıq kataloqu | 12 saat | 4 saat | Məlumat mənbəyindən yenidən qurma imkanı |
| Kafedranın sınaq mühiti | 48 saat | 24 saat | Koddan təkrar yaratma və məhdud nüsxə |

Bu rəqəmlər universitet üçün normativ deyil; imtahanın növü və məlumatın yenidən yaradılma imkanı hədəfi dəyişir. Gündə bir dəfə nüsxə almaq uğurlu halda belə təxminən bir günlük itki pəncərəsi yarada bilər (məsələn, 24 saatlıq qiymət dəyişiklikləri itə bilər); uğursuz nüsxə bu pəncərəni böyüdər. Cədvəl nüsxənin faktiki uğurunu və bərpa edilə bilməsini əvəz etmir.

### Bərpa sərhədinin qorunması

Ehtiyat nüsxələr ayrıca hesab və ayrıca icazə dəsti ilə qorunur. Saxlama kilidi və dəyişməzlik (immutability) seçiləndə müddət, istisnalar və administratorun onu dəyişmə imkanları yoxlanır. Ehtiyat hesabın etibarı eyni oğurlanmış kimlikdən asılı qalırsa, hesabların adının ayrı olması kifayət deyil. Açarlar, audit və fövqəladə giriş də bərpa planına daxildir.

Bərpa sınağı yalnız bazanın açılmasını yoxlamır: LMS-in fayllarla bazası uyğun olmalı, rol və kurs əlaqələri düzgün qalmalı, DNS və sertifikat işləməli, tələbə tapşırığını görməlidir. KMS açarı və ya kimlik provayderi əlçatmazdırsa, sağlam ehtiyat nüsxə də xidməti qaytarmaya bilər. Universitet bərpanı təcrid olunmuş mühitdə sınayır, ölçülmüş vaxtı və itki pəncərəsini hədəflərlə müqayisə edir.

:::reveal RPO və RTO hədəflərini faktiki bərpa nəticələrindən necə ayırmaq olar?
Hədəflər əvvəl iş sahibi tərəfindən qoyulur; faktiki nəticələr bərpa sınağında və ya insidentdə ölçülür. Nəticə (itki pəncərəsi, dayanma müddəti) hədəflə müqayisə edilir. 15 dəqiqəlik itki 5 dəqiqəlik RPO-nu ödəmir, 90 dəqiqəlik dayanma isə 1 saatlıq RTO-nu aşır.
:::

## Standartlar, məlumatın yerləşməsi və çıxış strategiyası

Təhlükəsizlik standartı nəzarət suallarını sistemləşdirir. Sertifikatın mövcudluğu universitetin konkret saxlanc siyasətinin, rolunun və bərpasının düzgün olduğunu sübut etmir. Universitet sertifikatın əhatə etdiyi hüquqi şəxsi, xidmətləri və mühitləri araşdırır; audit hesabatında təsvir edilən nəzarətin kimə aid olduğu ortaq məsuliyyət cədvəlinə bağlanır. Provayderin sübutu ilə universitetin öz icra sübutu bir-birini tamamlayır.

### Tələbdən nəzarətə və sübuta

CSA Bulud nəzarət matrisi (Cloud Controls Matrix, CCM) v4.1 yanvar 2026 tarixlidir və 17 sahədə 207 nəzarət ehtiva edir. Universitet onu kimlik, məlumat, əməliyyat, təchizatçı və digər sahələr üzrə boşluqları tapmaq üçün işlədir. Hər nəzarətə cavabdeh və yoxlama sübutu bağlanır.

ISO/IEC 27001:2022 informasiya təhlükəsizliyi idarəetmə sisteminin tələblərini, ISO/IEC 27002:2022 nəzarət tədbirlərinə dair tövsiyələri verir. ISO/IEC 27017 bulud xidmətlərində təhlükəsizlik nəzarətlərinə, ISO/IEC 27018 fərdi məlumatları emal edən ictimai bulud xidmətlərində məxfiliyin qorunmasına dair qaydalar verir. Bunlar tətbiqin kod yoxlamasını və müqaviləni əvəz etmir.

| Tələb | Nəzarət nümunəsi | Yoxlama sübutu |
| --- | --- | --- |
| Tələbə məlumatını yalnız səlahiyyətli şəxs görsün | Rol bölgüsü, MFA, obyekt səviyyəli yoxlama | Rol matrisi və rədd edilmiş sınaq sorğusu |
| Kritik dəyişiklik sonradan araşdırılsın | İdarəetmə auditi və qorunan arxiv | Sınaq hadisəsinin SIEM-də tapılması |
| İmtahan məlumatı bərpa olunsun | Ayrı nüsxə, açar və bərpa proseduru | Ölçülmüş bərpa sınağı |
| Məlumat təsdiqlənmiş yerdə qalsın | Region məhdudiyyəti və müqavilə | Resurs reyestri və provayder sənədi |
| Xidmətdən çıxmaq mümkün olsun | İxrac və alternativdə bərpa planı | Yoxlanmış ixrac və sınaq bərpası |

NIST CSF 2.0 (fevral 2024) altı funksiyanı birləşdirir: idarə et (Govern), müəyyən et (Identify), qoru (Protect), aşkar et (Detect), cavab ver (Respond), bərpa et (Recover). Bulud qərarında idarəetmə funksiyası satınalma, risk qəbulu və təchizatçı nəzarətini əhatə edir.

### Məlumatın yerləşməsi

Məlumatın yerləşməsi (data residency) məlumatın hansı coğrafi yerdə saxlandığı və emal edildiyi məsələsidir. Region seçimi yalnız əsas baza ilə məhdudlaşmır: ehtiyat nüsxələr, loglar, analitika, dəstək alətləri və xidmətin başqa emalçıları da məlumat saxlaya bilər. Məlumat suverenliyi (data sovereignty) həmin məlumat üzərində hüquqi yurisdiksiya və nəzarət məsələlərini də əhatə edir; texniki region seçimi bütün hüquqi sualları həll etmir.

Qəbul sənədləri üçün universitet məlumat axını xəritəsi qurur: tələbədən LMS-ə, saxlanca, ehtiyat nüsxəyə və dəstək xidmətinə hansı sahələr gedir? Müqavilədə emal məqsədi, giriş, insident bildirişi, alt emalçılar və xidmət bitəndə məlumatın taleyi araşdırılır. Konkret yerli hüquqi öhdəlik hüquq mütəxəssisi ilə müəyyən edilir.

### Provayderə bağlılıq və çıxış planı

Provayderə bağlılıq (vendor lock-in) məlumat formatı, API, xüsusi xidmət, kimlik inteqrasiyası və əməliyyat bacarığı səbəbindən köçün çətinləşməsidir. İdarə olunan xidmət bu asılılığı artıra, eyni zamanda istismar işini azalda bilər; qərar bu fayda ilə çıxış xərcinin müqayisəsinə əsaslanır.

Çıxış strategiyası (exit strategy) müqavilə bitməmiş hazırlanır. LMS-dən kurslar, qiymətlər, fayllar, istifadəçi əlaqələri və audit hansı formatda çıxarılacaq? İxracı kim təsdiq edəcək, açarlar necə qorunacaq, alternativ mühit nə qədər vaxta hazır olacaq? Universitet faylların sayını, bütövlüyünü və bazadakı əlaqələri yoxlayır; ixracın endirilməsi onun başqa tətbiqdə işləməsi demək deyil.

Çıxış sınağında şərti bir kurs alternativ mühitə bərpa edilir; keçidlər, qiymət əlaqələri və giriş hüquqları yoxlanır. Sonra köhnə xidmətin sessiya və inteqrasiya açarları ləğv olunur, məlumat silinməsi və ehtiyat nüsxələrdə saxlanma müddəti barədə sübut alınır.

## İki insidentdən texniki dərslər

### Capital One, 2019

Capital One-un 2019-cu ildə açıqladığı insident bulud resursuna tətbiq yolundan çıxışın təhlükəsini göstərir. Açıq texniki təsvirlər server tərəfli sorğu saxtalaşdırmasını (Server-Side Request Forgery, SSRF), müvəqqəti rol kimlik məlumatlarına çıxışı və həmin səlahiyyətlərlə saxlanc məlumatlarının götürülməsini əlaqələndirir. Hadisəni sadəcə bütün saxlancın anonim açılması kimi təsvir etmək dəqiq deyil: hücum zəncirində tətbiq və konfiqurasiya ilə rol səlahiyyəti birlikdə nəzərdən keçirilir.

SSRF zamanı hücumçu serverə nəzərdə tutulmayan hədəfə sorğu göndərdirir. LMS-də xarici URL-dən şəkil gətirmə funksiyası varsa, tətbiqin daxili xidmətlərə sorğu göndərməsinin qarşısı alınmalıdır: URL-in yoxlanması, yönləndirmələr, DNS həlli və çıxış şəbəkəsi nəzərə alınır. Bulud metadata xidmətinə çıxış ayrıca qorunur; AWS mühitində IMDSv2 kimi mexanizmlər kömək edə bilər, lakin bu, bütün SSRF növlərinin universal həlli deyil.

Universitet üçün dərs: tətbiqin sorğu imkanını daraltmaq, iş yükünün rolunu yalnız lazım olan obyektlərlə məhdudlaşdırmaq, rolun qeyri-adi istifadəsini izləmək. Tətbiq zəifliyi baş versə belə, onun bütün arxivi oxumağa çevrilməməsi hədəflənir; bir nəzarətin çatışmazlığını digər qatlar azaldır.

### Snowflake müştəri hesabları, 2024

Mandiant-ın 2024-cü ildə dərc etdiyi UNC5537 araşdırması Snowflake müştəri instansiyalarından məlumat oğurluğu və şantaj kampaniyasını təsvir edir. Araşdırmada əvvəldən oğurlanmış kimlik məlumatlarının istifadəsi və MFA ilə qorunmayan hesablar göstərilir. Bunu Snowflake platformasının özünün sındırıldığına dair ümumi hökmə çevirmək olmaz: hadisələr müştəri hesablarının qorunması və həmin hesabların daxil olduqdan sonrakı imkanları ilə əlaqələndirilir.

Universitetin analitika platformasında köhnə parolun dəyişməməsi, hesabın daraldılmaması və MFA çatışmazlığı oxşar risk yaradar. Məlumatı yalnız saxlanarkən şifrələmək etibarlı hesabla aparılan ixracı dayandırmaya bilər. İnsan girişində güclü MFA, xidmətlərdə iş yükü kimliyi, köhnə kimlik məlumatlarının ləğvi və qeyri-adi ixracın aşkarlanması birlikdə seçilir. Dəstək podratçısının cihazında saxlanan kimlik məlumatı da universitetin təhdid modelinə daxil edilir.

## Universitet LMS-inin buluda köçürülməsi

### İlkin vəziyyət və qərar

Bütün təşkilati adlar, həcmlər və hədəflər şərtidir. Universitetin lms.unec.example sistemi yerli virtual maşında, tələbə reyestri özəl buludda işləyir. İmtahan dövründə yük artır, texniki komanda isə baza əməliyyat sistemlərinin istismarını azaltmaq istəyir. İctimai buludda idarə olunan tətbiq platforması, idarə olunan PostgreSQL və özəl obyekt saxlancı seçilir; hər xidmətin məsuliyyəti ayrıca qiymətləndirilir.

Köçürmədən əvvəl asılılıqlar siyahıya alınır: kimlik provayderi, kurs əlavələri, planlı tapşırıqlar, poçt, fayl yolları və tələbə reyestri ilə sinxronlaşma. Lokal diskdə saxlanan sessiya və fayllar nüsxələrin çoxalmasına mane ola bilər.

Məlumat sahibi qiymətlər, tapşırıqlar və imtahan sualları üçün giriş və bərpa tələblərini təsdiqləyir. Şərti layihədə imtahan bazası üçün RPO 5 dəqiqə, RTO 1 saatdır. Region, audit, ixrac və açar imkanları satınalma meyarlarına daxil edilir; universitet əvvəlcə məhdud kursla sınaq aparır.

### Hədəf quruluş və məsuliyyət matrisi

İstehsalat, sınaq, audit və bərpa mühitləri ayrı idarəetmə sərhədlərində qurulur. Tələbələr giriş balanslaşdırıcısından tətbiqə çatır; baza və saxlanc özəl yollarla işləyir, tətbiq saxlanca ayrıca rol ilə müraciət edir. Tələbə reyestrinə yalnız tələb olunan inteqrasiya axını açılır. Sınaqda istehsalat sirləri və şəxsiyyəti müəyyən edən real məlumat işlədilmir. Matrisdə icraçı işi görür, qərar sahibi universitet daxilində tələbin və nəticənin qəbuluna cavabdehdir; provayderin iştirak etdiyi işlərdə də universitet nəticənin öz xidmətinə uyğunluğunu yoxlayır.

| İş | Universitetdə icraçı | Universitetdə qərar sahibi | Provayderin işi |
| --- | --- | --- | --- |
| Məlumatın təsnifatı və region seçimi | Məlumat sahibi, təhlükəsizlik qrupu | Tədris üzrə səlahiyyətli rəhbər | Region və emal imkanlarını açıqlamaq |
| Fiziki infrastruktur və platforma yamaqları | Xidmət meneceri nəticəni izləyir | İT rəhbəri | Seçilən idarə olunan qatları qorumaq |
| LMS kodu və əlavələrin yoxlanması | Tətbiq komandası | LMS xidmət sahibi | Platformanın dəstəklədiyi interfeysləri vermək |
| İstifadəçi rolları və MFA | Kimlik və LMS administratorları | Məlumat sahibi və təhlükəsizlik rəhbəri | Kimlik və audit mexanizmlərini işlətmək |
| Şəbəkə və özəl endpoint-lər | Bulud şəbəkə administratoru | İT təhlükəsizlik rəhbəri | Şəbəkə xidmətinin baza işini saxlamaq |
| KMS və sirlərin sazlanması | Açar və xidmət administratorları | İT təhlükəsizlik rəhbəri | Açar xidmətinin müqavilə funksiyaları |
| Auditin SIEM-ə ötürülməsi | SOC və bulud administratoru | SOC rəhbəri | Seçilmiş audit mənbələrini təqdim etmək |
| Nüsxə siyasəti və bərpa sınağı | Baza və bərpa komandası | LMS xidmət sahibi | Seçilmiş nüsxə və bərpa imkanları |
| İnsidentin idarəsi | SOC, tətbiq və hüquq qrupu | Təyin edilmiş insident rəhbəri | Öz qatında araşdırma və razılaşdırılmış dəstək |
| İxrac və xidmətdən çıxış | Tətbiq və məlumat komandası | Məlumat sahibi | Razılaşdırılmış ixrac və silmə imkanları |

Sərhədlər müqavilə və seçilən xidmət sənədləri ilə təsdiqlənir. SOC (Security Operations Center) burada auditin SIEM-ə ötürülməsi və insident işində icraçıdır.

### Köçürmənin ardıcıllığı və yoxlama

:::steps Köçürmənin dörd mərhələsi
[[step]]
title = "Təhlükəsiz baza mühiti"
body = "Hesablar, federasiya, audit arxivi, şəbəkə və xərc nəzarəti qurulur. Resurslar nəzərdən keçirilən IaC şablonlarından yaradılır ki, bərpa və sınaqda quruluşun təkrarı mümkün olsun. Paneldən edilən fövqəladə dəyişiklik sonradan kodla uyğunlaşdırılır, əks halda növbəti yerləşdirmə işlək düzəlişi geri çevirə bilər."

[[step]]
title = "Sınaq"
body = "Şəxsiyyətsizləşdirilmiş məlumatla funksional və yük sınağı aparılır. Şərti olaraq 2 000 paralel sessiya real tələbənin davranışını təqlid edən sorğu qarışığı ilə əsaslandırılır; təkcə giriş səhifəsi yox, tapşırıq yükləmə, qiymət yazma və baza əlaqələri də yoxlanır. Mənfi təhlükəsizlik sınağında tələbənin başqa kurs sənədini oxuya bilməməsi, sınaq rolunun istehsalat saxlancına buraxılmaması və audit hadisəsinin görünməsi tələb olunur."

[[step]]
title = "Məlumatın sinxronlaşması və keçid"
body = "Yazıların hansı anda dayandırılacağı, son fərqin necə köçürüləcəyi və fayllarla bazanın uyğunluğu müəyyən edilir. İki mühitdə nəzarətsiz paralel yazı ziddiyyət yarada bilər. Geri dönüş şərti əvvəlcədən yazılır (məsələn, kritik kurs əməliyyatı uğursuzdursa, xidmət açılmır). DNS dəyişməsi təkbaşına məlumatın geri sinxronlaşdırılması problemini həll etmir."

[[step]]
title = "Açılış və gücləndirilmiş müşahidə"
body = "Səhv sayı, gecikmə, baza bağlantısı, rol dəyişiklikləri və xərc izlənir. Tədris bölməsi nümunə kurs əməliyyatını qəbul edir, təhlükəsizlik komandası qorunan arxivdə sınaq hadisəsini tapır, bərpa komandası şərti kursu ayrıca mühitə qaytarıb hədəflə müqayisə edir. Köhnə mühit yalnız qəbul və geri dönüş müddəti bitəndən sonra təsdiqlənmiş silmə qaydasına uyğun çıxarılır."
:::

### Layihənin qəbul meyarları

| Meyar | Gözlənilən sübut | Qəbul edən |
| --- | --- | --- |
| İcazə sərhədləri işləyir | İcazəli və rədd olunan kurs əməliyyatları | LMS xidmət sahibi |
| Şəxsi saxlanc anonim açılmır | Siyasət yoxlaması və anonim sorğunun rəddi | Təhlükəsizlik qrupu |
| Admin girişi qorunur | MFA və müvəqqəti rol sınağı | Kimlik üzrə məsul şəxs |
| Dəyişiklik araşdırılır | Tam rol sessiyası ilə audit qeydi | SOC |
| Bərpa hədəfə uyğundur | Ölçülmüş vaxt və itki pəncərəsi | Məlumat sahibi |
| Çıxış mümkündür | Kursun ixracı və alternativdə bərpası | Tətbiq komandası və məlumat sahibi |

Bu meyarlar istismar işinin başlanğıcıdır: hesablar və əlavələr dəyişdikcə sərhədlər yenidən yoxlanır. Universitet istisnaların bitmə tarixini, istifadə olunmayan açarları, bərpa nəticələrini və müqavilə dəyişikliklərini xidmət icmalına daxil edir. Qəbul edilmiş riskin sahibi və əsaslandırması saxlanır.

## Konspektdən əlavə: Code Spaces

Konspekt ssenarisi: admin hesabı fişinqlə ələ keçirilir (MFA yox), istehsalat serverləri və eyni hesabdakı bütün ehtiyat nüsxələr silinir. Çatışmayan tədbirlər: fişinqə davamlı MFA (FIDO2), PAM və just-in-time ilə müvəqqəti admin hüququ, ayrı hesabda immutable nüsxələr, ayrı yerə göndərilən audit logları, sınanan bərpa planı (RTO/RPO). 2014-cü ildə Code Spaces şirkəti oxşar hücumdan sonra bağlanıb.
