+++
title = "Simsiz autentifikasiya və simsiz rabitənin təhlükəsizliyi"
unit = "uzun"
order = 9
summary = "Tam mühazirə: simsiz sərhəd, Personal və Enterprise, 802.1X və EAP üsulları, sertifikat yoxlaması, RADIUS və Blast-RADIUS, RadSec, eduroam, simsiz hücumlar, WIDS/WIPS, Bluetooth, mobil rabitə, BYOD/MDM və kampus layihəsi."
updated = 2026-11-09

[[source]]
title = "Mühazirə 9: Simsiz autentifikasiya və simsiz rabitənin təhlükəsizliyi"
note = "Elmar Cabbarov, 2026–2027"
+++

Bu mövzu universitetin simsiz şəbəkəsində kimlik yoxlamasını layihələndirməyi və onun səhvlərini araşdırmağı öyrədir. Mövzunun sonunda 802.1X mübadiləsinin hər addımını tərəflər üzrə izah etməli, EAP üsulunu cihaz imkanlarına və riskə görə seçməli, server sertifikatının yoxlanmasını əsaslandırmalı və RADIUS ilə verilən hüquqları firewall siyasəti ilə əlaqələndirməlisən. Saxta və icazəsiz giriş nöqtəsini fərqləndirməli, eduroam-da etimad sərhədlərini göstərməli və kampus üçün ölçülə bilən qəbul meyarları hazırlamalısan. Mühazirədəki universitet topologiyası, ünvanlar və VLAN nömrələri şərti tədris nümunəsidir.

:::exam
Konspektə görə bu mövzudan sonra bacarmalısan: Personal (PSK/SAE) və Enterprise (802.1X) rejimlərini müqayisə etməyi; 802.1X-in üç rolunu və EAP üsullarını izah etməyi; evil twin, rogue AP, deauth kimi hücumları tanıyıb hər birinə uyğun tədbiri seçməyi.
:::

## Simsiz rabitədə təhlükəsizlik sərhədi

### Radioəlaqə niyə ayrıca yanaşma tələb edir

Simsiz rabitə məlumatın kabel olmadan elektromaqnit dalğaları ilə ötürülməsidir. Simsiz lokal şəbəkədə (wireless local area network, WLAN) cihazlar adətən giriş nöqtəsinə (access point, AP) qoşulur. Wi-Fi kampus daxilində bu rabitəni qurur, Bluetooth qısa məsafəli cihaz əlaqələrində işləyir, mobil rabitə isə operatorun əhatə şəbəkəsindən istifadə edir. Bu sistemlərin kimlik yoxlaması eyni deyil: telefonun SIM kartı ilə operatora tanınması universitetin tələbə bazasına giriş hüququ vermir.

Kabel şəbəkəsində hücumçu çox vaxt əvvəlcə rozetkaya və ya aralıq cihaza çatmalıdır. Radio siqnalı isə divardan və pəncərədən kənara çıxa bilər: kitabxananın qarşısında dayanan şəxs binaya girmədən Wi-Fi kadrlarını qəbul edə bilər. Fiziki mühafizə yenə lazımdır, amma radio sərhədi bina sərhədi ilə üst-üstə düşmür. 

- **SSID** (service set identifier) şəbəkə adıdır və istifadəçinin seçim etməsinə kömək edir.
- **BSSID** (basic service set identifier) konkret radio xidmət dəstini tanıdan identifikatordur, adətən MAC ünvanı formasındadır.
- Bir SSID kampusun çoxlu AP-sində yayıla bilər; eyni fiziki AP bir neçə SSID və BSSID təqdim edə bilər.
- Nə SSID, nə də ayrıca BSSID universitetə məxsusluğu kriptoqrafik şəkildə sübut edir.

:::example
Tələbə kitabxanada UNI-Student adını görür. Hücumçu da həmin adı yayımlaya bilər. Universitetə oxşayan adın görünməsi kifayət deyil. Enterprise profilində gözlənilən autentifikasiya serverinin sertifikatı yoxlanarsa, cihaz saxta serverlə kimlik mübadiləsini dayandıra bilər.
:::

### Qorunan məlumat və qərarlar

Məxfilik məlumatın icazəsiz oxunmamasını, bütövlük dəyişikliklərin aşkarlanmasını, əlçatanlıq xidmətin tələb olunan vaxtda işləməsini ifadə edir. Simsiz şəbəkədə bunlara qarşılıqlı autentifikasiya, düzgün avtorizasiya və hadisələrin izlənə bilməsi əlavə olunur. Radio səviyyəsində şifrələnən paket AP-dən sonra başqa şəbəkələrdən keçə bilər. Buna görə lms.uni.example ilə HTTPS bağlantısı Wi-Fi şifrələməsi olan kampusda da saxlanılır.

| Tələb | Nə qorunur | Yoxlama nümunəsi |
| --- | --- | --- |
| Məxfilik | LMS məlumatı və kimlik mübadiləsi | Radio qoruması və tətbiqin HTTPS bağlantısı yoxlanır |
| Bütövlük | Paket və giriş qərarı | Dəyişdirilmiş mübadilənin qəbul edilmədiyi sınanır |
| Əlçatanlıq | Dərsdə əlaqənin davam etməsi | AP və RADIUS sıradan çıxma sınağı aparılır |
| Autentifikasiya | İstifadəçi və server kimliyi | Yanlış server sertifikatı rədd edilir |
| Avtorizasiya | Resursa çıxış həddi | Tələbə seqmentindən maliyyə xidmətinə yol bağlanır |
| İzlənə bilmə | Sessiyanın hesab və cihazla əlaqəsi | RADIUS, DHCP və kontroller qeydləri tutuşdurulur |

Autentifikasiya kimliyin yoxlanmasıdır; avtorizasiya həmin kimliyə verilən hüququ müəyyən edir. İstifadə uçotu (accounting) sessiyanın başlanması, bitməsi və müəyyən istifadə göstəricilərinin qeydə alınmasıdır. Bu üç vəzifə **AAA** adlanır. Uğurlu Wi-Fi autentifikasiyası tələbə bazasının administratoru olmaq demək deyil: bazaya girişdə tətbiq ayrıca hesabı və səlahiyyəti yoxlamalıdır.

Cihaz kimliyi ilə insan kimliyi də ayrılır. Əks halda cihazın adına baxıb əməliyyatı konkret əməkdaşa aid etmək yanlış nəticə verər.

## Giriş rejiminin seçilməsi

### Ortaq sirr və fərdi kimlik

Personal rejimində istifadəçilər adətən ortaq parolu bilir. WPA2-Personal-da əvvəlcədən paylaşılmış açar (pre-shared key, PSK) yanaşması işləyir; WPA3-Personal SAE mübadiləsindən istifadə edir. Açarların hesablanması, WEP-dən WPA3-ə keçid və kriptoqrafik hücumların detalları 8-ci mövzudadır. Burada seçimə idarəetmə baxımından baxılır: kimin girişini ayrıca dayandırmaq, hansı cihazın qoşulduğunu müəyyən etmək və hüquqları necə bölmək mümkündür?

Kafedrada bir parolu bütün tələbələrə vermək asandır, amma semestr bitəndə parolu kimlərin saxladığı bilinmir. Parol dəyişəndə printerdən əməkdaş telefonuna qədər bütün cihazlara müdaxilə lazım gəlir. Adi vahid PSK şəbəkəsində MAC bloklaması bir istifadəçinin sirrini etibarlı şəkildə ləğv etmir.

Enterprise rejimində hər şəxsə və ya cihaza ayrıca kimlik məlumatı verilir: hesab və parol, yaxud sertifikat və şəxsi açar. Cihaz itəndə yalnız onun kimlik məlumatı ləğv edilir, digər cihazlar işləməyə davam edir. Əvəzində universitet autentifikasiya serverlərini, sertifikat infrastrukturunu (PKI) və istifadəçi dəstəyini işlək saxlamalıdır.

| Meyar | Adi ortaq parollu Personal | Fərdi kimlikli Enterprise |
| --- | --- | --- |
| Giriş məlumatı | Qrupun bildiyi sirr | Hesab və ya cihaz sertifikatı |
| Bir cihazı çıxarmaq | Ortaq sirr yayıldıqda ümumi dəyişiklik | Həmin kimlik və aktiv sessiya ləğv edilir |
| Hüquqların verilməsi | Adətən SSID üzrə ümumi qayda | Kimlik və qrup üzrə rol təyin oluna bilər |
| İzləmə | Hesab kimliyi birbaşa bilinmir | Kimlik sessiya ilə əlaqələndirilə bilər |
| İstismar yükü | İlkin quruluş sadədir | AAA, profil və kimlik həyat dövrü tələb edir |
| Universitet nümunəsi | Məhdud imkanlı laboratoriya cihazı | Əməkdaş noutbukları və tələbə cihazları |

:::note Konspektdən əlavə
Konspektin cədvəlində: Personal-da hamı üçün eyni PMK (WPA2), Enterprise-da hər istifadəçiyə ayrıca PMK; Personal ev, kiçik ofis və IoT seqmenti üçün, Enterprise universitet, şirkət və xəstəxana üçündür. Personal-da kimin qoşulduğu bilinmir, Enterprise-da hər qoşulma konkret şəxsə bağlıdır. Bir nəfəri çıxarmaq Personal-da parolu hamı üçün dəyişmək, Enterprise-da hesabı bloklamaq və ya sertifikatı ləğv etməkdir.
:::

:::tip Yadda saxla
Personal və Enterprise arasındakı əsas fərq: bir cihazı ayırmaq. PSK-da bu mümkün deyil (parol hamı üçün dəyişir), EAP-TLS-də yalnız həmin cihazın sertifikatı ləğv edilir.
:::

### WPA2/WPA3-Enterprise sərhədləri

WPA2-Enterprise IEEE 802.1X və uyğun EAP üsulu ilə şəbəkəyə girişi yoxlayır. Məlumat kadrlarının qorunması üçün təhlükəsiz konfiqurasiyada AES əsaslı CCMP işlədilir: AES alqoritmdir, CCMP isə ondan istifadə edən qoruma mexanizmidir. WEP və TKIP kampusun qəbul edilən rejimlərinə daxil edilmir. 

WPA3-Enterprise də 802.1X/EAP əsasında işləyir və qorunan idarəetmə kadrları (protected management frames, PMF) onun tələblərindədir. Ayrı 192 bit təhlükəsizlik rejimi var və kriptoqrafik profili daha sərtdir. WPA3 yazısı bütün qoşulmaların avtomatik həmin rejimdə işlədiyini göstərmir: universitet avadanlığın, əməliyyat sisteminin və EAP/TLS konfiqurasiyasının birlikdə uyğunluğunu yoxlayır.

