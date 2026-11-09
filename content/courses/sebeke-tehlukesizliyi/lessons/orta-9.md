+++
title = "Simsiz autentifikasiya və simsiz rabitənin təhlükəsizliyi"
unit = "orta"
order = 9
summary = "Hər anlayış 1–3 cümlə ilə izah olunur: 802.1X axını, EAP üsullarının seçimi, sertifikat yoxlaması, RADIUS və Blast-RADIUS, eduroam, simsiz hücumlar, WIDS/WIPS, Bluetooth, BYOD/MDM və kampus layihəsi."
updated = 2026-11-09

[[source]]
title = "Mühazirə 9: Simsiz autentifikasiya və simsiz rabitənin təhlükəsizliyi"
note = "Elmar Cabbarov, 2026–2027"
+++

Simsiz şəbəkədə əsas sual belədir: kimin şəbəkəyə buraxılacağına necə qərar veririk və bu qərarı necə yoxlayırıq? Mövzu ortaq paroldan fərdi sertifikata qədər autentifikasiya üsullarını, simsiz hücumları və kampus layihəsini əhatə edir. Universitet topologiyası, ünvanlar və VLAN nömrələri şərti tədris nümunəsidir.

## Simsiz rabitədə təhlükəsizlik sərhədi

Simsiz rabitə məlumatın elektromaqnit dalğaları ilə ötürülməsidir. Simsiz lokal şəbəkədə (wireless local area network, WLAN) cihazlar giriş nöqtəsinə (access point, AP) qoşulur. Wi-Fi kampus daxilində, Bluetooth qısa məsafədə, mobil rabitə isə operatorun şəbəkəsində işləyir; bunların kimlik yoxlaması eyni deyil. SIM kartla operatora tanınmaq universitetin tələbə bazasına giriş hüququ vermir.

Kitabxananın qarşısındakı şəxs binaya girmədən Wi-Fi kadrlarını qəbul edə bilər; radio sərhədi bina sərhədi ilə üst-üstə düşmür.

- **SSID** (service set identifier) şəbəkə adıdır. **BSSID** (basic service set identifier) konkret radio xidmət dəstinin identifikatorudur, adətən MAC ünvanı formasındadır.
- Bir SSID çox AP-də yayıla bilər, ona görə nə SSID, nə BSSID universitetə məxsusluğu kriptoqrafik sübut etmir. Hücumçu UNI-Student adını yayımlaya bilər.

Təhlükəsizlik tələbləri: məxfilik, bütövlük, əlçatanlıq; simsizdə qarşılıqlı autentifikasiya, avtorizasiya və izlənə bilmə də əlavə olunur. Autentifikasiya kimliyin yoxlanmasıdır, avtorizasiya həmin kimliyə verilən hüquqdur, istifadə uçotu (accounting) sessiyanın qeydidir; üçü birlikdə **AAA** adlanır. Wi-Fi autentifikasiyası tələbə bazasının administratoru olmaq demək deyil, bazaya girişdə tətbiq ayrıca yoxlayır. Radio şifrələməsi də HTTPS-i əvəz etmir: paket AP-dən sonra başqa şəbəkələrdən keçir.

:::warning
Cihaz kimliyi insan kimliyi deyil. Kafedra noutbukunun sertifikatı noutbuku tanıdır, klaviaturada kimin oturduğunu yox.
:::

## Giriş rejiminin seçilməsi

**Personal** rejimində hamı ortaq parolu bilir: WPA2-Personal əvvəlcədən paylaşılmış açar (pre-shared key, PSK), WPA3-Personal isə SAE mübadiləsi işlədir. Semestr bitəndə parolu kimlərin saxladığı bilinmir; parol dəyişəndə bütün cihazlara müdaxilə lazımdır. Vahid PSK şəbəkəsində MAC bloklaması bir istifadəçinin sirrini etibarlı ləğv etmir.

**Enterprise** rejimində hər şəxsə və ya cihaza ayrı kimlik verilir: hesab və parol, yaxud sertifikat və şəxsi açar. İtən cihazın kimliyi ləğv edilir, qalanlar işləyir. Əvəzində AAA serverləri, sertifikat infrastrukturu (PKI) və dəstək işlək saxlanmalıdır.

