+++
title = "Seqmentasiya, şəbəkələrarası ekranlar və IDS/IPS"
unit = "uzun"
order = 6
summary = "Mühazirə tam həcmdə: seqmentasiya, VLAN və alt şəbəkə, DMZ, mikroseqmentasiya və Zero Trust, firewall növləri və qayda dəsti, NAT, IPv6 və VPN, IDS/IPS, Suricata qaydası, yanlış nəticələrin hesabı, jurnal təhlili və insident cavabı."
updated = 2026-11-09

[[source]]
title = "Mühazirə 6: Seqmentasiya, şəbəkələrarası ekranlar və IDS/IPS"
note = "Elmar Cabbarov, 2026–2027"
+++

Üç vasitə üç suala cavab verir. **Seqmentasiya:** şəbəkəni hansı hissələrə bölək? **Firewall:** hissələr arasında hansı trafik keçə bilər? **IDS/IPS:** keçən trafikin içində hücum varmı? Mühazirə üçünü universitet şəbəkəsi üzərində ardıcıl qurur: zonalar, ünvan planı, icazə matrisi, firewall qaydaları, sensorlar, sübut jurnalı.

:::note Şərti tədris nümunəsi
Universitet topologiyası, cihaz adları, ünvan bölgüsü, VLAN nömrələri, hadisə vaxtları, saylar və tutum hesabları **şərti tədris nümunəsidir**. Protokol portları və standart identifikatorları texniki mənaları ilə verilir. `.example` domenləri və sənədləşdirmə ünvanları real xidmətə müraciət üçün deyil.
:::

## Müdafiə arxitekturası və qorunan xidmətlər

Dərs platforması (LMS), tələbə bazası, maliyyə sistemi və yataqxana Wi-Fi şəbəkəsi eyni infrastrukturdan istifadə edə bilər, amma istifadəçiləri və riskləri fərqlidir: tələbənin şəxsi noutbukunda administrator nəzarəti zəif ola bilər, tələbə bazasında isə qiymətlər və fərdi məlumatlar saxlanılır. Müdafiə arxitekturası hansı resursun kimdən və hansı yolla qorunacağını əvvəlcədən müəyyənləşdirir.

Məxfilik məlumatın icazəsiz oxunmamasıdır, bütövlük məlumatın və sistem vəziyyətinin icazəsiz dəyişməməsi, əlçatanlıq qanuni istifadəçinin lazım olan vaxt xidmətdən istifadə edə bilməsi. Kataloqda axtarış nəticələrinin açıqlığı normaldır; oxucunun götürdüyü kitabların tarixçəsi isə məhdud giriş tələb edir. Eyni tətbiqin ayrı məlumatlarına fərqli siyasət lazım ola bilər; şəbəkə sərhədi bunu tam həll etmir, tətbiqin avtorizasiyası da işləməlidir.

### Təhdid modeli və hücum növləri

**Təhdid modeli** mümkün hücumçunu, onun başlanğıc imkanını, hədəfini və keçə biləcəyi yolları təsvir edir. Başlanğıc nöqtə yoluxmuş laboratoriya kompüteri, oğurlanmış əməkdaş hesabı və ya İnternetə açıq LMS ola bilər; hədəf qiymətləri dəyişmək, tələbə siyahısını çıxarmaq və ya imtahanı dayandırmaq. Bu məqsədlər üçün eyni nəzarət kifayət etmir: oxunmaya məhdudiyyətlə həddindən artıq yükə qarşı tədbir fərqlidir.

Kiberhücum icazəsiz giriş, məlumatın ələ keçirilməsi, dəyişdirilməsi və ya xidmətin pozulması məqsədli fəaliyyətdir.

| Hücum | Mahiyyət |
| --- | --- |
| Fişinq | İstifadəçini aldadaraq hesab və ya ilkin giriş verir |
| Zərərli proqram, o cümlədən fidyə proqramı | Cihazdakı faylları və əlçatan şəbəkə resurslarını zədələyir |
| Ortadakı tərəf hücumu (man-in-the-middle) | Ötürülən əlaqəyə müdaxilə |
| SQL inyeksiyası | Tətbiqin sorğu qurmasındakı qüsurdan istifadə |
| Yanlış paylaşım | Əməkdaşın səhvən paylaşım açması qəsd olmadan da sızma yaradır |

### Çoxqatlı müdafiə

Çoxqatlı müdafiədə (defense in depth) ayrı tədbirlər müxtəlif səhvləri məhdudlaşdırır. Seqmentasiya resursları və əlaqə sərhədlərini ayırır, firewall sərhəddə trafikə qərar verir. Müdaxiləni aşkarlama sistemi (Intrusion Detection System, IDS) şübhəli əlamət axtarır; müdaxilənin qarşısını alma sistemi (Intrusion Prevention System, IPS) uyğun yerləşdirildikdə trafiki dayandıra bilir. Serverdə yeniləmə, autentifikasiya və tətbiq nəzarəti ayrıca hissələrdir.

| Tədbir | Universitetdə vəzifə | Özbaşına həll etmir |
| --- | --- | --- |
| Seqmentasiya | Laboratoriyadan maliyyə zonasına yolları azaltmaq | İcazəli tətbiqdə oğurlanmış hesabı |
| Firewall | Tələbə bazasına yalnız tətbiqdən bağlantı buraxmaq | Qanuni sessiyadakı zərərli sorğunu |
| IDS | Laboratoriya cihazının daxili skanını bildirmək | Trafiki avtomatik saxlamağı |
| IPS | Tanınmış zərərli sorğunu yol üzərində kəsmək | Görmədiyi və tanımadığı hücumu |
| Host və tətbiq nəzarəti | Proses, fayl və istifadəçi hüquqlarını yoxlamaq | İnternet xəttinin həcmli hücumla dolmasını |

Şimal–cənub trafiki (north–south) universitetlə xarici şəbəkə arasındadır, şərq–qərb trafiki (east–west) daxili sistemlər arasında. Tətbiq serverinin bazaya sorğusu ikincidir və İnternet firewall-ından keçməyə bilər. Klassik perimetr firewall-u yalnız birincini görür; hücumların çoxu içəri girdikdən sonra şərq–qərb istiqamətində yayılır, ona görə daxili seqmentasiya və mikroseqmentasiya lazımdır. Hücumçunun bir cihazdan başqa sistemə keçməsi **yanal hərəkətdir (lateral movement)**.

:::warning Paket yolunu çək
Paket yolunu çəkmədən nəzarət seçmək təhlükəlidir: qayda düzgün olsa da, paket həmin qurğudan keçməyə bilər.
:::

## Seqmentasiya, VLAN, alt şəbəkə və ACL

### Seqmentasiyanın sərhədi

Şəbəkə seqmentasiyası (network segmentation) şəbəkəni hissələrə bölüb aralarındakı əlaqələri siyasətlə məhdudlaşdırmaqdır. Seqmentasiyasız şəbəkə **yastı şəbəkədir (flat network)**: yoluxmuş tələbə noutbuku maliyyə serverinin xidmətlərini birbaşa yoxlaya bilər. Seqmentasiya bu imkanları azaldır, lakin yayılmayacağına zəmanət vermir: icazəli bağlantı, yanlış qayda və ya ələ keçirilmiş idarəetmə hesabı sərhədi aşa bilər.

:::note Sadə dillə
Gəmidəki su keçirməyən bölmələri xatırla: gövdə bir yerdən deşilsə, su yalnız həmin bölməni doldurur, gəmi batmır. Seqmentasiya da bir kompüterin «deşilməsini» bütün şəbəkənin batmasına çevirmir.
:::

Təsnifat meyarları qarışdırılmamalıdır. Fiziki və məntiqi bölgü sərhədin **necə qurulduğunu**, makro və mikroseqmentasiya nəzarətin **miqyasını**, funksiya, risk və identiklik siyasətin **əsasını** göstərir. Maliyyə şöbəsi ayrıca avadanlıqda, ayrıca VLAN-da və serverlər üzrə incə qaydalarla ola bilər; bunlar bir-birini istisna etmir.

| Yanaşma | Mexanizm | Universitet nümunəsi | Məhdudiyyət |
| --- | --- | --- | --- |
| Fiziki | Ayrı kabel və kommutator | Təcrid olunmuş imtahan laboratoriyası | Xərc, daşıyıcı və insan vasitəsilə keçid |
| Məntiqi | VLAN, VRF, virtual firewall | Eyni kampusda şöbə şəbəkələri | Ortaq infrastrukturda sazlama səhvi |
| Makroseqmentasiya | Böyük təhlükəsizlik zonaları | Tələbələr, serverlər, qonaqlar | Zona daxilində geniş əlaqələr qala bilər |
| Mikroseqmentasiya | İş yükünə görə qayda | LMS tətbiqindən yalnız öz bazasına | Etiket və qayda idarəsinin yükü |
| Risk üzrə bölgü | Həssaslıq və kritikliyə görə qruplaşdırma | Qiymət bazasının ayrıca qorunması | Aktiv inventarı düzgün olmalıdır |

Tam fiziki ayrılmış şəbəkə (air gap) normal şəbəkə bağlantısını aradan qaldırır, amma USB daşıyıcısı və texniki xidmət noutbuku məlumat daşıya bilər (konspektdə nümunə: Stuxnet). Universitetin bütün xidmətlərini ayırmaq mümkün deyil. **Karantin zonası** kompromitasiya şübhəsi olan cihazı məhdudlaşdırır, yalnız bərpa xidmətlərini açıq saxlayır.

:::exam VLAN təkbaşına sərhəd deyil
L3 kommutator VLAN-lar arasında hər şeyi marşrutlaşdırırsa və ACL yoxdursa, tələbə VLAN-ı ilə maliyyə VLAN-ı bir-birini görür. Seqmentasiya yalnız zonalar arasında qayda tətbiq edən nöqtə (firewall, ACL) olanda işləyir.
:::

### İkinci və üçüncü səviyyənin fərqi

Virtual lokal şəbəkə (Virtual Local Area Network, VLAN) ikinci səviyyədə ayrıca yayım domenidir; kommutator normal halda bir VLAN-dakı yayım kadrını başqa VLAN-a ötürmür. IP alt şəbəkəsi isə üçüncü səviyyədə ünvan və marşrutlaşdırma sərhədidir. Bir VLAN-a bir IPv4 alt şəbəkəsi vermək rahatdır, lakin anlayışlar eyni deyil: eyni yayım domenində iki IP prefiksi saxlamaq avtomatik L2 izolyasiyası yaratmır.

| Meyar | VLAN | IP alt şəbəkəsi |
| --- | --- | --- |
| Səviyyə | Kanal, L2 | Şəbəkə, L3 |
| Ayırdığı sahə | Kommutasiya və yayım domeni | Ünvan prefiksi və marşrut |
| Başqa hissəyə keçid | Marşrutlaşdırma tələb edir | Marşrut və uyğun növbəti qovşaq tələb edir |
| Təkbaşına müdafiə | L2 domenlərini ayırır | Girişi avtomatik qadağan etmir |
| Nümunə | VLAN 30 maliyyə portları | 10.10.30.0/24 maliyyə ünvanları |