| Rejim | Nə verir | Əməli məhdudiyyət |
| --- | --- | --- |
| WPA2-Enterprise | Fərdi EAP autentifikasiyası | Səhv sertifikat yoxlaması riski saxlanır |
| WPA3-Enterprise | Enterprise girişi və PMF tələbi | Müştəri uyğunluğu yoxlanmalıdır |
| 192 bit Enterprise rejimi | Müəyyən gücləndirilmiş kriptoqrafik profil | Bütün avadanlıq və üsullar uyğun deyil |
| OWE | Parolsuz radio şifrələməsi | AP sahibini autentifikasiya etmir |
| Ənənəvi açıq şəbəkə | Sərbəst radio qoşulması | Wi-Fi səviyyəsində məxfilik yoxdur |

Açıq şəbəkədə fürsətçi şifrələmə (opportunistic wireless encryption, OWE) passiv dinləməyə qarşı radio kanalını qoruyur. Qonaq həmin kanalla saxta AP-yə də qoşula bilər. Qonaq şəbəkəsi üçün OWE seçiləndə tətbiqin HTTPS sertifikatına nəzarət və daxili resurslardan izolyasiya saxlanılır. 

## IEEE 802.1X: rollar və mesaj axını

### Üç tərəfin məsuliyyəti

IEEE 802.1X port əsaslı şəbəkəyə giriş nəzarətini müəyyən edir. Simsiz şəbəkədə məntiqi idarə olunan port cihazın adi məlumat trafikinə açılan keçididir. Autentifikasiyaya qədər port yalnız EAP trafikini buraxır.

- **Qoşulmaq istəyən tərəf (supplicant)**: noutbukdakı və ya telefondakı 802.1X müştərisi.
- **Autentifikator (authenticator)**: AP və ya WLAN kontrollerindəki (konspektə görə kommutatordakı) girişə nəzarət funksiyası.
- **Autentifikasiya serveri**: EAP üsulunu tamamlayır, siyasət əsasında nəticəni qaytarır; praktikada çox vaxt RADIUS serverindədir (FreeRADIUS, NPS + AD/LDAP).

AP həmişə bütün EAP üsullarının daxili yoxlamasını aparmır; EAP mesajlarını müştəridən serverə və əks istiqamətə daşıya bilər. Lakin AP və kontroller passiv kabel də deyil: nəticəni sessiyaya tətbiq edir, açarları idarə edir, VLAN və rol məhdudiyyətlərini yerinə yetirir. 

:::warning
AP özü qərar vermir, yalnız ötürür və tətbiq edir; qərarı RADIUS serveri verir.
:::

| Rol | Universitetdə qarşılığı | Nəyi bilməli və yoxlamalıdır |
| --- | --- | --- |
| Supplicant | Tələbənin telefonu | Serverin etibar zənciri və gözlənilən adı |
| Autentifikator | AP və ya kontroller | Etibarlı RADIUS ünvanı, qorunan əlaqə və giriş siyasəti |
| Autentifikasiya serveri | FreeRADIUS və ya başqa AAA xidməti | İcazəli şəbəkə cihazları və istifadəçi kimliyi |
| Kimlik mənbəyi | Hesab kataloqu və ya PKI | Aktivlik, qrup və sertifikatın statusu |

Müştəri ilə autentifikator arasında EAP over LAN (EAPOL) işləyir; bu mübadilə üçün tələbənin əvvəlcədən IP ünvanı alması lazım deyil. Autentifikatorla RADIUS arasında EAP mesajları RADIUS atributlarında daşınır. Beləliklə, eyni məntiqi EAP söhbəti iki fərqli nəqliyyat hissəsindən keçir. AP-nin RADIUS üçün istifadə etdiyi IP ünvanı ilə tələbənin sonradan DHCP-dən alacağı ünvan fərqlidir.

:::figure
src = "m09-1.png"
alt = "Ardıcıllıq diaqramı: cihaz, AP (authenticator) və RADIUS arasında EAPOL-Start, EAP Request/Response Identity, RADIUS Access-Request, EAP-TLS və ya PEAP mübadiləsi, Access-Accept ilə açar materialı, EAP-Success, 4 addımlı əl sıxma (PTK, GTK) və adi şifrəli trafik."
caption = "Enterprise qoşulmasında EAPOL, RADIUS, açar razılaşdırılması və adi trafikin ardıcıllığı."
wide = true
:::

### Qoşulmanın addım-addım izahı

Şərti nümunədə tələbənin noutbuku UNI-Student şəbəkəsinə qoşulur. Kontrollerin idarəetmə ünvanı 10.90.0.10, RADIUS serverininki 10.90.0.20, tələbə seqmenti 10.20.0.0/16 kimi seçilib. Bunlar layihə nümunəsidir, real UNEC şəbəkəsinin ünvanları deyil.

:::steps 802.1X qoşulması
[[step]]
title = "İlkin 802.11 qoşulması"
body = "Noutbuk şəbəkəni tapır, təhlükəsizlik imkanlarını yoxlayır və AP ilə ilkin qoşulmanı qurur. Bu mərhələdəki Open System authentication adı istifadəçinin kimliyinin yoxlandığı mənasına gəlmir."

[[step]]
title = "İdarə olunan port bağlıdır"
body = "Adi məlumat trafiki üçün port bağlı qalır. Autentifikasiyaya aid idarə olunmayan yol EAPOL mesajlarını keçirir. Avadanlığın əlavə ilkin giriş imkanları ayrıca siyasətlə məhdudlaşdırılır."

[[step]]
title = "Identity mübadiləsi"
body = "Autentifikator EAP-Request/Identity göndərir, müştəri EAP-Response/Identity qaytarır. Müştəri EAPOL-Start ilə prosesi başlada bilər, lakin bütün qoşulmalarda bu mesajın görünməsi məcburi deyil."

[[step]]
title = "Access-Request"
body = "Kontroller kimlik cavabını Access-Request daxilində RADIUS-a ötürür. Sorğu AP, sessiya və cihaz haqqında atributlar da daşıya bilər."

[[step]]
title = "EAP üsulu və Access-Challenge"
body = "Server EAP üsulunu təklif edir, Access-Challenge cavabları ilə mübadilə davam edir. Böyük sertifikat mesajları hissələrə bölünə bilər; bir qoşulmada çoxlu sorğu-cavab normaldır."

[[step]]
title = "Kimliyin yoxlanması və nəticə"
body = "Seçilmiş üsul kimliyi yoxlayır. EAP-TLS-də tərəflər sertifikatları və uyğun şəxsi açara sahibliyi təsdiqləyir. Siyasət icazə verərsə server Access-Accept, əks halda Access-Reject qaytarır."

[[step]]
title = "Açar materialı"
body = "Uğurlu EAP mübadiləsindən açar materialı yaranır. Müştəri bunu öz EAP hesablamalarından əldə edir; server autentifikatora lazım olan materialı qorunan RADIUS mexanizmi ilə çatdırır. Hər tərəfə eyni parolun göndərilməsi baş vermir."

[[step]]
title = "Dörd addımlı açar razılaşdırması"
body = "Müştəri və AP dörd addımlı açar razılaşdırmasını tamamlayır. Bu mərhələ EAP autentifikasiyasından ayrıdır. Açarların uyğunluğu təsdiqlənəndən və siyasət tətbiq ediləndən sonra adi trafikə yol açılır."

[[step]]
title = "VLAN, DHCP, DNS, HTTPS"
body = "Cihaz uyğun VLAN-da DHCP ilə IP alır, DNS-dən istifadə edir və LMS-ə HTTPS bağlantısı qurur. Uçot aktivdirsə sessiyanın başlanması RADIUS accounting xidmətinə yazılır."
:::

Access-Accept görülməsi internetin işlədiyini sübut etmir. Kontroller qəbul cavabını düzgün sessiyaya bağlamalı, açar razılaşdırması tamamlanmalı, təyin olunmuş VLAN AP və kommutatorda mövcud olmalıdır; DHCP, DNS və firewall da ayrıca işləməlidir. 

:::exam
Autentifikasiya uğurlu olduqda RADIUS "Access-Accept" və PMK qaytarır, sonra AP ilə 4-way handshake aparılır. RADIUS istifadəçinin roluna görə VLAN da təyin edə bilər (şərti nümunə: tələbə VLAN 10, müəllim VLAN 20). Konspektdə də vurğulanır: 802.1X-in üç rolunda qərarı RADIUS verir.
:::

### Sessiya açarları və təkrar qoşulma

EAP üsulunun yaratdığı baş sessiya açarı (master session key, MSK) ilə Wi-Fi məlumat paketini qoruyan seans açarı eyni anlayış deyil. MSK-dən cüt baş açar (pairwise master key, PMK) materialı alınır; dörd addımlı razılaşdırma konkret rabitəyə aid açarları formalaşdırır. Məqsəd düsturları təkrar etmək deyil, məsuliyyət sərhədini görməkdir: EAP uğurlu ola, sonrakı açar mərhələsi isə uyğunluq səhvinə görə dayana bilər.

Tələbə korpuslar arasında hərəkət edəndə hər dəfə tam sertifikat mübadiləsi gecikmə yarada bilər. IEEE 802.11r sürətli keçid üçün istifadə oluna bilər, amma cihaz uyğunluğu və açarların paylanma sərhədi yoxlanmalıdır. Keşin olması ləğv edilmiş kimliyin nə vaxt yenidən yoxlanacağı sualını da yaradır.

Sessiya müddəti, yenidən autentifikasiya və aktiv bağlantının kəsilməsi ayrı parametrlərdir. Noutbukun sertifikatı ləğv edildikdə cari sessiya avtomatik yox olmaya bilər: kontrollerdə sessiyanın dayandırılması və keşlərin siyasətə uyğun təmizlənməsi tələb olunur. 

## EAP üsulları və seçimin əsaslandırılması

### Çərçivə ilə üsulun fərqi

Genişləndirilə bilən autentifikasiya protokolu (Extensible Authentication Protocol, EAP) müxtəlif üsullar üçün mesaj çərçivəsidir. EAP adı özlüyündə nə sertifikat, nə parol, nə də güclü qarşılıqlı autentifikasiya vəd edir. EAP-Request və EAP-Response seçilmiş üsulun məlumatını daşıyır; üsulun kriptoqrafik xüsusiyyətləri, cihaz dəstəyi və server siyasəti birlikdə qiymətləndirilir.

| Üsul | Serveri necə tanıdır | Müştərini necə tanıdır | İdarəetmə və risk |
| --- | --- | --- | --- |
| EAP-TLS | Server sertifikatı | Müştəri sertifikatı və şəxsi açar | PKI tələb edir; açarın qorunması vacibdir |
| PEAP-MSCHAPv2 | Xarici TLS tunelində sertifikat | Tuneldə parol əsaslı challenge-response | Yanlış serverə cavab verilməsi parol riskidir |
| EAP-TTLS | Xarici TLS tunelində sertifikat | Tuneldə seçilən daxili üsul | Daxili üsul və kataloq uyğunluğu yoxlanır |
| EAP-MD5 | Qarşılıqlı server yoxlaması vermir | Sadə challenge-response | Enterprise Wi-Fi üçün uyğun seçim deyil |
| LEAP | Köhnə parol əsaslı yanaşma | Parol törəmələri | İstifadədən çıxarılmalıdır |

