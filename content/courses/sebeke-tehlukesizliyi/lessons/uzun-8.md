+++
title = "Simsiz şəbəkələrin əsasları və şifrələmə mexanizmləri"
unit = "uzun"
order = 8
summary = "Mühazirə tam həcmdə: radio mühiti, 802.11 standartları və kadrları, WEP-dən WPA3-ə şifrələmənin təkamülü, 4 addımlı əl sıxma, SAE, hücumlar və kampus üçün siyasət."
updated = 2026-11-09

[[source]]
title = "Mühazirə 8: Simsiz şəbəkələrin əsasları və şifrələmə mexanizmləri"
note = "Elmar Cabbarov, 2026–2027"
+++

Kabeldə trafiki dinləmək üçün kabelə və ya kommutatora fiziki yaxınlaşmaq lazımdır. Wi-Fi-da isə radiosiqnal divardan keçib korpusun qarşısındakı dayanacağa qədər çatır, hücumçu binaya girmədən trafiki qəbul edə bilir. Mövzu Wi-Fi-ın radio və kadr səviyyəsində necə işlədiyini, WEP-dən WPA3-ə qədər şifrələmənin təkamülünü, 4 addımlı əl sıxmanı, zəif parolun oflayn yoxlanmasını və universitet üçün radio planını əhatə edir. Bu mühazirədəki universitet topologiyası, ünvanlar, VLAN nömrələri və cihaz adları şərti tədris nümunəsidir.

:::note Sadə dillə
Kabeldə dinləmək üçün fiziki qoşulmaq lazımdır, Wi-Fi-da isə siqnal divarlardan keçir. Ona görə simsiz şəbəkədə şifrələmə seçimi kritikdir.
:::

## Simsiz mühitin xüsusiyyətləri

Radio mühiti ortaqdır. CSMA/CA kanal uğrunda rəqabəti idarə edir, uyğun OFDMA ötürməsində isə resurslar cihazlar arasında bölünə bilir. Bu və divardan keçən siqnal səbəbindən simsiz şəbəkədə şifrələmə seçimi kabel şəbəkəsinə nisbətən daha kritikdir.

### Əsas anlayışlar

| Anlayış | İzah |
| --- | --- |
| AP (Access Point) | Simsiz cihazları kabel şəbəkəsinə bağlayan qurğu |
| WLAN kontrolleri | Kampusdakı yüzlərlə AP-ni mərkəzdən idarə edən sistem |
| SSID | Service Set Identifier. Şəbəkənin adı, məsələn "UNI-Staff". Həqiqiliyi sübut etmir: hər kəs eyni adlı şəbəkə yarada bilər |
| BSS, BSSID | Basic Service Set və onun identifikatoru. BSS bir AP ilə əlaqəli cihazlar qrupudur; BSSID onu müəyyən edən MAC formatlı identifikatordur |
| ESS | Eyni şəbəkəyə birləşdirilmiş BSS-lər. Telefon korpusda gəzəndə bir AP-dən digərinə keçir (roaming) |
| İş rejimləri | İnfrastruktur (AP vasitəsilə, kampus şəbəkəsi), ad hoc (cihazlar birbaşa, AP-siz), mesh (AP-lər bir-biri ilə simsiz bağlıdır) |

:::exam
SSID yalnız addır. İstənilən kəs eyni adlı şəbəkə yarada bilər, ona görə ad şəbəkənin həqiqiliyini sübut etmir.
:::

### Məxfilik, tamlıq və giriş hüququ

Simsiz lokal şəbəkə (Wireless Local Area Network, WLAN) məhdud ərazidə radio vasitəsilə məlumat mübadiləsidir. Universitetdə faydası tələbənin kitabxanadan auditoriyaya gedərkən LMS sessiyasını davam etdirməsidir; kabel çəkilməsi çətin olan tarixi binada və ya müvəqqəti sərgi zalında bağlantı asanlaşır. Əvəzində divar etibar sərhədi olmur: antenanın əhatəsi ilə giriş hüququ ayrı anlayışlardır, siqnalı alan şəxs qanuni istifadəçi sayılmır.

- **Autentifikasiya (authentication)** qarşı tərəfin iddia etdiyi kimliyi yoxlayır.
- **Avtorizasiya (authorization)** tanınmış tərəfin hansı resursa çata biləcəyini müəyyənləşdirir. Tələbənin şəbəkəyə uğurlu girişi ona tələbə bazasında qiymət dəyişmək hüququ vermir; bu hüququ tətbiq ayrıca yoxlamalıdır.
- **Şifrələmə** uyğun açarı olmayan şəxsdən məlumatı gizlədir.
- **Kriptoqrafik tamlıq yoxlaması** saxtalaşdırmanı aşkar edir.
- **Təkrar ötürmədən qoruma** əvvəllər qəbul edilmiş etibarlı kadrın sonradan yenidən qəbulunu dayandırır.

Wi-Fi qorumasının sərhədi adətən cihazla AP arasındadır; AP kadrı açdıqdan sonra trafik kabel şəbəkəsinə keçir. lms.uni.example xidmətinə HTTPS bağlantısı cihazdan həmin xidmətə qədər ayrıca qorunur. AP-nin və ya kontrollerin ələ keçirilməsi radio şifrələməsinin müdafiəsini zəiflədir, amma düzgün yoxlanan HTTPS-in məzmunu şifrəli qalır. Radio qoruması tətbiq səviyyəsindəki şifrələməni əvəz etmir.

### BSS, ESS və hərəkət zamanı bağlantı

İnfrastruktur rejimində BSS bir AP funksiyası ətrafında yaranır. Bir fiziki AP müxtəlif SSID-lər üçün bir neçə virtual BSS elan edə bilər, deməli AP sayı ilə BSSID sayı bərabər olmaya bilər. SSID insan üçün addır, BSSID radio mübadiləsinin konkret xidmət dəstini ayırır; BSSID də kriptoqrafik kimlik sübutu deyil və saxtalaşdırıla bilər.

Genişləndirilmiş xidmət dəsti (Extended Service Set, ESS) paylama sistemi (Distribution System, DS) ilə əlaqələndirilmiş BSS-lərdən qurulur; mərtəbələrdəki AP-lər eyni siyasəti davam etdirəndə tələbə birindən digərinə keçir. Eyni SSID-li, amma universitetdən asılı olmayan iki AP öz-özünə eyni ESS yaratmır: arxa şəbəkə, təhlükəsizlik parametrləri və mobil keçid üçün koordinasiya lazımdır. Mesh rejimində arxa bağlantı da radio üzərindən gedir və ona ayrıca tutum ayrılmalıdır.

Rouminq (roaming) zamanı növbəti AP seçimini əsasən müştəri edir (siqnal gücü, səhv sayı, sürücü). 802.11k qonşular barədə məlumat, 802.11v şəbəkənin keçid təklifi, 802.11r sürətli keçid üçün açar mexanizmləri verir; heç biri ən yaxın AP-yə keçməyə zəmanət deyil. Köhnə AP-də zəif siqnalla qalan cihaz radio vaxtını çox tutur, ona görə əvvəl radio planı və müştəri uyğunluğu yoxlanır, sonra keçid hədləri tənzimlənir.

AP dəyişməsi ilə IP alt şəbəkəsinin dəyişməsi fərqlənir: birinci halda qısa radio fasiləsi, ikincidə ünvan yenilənməsi və sessiya qırılması da ola bilər. Açar keşlənməsi tam autentifikasiya ehtiyacını azaldır; keşin müddəti, cihaz itəndə və sertifikat ləğv ediləndə girişin dayandırılması nəzərə alınmalıdır. 802.1X və EAP-in daxili mübadiləsi 9-cu mövzuda öyrənilir.

## Standartlar və tezliklər

| Standart | Ticari ad | İl | Diapazon | Qeyd |
| --- | --- | --- | --- | --- |
| 802.11b | — | 1999 | 2,4 GHz | 11 Mbit/s |
| 802.11a | — | 1999 | 5 GHz | 54 Mbit/s |
| 802.11g | — | 2003 | 2,4 GHz | 54 Mbit/s |
| 802.11n | Wi-Fi 4 | 2009 | 2,4 və 5 GHz | MIMO |
| 802.11ac | Wi-Fi 5 | 2013 | 5 GHz | Geniş kanallar |
| 802.11ax | Wi-Fi 6, 6E | 2021 | 2,4, 5, 6 GHz | Sıx mühitdə səmərəli |
| 802.11be | Wi-Fi 7 | 2024 | 2,4, 5, 6 GHz | MLO: eyni anda bir neçə diapazon |

2,4 GHz divarlardan yaxşı keçir və uzağa çatır, amma kanal ehtiyatı azdır. 20 MHz enində kanallar üçün geniş işlədilən plan 1, 6, 11-dir. Mikrodalğalı soba və Bluetooth da bu diapazondadır, ona görə müdaxilə çoxdur. Yerli qaydaların icazə verdiyi 5 və 6 GHz kanalları daha çox spektr və ötürmə imkanı verir, amma divarlardan pis keçir; böyük auditoriyada çoxlu AP qoymaq lazım gəlir.

:::exam Tələ: Wi-Fi 6 təhlükəsizlik standartı deyil
"Wi-Fi 6" sürət və radio texnologiyasının adıdır. Wi-Fi 6 routerdə WPA2 də seçilə bilər; təhlükəsizliyi WPA2 və WPA3 müəyyən edir. Yalnız 6 GHz diapazonunda (Wi-Fi 6E və Wi-Fi 7) WPA3 və ya OWE məcburidir. Wi-Fi 7 sertifikatlaşdırmasında WPA3 tələbləri var; autentifikasiyasız şifrəli giriş isə ayrıca Enhanced Open proqramı ilə əlaqəlidir.
:::

### Tezlik, kanal eni və siqnal keyfiyyəti

Tezlik saniyədə rəqslərin sayıdır; GHz milyard hers deməkdir. Dalğa uzunluğu lambda = c / f ilə hesablanır (c təxminən 3 × 10⁸ m/s): 2,4 GHz üçün təxminən 12,5 sm, 5 GHz üçün 6 sm. Bunlar fiziki hesablamalardır, əhatə radiusu deyil: divar, antenna, ötürmə gücü və qəbuledicinin həssaslığı ayrıca təsir edir.

Kanal mərkəzi tezlik ətrafında ayrılmış spektr hissəsidir. Kanal eni 20 MHz-dən 80 MHz-ə artırılanda daha çox alt daşıyıcı yerləşir, amma qonşu AP-lər üçün sərbəst spektr azalır. Geniş kanal zəif siqnalı düzəltmir: qəbuledici küyü daha enli zolaqdan toplayır, toqquşma ehtimalı artır. Sıx auditoriyada məqsəd bütün tələbələrin istifadə edə bildiyi ümumi tutumdur.

