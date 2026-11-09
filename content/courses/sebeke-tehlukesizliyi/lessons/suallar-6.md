+++
title = "Seqmentasiya, şəbəkələrarası ekranlar və IDS/IPS"
unit = "suallar"
order = 6
summary = "Mühazirənin bütün nəzarət sualları, 8 situasiya tapşırığı, konspektdəki 3 situasiya, ehtimal olunan əlavə suallar və özünü yoxlama testi cavablarla."
updated = 2026-11-09

[[source]]
title = "Mühazirə 6: Seqmentasiya, şəbəkələrarası ekranlar və IDS/IPS"
note = "Elmar Cabbarov, 2026–2027"

[[source]]
title = "Midterm konspekti, Mövzu 6"
note = "Elmar Cabbarov"
+++

Hər sualı əvvəl özün cavabla, sonra cavabı aç. Universitet ünvanları, VLAN nömrələri və saylar şərti tədris nümunəsidir.

## Nəzarət sualları

:::reveal Seqmentasiya, firewall, IDS və IPS hansı ayrı qərarları verir?
- Seqmentasiya: şəbəkəni hansı hissələrə (zonalara) bölək.
- Firewall: hissələr arasında hansı trafik keçə bilər (mənbə, təyinat, xidmət).
- IDS: keçən trafikdə hücum əlaməti varmı, varsa xəbərdarlıq verir.
- IPS: uyğun yerləşdirilibsə, tanınmış hücumu yol üzərində dayandırır.
- Heç biri tətbiq avtorizasiyasını əvəz etmir; çoxqatlı müdafiədə (defense in depth) ayrı səhvləri məhdudlaşdırırlar.
:::

:::reveal Fiziki bölgü ilə mikroseqmentasiya niyə eyni təsnifat meyarı deyil?
- Fiziki/məntiqi bölgü sərhədin necə qurulduğunu göstərir (ayrı kabel və kommutator; VLAN, VRF, virtual firewall).
- Makro/mikroseqmentasiya nəzarətin miqyasını göstərir (böyük zona; iş yükü).
- Funksiya, risk və identiklik siyasətin əsasını göstərir.
- Bunlar bir-birini istisna etmir: maliyyə ayrı avadanlıqda, ayrı VLAN-da və serverlər üzrə incə qaydalarla ola bilər.
:::

:::reveal VLAN ilə IP alt şəbəkəsi nə ilə fərqlənir? İki prefiks eyni yayım domenində qala bilərmi?
- VLAN: L2, kommutasiya və yayım domeni; başqa hissəyə keçid marşrutlaşdırma tələb edir.
- Alt şəbəkə: L3, ünvan prefiksi və marşrut sərhədi; girişi avtomatik qadağan etmir.
- Bir VLAN-a bir alt şəbəkə verilməsi rahatlıqdır, qayda deyil.
- Bəli, iki prefiks eyni yayım domenində qala bilər, amma bu avtomatik L2 izolyasiyası yaratmır.
- Alt şəbəkənin sərhədini dəyişmək yayım domenini kiçiltmir; onu VLAN və ya marşrutlaşdırılan interfeys bölür.
:::

:::reveal Eyni VLAN-dakı iki cihazın trafiki niyə şlüz firewall-ından keçməyə bilər?
- Eyni VLAN-da cihazlar MAC ünvanı ilə birbaşa kommutator vasitəsilə əlaqə qurur, paket şlüzə getmir.
- Şlüz firewall-ı bu trafiki görmür.
- Həll: host firewall, port izolyasiyası, private VLAN, simsiz müştəri izolyasiyası.
- Simsiz izolyasiyanın yalnız eyni giriş nöqtəsində, yoxsa bütün mühitdə işləməsi iki fərqli giriş nöqtəsindəki cihazlarla yoxlanır.
:::

:::reveal Access, trunk və native VLAN sazlamalarında hansı səhvlər sərhədi zəiflədir?
- Adi istifadəçi portunda ehtiyacsız trunk açılması: istifadəçi nəzərdə tutulmayan VLAN-a çatır.
- Native VLAN-ın (işarəsiz kadr) iki tərəfdə uyğun qurulmaması.
- Trunk üzərində lazımsız VLAN-ların daşınması; son cihaz portunda trunk razılaşdırılmasının açıq qalması.
- İstifadə olunmayan portun bağlanmaması; idarəetmə VLAN-ının istifadəçi portlarına verilməsi.
- Portun təyinatının sənəd və real kommutatorda uyğun olmaması; VLAN nömrəsinin gizlədilməsinə güvənmək (o parol deyil).
:::