| Meyar | Ortaq parollu Personal | Fərdi kimlikli Enterprise |
| --- | --- | --- |
| Giriş məlumatı | Qrupun bildiyi sirr | Hesab və ya cihaz sertifikatı |
| Bir cihazı çıxarmaq | Ümumi parol dəyişikliyi | Həmin kimlik və sessiya ləğv edilir |
| Hüquqlar | SSID üzrə ümumi qayda | Kimlik və qrup üzrə rol |
| İzləmə | Hesab kimliyi bilinmir | Kimlik sessiya ilə əlaqələnir |
| Yük | İlkin quruluş sadə | AAA, profil, kimlik həyat dövrü |
| Nümunə | Məhdud laboratoriya cihazı | Əməkdaş və tələbə cihazları |

**Enterprise sərhədləri.** WPA2-Enterprise IEEE 802.1X və EAP ilə yoxlayır; məlumatı AES əsaslı CCMP qoruyur (AES alqoritm, CCMP mexanizmdir). WEP və TKIP qəbul edilmir. WPA3-Enterprise də 802.1X/EAP əsaslıdır, qorunan idarəetmə kadrları (protected management frames, PMF) tələb edir və 192 bit rejimi var; WPA3 yazısı avtomatik həmin rejim demək deyil, uyğunluq yoxlanır.

Fürsətçi şifrələmə (opportunistic wireless encryption, OWE) açıq şəbəkədə passiv dinləməyə qarşı radio kanalını parolsuz şifrələyir, amma AP sahibini autentifikasiya etmir: qonaq saxta AP-yə də qoşula bilər. Qonaq şəbəkəsində HTTPS və daxili resurslardan izolyasiya yenə lazımdır.

## IEEE 802.1X: rollar və mesaj axını

IEEE 802.1X port əsaslı giriş nəzarətidir. Autentifikasiyaya qədər idarə olunan port bağlıdır və yalnız EAP trafiki keçir.

| Rol | Nümunə | Vəzifə |
| --- | --- | --- |
| Supplicant | Tələbənin telefonu | 802.1X müştərisi; serverin etibar zəncirini və adını yoxlayır |
| Authenticator | AP və ya kontroller | EAP-ı ötürür, nəticəni sessiyaya tətbiq edir, açarları, VLAN və rolu idarə edir |
| Autentifikasiya serveri | FreeRADIUS və s. | EAP üsulunu tamamlayır, qərar verir |

Müştəri ilə autentifikator arasında EAP over LAN (EAPOL) işləyir və əvvəlcədən IP tələb etmir. Autentifikatorla RADIUS arasında EAP mesajı RADIUS atributlarında daşınır. Yəni eyni EAP söhbəti iki fərqli nəqliyyatdan keçir.

:::figure
src = "m09-1.png"
alt = "Cihaz, AP (authenticator) və RADIUS arasında EAPOL-Start, Identity mübadiləsi, Access-Request, EAP-TLS və ya PEAP mübadiləsi, Access-Accept ilə açar materialı, EAP-Success, 4 addımlı əl sıxma və şifrəli trafikin ardıcıllığı."
caption = "Enterprise qoşulmasının ardıcıllığı."
wide = true
:::

:::reveal Access-Accept göründü, amma telefon IP ala bilmir. Niyə?
Access-Accept yalnız EAP mərhələsinin bitdiyini göstərir. Sonra kontroller qəbulu düzgün sessiyaya bağlamalı, dörd addımlı açar razılaşdırması tamamlanmalı, təyin olunan VLAN AP və kommutatorda mövcud olmalıdır; DHCP, DNS və firewall da ayrıca işləməlidir. Diaqnostika uğurun dayandığı mərhələdən davam edir, server sertifikatı yoxlamasını söndürmək isə problemi həll etmir.
:::

**Addımlar.** Noutbuk AP ilə ilkin 802.11 qoşulmasını qurur (Open System authentication istifadəçi yoxlaması deyil). Port bağlı qalır, yalnız EAPOL keçir. Autentifikator EAP-Request/Identity göndərir, müştəri cavab verir (EAPOL-Start məcburi deyil). Kontroller kimliyi Access-Request daxilində RADIUS-a ötürür. Server üsul təklif edir, Access-Challenge ilə mübadilə davam edir. Nəticə Access-Accept və ya Access-Reject olur. Uğurlu EAP açar materialı yaradır, sonra dörd addımlı açar razılaşdırması gəlir və adi trafik açılır; cihaz VLAN-da DHCP ilə IP alır.