:::warning Yayım domenini kim bölür?
Alt şəbəkənin sərhədini dəyişmək yayım domenini özü kiçiltmir; onu VLAN və ya marşrutlaşdırılan interfeys bölür.
:::

**Access, trunk və native VLAN.** Access port son cihazı adətən bir VLAN-a bağlayır. Trunk bir neçə VLAN daşıyır; IEEE 802.1Q işarəsi (teqi) kadrın mənsubiyyətini göstərir. İşarəsiz kadrın düşdüyü native VLAN iki tərəfdə uyğun qurulmalıdır. Kafedra otağındakı adi portda ehtiyacsız trunk açılması istifadəçinin nəzərdə tutulmayan VLAN-a çatmasına imkan verə bilər; portun təyinatı sənəddə və real kommutatorda eyni olmalıdır.

**Sərtləşdirmə.** İstifadə olunmayan port bağlanır, son cihaz portunda trunk razılaşdırılması söndürülür, trunk üzərində yalnız lazımi VLAN-lar daşınır, idarəetmə VLAN-ı istifadəçi portlarına verilmir. VLAN nömrəsi parol deyil: gizlədilməsi autentifikasiyanı əvəz etmir. Yataqxana Wi-Fi-da ayrıca SSID açmaq da yetərli deyil: SSID-nin hansı VLAN-a və firewall siyasətinə bağlandığı yoxlanır.

**Ünvan hesabı.** 10.10.30.0/24-də şəbəkə hissəsi 24 bitdir; IPv4 32 bit olduğundan host hissəsinə 8 bit qalır: 2 üstü 8 = 256 ünvan. Adi /24-də .0 şəbəkə, .255 yayım ünvanıdır, 254 host ünvanı qalır; şlüz .1-i tutduqda 253. Yataqxananın cihaz sayı bu həddi aşarsa, /24-ü böyütmək əvəzinə bina və mərtəbələr üzrə əlavə VLAN-lar planlaşdırmaq mümkündür.

### ACL və faktiki paket yolu

Girişə nəzarət siyahısı (Access Control List, ACL) paket başlığındakı meyarlara görə icazə və ya qadağa verir. Klassik marşrutlaşdırıcı ACL-i mənbə, təyinat, protokol və portlara baxır, adətən tam sessiya cədvəli saxlamır. TCP portu nəqliyyat səviyyəsinin sahəsidir, ona görə IP və port yoxlayan süzgəci yalnız L3 vasitəsi adlandırmaq dəqiq deyil. Stateful firewall sessiyanın vəziyyətini də nəzərə alır.

Tələbə cihazı 10.10.10.25 maliyyə serveri 10.10.30.15 ilə danışarkən paket şlüzə gedir. Şlüz L3 kommutatordadırsa, qərar orada verilə bilər; İnternet sərhədindəki firewall bu əlaqəni süzmür. ACL-in istiqaməti konkret interfeysə nəzərən yazılır: tələbə VLAN-ından kommutatora daxil olan paket üçün giriş ACL-i işləyir, yanlış istiqamətə bağlanan qayda gözlənilən qadağanı yaratmır.

Eyni VLAN-dakı iki tələbə kompüteri MAC ünvanları ilə birbaşa kommutator vasitəsilə əlaqə qura bilər; trafik şlüzə getmədiyindən şlüz firewall-ı onu görməz. Bu sahə üçün host firewall, port izolyasiyası, private VLAN və simsiz müştəri izolyasiyası seçilir. Müştəri izolyasiyasının yalnız eyni giriş nöqtəsində, yoxsa bütün simsiz mühitdə işləməsi ayrıca yoxlanır: iki fərqli giriş nöqtəsindəki yataqxana cihazları ilə sınaq bunu göstərir.

## Universitetin ünvan planı və DMZ

### Aktivlərdən ünvan planına

Ünvan planından əvvəl aktiv inventarı hazırlanır: sahib, xidmət, məlumat həssaslığı, ünvan, autentifikasiya asılılığı, dayanma təsiri. Dinamik cihaz ünvanları DHCP qeydləri ilə, server ünvanları idarə olunan inventarla əlaqələndirilir; IP ünvanının dünən hansı tələbəyə aid olması bugünkü DHCP icarəsindən çıxarıla bilməz.

Marşrutlaşdırılan VLAN-larda .1 məntiqi şlüzdür (zonalararası şlüzlər daxili firewall-da və ya ona məcburi yönəldilən nəzarətli qatdadır); server və şəbəkə avadanlığı üçün ünvanlar rezerv edilir. İstifadəçi zonalarında .100–.230 DHCP diapazonu ayrılır, qalanı planlı ehtiyatdır. VPN hovuzu Ethernet VLAN-ı deyil, DHCP diapazonu qaydası ona tətbiq olunmur.

| Zona | VLAN | IPv4 prefiksi | Təyinat |
| --- | --- | --- | --- |
| Tələbə laboratoriyası | 10 | 10.10.10.0/24 | İdarə olunan dərs kompüterləri |
| Kafedra iş yerləri | 20 | 10.10.20.0/24 | Əməkdaş və müəllim cihazları |
| Maliyyə | 30 | 10.10.30.0/24 | Maliyyə iş yerləri |
| Tətbiqlər | 40 | 10.10.40.0/24 | LMS və maliyyə tətbiqləri |
| Qonaq Wi-Fi | 50 | 10.10.50.0/24 | Daxili resurslara çıxışı yoxdur |
| İdarəetmə | 60 | 10.10.60.0/24 | Nəzarətli administrator yolu |
| DMZ | 70 | 10.10.70.0/24 | Açıq xidmət girişləri |
| Məlumat bazaları | 80 | 10.10.80.0/24 | LMS və maliyyə bazaları |
| İnfrastruktur | 90 | 10.10.90.0/24 | DNS, vaxt, jurnal, yeniləmə |
| Yataqxana | 100 | 10.10.100.0/24 | Şəxsi tələbə cihazları |
| Kitabxana | 110 | 10.10.110.0/24 | Kataloq və oxu zalı cihazları |
| Karantin | 120 | 10.10.120.0/24 | Məhdud bərpa çıxışları |
| Uzaq giriş hovuzu | yoxdur | 10.10.130.0/24 | Rol üzrə təyin olunan tunel ünvanları (şlüz: VPN sonluğu) |

Siyasətdə istifadə olunan sabit ünvanlar:

| Obyekt | Şərti ünvan | Funksiya |
| --- | --- | --- |
| İctimai LMS ünvanı | 203.0.113.10 | lms.uni.example, DMZ-yə DNAT |
| DMZ giriş serveri | 10.10.70.10 | HTTPS qəbul edən tərs proksi (reverse proxy) və WAF |
| LMS tətbiqi | 10.10.40.10 | Dərs məzmunu və qiymətləndirmə |
| Maliyyə tətbiqi | 10.10.40.20 | Maliyyə iş yerlərinin xidməti |
| LMS bazası | 10.10.80.10 | PostgreSQL, TCP 5432 |
| Maliyyə bazası | 10.10.80.20 | Ayrı tətbiq hesabı ilə PostgreSQL |
| Keçid hostu | 10.10.60.10 | Jump host, administrator sessiyaları |
| DNS və vaxt | 10.10.90.53; 10.10.90.123 | Daxili resolver; NTP serveri |
| Jurnal qəbuledicisi | 10.10.90.20 | Mərkəzi təhlükəsizlik qeydləri |
| Yeniləmə serveri | 10.10.90.30 | Təsdiqlənmiş paket və yeniləmələr |
| Kitabxana kataloqu | 10.10.110.10 | Daxili HTTPS xidməti |

Kataloq ilə oxu zalı cihazlarının eyni VLAN-da olması bu planda host firewall tələb edir; daha sərt tələbdə kataloq ayrıca server seqmentinə keçirilə bilər. Cədvəldə ayrı zona adı yazmaq hər cihazın ayrıca qorunduğu demək deyil. Maliyyə və LMS bazaları eyni /24-dədir, lakin bir-birinə çıxışı mikroseqmentasiya ilə bağlanır.

### DMZ və üçpilləli xidmət

Demilitarizasiya zonası (demilitarized zone, DMZ) xaricdən əlçatan xidmətlər (veb, poçt, DNS) üçün ayrılmış bufer zonadır. İnternet istifadəçisi DMZ-dəki giriş serverinə TCP 443 ilə bağlanır; giriş serveri LMS tətbiqinə ayrıca HTTPS bağlantısı açır; LMS tətbiqi öz bazasına TCP 5432 ilə sorğu göndərir. Hər üç bağlantının ayrıca mənbəsi, təyinatı və icazəsi var; DMZ giriş serverinin bazaya birbaşa yolu açılmır.

:::figure
src = "m06-1.png"
alt = "Sxem: İnternet xarici firewall-dan keçərək DMZ-dəki tərs proksiyə TCP 443 ilə gəlir; tərs proksi daxili firewall vasitəsilə tətbiq və baza zonalarına yol açır; bütün zonalar arasında default deny."
caption = "Şəkil 1. Xarici sərhəd, DMZ və daxili zonalar. Oxlar seçilmiş icazəli yolları göstərir."
wide = true
:::

DMZ bir neçə interfeysli tək firewall ilə və ya xarici və daxili olmaqla iki firewall ilə qurula bilər. Tək qurğu sadə idarə olunur, lakin ümumi nasazlıq nöqtəsi yarada bilər. İki qurğu sərhədləri ayırır, amma eyni geniş icazə hər ikisindədirsə, sayın artması qorumanı düzəltmir. Ehtiyat cütlük, sessiya sinxronluğu və idarəetmə ayrılığı ayrıca qərardır. İki firewall-lu dizaynda xarici firewall İnternetdən DMZ-yə, daxili firewall DMZ-dən daxiliyə keçidi süzür.

DMZ serveri ələ keçiriləndə hücumçu onun icazəli tətbiq bağlantısından sui-istifadə edə bilər; buna görə DMZ-dən daxilə açılan TCP 443 də risksiz deyil: tətbiq autentifikasiyası, sorğu məhdudiyyəti, yeniləmə və jurnal təhlili qalır. Sındırılmış DMZ serveri hücumçuya daxili şəbəkəyə birbaşa yol verməməlidir. Tərs proksinin iki bağlantı qurması NAT deyil. Proksi və tələ sistemləri 7-ci mövzudadır.

**İdarəetmə yolu.** İnternetdən serverlərin SSH portunu açmaq əvəzinə uzaq girişdən idarəetmə zonasına nəzarətli yol verilir: administrator güclü autentifikasiya ilə keçid hostuna (jump host) daxil olur, oradan yalnız təyin olunmuş serverə keçir. Keçid hostu yüksək riskli aktivdir: sessiyalar yazılır, yenilənir, adi veb baxışı üçün işlədilmir. Kompromitasiyası geniş idarəetmə hüququ verdiyindən «daxildədir» arqumenti ilə istisna edilməməlidir.