:::reveal Universitetin DMZ giriş serverindən bazaya birbaşa yol niyə bağlanır?
- DMZ xaricdən əlçatan olduğundan ələ keçirilmə ehtimalı yüksəkdir.
- Üç ayrı bağlantı var: İnternet-giriş serveri TCP 443, giriş serveri-LMS tətbiqi TCP 443, tətbiq-baza TCP 5432; hər birinin ayrı icazəsi var.
- Ələ keçən DMZ serveri daxili şəbəkəyə, xüsusilə bazaya birbaşa yol tapmamalıdır.
- DMZ-dən daxilə açılan TCP 443 də risksizdir demək deyil: tətbiq autentifikasiyası, sorğu məhdudiyyəti, yeniləmə, jurnal qalır.
:::

:::reveal Mikroseqmentasiya etiketini dəyişmək hüququ niyə həssasdır?
- Qayda «LMS tətbiqi» kimi etiketə bağlıdırsa, etiket verə bilən istifadəçi öz maşınını həmin rola daxil edib siyasəti dolana bilər.
- Ona görə etiket dəyişməsi inzibati hüquq sayılır və audit edilir.
- Asılılıqlar əvvəl müşahidə olunur, xidmət sahibi ilə yoxlanır, sonra dar qaydaya çevrilir; müşahidə olunan hər trafiki avtomatik qanuni saymaq köhnə səhvi və mövcud hücumu normaya daxil edə bilər.
:::

:::reveal AWS security group ilə network ACL-in cavab trafikinə münasibəti necə fərqlənir?
- Security group: resurs interfeyslərində, stateful; cavab avtomatik uyğunlaşdırılır; yalnız icazə qaydaları, tətbiq olunan qrupların icazələri birləşir (birinci uyğun qadağa qaydası yoxdur).
- Network ACL: alt şəbəkədə, stateless, nömrələnmiş qaydalar; cavab trafiki, o cümlədən müştərinin müvəqqəti portları ayrıca nəzərə alınır.
- Bu davranışlar bütün bulud məhsullarına eynilə köçürülməməlidir.
:::

:::reveal Kubernetes-də namespace və NetworkPolicy hansı şərtlərlə real ayrılma yaradır?
- Namespace özü şəbəkə izolyasiyası vermir.
- NetworkPolicy-ni tətbiq edə bilən şəbəkə plagini olmalıdır; plagin dəstəkləmirsə, fayl faktiki qadağa deyil.
- Siyasət doğru namespace-də və doğru seçicilərlə olmalı; uyğun icazələr toplanır.
- Hər iki istiqamət məhdudlaşdırılıbsa, mənbənin çıxış və təyinatın giriş siyasəti əlaqəni buraxmalıdır.
- Default deny DNS (UDP və TCP 53) və asılılıqları da dayandırır, onlar ayrıca dar açılır.
:::

:::reveal Stateless və stateful süzgəc eyni TCP cavabını necə fərqli qiymətləndirir?
- Stateless süzgəc hər paketə ayrıca baxır, sessiya əlaqəsi saxlamır: cavab üçün geniş müvəqqəti port diapazonu açmaq lazım gəlir, saxta paketi ayırmaq çətindir.
- Stateful süzgəc sessiya cədvəli saxlayır: daxildən açılmış bağlantının cavabını həmin əlaqəyə uyğunlaşdırıb buraxır, gözlənilməyəni atır.
- Yalnız ACK bayrağının olması paketi etibarlı cavab etmir.
- Hər ikisi icazəli sessiyanın içindəki zərərli tətbiq sorğusunu ayırmır.
:::