EAP-ın baş sessiya açarı (master session key, MSK) paketi qoruyan seans açarı deyil: MSK-dən cüt baş açar (pairwise master key, PMK) materialı alınır, dörd addımlı razılaşdırma konkret rabitənin açarlarını yaradır. Sessiya müddəti, yenidən autentifikasiya və aktiv bağlantının kəsilməsi ayrı parametrlərdir: sertifikat ləğvindən sonra sessiya kontrollerdə ayrıca dayandırılmalıdır.

## EAP üsulları və seçimin əsaslandırılması

Genişləndirilə bilən autentifikasiya protokolu (Extensible Authentication Protocol, EAP) mesaj çərçivəsidir; özü nə sertifikat, nə parol, nə də güclü qarşılıqlı autentifikasiya vəd edir. Üsulun xüsusiyyətləri, cihaz dəstəyi və server siyasəti birlikdə qiymətləndirilir.

| Üsul | Serveri necə tanıdır | Müştərini necə tanıdır | Risk |
| --- | --- | --- | --- |
| EAP-TLS | Server sertifikatı | Müştəri sertifikatı və şəxsi açar | PKI lazımdır; açar qorunmalıdır |
| PEAP-MSCHAPv2 | Xarici TLS tunelində sertifikat | Tuneldə parol əsaslı challenge-response | Yanlış serverə cavab parol riskidir |
| EAP-TTLS | Xarici TLS tunelində sertifikat | Tuneldə seçilən daxili üsul | Daxili üsul və kataloq uyğunluğu |
| EAP-MD5 | Qarşılıqlı yoxlama yoxdur | Sadə challenge-response | Enterprise Wi-Fi üçün uyğun deyil |
| LEAP | Köhnə parol yanaşması | Parol törəmələri | İstifadədən çıxarılmalıdır |

**EAP-TLS.** TLS əsasında qarşılıqlı sertifikat autentifikasiyası. Etibarlı sertifikat sertifikatlaşdırma mərkəzinin (certificate authority, CA) imzasını daşıyır; sertifikatı görmək kifayət deyil, uyğun şəxsi açarla sübut tələb olunur. Noutbuk əvvəl serverin zəncirini, adını və məqsədini yoxlayır, sonra server müştəri sertifikatını yoxlayır. RADIUS sertifikatı kataloqdakı aktiv qeydlə əlaqələndirir və rolu seçir. 

**PEAP-MSCHAPv2.** Qorunan EAP (Protected EAP, PEAP) server sertifikatı ilə TLS tuneli qurur, içində MSCHAPv2 paroldan törəyən challenge-response ötürür; parol adi mətn getmir. Cihaz server sertifikatını yoxlamırsa, hücumçu öz serveri ilə tunel qurub parol törəmələrini sındıra bilər. Wi-Fi və LMS üçün eyni parol təhlükənin dairəsini böyüdür.

**EAP-TTLS.** Server sertifikatı ilə qorunan xarici kanalda PAP, CHAP, MSCHAPv2 və ya EAP işləyir; daxili üsul sənəddə göstərilməlidir. TTLS-PAP-də parolun özü tunel daxilində serverə gedir: saxta serverə etibar edilərsə parol sızır, PEAP-MSCHAPv2-də isə challenge-response materialı. 

**TEAP.** Tunelli EAP (Tunnel Extensible Authentication Protocol, TEAP) TLS tunelində cihazın və istifadəçinin ardıcıl yoxlanmasını dəstəkləyir. Kriptoqrafik bağlama (crypto-binding) daxili autentifikasiyanın açar materialını xarici tunellə əlaqələndirir; beləliklə siyasət həm cihaz, həm istifadəçi tələb edə bilər. Server sertifikatı yoxlanması saxlanılır.

## Sertifikat yoxlaması və kimliyin həyat dövrü

Server sertifikatının yoxlanması ayrı suallardan ibarətdir və biri digərini əvəz etmir.