Universitet imtahan həftəsində hamını başqa üsula keçirərsə, kriptoqrafik baxımdan düzgün seçim xidmət itkisinə çevrilə bilər. Pilot qrup, idarə olunan profil və geri dönüş planı buna görə hazırlanır.

### EAP-TLS

EAP-TLS TLS əsasında qarşılıqlı sertifikat autentifikasiyası qurur. Serverdə sertifikat və ona uyğun şəxsi açar, cihazda isə müştəri sertifikatı və şəxsi açar olur. Etibarlı sertifikat sertifikatlaşdırma mərkəzinin (certificate authority, CA) imzasını daşıyır. Sertifikatı görmək kifayət etmir: tərəf ona uyğun şəxsi açarla protokolun tələb etdiyi sübutu verməlidir. Sertifikatın surətini köçürən şəxs şəxsi açar olmadan eyni kimliklə autentifikasiya edə bilməz.

Əvvəlcə noutbuk serverin sertifikat zəncirini, adını və istifadə məqsədini yoxlayır. Sonra server müştəri sertifikatını qəbul edib öz etibar siyasətinə görə yoxlayır. Hər iki tərəf TLS mübadiləsinin bütövlüyünü təsdiqləyir. Alınmış açar materialı Wi-Fi sessiyasının qurulmasında işlədilir; istifadəçinin şəbəkə parolunu hər qoşulmada təqdim etməsi tələb olunmur.

Lakin yoluxmuş və açıq cihaz qanuni autentifikasiya əməliyyatından sui-istifadə edə bilər. Ona görə EAP-TLS cihazın proqram vəziyyətini avtomatik sağlam elan etmir; yeniləmə, disk şifrələməsi və son qurğu mühafizəsi saxlanılır.

RADIUS sertifikatın kimliyini kataloqdakı aktiv cihaz və ya istifadəçi qeydi ilə əlaqələndirir, icazəli sertifikat siyasətini yoxlayır və rolu bundan sonra seçir. CN sahəsində istənilən adın yazılması hüquq qazanmağa əsas olmamalıdır.

EAP-TLS-də sertifikat müddətinin bitməsi, yanlış saat, aralıq sertifikatın çatışmaması və ləğv siyahısına çatmamaq tipik dayanma səbəbləridir. Üsul parol təxminini aradan qaldırsa da sertifikat idarəsini tələb edir. 

:::note Konspektdən
Konspektə görə EAP-TLS ən güclü üsuldur: həm server, həm istifadəçi (cihaz) sertifikat göstərir, parol yoxdur. Sertifikatların verilməsi və ləğvi üçün PKI lazımdır; MDM paylamanı avtomatlaşdırır, amma məcburi deyil. TLS 1.3 ilə işləyə bilir.
:::

### PEAP-MSCHAPv2

Qorunan EAP (Protected EAP, PEAP) əvvəlcə server sertifikatı ilə TLS tuneli yaradır. Geniş yayılmış PEAP-MSCHAPv2 quruluşunda istifadəçi bu tunelin daxilində EAP-MSCHAPv2 ilə yoxlanılır. MSCHAPv2 paroldan törəyən challenge-response cavabları ötürür; parolun özü bu mübadilədə adi mətn kimi göndərilmir. Buna baxmayaraq cavabların təhlükəsizliyi parolun və üsulun xüsusiyyətlərindən asılıdır.

Cihaz server sertifikatını yoxlamırsa, TLS tunelini hücumçunun serveri ilə qura bilər. Hücumçu tunelin öz tərəfində daxili autentifikasiya mübadiləsini görə və parol törəmələrinə qarşı sındırma cəhdi apara bilər. Problem Wi-Fi adının təqlidi ilə başlayan yanlış etimaddır. Uzun parol riski azalda bilər, lakin server yoxlamasının söndürülməsini təhlükəsiz etmir.

Ancaq hər LDAP kataloqu parolu açmadan MSCHAPv2 yoxlaması aparmağa imkan vermir: serverin uyğun parol törəməsinə və ya uyğun domen autentifikasiya mexanizminə çıxışı lazımdır. Sadə LDAP bind işləməsi PEAP-MSCHAPv2-nin də işləyəcəyini göstərmir; seçim pilotda kataloq imkanları ilə yoxlanır.

Ayrı xidmət kimliyi və ya sertifikata keçid bu əlaqəni azaldır. Tətbiqin çoxamilli autentifikasiyası yenə saxlanılır; adi PEAP qoşulmasının telefon bildirişi ilə MFA verdiyi düşünülmür.

### EAP-TTLS və uyğunluq

Tunellənmiş TLS (EAP-TTLS) də server sertifikatı ilə qorunan xarici kanal qurur. Müştəri tunelin daxilində PAP, CHAP, MSCHAPv2 və ya uyğun EAP üsulu ilə yoxlanıla bilər; dəqiq imkanlar müştəri və serverdən asılıdır. Buna görə sənəddə yalnız TTLS yazmaq azdır: daxili autentifikasiya üsulu da göstərilməlidir.

TTLS-PAP-də parol xarici TLS tunelinin daxilində serverə təqdim edilir. Radio dinləyicisi TLS düzgün qurulubsa parolu oxumur, amma tuneli bitirən server parolu emal edir. Cihaz saxta serverə etibar edərsə, hücumçu parolun özünü ala bilər. Fərq vacibdir: PEAP-MSCHAPv2-də saxta serverə challenge-response materialı, TTLS-PAP-də tunel daxilindəki parol sızır.

Lakin uyğunluq sözlə qəbul edilmir: dəstəklənən daxili üsul, server adı məhdudiyyəti və profil paylanması hər platformada sınanır. EAP üsullarının sayını səbəbsiz artırmaq istifadəçi cihazının daha zəif variantı seçməsi riskini və dəstək yükünü böyüdür; universitet yalnız əsaslandırılmış üsulları aktiv saxlayır.

### TEAP və autentifikasiyaların birləşdirilməsi

Tunelli EAP (Tunnel Extensible Authentication Protocol, TEAP) TLS tuneli daxilində müxtəlif autentifikasiya üsullarını, o cümlədən cihazın və istifadəçinin ardıcıl yoxlanmasını dəstəkləyir. Kriptoqrafik bağlama (crypto-binding) daxili autentifikasiyadan alınan açar materialını xarici TLS tuneli ilə əlaqələndirir. Beləliklə, yalnız cihaz sertifikatına əsaslanan girişdən fərqli olaraq, həm cihazın, həm istifadəçinin yoxlanmasını tələb edən siyasət qurula bilər. Server sertifikatının yoxlanması saxlanılır; TEAP dəstəyi, daxili üsullar və bağlama siyasəti pilotda sınanır.

:::note Konspektdən
Konspekt əlavə edir: PEAP-ın xarakteristikası "geniş yayılıb; cihaz server sertifikatını yoxlamırsa saxta AP parolu ələ keçirə bilər". EAP-TTLS PEAP-a bənzər tuneldir, içində müxtəlif köhnə üsullar ola bilər; eyni şərt: server sertifikatı yoxlanmalıdır. TEAP müasirdir, EAP-FAST-ın davamıdır (RFC 9930, RFC 7170-ni əvəz edib). LEAP və EAP-MD5 köhnə, etibarsız üsullardır və işlədilməməlidir.
:::

## Sertifikat yoxlaması və kimliyin həyat dövrü

### Sertifikatın hansı hissələri yoxlanılır

Server sertifikatının yoxlanması bir neçə ayrı sualdan ibarətdir. İmza etibarlı zəncirə bağlanırmı? Müddət keçməyibmi? Server gözlənilən ada malikdirmi? Sertifikat bu istifadə üçün uyğundurmu? Profilin güvəndiyi CA düzgün seçilibmi? Ləğv yoxlaması hansı siyasətlə aparılır? Bu sualların birinə müsbət cavab digərlərinin cavabını əvəz etmir.

| Nəzarət | Yoxlanılan xüsusiyyət | Universitetdə səhv nümunəsi |
| --- | --- | --- |
| Etibar zənciri | İcazəli kök və aralıq CA imzaları | Təsadüfi endirilmiş kök CA quraşdırılıb |
| Server adı | Profildəki ad ilə SAN uyğunluğu | Başqa xidmətə verilmiş sertifikat qəbul edilir |
| Vaxt | Başlama və bitmə tarixləri | Telefonun saatı yanlışdır |
| İstifadə məqsədi | Uyğun açar istifadəsi və EKU | Uyğunsuz məqsədli sertifikat seçilib |
| Ləğv statusu | CRL və ya OCSP siyasəti | Oğurlanan cihazın sertifikatı hələ qəbul edilir |
| Açara sahiblik | Şəxsi açarla protokol sübutu | Yalnız sertifikat faylı köçürülüb |

Profil yalnız geniş istifadə olunan ictimai CA-ya etibar edib server adını məhdudlaşdırmırsa, başqa təşkilatın düzgün sertifikatı da qəbul edilə bilər. Universitet üçün gözlənilən ad açıq müəyyən edilir, məsələn, radius.wifi.uni.example. İstifadəçinin ekranında xəbərdarlığı əl ilə qəbul etməsi bu nəzarətin əvəzi sayılmır.

:::figure
src = "m09-2.png"
alt = "Server sertifikatı RADIUS-dan gəlir və dörd yoxlamadan keçir: zəncir (profil CA-sına çatır?), ad (server adı uyğundur?), vaxt (müddət keçməyib?), siyasət (EKU, ləğv). Cavab bəlidirsə kimlik məlumatı göndərilir, xeyrdirsə qoşulma dayandırılır."
caption = "Cihazın serverə etibar etməsi üçün zəncir, ad, vaxt və siyasət yoxlamaları."
wide = true
:::

Ləğv siyahısı (certificate revocation list, CRL) CA-nın ləğv edilmiş sertifikatlarını göstərir. Onlayn sertifikat status protokolu (OCSP) konkret sertifikatın statusu haqqında sorğuya cavab verir. Server müştəri sertifikatının ləğvini həqiqətən yoxlamalıdır: PKI panelində ləğv düyməsini basmaq RADIUS keşinin yeniləndiyini sübut etmir. CRL-in növbəti yenilənmə vaxtı və əldə olunmama siyasəti sənədləşdirilir.

Əvvəlcədən paylanmış etibar məlumatı, saxlanmış ləğv məlumatı və platformanın dəstəklədiyi status mexanizmləri qiymətləndirilir; bütün müştərilərin eyni OCSP davranışına malik olduğu fərz edilmir. Status xidmətinə çatmama halında girişi bağlamaqla davam etdirmək arasında seçim risk və əlçatanlıq qərarıdır.

### İdarə olunan profil nümunəsi

Aşağıdakı wpa_supplicant fraqmenti EAP-TLS profilinin məntiqini göstərir. SSID, fayl yolları və cihaz kimliyi şərtidir. Müştəri sertifikatı, şəxsi açar və CA zənciri əvvəlcədən təhlükəsiz kanalla verilməlidir. Fayl şəklində açar tədris nümunəsidir; istehsalda aparat açar anbarı və əməliyyat sisteminin idarə olunan sertifikat mexanizmi seçilə bilər.