## Mikroseqmentasiya, Zero Trust və virtual mühit

### İş yükü səviyyəsində qərar

Mikroseqmentasiya (microsegmentation) qaydanı ayrıca iş yükünə (fiziki server, virtual maşın, konteyner, xidmət) qədər endirir. Məqsəd hər qovşağı əlaqəsiz qoymaq deyil: LMS tətbiqinin bazaya ehtiyacı var, maliyyə bazasına yoxdur. «Serverlər bir-birinə çıxa bilər» qaydası bu fərqi itirir.

Nəzarət hipervizorun virtual kommutatorunda, paylanmış firewall-da və ya host agentində tətbiq oluna bilər. İki virtual maşın eyni fiziki serverdədirsə, trafik fiziki sensora çıxmadan ötürülə bilər; host əsaslı qayda əlaqəni yerində dayandırır. Agentin dayanması, siyasət serverindən ayrılması və köhnə qaydanın qalması üçün davranış müəyyən edilir; «agent quraşdırılıb» ilə «siyasət indi tətbiq olunur» ayrı yoxlamalardır.

| Mənbə rolu | Təyinat rolu | İcazə | Qalan əlaqə |
| --- | --- | --- | --- |
| DMZ giriş serveri | LMS tətbiqi | TCP 443 | Maliyyə tətbiqi və bazalara qadağa |
| LMS tətbiqi | LMS bazası | TCP 5432 | Maliyyə bazasına qadağa |
| Maliyyə tətbiqi | Maliyyə bazası | TCP 5432 | LMS bazasına qadağa |
| Keçid hostu | Təyin edilmiş Linux serverləri | TCP 22 | Başqa idarəetmə mənbələrinə qadağa |
| LMS bazası | Jurnal və vaxt xidməti | Müəyyən xidmətlər | İstifadəçi cihazlarına yeni sessiya yoxdur |

Zero Trust arxitekturası daxili şəbəkədə olmağa görə avtomatik etibar vermir: qərar identiklik, cihazın vəziyyəti, resurs və tələb olunan əməliyyatla bağlanır; mikroseqmentasiya onun tətbiqi vasitələrindən biridir (Zero Trust üçün əsasdır). Şəbəkə səviyyəsində TCP 443 icazəsi tələbəyə başqa tələbənin qiymətini dəyişmək səlahiyyəti vermir: tətbiq hər sorğuda avtorizasiya yoxlamalıdır. Şəbəkə və tətbiq sərhədləri fərqli sualları cavablandırır.

İdentiklik əsaslı qaydada «LMS tətbiqi» etiketi dəyişən IP ünvanlarını qismən əvəz edə bilər. Lakin etiketi kim təyin edir? Kafedranın adi istifadəçisi öz virtual maşınına bu etiketi verə bilirsə, siyasət dolanılır. Etiket dəyişməsi inzibati hüquq sayılır və audit edilir. Asılılıqlar əvvəl müşahidə olunur, xidmət sahibi ilə yoxlanır, sonra dar qaydaya çevrilir; müşahidə olunan bütün trafiki avtomatik qanuni saymaq köhnə səhvi və mövcud hücumu normaya daxil edə bilər.

### Bulud və konteyner sərhədləri

Virtual özəl buludda (Virtual Private Cloud, VPC) alt şəbəkələr, marşrut cədvəlləri və resurs qaydaları birlikdə işləyir. Public subnet adı hər resursun İnternetdən əlçatan olduğunu göstərmir: ictimai ünvan, marşrut və giriş icazəsi də lazımdır. Private subnet-dəki serverin geniş çıxışı sızmaya imkan verə bilər. LMS-in bir hissəsi buluda köçəndə kampusdan buluda tunel və bulud idarəetmə API-si də təhdid modelinə əlavə olunur.

| | AWS security group | Network ACL |
| --- | --- | --- |
| Səviyyə | Resursun şəbəkə interfeysləri | Alt şəbəkə |
| Vəziyyət | Stateful | Stateless |
| Qaydalar | Yalnız icazə; tətbiq olunan qrupların icazələri birləşir | Nömrələnmiş qaydalar |
| Cavab trafiki | Avtomatik uyğunlaşdırılır | Müştərinin müvəqqəti portları ayrıca nəzərə alınır |

Buna görə security group-un «birinci uyğun qadağa» qaydası olduğunu demək səhvdir; bu davranışlar bütün bulud məhsullarına eynilə köçürülməməlidir.

Kubernetes-də namespace yaratmaq avtomatik şəbəkə izolyasiyası vermir; NetworkPolicy-ni tətbiq edə bilən şəbəkə plagini lazımdır. Şərti nümunə lms ad məkanındakı bütün pod-lar üçün giriş və çıxışı bağlayır. Tək tətbiq edilərsə, DNS və tətbiq asılılıqları da dayanır; işlək layihədə seçicilərlə yalnız lazımi əlaqələr açılır.

```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: default-deny
  namespace: lms
spec:
  podSelector: {}
  policyTypes:
  - Ingress
  - Egress
```

Standart NetworkPolicy-də uyğun icazələr toplanır. Hər iki istiqamət məhdudlaşdırılıbsa, mənbənin çıxış siyasəti və təyinatın giriş siyasəti əlaqəni buraxmalıdır. DNS üçün UDP və TCP 53, monitorinq və identiklik xidmətləri ayrıca planlaşdırılır. Plaginin dəstəkləmədiyi siyasətin faylda olması faktiki qadağa demək deyil. Service mesh və qarşılıqlı TLS xidmət kimliyini yoxlaya bilər, amma xidmətə hər məlumatı oxumaq hüququ vermir.

:::exam Mikroseqmentasiya hər şeyi bağlamır
«Mikroseqmentasiyada hər qovşaq tamamilə izolyasiya olunur» səhvdir: yalnız lazım olan bağlantılara icazə verilir.
:::

## Firewall növləri və işləmə prinsipi

### Paketdən tətbiq sorğusuna

Şəbəkələrarası ekran (firewall) şəbəkələr və ya hostlar arasında trafiki siyasətə görə buraxan və ya dayandıran proqram və ya qurğudur; müasir növləri tətbiqin özünü də tanıyır. Yoxlama mexanizmi ilə yerləşmə forması fərqlidir: stateful mexanizm fiziki qurğuda, virtual maşında və hostda işləyə bilər; «aparat firewall» dərin yoxlama demək deyil. Yerləşməyə görə: şəbəkə firewall-u (sərhəddə), host firewall-u (fərdi, məs. Windows Defender Firewall, çıxış qaydaları da ola bilər), virtual və bulud firewall-u (AWS Security Group, Azure NSG).

**Paket süzgəci (packet filter)** hər paketin IP ünvanlarına, protokoluna, portlarına və başqa başlıq sahələrinə baxır; stateless süzgəc sessiya əlaqəsini saxlamır. Kataloqun TCP 443 portunu açmaq sadə nümunədir, lakin eyni portda zərərli HTTP sorğusu da gedə bilər. Cavab üçün geniş müvəqqəti port diapazonu açmaq əlavə diqqət tələb edir; port nömrəsi istifadəçinin kimliyini sübut etmir.

**Vəziyyəti izləyən yoxlama (stateful inspection)** sessiya cədvəli saxlayır: tələbədən kataloqa yeni TCP bağlantısı açılanda ünvanlar, portlar, protokol və vəziyyət qeyd edilir, serverin cavabı həmin əlaqəyə uyğunlaşdırılır, gözlənilməyən paket atılır. Yalnız ACK bayrağı paketi etibarlı cavab etmir. İcazəli sessiyanın içindəki tətbiq sorğusunun təhlükəsizliyi ayrıca yoxlanmalıdır.

| Növ | OSI və yoxladığı | Universitetdə tətbiq | Məhdudiyyət |
| --- | --- | --- | --- |
| Paket süzgəci | L3–L4 başlıqları | Sadə marşrut sərhədində ACL | Məzmun və sessiya konteksti məhduddur |
| Stateful firewall | L3–L4 + sessiya vəziyyəti | Zonalararası əsas giriş nəzarəti | Şifrəli məzmunu özü açmır |
| Tətbiq proksisi | L7, protokol və əmrlər | Poçt və veb girişinə vasitəçilik | Protokol dəstəyi və uyğunluq xərci |
| NGFW | L3–L7, sessiya, tətbiq, əlavə təhlükə əlamətləri | Kampus çıxışında tətbiq üzrə siyasət | Görünürlük və aktiv funksiyalardan asılıdır |
| WAF | L7 (HTTP) sorğu və cavab | LMS qarşısında veb nəzarəti | Başqa protokolları və bütün məntiq səhvlərini qorumur |

Tətbiq səviyyəli şlüz (application-level gateway, application proxy) müştəri ilə server arasında vasitəçilik edir, protokolun (HTTP, FTP, SMTP) əmrlərini yoxlayır; yavaşdır, hər protokol üçün ayrıca proksi lazımdır. İki ayrı bağlantı saxladığından mənbə ünvanı serverdə dəyişə bilər; real müştəri ünvanının jurnala etibarlı ötürülməsi ayrıca qurulur, istifadəçinin göndərə bildiyi başlıq real IP sübutu deyil. Proksi arxitekturası 7-ci mövzudadır.

Növbəti nəsil firewall (next-generation firewall, NGFW) stateful yoxlamanı tətbiq tanınması (port 443-də Telegram ilə bankı ayırır), istifadəçi konteksti, daxili IPS və TLS yoxlaması ilə birləşdirir; vahid standart funksiyalar siyahısı yoxdur. Port 443-dəki hər tətbiqin düzgün tanınacağını və TLS məzmununun avtomatik görünəcəyini fərz etmək olmaz. Satınalma sınağında universitet öz LMS, video dərs və kitabxana trafiki ilə tanınma, gecikmə və səhv bloklamanı ölçməlidir. Bütün funksiyalar açıq olanda sürət düşür, qurğu bahadır.

Veb tətbiq firewall-ı (Web Application Firewall, WAF) HTTP metodunu, URI-ni, başlıqları və gövdəni təhlil edir (SQL inyeksiyası, XSS). LMS formasına SQL fraqmenti şübhəlidir, lakin proqramlaşdırma dərsində həmin mətn qanuni cavab da ola bilər. WAF parametrli sorğuları, təhlükəsiz proqramlaşdırmanı, tətbiq avtorizasiyasını və şəbəkə firewall-unu əvəz etmir: obyekt identifikatorunu dəyişib başqa tələbənin sənədini oxumaq normal HTTP sorğusu kimi görünür, istifadəçi hüququnu tətbiq yoxlamalıdır.

:::exam Köhnə OSI təsnifatı
Köhnə slaydlarda firewall-lar «şəbəkə, seans və tətbiq səviyyəsində» verilib. Dəqiqi: paket süzgəci IP ünvanlarına (L3) və portlara (L4) baxır; stateful inspection ayrıca «seans səviyyəli firewall» deyil, L3–L4 süzgəcin sessiya cədvəli ilə formasıdır.
:::