:::reveal Tətbiq proksisi, NGFW və WAF hansı məhdudiyyətlərə malikdir?
- Tətbiq proksisi: yavaş, hər protokol üçün ayrıca proksi, uyğunluq xərci; iki bağlantı saxladığından real müştəri IP-sinin jurnala ötürülməsi ayrıca qurulur.
- NGFW: vahid standart funksiya siyahısı yoxdur; port 443-dəki hər tətbiqin tanınacağı və TLS məzmununun görünəcəyi fərz edilmir; baha, funksiyalar açıq olanda sürət düşür, satınalmada öz trafikinlə sınaq lazımdır.
- WAF: yalnız veb trafiki; parametrli sorğunu, təhlükəsiz proqramlaşdırmanı, tətbiq avtorizasiyasını, şəbəkə firewall-unu əvəz etmir; qanuni SQL mətnində yanlış müsbət, obyekt ID-ni dəyişmə isə normal görünür.
:::

:::reveal Default deny siyasətində DNS, NTP və jurnal çıxışları necə planlaşdırılır?
- Hər biri matrisdə ayrıca dar qayda kimi yazılır: DNS UDP və TCP 53 (10.10.90.53), vaxt UDP 123 (10.10.90.123), jurnal TCP 6514 TLS üzərindən syslog (10.10.90.20), yeniləmə TCP 443 (10.10.90.30).
- Mənbə yalnız idarə olunan zonalar və ya konkret qurğulardır.
- Qonaq və yataqxana öz şlüzündəki məhdud resolverə çıxır; DHCP yayımı və relay ayrıca qurulur.
- Ortaq xidmət istisnaları default deny-ni deşən ümumi «infrastrukturaya hər şey açıqdır» qaydasına çevrilməməlidir.
:::

:::reveal Qaydanın kölgədə qalması nədir və hansı sınaqla tapılır?
- Əvvəlki daha geniş qayda sonrakı qaydanı işlətmir (ilk uyğunluq).
- Nümunə: 3-cü sətir «istənilən mənbədən printerə TCP 9100 icazə», 15-ci sətir «qonaqdan daxilə qadağa»; qonaq printerə çatır.
- Sınaq: qonaqdan mənfi (qadağa gözlənilir) və səlahiyyətli cihazdan müsbət sınaq; faktiki qayda sayğacları və jurnal nəticə ilə tutuşdurulur, ilk uyğun qayda tapılır.
- Həll: icazənin mənbəsini daraltmaq, qadağanı yuxarı qaldırmaq; təkrar və ziddiyyətli qaydalar audit edilir.
:::

:::reveal NAT-ın təhlükəsizlik siyasətindən fərqi nədir? Filtr hansı ünvanı görə bilər?
- NAT yalnız ünvan sahəsini dəyişir (SNAT mənbəni, DNAT təyinatı); şifrələmə, autentifikasiya, proksi və icazə deyil. Açıq portu, zərərli çıxış sessiyasını, zəif tətbiqi qorumur.
- İcazəni firewall qaydası verir; DNAT-dan sonra da ayrıca icazə lazımdır.
- Filtrin ilkin, yoxsa çevrilmiş ünvanı görməsi məhsuldan asılıdır; Linux-un tipik DNAT yolunda təyinat prerouting-də dəyişir, forward filtri daxili təyinatı görür, SNAT postrouting-dədir. Sənəd və iz qeydi ilə təsdiqlənir.
:::

:::reveal IPv6 və VPN üzrə hansı yollar IPv4-dəki qadağanı yan keçə bilər?
- IPv6: IPv4 qadağası IPv6-ya keçmir; qlobal IPv6 ünvanlı bazaya ayrıca qayda yoxdursa giriş qalır. ICMPv6 bütövlükdə bloklanmır, RA Guard nəzərdən keçirilir.
- VPN: xarici sensor tunelin içini görmür; hovuza serverlərə ümumi giriş verilərsə, oğurlanmış hesab geniş hüquq qazanır.
- Bölünmüş tunelin IPv6 və DNS yolları; ikinci şəbəkəyə qoşulmuş host, ehtiyat marşrut, bulud peering, icazəsiz şəxsi tunel.
- Düzəliş yalnız port qadağası yox, marşrut və sonluq siyasətidir.
:::

:::reveal SPAN, TAP və inline yerləşdirmə arasında hansı fərqlər var?
- SPAN: kommutatorun seçilmiş trafikini başqa porta köçürür; iki istiqamətin cəmi port tutumunu aşarsa, itki olur.
- TAP: fiziki keçiddən nüsxə verir; çıxışları və sensorun qəbul imkanı ölçülməlidir.
- Hər ikisi out-of-band (passiv): xəbərdarlıq verir, gecikən reaksiya ilk zərərli sorğunu buraxa bilər.
- Inline: paket ötürülməzdən əvvəl yoxlanıb atılır; yanlış müsbət və nasazlıq xidməti dayandırır.
- Suricata nüsxəni passiv oxuyursa, `drop` real paketi saxlamır.
:::