Siqnal gücü dBm ilə yazılır; bu loqarifmik ölçüdə mənfi ədədlər normaldır, −55 dBm siqnal −75 dBm-dən güclüdür. Siqnal-küy nisbəti (Signal-to-Noise Ratio, SNR) siqnal ilə küy səviyyəsinin desibellə fərqidir: siqnal −60 dBm, küy −90 dBm olarsa SNR 30 dB; küy −70 dBm-ə qalxanda SNR 10 dB qalır və daha sadə modulyasiya, daha çox təkrar ötürmə lazım gələ bilər.

Qəbul edilən siqnal göstəricisi (Received Signal Strength Indicator, RSSI) avadanlığın verdiyi ölçüdür, müxtəlif istehsalçıların təqdimatları birbaşa müqayisə edilməməlidir. Ölçmə həm boş zalda, həm tələbələr əyləşəndə aparılır. AP-nin gücünü maksimuma qaldırmaq telefonun cavabını gücləndirmir: ikitərəfli bağlantıda zəif istiqamət məhdudiyyət qalır.

### OFDM, OFDMA və ortaq radio vaxtı

**OFDM** (Orthogonal Frequency Division Multiplexing) məlumatı çoxlu dar alt daşıyıcıya bölür; alt daşıyıcılar riyazi ortoqonallıqla bir-birindən ayrılır və ötürmə çoxşüalı yayılmaya daha davamlı olur. OFDM-in olması müxtəlif tələbələrin eyni anda eyni alt daşıyıcıda ötürməsi demək deyil: ənənəvi istifadədə bir ötürmə kanalın resurslarını müəyyən müddət tutur.

**OFDMA** (Orthogonal Frequency Division Multiple Access) alt daşıyıcı qruplarını resurs vahidlərinə (Resource Unit, RU) ayırır; AP bir planlaşdırılmış mübadilədə müxtəlif cihazlara fərqli RU verə bilər. Məsələn, LMS testində çoxlu kiçik cavab paketini ayrı-ayrı tamkanallı ötürmələr əvəzinə qruplaşdırmaq mümkündür. Fayda cihazların uyğunluğundan və planlaşdırmadan asılıdır; OFDMA idarəetmə xərclərini və kanal uğrunda rəqabəti aradan qaldırmır.

**CSMA/CA** (Carrier Sense Multiple Access with Collision Avoidance) ötürmədən əvvəl kanalı dinləyir. Kanal boş görünəndə cihaz gözləmə aralığını və təsadüfi geri saymanı tətbiq edir; kanal məşğul olanda geri sayma dayanır, boşalanda davam edir. Unicast kadrdan sonra ACK gözlənilir, təsdiq gəlməzsə təkrar ötürmə aparıla bilər. Radio cihazı kabel Ethernet-dəki kimi bütün toqquşmaları etibarlı aşkarlaya bilmir, ona görə mexanizm toqquşmadan yayınmağa çalışır.

**Gizli düyün (hidden node)** problemi eyni AP-ni eşidən iki cihazın bir-birini eşitməməsidir: auditoriyanın iki küncündəki noutbuklar kanalı boş sayıb eyni anda göndərir və AP-də toqquşma olur. RTS/CTS mübadiləsi və virtual daşıyıcı hissiyyatı olan NAV ayrılmış vaxtı qonşulara bildirərək bəzi belə toqquşmaları azaldır. Xərci: hər kiçik paketdən əvvəl RTS/CTS əlavə radio vaxtı tutur. Universal həll deyil; antenna yerləşməsi və hüceyrə ölçüsü əvvəl yoxlanır.

**MIMO** (Multiple Input Multiple Output) bir neçə antenna və radio yolları ilə məkan axınlarından istifadə edir. Kanal eni ilə məkan axını sayı fərqli resurslardır: şərti ikiantenalı noutbuk AP-nin bütün axınlarını qəbul etməyə bilər. **MU-MIMO** uyğun istifadəçilərə məkan üzrə resurs ayırır, OFDMA isə tezlik üzrə bölmə aparır. Hər ikisinin faydası cihazlara və radio şəraitinə bağlıdır.

### Auditoriya üçün kanal planı

Plan şərti universitet binası üçündür. Kanalın icazəli olması, ötürmə gücü və 6 GHz hüququ ölkənin radio qaydaları ilə müəyyənləşir; menyuda kanalın görünməsi icazə demək deyil. 1, 6, 11 planı geniş yayılıb, amma bütün ölkələrdə yeganə mümkün dəst deyil. Kanal eni və spektr maskası da üst-üstə düşmənin qiymətləndirilməsinə daxildir.

| Diapazon | Başlanğıc seçim | Yerləşdirmə prinsipi | Yoxlanılacaq məhdudiyyət |
| --- | --- | --- | --- |
| 2,4 GHz | 20 MHz, 1/6/11 təkrar istifadəsi | Yalnız tələb olunan əhatə, seçilmiş radiolar aktiv | Bluetooth, qonşu şəbəkələr, az kanal |
| 5 GHz | 20 MHz, ölçmə əsas verərsə 40 MHz | Qonşu hüceyrələrdə ayrı kanallar | DFS, müştəri uyğunluğu, kanal doluluğu |
| 6 GHz | İcazəli spektrdə 20 və ya 40 MHz-dən başlamaq | Uyğun cihazların sıx olduğu hissələr | WPA3 və ya OWE, sürücü və yerli icazə |

Dinamik tezlik seçimi (Dynamic Frequency Selection, DFS) müəyyən 5 GHz kanallarında radar xidmətlərini qorumaq üçün işləyir. Radar aşkarlananda AP kanal dəyişə bilər və dərsin ortasında qısa fasilə görünər; bu dərhal hücum sayılmır, kontrollerin radar və kanal dəyişməsi qeydləri yoxlanır. 6 GHz-in mümkün spektri ölkədən ölkəyə dəyişdiyi üçün kanal sayını universal rəqəmlə göstərmək düzgün deyil.

Tutum hesabında qoşulan cihaz sayı ilə eyni anda işləyən cihaz sayı ayrılır. Şərti 180 tələbədən 120-si eyni anda 1 Mbit/s tələb edirsə, ən azı 120 Mbit/s tətbiq yükü alınır; fiziki sürət bundan yüksək olmalıdır (başlıqlar, gözləmə, ACK, təkrar ötürmə). AP sayı yalnız bu hesabdan çıxarılmır: müştəri qarışığı, kanal doluluğu, aşağı sürətli cihazlar və kabel uplink-i ölçülməlidir.

Eyni kanalda yanaşı AP-lər radio vaxtını bölüşür; qismən üst-üstə düşən kanallarda bir-birinə yararsız müdaxilə yarada bilər. Hər partanın üstünə AP qoymaq tutumu artırmır: əvvəl əhatə xəritəsi, sonra kanal təkrar istifadəsi və güc tənzimlənir. Wi-Fi 6E 802.11ax imkanlarını 6 GHz-ə genişləndirir; Wi-Fi 6-nın 2,4 və 5 GHz-də işləməsi qüvvədə qalır.

## Kadrlar və qoşulma

802.11-də üç kadr növü var:

- **İdarəetmə kadrları** (beacon, probe, autentifikasiya, assosiasiya, deauthentication) şəbəkənin qurulmasını idarə edir.
- **Nəzarət kadrları** (RTS, CTS, ACK) radio mühitinə giriş üçündür.
- **Məlumat kadrları** faydalı yükü daşıyır.

:::figure
src = "m08-1.png"
alt = "Cihazın şəbəkəyə qoşulma mərhələləri: skan (beacon/probe), 802.11 autentifikasiya, assosiasiya, 802.1X/EAP (yalnız Enterprise), 4 addımlı əl sıxma, şifrəli trafik (DHCP, IP)."
caption = "Cihazın simsiz şəbəkəyə qoşulma mərhələləri. WPA3-Personal-da SAE 802.11 autentifikasiya mərhələsində işləyir."
wide = true
:::

802.11 mərhələsindəki "autentifikasiya" adı aldadıcıdır: açıq sistem (Open System) rejimində heç bir yoxlama aparılmır, bu yalnız protokol addımıdır. Əsl yoxlama sonrakı mərhələlərdə gedir.

Tarixən idarəetmə kadrları heç qorunmurdu, ona görə hücumçu saxta deauthentication kadrı ilə istənilən cihazı şəbəkədən ata bilirdi. **PMF** (Protected Management Frames, 802.11w) bəzi idarəetmə kadrlarını qoruyur: WPA2-də istəyə bağlıdır, WPA3-də məcburidir. Beacon, probe və ilkin assosiasiya kadrları PMF-ə daxil deyil, ona görə PMF saxta AP-nin yaradılmasına qarşı qorumur.

### Kadrın sahələri və ünvanları

802.11 kadrı radio ötürməsinin MAC səviyyəsindəki vahididir: Frame Control, Duration/ID, ünvanlar, Sequence Control, faydalı yük və FCS. Dörd ünvan və QoS sahəsi bütün kadrlarda olmur; ACK kimi nəzarət kadrları daha qısadır. Ethernet başlığını bütün radio kadrlarına tətbiq etmək səhv ünvan seçməyə gətirir.

| Sahə | Tipik ölçü | Məzmun və məhdudiyyət |
| --- | --- | --- |
| Frame Control | 2 bayt | Növ, alt növ, To DS/From DS, Retry, Protected bitləri |
| Duration/ID | 2 bayt | Radio vaxtının rezervasiyası və ya növdən asılı identifikator |
| Address 1, 2, 3 | Hər biri 6 bayt | Radio qəbuledicisi, ötürən və digər ünvan funksiyaları |
| Sequence Control | 2 bayt | Ardıcıllıq və fraqment nömrəsi, təkrarların ayrılması |
| Address 4 | Şərti, 6 bayt | Dördünvanlı paylama bağlantısında əlavə ünvan |
| QoS Control | Şərti, 2 bayt | Trafik prioriteti və əlaqəli idarəetmə məlumatı |
| Frame body | Dəyişən | İdarəetmə elementləri və ya qorunan məlumat |
| FCS | 4 bayt | Radio səhvləri üçün CRC-32, kriptoqrafik autentifikasiya deyil |

To DS və From DS bitləri paylama sisteminə (DS) istiqaməti göstərir. Ünvan rolları: **RA** radio qəbuledicisi (Receiver Address), **TA** radio ötürən (Transmitter Address), **SA** ilkin mənbə (Source Address), **DA** son təyinat (Destination Address). Radio qəbuledicisi ilə son IP xidmətinin ünvanı fərqli ola bilər: tələbə LMS-ə paket göndərəndə birinci radio qəbuledicisi AP-dir, internetdəki serverin MAC ünvanı həmin radio hopunun RA-sı deyil.

| To DS | From DS | Address 1 | Address 2 | Address 3 və 4 |
| --- | --- | --- | --- | --- |
| 0 | 0 | DA və RA | SA və TA | BSSID; dördüncü ünvan yoxdur |
| 1 | 0 | BSSID və RA | SA və TA | DA; dördüncü ünvan yoxdur |
| 0 | 1 | DA və RA | BSSID və TA | SA; dördüncü ünvan yoxdur |
| 1 | 1 | RA | TA | Address 3 DA, Address 4 SA |