### Sessiya və resurs məhdudiyyətləri

UDP-də TCP əl sıxışması yoxdur; stateful qurğu UDP axınını ünvanlar, portlar və vaxt həddi ilə izləyə bilər. DNS cavabı sorğuya bağlanır, amma məzmunun həqiqiliyinə zəmanət deyil. ICMP-də port anlayışı bütün mesajlara tətbiq olunmur: tip, kod və əlaqəli xəta məlumatı nəzərə alınır.

Sessiya cədvəlinin tutumu məhduddur: çoxlu yarımçıq və ya qısamüddətli bağlantı onu doldura bilər. Asimmetrik marşrutda sorğu bir firewall-dan, cavab digərindən keçirsə, vəziyyət cədvəli cavabı tanımaya bilər; ona görə ehtiyat qurğular arasında sessiya sinxronluğu və marşrutlar yoxlanır. İmtahan portalında uğursuz ehtiyat keçidi təhlükəsizlik hadisəsi olmadan da dərsi poza bilər.

Firewall seçərkən yalnız reklam edilən maksimum sürət götürülmür: paket ölçüsü, saniyədə yeni sessiya, eyni vaxtda sessiyalar, TLS yoxlaması, IPS qaydaları və jurnal yazısı birlikdə ölçülür; bütün yoxlamalar açıldıqda qurğu gecikmə həddini aşa bilər. Yeniləmə qaydası və heyətin bacarığı da istismar xərcidir.

## İcazə matrisi və işlənmiş qayda dəsti

### Tələbin qaydaya çevrilməsi

Minimal səlahiyyət (least privilege) mənbəyə yalnız iş üçün lazım olan təyinat və xidməti açır. Standart qadağa (default deny) açıq icazəsi olmayan əlaqəni dayandırır; bu, minimal səlahiyyətin şəbəkədəki formasıdır. «Kafedra serverlərə çıxsın» yoxlana bilən tələb deyil; «Kafedra cihazları DMZ giriş serverinin TCP 443 xidmətinə çıxsın» konkretdir. Qaydanın sahibi, məqsədi, dəyişiklik qeydi və yenidən baxış vaxtı saxlanılır; müvəqqəti istisnaya bitmə tarixi verilir.

| Mənbə | Təyinat | Xidmət | Məqsəd və məsul tərəf |
| --- | --- | --- | --- |
| İnternet | 203.0.113.10 | TCP 443 | LMS açıq girişi; LMS xidməti |
| VLAN 10 və 20 | 10.10.70.10 | TCP 443 | Daxili DNS ilə LMS girişi; tədris İT-si |
| VLAN 30 | 10.10.40.20 | TCP 443 | Maliyyə tətbiqi; maliyyə İT-si |
| 10.10.70.10 | 10.10.40.10 | TCP 443 | Tərs proksidən LMS-ə; LMS xidməti |
| 10.10.40.10 | 10.10.80.10 | TCP 5432 | LMS sorğuları; baza administratoru |
| 10.10.40.20 | 10.10.80.20 | TCP 5432 | Maliyyə sorğuları; baza administratoru |
| 10.10.60.10 | Təyin olunmuş serverlər | TCP 22 | Nəzarətli idarəetmə; sistem qrupu |
| İdarə olunan zonalar | 10.10.90.53 | UDP və TCP 53 | Daxili ad həlli; şəbəkə qrupu |
| İdarə olunan zonalar | 10.10.90.123 | UDP 123 | Vaxt sinxronluğu; şəbəkə qrupu |
| Server və şəbəkə qurğuları | 10.10.90.20 | TCP 6514 | TLS üzərindən syslog; SOC |
| Serverlər və karantin | 10.10.90.30 | TCP 443 | Təsdiqli yeniləmə; sistem qrupu |
| Tələbə və kafedra zonaları | 10.10.110.10 | TCP 443 | Kitabxana kataloqu; kitabxana İT-si |

İdarə olunan zonalar bu nümunədə VLAN 10, 20, 30, 40, 60, 70, 80, 90 və 110-dur. Qonaq və yataqxana DNS sorğusunu öz şlüzündəki məhdud resolver xidmətinə göndərir, daxili resolverə giriş almır; ictimai LMS ünvanına İnternet siyasəti ilə çıxır. DHCP-nin lokal yayımı və relay trafiki marşrutlaşdırılan axınlardan ayrıca qurulur; relay-dən serverə icazə qonaqdan bütün infrastruktura icazə deyil.

Karantinə keçən cihaz yalnız ünvan alma, məhdud DNS və yeniləmə çıxışlarını alır; sərbəst veb və daxili resurslar bağlanır. Yeniləmə serveri vasitəsilə istənilən sayta tunel mümkün olmamalıdır, serverin öz çıxışı da nəzarətdədir. Ortaq xidmət istisnaları default deny-ni deşən «infrastrukturaya hər şey açıqdır» qaydasına çevrilməməlidir (DNS, NTP və jurnal çıxışları matrisdə ayrıca dar qaydalardır).

### Ardıcıllıq və qaydanın kölgədə qalması

Klassik ardıcıl siyasətdə qaydalar yuxarıdan aşağı yoxlanır və ilk uyğun qayda yekun qərardır (bəzi bulud vasitələri, məs. AWS Security Group, başqa cür işləyir). Konkret məhsulda zəncirlər, prioritetlər və əlavə mərhələlər fərqlənə bilər. Cədvəl yeni sessiyalar üçün məntiqi ardıcıllıqdır; DNAT tələb olunan halda uyğun mərhələdə aparılmış sayılır, zona daxilində host qaydaları ayrıca qalır.

| Sıra | Uyğunluq | Qərar | İzah |
| --- | --- | --- | --- |
| 1 | Mənbə ünvanı giriş zonasına uyğun deyil | At və qeyd et | Mənbə saxtalaşdırılmasına nəzarət |
| 2 | Etibarsız vəziyyətli paket | At | Sessiya məntiqinə uyğun deyil |
| 3 | İcazəli sessiyanın uyğun cavabı | Burax | Established və əlaqəli cavablar |
| 4 | Qonaq və yataqxanadan öz şlüz xidmətlərinə | Dar icazə | DNS və ünvanlama ehtiyacı |
| 5a | Qonaq və yataqxanadan ilkin təyinatı 203.0.113.10:443, DNAT-dan sonrakı təyinatı 10.10.70.10:443 olan TCP | Burax | İctimai LMS üçün hairpin DNAT ayrıca qurulur |
| 5b | Qonaq və yataqxanadan kampus prefikslərinə qalan əlaqələr | At və məhdud log yaz | LMS istisnasından sonra daxili şəbəkəyə ümumi qadağa |
| 6 | İnternetdən DMZ giriş serverinə TCP 443 | Burax | Yalnız ictimai xidmət |
| 7 | Matrisdəki konkret tətbiq əlaqələri | Burax | Mənbə, təyinat və xidmət birlikdə |
| 8a | Administrator roluna bağlı VPN ünvanlarından 10.10.60.10-a TCP 22 | Burax və qeyd et | Keçid hostuna giriş; adi VPN istifadəçilərinə aid deyil |
| 8b | Keçid hostundan seçilmiş serverə TCP 22 | Burax və qeyd et | Keçid hostundan sonrakı idarəetmə yolu |
| 9 | Müəyyən mənbədən DNS, vaxt, jurnal, yeniləməyə | Dar icazə | Ortaq xidmətlər |
| 10 | Qonaq, yataqxana və təsdiqli istifadəçidən xaricə | Siyasətə uyğun burax | Daxili təyinatlar əvvəl ayrılıb |
| 11 | Qalan bütün yeni əlaqələr | At və məhdud log yaz | Default deny |

Xarici təyinat «universitetin öz prefiksləri deyil» şərti və çıxış interfeysi ilə müəyyənləşir. Təkcə RFC 1918 ünvanlarını bağlamaq kifayət deyil: universitetin ictimai və IPv6 prefiksləri də daxili resurs daşıyır. İnternetdən gələn öz daxili ünvanımızı iddia edən paket girişdə atılır; VPN istifadəçisinin tunel ünvanı onun sonlandığı zona ilə yoxlanır. Anti-spoof qaydası real topologiyanı bilmədən yazılarsa, qanuni tunel trafikini poza bilər.

Kölgədə qalmış qayda (rule shadowing) əvvəlki daha geniş qaydaya görə işləməyən qaydadır. 3-cü sətirdə «istənilən mənbədən printerə TCP 9100 icazə», 15-ci sətirdə «qonaqdan daxilə qadağa» varsa, qonaq trafiki 3-cü sətrə uyğun gəlir, 15-ə çatmır və qonaq printerə çıxır. Həll yalnız qadağanı yuxarı qaldırmaq deyil, printer icazəsinin mənbəsini də daraltmaqdır.

:::exam Qayda var, amma işləmir
Situasiya sualında «qayda var, amma işləmir» deyilirsə, ilk növbədə sıraya bax: «İstənilən → istənilən → icazə» qaydası yuxarıdadırsa, altındakı bütün qadağalar heç vaxt işləmir.
:::

### Konfiqurasiya fraqmenti və paketin izlənməsi

nftables fraqmenti tədris laboratoriyasında üçpilləli LMS yolunu göstərir; interfeyslər VLAN nömrəsinə uyğun adlanıb. Bu, tam kampus konfiqurasiyası deyil: NAT, idarəetmə, anti-spoof, DNS və digər icazələr yoxdur. `forward` qurğudan keçən trafik üçündür; qurğuya gələn `input` və ondan çıxan `output` ayrıca siyasət tələb edir. Fraqment işlək firewall-a bütöv əvəzləmə kimi tətbiq edilməz.

```nft
table inet campus_demo {
  chain forward {
    type filter hook forward priority 0; policy drop;
    ct state invalid drop
    ct state established,related accept
    iifname "v10" ip saddr 10.10.10.0/24 \
      ip daddr 10.10.70.10 tcp dport 443 counter accept
    iifname "v70" ip saddr 10.10.70.10 \
      ip daddr 10.10.40.10 tcp dport 443 counter accept
    iifname "v40" ip saddr 10.10.40.10 \
      ip daddr 10.10.80.10 tcp dport 5432 counter accept
    limit rate 5/second burst 10 packets \
      log prefix "campus_drop " counter drop
  }
}
```

Log tezliyi və partlayış həddi şərti seçilib. Məhdudlaşdırılmış log qaydası paketi buraxmır, sonrakı drop qalanları atır; sürət məhdudiyyəti ilə drop eyni qaydada yanlış birləşdirilsə, həddən artıq paketlərin aqibəti sonrakı qaydadan asılı qalar, ona görə ayrı göstərilib. `inet` ailəsi hər iki IP ailəsini əhatə etsə də, `ip` meyarları yalnız IPv4-dür: ayrıca IPv6 icazələri olmadan tam ikili protokol siyasəti alınmır.