:::reveal İmza, anomaliya və protokol analizi hansı hallarda yanılır?
- İmza: variant, fərqli kodlaşdırma və ya görünməyən (şifrəli) məzmun; yeni (zero-day) hücum.
- Anomaliya: normal dəyişəndə (imtahan həftəsi yükü) yanlış həyəcan; planlı inventar yoxlaması skan sayıla bilər.
- Protokol analizi: parser fərqi və natamam axın; düzgün sintaksis qanuni istifadəni sübut etmir.
- Birləşmiş yanaşmada mənbələrin susması və yanlış zaman.
:::

:::reveal Suricata qaydasındakı protokol, istiqamət, flow, content, sid və rev nə deməkdir?
- `http`: tətbiq protokolu (port 80 özü HTTP sübutu deyil); `->` istiqamət; mənbə prefiksi 10.10.10.0/24, `any` mənbə portu, təyinat 10.10.40.15:80.
- `flow:to_server,established`: serverə gedən qurulmuş axın, tək SYN ödəmir.
- `http.method` və `content:"GET"`: metod sahəsində GET; `http.uri` və `content:"/ids-test"` ilə `startswith`: normallaşdırılmış URI /ids-test ilə başlayır (/ids-test-other də uyğun gəlir).
- `sid:1000006` lokal identifikator, qayda dəstində toqquşmamalı; `rev:1` dəyişiklik nömrəsi, proqram versiyası deyil.
- Qayda görünürlük testidir, hücum imzası deyil.
:::

:::reveal TP, FP, FN və TN əsasında precision ilə recall necə hesablanır?
- TP real hücuma xəbərdarlıq, FP qanuni fəaliyyətə xəbərdarlıq, FN qaçırılmış hücum, TN düzgün sakitlik.
- Precision = TP / (TP + FP); recall = TP / (TP + FN).
- Nümunə: 50 hücum, 30 tutulub, 40 xəbərdarlıq: FP = 10, FN = 20; precision 30/40 = 75%, recall 30/50 = 60%.
- TN verilmədiyindən ümumi düzgünlük və FP tezliyi hesablanmır.
:::

:::reveal TLS, paket itkisi və asimmetrik routing aşkarlamanı necə məhdudlaşdırır?
- TLS: passiv sensor açıq məzmunu görmür (IP, port, vaxt, həcm görünür); TLS yoxlaması və ya host sensoru (HIDS/EDR) lazımdır; DMZ-də sonlanıb təkrar şifrələnərsə, yenə görmür.
- Paket itkisi: SPAN və ya TAP tutumu aşılanda qaydanın tələb etdiyi baytlar sensora çatmır.
- Asimmetrik yol: sessiyanın yalnız bir istiqaməti sensora düşür, axın yığılmır, vəziyyət izlənmir; firewall-da da cavab tanınmaya bilər.
- Tədbir: hər iki istiqaməti sensora gətirmək, tutumu ölçmək, sonlandırmadan sonra və hostda müşahidə.
:::

:::reveal IPS üçün fail-open və fail-closed seçimi universitetdə necə əsaslandırılır?
- Fail-open: nasazlıqda trafik yoxlamasız keçir, əlçatanlıq qorunur. Fail-closed: trafik dayanır, təhlükəsizlik qorunur.
- İmtahan portalında əlçatanlıq tələbi yüksəkdir, qiymət bazasına icazəsiz girişin təsiri ağırdır; heç biri avtomatik düzgün deyil (bank üçün fail-closed, xəstəxananın təcili sistemi üçün fail-open).
- Ehtiyat sensor, məhdud bypass və xəbərdarlıqla plan iki riski azaldır.
- Rejimin adı yox, konkret nasazlıqda real davranış sınanır.
:::