| Nəzarət | Yoxlanan | Səhv nümunəsi |
| --- | --- | --- |
| Etibar zənciri | Kök və aralıq CA imzaları | Təsadüfi kök CA quraşdırılıb |
| Server adı | Profildəki ad ilə SAN | Başqa xidmətin sertifikatı qəbul edilir |
| Vaxt | Başlama və bitmə | Telefonun saatı yanlışdır |
| Məqsəd | Açar istifadəsi və EKU | Uyğunsuz sertifikat |
| Ləğv | CRL və ya OCSP | Oğurlanmış cihaz hələ qəbul edilir |
| Açara sahiblik | Şəxsi açar sübutu | Yalnız fayl köçürülüb |

Profil yalnız ictimai CA-ya etibar edib adı məhdudlaşdırmırsa, başqa təşkilatın düzgün sertifikatı da qəbul edilə bilər; gözlənilən ad (məsələn, radius.wifi.uni.example) açıq müəyyən edilir. İstifadəçinin xəbərdarlığı əl ilə qəbul etməsi nəzarət sayılmır.

Ləğv siyahısı (certificate revocation list, CRL) ləğv olunmuş sertifikatları göstərir; onlayn sertifikat status protokolu (OCSP) konkret sertifikatın statusunu soruşur. Server müştəri ləğvini həqiqətən yoxlamalıdır: PKI-də düyməni basmaq RADIUS keşinin yeniləndiyini göstərmir. 



İlkin qeydiyyat (onboarding) həssas mərhələdir: profil və CA təsadüfi açıq portaldan yox, yoxlanmış HTTPS ünvanı, idarə olunan cihaz sistemi və ya nəzarətli kanaldan alınır. Əməkdaş ayrıldıqda hesab, sertifikat, RADIUS siyasəti və aktiv sessiyalar bir iş axınında bağlanır; yenilənə bilməyən sertifikat üçün server yoxlamasını söndürən müvəqqəti təlimat verilmir.

## RADIUS xidməti və konfiqurasiya məntiqi

RADIUS giriş qərarını və uçot məlumatını şəbəkə cihazı ilə AAA xidməti arasında daşıyır. RADIUS müştərisi telefon deyil, sorğunu göndərən AP və ya kontrollerdir; server yalnız qeydiyyatlı cihazlardan sorğu qəbul edir. Telefonun sertifikatı ilə kontrollerin RADIUS sirri müxtəlif tərəfləri tanıyır.

Ənənəvi RADIUS autentifikasiya üçün UDP 1812, uçot üçün UDP 1813 işlədir. Access-Request-ə Access-Challenge, Access-Accept və ya Access-Reject cavab verir; uçotda Accounting-Request və Accounting-Response var. Paket tam şifrələnmir, atributların bir hissəsi açıq görünür.

| Atribut | Mənası |
| --- | --- |
| User-Name | Təqdim olunan kimlik (anonim ola bilər) |
| NAS-IP-Address | Giriş cihazının ünvanı |
| Calling-Station-Id | Adətən müştərinin MAC ünvanı; insan kimliyi deyil |
| Called-Station-Id | AP və SSID məlumatı |
| EAP-Message | EAP mesajının daşınması |
| Message-Authenticator | Mesajın bütövlük yoxlaması |
| Tunnel-Private-Group-Id | Dinamik VLAN |
| Acct-Session-Id | Uçot sessiyasının identifikatoru |

RADIUS-un qaytardığı rol tətbiq olunmalıdır: əməkdaşa VLAN 20, tələbəyə VLAN 10 (şərti). VLAN kontrollerdə tanınmırsa cihaz giriş almır və ya səhv seqmentə düşür; RADIUS atributu firewall qaydasını yaratmır.

FreeRADIUS-da: `clients.conf` hər kontrollerə ayrı, uzun, təsadüfi sirr və `require_message_authenticator` verir, RADIUS portuna yalnız idarəetmə şəbəkəsindən yol açılır. EAP modulunda `server-chain.pem` serverin zəncirini, `client-ca.pem` müştərilərə etibar mənbəyini göstərir (eyni şey deyil); `check_crl` təkbaşına ləğv xidməti yaratmır. Avtorizasiyada sertifikat aktiv inventar və qrupla bağlanmalıdır, VLAN cavabı yalnız uyğun rola verilir. `radiusd -XC` yalnız sintaksisi yoxlayır; `radtest` tam EAP sınağı deyil, `eapol_test` və real radio sınağı lazımdır, mənfi sınaqlarla birlikdə.