**Paketin izlənməsi.** Tələbə 10.10.10.25:51514-dən 10.10.70.10:443-ə SYN göndərir; ilk yeni sessiya icazəli qaydaya uyğun gəlir və vəziyyət cədvəlinə düşür, qayıdan SYN-ACK həmin əlaqəyə aiddir. Tələbənin yüksək nömrəli portunu bütün mənbələrə açmaq lazım deyil. Eyni anda 10.10.80.10:5432-yə yeni sessiya açsa, icazə tapılmır və son qayda paketi atır.

**Çıxış trafiki (egress).** Yalnız daxil olan (ingress) trafiki süzmək azdır. Bazanın istənilən İnternet ünvanına TCP 443 açması C2 və məlumat çıxarılması kanalı yarada bilər; çıxış süzgəci yoluxmuş kompüterin hücumçunun serverinə qoşulmasını çətinləşdirir (serverlər İnternetə istənilən portla çıxmamalıdır). Daha dar seçim: təsdiqli yeniləmə serveri, konkret xarici asılılıq və DNS yolu. Domen əsaslı icazədə adın IP-yə çevrilməsi, ortaq hostinq və ünvan dəyişməsi qiymətləndirilir; domenin siyahıda olması uzaq xidmət hesabının kompromitasiya riskini aradan qaldırmır.

## NAT, IPv6 və VPN yolları

### Ünvan çevrilməsi giriş icazəsi deyil

Şəbəkə ünvanlarının çevrilməsi (Network Address Translation, NAT) paketin ünvan sahəsini dəyişir. Mənbə NAT-ı (SNAT) çıxan paketin mənbəsini, təyinat NAT-ı (DNAT) gələn paketin təyinatını dəyişir; port çevrilməsi bir ictimai ünvanı çoxlu daxili əlaqə üçün paylaşmağa imkan verir. NAT şifrələmə, istifadəçi autentifikasiyası və ya tətbiq proksisi deyil; eyni qurğuda NAT və firewall işlədiyindən qarışdırılır.

| Axın | Çevrilmədən əvvəl | Çevrilmədən sonra |
| --- | --- | --- |
| İnternetdən LMS-ə | 198.51.100.25:51514 → 203.0.113.10:443 | 198.51.100.25:51514 → 10.10.70.10:443 |
| Tələbədən xaricə | 10.10.10.25:52000 → 192.0.2.80:443 | 203.0.113.20:62001 → 192.0.2.80:443 |
| DMZ-dən tətbiqə | 10.10.70.10:53000 → 10.10.40.10:443 | NAT yoxdur; ayrıca proksi bağlantısıdır |

Birinci sətirdə DNAT ictimai ünvanı DMZ ünvanına dəyişir, amma trafik ayrıca firewall icazəsi də almalıdır. İkinci sətirdə ünvan və port uyğunluğu cavabın düzgün daxili cihaza qayıtması üçün saxlanılır (əks çevrilmə). Daxili ünvanın görünməməsi müəyyən təsir yaratsa da, NAT açıq portu, zərərli çıxış sessiyasını və zəif tətbiqi özbaşına qorumur. IPv6-da NAT olmadan da stateful giriş nəzarəti qurulur.

NAT ilə filtrin icra sırası məhsuldan asılıdır. Linux-un tipik yönləndirilən DNAT yolunda təyinat prerouting mərhələsində dəyişir, forward filtri daxili təyinatı görür, SNAT adətən postrouting-də aparılır; başqa məhsul qayda interfeysində ilkin və ya çevrilmiş ünvanla işləyə bilər. Audit zamanı «qayda hansı ünvanı görür?» sualı sənəd və iz qeydi ilə cavablanır, təxmin əsasında yazılan qayda yararsız ola bilər.

Daxili tələbə ictimai LMS adına müraciət edəndə hairpin NAT tələb oluna bilər. Nümunədə daxili DNS adı 10.10.70.10-a həll edir və trafik yenə DMZ siyasətindən keçir; sertifikat adla uyğun qalmalıdır. NAT jurnalları vaxt, protokol və portları saxlamasa, ünvanı paylaşan cihazlardan hansının hadisəyə aid olduğunu tapmaq çətinləşir.

### IPv6-da paralel sərhəd

İkili protokol mühitində (dual stack) IPv4 qadağası IPv6 qadağası demək deyil. Sənədləşdirmə prefiksi 2001:db8:6::/48: VLAN 10-a 2001:db8:6:10::/64, VLAN 80-ə 2001:db8:6:80::/64 ayrılır. Qlobal IPv6 ünvanı olan bazanın girişində ayrıca qadağa yoxdursa, IPv4 testinin uğuru yanlış rahatlıq yaradır; ünvanın ictimai routable olması ilə firewall icazəsi ayrı anlayışlardır.

IPv6-da ICMPv6-nı bütövlükdə bloklamaq düzgün deyil: qonşu aşkarlanması və Packet Too Big mesajları bağlantı üçün lazımdır; növlər və istiqamətlər üzrə əsaslandırılmış qaydalar yazılır. Saxta marşrut elanlarına qarşı kommutator funksiyaları, məsələn RA Guard, nəzərdən keçirilir. Genişlənmə başlıqları və fraqmentlər də sensor və firewall sınağına daxildir. IPv6-nı idarə etməmək onun işləmədiyi demək deyil.

### Tunelin açıldığı nöqtədən sonrakı siyasət

Xarici sensor VPN paketini şifrəli tunel kimi görür; daxili tətbiq trafiki tunel sonluğundan sonra görünür. Uzaqdan giriş, kampuslararası və tərəfdaş bağlantıları fərqli rol qruplarına ayrılır. Tunel firewall-da, marşrutlaşdırıcıda, ayrıca qurğuda və ya proqram xidmətində sonlana bilər; nəzarət onun açıldığı yerdən sonra qurulur. 10.10.130.0/24 hovuzunun hamısına serverlərə ümumi giriş vermək oğurlanmış əməkdaş hesabını geniş şəbəkə hüququna çevirər.

Şifrəli VPN etibarsız daşıma şəbəkəsini etibarlı etmir, iki sonluq arasında qorunan kanal qurur. MPLS əsaslı ayrılma və L2TP təkbaşına məxfilik şifrələməsi vermir; PPTP təhlükəsiz seçim sayılmır. VPN protokolları 7-ci mövzudadır; burada tələb: tunel istifadəçisinin rolu, cihaz vəziyyəti və hədəf xidməti açıldıqdan sonra da yoxlanır.

Bölünmüş tuneldə (split tunnel) istifadəçinin bəzi trafiki universitetə, qalanı birbaşa İnternetə gedir. Tam tuneldə də IPv6 və DNS yolları ayrıca yoxlanmasa, çıxış nəzarətdən kənarda qala bilər. İki şəbəkəyə qoşulmuş host, ehtiyat marşrut, bulud peering və icazəsiz şəxsi tunel eyni problemi yaradır. Nəzarəti yan keçən yol tapılanda yalnız port qadağası deyil, marşrut və sonluq siyasəti də düzəldilir.

## Firewall auditi və təhlükəsiz istismar

Audit planlaşdırılmış siyasətlə faktiki konfiqurasiyanı müqayisə edir: əvvəl topologiya və ünvan obyektləri, sonra qaydalar xidmət sahibləri ilə yoxlanır. «Sayğac sıfırdır» qaydanın lazımsız olduğunu təkbaşına sübut etmir (illik qeydiyyat xidməti hələ işləməyə bilər); silməzdən əvvəl müşahidə müddəti və xidmət təqvimi yoxlanır. Çox istifadə olunan qaydanın qanuni olması da avtomatik nəticə deyil.

| Səhv | Universitetdə nəticə | Yoxlama və düzəliş |
| --- | --- | --- |
| Yuxarıda geniş icazə | Qonaq daxili printerə çatır | İlk uyğun qaydanı tapıb mənbəni daraltmaq |
| Köhnə ünvan obyekti | İcazə sonradan başqa serverə verilir | İnventar və DHCP tarixi ilə tutuşdurmaq |
| VLAN-lararası sərbəst routing | Tələbə maliyyə portlarını görür | Nəzarət nöqtəsini real yola qoymaq |
| Müddətsiz test istisnası | Artıq servis açıq qalır | Sahib və bitmə tarixi tələb etmək |
| Açıq idarəetmə interfeysi | Firewall hesabı hücum hədəfidir | Ayrı zona, MFA və rol bölgüsü |
| Yalnız IPv4 auditi | IPv6-dan giriş qalır | Hər iki ailə ilə eyni siyasəti sınamaq |
| Ehtiyat yol nəzarətsizdir | Nasazlıqda qadağalar itir | Ehtiyat keçidini ayrıca yoxlamaq |
| Jurnal və saat problemi | Hadisələr əlaqələndirilmir | Toplama sağlamlığı və NTP-ni yoxlamaq |

Dəyişiklik əvvəl ayrıca mühitdə və ya təsiri məhdud qaydada sınanır; cari konfiqurasiya saxlanır, konkret geri dönüş addımı hazırlanır, idarəetmə bağlantısını itirməyə qarşı ayrıca çıxış yolu olur. Uzaqdan default deny tətbiq edib administratorun öz yolunu bağlamaq tipik səhvdir. Dəyişiklikdən sonra yeni xidmətlə yanaşı, əvvəl işləyən kritik xidmətlər də yoxlanır. İmtahan dövründə plansız qayda dəyişməsi ayrıca riskdir.

Konfiqurasiya ehtiyatı parollar, sertifikat açarları və şəbəkə məlumatı saxlaya bilər: girişi məhdudlaşdırılır, bərpa sınanır. Yüksək əlçatanlıq cütlüyündə qayda uyğunluğu, lisenziya və sessiya keçidi yoxlanır. Audit sübutu ekran görüntüsü deyil: mənbə, təyinat, xidmət, vaxt və qayda identifikatoru olan test qeydi tələb olunur.

## IDS/IPS növləri və yerləşdirilməsi

Firewall «bu porta icazə var» deyib buraxır, amma 443-dən keçən paketin içində eksploit olub-olmadığını adi firewall bilmir; bunu IDS və IPS yoxlayır.

### Müşahidə mənbəyinə görə bölgü

IDS gördüyü hadisələri təhlil edir və şübhəli uyğunluq tapanda xəbərdarlıq yaradır. Söhbət **icazəsiz (unauthorized) girişdən** gedir, müəllif hüququndan yox. Hər xəbərdarlıq uğurlu müdaxilə deyil: cəhd əvvəl firewall-da dayandırılmış, qayda isə paketin nüsxəsində yenə işləmiş ola bilər. Analitik cəhd, ötürülmüş trafik və təsdiqlənmiş kompromitasiyanı ayırmalıdır.

Şəbəkə IDS-i (Network IDS, NIDS) paketlərə və axınlara baxır. Host IDS-i (Host IDS, HIDS) konkret cihazın jurnalını, fayl bütövlüyünü və hadisələrini izləyir. Yataqxana trafikinə baxan şəbəkə sensoru serverin lokal faylının dəyişməsini görmür; server agenti isə başqa VLAN-dakı əlaqələri görmür. Sensor seçimi məlumatın harada yarandığına əsaslanır. IPS-in ekvivalentləri NIPS və HIPS-dir.