:::reveal Xəbərdarlıqdan təsdiqlənmiş insidentə keçmək üçün hansı sübutlar tələb olunur?
- Xəbərdarlıq qaydanın nəticəsidir; hər biri uğurlu müdaxilə deyil (cəhd, ötürülmüş trafik, təsdiqlənmiş kompromitasiya ayrılır).
- Firewall `drop` yalnız nəzarət nöqtəsində dayanmanı göstərir; host qeydi (proses), qayda ID-li qeyd, vaxt və xidmət təsiri birlikdə yoxlanır.
- Cihazın həmin vaxt kimə aid olduğu DHCP və inventardan tapılır; bağlantı sayı, fərqli təyinatlar, dəyişiklik qeydi.
- Saatlar sinxron, NAT-dan əvvəl və sonra ünvanlar uyğunlaşdırılır; tək IP günah sübutu deyil; sosial şəbəkə bəyanatı sübut deyil.
:::

## Situasiya tapşırıqları

**Situasiya 1.** Universitetdə laboratoriya VLAN 10-da, maliyyə VLAN 30-dadır. Tələbə kompüterindən maliyyə serverinin TCP 445 portuna bağlantı qurulur. Şəbəkə administratoru ayrı VLAN-ların bunu dayandırmalı olduğunu düşünür. Problem haradadır?

:::reveal Cavab
- Aktiv və xassə: maliyyə serveri; məxfilik və əlçatanlıq sərhədi.
- Səbəb: VLAN ikinci səviyyəni ayırır, lakin L3 kommutator sərbəst marşrutlaşdırırsa, əlaqə mümkündür; VLAN təkbaşına təhlükəsizlik sərhədi deyil.
- Tədbir: paket yolu tapılır, həmin yolda ACL və ya daxili firewall ilə default deny tətbiq edilir; yalnız konkret xidmət ehtiyacları açılır.
- Yoxlama: portalın işlədiyi müsbət, maliyyə portunun dayandığı mənfi sınaq; qadağa uyğun qaydanın jurnalında təsdiqlənir. Eyni VLAN daxilindəki yollar ayrıca qiymətləndirilir.
:::

**Situasiya 2.** İmtahan portalında IPS proqramlaşdırma sualına verilən qanuni SQL mətnli cavabı bloklayır. Digər dərslərdə problem yoxdur. Bütün IPS-i söndürmək təklif edilir. Hansı qərar əsaslıdır?

:::reveal Cavab
- Pozulan xassə: əlçatanlıq; səbəb: yanlış müsbət və inline bloklama.
- Əvvəl konkret qayda, parametr və sorğu yolu tapılır.
- Dar istisna və ya həmin qaydanın müvəqqəti müşahidə (aşkarlama) rejimi seçilir; hücum nümunələri ilə yenidən yoxlanır.
- Bütün müdafiənin söndürülməsi əvəzinə təsiri məhdud dəyişiklik və geri dönüş tətbiq edilir.
- Növbəti imtahandan əvvəl qanuni cavab korpusu ilə sınaq aparılır.
:::

**Situasiya 3.** Kitabxana printerinə 3-cü qayda istənilən mənbədən TCP 9100 icazəsi verir. 15-ci qayda qonaq şəbəkəsindən daxili ünvanlara girişi bağlayır. Qonaq printerə çıxır. Qadağa niyə işləmir?

:::reveal Cavab
- Səbəb: ilk uyğunluqla işləyən siyasətdə trafik əvvəl geniş icazəyə düşür; aşağıdakı qadağa bu axın üçün kölgədə qalır (rule shadowing).
- Tədbir: printer icazəsinin mənbələri səlahiyyətli zonalarla məhdudlaşdırılır, qonaq siyasətinin sırası yoxlanır.
- Yoxlama: qonaqdan mənfi, kitabxananın səlahiyyətli cihazından müsbət sınaq; faktiki qayda sayğacları nəticə ilə tutuşdurulur.
:::

**Situasiya 4.** Universitet bazası IPv4 ilə tələbə zonasından bağlıdır. Lakin eyni cihaz IPv6 ünvanı ilə bazaya çatır. Komanda NAT olmadığı üçün IPv6-nı təhlükəli sayır. Düzgün izah nədir?

:::reveal Cavab
- Səbəb: problem IPv6 giriş siyasətinin çatışmamasıdır; NAT giriş nəzarətinin şərti deyil.
- Tədbir: IPv6 prefiksləri, marşrutlar və host firewall qaydaları inventara daxil edilir; eyni minimal icazələr hər iki IP ailəsində qurulur; lazımi ICMPv6 mesajları saxlanılır.
- Yoxlama: IPv4 və IPv6 üzrə ayrı müsbət və mənfi testlər; alternativ yolun bağlandığı jurnalla təsdiqlənir.
:::