## RADIUS nəqliyyatının qorunması

**Blast-RADIUS** (CVE-2024-3596) ənənəvi RADIUS-un kriptoqrafik quruluşundakı zəifliyə əsaslanır: şəbəkə yolunda hücumçu MD5 toqquşması ilə cavabın mənasını dəyişməyə çalışa bilər. Bu, Wi-Fi parolunun radio ilə təxmini deyil. EAP paketlərində Message-Authenticator tələbi və yoxlaması qoruyucu sərhəddir; bütün 802.1X quruluşları eyni dərəcədə açıq deyil, hər RADIUS istifadə yolu ayrıca araşdırılır. Tədbir: server və kontrollerin düzəlişli versiyası, Message-Authenticator tələbi, köhnə cihazlar üçün yenilənmə və məhdudlaşdırma. Uzun ortaq sirr zəifliyin düzəlişini əvəz etmir.

**RadSec** RADIUS-un TLS üzərindən daşınmasıdır (RFC 6614, standart port TCP 2083). TLS RADIUS tərəfləri arasında məxfilik və bütövlük verir; server adı, icazəli CA-lar və yenilənmə yenə lazımdır. RadSec-in TLS-i EAP-TLS-in TLS-indən ayrıdır, proksi bir RadSec bağlantısını bitirib növbəti proksiyə ayrı bağlantı qura bilər.

| Meyar | EAP-TLS | RadSec |
| --- | --- | --- |
| Tərəflər | Supplicant və EAP serveri | RADIUS müştərisi, proksi, server |
| Vəzifə | Girən kimliyi yoxlamaq | RADIUS nəqliyyatını qorumaq |
| Əvəz etmədiyi | VLAN və tətbiq səlahiyyəti | Müştəridə EAP server sertifikatı yoxlaması |

## eduroam federasiyası

eduroam iştirakçı təhsil və tədqiqat təşkilatlarında istifadəçinin öz təşkilatının kimliyi ilə qoşulmasına imkan verir. Qonaq kampus radio xidməti verir və yerli qaydaları tətbiq edir, kimliyi isə ev təşkilatı yoxlayır. Şərti ayla@uni.example kimliyində `uni.example` realm adlanır və sorğunun marşrutunu göstərir; qonaq RADIUS sorğunu federasiya proksiləri ilə ev serverinə ötürür.

:::figure
src = "m09-3.png"
alt = "Cihaz qonaq kampus AP-sinə, qonaq RADIUS-a, federasiya proksilərinə və ev universitetinin RADIUS-una qoşulur; cihazla ev EAP serveri arasında TLS kanalı göstərilir, marşrut realm hissəsinə görə seçilir."
caption = "EAP sorğusunun qonaq kampusdan ev universitetinə ötürülməsi."
wide = true
:::

Düzgün tunelli EAP-də daxili kimlik ev serverinə qədər qorunur, amma proksilər marşrut atributlarını, xarici kimliyi və bəzi metadata görə bilər. Etibarlı server adı qonaq kampusun yox, ev təşkilatının profilində olan addır; profil CAT və ya geteduroam ilə verilir, saxta saytdan yüklənmiş profil etimadı həll etmir. Öz kampusunda qoşulub səfərdə qoşulmayan tələbə üçün realm səhvi, federasiya marşrutu, RADIUS nəqliyyatı və qonaq siyasəti yoxlanır. eduroam uğuru tətbiq səlahiyyəti vermir; ev təşkilatı hesabı bağlasa da, qurulmuş sessiya ayrıca kəsilməlidir.

## MAC filtrləməsi, gizli SSID və captive portal