Məsələn, noutbuk 02:00:00:00:08:21, AP 02:00:00:00:08:01 ünvanındadır (şərti, yerli idarə olunan MAC-lar). Noutbukdan DS-ə gedən kadrda To DS 1, From DS 0; Address 1 AP, Address 2 noutbuk. Şifrələmə məlumatı gizlətsə də radio başlığının çox hissəsi müşahidə edilə bilir.

### Qoşulma zamanı imkanların razılaşdırılması

Beacon və probe cavablarında AP şəbəkə adını, dəstəklənən sürətləri və təhlükəsizlik imkanlarını elan edir. **RSN elementi** (Robust Security Network element) şifr dəstlərini, autentifikasiya və açar idarəetməsi (Authentication and Key Management, AKM) üsullarını və PMF imkanlarını daşıyır. Cihaz assosiasiya sorğusunda uyğun seçimlərini bildirir. Eyni SSID-nin görünməsi cihazın həmin təhlükəsizlik siyasəti ilə qoşulduğunu göstərmir; seçilmiş AKM və şifr dəsti yoxlanmalıdır.

Mərhələlərin ardıcıllığı:

:::steps Qoşulma ardıcıllığı
[[step]]
title = "Kəşf"
body = "AP beacon yayır, cihaz probe göndərir; AP RSN elementi ilə təhlükəsizlik imkanlarını elan edir."

[[step]]
title = "802.11 autentifikasiya"
body = "WPA2-də Open System mübadiləsi hesabın yoxlanması deyil. WPA3-Personal-da bu mərhələdə SAE işləyir."

[[step]]
title = "Assosiasiya"
body = "Cihaz AP-yə bağlanır, imkanlar razılaşdırılır."

[[step]]
title = "Enterprise autentifikasiyası"
body = "Yalnız Enterprise-da: 802.1X/EAP mübadiləsi və uyğun açarın əldə edilməsi. Personal-da bu addım yoxdur."

[[step]]
title = "4 addımlı əl sıxma"
body = "Şifrələmə açarları yaradılır."

[[step]]
title = "Şifrəli trafik"
body = "Qorunan ötürmə qurulandan sonra DHCP ünvanı alınır, DNS ilə xidmət tapılır. EAPOL uğurlu olub DHCP cavabı gəlməyəndə problemi parol və ya AES zəifliyi kimi təsvir etmək düzgün deyil."
:::

## WEP

WEP (Wired Equivalent Privacy) 1997-ci ildə ilkin IEEE 802.11 standartının tərkibinə daxil edilib. Adı kabel şəbəkəsinə ekvivalent məxfilik vəd edirdi, bu vədi yerinə yetirmədi.

:::figure
src = "m08-2.png"
alt = "WEP-də şifrələmə prosesi: IV gizli açarla birləşdirilir, RC4 açar axını yaradır, axın XOR ilə məlumat və ICV ilə toplanır."
caption = "WEP-də şifrələmə prosesi."
:::

WEP RC4 axın şifrindən istifadə edir. Hər kadr üçün 24 bitlik başlanğıc vektoru (Initialization Vector, IV) gizli açarın əvvəlinə birləşdirilir. RC4 psevdotəsadüfi açar axını yaradır, axın XOR ilə məlumatla toplanır. Tamlıq üçün CRC-32 işlədilir. Zəifliklər üç yerdən gəlir:

- **IV qısadır.** 24 bit 16 777 216 variant deməkdir. IV-lər müstəqil və bərabər ehtimalla seçilirsə, ad günü paradoksuna görə təxminən 5000 kadrdan sonra təkrar ehtimalı 50%-ə çatır. Eyni IV eyni açar axını deməkdir və iki şifrəli mətnin XOR-u iki açıq mətnin XOR-unu verir: C1 ⊕ C2 = P1 ⊕ P2.
- **RC4-ün IV ilə birləşmə üsulu zəifdir.** Fluhrer, Mantin və Şamir 2001-ci ildə (FMS hücumu) açarı trafik yığmaqla bərpa etməyin mümkünlüyünü göstərdilər. 2007-ci ildə PTW işi uyğun trafik şəraitində açarın bərpasını xeyli sürətləndirdi.
- **CRC-32 kriptoqrafik funksiya deyil.** Hücumçu kadrın müəyyən bitlərini dəyişib CRC-ni uyğun düzəldə bilər, qəbul edən tərəf bunu görmür.

:::exam
Parolun uzunluğu burada heç nəyi dəyişmir: WEP protokol səviyyəsində sınıb. 26 onaltılıq simvoldan ibarət 104 bitlik WEP açarı da kifayət qədər uyğun trafik olduqda bərpa edilə bilər. Müddət trafikdən, açarın qurulmasından və analiz üsulundan asılıdır; bütün şərait üçün sabit dəqiqə sayı yoxdur (konspekt "bir neçə dəqiqə" deyir, mühazirə isə sabit rəqəm verməyi düzgün saymır).
:::

### XOR və axın şifrinin riyazi əsası

İstisna edən VƏ YA (exclusive OR, XOR) bitlər fərqli olduqda 1, eyni olduqda 0 verir: 0 ⊕ 0 = 0, 0 ⊕ 1 = 1, 1 ⊕ 0 = 1, 1 ⊕ 1 = 0. Hər bit üçün x ⊕ x = 0 və x ⊕ 0 = x olduğundan eyni axınla iki dəfə XOR ilkin məlumatı qaytarır. Axın şifrində (stream cipher) şifrələmə C = P ⊕ Z, açma P = C ⊕ Z formasındadır; P açıq mətn, C şifrəli mətn, Z açar axınıdır.

Şərti birbaytlıq hesab (real WEP açarı deyil): P = 10110100, Z = 01101001 olarsa C = 11011101; qəbuledici eyni Z ilə P-ni bərpa edir. Əməliyyatın sadəliyi qüsur deyil; qoruma Z-nin proqnozlaşdırıla bilməməsindən və təkrar işlədilməməsindən asılıdır.

```
P = 10110100    C = 11011101    C = 11011101
Z = 01101001    Z = 01101001    Z = 01101001
C = 11011101    P = 10110100    (açma: eyni Z)
```

Eyni Z ikinci şərti bayt P2 = 00110010 üçün işlədilsə, C2 = 01011011 alınır. İndi C ⊕ C2 = 10000110 və P ⊕ P2 = 10000110 bərabərdir: hücumçu açarı bilmədən açıq mətnlər arasında əlaqə qazanır. Birinci baytın dəyəri protokol quruluşundan məlumdursa, ikinci bayt da hesablanır. Bu, WEP, CTR və başqa axın yaratma üsullarında təkrar açar axınının niyə təhlükəli olduğunu izah edir.

XOR özü tamlıq vermir: C-nin bir biti dəyişəndə açılmış P-nin eyni biti dəyişir, kriptoqrafik autentifikasiya kodu yoxdursa qəbuledici dəyişikliyi görməyə bilər (məsələn, sensorun vəziyyət baytı). Qoruma həm gizlilik, həm etibarlı tamlıq yoxlaması tələb edir.

### WEP kadrının hazırlanması və açılması

Uzunmüddətli gizli açar çox vaxt 40 və ya 104 bitdir; reklamdakı 64 və 128 bit ifadələri buna açıq ötürülən 24 bitlik IV-ni də əlavə edir. IV gizli açarın hissəsi deyil. Problem IV ilə açarın RC4 girişində zəif birləşdirilməsi və kiçik IV məkanıdır; eyni açarı işlədən bütün cihazların IV istifadəsi birlikdə qiymətləndirilməlidir.

1. Göndərən məlumat üçün CRC-32 hesablayıb ICV (Integrity Check Value) əlavə edir.
2. IV-ni gizli açarın əvvəlinə birləşdirərək RC4 üçün giriş hazırlayır.
3. RC4 açar axını yaradır; məlumat və ICV birlikdə həmin axınla XOR edilir.
4. Kadrda IV və açar identifikatoru açıq, məlumatla ICV şifrəli ötürülür.
5. Qəbuledici IV-ni oxuyur, eyni gizli açarla axını qurur, mətni açır və CRC-ni təkrar hesablayır.

CRC təsadüfi ötürmə səhvini aşkar etmək üçün əlverişlidir, amma gizli açarla hesablanmadığına və xətti xüsusiyyətlərinə görə məqsədli dəyişikliyə qarşı sübut deyil; içəridə şifrələnməsi bunu dəyişmir. Kitabxana terminalında daha uzun WEP açarı yazmaq üç problemdən heç birini həll etmir.

### Ad günü hesabı nəyi göstərir

IV-lərin N = 2²⁴ = 16 777 216 mümkün dəyərdən müstəqil və bərabər ehtimalla seçildiyini fərz edək. İlk iki IV-nin fərqli qalma ehtimalı (N−1)/N, üçüncünün əvvəlkilərdən fərqli olması (N−2)/N-dir; n seçimdə heç bir təkrarın olmaması bu vuruqların hasilidir. n, N-dən xeyli kiçik olduqda ən azı bir təkrar ehtimalı belə yaxınlaşdırılır:

```
Pr(təkrar) ≈ 1 − exp(−n(n − 1) / (2N))
Pr(təkrar) = 0,5 üçün: n ≈ sqrt(2N ln(2)) ≈ 4823
n = 5000 üçün Pr(təkrar) ≈ 0,525
```

Beləliklə, təxminən beş min təsadüfi IV-dən sonra təkrar ehtimalı yarıya çatır. Bu, açarın mütləq bərpası demək deyil: IV toqquşması, eyni açar axınının istifadəsi və statistik açar bərpası əlaqəli, amma fərqli hadisələrdir; FMS və PTW konkret açar quruluşunu da istifadə edir.

Ardıcıl sayğacla IV seçən ötürücü sayğac dolana qədər təsadüfi modelə uyğun gəlmir, lakin yenidən başlama, eyni sayğacdan başlayan cihazlar və dövr etmə təkrar yarada bilər. Şərti 1000 kadr/s sürətində 24 bitlik məkan təxminən 4,66 saata tükənər (şərti hesab). WEP-in təhlükəsiz sayılmaması təkcə ad günü yaxınlaşdırmasına əsaslanmır.

## WPA və TKIP

WPA 2003-cü ildə müvəqqəti həll kimi çıxdı. Məqsəd WEP avadanlığını proqram yeniləməsi ilə qorumaq idi, ona görə RC4 saxlanıldı. TKIP hər paket üçün açarı qarışdırır, 48 bitlik TKIP ardıcıllıq sayğacı tətbiq edir, CRC-32 əsaslı ICV-ni saxlayır və əlavə olaraq Michael MIC tətbiq edir. Bu WEP-dən yaxşı idi, amma RC4 irsini aradan qaldırmadı. 2008-ci ildə Beck və Tews TKIP-ə qarşı məhdud hücumu göstərdilər. Bu gün WPA və TKIP işlədilməməlidir.