| Növ | Mənbə | Universitet nümunəsi | Məhdudiyyət |
| --- | --- | --- | --- |
| NIDS və NIPS | Şəbəkə paketi və axını (Snort, Suricata) | DMZ və baza sərhədinin trafiki | Şifrələmə, paket itkisi, görünməyən yol |
| HIDS və HIPS | Host hadisələri və dəyişikliklər (Wazuh, OSSEC) | LMS faylları və administrator fəaliyyəti | Agent və hostun etibarlılığı |
| Simsiz IDS/IPS (WIDS/WIPS) | Radio və Wi-Fi hadisələri | Saxta kampus giriş nöqtəsi | Radio örtüyü və müdaxilə riski |
| Davranış analizi (NBA) | Axın (NetFlow), həcm, əlaqə qrafı | Laboratoriyadan çoxsaylı daxili təyinat | Dəyişmiş normal fəaliyyəti hücum saya bilər |

HIPS hostda fəaliyyəti dayandıra bilər. Son nöqtədə aşkarlama və cavab sistemi (Endpoint Detection and Response, EDR) daha geniş telemetriya və araşdırma imkanı verə bilər; HIDS ilə eyni termin deyil. Simsiz IPS-in aktiv müdaxiləsi qonşu qanuni şəbəkəyə təsir edə bilər, ona görə konkret radio mühiti və səlahiyyət çərçivəsində seçilir; sadə paket sensorundan radio örtüyü gözləmək olmaz.

### Trafik nüsxəsi və yol üzərində nəzarət

Kənar müşahidədə (out-of-band) NIDS SPAN portundan və ya şəbəkə TAP qurğusundan paket nüsxəsi alır. SPAN kommutatorun seçilmiş trafikini başqa porta köçürür; iki istiqamətin cəmi monitor portunun tutumunu aşarsa, sensor bütün paketləri almaya bilər. TAP fiziki keçiddən nüsxə verir, amma çıxışları və sensorun qəbul imkanı da düzgün seçilməlidir; «TAP var, itki yoxdur» ölçməsiz qəbul edilmir.

Yol üzərində (inline) NIPS paketi ötürülməzdən əvvəl yoxlayıb ata bilir. IPS yalnız trafik onun üzərindən keçəndə, qayda hücumu tanıyanda və bloklama açıq olanda qarşısını alır. Eyni Suricata qurğusu nüsxəni passiv oxuyursa, qaydada `drop` yazılması real paketi saxlamaq üçün kifayət deyil: icra rejimi və fiziki yol qaydanın mətnindən ayrı şərtdir.

:::figure
src = "m06-2.png"
alt = "İki sxem: yuxarıda passiv IDS kommutatorun SPAN və ya TAP nüsxəsini alıb xəbərdarlıq verir; aşağıda inline IPS İnternet ilə server arasında dayanıb yalnız buraxılan trafiki ötürür."
caption = "Şəkil 2. Passiv sensor nüsxə alır; inline IPS ötürülən paketin yolunda qərar verir."
:::

Passiv IDS başqa qurğuya bloklama əmri göndərə və ya sessiyanı sıfırlamağa cəhd edə bilər, lakin gecikən reaksiya inline nəzarət qədər zəmanət vermir: ilk zərərli sorğu serverə çata bilər. İnline IPS isə yanlış müsbətdə qanuni imtahan cavabını birbaşa dayandıra bilər. Seçim aşkarlama ilə əlçatanlıq riskinin birlikdə qiymətləndirilməsini tələb edir.

:::note Sadə dillə
IDS = siqnalizasiya, IPS = siqnalizasiya + qapını bağlayan mühafizəçi. IDS trafikin surətini analiz edib xəbərdarlıq edir; IPS yoldadır və dayandıra bilir, amma özü sıradan çıxsa və ya səhv bloklasa, xidmət də dayanar.
:::

Nasazlıqda açıq keçid (fail-open) trafikin yoxlamasız davam etməsidir (əlçatanlıq qorunur); qapalı keçid (fail-closed) trafikin dayanmasıdır (təhlükəsizlik qorunur). Heç biri hər xidmət üçün avtomatik düzgün deyil: bank üçün fail-closed, xəstəxananın təcili sistemi üçün fail-open məntiqli ola bilər. İmtahan portalında əlçatanlıq tələbi yüksəkdir, qiymət bazasına icazəsiz girişin təsiri də ağırdır. Ehtiyat sensor, məhdud bypass və xəbərdarlıqlı plan iki riski azalda bilər. Rejimin adı yox, konkret nasazlıqda real davranış sınanır.

Sensor firewall-dan əvvəl olsa, bloklanan cəhdləri də görər; sonra olsa, buraxılan trafikə diqqət verər. VPN və TLS üçün açıq məzmunun yarandığı nöqtə seçilir. Daxili baza sərhədində ikinci sensor yanal hərəkəti görə bilər; eyni hostdakı virtual maşınlar üçün virtual trafik güzgüsü və ya host monitorinqi lazımdır.

:::exam IPS həmişə bloklamır
«IPS bağlantını dərhal bloklayır» mütləq doğru deyil: IPS yalnız düzgün yerləşdiriləndə, trafiki görəndə, aşkarlama mexanizmi (imza, anomaliya və ya protokol analizi) hücumu tanıyanda və bloklama rejimi açıq olanda bloklayır.
:::

## Aşkarlama üsulları və yayınma cəhdləri

### İmza, anomaliya və protokol analizi

İmza əsaslı aşkarlama (signature-based detection) məlum nümunə və şərtlə uyğunluq axtarır. İmza sadəcə bayt sətri olmaya bilər: protokol sahəsi, istiqamət, sessiya vəziyyəti və hadisələr ardıcıllığı da şərtə daxildir. Yanlış həyəcan azdır, amma yeni (zero-day) hücumu görmür; hücumçu başqa yol və ya kodlaşdırma seçəndə sadə uyğunluq qaça bilər. İmzanın mövcudluğu bütün variantların tutulması demək deyil. Digər tərəfdən «imza heç bir naməlum hücumu tutmur» də həddən artıq qətidir: ümumi təhlükəli davranış imzası yeni istismara uyğun gələ bilər.

Anomaliya əsaslı aşkarlama (anomaly-based detection) əvvəl «normal»ı öyrənir və profildən kənarlaşmanı bildirir. Yeni hücumları tuta bilir, yanlış həyəcanı çoxdur. Kafedra fayl serveri adətən az tətbiqlə danışır, birdən çoxlu daxili ünvana yeni sessiya açır: bu, skan ola bilər, planlı inventar yoxlaması da. İmtahan həftəsi LMS yükünün artması normanın dəyişməsinə nümunədir. Profil xidmət təqvimi, istifadəçi qrupu və keçmiş insidentlərlə qurulur.

Protokol vəziyyəti analizi (stateful protocol analysis) trafiki protokolun gözlənilən qaydaları və ardıcıllığı ilə müqayisə edir; yanlış struktur, uyğunsuz uzunluq, qeyri-adi əmr ardıcıllığı şübhə yaradır. Firewall «bu paket icazəli TCP əlaqəsinə aiddirmi?» sualını, protokol analizi «bu əlaqədə protokol məntiqli işləyirmi?» sualını araşdırır. Düzgün sintaksis qanuni istifadəni sübut etmir.

| Üsul | Güclü tərəf | Universitet nümunəsi | Uğursuzluq səbəbi |
| --- | --- | --- | --- |
| İmza | Uyğunluğu izah etmək asandır | Məlum zərərli URI nümunəsi | Variant və ya görünməyən məzmun |
| Anomaliya | Əvvəl yazılmamış fərqi göstərə bilər | Bazadan qeyri-adi əlaqə həcmi | Qeydiyyat mövsümü normanı dəyişir |
| Protokol analizi | Sintaksis və ardıcıllığı yoxlayır | HTTP strukturunda uyğunsuzluq | Parser fərqi və natamam axın |
| Birləşmiş yanaşma | Fərqli sübutları əlaqələndirir | İmza, proses və baza auditinin uyğunluğu | Mənbələrin susması və yanlış zaman |

### Şifrələnən məzmun və sensorun gördüyü hissə

TLS ilə qorunan HTTP məzmununu passiv sensor açarlar və sonlandırma olmadan oxumur. IP ünvanları, portlar, vaxt, həcm və bəzi əl sıxışması məlumatı görünə bilər; bütün domen və istifadəçi məlumatının görünməsi qəbul edilmir, əlavə məxfilik mexanizmləri metadatanı da məhdudlaşdırır. «443-də hücum yoxdur» nəticəsi yalnız açıq məzmun imzasının susmasına əsaslana bilməz. Ya TLS yoxlaması (deşifrə), ya da host səviyyəsində sensor (HIDS/EDR) lazımdır.

TLS DMZ girişində sonlana bilər; girişdən tətbiqə yenidən TLS qurularsa, həmin hissədə passiv sensor yenə oxumur. WAF-ın sonlandırma nöqtəsində baxması, tətbiq jurnalları və host telemetriyası alternativ sübutdur. Şifrə açma ilə bütün daxili trafiki açıq saxlamaq eyni qərar deyil.

İstifadəçi çıxışında TLS yoxlaması etibarlı sertifikat infrastrukturu və ayrıca siyasət tələb edir; sertifikat sabitlənməsi, qarşılıqlı TLS və şəxsi cihazlar onu çətinləşdirir. Yoxlama nöqtəsi açıq məzmunla işlədiyindən özü həssasdır; istisnalar sənədləşdirilir. Şifrələməni söndürmək universal tədbir deyil.

### Sensorla son sistemin fərqli oxuması

Yayınma (evasion) sensorun gördüyü ilə son sistemin işlətdiyi məlumat arasında fərq yaratmağa çalışır. IP fraqmentləşməsi və TCP seqmentləşməsi normaldır; zərərli məzmun bir neçə paketə bölünəndə hər paketi ayrıca axtaran qayda onu qaçırar, ona görə sensor axını yenidən yığmalıdır. Üst-üstə düşən məlumat, fərqli vaxt hədləri və protokolun müxtəlif yozulması sensorla serverin fərqli məzmun çıxarmasına səbəb olur.

| Hal | Nə itə bilər | Tədbir və qalan məhdudiyyət |
| --- | --- | --- |
| Fraqment və seqmentlər | Bir neçə paketə yayılmış uyğunluq | Axını yığmaq; yaddaş və vaxt həddi qalır |
| Kodlaşdırma fərqi | URI-də eyni mənanın başqa yazılışı | Normallaşdırılmış protokol sahəsini yoxlamaq |
| Asimmetrik yol | Sessiyanın bir istiqaməti | Hər iki istiqaməti sensora gətirmək |
| SPAN və qəbul itkisi | Qaydanın tələb etdiyi baytlar | Port və sensor tutumunu ölçmək |
| Şifrəli tunel | Daxili protokol və məzmun | Sonlandırmadan sonra və hostda müşahidə |
| Aşağı sürətli davranış | Sabit say həddindən aşağı cəhdlər | Daha uzun tarix və kontekstlə korrelyasiya |