- **MAC filtri** yalnız siyahıdakı ünvanlara icazə verir. MAC kimlik sübutu deyil, müşahidə edilir və dəyişdirilə bilər. 
- **Gizli SSID** adı beacon-da yaymır; qoşulma və aktiv axtarışlar adı yenə göstərə bilər. Kriptoqrafik nəzarət deyil.
- **Captive portal** brauzerdə qeydiyyat və ya şərtlərin qəbulu səhifəsidir; radio kadrlarını şifrələmir, AP kimliyini sübut etmir. Əməkdaş parolu qonaq portalında yığılmır.
- **Müştəri izolyasiyası** başqa AP-dəki və ya kabeldəki müştəriyə yolu bağlamaya bilər, ona görə qonaq VLAN-ından daxili ünvanlara firewall qaydası saxlanır.

## Simsiz hücumlar və qarşı tədbirlər

**Evil twin** etibarlı şəbəkənin adını və görünüşünü təqlid edir; güclü siqnal, tanış SSID və loqo etibar sübutu deyil. Əsas tədbir: server sertifikatının yoxlanması və idarə olunan profil.

**Rogue AP** təşkilatın razılığı olmadan infrastruktura qoşulmuş AP-dir (məsələn, əməkdaşın şəxsi routeri); məqsəd zərərli olmasa da kabel şəbəkəsinə nəzarətsiz radio yolu açır. Tədbir: radio inventarını kabel portu uçotu ilə birləşdirmək, boş rozetkaları bağlamaq, kabel portlarında 802.1X və şəbəkəyə girişə nəzarət (network access control, NAC). Bir cihaz həm rogue, həm evil twin ola bilər.

| Təhdid | Risk | Tədbir və məhdudiyyət |
| --- | --- | --- |
| Passiv dinləmə | Metadata (vaxt, ölçü) görünür | Şifrələmə məzmunu qoruyur; HTTPS lazımdır |
| Saxta ayırma (deauth) kadrları | Sessiya qırılır | PMF; bütün DoS hallarını bağlamır |
| Radio basdırma (jamming) | Kanal yararsızdır | Spektr araşdırması, kabel ehtiyatı; PMF kömək etmir |
| Parol təxmini | Personal və zəif EAP | Güclü sirr, uyğun üsul, cəhd monitorinqi |
| WPS | Sadələşdirilmiş qeydiyyat zəifliyi | Söndürmək |
| KRACK sinfi proqram səhvi | Açar və idarəetmə pozulur | Müştəri, AP, kontroller yenilənir; parolu dəyişmək kömək etmir |
| War driving | SSID və əhatə xəritələnir | Adı gizlətmək maneə deyil; icazəli yoxlama yazılı sərhədlə |



## WIDS/WIPS və icazəsiz AP ilə işləmə

Simsiz müdaxilə aşkarlama sistemi (wireless intrusion detection system, WIDS) radio mühitində şübhəli vəziyyəti tapıb xəbərdarlıq verir; simsiz müdaxilənin qarşısının alınması sistemi (wireless intrusion prevention system, WIPS) cavab əməliyyatları da təklif edir. Sensor inventarda olmayan BSSID-ni və fərqli təhlükəsizlik rejimli SSID-ni görür, amma naməlum AP qonşu mağazanın qanuni cihazı da ola bilər. Xəbərdarlıq yekun hökm deyil.

Hər birinin zəif tərəfi var (məsələn, sensor kabel portunu görmür).

:::reveal UNI-Staff adı yayan naməlum AP aşkarlandı. Ardıcıllıq nədir?
Əvvəl xəbərdarlığın vaxtı, yeri, kanalı və rejimi saxlanır və inventarda planlı dəyişiklik yoxlanır. Sonra radio məlumatı inventar və kontroller qeydləri ilə tutuşdurulur, bir neçə sensorla yer daraldılır və otaq fiziki təsdiqlənir. Kabel bağlantısı kommutator portları, MAC cədvəli və DHCP ilə araşdırılır. Universitetin portu tapılsa, səlahiyyətli komanda onu karantinə alır və ya bağlayır. Təsirlənmiş istifadəçilər, mümkün kimlik sızması qiymətləndirilir, sübut saxlanır, sahib və səbəb müəyyən edilir, port siyasəti düzəldilir. Radio ilə avtomatik ayırma qonşu şəbəkələrə təsir edə bilər, ona görə kabel portunu bağlamaq çox vaxt daha dəqiqdir.
:::

Xəbərdarlığın olmaması təhlükənin yoxluğunu sübut etmir; test AP-si ilə aşkarlama yolu yoxlanır.