### TKIP-in etdiyi dəyişikliklər və həddi

Müvəqqəti açar tamlığı protokolu (Temporal Key Integrity Protocol, TKIP) köhnə çiplərin RC4 imkanını saxlayıb WEP-in bəzi qüsurlarını azaltmaq üçün hazırlanıb. Per-paket açar qarışdırılması müvəqqəti açarı, ötürənin MAC ünvanını və TKIP ardıcıllıq sayğacını (TKIP Sequence Counter, TSC) əlaqələndirir; TSC təkrar qəbulun yoxlanmasına da xidmət edir.

Michael adlı mesaj tamlığı kodu (Message Integrity Code, MIC) köhnə avadanlıq üçün yüngül hazırlanıb və güclü kriptoqrafik MAC səviyyəsində müdafiə vermir. MIC səhvlərinə qarşı əks tədbirlər xidmətin kəsilməsi ilə nəticələnə bilər. ICV yenə CRC-32-dir, ona görə TKIP AES əsaslı qoruma səviyyəsinə çatmır.

Kafedranın arxiv printeri yalnız TKIP dəstəkləyirsə, əsas şəbəkədə qarışıq TKIP/CCMP açmaq bütün istifadəçilərə köhnə seçimi saxlamaqdır; düzgün həll printerin kabelə keçirilməsi və ya dəyişdirilməsidir. Məcburi müvəqqəti istisna ayrıca seqment, məhdud xidmətlər və çıxarılma tarixi ilə sənədləşdirilir. Seqmentasiya TKIP-in zəifliyini düzəltmir.

## WPA2 və CCMP

WPA2 (2004, 802.11i standartı) RC4-ü AES ilə əvəz etdi. CCMP rejimi eyni anda iki iş görür: AES-CTR ilə şifrələyir və CBC-MAC ilə tamlığı yoxlayır.

WPA2-nin iki rejimi var. **Personal (PSK)** rejimində hamı eyni parolu işlədir. **Enterprise (802.1X)** rejimində hər istifadəçi fərdi hesabla RADIUS serverindən keçir; bu 9-cu mövzuda ətraflı öyrənilir.

### Açarlar və 4 addımlı əl sıxma

:::figure
src = "m08-3.png"
alt = "WPA2 4 addımlı əl sıxması: hər iki tərəfdə PMK var; M1 ANonce AP-dən cihaza, M2 SNonce və MIC cihazdan AP-yə, M3 şifrəli GTK və MIC, M4 təsdiq."
caption = "WPA2 4 addımlı əl sıxması (Personal rejim)."
wide = true
:::

| Açar | İzah |
| --- | --- |
| PMK | Pairwise Master Key. Personal rejimdə paroldan və SSID-dən hesablanır: PBKDF2-HMAC-SHA1, 4096 iterasiya, 256 bit. Enterprise rejimdə 802.1X-dən gəlir |
| ANonce, SNonce | AP-nin və cihazın yaratdığı təsadüfi ədədlər |
| PTK | Pairwise Transient Key. PMK, iki nonce və iki MAC ünvanından hesablanır, hər təzə açar mübadiləsində dəyişir. KCK (MIC üçün), KEK (GTK-nın şifrələnməsi üçün) və TK (məlumat üçün) hissələrinə bölünür |
| GTK | Group Temporal Key. Yayım (broadcast) trafiki üçün ortaq açar |
| MIC | Mesajın doğru açarla göndərildiyini sübut edən kod |

:::note Sadə dillə
Parol şəbəkədə heç vaxt ötürülmür. Tərəflər yalnız eyni PMK-ya sahib olduqlarını sübut edirlər. PTK hər qoşulmada yenidir və bu cihazla AP arasındakı şəxsi trafiki şifrələyir.
:::

Mesajların gedişi: M1-də AP ANonce göndərir. Cihaz öz SNonce-unu yaradıb PTK hesablayır və M2 ilə SNonce və MIC göndərir. AP eyni PTK-nı hesablayıb MIC-i yoxlayır, M3 ilə şifrəli GTK göndərir. Cihaz M4 ilə təsdiqləyir.

PMK ilə PTK müxtəlif ömürlü açarlardır: PMK trafik şifrəsinin özü deyil, ondan AP-cihaz cütlüyünə bağlı PTK törəyir. Personal rejimdə eyni parol və SSID eyni PMK verir, təzə nonce-lar PTK-nı dəyişir. Enterprise-da PMK autentifikasiya nəticəsindən alınır. SAE-də parol sabit PSK kimi işlənmir, qarşılıqlı mübadilə PMK yaradır.

**PBKDF2 hesabı.** Parol əsaslı açar törətmə funksiyası (Password-Based Key Derivation Function 2, PBKDF2) parolu hesablaması xərc tələb edən açara çevirir. Duz (salt) SSID-nin baytlarıdır (gizli deyil, fərqli SSID-lərdə əvvəlcədən hesablanmış nəticənin işləməsini çətinləşdirir). HMAC-SHA1 çıxışı 20 bayt, PMK 32 bayt olduğundan iki blok hesablanır: U1 = HMAC(P, S || INT32_BE(1)), Uj = HMAC(P, U(j−1)), 4096 U XOR edilib T1 alınır; ikinci blok sonuna 2 yazılaraq hesablanır, T1 və T2 birləşdirilib ilk 32 bayt seçilir. 4096 iterasiya zəif parolu güclü sirrə çevirmir.

Python nümunəsi yalnız şərti laboratoriya parolunu hesablayır ("password" real şəbəkə üçün zəifdir). SSID-də hərf və baytların fərqi PMK-nı dəyişir.

```python
import hashlib
pmk = hashlib.pbkdf2_hmac(
    'sha1', b'password', b'IEEE', 4096, dklen=32
)
print(pmk.hex())
```

Nəticə oxunaqlılıq üçün iki sətirdə göstərilir (proqram bir sətirdə çap edir); 64 onaltılıq simvol 32 baytdır:

```
f42c6fc52df0ebef9ebb4b90b38a5f90
2e83fe1b135a70e23aed762e9710a12e
```

Birbaşa 256 bitlik PSK yazmaq parolun PBKDF2 ilə hesablanmasından fərqli giriş üsuludur; iki format qarışdırılmamalıdır.

PTK hesabında iki MAC ünvanı və iki nonce standartın müəyyən etdiyi ardıcıllıqla yerləşdirilir. Klassik WPA2-CCMP-128 dəstində PTK 48 baytdır: 16 bayt açar təsdiqi açarı (Key Confirmation Key, KCK), 16 bayt açar şifrələmə açarı (Key Encryption Key, KEK), 16 bayt müvəqqəti trafik açarı (Temporal Key, TK). Başqa AKM və şifr dəstlərində uzunluqlar fərqlənə bilər, bölgü bütün WPA3 rejimlərinə tətbiq olunmur.

KCK EAPOL-Key mesajlarının MIC-i, KEK M3-dəki açar məlumatının qorunması, TK unicast məlumat kadrları üçün işlədilir. GTK broadcast və multicast trafikini qoruyur; qrup açarını alan bütün cihazlar eyni sirri bildiyi üçün GTK istifadəçinin kimliyini sübut etmir. PMF üçün qrup idarəetmə açarı IGTK trafik GTK-sından ayrıdır.

| Mesaj | İstiqamət | Əsas sahələr | Qəbuledicinin işi |
| --- | --- | --- | --- |
| M1 | AP-dən cihaza | ANonce, replay counter, açar məlumatı | SNonce yaratmaq, PTK hesablamaq |
| M2 | Cihazdan AP-yə | SNonce, M1 sayğacına uyğun dəyər, MIC, RSN məlumatı | PTK hesablamaq, MIC və seçimləri yoxlamaq |
| M3 | AP-dən cihaza | ANonce, MIC, artmış sayğac, KEK ilə qorunan GTK | MIC və sayğacı yoxlamaq, açarları düzgün quraşdırmaq |
| M4 | Cihazdan AP-yə | M3-ə uyğun sayğac və MIC, təsdiq | Qarşı tərəfin tamamladığını yoxlamaq |

- **M1.** AP təsadüfi ANonce və EAPOL-Key replay counter göndərir. Cihaz bu nöqtədə PTK hesablaya bilir, çünki PMK, iki ünvan və öz SNonce-u artıq əlindədir. M1 adətən MIC daşımır; onun tək görünməsi AP-nin həqiqiliyini sübut etmir. Yeni qoşulmada keyfiyyətli təsadüfi nonce yaradılmalıdır, zəif generator müxtəlif sessiyaların ayrılmasını poza bilər.
- **M2.** Cihaz SNonce-u və KCK ilə hesabladığı MIC-i göndərir. AP eyni PTK-nı qurub MIC-i yoxlayır. Uyğun gəlmirsə yanlış parol, yanlış PMK, pozulmuş kadr və ya uyğunluq problemi araşdırılır. M2 parolun özünü daşımır; buna baxmayaraq WPA2-PSK-da məlum sahələr və MIC parol namizədinin düzgünlüyünü oflayn yoxlamağa kifayət edə bilər.
- **M3.** AP MIC ilə qorunan mesajda ANonce-u təkrarlayır və KEK ilə qorunan açar məlumatını, o cümlədən GTK-nı çatdırır. Cihaz RSN razılaşmasını, nonce-u, replay counter-i və MIC-i yoxlayır. Paket itkisinə görə M3 yenidən gələ bilər. Təhlükəsiz tətbiq həmin mesajı cavablandıra bilər, amma artıq quraşdırılmış açarı yenidən quraşdırıb PN-ni sıfırlamamalıdır. KRACK qüsurunun səbəbi bu vəziyyət keçididir.
- **M4.** Cihaz KCK ilə MIC hesablayaraq M3-ün qəbulunu təsdiqləyir. M4 adi radio ACK kadrı deyil, EAPOL-Key mesajıdır. AP təsdiqi aldıqdan sonra açar vəziyyəti tamamlanır və qorunan məlumat ötürülür. Əl sıxma açarların düzgün tutulmasını yoxlayır; maliyyə serverinə giriş kimi avtorizasiya qərarı ayrıca qalır.

EAPOL-Key replay counter ilə CCMP/GCMP PN eyni sayğac deyil: birincisi açar mübadiləsinin təzəliyini və sorğu-cavab uyğunluğunu, ikincisi qorunan məlumat kadrlarının təkrar qəbul edilməməsini idarə edir. M2 M1-ə, M4 M3-ə uyğun sayğacı qaytarır. Açar dəyişəndə sayğac kontekstinin hansı açara aid olduğu da izlənir.

:::example
Şərti kitabxana noutbuku M3-ü qəbul edir, M4 isə radio itkisinə görə AP-yə çatmır. AP M3-ü təkrar göndərir. Noutbuk yenidən təsdiq verir, məlumat sayğacını əvvəlki vəziyyətdə saxlayır. Təkrar M3-ün görünməsi təkbaşına KRACK sübutu deyil: qüsur eyni açarın yenidən quraşdırılması və nonce vəziyyətinin geri qaytarılmasıdır.
:::