```
network={
  ssid="UNI-Staff"
  key_mgmt=WPA-EAP
  eap=TLS
  identity="device-042@uni.example"
  ca_cert="/etc/wifi/campus-ca.pem"
  domain_match="radius.wifi.uni.example"
  client_cert="/etc/wifi/device-042.pem"
  private_key="/etc/wifi/device-042.key"
  ieee80211w=2
}
```

`domain_match` gözlənilən server adına məhdudiyyət qoyur; `ca_cert` etibar mənbəyini göstərir. `ieee80211w=2` PMF-i tələb edir, buna görə AP və müştəri uyğun olmalıdır. `WPA-EAP` yazısı özlüyündə WPA3 192 bit profilini qurmur; rejim və alqoritm tələbləri ayrıca uyğunlaşdırılır. Şəxsi açara fayl icazələri verilməli, fayl ümumi tələbə qovluğunda saxlanılmamalıdır.

Domen hissəsi federasiyada marşrutlaşdırma üçün lazımdır. Xarici kimliyin gizlədilməsi bütün EAP variantlarında eyni davranışı vermir; xüsusən sertifikat məlumatının görünməsi protokol versiyasından da asılıdır. Universitet məxfilik iddiasını konkret profil və paket izi əsasında yoxlayır.

### Sertifikatın verilməsi və ləğvi

İlkin qeydiyyat (onboarding) ən həssas mərhələlərdəndir. Cihaz hələ universitet Wi-Fi-ına güvənmədiyi vaxt profil və CA almalıdır. Bunlar təsadüfi açıq şəbəkədəki portalın göstərişi ilə quraşdırılmır: universitetin yoxlanmış HTTPS ünvanı, idarə olunan cihaz sistemi və ya nəzarət edilən ilkin qeydiyyat kanalı istifadə olunur. Kök CA quraşdırılması cihazın etibar sərhədini dəyişdirdiyi üçün istifadəçiyə aydın izah edilir.

Eyni sertifikat və açar bütün yataqxana cihazlarına köçürülərsə, bir cihazın itməsi bütün qrupu riskə atar. Şərti uçotda sertifikat seriya nömrəsi cihaz inventarı və sahibin hesabı ilə əlaqələndirilir. Seriya nömrəsi parol deyil, amma şəxsi məlumatlarla birləşdirilmiş uçota giriş məhdudlaşdırılır.

Yenilənmə üçün cihazın sertifikatı bitənə qədər gözlənilmir. Sertifikat yenilənə bilməyibsə dəstək xidməti səbəbi araşdırır; server yoxlamasını söndürən müvəqqəti təlimat yaymır. Tələbənin semestrlik status dəyişikliyi də eyni qaydada səlahiyyət siyasətinə ötürülür.

## RADIUS xidməti və konfiqurasiya məntiqi

### Paketlər və atributlar

RADIUS şəbəkə cihazı ilə AAA xidməti arasında giriş qərarını və uçot məlumatını daşıyır. RADIUS müştərisi tələbənin telefonu deyil, sorğunu göndərən AP və ya kontrollerdir. Server yalnız qeydiyyata alınmış şəbəkə cihazlarından sorğu qəbul etməlidir. Telefonun sertifikatı ilə kontrollerin RADIUS sirri müxtəlif tərəfləri tanıyır və bir-birini əvəz etmir.

Ənənəvi RADIUS autentifikasiya üçün UDP 1812, uçot üçün UDP 1813 portlarından istifadə edir. Access-Request sorğusuna Access-Challenge, Access-Accept və ya Access-Reject cavabı gələ bilər; uçotda Accounting-Request və Accounting-Response işləyir. RADIUS bütün paketi avtomatik şifrələyən protokol deyil: atributların bir hissəsi ənənəvi daşınmada açıq görünür, parol sahəsinin xüsusi gizlədilməsi isə bütöv kanalın məxfiliyinə bərabər deyil.

| Atribut | Məna | İstifadə məhdudiyyəti |
| --- | --- | --- |
| User-Name | Təqdim olunan kimlik | Xarici anonim kimlik real şəxsdən fərqlənə bilər |
| NAS-IP-Address | Şəbəkə giriş cihazının ünvanı | Mənbə və etibarlı cihaz uçotu ilə yoxlanır |
| Calling-Station-Id | Adətən müştərinin MAC ünvanı | İnsan kimliyini sübut etmir |
| Called-Station-Id | AP və SSID haqqında məlumat | Format istehsalçıdan asılıdır |
| EAP-Message | EAP mesajının daşınması | Daxili üsul ayrıca işlənir |
| Message-Authenticator | RADIUS mesajının bütövlük yoxlaması | Tələbi və yoxlaması aktiv olmalıdır |
| Tunnel-Private-Group-Id | Dinamik VLAN identifikatoru | Kontrollerin uyğun dəstəyi tələb olunur |
| Acct-Session-Id | Uçot sessiyasının identifikatoru | Qurğu və vaxt konteksti ilə əlaqələndirilir |

RADIUS serverinin qaytardığı rol əməli olaraq tətbiq edilməlidir. Şərti nümunədə əməkdaşa VLAN 20, tələbəyə VLAN 10 təyin edilir; bu nömrələr nümunədir. VLAN identifikatoru kontrollerdə tanınmırsa, cihaz giriş ala bilməyə və ya yanlış standart seqmentə düşə bilər. Xüsusilə ehtiyat konfiqurasiyanın bütün istifadəçiləri geniş səlahiyyətli VLAN-a keçirmədiyi yoxlanılır.

### FreeRADIUS fraqmentləri

Aşağıdakı fraqmentlər FreeRADIUS 3.x üslubundadır; tam server faylı deyil, tədris nümunəsidir. Kataloq yolları paketdən asılıdır. Sertifikat faylları, etibarlı müştəri CA-sı, ləğv məlumatı və sertifikat kimliyini rola bağlayan siyasət əvvəlcədən hazırlanmalıdır. İstehsalda istifadə ediləcək sirr ayrıca yaradılır, nümunədəki qiymət köçürülmür.

RADIUS müştərisinin qeydiyyatı üçün `clients.conf`:

```
client campus_wlc {
  ipaddr = 10.90.0.10
  secret = "b39e84a1f79260dc475ba8e693d1c052"
  require_message_authenticator = yes
}
```

Hər kontrollerə ayrıca, uzun və təsadüfi sirr verilir; sirr mənbə koduna və açıq jurnal qeydinə salınmır. Yalnız AP-lərin idarəetmə şəbəkəsindən RADIUS portuna yol açılır; bütün tələbə VLAN-ına bu icazə lazım deyil. Sirr sızarsa şəbəkə məhdudiyyəti zərəri azalda bilər, amma sirr yenə dəyişdirilməlidir.

EAP modulu üçün sadələşdirilmiş fraqment:

```
eap {
  default_eap_type = tls
  tls-config tls-campus {
    private_key_file = /etc/raddb/certs/server.key
    certificate_file = /etc/raddb/certs/server-chain.pem
    ca_file = /etc/raddb/certs/client-ca.pem
    ca_path = /etc/raddb/certs/trust
    check_crl = yes
    tls_min_version = "1.2"
  }
  tls { tls = tls-campus }
}
```

`server-chain.pem` serverin sertifikatını və lazım olan aralıq sertifikatları daşıyır; `client-ca.pem` müştəri sertifikatlarına etibar mənbəyidir. Bunlar eyni vəzifə deyil. `check_crl` yazısı təkbaşına ləğv xidmətini yaratmır: CA və CRL faylları TLS kitabxanasının tələb etdiyi quruluşda yerləşdirilməli, CRL yenilənməsi izlənilməlidir. Vaxtı keçmiş CRL ilə davranış ayrıca sınanır.

Virtual serverdə EAP modulunun çağırılması:

```
authorize { eap { ok = return } }
authenticate { eap }
```

Sertifikatın etibarlılığı təsdiqlənəndən sonra aktiv inventar qeydi və icazəli qrup üzrə yoxlama əlavə edilir. İstehsal konfiqurasiyasındakı mövcud siyasət blokları bu fraqmentlə kor-koranə əvəz olunmur. Yanlış CA-dan verilmiş və ya kataloqda bağlanmış cihaza aid sertifikatın rədd edilməsi qəbul sınağının hissəsidir.

Standart tunel atributları ilə şərti VLAN cavabı:

```
update reply {
  Tunnel-Type := VLAN
  Tunnel-Medium-Type := IEEE-802
  Tunnel-Private-Group-Id := "20"
}
```

Kontrollerdə VLAN 20-nin mövcudluğu, daşındığı kommutator xətləri və həmin VLAN üçün firewall siyasəti ayrıca yoxlanır. RADIUS atributu firewall qaydasını öz-özünə yaratmır.

### Yerli yoxlama və diaqnostika

Laboratoriya serverində konfiqurasiyanın yüklənməsi `radiusd -XC` (və ya paketdəki `freeradius -XC`) əmri ilə yoxlanır. Bu, sintaksis və yüklənmə yoxlamasıdır; sertifikat siyasətinin təhlükəsiz olduğunu sübut etmir. Ətraflı diaqnostika rejimi yalnız nəzarət olunan mühitdə açılır, çünki çıxışda kimliklər və həssas texniki məlumat görünə bilər.

```
radiusd -XC
openssl x509 -in server.pem -noout -subject -issuer -dates
openssl x509 -in server.pem -noout -ext subjectAltName
```

EAP sınağı üçün uyğun müştəri və ya `eapol_test` kimi alət, sonra real radio sessiyası lazımdır. Şəbəkə komandası müsbət sınaqla kifayətlənmir: yanlış server adı, etibarsız CA və ləğv edilmiş müştəri sertifikatı ilə mənfi sınaqlar da aparır.

## RADIUS nəqliyyatının qorunması

### Blast-RADIUS nəyi dəyişdi

Blast-RADIUS (CVE-2024-3596) RADIUS-un ənənəvi kriptoqrafik quruluşundakı zəiflikdir. Müəyyən şəraitdə şəbəkə yoluna müdaxilə edən hücumçu MD5 toqquşması yanaşması ilə cavabın mənasını dəyişdirməyə çalışa bilər. Bu, Wi-Fi parolunu radio kanalından təxmin etmək hücumu deyil. Risk əsasən lazımi mesaj bütövlüyü qoruması olmayan RADIUS mübadilələrinə aiddir.

EAP daşıyan RADIUS paketlərində Message-Authenticator tələbi artıq mövcuddur və onun düzgün yoxlanması qoruyucu sərhəddir. Ona görə bütün 802.1X quruluşlarının eyni dərəcədə açıq olduğunu demək düzgün deyil. 

Universitet server və kontrollerləri düzəlişli versiyaya keçirir, Message-Authenticator atributunun tələb edilməsini və yoxlanmasını uyğun tərəflərdə aktivləşdirir. Köhnə cihazların atributu düzgün göndərib-göndərmədiyi pilotda ölçülür. Uyğunsuz cihaz üçün bütövlük yoxlamasını bütün serverdə söndürmək əvəzinə cihazın yenilənməsi və məhdudlaşdırılması planlaşdırılır. Uzun ortaq sirr bu protokol zəifliyinin düzəlişini əvəz etmir.