**Situasiya 5.** Universitetin oflayn sınağında 50 hücum ssenarisindən 30-u tutulub, cəmi 40 xəbərdarlıq var. Layihə qrupu sensorun tamlığını 75% göstərir. Hesabı düzəldin və hansı məlumatın çatışmadığını deyin.

:::reveal Cavab
- TP = 30, FP = 40 − 30 = 10, FN = 50 − 30 = 20.
- Precision = 30 / 40 = 75%; recall (tamlıq) = 30 / 50 = 60%. 75% xəbərdarlıqların dəqiqliyidir, tamlıq 60%-dir.
- TN və normal ssenarilərin sayı olmadığından ümumi düzgünlük və yanlış müsbət tezliyi hesablanmır.
- Təkrar xəbərdarlıqlar varsa, əvvəl eyni ssenariyə aid qeydlər birləşdirilməlidir.
:::

**Situasiya 6.** Kafedra əməkdaşı VPN ilə qoşulur və bütün baza serverlərinə birbaşa çıxır. Xarici IDS yalnız şifrəli tunel görür. VPN administratoru güclü şifrələmənin kifayət etdiyini deyir. Hansı nəzarətlər çatışmır?

:::reveal Cavab
- Səbəb: tunelin qorunması daxili avtorizasiyanı əvəz etmir; hovuza geniş giriş oğurlanmış hesabı geniş hüquqa çevirir.
- Tədbir: istifadəçi roluna görə ayrıca VPN zonası və dar hədəf icazələri; idarəetmə keçid hostundan; sensor və ya nəzarət tunelin açıldığı nöqtədən sonrakı trafikə baxır.
- Yoxlama: cihaz vəziyyəti, hesabın autentifikasiyası və bağlantı jurnalları əlaqələndirilir; bölünmüş tunelin IPv6 və DNS yolları da yoxlanır.
:::

**Situasiya 7.** Universitet LMS-i Kubernetes-ə köçürüb. lms və finance namespace-ləri ayrıdır, lakin pod-lar qarşılıqlı bağlanır. Default deny faylı yazıldıqdan sonra da davranış dəyişmir. Nə araşdırılmalıdır?

:::reveal Cavab
- Səbəb: namespace avtomatik şəbəkə izolyasiyası deyil; şəbəkə plagininin NetworkPolicy dəstəyi olmaya bilər.
- Yoxlanır: plaginin dəstəyi, siyasətin doğru namespace-də olması, seçicilər, başqa siyasətlərin birləşən icazələri.
- Tədbir: həm giriş, həm çıxış məhdudiyyətləri qurulur; DNS və tətbiq asılılıqları dar açılır.
- Yoxlama: faktiki pod-lar arasında müsbət və mənfi sınaqlar; faylın mövcudluğu tətbiq sübutu sayılmır.
:::

**Situasiya 8.** İmtahan günü universitetin İnternet xətti dolur. Firewall CPU-su normaldır, amma LMS-ə heç kim çata bilmir. Server sayını artırmaq və IPS-də daha çox imza açmaq təklif edilir. Bu addımlar yetərlidirmi?

:::reveal Cavab
- Pozulan xassə: əlçatanlıq; əvvəl dar boğaz müəyyən edilir.
- Səbəb: xəttin tutumu hücum trafiki ilə dolubsa, lokal server artırılması və IPS imzaları onu boşaltmır (DDoS).
- Tədbir: operator və ya upstream trafik təmizləmə xidməti; tətbiq səviyyəli yük ayrıca araşdırılır, uyğun sürət məhdudiyyəti və paylanma seçilə bilər.
- Yoxlama: qanuni imtahan yükü ilə hücum fərqləndirilir; cavabdan sonra əsas və ehtiyat girişin işlədiyi ölçülür.
:::

## Konspektdən situasiyalar

**Situasiya 1 (konspekt).** Şirkətdə tələbə laboratoriyası VLAN 10-da, maliyyə şöbəsi VLAN 30-dadır. Pentest göstərir ki, laboratoriya kompüterindən maliyyə serverinin 445-ci portuna (SMB) qoşulmaq olur. Admin deyir: «Biz onları ayrı VLAN-lara qoymuşuq, bu mümkün deyil.» Problem nədir və necə həll edilir?