## Bluetooth və mobil rabitənin təhlükəsizliyi

**Bluetooth.** Cütləşmə (pairing) zamanı cihazlar əlaqə açarı yaradır; sonrakı bağlantılar üçün açarların saxlanması bonding adlanır. Klassik Bluetooth ilə Bluetooth Low Energy təhlükəsizlik davranışına görə eyni deyil. Just Works üsulu şifrələmə yarada bilər, amma aradakı adam hücumuna qarşı autentifikasiya vermir. Daim cütləşmə rejimində qalan iclas otağı adapteri yaxınlıqdakı kənar cihaza açıqdır; quraşdırıcı onu fiziki nəzarətdə cütləşdirir və sonra imkanı məhdudlaşdırır. Cütləşmə və xidmət səlahiyyəti ayrıdır: səs qulaqcığına qoşulmaq kontakt və fayl paylaşmaq demək deyil. İtirilmiş cihazın cütləşmə qeydi silinir.

**Mobil rabitə.** SIM və ya eSIM abunə kimliyini operatora təqdim edir; bu, universitetdəki rolu təsdiqləmir, operator şifrələməsi də tətbiq yolunu ucdan-uca qorumur, HTTPS yenə yoxlanır. Köhnə 2G şəbəkənin cihaza autentifikasiyasında çatışmazlıqlara malikdir; yeni nəsillərdə aşağı nəsilə keçid və yanlış baza stansiyası riski qalır. SIM dəyişdirmə fırıldağında hücumçu nömrəni başqa SIM-ə keçirir; yalnız SMS-ə bağlı hesab bərpası riskdir, çoxamilli autentifikasiya bunu azaldır. 

## BYOD, MDM və cihaz vəziyyəti

Şəxsi cihazdan istifadə (bring your own device, BYOD) cihazın yenilənməsinə və disk qorumasına nəzarət olmaya bilər, ona görə giriş hüququ məhdud görünməyə uyğun seçilir. Mobil cihazların idarə edilməsi (mobile device management, MDM) profil, sertifikat və siyasət paylayır, cihaz vəziyyətini yoxlayır və idarə olunan məlumatı uzaqdan silir; EAP-TLS üçün məcburi deyil. 

NAC kimliklə yanaşı cihaz vəziyyətindən də istifadə edir: yenilənmiş idarə olunan noutbuk əməkdaş roluna, uyğunsuz cihaz bərpa seqmentinə yönəlir. Adi EAP-TLS sertifikatı antivirusun işlədiyini bildirmir. Zero Trust-da daxili şəbəkədə olmaq bütün xidmətlərə etibar üçün əsas deyil; Wi-Fi sessiyasını kəsmək tətbiq tokenini həmişə ləğv etmir.

| Cihaz sinfi | Kimlik və idarəetmə | İcazə sərhədi |
| --- | --- | --- |
| Universitet noutbuku | Ayrı sertifikat və MDM | Rol üzrə daxili xidmətlər |
| Şəxsi cihaz | Fərdi profil və qeydiyyat | Tədris xidmətləri və internet |
| Qonaq telefonu | Müddətli qonaq qeydiyyatı | Daxili resurs yoxdur |
| Uyğunsuz cihaz | Kimlik tanınır, vəziyyət pisdir | Bərpa və dəstək |
| Məhdud imkanlı IoT | İnventar və ayrıca sirr | Yalnız idarəetmə ünvanları |



## Kampus simsiz şəbəkəsinin layihəsi

**Radio planı və tutum.** Layihə cihaz sayından əvvəl istifadə ssenarilərindən başlayır. İlkin ərazi ölçməsi (site survey) əhatəni, maneələri və kanalları öyrənir, quraşdırmadan sonra real cihazlarla təkrarlanır. Boş binada yaxşı siqnal dolu auditoriyada tutumu göstərmir. Şərti amfiteatrda 180 tələbə × 1 Mbit/s = 180 Mbit/s tətbiq yükü alınır; bu rəqəm radionun elan olunan fiziki sürəti ilə birbaşa müqayisə olunmur (mühit paylaşılır, əlavə yük və təkrar ötürmə var), AP sayı ölçmə ilə seçilir. 