### Oflayn lüğət hücumu

WPA2-Personal-ın əsas zəifliyi budur. Hücumçu əl sıxmasını havadan yazır (lazım olsa cihazı deauth ilə şəbəkədən atıb yenidən qoşulmağa məcbur edir). Sonra öz kompüterində (məsələn, Hashcat ilə) parol namizədlərini sınayır: hər namizəddən PMK, PTK hesablayıb MIC-i tutuşdurur. Şəbəkəyə bir dəfə də qoşulmaq lazım gəlmir, ona görə AP bu cəhdləri görmür və məhdudlaşdıra bilmir. "Universitet2024" kimi parol lüğətdə tez tapılır. 8 simvoldan qısa parol qəbul edilmir, amma 8 simvolun qəbul edilməsi güclü parol demək deyil. Praktiki tövsiyə 20 simvoldan uzun təsadüfi paroldur.

2018-ci ildə hashcat müəllifi Jens Steube PMKID hücumunu göstərdi: bəzi AP-lərin birinci EAPOL-Key mesajına daxil etdiyi PMKID-dən parol namizədini yoxlamaq olur; bunun üçün qoşulan cihaz və tam əl sıxması lazım deyil. Hücum AP-nin PMKID göndərməsindən asılıdır, ona görə hər yerdə işləmir.

Ortaq parolun başqa fəsadı: WPA2-Personal-da parolu bilən və əl sıxmasını yazan istifadəçi başqa cihazın PTK-sını hesablaya bilir, çünki hesaba girən nonce və MAC ünvanları açıq gedir. SAE bu problemi aradan qaldırır.

Parolun uzunluğu niyə vacibdir? Hücumçu GPU ilə saniyədə şərti 1 000 000 namizəd yoxlaya bilsin:

| Parol tipi | Variant sayı | Bütün sahənin yoxlanması |
| --- | --- | --- |
| 8 rəqəm | 10⁸ | 100 saniyə |
| 8 kiçik hərf | 26⁸ ≈ 2,1 × 10¹¹ | Təxminən 58 saat |
| 8 simvol, hərf və rəqəm | 62⁸ ≈ 2,2 × 10¹⁴ | Təxminən 7 il |
| 12 simvol, hərf və rəqəm | 62¹² ≈ 3,2 × 10²¹ | 100 milyon ildən çox |
| 20 təsadüfi simvol | 62²⁰ ≈ 7 × 10³⁵ | Praktiki mümkün deyil |

Cədvəl tam axtarış üçündür. Real hücumda lüğət və qaydalar işlədilir; "Universitet2024" ona görə erkən yoxlanır ki, insanın seçdiyi parol təsadüfi deyil. Bir çox GPU-nu paralel işlətmək müddətləri daha da qısaldır.

### KRACK

2017-ci ildə Mathy Vanhoef KRACK (Key Reinstallation Attack) hücumunu dərc etdi. Hücumçu M3 mesajını təkrar göndərir, cihaz isə eyni açarı yenidən quraşdırır və paket sayğacını sıfırlayır. Nəticədə eyni açar axını təkrarlanır və trafik açıla bilir. KRACK parolu tapmır, protokolun vəziyyət maşınından istifadə edir. Həlli parolu dəyişmək deyil, cihazı yeniləməkdir.

### Personal və Enterprise rejimlərinin fərqi

| Meyar | Personal (PSK/SAE) | Enterprise (802.1X) |
| --- | --- | --- |
| Kimlik | Ortaq parol | Hər istifadəçinin hesabı və ya sertifikatı |
| Autentifikasiya serveri | Yoxdur | RADIUS |
| İstifadəçini ayırmaq | Parolu hamı üçün dəyişmək lazımdır | Bir hesab bloklanır |
| Qeydiyyat | Tək PSK istifadəçinin kimliyini ayırmır | İstifadəçi adı qeydə düşür |
| PMK | Paroldan və ya SAE mübadiləsindən alınır | Autentifikasiyadan alınır, siyasətlə keşlənə bilər |
| Uyğun yer | Ev, kiçik ofis | Universitet, şirkət |

### AES-CCMP və GCMP

AES blok şifridir (128 bitlik bloklar). WPA2-də bloklar Counter (CTR) rejimi ilə şifrələnir: AES hər kadr üçün nonce və sayğacdan açar axını yaradır, axın məlumatla XOR edilir. Tamlıq üçün eyni açarla CBC-MAC hesablanır, kadr dəyişsə kod uyğun gəlmir. GCMP-də CTR Galois sahəsində autentifikasiya ilə birləşir; aparatda paralelləşdirmək asandır, ona görə Wi-Fi 6 və 7-də üstünlük verilir. WEP-dən əsas fərqlər: AES əsaslı autentifikasiyalı şifrələmə, böyük nonce məkanı, təkrar qəbuldan qorunma. Eyni açar altında nonce təkrarlanmamalıdır; KRACK məhz bunu pozduğu üçün ciddi idi.

### AES, CTR və autentifikasiyalı şifrələmə

Qabaqcıl şifrələmə standartı (Advanced Encryption Standard, AES) 128 bitlik bloku gizli açardan asılı çevrilmə ilə başqa 128 bitlik bloka keçirir. AES-128, AES-192, AES-256 açarın uzunluğunu göstərir, blok hamısında 128 bitdir. AES-128-də 10 raund var (baytların əvəzlənməsi, sətirlərin sürüşdürülməsi, sütunların qarışdırılması, raund açarı; son raund fərqlənir). Çevrilmələrin özü kriptoqrafiyanın mövzusudur.

AES təkbaşına dəyişən uzunluqlu kadrın necə şifrələnəcəyini müəyyən etmir; bunu iş rejimi (blokları və autentifikasiya məlumatını əlaqələndirən) həll edir. Eyni AES səhv nonce idarəetməsi ilə təhlükəli ola bilər, ona görə auditdə "AES" yetərli deyil, CCMP/GCMP dəsti və açar istifadəsi də yoxlanır.

Sayğac rejimində (Counter mode, CTR) hər blok üçün fərqli sayğac bloku AES ilə şifrələnərək axın parçası verir: Z_i = AES_K(A_i), C_i = P_i ⊕ Z_i. Açma eyni axınla aparılır, son blok qısadırsa axının uyğun hissəsi işlənir. Paket nömrəsi və blok indeksi girişin təkrarlanmamasına xidmət edir.

CBC-MAC (Cipher Block Chaining Message Authentication Code) məlumatı blok-blok zəncirləyib tamlıq kodu hesablayır: X_i = AES_K(X_(i−1) ⊕ B_i) (sadələşdirilmiş). Uzunluğun kodlanması düzgün qurulmalıdır, ixtiyari CBC-MAC reseptini dəyişən uzunluqlu mesajlara tətbiq etmək təhlükəsizdir demək olmaz. CCMP-nin CCM rejimi uzunluğu, nonce-u, əlavə məlumatı və teqi qaydalı formatlaşdırır.

CCM (Counter with CBC-MAC) həm gizlilik, həm tamlıq verir. Şifrələnməyən, amma dəyişdirilməməli başlıq hissələri əlavə autentifikasiya məlumatı (Additional Authenticated Data, AAD) kimi daxil edilir; ötürmədə dəyişə bilən sahələr maskalanır. Autentifikasiya kodu səhvdirsə mətn yuxarı qata ötürülmür. Bu, WEP-dəki CRC-dən fərqli, açarlı yoxlamadır.

### CCMP və GCMP kadrında hansı sahələr var

CCMP-128-də AES açarı 128 bit, paket nömrəsi (Packet Number, PN) 48 bit, autentifikasiya teqi 8 baytdır. MAC başlığından sonra 8 baytlıq CCMP başlığı gəlir (PN-nin altı baytı bitişik olmayan hissələrlə daşınır), ardınca şifrəli məlumat, teq və FCS. Başlığın görünməsi zəiflik deyil, qəbuledicinin düzgün konteksti seçməsi üçündür.

Başlığın bayt sırası: PN0 PN-nin ən kiçik qiymətli baytıdır; Reserved ehtiyatdır; Key ID/ExtIV açar identifikatoru və genişləndirilmiş IV göstəricisi daşıyır. GCMP başlığı eyni düzülüşdədir. Wireshark-da yığılmış PN ilə naqildəki bayt sırası qarışdırılmamalıdır.

```
PN0  PN1  Reserved  KeyID/ExtIV  PN2  PN3  PN4  PN5
```

CCMP nonce-u 13 baytdır: prioritet baytı, ötürənin 6 baytlıq ünvanı və 6 baytlıq PN. Eyni TK ilə nonce təkrarlanmamalıdır. PN gizli və təsadüfi deyil; tələb fərqli məzmun şifrələnərkən eyni açar altında tam nonce-un təkrarlanmamasıdır. Nonce-a ötürən ünvanı və prioritet də daxildir, ona görə müxtəlif ötürənlərdə eyni PN öz-özünə təkrar deyil; eyni kadrın MAC səviyyəsində retransmissiyası da fərqli məzmunun yenidən şifrələnməsi deyil.

Galois/Counter Mode protokolu (GCMP) AES-CTR-i Galois sahəsində GHASH autentifikasiyası ilə birləşdirir. GCMP-128 və GCMP-256 açar uzunluğuna görə fərqlənir, teq 16 baytdır; başlıq 8 bayt, PN 48 bit, nonce ötürən ünvanı ilə PN-dən qurulan 12 baytdır. Nonce təkrarı həm məxfilik, həm tamlıq üçün ağır nəticə verə bilər.

| Meyar | CCMP-128 | GCMP-128 | GCMP-256 |
| --- | --- | --- | --- |
| AES açarı | 128 bit | 128 bit | 256 bit |
| Başlıq | 8 bayt | 8 bayt | 8 bayt |
| Paket nömrəsi | 48 bit | 48 bit | 48 bit |
| Nonce | 13 bayt | 12 bayt | 12 bayt |
| Autentifikasiya teqi | 8 bayt | 16 bayt | 16 bayt |
| Tamlıq üsulu | CCM daxilində CBC-MAC | GCM daxilində GHASH | GCM daxilində GHASH |

:::figure
src = "m08-4.png"
alt = "Qorunan məlumat kadrı: açıq başlıq, paket nömrəsi və şifrəli yük."
caption = "Qorunan məlumat kadrında açıq başlıq, paket nömrəsi və şifrəli yük."
:::

Qəbuledici PN-ni uyğun açar və kontekstdə saxlanmış vəziyyətlə tutuşdurur; köhnə kadr replay qaydasından keçmirsə atılır, sonra kriptoqrafik yoxlama aparılır. QoS və qəbul sırası səbəbindən bunu tək qlobal sayğac kimi təsvir etmək olmaz. Sequence Control təkrar ötürməni idarə edən MAC sahəsidir, PN-nin əvəzi deyil.