### RadSec və etimad sərhədi

RadSec RADIUS-un TLS üzərindən daşınması üçün işlədilən addır. RFC 6614 RADIUS over TLS mexanizmini təsvir edir; standart xidmət portu TCP 2083-dür. TLS nəqliyyat kanalının məxfiliyini və bütövlüyünü qoruyur, sertifikat siyasəti ilə qarşı tərəfi tanıdır. Burada da server adının yoxlanması, icazəli CA-lar və sertifikatların yenilənməsi tələb olunur.

RadSec-də qurulan TLS ilə EAP-TLS daxilindəki TLS müxtəlif bağlantılardır. EAP-TLS istifadəçi cihazı ilə ev autentifikasiya serveri arasındakı kimlik mübadiləsinə aiddir. RadSec isə iki RADIUS tərəfi arasındakı nəqliyyat hissəsini qoruyur. Federasiya proksisi RadSec bağlantısını bitirib növbəti proksiyə ayrı TLS bağlantısı qura bilər; buna görə RadSec bütün federasiyanı birbaşa cihazdan serverə uzanan tək kanal etmir.

| Meyar | EAP-TLS | RadSec |
| --- | --- | --- |
| Tərəflər | Supplicant və EAP serveri | RADIUS müştərisi, proksi və ya server |
| Vəzifə | Şəbəkəyə girən kimliyi yoxlamaq | RADIUS nəqliyyatını qorumaq |
| Sertifikat siyasəti | İstifadəçi və cihaz giriş siyasəti | RADIUS qonşularının etibar siyasəti |
| Universitet nümunəsi | Kafedra noutbukunun tanınması | Kampusla federasiya proksisi arasında kanal |
| Əvəz etmədiyi tədbir | VLAN və tətbiq səlahiyyətləri | EAP server sertifikatının müştəridə yoxlanması |

Dəstək yoxdursa qorunan idarəetmə şəbəkəsi və uyğun tunel həlli qiymətləndirilir. Server sertifikatını qəbul edib qarşı tərəfi məhdudlaşdırmayan TLS sazlaması düzgün tamamlanmış həll sayılmır; sertifikatı olan hər RADIUS qonşusuna bütün sorğuları göndərmək federasiya siyasətini poza bilər.

## eduroam federasiyası

### Kimlik evdə, giriş səfər edilən şəbəkədə

eduroam iştirakçı təhsil və tədqiqat təşkilatlarında istifadəçinin öz təşkilatının kimlik məlumatı ilə şəbəkəyə qoşulmasına imkan verən federasiyadır. Bu izah konkret universitetin iştirak statusu haqqında iddia deyil. İştirakçı universitetdən olan tələbə başqa üzv kampusda eduroam SSID-sini seçir: qonaq kampus radio xidmətini verir, kimliyi isə tələbənin ev təşkilatı yoxlayır.

Şərti tələbə kimliyi ayla@uni.example olsun. `uni.example` hissəsi realm adlanır və sorğunun hara yönəldilməsini göstərir. Qonaq təşkilatın RADIUS sistemi federasiya qaydalarına əsasən sorğunu uyğun marşrutla ev təşkilatına ötürür. Ev serveri EAP mübadiləsini tamamlayır və nəticəni geri qaytarır. Qonaq təşkilat girişin yerli qaydalarını (internetə çıxış, daxili şəbəkədən izolyasiya) tətbiq edir.

:::figure
src = "m09-3.png"
alt = "Cihaz (ali@ev.example) qonaq kampus AP-sinə, sonra qonaq RADIUS-a, federasiya proksilərinə və ev universitetinin RADIUS-una qoşulur; yuxarıda cihazla ev EAP serveri arasında TLS kanalı göstərilir. Marşrut istifadəçi adının realm hissəsinə görə seçilir."
caption = "Qonaq kampusdan ev universitetinə EAP sorğusunun federasiya üzərindən ötürülməsi."
wide = true
:::

Düzgün qurulmuş tunelli EAP-də daxili kimlik mübadiləsi ev EAP serverinə qədər qorunur. Bununla belə proksilər marşrutlaşdırma atributlarını, xarici kimliyi və müəyyən sessiya metadatasını görə bilər; görülən məlumat seçilmiş EAP üsulundan və konfiqurasiyadan asılıdır. Federasiya nə bütün metadatanı gizlədir, nə də iştirakçıların jurnal və məxfilik öhdəliklərini aradan qaldırır.

### Profil paylanması və nasazlığın yeri

eduroam-da etibarlı server adı qonaq kampusun adı deyil, istifadəçinin ev təşkilatının profilində göstərilən addır. Tələbənin hər səfərdə təsadüfi CA və server qəbul etməsi lazım deyil. Rəsmi təşkilat profili CAT və ya geteduroam kimi quraşdırma vasitələri ilə verilə bilər. İstifadəçi profili seçəndə ev təşkilatını düzgün seçməlidir; saxta saytdan yüklənmiş profil etimad problemini həll etmir.

Realm-in səhv yazılması, federasiya marşrutunun dayanması, RADIUS nəqliyyatının pozulması və qonaq təşkilatın siyasəti araşdırılır. Eyni ev təşkilatının bir neçə istifadəçisi eyni qonaq kampusda dayanıbsa, ortaq yol yoxlanır. Tək cihaz dayanıbsa profil, saat və sertifikat dəstəyi əvvəl araşdırılır.

eduroam uğuru qonaq kampusun tələbə bazasına giriş vermir: şəbəkə xidməti ilə tətbiq səlahiyyəti yenə ayrıdır. Ev təşkilatı hesabı bağladıqda federasiya üzrə növbəti autentifikasiya rədd edilməlidir, amma artıq qurulmuş sessiyaların müddəti və kəsilməsi ayrıca idarə edilir. Buna görə ev və qonaq təşkilatların əməli əlaqə kanalı və məhdudiyyət siyasəti olmalıdır.

:::note Konspektdən
Konspekt eduroam-ı belə təsvir edir: dünya üzrə universitetlərin ortaq Wi-Fi şəbəkəsidir; texniki əsası 802.1X-dir, qonaq universitetin AP-si sorğunu RADIUS iyerarxiyası ilə tələbənin öz universitetinin RADIUS serverinə ötürür. Ən çox rast gəlinən səhv cihazda server sertifikatını yoxlamamaqdır: "eduroam" adlı saxta AP qurmuş hücumçu tələbənin məlumatlarını ələ keçirib parolunu sındırmağa çalışa bilir. Ona görə universitetlər rəsmi quraşdırma aləti (geteduroam / CAT) ilə profil paylayır.
:::

## MAC filtrləməsi, gizli SSID və captive portal

### İdentifikator niyə sübut deyil

MAC filtrləməsi yalnız siyahıdakı ünvanların qoşulmasına icazə verən əlavə qaydadır. MAC ünvanı şəxsi açarla kimlik sübutu vermir və uyğun avadanlıqda dəyişdirilə bilər. Radio mübadiləsində lazım olan ünvanlar müşahidə edilə bildiyi üçün hücumçu icazəli ünvanı təqlid etməyə çalışa bilər. Şəbəkə siyahısında görünən ünvanı insanın kimliyi kimi qəbul etmək düzgün deyil.

Cihaz bir SSID üçün sabit təsadüfi ünvan işlədə və ya platforma siyasətinə görə ünvanı dəyişə bilər. Dəstək xidməti buna görə tələbənin cihazını qəsdən ünvan saxtalaşdıran hücumçu kimi dərhal təsnif etmir. Sertifikat kimliyi daha sabit giriş meyarı verə bilər.

Gizli SSID şəbəkə adının beacon kadrında açıq yayımını azaldır. Qoşulma mübadilələri və bəzi aktiv axtarışlar (probe sorğuları) adı yenidən göstərə bilər. Gizlətmə kriptoqrafik giriş nəzarəti deyil: kitabxanada adı gizlədilmiş, lakin ortaq parolu yayılmış AP-ni təhlükəsiz hesab etmək olmaz. Şəbəkənin istifadəsi çətinləşə bilər, autentifikasiya güclənmir.

### Portal nəyi idarə edir

Captive portal istifadəçini brauzerdə qeydiyyat və ya şərtləri qəbul etmə səhifəsinə yönəldən giriş mexanizmidir. Bu mərhələyə qədər cihaz radioya qoşulub IP almış ola bilər. Şəbəkə yalnız məhdud ilkin xidmətləri buraxır, portal təsdiqindən sonra sessiyaya başqa qayda tətbiq edir. Portalın özü radio kadrlarını şifrələmir; bunun üçün ayrıca Wi-Fi rejimi lazımdır (8-ci mövzu).

Universitetin əsas əməkdaş parolunu hər açıq Wi-Fi portalında yazmaq vərdişi yaradılmamalıdır. Portalın HTTPS ünvanı və sertifikatı düzgün olmalı, qonağa hansı təşkilatın səhifəsi olduğu aydın görünməlidir. Portalı göstərmək üçün HTTPS saytının sertifikatını saxtalaşdırmaq qəbuledilən həll deyil.

| Mexanizm | Faydalı olduğu yer | Vermədiyi zəmanət |
| --- | --- | --- |
| MAC filtri | Sadə cihaz uçotuna əlavə nəzarət | İnsan və cihazın kriptoqrafik kimliyi |
| Gizli SSID | Yayım davranışının idarəsi | Şəbəkənin gizli və əlçatmaz qalması |
| Captive portal | Qonaq qeydiyyatı və şərtlərin qəbulu | Radio şifrələməsi və AP kimliyi |
| Müştəri izolyasiyası | Qonaqların birbaşa əlaqəsinin azaldılması | Bütün VLAN və kabel yollarının bağlanması |
| OWE | Qonaq radio kanalında passiv dinləmənin azaldılması | Universitetin AP-sinin autentifikasiyası |

Qonaq VLAN-ından daxili ünvanlara firewall qaydası buna görə saxlanılır. Portalın vaxtı bitəndə girişin həqiqətən dayandığı, DNS və ilkin icazəli xidmətlərdən sui-istifadə imkanları ayrıca sınanır. Portal şəbəkəsi əməkdaş seqmenti ilə eyni giriş səviyyəsində qalmamalıdır.

:::exam
MAC süzgəci zəif tədbirdir: MAC havada açıq görünür və asanlıqla saxtalaşdırılır. Gizli SSID təhlükəsizlik vermir: ad cihazların probe sorğularında yenə görünür. Captive portal qonaq şəbəkələri üçündür, şifrələmə vermir.
:::

## Simsiz hücumlar və qarşı tədbirlər

### Evil twin və rogue AP

Saxta qoşa giriş nöqtəsi (evil twin) istifadəçini aldatmaq üçün etibarlı şəbəkənin adını və görünən xüsusiyyətlərini təqlid edir. Güclü siqnal, tanış SSID və universitet loqosu etibar sübutu deyil. Müştərinin hansı AP-ni seçməsi siqnal, keçmiş profil və platforma siyasətindən asılıdır; həmişə ən güclü AP-yə qoşulduğunu fərz etmək olmaz. Hücumçu saxta portal və ya yanlış EAP serveri ilə kimlik məlumatını almağa çalışa bilər.