:::reveal Cavab
- Səbəb: VLAN-lar 2-ci səviyyədə ayrılıb, amma L3 kommutator VLAN-lar arasında trafiki qaydasız marşrutlaşdırır. VLAN təkbaşına təhlükəsizlik sərhədi deyil.
- Həll: VLAN-lararası trafikə ACL və ya daxili firewall, default deny; maliyyə serverinə yalnız lazım olan mənbələrdən lazım olan portlara icazə.
- Yoxlama: müsbət (icazəli bağlantı işləyir) və mənfi (laboratoriyadan 445 bloklanır) testlər; bloklanma loqda görünür.
:::

**Situasiya 2 (konspekt).** Universitet imtahan portalının qarşısına inline IPS qoyulub. İmtahan günü IPS yeni imza ilə tələbələrin cavab göndərmə sorğularını SQL inyeksiyası sayıb bloklayır, yüzlərlə tələbə cavabını göndərə bilmir. Bu hansı növ xətadır və nə edilməli idi?

:::reveal Cavab
- Yanlış müsbətdir (false positive): legitim trafik hücum sayılıb və IPS inline olduğu üçün əlçatanlıq birbaşa pozulub.
- Dərhal: problemli imza üçün istisna yazılmalı və ya imza yalnız aşkarlama rejiminə keçirilməlidir.
- Gələcək üçün: yeni imzalar əvvəl IDS rejimində sınanmalı, kritik günlərdən əvvəl dəyişiklik dondurulmalı, IPS üçün geri qaytarma (rollback) planı olmalıdır.
:::

**Situasiya 3 (konspekt).** Firewall-da 15-ci sətirdə «Qonaq Wi-Fi → Daxili şəbəkə → qadağan» qaydası var. Amma qonaqlar daxili printerə qoşula bilir. Yoxlayanda məlum olur ki, 3-cü sətirdə «İstənilən → Printerlər → TCP 9100 → icazə» qaydası durur. Nə baş verir?

:::reveal Cavab
- Qaydalar yuxarıdan aşağı oxunur və ilk uyğun qayda tətbiq edilir; qonaq trafiki 3-cü sətirdəki geniş «İstənilən» qaydasına uyğun gəlir və 15-ə çatmır: kölgədə qalmış qayda (shadowing).
- Həll: 3-cü qaydada mənbəni konkret daxili VLAN-larla məhdudlaşdırmaq və ya qonaq qadağasını yuxarı qaldırmaq.
- Qaydalar müntəzəm audit edilməlidir.
:::

## Ehtimal olunan əlavə suallar

:::reveal Seqmentasiya yayılmanı tam dayandırırmı? Mikroseqmentasiya hər qovşağı izolyasiya edirmi?
Xeyr. Seqmentasiya yayılmanı məhdudlaşdırır və çətinləşdirir; icazəli bağlantı, yanlış qayda və ya ələ keçirilmiş idarəetmə hesabı sərhədi aşa bilər. Mikroseqmentasiya hər şeyi bağlamır, yalnız lazım olan bağlantılara icazə verir (LMS tətbiqi öz bazasına, maliyyə bazasına yox). Zero Trust üçün əsasdır, amma qayda sayı kəskin artır və etiket idarəsi yükü yaranır.
:::

:::reveal Stateful inspection ilə protokol vəziyyəti analizinin (stateful protocol analysis) fərqi nədir?
Stateful firewall «bu paket icazəli TCP əlaqəsinə aiddirmi?» sualını (sessiya cədvəli, L3–L4) cavablandırır. IDS-in protokol vəziyyəti analizi «bu əlaqədə protokol standartdan kənara çıxmadan, məntiqli işləyirmi?» sualını araşdırır. Stateful inspection ayrıca «seans səviyyəli firewall» deyil, L3–L4 süzgəcin sessiya cədvəli ilə formasıdır.
:::