**Seqmentasiya.** SSID sayını artırmaq izolyasiya yaratmır; əsas olan sessiyanın düzgün VLAN və ya rola düşməsi və aradakı trafikin firewall ilə məhdudlaşdırılmasıdır. Rol təyinatı radio keyfiyyətindən asılı deyil.

| Rol | LMS HTTPS | Kitabxana | Tələbə bazası idarəsi | İnternet |
| --- | --- | --- | --- | --- |
| Tələbə | İcazə | İcazə | Qadağa | Siyasətlə |
| Əməkdaş | İcazə | İcazə | Yalnız səlahiyyətli rol | Siyasətlə |
| Qonaq | İctimai hissə | İctimai hissə | Qadağa | İcazə |
| IoT | Qadağa | Yalnız lazım olan | Qadağa | Zərurətə görə |
| Karantin | Dəstək səhifəsi | Qadağa | Qadağa | Yeniləmə ünvanları |



**İdarəetmə və dayanıqlılıq.** AP, kontroller və RADIUS ayrıca idarəetmə seqmentindədir; standart admin parolları dəyişdirilir, ehtiyat konfiqurasiya qorunur (içində RADIUS sirləri ola bilər), yeniləmə əvvəl pilotda yoxlanır. İki RADIUS serveri eyni enerji, kataloq və ya ləğv xidmətindən asılıdırsa ortaq dayanma qalır; ehtiyat serverdə də ləğv yoxlaması və eyni siyasət olmalıdır. Autentifikasiya dayananda açıq şəbəkəyə avtomatik keçid olmamalıdır.

## Monitorinq, miqrasiya və qəbul sınaqları

RADIUS qeydi kimlik cəhdini, kontroller radio sessiyasını, DHCP verilən IP-ni göstərir; saatlar uyğunlaşdırılır, tək MAC ilə bütün həftəni bir tələbəyə aid etmək olmaz. SIEM-də uğursuz cəhd və sertifikat xətaları izlənir, amma ortaq kontroller IP-si üzrə kilidləmə kampusu dayandıra bilər; sertifikat bitmə dalğası ilə parol hücumu eyni xəbərdarlıq deyil. 

| Əlamət | Əvvəl yoxlanan | Tələsik verilməməli qərar |
| --- | --- | --- |
| SSID görünmür | Radio, kanal, AP | Parolu dəyişmək |
| Server sertifikatı rədd | Ad, CA zənciri, vaxt | Yoxlamanı söndürmək |
| RADIUS cavabı yoxdur | Marşrut, firewall, server | Sorğuları internetə açmaq |
| Access-Reject | EAP və avtorizasiya səbəbi | İstənilən sertifikatı qəbul etmək |
| Accept var, IP yoxdur | Açar mərhələsi, VLAN, DHCP | Autentifikasiyanı zəiflətmək |
| IP var, LMS açılmır | DNS, firewall, tətbiq | AP-ni nasaz elan etmək |

**Miqrasiya** (vahid PSK-dan Enterprise-a): cihaz və qrupların inventarı, dəstəklənən EAP üsulları, sınaq mühitində RADIUS, PKI və profil paylanması, kiçik pilot, korpus üzrə mərhələ, köhnə PSK-nın müddətli bağlanması, istisna IoT planı. Tələbəyə sertifikat xəbərdarlığını keçmək təlimatı verilmir.

**Qəbul sınağı** həm düzgün işi, həm yanlış kimliyin rəddini yoxlayır: düzgün EAP-TLS profili, yanlış server adı, ləğv edilmiş sertifikat, aktiv sessiyanın ləğvi, qonaqdan daxili resursa cəhd, əsas RADIUS dayanması, sensor susması və dolu auditoriya yükü. Ölçülən göstəricilər: uğurlu autentifikasiya faizi, mərhələ üzrə səbəblər, ehtiyat serverə keçid vaxtı, ləğvdən rəddə qədər müddət. 

:::exam
Üç tələ: MAC filtri və gizli SSID təhlükəsizlik vermir (MAC açıq görünür, ad probe sorğularında çıxır); Access-Accept internetin işlədiyini sübut etmir; sertifikat ləğvi aktiv sessiyanı avtomatik kəsmir, RADIUS CRL/OCSP-ni həqiqətən yoxlamalıdır.
:::