İcazəsiz giriş nöqtəsi (rogue AP) təşkilatın razılığı olmadan infrastruktura qoşulmuş AP-dir. Kafedrada zəif siqnalı düzəltmək istəyən əməkdaşın şəxsi routeri də bu kateqoriyaya düşür. Məqsəd zərərli olmasa belə kabel şəbəkəsinə nəzarətsiz radio yolu açıla bilər. Bir cihaz həm icazəsiz qoşulmuş, həm də universitet SSID-sini aldadıcı şəkildə təqlid etmiş ola bilər; kateqoriyalar bir-birini istisna etmir.

Evil twin-ə qarşı müştərinin server sertifikatını yoxlaması və idarə olunan profil əsas tədbirdir. Rogue AP-yə qarşı radio inventarı kabel portu uçotu ilə birləşdirilir. İstifadə olunmayan rozetkalar bağlanır, uyğun kabel portlarında 802.1X və şəbəkəyə girişə nəzarət (network access control, NAC) tətbiq edilir. Qanuni AP portunun sadəcə açıq trunk kimi hər kəsə verilməsi əlavə riskdir.

### Dinləmə və xidmətdən imtina

Passiv dinləmədə hücumçu radio trafikini qəbul edir. Güclü Wi-Fi şifrələməsi məzmunu qoruyur, amma trafik vaxtı, kadr ölçüsü və bəzi identifikatorlar görünə bilər. Tətbiq səviyyəli HTTPS qoruması AP-dən sonrakı yollar üçün də lazımdır.

Deautentifikasiya və disassosiasiya kadrlarının saxtalaşdırılması bəzi quruluşlarda cihazı bağlantıdan ayıra bilər. PMF uyğun əlaqədə müəyyən möhkəm idarəetmə kadrlarını qoruyur; bütün idarəetmə kadrlarını və hər ilkin qoşulma vəziyyətini eyni şəkildə qorumur. Radio basdırma (jamming) isə kanalı enerji və maneə ilə yararsız edə bilər; PMF fiziki radio maneəsini dayandırmır.

Amfiteatr dolanda kanalın sıxlığı, zəif müştəri antenası, qonşu avadanlıq və səhv kanal seçimi eyni şikayət yarada bilər. Şəbəkə komandası kadr sayğaclarını, spektr göstəricilərini və məkan üzrə ölçmələri tutuşdurur. Kritik imtahan xidməti üçün kabel ehtiyatı, alternativ otaq və əməli əlaqə planı hazırlanır.

| Təhdid | Müşahidə edilən risk | Əsas tədbir və məhdudiyyət |
| --- | --- | --- |
| Evil twin | Yanlış serverlə kimlik mübadiləsi | Server adı və CA yoxlanır; SSID yetərli deyil |
| Rogue AP | Kabel şəbəkəsinə nəzarətsiz radio yolu | Port nəzarəti və inventar; yer fiziki təsdiqlənir |
| Saxta ayırma kadrları | Sessiyaların qırılması | PMF; bütün radio DoS hallarını bağlamır |
| Radio basdırma | Kanalın yararsız olması | Spektr araşdırması və ehtiyat yol |
| Parol təxmini | Personal və parollu EAP kimliyinin riski | Uyğun üsul, güclü sirr və cəhd monitorinqi |
| WPS-dən sui-istifadə | Sadələşdirilmiş qeydiyyatın zəifliyi | Ehtiyac yoxdursa WPS söndürülür |
| Köhnə proqram səhvi | Açar və idarəetmə funksiyasının pozulması | Müştəri, AP və kontroller yenilənir |

WPS rahat qoşulma funksiyasıdır; Enterprise autentifikasiyası üçün əsas mexanizm deyil və ehtiyac olmadığı halda söndürülür. KRACK kimi açarın yenidən quraşdırılması sinfindəki səhvlər proqram yeniləmələrinin niyə həm AP, həm müştəri üçün lazım olduğunu göstərir; kriptoqrafik mexanizm 8-ci mövzuya aiddir. Təkcə ortaq parolu dəyişmək proqram səhvini düzəltmir.

Şəbəkənin adını gizlətmək buna qarşı etibarlı maneə deyil. Universitet radio əhatəsini ehtiyaca görə tənzimləyir, lakin küçədən siqnalın görünməməsini təhlükəsizlik şərti seçmir. İcazəli yoxlama yazılı ərazi və vaxt sərhədi ilə aparılır; qonşu təşkilatların şəbəkəsinə müdaxilə edilmir.

:::note Konspektdən əlavə
Konspekt hücumları bu şəkildə verir: **Deauthentication**, saxta idarəetmə kadrları ilə cihazları şəbəkədən atmaq (DoS və ya əl sıxmasını yazmaq üçün), tədbir PMF (802.11w) və WPA3. **Jamming** protokolla qorunmur; tədbir aşkarlama (WIDS, spektr analizi), fiziki axtarış, kritik sistemlər üçün kabel ehtiyatı. **Offline parol təxmini**: WPA2-PSK əl sıxmasını yazıb parolu kompüterdə sınamaq; tədbir WPA3-SAE, uzun təsadüfi parol, Enterprise rejim. **WPS PIN hücumu**: 8 rəqəmli PIN hissə-hissə sınanır (Reaver); tədbir WPS-i söndürmək. **KRACK (2017)**: WPA2 əl sıxmasında açarın yenidən quraşdırılması səhvi; tədbir cihaz və AP proqramını yeniləmək. **War driving**: maşınla gəzib şəbəkələri xəritələmək; tədbir güclü şifrələmə və siqnalı lazım olan əraziyə uyğunlaşdırmaq. Evil twin üçün konspekt də 802.1X-də server sertifikatının yoxlanması, idarə olunan profillər, WIPS və istifadəçilərə sertifikat xəbərdarlığını keçməmək öyrətməyi göstərir; rogue AP üçün kabel portlarında 802.1X/NAC, WIDS/WIPS ilə radio skanı, icazəli AP inventarı.
:::

## WIDS/WIPS və icazəsiz AP ilə işləmə

### Aşkarlama mənbələri

Simsiz müdaxilə aşkarlama sistemi (wireless intrusion detection system, WIDS) radio mühitində şübhəli vəziyyətləri tapır və xəbərdarlıq yaradır. Simsiz müdaxilənin qarşısının alınması sistemi (wireless intrusion prevention system, WIPS) müəyyən cavab əməliyyatları da təklif edir. Sensor ayrıca cihaz və ya AP-nin ayrılmış radio funksiyası ola bilər. Xidmət göstərən radionun bütün kanalları fasiləsiz izlədiyi fərz edilmir.

Sensor icazəli SSID-nin fərqli təhlükəsizlik rejimi ilə yayıldığını, inventarda olmayan BSSID-ni və qeyri-adi idarəetmə trafiki sıxlığını görə bilər. Lakin inventarda olmayan AP qonşu mağazanın qanuni cihazı da ola bilər. Sadəcə SSID bənzərliyinə əsasən radio müdaxiləsi etmək qonşuların xidmətini poza bilər. WIDS xəbərdarlığı təsnif etməyə başlanğıcdır, yekun hökm deyil.

| Mənbə | Nəyi göstərir | Görmədiyi və ya zəif gördüyü hissə |
| --- | --- | --- |
| Radio sensoru | SSID, BSSID, kanal və bəzi kadr davranışı | Kabeldəki dəqiq qoşulma portu |
| Kontroller | Qoşulma, keçid və AP vəziyyəti | Özündən kənar AP-nin tam fəaliyyəti |
| RADIUS | Kimlik cəhdi və giriş nəticəsi | DHCP-dən sonrakı tətbiq fəaliyyəti |
| Kommutator | Port və MAC cədvəli | NAT arxasındakı bütün müştərilər |
| DHCP və DNS | Ünvan ayrılması və sorğular | Kimliyin kriptoqrafik sübutu |
| Firewall | Seqmentlərarası icazə və bloklar | Radio maneəsinin fiziki səbəbi |

### Rogue AP üçün iş ardıcıllığı

Kitabxanada UNI-Staff adını yayan naməlum cihaz aşkarlandığını düşünək. Xəbərdarlığın vaxtı və yeri qeyd edilir, sensorun gördüyü kanal və təhlükəsizlik rejimi saxlanılır. Komanda əvvəl inventarda planlı dəyişiklik olub-olmadığını yoxlayır: AP yenilənəndə BSSID dəyişə və köhnə inventar yanlış həyəcan yarada bilər. Təsdiq olmadan cihazın hücumçuya aid olduğu elan edilmir.

:::steps Rogue AP-yə cavab
[[step]]
title = "Tutuşdurma"
body = "Xəbərdarlığın radio məlumatı inventar, kontroller və dəyişiklik qeydləri ilə tutuşdurulur."

[[step]]
title = "Yerin daraldılması"
body = "Bir neçə sensorun müşahidəsi ilə ehtimal olunan yer daraldılır; dəqiq otaq fiziki baxışla təsdiqlənir."

[[step]]
title = "Kabel bağlantısı"
body = "Kabel bağlantısı ehtimalı kommutator portları, MAC cədvəli və DHCP qeydləri ilə araşdırılır."

[[step]]
title = "Port karantini"
body = "Cihazın universitetə aid portu müəyyən edilərsə, səlahiyyətli komanda portu karantinə keçirir və ya bağlayır."

[[step]]
title = "Təsirin qiymətləndirilməsi"
body = "Təsirlənmiş istifadəçilər və mümkün kimlik sızması qiymətləndirilir; lazım gələrsə parol və sessiyalar ləğv edilir."

[[step]]
title = "Sübut və düzəliş"
body = "Sübutlar saxlanılır, cihazın sahibi və qoşulma səbəbi müəyyən edilir, təkrarın qarşısı üçün port siyasəti düzəldilir."
:::

Səlahiyyət sərhədi və yerli qaydalar nəzərə alınır, qonşu şəbəkələrə təsir edilməməlidir. PMF aktiv cihazlarda saxta ayırma yanaşması texniki olaraq da məhdudlaşa bilər. Universitetin öz kabel portunu bağlamaq və icazəsiz cihazı fiziki ayırmaq çox vaxt daha dəqiq tədbirdir.

Sensor susarsa, kanal skanı dayansa və ya hadisələr mərkəzə çatmasa görünmə azalır. Buna görə sensorların sağlamlığı, son hesabat vaxtı və əhatə boşluqları izlənilir. Həftələrlə heç bir xəbərdarlıq gəlməməsi təhlükənin yoxluğunu sübut etmir; test AP-si və icazəli sınaqla aşkarlama yolu yoxlanır.

## Bluetooth və mobil rabitənin təhlükəsizliyi

### Bluetooth-da cütləşmə və səlahiyyət