:::reveal IDS ilə IPS-in fərqi, növləri və yerləşməsi (NIDS, HIDS, WIDS, NBA)?
- IDS out-of-band (SPAN və ya TAP nüsxəsi) xəbərdarlıq verir; IPS inline, uyğun yerləşdikdə, qayda hücumu tanıdıqda və bloklama açıq olduqda dayandırır.
- NIDS/NIPS şəbəkə seqmentindəki trafikə (Snort, Suricata), HIDS/HIPS konkret hostda jurnal, fayl, prosesə (Wazuh, OSSEC), WIDS/WIPS simsiz mühitdə saxta giriş nöqtəsinə, NBA axın məlumatında (NetFlow) qeyri-adi həcm və istiqamətə baxır. EDR HIDS-dən geniş telemetriya verir.
- IDS: siqnalizasiya; IPS: siqnalizasiya və qapını bağlayan mühafizəçi. IDS tərifində söhbət icazəsiz girişdən gedir.
:::

:::reveal İmza əsaslı və anomaliya əsaslı aşkarlamanı müqayisə et.
- İmza: məlum nümunə; yanlış həyəcan azdır, izah asandır; yeni (zero-day) hücumu və variantı görmür. «İmza heç bir naməlum hücumu tutmur» də həddən artıq qətidir.
- Anomaliya: əvvəl «normal»ı öyrənir, kənarlaşmanı bildirir; yeni hücumu tuta bilir, yanlış həyəcanı çoxdur, norma dəyişəndə uğursuz olur.
- Protokol vəziyyəti analizi: protokolun standartdan kənar istifadəsini tapır.
- Praktikada birləşmiş yanaşma.
:::

:::reveal IDS-in niyə TLS trafikinin içini görmür və nə edilir?
TLS məzmununu passiv şəbəkə sensoru açarlar və sonlandırma olmadan oxumur; yalnız IP, port, vaxt, həcm və bəzi əl sıxışması görünür. Həll: TLS yoxlaması (deşifrə, etibarlı sertifikat infrastrukturu və ayrıca siyasətlə; yoxlama nöqtəsi özü həssasdır) və ya host səviyyəsində sensor (HIDS, EDR). Şifrələməni söndürmək universal tədbir deyil.
:::

:::reveal Yanlış müsbət ilə yanlış mənfinin fərqi; hansı daha təhlükəlidir və niyə?
FP normal trafikə hücum deyə həyəcan verməkdir; çox olsa analitik yorulur və real həyəcanları da görməzdən gəlir (alert fatigue), IPS-də isə qanuni istifadəçi bloklanır. FN real hücumu görməməkdir, daha təhlükəlidir, çünki heç kim xəbər tutmur. İstehsalatda bütün FN-ləri bilmək çətindir, ona görə nəzarətli sınaq və ayrıca mənbələrin sübutu lazımdır.
:::

:::reveal 80 hücumdan 60-ı tutulub, 100 xəbərdarlıq var. Precision, recall, FP, FN nə qədərdir?
Bu mühazirənin düsturu ilə (nümunə: 50, 30, 40): TP = 60; FP = 100 − 60 = 40; FN = 80 − 60 = 20. Precision = TP/(TP+FP) = 60/100 = 60%; recall = TP/(TP+FN) = 60/80 = 75%. TN verilmədiyindən ümumi düzgünlük hesablanmır. (Hesab nümunə olaraq düsturun tətbiqidir; mühazirədəki rəqəmlər 30/40 = 75% və 30/50 = 60%-dir.)
:::

:::reveal VLAN, alt şəbəkə, DMZ və mikroseqmentasiyanı bir cümlə ilə fərqləndir.
VLAN: L2 yayım domeni. Alt şəbəkə: L3 ünvan bloku və marşrut sərhədi, özü heç nəyi qorumur. DMZ: İnternetə açıq xidmətlərin bufer zonası; sındırılsa belə daxiliyə birbaşa yol olmamalıdır. Mikroseqmentasiya: qaydanın iş yükü səviyyəsinə endirilməsi, yalnız lazım olan bağlantılara icazə.
:::

:::reveal Firewall növlərini (texnologiyaya və yerləşməyə görə) say.
Texnologiyaya görə: paket süzgəci (stateless, L3–L4), stateful inspection (L3–L4 + sessiya cədvəli), tətbiq səviyyəli şlüz (application proxy, L7), NGFW (L3–L7, tətbiq tanıma, istifadəçi, IPS, TLS yoxlaması), WAF (L7 HTTP). Yerləşməyə görə: şəbəkə firewall-u, host (fərdi) firewall (Windows Defender Firewall), virtual və bulud firewall-u (AWS Security Group, Azure NSG).
:::