HTTP parserinin normallaşdırdığı URI ilə xam baytlar eyni olmaya bilər; qayda hansı sahəyə baxdığını göstərməlidir. Çox sərt normallaşdırma qanuni tətbiqi poza bilər, çox yumşaq yoxlama yayınmaya imkan verər. Sensor parametrləri öz serverlərin protokol davranışı ilə sınanır. CPU normal olsa belə, axın yığma limitinin aşılması aşkarlama boşluğu yaradır.

## Suricata qaydasının sahələr üzrə izahı

Suricata və Snort şəbəkə IDS/IPS alətləridir; qayda dilləri oxşardır, lakin versiya və açar söz fərqlərinə görə qaydalar yoxlanmadan köçürülmür. Aşağıdakı zərərsiz laboratoriya qaydasında ayrı sınaq serveri 10.10.40.15:80-də açıq HTTP qəbul edir (istehsalat LMS yoluna daxil deyil, təcrid olunmuş məşğələdə açılır); sensor hər iki istiqaməti görür.

```suricata
alert http 10.10.10.0/24 any -> 10.10.40.15 80 (\
  msg:"UNEC lab URI marker"; \
  flow:to_server,established; \
  http.method; content:"GET"; \
  http.uri; content:"/ids-test"; startswith; \
  sid:1000006; rev:1;)
```

Sətirsonu `\` qaydanı bir neçə sətirdə yazmaq üçündür. `alert` xəbərdarlıq əməli, `http` tətbiq protokoludur. Mənbə prefiksi yalnız laboratoriya VLAN-ı, `any` mənbə portunun sabit olmadığını bildirir, `->` istiqamətdir; təyinat sınaq serveri, port 80. Mötərizədəki seçimlər əlavə şərtlərdir. Port 80 HTTP olduğuna zəmanət vermir, ona görə protokolun tanınması da tələb olunur.

| Sahə | Məna | Səhv yozumdan qorunma |
| --- | --- | --- |
| `msg` | Analitikə göstərilən mətn | Mətnin özü trafiklə müqayisə edilmir |
| `flow:to_server,established` | Serverə gedən qurulmuş axın | Tək SYN bu şərti ödəmir |
| `http.method` | Növbəti content yoxlaması metod sahəsindədir | Bütün paketdə GET axtarılmır |
| `content:"GET"` | Metod sahəsində GET uyğunluğu | Tam bərabərlik ayrıca sərtləşdirilə bilər |
| `http.uri` | Normallaşdırılmış URI sahəsini seçir | Xam bayt axtarışı ilə eyni deyil |
| `content` və `startswith` | URI /ids-test ilə başlayır | /ids-test-other də uyğun gələ bilər |
| `sid:1000006` | Lokal qayda identifikatoru | Qayda dəstində toqquşmamalıdır |
| `rev:1` | Qaydanın dəyişiklik nömrəsi | Proqram versiyası deyil |

Bu qayda hücum imzası deyil, **görünürlük testidir**: URI-nin əvvəlində marker olan istənilən GET xəbərdarlıq yarada bilər, onu bloklamaya çevirmək mənasızdır. Şərt dəyişəndə `rev` artırılır və fərq sənədləşdirilir. `drop` əməli yalnız uyğun IPS rejimində paketi dayandırar; qaydanın adı və mətni fiziki yerləşməni dəyişmir.

**Laboratoriyada yoxlama.** Əvvəl konfiqurasiya yoxlanır, sonra hazır trafik yazısı oflayn oxunur; yollar şərtidir, oflayn nəticə üçün ayrıca mövcud çıxış qovluğu seçilir. Əmrlər şəbəkəyə hücum göndərmir: `-r` saxlanmış PCAP faylını oxuyur. Real serverdə xam HTTP sınağı əvəzinə təcrid olunmuş laboratoriya saxlanılır.

```bash
suricata -T -c /etc/suricata/suricata.yaml -S local.rules
suricata -r lab.pcap -c /etc/suricata/suricata.yaml \
  -S local.rules -l ./lab-out
```

`-T` konfiqurasiyanın və qaydanın yüklənməsini yoxlayır, düzgün aşkarlama sübutu deyil. PCAP-da uyğun GET, uyğun olmayan URI və başqa mənbədən gələn eyni marker saxlanılır; gözlənti: yalnız bütün şərtləri ödəyən sorğu xəbərdarlıq yaratsın. Sonra eyni URI TLS içində göndərilən yazıda yoxlanır: şifrə açılmırsa, qaydanın susması gözlənilir. Bu, qaydanın görünürlük sərhədini göstərir.

HOME_NET və EXTERNAL_NET dəyişənlərinin faktiki tərifi yoxlanır. EXTERNAL_NET sadəcə HOME_NET-in tərsidirsə, daxildəki iki host arasındakı hücum «xaricdən daxilə» qaydasına düşməyə bilər; yanal hərəkət üçün ayrıca istiqamət və qaydalar lazımdır. Adın «xarici» olması hər hücumçunu əhatə etdiyini göstərmir.

## Yanlış nəticələr və qaydaların tənzimlənməsi

Doğru müsbət (true positive, TP) real hücuma uyğun xəbərdarlıqdır. Yanlış müsbət (false positive, FP) qanuni fəaliyyəti hücum sayır. Yanlış mənfi (false negative, FN) real hücumu qaçırır. Doğru mənfi (true negative, TN) normal fəaliyyət barədə düzgün susur. Əvvəl sayılan vahid müəyyən edilir: paket, sorğu, sessiya, yoxsa hücum ssenarisi; bir ssenaridə yüz xəbərdarlıq yüz ayrı hücum demək deyil.

| Real vəziyyət | Sistem xəbərdarlıq verir | Sistem susur |
| --- | --- | --- |
| Hücum var | TP: doğru müsbət | FN: yanlış mənfi |
| Hücum yoxdur | FP: yanlış müsbət | TN: doğru mənfi |

Bu cədvəl qarışıqlıq matrisidir (confusion matrix). Çox yanlış müsbət analitikləri yorur, onlar real həyəcanları da görməzdən gəlməyə başlayır (alert fatigue); IPS-də isə legitim istifadəçi bloklanır. Yanlış mənfi daha təhlükəlidir: heç kim xəbər tutmur.

**İşlənmiş hesab.** 50 real hücum ssenarisinin 30-u aşkar edilir, cəmi 40 xəbərdarlıq var və hərəsi ayrıca ssenariyə uyğundur: TP = 30, FP = 40 − 30 = 10, FN = 50 − 30 = 20. Dəqiqlik (precision) = 30 / 40 = 75%, tamlıq (recall, tutma faizi) = 30 / 50 = 60%. TN verilmədiyindən ümumi düzgünlük və yanlış müsbət tezliyi hesablanmır; «xəbərdarlıqların 25%-i yanlışdır» FP-nin bütün normal hadisələrə nisbəti deyil.

:::figure
src = "m06-3.png"
alt = "İki zolaq: 50 real hücum TP = 30 və FN = 20-yə bölünür; 40 xəbərdarlıq TP = 30 və FP = 10-a bölünür. Dəqiqlik 30/40 = 75%, tamlıq 30/50 = 60%."
caption = "Şəkil 3. Şərti sınaqda 50 hücumun və 40 xəbərdarlığın bölgüsü; TN verilməyib."
:::

Çoxlu normal trafik fonunda yüksək ümumi düzgünlük aldadıcıdır: həmişə susan sensor normal hadisələrdə düzgün görünür, hücumları qaçırır. İstehsalatda bütün FN-ləri bilmək çətindir, ona görə nəzarətli sınaq, insident araşdırması və ayrıca mənbələrin sübutu tələb olunur. FP analitikin vaxtını alır, IPS-də xidməti dayandırır; FN-in təsiri hücumun nəyə çatmasından asılıdır.

Tənzimləmə (tuning) qaydanın xidmətə uyğun dəqiqləşdirilməsidir. Proqramlaşdırma imtahanında SQL mətni FP yaradırsa, bütün SQL inyeksiyası qaydalarını söndürmək əvəzinə konkret parametr, yol və tətbiq davranışı araşdırılır. İstisna dar mənbə və xidmət kontekstinə bağlanır, sahibi və baxış vaxtı yazılır; hücumçunun eyni yoldan istifadə edə biləcəyi də yoxlanır. Səs-küyün azalması təkbaşına yaxşılaşma sübutu deyil.

Hədd tətbiqi təkrar xəbərdarlıqları azaldır, amma aşağı sürətli hücumu gizlədə bilər; xəbərdarlığın sıxışdırılması ilə paketin bloklanması ayrı əməliyyatlardır. Yeni IPS qaydaları əvvəl yalnız aşkarlama (müşahidə) rejimində sınanır, yanlış müsbətlər azaldıqdan sonra məhdud əhatədə bloklama açılır; qanuni imtahan sorğuları, hücum nümunələri və yük sınaqları birlikdə yoxlanır, əvvəlki TP-lərin hələ tutulduğu təsdiqlənir.

Sensorun sağlamlığı üçün qəbul edilən və atılan paketlər, axın yığma xətaları, CPU, yaddaş, növbələr və son qayda yeniləməsi izlənir. Xəbərdarlıq gecikməsi də ölçülür: məlumat saatlarla növbədə qalırsa, fayda azalır.

## Jurnal təhlili və insident cavabı

### Hadisədən əsaslandırılmış qərara

Hadisə sistemdə baş verən fəaliyyətdir, jurnal qeydi onun saxlanılan təsviri, xəbərdarlıq aşkarlama qaydasının nəticəsi. Təhlükəsizlik insidenti məxfiliyi, bütövlüyü və ya əlçatanlığı pozan və ya real təhdid edən hadisədir. Texniki nasazlıq təhlükəsizlik insidenti olmadan da yarana bilər; disk dolması həm tutum səhvi, həm hücum nəticəsi ola bilər. Təsnifat ilkin ehtimalla açılır, sübutla dəqiqləşdirilir.

Şərti qeydlər eyni laboratoriya cihazının baza xidmətinə cəhdini və hostunda proses görünməsini göstərir (firewall sətri məhsula bağlı olmayan tədris formatıdır, vaxtlar UTC). `drop` əlaqənin bu nəzarət nöqtəsində dayandığını göstərir, bazaya daxil olunduğunu yox; ikinci sətrin ayrıca xəbərdarlıq olması birinci nəticəni dəyişmir.

```text
2026-11-08T06:15:02Z fw01 action=drop rule=R11 src=10.10.10.25 sport=52110 dst=10.10.80.10 dport=5432 proto=tcp state=new

2026-11-08T06:15:03Z nids01 event=alert sid=1000200 src=10.10.10.25 dst=10.10.80.10 label=internal_probe