Nümunə: son qəbul olunmuş PN 100-dür; PN 101 ilə gələn, yoxlamadan keçən kadr vəziyyəti irəli aparır; sonradan PN 100 ilə gələn kadr teqi düzgün olsa da köhnədir və replay qaydasından keçməməlidir (bir qəbul konteksti, sadələşdirilmiş).

Radio itkisinə görə yenidən göndərilən kadr dərhal hücum deyil: Retry biti, ardıcıllıq nömrəsi, ACK itkisi və sürücü qaydaları birlikdə oxunur. Əsas qüsur eyni açarın təkrar quraşdırılması ilə PN-nin geri salınması və nonce-un yenidən işlədilməsidir. Səhv teqlər küydən də, saxtalaşdırmadan da yarana bilər.

## WPA3

WPA3 2018-ci ildə elan olundu. Əsas yenilikləri:

- **SAE** (Simultaneous Authentication of Equals, "Dragonfly"): PSK əvəzinə işlənir. Hər parol təxmini üçün AP ilə canlı əlaqə lazımdır, yəni oflayn lüğət hücumu mümkün olmur. Hər sessiyanın açarı ayrıdır, parol sonradan məlum olsa da köhnə trafik açılmır.
- **PMF məcburidir.**
- **WPA3-Enterprise-ın 192 bitlik rejimi** GCMP-256 və güclü kriptoqrafik dəstdən istifadə edir.

WPA3-dən ayrı, amma əlaqəli proqram Wi-Fi Enhanced Open-dur (OWE, RFC 8110). O, parolsuz şəbəkədə hər cihaz üçün ayrı açarla şifrələmə verir. OWE AP-nin həqiqiliyini yoxlamır, yəni saxta AP-yə qarşı qorumur.

WPA3 də qüsursuz deyil. 2019-cu ildə Vanhoef və Ronen Dragonblood adlı hücumları dərc etdilər: yan kanal və endirmə (downgrade) hücumları. Köhnə cihazlar üçün açılmış WPA2/WPA3 keçid rejimi (transition mode) hücumçuya cihazı WPA2-yə endirməyə imkan verir; keçid rejimini ayrı SSID ilə və müvəqqəti saxlamaq lazımdır. Bu hücumlara cavab olaraq Hash-to-Element (H2E) metodu gəlib, 6 GHz-də məcburidir.

### SAE necə işləyir

SAE-də iki tərəf bərabərdir. Elliptik əyri qrupunda ikisi də paroldan əyri üzərində nöqtə çıxarır, **Commit** mesajları ilə təsadüfi açıq dəyərləri, **Confirm** mesajları ilə eyni sirri bildiklərinin sübutunu mübadilə edirlər. Yazılan mübadilədən parolu oflayn yoxlamaq olmur, çünki hər təxmin üzrə ayrıca Commit lazımdır; AP uğursuz cəhdləri görür və məhdudlaşdırır. PMK təzə mübadilənin sirrindən alınır, düzgün tətbiqdə irəli məxfilik verir. SAE yalnız PMK-nı qurur, trafik açarları üçün WPA3-Personal-da da 4 addımlı əl sıxma işləyir.

SAE parol əsasında autentifikasiyalı açar mübadiləsidir (Password-Authenticated Key Exchange, PAKE). Hər iki tərəf eyni paroldan razılaşdırılmış qrupda parol elementi (Password Element, PWE) alır; hər tərəf məxfi təsadüfi ədədlər yaradır, Commit mesajı scalar və element kimi açıq dəyərləri daşıyır (parolun heşi deyil).

Qrup, scalar və element yoxlanır, tərəflər eyni ortaq sirri hesablayır, Confirm açarlı təsdiqlə uyğunluğu yoxlayır. Bundan PMK alınır, sonra 4 addımlı əl sıxma trafik açarlarını qurur. SAE-nin Confirm-i ilə M4 eyni mesaj deyil.

Passiv müşahidəçi Commit və Confirm-i yazmaqla WPA2-PSK-dakı kimi yoxlama meyarı qura bilməməlidir (düzgün qrup yoxlaması, təsadüfi ədədlər və düzgün tətbiq fərziyyəsi ilə). Hücum yükünə qarşı anti-clogging token var, amma o kimlik sənədi deyil. Uzun təsadüfi parol və yeniləmələr SAE-də də tələb olunur.

**H2E** (Hash-to-Element) parolun qrup elementinə standartlaşdırılmış xəritələnməsidir ("parolu bir dəfə heşləmək" deyil). Əvvəlki hunting-and-pecking yanaşmasının məlumatdan asılı davranışı yan kanal problemlərinə yol verirdi. 6 GHz-də SAE üçün H2E tələbi var; aktivliyi, qrup və müştəri sürücüsü birlikdə sınaqdan keçirilməlidir. Dragonblood protokol üstünlüyünün yan kanal, endirmə və tətbiq səhvləri ilə pozula bildiyini göstərdi.

İrəli məxfilik (forward secrecy) keçmiş sessiyaların sonradan parol açıqlansa da qorunmasıdır; sessiyanın gizli təsadüfi dəyərləri saxlanılmamalıdır. Yataqxananın SAE parolu semestr sonunda yayılsa, passiv yazılmış əvvəlki sessiyalar yalnız bu parola görə açılmamalıdır. Ələ keçirilmiş telefonun yaddaşındakı işlək açarlar bu təminatdan kənardadır.

### Keçid rejimi, OWE və PMF

WPA2/WPA3 keçid rejimində eyni SSID PSK və SAE-ni birlikdə elan edə bilər; PSK ilə qoşulan köhnə cihazın əl sıxması WPA2 xüsusiyyətlərini saxlayır. Eyni parol iki yolda işlənirsə, zəif yol güclü yolun sirrini də ifşa edir. "SSID-də WPA3 yazılıb" kifayət deyil, kontroller hər cihazın seçdiyi AKM-i göstərməlidir; uyğunluq istisnası ayrıca SSID ilə müvəqqəti saxlanılır.

OWE-də cihaz və AP assosiasiyaya Diffie–Hellman açıq dəyərlərini daxil edir, ortaq sirrdən PMK alınır, 4 addımlı əl sıxma trafik açarlarını qurur. Parol olmadığı üçün giriş sirri yoxdur; iki ziyarətçinin hərəsinin AP ilə ayrıca cüt açarı olur və passiv qonşu unicast trafiki oxuya bilmir.

OWE-də AP-nin etibarlı qurğu olduğunu təsdiqləyən autentifikasiya yoxdur: aktiv vasitəçi və ya saxta AP riski qalır. Captive portalın HTTPS sertifikatı portalı təsdiqləyə bilər, radio AP-ni yox. Qonaqlar üçün daxili seqment bağlanır, müştəri izolyasiyası açılır, HTTPS saxlanılır. OWE keçid rejimində açıq BSS qalarsa, köhnə cihazın trafiki açıqdır.

:::note Sadə dillə
Kafe və ya qonaq şəbəkəsində çox vaxt parol olmur, brauzerdə qeydiyyat səhifəsi (captive portal) açılır. Portal yalnız qaydaları qəbul etdirir və qeydiyyat aparır, radioda heç nəyi şifrələmir. OWE ("Wi-Fi Enhanced Open") parolsuz şəbəkədə hər cihaz üçün ayrıca açarla şifrələmə verir, amma saxta AP-yə qarşı qorumur.
:::

Qorunan idarəetmə kadrları (PMF) açarlar qurulduqdan sonra deauthentication, disassociation və müəyyən robust action kadrlarının saxtalaşdırılmasını məhdudlaşdırır. Unicast qoruma ilə qrup idarəetmə qoruması fərqlənir; qrup kadrları üçün BIP və IGTK işlədilir. Qrup idarəetmə kadrının autentifikasiya olunması onun məzmununun şifrəli olması demək deyil. PMF-in məqsədi bu kadrların icazəsiz dəyişdirilməsini və təkrarını aşkar etməkdir.

| Rejim | Assosiasiya şərti | Universitet üçün nəticə |
| --- | --- | --- |
| Disabled | PMF razılaşdırılmır | Saxta robust idarəetmə kadrlarına qarşı qoruma yoxdur |
| Capable və ya optional | PMF dəstəkləyən cihazla razılaşa bilər | Köhnə cihazlar qaldıqda bütün bağlantılar qorunmur |
| Required | Cihaz PMF dəstəkləməlidir | Uyğun olmayan cihaz qoşulmur; WPA3 üçün tələbdir |

PMF beacon, probe və ilkin əlaqə mübadiləsinin hamısını qorumur. Radio basdırma, kanalın dolması və AP-nin enerjisinin kəsilməsi də PMF-lə dayanmaz. PMF required əvvəl cihaz inventarı üzərində yoxlanır; uyğun olmayan cihazın qoşula bilməməsi hücum deyil, siyasətin gözlənilən nəticəsidir.

### Wi-Fi 6E, Wi-Fi 7 və çoxbağlantılı iş

Wi-Fi 7-də çoxbağlantılı iş (Multi-Link Operation, MLO) çoxbağlantılı cihazın (Multi-Link Device, MLD) müxtəlif radio bağlantılarını koordinasiya etməsidir; yükü bölməyə və gecikməni azaltmağa kömək edir. Bütün cihazlar bütün diapazonlarda eyni anda ötürmür. MLO iki müstəqil VPN və ya avtomatik ikiqat sürət deyil.

Təhlükəsizlikdə məntiqi MLD kimliyi ilə link ünvanları əlaqələndirilir; açar, nonce/PN konteksti və replay yoxlaması MLO qaydalarına uyğun olmalıdır, bir link ayrılıb qoşulanda digərinin açar sayğacı sıfırlanmamalıdır. Qeydlərdə yalnız bir radio MAC-ına baxmaq eyni noutbuku bir neçə istifadəçi kimi saya bilər.

6 GHz siqnalı zəifləyəndə trafikin 5 GHz-ə keçməsi öz-özünə endirmə hücumu deyil; AKM və siyasətin zəifləyib-zəifləmədiyi yoxlanır, diaqnostika hər linkin kanalını, PN/replay xətalarını və keçid vaxtını ayrıca göstərir. Geniş kanal və çox link sertifikat yoxlaması, firmware yenilənməsi və seqmentasiya tələblərini azaltmır.

### Protokolların təkamülü və müqayisəsi

:::figure
src = "m08-5.png"
alt = "Simsiz şifrələmə standartlarının təkamülü: WEP, WPA, WPA2, WPA3."
caption = "Simsiz şifrələmə standartlarının təkamülü. Qırmızı: istifadə edilməməli; narıncı: düzgün sazlananda uyğunluq üçün qəbul edilir; yaşıl: tövsiyə olunan."
wide = true
:::