Bluetooth qulaqcıq, klaviatura, telefon və sensor kimi cihazlar arasında qısa məsafəli rabitə qurur. Klassik Bluetooth və Bluetooth Low Energy eyni istifadə ssenarilərinə və tam eyni təhlükəsizlik davranışına malik deyil. Cütləşmə (pairing) zamanı cihazlar əlaqə açarları yaradır və seçilmiş üsuldan asılı olaraq qarşı tərəfi müəyyən dərəcədə yoxlayır. Sonrakı bağlantılar üçün bu açarların saxlanması bonding adlanır.

Ədədin müqayisəsi, keçid kodu və ayrıca kanal kimi üsullar insanın və cihazın imkanlarına görə seçilir. Just Works kimi istifadəçi təsdiqini sadələşdirən üsul uyğun rejimdə şifrələmə yarada bilər, amma aradakı adam hücumuna qarşı autentifikasiya zəmanəti vermir. Ekranı olmayan kitabxana sensorunda bu seçim rahat görünə bilər; həmin sensorun idarəetmə əmri ilə qapı açması isə daha sərt risk qiymətləndirilməsi tələb edir.

Quraşdırıcı cihazı fiziki nəzarət altında cütləşdirir, tələb olunan xidməti açır və sonradan cütləşmə imkanını məhdudlaşdırır. İcazəsiz fayl qəbulu və lazımsız xidmətlər bağlanır.

Bluetooth bağlantısı üzrə verilən səlahiyyət də ayrıca yoxlanılır: səs qulaqcığına qoşulmaqla kontaktları və faylları paylaşmaq eyni qərar deyil. Telefon hansı tətbiqə yaxınlıqdakı cihazları axtarmaq və məlumat oxumaq icazəsi verdiyini idarə etməlidir. Tələbənin şəxsi telefonunda həddən artıq icazəli tətbiq Wi-Fi təhlükəsizliyindən asılı olmayaraq məlumat sızdıra bilər.

| Risk | Universitet nümunəsi | Tədbir |
| --- | --- | --- |
| Yanlış cihazla cütləşmə | Eyni adlı ekran adapteri | Fiziki təsdiq və uyğun autentifikasiyalı üsul |
| Daim açıq cütləşmə | Kafedranın ortaq avadanlığı | Qeydiyyat pəncərəsi məhdudlaşdırılır |
| Köhnə proqram zəifliyi | Yenilənməyən sensor | İnventar və proqram yeniləməsi |
| Artıq xidmət icazəsi | Telefonun fayl və kontakt paylaşması | Yalnız tələb olunan profil və tətbiq icazəsi |
| Saxlanmış açarın sui-istifadəsi | İtirilmiş planşet | Cütləşmə qeydi silinir və cihaz ayrılır |

Təhlükəsizliyi konkret metr rəqəminə bağlamaq əvəzinə kimlik yoxlaması, açarların idarəsi və xidmət səlahiyyəti qiymətləndirilir. İstifadə olunmayan radio funksiyasının bağlanması hücum səthini azaldır, lakin tələb olunan əlçatanlıq funksiyalarını pozmamalıdır.

### Mobil şəbəkədə etimad

Mobil rabitədə SIM və ya eSIM daxilindəki abunə kimliyi operatorla autentifikasiya üçün istifadə edilir. Bu, telefon sahibinin universitetdəki rolunu təsdiqləmir. Operator səviyyəli radio şifrələməsi də bütün tətbiq yolunu ucdan-uca qorumur: tələbə mobil internetlə LMS-ə girəndə serverin HTTPS sertifikatını yenə yoxlamalıdır. Operatorun qanuni olması saxta tətbiqə daxil edilən parolu qorumaz.

Mobil nəsillərin təhlükəsizlik xüsusiyyətləri fərqlidir. Köhnə 2G yanaşmalarında şəbəkənin cihaza autentifikasiyası baxımından çatışmazlıqlar var. Sonrakı nəsillər gücləndirilmiş mexanizmlərdən istifadə edir, lakin cihazın aşağı nəsilə keçməsi və yanlış baza stansiyası kimi risklər qalır. Telefonun dəstəklədiyi və operatorun imkan verdiyi halda zəif köhnə rejimlərin məhdudlaşdırılması qiymətləndirilir; əhatə ehtiyacı da nəzərə alınır.

Saxta baza stansiyası və abunə izləmə riski ilə SIM dəyişdirmə fırıldağı ayrı məsələlərdir. İkincidə hücumçu operator hesabının idarəsini alaraq nömrəni başqa SIM-ə keçirməyə çalışır. Universitetin əsas hesab bərpası yalnız SMS-ə bağlıdırsa, nömrənin ələ keçirilməsi hesab riskinə çevrilə bilər. Daha güclü çoxamilli autentifikasiya və nəzarətli hesab bərpası bu asılılığı azaldır.

Bu, özlüyündə kabel şəbəkəsinə qoşulmuş rogue AP demək deyil. Lakin idarə olunan noutbukun eyni anda kampusa və nəzarətsiz hotspot-a qoşulması körpüləmə və məlumat nəzarəti riskləri yarada bilər. Universitet belə halları cihaz siyasətində dəqiq müəyyən edir; bütün şəxsi telefonları radio vasitəsilə susdurmağa çalışmır.

## BYOD, MDM və cihaz vəziyyəti

### Şəxsi cihaz üçün etibar səviyyəsi

Şəxsi cihazdan istifadə (bring your own device, BYOD) tələbə və əməkdaşın öz telefonunu və noutbukunu universitet xidmətlərinə qoşmasıdır. Cihazın universitetə məxsus olmaması onu avtomatik zərərli etmir. Bununla belə İT xidməti həmin cihazın yenilənməsinə, disk qorumasına və başqa istifadəçilərinə tam nəzarət etməyə bilər; giriş hüququ bu məhdud görünməyə uyğun seçilir.

Mobil cihazların idarə edilməsi (mobile device management, MDM) profil, sertifikat və siyasət paylaya, uyğun platformalarda cihaz vəziyyətini yoxlaya və idarə olunan məlumatı uzaqdan silə bilər. MDM EAP-TLS üçün məcburi texniki şərt deyil: sertifikat başqa təhlükəsiz qeydiyyat üsulu ilə də verilə bilər. MDM çoxsaylı cihazın profilini eyni siyasətlə idarə etməyi sadələşdirir.

Universitetin profilini silmək şəxsi fotoşəkilləri silmək səlahiyyəti ilə qarışdırılmamalıdır. Platforma imkan verirsə iş profili və idarə olunan tətbiq sahəsi seçilir. Şəxsi cihazı tam idarəyə verməyən tələbə üçün məhdud tədris çıxışı kimi alternativ hazırlanır.

### NAC və Zero Trust

NAC kimliklə yanaşı cihazın vəziyyəti haqqında məlumatdan da istifadə edə bilər. Şərti siyasətdə idarə olunan, yenilənmiş noutbuk əməkdaş roluna, uyğunluq problemi olan cihaz isə bərpa seqmentinə yönəldilir. Bu məlumat MDM, son qurğu agenti və inventardan gələ bilər. Adi EAP-TLS sertifikatı özü antivirusun işlədiyini və ya son yeniləmənin qurulduğunu bildirmir.

Zero Trust yanaşmasında daxili şəbəkədə yerləşmək bütün xidmətlərə etibar üçün əsas deyil. Kafedra noutbuku Wi-Fi-a uğurla qoşulsa da tələbə bazasına giriş ayrıca hesab, cihaz vəziyyəti və səlahiyyətlə yoxlanılır. Tətbiq sessiyası və şəbəkə sessiyası müxtəlif müddətlərdə yaşaya bilər: Wi-Fi sessiyasını kəsmək artıq yaradılmış tətbiq tokenini həmişə ləğv etmir.

| Cihaz sinfi | Kimlik və idarəetmə | İcazə sərhədi |
| --- | --- | --- |
| Universitet noutbuku | Ayrı sertifikat və MDM | Rol üzrə daxili xidmətlər |
| Tələbənin şəxsi cihazı | Fərdi profil və qeydiyyat | Tədris xidmətləri və internet |
| Qonaq telefonu | Müddətli qonaq qeydiyyatı | Daxili resurslara yol verilmir |
| Uyğunsuz cihaz | Kimlik tanınır, vəziyyət qəbuledilməzdir | Bərpa və dəstək xidmətləri |
| Məhdud imkanlı IoT | İnventar və dəstəklənən ayrıca sirr | Yalnız tələb olunan idarəetmə ünvanları |

Köhnə məlumatı həmişə etibarlı saymaq da, bütün tələbələri dərhal ayırmaq da problem yarada bilər. Riskə görə məhdud keçid müddəti və minimum səlahiyyət müəyyən edilir; məlumatın mənbəyi və yoxlanma vaxtı qərar jurnalına yazılır.

## Kampus simsiz şəbəkəsinin layihəsi

### Radio planı və tutum

Layihə cihaz sayından əvvəl istifadə ssenarilərini müəyyən edir: amfiteatrda eyni vaxtda LMS imtahanına girən tələbələr, kitabxanada səssiz işləyən noutbuklar və yataqxanadakı şəxsi cihazlar fərqli yük yaradır. İlkin ərazi ölçməsi (site survey) əhatəni, maneələri və kanal istifadəsini öyrənir. Quraşdırmadan sonra real cihazlarla təkrar ölçmə aparılır. Boş binada yaxşı siqnal görünməsi dolu auditoriyada kifayət qədər tutum olduğunu göstərmir.

:::example
Şərti amfiteatrda 180 tələbənin hər birinə orta 1 Mbit/s tətbiq yükü planlaşdırılsın: cəmi 180 Mbit/s tətbiq yükü alınır. Bu rəqəm radionun elan olunan fiziki sürəti ilə birbaşa müqayisə edilmir, çünki mühit paylaşılır, protokol əlavələri və təkrar ötürmələr var, müştərilər müxtəlif sürətlərlə işləyir. AP sayı və kanal planı ölçmə ilə seçilir. Hesab ilkin tutum sualını qoyur, hazır avadanlıq sifarişi vermir.
:::

Həddən artıq əhatə qonşu hüceyrələrin müdaxiləsini və gecikmiş keçidləri artıra bilər. Kanal eni də yerli sıxlığa görə seçilir; daha geniş kanal hər məkanda daha yaxşı nəticə vermir. Tezlik və ötürmə gücü yerli radio qaydalarına uyğun qurulur.

### Məntiqi seqmentasiya

SSID adlarını artırmaq öz-özünə izolyasiya yaratmır və radio idarəetmə yükünü böyüdə bilər. Universitet tələbə və əməkdaşları eyni Enterprise SSID-də fərdi rol ilə ayıra bilər; uyğunluq tələb edirsə ayrı SSID də seçilə bilər. Əsas tələb sessiyanın düzgün VLAN və ya rola düşməsi, sonra isə aradakı trafikin firewall ilə məhdudlaşdırılmasıdır. Rol təyinatının səhvi fiziki radio keyfiyyətindən asılı deyil.