2026-11-08T06:15:04Z lab25 event=process_start user=student process=network_probe parent=unknown_script
```

Analitik əvvəl cihazın həmin vaxt kimə aid olduğunu DHCP və inventardan tapır, sonra bağlantı sayını, fərqli təyinatları, host prosesini və dəyişiklik qeydini yoxlayır. Razılaşdırılmış laboratoriya işi varsa, kontekst fərqlidir; naməlum skript və əlaqəsiz həssas hədəflər varsa, cihazın məhdudlaşdırılması əsaslıdır. Tək IP uyğunluğu istifadəçinin günahını sübut etmir.

Log təhlili təhlükəsizlik və nasazlıq diaqnostikası üçündür: bağlantı alınmadıqda DNS səhvi, marşrutun olmaması, firewall qadağası və serverin dayanması ayrılır. Saatlar sinxron saxlanılır, ilkin qeyd ilə toplama vaxtı fərqləndirilir; NAT-dan əvvəl və sonra ünvanlar, sessiya və qayda identifikatorları əlaqəni bərpa edir. Parol, sessiya tokeni və imtahan cavabı jurnala ehtiyacsız yazılmamalıdır.

### Alətlər və iş axını

Təhlükəsizlik məlumatı və hadisələrinin idarə edilməsi sistemi (Security Information and Event Management, SIEM) müxtəlif mənbələrin qeydlərini toplayır, normallaşdırır və əlaqələndirir: firewall bağlantını, HIDS fayl dəyişməsini, tətbiq hesabın əməliyyatını göstərə bilər. Nümunələr: Splunk, IBM QRadar, Microsoft Sentinel, Elastic əsaslı həllər, AlienVault OSSIM. Məhsuldan əvvəl hansı aşkarlama sualına cavab lazım olduğu müəyyənləşdirilir.

| Vasitə | Verdiyi məlumat və funksiya | Əvəz etmədiyi iş |
| --- | --- | --- |
| Snort və Suricata | Şəbəkə qaydaları, xəbərdarlıq, uyğun rejimdə bloklama | Tətbiq avtorizasiyası |
| Zeek | Protokol və əlaqə jurnalları, şəbəkə müşahidəsi | Klassik inline IPS funksiyası |
| Wazuh | Host hadisələri və fayl bütövlüyü monitorinqi | Bütün şəbəkənin paket görünürlüyü |
| SIEM | Çoxmənbəli korrelyasiya və axtarış | Sübutun insan tərəfindən qiymətləndirilməsi |
| ServiceNow Security Incident Response | İnsident işi, tapşırıq, cavabın izlənməsi | Hər şəbəkə hücumunun aşkarlanması |
| Cortex XSOAR kimi SOAR | Cavab addımlarının əlaqələndirilməsi və avtomatlaşdırılması | Yanlış qaydanın düzgün qərara çevrilməsi |
| Graylog və ELK əsaslı log mühiti | Toplama, axtarış, jurnal təhlili | Hazır və tam aşkarlama örtüyü |

Təhlükəsizlik orkestrasiya, avtomatlaşdırma və cavab sistemi (Security Orchestration, Automation and Response, SOAR) təkrarlanan işi əlaqələndirir: laboratoriya cihazı məlumatını inventardan götürür, firewall qeydlərini yığır, insident işi açır. Bütün kafedra şəbəkəsini avtomatik bağlamaq yüksək təsirlidir; səlahiyyət konkret obyekt, müddət və geri dönüşlə məhdudlaşdırılır, çünki yanlış siqnal sürətlə icra olunanda səhvin təsiri də sürətlə artır.

:::figure
src = "m06-4.png"
alt = "Səkkiz addımlı axın: xəbərdarlıq qəbulu, çeşidləmə, sübut, təsir dairəsi, məhdudlaşdırma (cihaz karantini), aradan qaldırma, bərpa, bağlanma."
caption = "Şəkil 4. Xəbərdarlığın araşdırılması və məhdud cavab; təsdiq üçün firewall və host qeydləri birlikdə yoxlanır."
wide = true
:::

İş axını xəbərdarlığın qəbulundan və çeşidləmədən başlayır; aktivin kritikliyi və mümkün təsir prioriteti müəyyən edir. Analitik sübutları toplayır, təsir dairəsini yoxlayır, məhdudlaşdırma seçir: yoluxmuş cihaz karantinə keçir, LMS-ə digər qanuni girişlər saxlanılır. Sonra səbəb aradan qaldırılır, cihaz təmiz vəziyyətdən bərpa edilib normal zonaya qayıtmazdan əvvəl yoxlanır; iş görülən addımlar və aşkarlama boşluqları ilə bağlanır.

NIST SP 800-61 Rev. 3 (aprel 2025) insident cavabını kiberrisklərin idarəsi və NIST CSF 2.0 ilə bağlayır. CSF 2.0-nın altı funksiyası: Govern, Identify, Protect, Detect, Respond, Recover. Hazırlıq hücum başlananda yazılan plan deyil: məsul şəxslər, əlaqə kanalı, sübutun saxlanması, bərpa hüquqları və məşqlər əvvəl müəyyən edilir; kitabxana serverini kim təcrid edə bilər, imtahan portalı üçün kim qərar verir, planda aydın olmalıdır.

CERT və ya CSIRT insidentlərin qəbulunu, təhlilini və aidiyyəti tərəflərlə əlaqəni təşkil edən komandadır. Universitetin daxili qrupu şəbəkə operatoru və milli, sahəvi komandalarla əlaqə planı saxlayır. Azərbaycanda tanınmış mənbələr: cert.az, cert.gov.az və elmi şəbəkə üzrə sciencecert.az. Müraciətdən əvvəl təşkilatın aidiyyəti, qüvvədə olan kanal və paylaşılacaq məlumat dəqiqləşdirilir; köhnə struktur adı avtomatik cari səlahiyyət sayılmır.

Təhdid qrupuna aidiyyət iddiası texniki müşahidədən ayrılır: sosial şəbəkə bəyanatı müdaxilə sübutu deyil, vaxt, təsir, trafik və host sübutları yoxlanır. VirusTotal-da mövcud heş məlumatına baxmaq kömək edə bilər, lakin tələbə məlumatı olan faylı açıq xidmətə yükləmək sızma riskidir; nəticə mütləq zəmanət deyil.

### DDoS və xidmət davamlılığı

Paylanmış xidmətdən imtina hücumu (Distributed Denial of Service, DDoS) çoxsaylı mənbələrdən resursu və ya tətbiqi yükləyir. Kampusun İnternet xətti dolubsa, arxadakı firewall xəttin tutumunu geri qaytara bilməz; operator səviyyəsində süzgəcləmə və trafik təmizləmə xidməti (Cloudflare, Akamai kimi) tələb oluna bilər, seçim xidmətin quruluşuna uyğunlaşdırılır.

Yük balanslaşdırma normal sorğuları bir neçə serverə paylayır; coğrafi paylanma və ehtiyat xidmət dayanmanı azaldır, amma hücum filtri deyil. Bahalı axtarış və ya qiymət hesablaması az həcmli trafiklə də resurs yeyə bilər. Sürət məhdudiyyəti, keş, tətbiq optimallaşdırması və upstream müdafiə müxtəlif problemləri həll edir. Qanuni kütləvi girişi hücumdan ayırmaq üçün əvvəlki yük sınağı və xidmət təqvimi lazımdır.

## Kompleks sınaq və layihənin qiymətləndirilməsi

Magistrantın işi topologiya, ünvan planı, icazə matrisi və sübut edilən sınaq nəticəsi arasında əlaqə qurmalıdır. Ən azı beş əsas əlaqə seçilir və hər birinin niyə açıq və ya bağlı olduğu izah edilir. İki nəzarət nöqtəsinin yeri əsaslandırılır (məsələn, DMZ sərhədində firewall, baza yolunda sensor); eyni VLAN daxilində qalan əlaqə üçün işləyən əlavə nəzarət göstərilir. Sxemdə qurğu çəkmək qiymətləndirmə sübutu deyil.

| Mənbə və sınaq | Gözlənilən nəticə | Sübut | Əlavə yoxlama |
| --- | --- | --- | --- |
| VLAN 10-dan LMS-ə TCP 443 | Xidmət işləyir | İcazə sayğacı və tətbiq qeydi | Cavab yolu görünür |
| VLAN 10-dan LMS bazasına TCP 5432 | Yeni əlaqə dayanır | Qadağa qeydi və qayda ID-si | Baza başqa icazəli mənbədən işləyir |
| Qonaqdan daxili kataloqa TCP 443 | Giriş dayanır | Qonaq qadağası qeydi | İctimai LMS çıxışı qalır |
| LMS tətbiqindən öz bazasına | Sorğu işləyir | Sessiya və baza auditi | Maliyyə bazasına eyni yol bağlıdır |
| Eyni VLAN-dakı iki baza hostu | İcazəsiz əlaqə dayanır | Host və ya paylanmış firewall qeydi | Şlüzdən keçdiyi fərz edilmir |
| IPv6 ilə tələbədən bazaya | Eyni qadağa saxlanır | IPv6 qayda qeydi | ICMPv6 ehtiyacları işləyir |
| VPN-dən tələbə bazasına birbaşa giriş | Rol icazəsi yoxdursa dayanır | Tunel hesabı və daxili qayda | Tuneldən sonrakı görünürlük var |
| Ehtiyat qurğuya keçid | Siyasət saxlanır | Keçid və sessiya qeydləri | Bərpa müddəti ölçülür |

İcazəli laboratoriyada bağlantı səviyyəsi `nc -vz -w 3 10.10.80.10 5432` ilə yoxlana bilər (vaxt həddi şərtidir). Uğursuzluğu təkbaşına firewall sübutu deyil: eyni vaxtda qadağa qeydi və hədəfin işləkliyi yoxlanır. Ping-in susması TCP xidmətinin bağlı olduğunu göstərmir; brauzerdə portalın açılması bazaya birbaşa yolun bağlandığını sübut etmir. Sınaq konkret protokol və qaydaya bağlanır.

Qiymətləndirmədə istifadəçi təcrübəsi, gecikmə, yanlış bloklama, inteqrasiya, qayda idarəsi və istismar xərci nəzərə alınır. Şərti 20 ballıq rubrika: zonaların əsaslandırılması 5, icazə matrisi 5, nəzarət və sensor yerləşdirilməsi 4, sınaq sübutları 4, xidmət davamlılığı 2. Təqdimatda ən azı bir müsbət və iki mənfi sınaq olmalıdır; nəticə əsas və alternativ yollardakı qeydlərlə müdafiə edilir.

## Köhnə slaydlarla fərq

:::note Köhnə slaydlarla fərq
- Seqmentasiya yayılmanı məhdudlaşdırır, tam dayandırmır; mikroseqmentasiya hər qovşağı izolyasiya etmir.
- Alt şəbəkə yayım domenini özü bölmür (VLAN və ya marşrutlaşdırılan interfeys bölür).
- Firewall təsnifatı köhnə OSI ilə verilib; IDS tərifində «müəlliflik hüququ» səhvdir, «IPS dərhal bloklayır» mütləq deyil.
:::