| Meyar | WEP | WPA | WPA2 | WPA3 |
| --- | --- | --- | --- | --- |
| İl | 1997 | 2003 | 2004 | 2018 |
| Şifrələmə | RC4 | RC4 + TKIP | AES-CCMP | AES-CCMP, GCMP-256 |
| Tamlıq | CRC-32 | Michael MIC | CBC-MAC | CCMP/GCMP, PMF |
| Personal | Paylaşılan açar | PSK | PSK | SAE |
| Enterprise | Tarixən 802.1X ilə dinamik WEP; təhlükəsiz deyil | 802.1X | 802.1X | 802.1X, istəyə görə 192 bit rejim |
| Əsas zəiflik | IV təkrarı, açar bərpası | RC4 irsi | Oflayn lüğət, PMF məcburi deyil | Keçid rejimində endirmə |
| Status | Qadağan | Qadağan | Qəbul edilir | Tövsiyə olunur |

## Simsiz şəbəkə hücumları

| Hücum | Mahiyyəti | Qorunma |
| --- | --- | --- |
| Evil Twin | Hücumçu eyni SSID-li saxta AP açır | 802.1X və sertifikat yoxlaması, WIPS |
| Rogue AP | İcazəsiz AP şəbəkəyə qoşulur (işçi "rahatlıq üçün" router taxır) | 802.1X port nəzarəti, NAC, simsiz skan |
| Deauthentication | Saxta kadrla cihaz şəbəkədən atılır | PMF |
| Oflayn parol hücumu | Əl sıxması və ya PMKID yazılır, parol sınanır | WPA3-SAE, 802.1X, uzun parol |
| WPS PIN hücumu | 8 rəqəmli PIN praktiki olaraq 11 000 cəhdə enir (Viehböck, 2011) | WPS-i söndürmək |
| Karma, probe hücumu | Cihazın axtardığı şəbəkəyə AP "mən oyam" deyir | Köhnə SSID-ləri silmək, avtomatik qoşulmanı söndürmək |
| MAC saxtalaşdırması | Captive portaldan keçmiş cihazın MAC-ı təqlid olunur | Portal əvəzinə 802.1X |
| Radio basdırma (jamming) | Radio mühiti küylə doldurulur | Kriptoqrafik həlli yoxdur, fiziki aşkarlama |

:::exam
MAC süzgəci və SSID-nin gizlədilməsi təhlükəsizlik tədbiri sayılmamalıdır: MAC ünvanı və SSID havada açıq görünür. Captive portal yalnız qeydiyyatdır, radioda heç nəyi şifrələmir.
:::

### Hücum əlamətini nasazlıqdan ayırmaq

Simsiz müdaxilənin aşkarlanması sistemi (Wireless Intrusion Detection System, WIDS) radio mühitini izləyir; WIPS avtomatik tədbirlər də görə bilər, amma yanlış qərar qanuni bağlantını kəsə bilər. Naməlum BSSID onun kabel şəbəkəsinə qoşulduğunu sübut etmir: qonşu AP, telefon hotspot-u və icazəsiz daxili AP fərqləndirilir; kommutator portu, AP inventarı və radio müşahidəsi birlikdə yoxlanır.

WPS PIN zəifliyində 8 rəqəmin sonuncusu yoxlama rəqəmidir; hissələrin ayrıca yoxlanması axtarışı təxminən 10⁴ + 10³ = 11 000 cəhdə endirir. Bu rəqəm səbəbi göstərir, hər qurğuda müddəti yox (kilidləmə fərqlənir). WPS söndürülür; MAC siyahısı əlavə uçot ola bilər, güclü autentifikasiya əvəzi deyil.

Müdafiə məqsədli Wireshark ekran süzgəcləri:

| Süzgəc | Nəyi göstərir |
| --- | --- |
| wlan.fc.type == 0 | İdarəetmə kadrları |
| wlan.fc.type_subtype == 0x08 | Beacon kadrları və elan edilən imkanlar |
| wlan.fc.type_subtype == 0x0c | Deauthentication kadrları |
| wlan.fc.type_subtype == 0x0a | Disassociation kadrları |
| eapol | EAP over LAN, o cümlədən EAPOL-Key mübadiləsi |
| wlan.fc.retry == 1 | Təkrar ötürmə kimi işarələnmiş kadrlar |
| wlan.fc.protected == 1 | Protected biti qoyulmuş kadrlar |
| wlan.bssid == 02:00:00:00:08:01 | Şərti BSSID ilə əlaqəli görünən kadrlar |

Süzgəclər icazəli qaydada toplanmış yazının təhlili üçündür. Adi Ethernet capture-da 802.11 idarəetmə kadrları görünməyə bilər: radio adapteri, monitor rejimi və düzgün kanal lazımdır; bir sensor bütün kanalları görmür. Protected biti yalnız başlıq əlamətidir, MIC-in düzgünlüyünü sübut etmir.

Şərti imtahan hadisəsində əvvəl vaxt, auditoriya, BSSID və təsirlənən cihazlar müəyyən edilir; sonra deauthentication sayı, reason code, Retry artımı, kanal doluluğu və DFS hadisəsi tutuşdurulur. Çox cihaz düşürsə AP enerjisi və uplink, tək noutbukda sürücü və sertifikat vaxtı yoxlanır. Reason code iddiadır, saxta kadrda etibarlı diaqnoz deyil.

Normallaşdırılmış nümunə qeydlər (real log sintaksisi deyil): SAE ilə qoşulma, uyğun olmayan PMF istəyinin rəddi, araşdırılmalı replay hadisəsi.

```
2026-10-20T08:00:01Z ap=aud08 event=join akm=SAE pmf=yes
2026-10-20T08:02:10Z ap=aud08 event=reject cause=pmf_required
2026-10-20T08:05:40Z ap=aud08 event=replay_drop key=pairwise
```

SIEM qaydası bir MAC-a kor-koranə bağlanmır, çünki cihazlar təsadüfiləşdirilmiş MAC işlədə bilər; kontroller sessiyası, fərdi autentifikasiya nəticəsi və DHCP uyğunluğu əlaqələndirilir. Şərti on dəqiqədə çoxlu naməlum BSSID və şikayət prioritet araşdırma yarada bilər, hədd normal mənzərəyə görə seçilir. Tam trafik yazıları şəxsi məlumat daşıya bilər; giriş və saxlama məhdudlaşdırılır. Hücumu təqlid edən addımlar istehsalat şəbəkəsində aparılmır.

### Niyə zəif WPA2 parolu təhlükəlidir

:::note Sadə dillə
Hücumçu əl sıxmasını yazır (lazım gəlsə cihazı deauth ilə atıb yenidən qoşulmağa məcbur edir), sonra öz kompüterində milyonlarla parolu sınayıb MIC-i yoxlayır. Bunun üçün şəbəkəyə bir dəfə də qoşulmaq lazım deyil. WPA3-ün SAE mexanizmi buna imkan vermir: hər təxmin üçün AP ilə canlı əlaqə lazımdır.
:::

## Digər simsiz texnologiyalar

| Texnologiya | Məsafə, istifadə | Əsas risklər |
| --- | --- | --- |
| Bluetooth, BLE | Məsafə qurğudan asılıdır; 10 m tipik qısa məsafə nümunəsidir, qulaqlıq, IoT | Bluejacking, bluesnarfing, köhnə versiyalarda zəif cütləşmə |
| NFC | Bir neçə sm, ödəniş | Yaxın məsafədə dinləmə və relay hücumu |
| RFID | Sm-dən metrlərə, tələbə kartları, kitabxana | Köhnə kartların (MIFARE Classic) klonlanması |
| Mobil (4G/5G) | Km, telefon, modem | Saxta baza stansiyası (IMSI catcher), SIM-swap |

Bluejacking istənməyən mesaj göndərməkdir, bluesnarfing məlumat oğurluğudur. "Görünən" (aşkarlanma) rejimini söndürmək lazımdır.

Korporativ cihazlarda şəbəkə profili mərkəzdən yayılır (GPO, MDM), RADIUS sertifikatının adı profilə yazılır. Profil düzgün qurulmayanda istifadəçi saxta autentifikasiya serverinin sertifikatını qəbul edə bilər. EAP-TTLS/PAP istifadə edilirsə hücumçu parolu əldə edə, PEAP-MSCHAPv2 istifadə edilirsə parolun oflayn yoxlanmasına yarayan cavabı yığa bilər. EAP-TLS-də isə parol göndərilmir və müştərinin şəxsi açarı qarşı tərəfə ötürülmür. 9-cu mövzudakı EAP metodlarının təhlükəsizliyi bu yoxlamadan asılıdır.

### Bluetooth və BLE-də cütləşmə

Bluetooth qulaqlıq, klaviatura və yaxın cihazlarda, Bluetooth Low Energy (BLE) azenerjili sensorlarda işlənir. Məsafə gücdən və antenadan asılıdır, 10 metr sərt sərhəd deyil. Aşkarlanma rejiminin bağlanması görünməni azaldır, mövcud bağlantı və proqram zəifliklərini aradan qaldırmır.

Cütləşmə (pairing) açar razılaşdırmasını, bonding həmin açarların saxlanmasını ifadə edir. Rəqəm müqayisəsi və ya doğrulanmış ayrıca kanal tərəflərin uyğunluğunu yoxlayır; Just Works rahatdır, amma vasitəçiyə qarşı təsdiq imkanı məhduddur. İtmiş cihazın saxlanmış bağlantısı silinir, istifadə olunmayan Bluetooth söndürülür, firmware yenilənir.

### NFC, RFID və mobil rabitənin sərhədləri

Yaxın sahə rabitəsi (Near Field Communication, NFC) çox qısa məsafədə işləyir, amma bu relay hücumunu dayandırmır: aradakı qurğular mübadiləni uzağa daşıya bilər. Kartın oxuyucuya yaxın görünməsi sahibinin qapıda olduğunu həmişə sübut etmir; həssas girişdə vaxt, kontekst yoxlamaları və əlavə təsdiq seçilir.

Radiotezlik identifikasiyası (Radio Frequency Identification, RFID) passiv kitab etiketi ilə kriptoqrafik giriş kartını eyni ailədə birləşdirir. Yalnız açıq UID-yə əsaslanan avtorizasiya kopyalanmaya həssasdır. MIFARE Classic-in zəiflikləri bütün RFID-in sındırıldığı demək deyil: etiket inventar üçün, giriş kartı qarşılıqlı kriptoqrafik yoxlama üçün qiymətləndirilir. Kart itəndə giriş ləğv olunur.

Mobil 4G/5G operator infrastrukturuna bağlıdır. Saxta baza stansiyası (radio və şəbəkə kimliyi) ilə SIM-swap (nömrənin başqa SIM-ə keçirilməsi) eyni hadisə deyil; telefon nömrəsinə gələn kodun zəbti universitet hesabını riskə atır. Mobil modem zəif AP-ni düzəltmir və noutbukdakı zərərli proqramı dayandırmır.

## Kampus şəbəkəsi üçün tövsiyələr