:::figure
src = "m09-4.png"
alt = "Cihaz AP/kontrollerə qoşulur; RADIUS və NAC ilə rol mübadiləsi gedir; AP rol üzrə VLAN-lara (tələbə, əməkdaş, qonaq, IoT) yönəldir; əməkdaş seqmentindən trafik firewall-dan keçərək LMS, maliyyə və internetə çatır."
caption = "Kampusda AAA xidməti, rol üzrə seqmentlər və daxili resurslara nəzarət."
wide = true
:::

| Mənbə rolu | LMS HTTPS | Kitabxana xidməti | Tələbə bazası idarəsi | İnternet |
| --- | --- | --- | --- | --- |
| Tələbə | İcazə | İcazə | Qadağa | Siyasətlə icazə |
| Əməkdaş | İcazə | İcazə | Yalnız səlahiyyətli rol | Siyasətlə icazə |
| Qonaq | İctimai hissə | İctimai hissə | Qadağa | İcazə |
| IoT | Qadağa | Yalnız tələb olunan xidmət | Qadağa | Zərurətə görə |
| Karantin | Dəstək səhifəsi | Qadağa | Qadağa | Yeniləmə ünvanları |

İnternetdə yayımlanan LMS qonağa açıq ola bilər, amma daxili inzibati interfeys ayrıca bağlanmalıdır. IPv4 üçün bağlanan yolun IPv6 ilə açıq qalmadığı da sınanır. AP-də müştəri izolyasiyası ilə firewall qaydası birlikdə işlədilir; DNS, DHCP və vaxt xidmətləri hər rolun ehtiyacına uyğun buraxılır.

Printer yalnız çap xidmətinin lazım olan istiqamətlərini qəbul edir. Sertifikat dəstəkləməyən cihaz üçün ayrıca sirr istifadə edilirsə onun sahibi, yenilənmə müddəti və istisnanın bitmə tarixi yazılır. Köhnə cihaz üçün zəif rejimi bütün əməkdaş SSID-sində açmaq əvəzinə məhdud istisna seqmenti yaradılır və dəyişdirmə planı qoyulur.

### İdarəetmə və dayanıqlılıq

AP, kontroller və RADIUS idarəetməsi ayrıca idarəetmə seqmentində yerləşdirilir. Standart administrator parolları dəyişdirilir, uzaq idarəetmə yalnız səlahiyyətli idarəetmə yolundan açılır. Ehtiyat konfiqurasiyalar qorunur, çünki orada RADIUS sirləri və başqa həssas məlumat ola bilər. Yeniləmə əvvəl pilot AP-də yoxlanır, sonra xidmət pəncərəsində mərhələli yayılır.

Kontrollerin birinci server susanda digərinə keçməsi real sınaqla yoxlanır. Hər iki server eyni kimlik və sertifikat siyasətini tətbiq etməlidir; ehtiyat serverdə ləğv yoxlamasının unudulması təhlükəsizlik boşluğu yaradar.

Universitet məhdud fövqəladə rabitə planı hazırlayır: kritik əməkdaş üçün kabel yolu, əvvəlcədən təsdiqlənmiş alternativ və xidmət statusu bildirişi. Belə qərar insident zamanı tələsik server yoxlamasını söndürməklə əvəz edilmir; ehtiyat mexanizminin səlahiyyət həddi əvvəlcədən müəyyən olunur.

## Monitorinq, miqrasiya və qəbul sınaqları

### Qeydlərin əlaqələndirilməsi

RADIUS qeydi kimlik cəhdini, kontroller qeydi radio sessiyasını, DHCP qeydi həmin vaxt verilmiş IP ünvanını göstərir. Bu mənbələrdə saatlar uyğunlaşdırılır və zaman qurşağı aydın saxlanılır. Tək MAC ünvanı ilə bütün həftənin fəaliyyətini bir tələbəyə aid etmək olmaz: ünvan dəyişməsi, cihaz paylaşılması və sessiyaların təkrar qurulması nəzərə alınır.

Aşağıdakı sətirlər istehsalçı formatını təqlid etməyən şərti, normallaşdırılmış jurnal nümunəsidir; vaxt, cihaz identifikatoru və sessiya nömrəsi şərtidir. Son sətir uğurlu autentifikasiyadan sonra məlumat yolunun ayrıca işlədiyini göstərir.

```
2026-11-08T08:10:01Z nas=wlc01 session=s042 eap=TLS result=accept identity=device-042 role=staff vlan=20
2026-11-08T08:10:02Z session=s042 key_exchange=complete
2026-11-08T08:10:03Z session=s042 dhcp=10.20.0.42
```

SIEM-də çoxsaylı uğursuz cəhd, gözlənilməyən EAP üsulu və sertifikat xətalarının artması izlənilə bilər. Ancaq hamının istifadə etdiyi bir kontroller IP-si üzrə hesab kilidləmək bütün kampusu dayandıra bilər. Müştəri sessiyası, kimlik, cihaz və səbəb kodu birlikdə araşdırılır. Sertifikat bitmə dalğası ilə parol hücumu eyni xəbərdarlıq kimi işlənməməlidir.

| Əlamət | Əvvəl yoxlanan hissə | Tələsik verilməməli qərar |
| --- | --- | --- |
| SSID görünmür | Radio, kanal və AP vəziyyəti | İstifadəçi parolunu dəyişmək |
| Server sertifikatı rədd edilir | Ad, CA zənciri və vaxt | Yoxlamanı söndürmək |
| RADIUS cavabı yoxdur | Marşrut, firewall və server | Bütün sorğuları internetə açmaq |
| Access-Reject gəlir | EAP və avtorizasiya səbəbi | İstənilən sertifikatı qəbul etmək |
| Accept var, IP yoxdur | Açar mərhələsi, VLAN və DHCP | Autentifikasiyanı təkrar zəiflətmək |
| IP var, LMS açılmır | DNS, firewall və tətbiq | AP-ni dərhal nasaz elan etmək |

Kimlik və məkan əlaqəsi şəxsi məlumat riski yaradır: saxlanma müddəti məqsədə görə seçilir, giriş məhdudlaşdırılır. Təhlükəsizlik araşdırması üçün tələb olunan məlumatla tələbənin bütün hərəkətini uzunmüddətli izləmək fərqli məqsədlərdir; məxfilik siyasəti texniki toplama qaydalarına çevrilməlidir.

### Ortaq paroldan Enterprise rejiminə keçid

Şərti başlanğıcda bütün kampus vahid PSK ilə işləyir. Komanda əvvəl cihaz və istifadəçi qruplarını inventarlaşdırır, dəstəklənən EAP üsullarını müəyyən edir. Sonra RADIUS, PKI və profil paylanması sınaq mühitində qurulur. Kafedranın kiçik pilot qrupu ilə düzgün qoşulma, yanlış sertifikatın rəddi və ləğv sınaqları aparılır. İstisna IoT cihazları ayrıca plana daxil edilir.

Köhnə PSK şəbəkəsinin qalma müddəti əvvəlcədən məhdudlaşdırılır, əks halda hamı rahat köhnə yolda qala bilər. Dəstək təlimatı platformaya görə hazırlanır, rəsmi profilin ünvanı bildirilir. Tələbəyə sertifikat xəbərdarlığını keçmək təlimatı verilmir. Köhnə şəbəkə bağlananda inventardakı bütün vacib cihazların alternativ yolu təsdiqlənir.

### Ölçülə bilən qəbul meyarları

Qəbul sınağı həm düzgün istifadəçinin işini, həm də yanlış kimliyin rəddini yoxlayır. Şərti sınaq planında idarə olunan noutbuk, şəxsi telefon və məhdud imkanlı cihaz ayrı qruplardır. Müsbət sınaq yalnız uğurlu EAP cavabında dayanmır: IP alınır, LMS açılır, qadağan edilmiş resursa girişin bağlandığı göstərilir. Mənfi sınaq üçün yalnız nəzarət olunan laboratoriya AP-si işlədilir.

| Sınaq | Gözlənilən nəticə | Sübut |
| --- | --- | --- |
| Düzgün EAP-TLS profili | Uyğun rol və xidmət çıxışı | AAA və kontroller qeydi |
| Yanlış server adı | Kimlik mübadiləsi dayandırılır | Müştəri sertifikat xətası |
| Ləğv edilmiş sertifikat | Növbəti tam giriş rədd edilir | RADIUS ləğv nəticəsi |
| Aktiv sessiyanın ləğvi | Cihazın cari çıxışı dayanır | Kontroller və trafik yoxlaması |
| Qonaqdan daxili resursa cəhd | Firewall bloklayır | Qayda qeydi |
| Əsas RADIUS dayanması | Ehtiyat server siyasəti saxlayır | Keçid vaxtı və server qeydi |
| Sensorun susması | Sağlamlıq xəbərdarlığı yaranır | Monitorinq hadisəsi |
| Auditoriyanın dolu yükü | Tələb olunan xidmət işləyir | Gecikmə, itki və uğurlu sessiyalar |

Uğurlu autentifikasiya faizi, mərhələ üzrə uğursuzluq səbəbləri, ehtiyat serverə keçid vaxtı və profil dəstəyi müraciətləri ölçülür. Hədlər yerli xidmət tələbinə görə seçilir; ölçülməmiş rəqəm norma elan edilmir. Sertifikat ləğvindən yeni girişin rəddinə qədər müddət və aktiv sessiyanın kəsilmə müddəti ayrı ölçülür. Belə sınaq təhlükəsizlik siyasətinin real şəbəkədə işlədiyini göstərir.

:::tip Kampus Wi-Fi yoxlama siyahısı (konspekt)
- Ayrı SSID və VLAN-lar: əməkdaş, tələbə, qonaq, IoT (kameralar, printerlər). Ayrı SSID kifayət deyil, VLAN-lar arasında firewall qaydası olmalıdır.
- Əməkdaş və tələbə üçün WPA2/WPA3-Enterprise; qonaq üçün OWE və ya captive portal + müştəri izolyasiyası.
- PMF aktiv, WPS söndürülmüş, köhnə rejimlər (WEP, TKIP) bağlı.
- AP və kontrollerlərin proqramı yenilənir, standart admin parolları dəyişdirilib, idarəetmə interfeysi ayrıca idarəetmə VLAN-ındadır.
- WIDS/WIPS ilə rogue və evil twin AP-lərin axtarışı; uğursuz autentifikasiyaların loglanması və SIEM-ə göndərilməsi.
- Radio planlaşdırma (site survey): siqnal binadan kənara lazımsız çıxmasın, kanallar üst-üstə düşməsin.
:::

:::note Köhnə slaydlarla fərq
Konspektə görə mühazirədə ciddi faktiki səhv yoxdur; iki yer dəqiqləşdirilir. Birincisi, PMK WPA2-Personal-da paroldan alınır, WPA3-Personal-da SAE mübadiləsi nəticəsində yaranır; hər iki rejimdə bundan sonra seans açarları üçün 4 addımlı əl sıxması aparılır. İkincisi, "sertifikat ləğv edilir" dedikdə RADIUS serveri ləğvi həqiqətən yoxlamalıdır (CRL/OCSP), aktiv sessiya isə ayrıca kəsilməlidir.
:::