- Əməkdaşlar və tələbələr: WPA2/WPA3-Enterprise, fərdi hesab, sertifikat yoxlaması məcburi.
- Qonaqlar: ayrı VLAN, OWE və ya WPA3-SAE, müştəri izolyasiyası (client isolation), daxili şəbəkəyə giriş yoxdur.
- IoT və köhnə avadanlıq: ayrı SSID və VLAN, ciddi firewall qaydaları.
- WEP, WPA və TKIP tamamilə söndürülür, WPS bağlanır.
- PMF ən azı "capable" rejimində, WPA3 üçün "required" rejimində.
- WIPS və ya mütəmadi radio skanı ilə icazəsiz AP-lər aşkarlanır.
- AP-nin firmware-i vaxtında yenilənir, idarəetmə interfeysi ayrı şəbəkədədir.

### Radio girişindən xidmətə qədər siyasət

Ünvanlar, VLAN nömrələri və cihaz adları şərtidir. SSID ilə VLAN arasında uyğunluq qurulur, aradakı trafik firewall ilə yoxlanır. Müxtəlif SSID-lər eyni daxili şəbəkəyə məhdudiyyətsiz bağlanırsa, istifadəçi siyahısının ayrılması real seqmentasiya vermir. Məxfi tələbə bazası birbaşa istifadəçi VLAN-ında saxlanılmır; ona yalnız icazəli tətbiq xidmətləri çatır.

| Qrup | Seqment | Radio qoruması | İcazəli xidmət |
| --- | --- | --- | --- |
| Əməkdaş | VLAN 20, 10.20.0.0/24 | Enterprise, PMF siyasəti | LMS, kitabxana, rola uyğun daxili tətbiqlər |
| Tələbə | VLAN 30, 10.30.0.0/24 | Fərdi Enterprise girişi | Tədris resursları, İnternet |
| Qonaq | VLAN 40, 10.40.0.0/24 | OWE, müştəri izolyasiyası | Yalnız İnternet, daxili ünvanlar bağlı |
| IoT | VLAN 50, 10.50.0.0/24 | Uyğun güclü dəst və ayrıca siyasət | Yalnız öz idarəetmə xidməti |
| AP idarəetməsi | VLAN 60, 10.60.0.0/24 | Ayrı idarəetmə bağlantısı | Yalnız səlahiyyətli administrator və log serveri |

:::figure
src = "m08-6.png"
alt = "Radio girişi (əməkdaş və tələbə, qonaq, IoT) VLAN 20/30, 40, 50-yə, oradan firewall-a, sonra tədris xidmətlərinə, İnternetə və idarəetmə xidmətinə yönəlir; AP idarəetməsi ayrı seqmentdədir."
caption = "Universitetdə radio bağlantısı, seqmentasiya və xidmətlərə nəzarət (ünvan və VLAN seçimi şərtidir)."
wide = true
:::

Müştəri izolyasiyası qonşu qonaqlara birbaşa yolu bağlaya bilər; fərqli AP-lər, kabel cihazları və IPv6 yolları ayrıca yoxlanır (qayda yalnız IPv4 üçündürsə IPv6 açıq qala bilər). DNS və DHCP təsdiqli olmalı, saxta ünvan paylaması məhdudlaşdırılmalıdır. LMS-də giriş ayrıca hesab, səlahiyyət və sessiya qaydaları ilə qorunur.

### Konfiqurasiya və dəyişikliklərin yoxlanması

hostapd parçası şərti laboratoriya üçün WPA3-Personal-only nümunəsidir, real kampusun fərdi Enterprise girişini əvəz etmir. İnterfeys, ölkə kodu və kanal radio planına uyğun seçilməlidir. Parol yalnız nümunədir; real sirr açıq dərs faylından götürülmür. wpa=2 RSN ailəsini seçir, təkbaşına WPA3 demək deyil; SAE və PMF sətirləri birlikdə oxunur.

```
interface=wlan0
ssid=UNI-Lab-SAE
wpa=2
wpa_key_mgmt=SAE
rsn_pairwise=CCMP
ieee80211w=2
sae_pwe=1
wpa_passphrase=Yalniz-Laboratoriya-Numunesi-2026
wps_state=0
```

ieee80211w=2 PMF tələb edir, sae_pwe=1 H2E-ni seçir; sürücü və proqram bunları dəstəkləməlidir. Parametr səhvinə görə proqram başlamırsa, təhlükəsizliyi səssiz zəiflətmək əvəzinə səbəb araşdırılır. Enterprise profilləri GPO və ya mobil cihaz idarəetməsi (Mobile Device Management, MDM) ilə yayılır; profilə etibarlı sertifikat mənbəyi və gözlənilən radius.uni.example adı yazılır.

Dəyişiklik əvvəl laboratoriyada, sonra məhdud auditoriyada yoxlanır: uğurlu qoşulma ilə yanaşı yanlış parolun rəddi, PMF tələbini ödəməyən cihazın rəddi, qonaqdan tələbə bazasına yolun bağlılığı və rouminq davranışı ölçülür. Konfiqurasiyanın ehtiyat nüsxəsi və geri qaytarma üsulu saxlanılır, standart administrator parolu dəyişdirilir, idarəetmə İnternetə açılmır.

**İtmiş noutbuk.** Əməkdaş cihazı itirəndə sertifikat və ya hesab girişi ləğv edilir, aktiv sessiyalar siyasətə uyğun kəsilir, PMK keşləri nəzərə alınır. Digər əməkdaşların sirrini dəyişmək tələb olunmaya bilər. Ortaq PSK işlənibsə həmin sirrin itmiş cihazda saxlandığı fərz edilir və paylaşan qrup üçün dəyişiklik planlanır. İnsident cavabı ilə dərsin davam etməsi üçün alternativ qanuni giriş yolu əvvəlcədən hazırlanır.

## Yadda saxla

:::tip Yadda saxla
- WEP-in problemi parolda deyil, protokoldadır (qısa IV, RC4 birləşməsi, CRC-32).
- WPA2-Personal-ın əsas zəifliyi oflayn lüğət hücumudur; WPA3-SAE-də hər təxmin canlı əlaqə tələb edir.
- KRACK parolu tapmır, M3-ün təkrarı ilə açarın yenidən quraşdırılmasından istifadə edir; həll cihazı yeniləməkdir.
- PMF deauth saxtalaşdırmasını dayandırır, jamming-i və saxta AP-ni yox.
- Captive portal şifrələmə vermir; OWE verir, amma AP-nin həqiqiliyini yoxlamır.
:::

## Situasiya tapşırıqları

**Situasiya 1.** Universitet kitabxanasının köhnə routeri hələ də WEP ilə işləyir, çünki bir neçə köhnə kataloq terminalı WPA2-ni dəstəkləmir. İT işçisi deyir: "Parol 26 simvoldur, sındırmaq olmaz." Doğrudurmu?

**Cavab.** Doğru deyil. WEP-in zəifliyi parolda deyil, protokoldadır: IV tez təkrarlanır, kifayət qədər trafik yığılanda açar uzunluğundan asılı olmayaraq bərpa olunur (konspekt: aircrack-ng). Həll: WPA2-AES və ya WPA3-ə keçmək, terminalları kabelə qoşmaq və ya dəyişdirmək. Onları ayrı, İnternetsiz seqmentdə saxlamaq yalnız yayılma riskini azaldır, radio trafikinin məxfiliyini qorumur.

**Situasiya 2.** Korpusda "UNI-Staff" WPA2-Personal ilə işləyir, bütün əməkdaşların parolu "Universitet2024"-dür. Yataqxanadan bir tələbə əl sıxmasını yazıb parolu tapır. Bu necə mümkün oldu və nə dəyişdirilməlidir?

**Cavab.** WPA2-PSK-da yazılmış əl sıxması ilə parol namizədləri oflayn yoxlanır, proqnozlaşdırılan parol lüğətdə tez tapılır. Ortaq parol olduğu üçün kimin qoşulduğunu bilmək və bir nəfəri ayırmaq da mümkün deyil. Şəbəkə WPA2/WPA3-Enterprise-a keçirilməli, fərdi hesab və sertifikat işlədilməli, PMF açılmalıdır. Parol dəyişdirilməlidir, çünki artıq məlumdur. Mümkün deyilsə, ən azı WPA3-SAE və uzun təsadüfi parol (konspekt).

**Situasiya 3.** Qonaq Wi-Fi-ı parolsuz, captive portal ilə işləyir. Rəhbərlik deyir: "Portalda telefon nömrəsi ilə qeydiyyat var, deməli trafik qorunur." Konfransda bir iştirakçı başqalarının şifrəsiz HTTP trafikini görür. Niyə?

**Cavab.** Captive portal qeydiyyat mexanizmidir, radio səviyyəsində şifrələmə vermir. Açıq şəbəkədə hər kəs havadakı şifrəsiz trafiki görə bilir. Həll: OWE və ya WPA3-SAE, müştəri izolyasiyası, qonaq şəbəkəsinin daxili şəbəkədən tam ayrılması. HTTPS və VPN tövsiyəsi əlavə qatdır (konspekt).

**Situasiya 4.** Əməkdaşlar imtahan günü Wi-Fi-dan tez-tez düşür, loglarda çoxlu deauthentication kadrı var. WPA2 işləyir, PMF sönülüdür. Hansı hücum ola bilər və nə etmək lazımdır?

**Cavab.** Bu əlamətlər saxta deauthentication hücumuna uyğun gəlir, lakin səbəb trafik və kontroller qeydləri ilə təsdiqlənməlidir. Məqsəd xidməti pozmaq, cihazları yenidən qoşulmağa məcbur edib əl sıxmasını yazmaq, yaxud saxta AP-yə çəkməkdir. PMF açılmalı, mümkünsə WPA3-ə keçilməli, WIPS ilə mənbə aşkar edilməlidir. Jamming olsa PMF kömək etməyəcək, fiziki aşkarlama lazım gələcək.

**Situasiya 5.** Universitetin şərti 180 nəfərlik auditoriyasında üç AP eyni 80 MHz kanalda işləyir. Siqnal güclüdür, LMS testi zamanı cavablar gecikir. Dördüncü AP əlavə etmək təklif edilir. Nə yoxlanmalıdır?

**Cavab.** Kanal doluluğu, təkrar ötürmələr və gizli düyün ehtimalı ölçülür. Eyni kanaldakı AP-lər radio vaxtını paylaşır. Daha dar, qonşuluqda ayrılmış kanallar, güc və yerləşdirmə planı yoxlanır. Müştəri imkanları, uplink və LMS serverinin yükü də qiymətləndirilir; AP artırmaq ölçməsiz həll deyil.

**Situasiya 6.** Kitabxanada WPA3 aktivdir, amma bəzi noutbuklar PSK ilə qoşulur. Eyni parol bütün cihazlarda saxlanır. Administrator H2E-nin bütün parol hücumlarını dayandırdığını deyir. Qiymətləndirin.

**Cavab.** Keçid rejimində PSK bağlantısı WPA2 xüsusiyyətlərini saxlayır. H2E SAE elementinin alınmasına aiddir, PSK mübadiləsini dəyişmir. Kontrollerdə hər cihazın AKM-i yoxlanır, uyğun cihazlar SAE-only siyasətinə keçirilir. Köhnə cihazlara məhdud və çıxarılma tarixi olan ayrı giriş verilir.
