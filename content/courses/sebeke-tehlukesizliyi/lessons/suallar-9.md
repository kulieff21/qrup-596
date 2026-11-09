+++
title = "Simsiz autentifikasiya və simsiz rabitənin təhlükəsizliyi"
unit = "suallar"
order = 9
summary = "İmtahan suallarına hazırlıq: mühazirənin bütün nəzarət sualları və situasiya tapşırıqları, konspektdən üç situasiya, ehtimal olunan əlavə suallar. Hər cavab əvvəlcə düşünüb sonra açmaq üçündür."
updated = 2026-11-09

[[source]]
title = "Mühazirə 9: Simsiz autentifikasiya və simsiz rabitənin təhlükəsizliyi"
note = "Elmar Cabbarov, 2026–2027"

[[source]]
title = "Midterm konspekti, Mövzu 9"
note = "Elmar Cabbarov"
+++

İmtahan yazılı açıq suallardan ibarətdir, ona görə cavabı əvvəlcə öz sözlərinlə yaz, sonra aç. Situasiya cavabında ardıcıllıq: aktiv, pozulan xassə, səbəb, tədbir, yoxlama. Universitet nümunələri şərti tədris nümunəsidir.

## Nəzarət sualları

:::reveal Radio əhatəsi ilə inzibati ərazi sərhədinin fərqi təhlükəsizlik planına necə təsir edir?
- Radio siqnalı divardan və pəncərədən kənara çıxır; kitabxananın qarşısındakı şəxs binaya girmədən Wi-Fi kadrlarını qəbul edə bilər.
- Kabel şəbəkəsində hücumçu əvvəl rozetkaya və ya aralıq cihaza çatmalıdır; radio sərhədi bina sərhədi ilə üst-üstə düşmür.
- Fiziki mühafizə yenə lazımdır, amma antena istiqaməti, güc və tikinti materialları autentifikasiyanı əvəz etmir.
- Nəticə: təhlükəsizlik planı radio sərhədinə güvənmir, kimlik yoxlaması, şifrələmə və seqmentasiya qurur.
:::

:::reveal SSID və BSSID hansı məlumatı verir, hansı kimlik sübutunu vermir?
- SSID (service set identifier) şəbəkə adıdır, istifadəçinin seçiminə kömək edir.
- BSSID (basic service set identifier) konkret radio xidmət dəstini tanıdır, adətən MAC ünvanı formasındadır.
- Bir SSID çox AP-də yayıla bilər, bir AP bir neçə SSID və BSSID verə bilər.
- Heç biri universitetə məxsusluğu kriptoqrafik sübut etmir: hücumçu UNI-Student adını yayımlaya bilər. Sübut Enterprise-da server sertifikatının yoxlanmasıdır.
:::

:::reveal Autentifikasiya, avtorizasiya və uçot universitet nümunəsində necə ayrılır?
- Autentifikasiya kimliyin yoxlanmasıdır (istifadəçi və server).
- Avtorizasiya həmin kimliyə verilən hüquqdur (məsələn, tələbə seqmentindən maliyyə xidmətinə yol bağlıdır).
- Uçot (accounting) sessiyanın başlanması, bitməsi və istifadə göstəricilərinin qeydidir. Üçü birlikdə AAA adlanır.
- Uğurlu Wi-Fi autentifikasiyası tələbə bazasının administratoru olmaq demək deyil, bazaya girişdə tətbiq ayrıca hesabı və səlahiyyəti yoxlayır.
:::

:::reveal Ortaq PSK ilə fərdi sertifikatın ləğv edilməsi arasında hansı əməli fərq var?
- PSK-da bir cihazı ayırmaq mümkün deyil: sirr yayıldıqda parol bütün cihazlar üçün dəyişir, MAC bloklaması etibarlı ləğv deyil.
- Enterprise-da yalnız itən cihazın kimliyi və aktiv sessiyası ləğv edilir, digərləri işləyir.
- PSK-da kimin qoşulduğu bilinmir, Enterprise-da kimlik sessiya ilə əlaqələndirilir və rol təyin oluna bilir.
- Əvəzində Enterprise AAA, PKI, profil və dəstək tələb edir.
:::

:::reveal 802.1X-in üç rolunu və hər rolun qərar sərhədini izah edin.
- **Supplicant** (cihazdakı 802.1X müştərisi): serverin etibar zəncirini və gözlənilən adını yoxlayır.
- **Authenticator** (AP və ya kontroller): EAP mesajlarını ötürür, nəticəni sessiyaya tətbiq edir, açarları, VLAN və rolu idarə edir; EAP üsulunun qərarını özü vermir.
- **Autentifikasiya serveri** (çox vaxt RADIUS): EAP üsulunu tamamlayır, siyasətə görə qərar verir, icazəli şəbəkə cihazlarını və istifadəçi kimliyini bilir.
- Kimlik mənbəyi (hesab kataloqu və ya PKI) aktivliyi, qrupu və sertifikatın statusunu verir.
:::

:::reveal EAPOL ilə RADIUS hansı tərəflər arasında işləyir? Müştəriyə əvvəlcədən IP lazımdırmı?
- EAPOL (EAP over LAN) müştəri ilə autentifikator arasındadır; bunun üçün IP lazım deyil.
- Autentifikatorla RADIUS arasında EAP mesajları RADIUS atributlarında (EAP-Message) daşınır.
- Eyni məntiqi EAP söhbəti iki nəqliyyatdan keçir; AP-nin RADIUS üçün IP-si ilə tələbənin sonra DHCP-dən alacağı IP fərqlidir.
:::

:::reveal İlkin 802.11 qoşulması niyə istifadəçi autentifikasiyası deyil?
- Open System authentication yalnız AP ilə ilkin əlaqəni qurur, istifadəçinin kimliyi yoxlanmır.
- Bu mərhələdə idarə olunan port adi trafik üçün bağlıdır, yalnız EAPOL keçir.
- Real kimlik yoxlaması sonrakı EAP mübadiləsində (Identity, EAP üsulu, Access-Accept/Reject) aparılır.
:::

:::reveal EAP uğuru, dörd addımlı açar razılaşdırılması və DHCP hansı ardıcıllıqla baş verir?
- Əvvəl EAP üsulu bitir və server Access-Accept qaytarır.
- EAP-dan açar materialı (MSK, ondan PMK) yaranır; server onu autentifikatora qorunan RADIUS mexanizmi ilə çatdırır.
- Sonra müştəri və AP dörd addımlı açar razılaşdırmasını (EAP-dan ayrı mərhələ) tamamlayır, siyasət tətbiq olunur və adi trafikə yol açılır.
- Yalnız bundan sonra cihaz VLAN-da DHCP ilə IP alır, DNS və HTTPS işləyir; uçot aktivdirsə sessiya yazılır.
:::

:::reveal EAP-TLS, PEAP-MSCHAPv2 və EAP-TTLS hansı kimlik məlumatlarından istifadə edir?
- **EAP-TLS**: server sertifikatı və müştəri sertifikatı ilə şəxsi açar; parol yoxdur, PKI lazımdır.
- **PEAP-MSCHAPv2**: server sertifikatı ilə TLS tuneli, içində paroldan törəyən challenge-response.
- **EAP-TTLS**: server sertifikatı ilə tunel, içində seçilən daxili üsul (PAP, CHAP, MSCHAPv2 və ya EAP).
- EAP-MD5 və LEAP köhnədir, istifadədən çıxarılmalıdır.
:::

:::reveal Yanlış serverə etibar ediləndə PEAP-MSCHAPv2 və TTLS-PAP-də hansı məlumat riskə düşür?
- PEAP-MSCHAPv2: hücumçu tunelin öz tərəfində challenge-response materialını görür və parol törəmələrini sındırmağa cəhd edə bilər.
- TTLS-PAP: parolun özü tunel daxilində serverə verilir, saxta server onu alır.
- Hər iki halda səbəb server sertifikatının yoxlanmamasıdır; uzun parol riski azaldır, amma yoxlamanın söndürülməsini təhlükəsiz etmir.
:::

:::reveal Sertifikatın etibar zənciri ilə server adının yoxlanması niyə ayrı tələblərdir?
- Zəncir imzanın etibarlı CA-ya bağlanıb-bağlanmadığını göstərir; ad sertifikatın məhz gözlənilən serverə (məsələn, radius.wifi.uni.example) aid olduğunu göstərir.
- Yalnız ictimai CA-ya etibar edib adı məhdudlaşdırmasan, başqa təşkilatın düzgün sertifikatı da qəbul edilə bilər.
- Bundan əlavə vaxt, istifadə məqsədi (EKU), ləğv statusu və açara sahiblik ayrıca yoxlanır; biri digərini əvəz etmir.
:::

:::reveal CRL və OCSP nə üçündür? Sertifikatın ləğvi aktiv sessiyanı niyə həmişə dayandırmır?
- CRL (certificate revocation list) ləğv edilmiş sertifikatların siyahısıdır; OCSP konkret sertifikatın statusunu soruşur.
- Server müştəri ləğvini həqiqətən yoxlamalıdır; PKI-də düyməni basmaq RADIUS keşinin yeniləndiyini göstərmir.
- Ləğv qərarı növbəti yoxlamaya təsir edir; artıq qurulmuş sessiya və keş ayrıca qala bilər, ona görə sessiya kontrollerdə kəsilir.
:::

:::reveal Blast-RADIUS hansı nəqliyyat riskini göstərir və Message-Authenticator niyə yoxlanmalıdır?
- CVE-2024-3596: ənənəvi RADIUS kriptoqrafiyasındakı zəiflik; şəbəkə yolunda hücumçu MD5 toqquşması ilə cavabın mənasını dəyişməyə çalışa bilər. Bu radio ilə parol təxmini deyil.
- Message-Authenticator mesaj bütövlüyünü qoruyur; EAP paketlərində tələbi və düzgün yoxlanması qoruyucu sərhəddir.
- Tədbir: düzəlişli versiya, atributun tələbi və yoxlanması, köhnə cihazların yenilənməsi; uzun ortaq sirr düzəlişi əvəz etmir.
:::

:::reveal EAP-TLS ilə RadSec arasındakı tərəf və məqsəd fərqini izah edin.
- EAP-TLS: supplicant və EAP serveri arasında; məqsəd şəbəkəyə girən kimliyi yoxlamaq.
- RadSec (RFC 6614, TCP 2083): RADIUS müştərisi, proksi və ya server arasında; məqsəd RADIUS nəqliyyatını TLS ilə qorumaq.
- Proksi RadSec bağlantısını bitirib növbəti proksiyə ayrı TLS qura bilər, ona görə RadSec cihazdan serverə tək kanal deyil.
- RadSec EAP server sertifikatının müştəridə yoxlanmasını əvəz etmir.
:::

:::reveal eduroam-da ev və qonaq təşkilat hansı qərarları verir? Realm nə üçündür?
- Ev təşkilatı kimliyi yoxlayır (EAP serveri) və nəticəni qaytarır; etibarlı server adı onun profilindədir.
- Qonaq təşkilat radio xidmətini verir və yerli qaydaları tətbiq edir (internet çıxışı, daxili şəbəkədən izolyasiya).
- Realm (məsələn, uni.example istifadəçi adında) sorğunun hansı ev təşkilatına yönələcəyini göstərir.
- Proksilər marşrut atributlarını və metadata görə bilər; eduroam uğuru tətbiq səlahiyyəti vermir.
:::

:::reveal MAC filtri, captive portal və OWE hansı məhdudiyyətlərə malikdir?
- MAC filtri: MAC kimlik sübutu deyil, müşahidə edilir və dəyişdirilə bilər.
- Captive portal: qonaq qeydiyyatı və şərtlərin qəbulu üçündür, radio şifrələməsi və AP kimliyi vermir.
- OWE: passiv dinləməyə qarşı radio kanalını şifrələyir, amma AP sahibini autentifikasiya etmir; saxta AP-yə qoşulmaq mümkündür.
- Gizli SSID də kriptoqrafik nəzarət deyil.
:::

:::reveal Evil twin və rogue AP hansı hallarda eyni cihaz ola bilər?
- Evil twin etibarlı şəbəkənin adını təqlid edən AP-dir (aldatmaq məqsədi).
- Rogue AP təşkilatın razılığı olmadan infrastruktura qoşulmuş AP-dir.
- Kabelə icazəsiz qoşulmuş cihaz eyni zamanda universitetin SSID-sini aldadıcı təqlid edirsə, hər iki kateqoriyaya düşür; kateqoriyalar bir-birini istisna etmir.
- Tədbir: evil twin üçün server sertifikatı yoxlaması, rogue AP üçün port nəzarəti (802.1X/NAC) və inventar.
:::

:::reveal PMF hansı riskləri azaldır və radio basdırmaya niyə mane olmur?
- PMF uyğun əlaqədə müəyyən idarəetmə kadrlarını qoruyur, ona görə saxta deautentifikasiya və disassosiasiya kadrları ilə sessiyanın qırılması çətinləşir.
- Bütün idarəetmə kadrlarını və hər ilkin qoşulma vəziyyətini eyni qorumur.
- Radio basdırma (jamming) kanalı enerji ilə doldurur, kadr saxtalaşdırılması deyil; PMF fiziki maneəni dayandırmır. Tədbir: spektr analizi, ehtiyat yol.
:::

:::reveal WIDS xəbərdarlığından sonra AP-nin kabel portu necə müəyyən edilir?
- Xəbərdarlığın vaxtı, yeri, kanalı və rejimi saxlanır, inventar və dəyişiklik qeydləri ilə tutuşdurulur.
- Bir neçə sensorla yer daraldılır, otaq fiziki təsdiqlənir.
- Kabel bağlantısı kommutator portları, MAC cədvəli və DHCP qeydləri ilə araşdırılır.
- Universitetin portu tapılsa, səlahiyyətli komanda onu karantinə alır və ya bağlayır; sübut saxlanır.
:::

:::reveal Bluetooth-da cütləşmə üsulu ilə xidmət səlahiyyəti arasında fərq nədir?
- Cütləşmə (pairing) cihazların açar yaratması və seçilmiş üsulla qarşı tərəfi yoxlamasıdır; sonrakı bağlantılar üçün açarların saxlanması bonding adlanır.
- Just Works kimi üsul şifrələmə verə bilər, amma aradakı adam hücumuna qarşı autentifikasiya vermir.
- Xidmət səlahiyyəti cütləşmədən sonra nəyə icazə verildiyidir: səs qulaqcığına qoşulmaq kontakt və fayl paylaşmaq demək deyil.
- Hər ikisi ayrıca yoxlanılır.
:::

:::reveal Mobil operator autentifikasiyası universitet tətbiqinə giriş hüququnu niyə sübut etmir?
- SIM və ya eSIM abunə kimliyini operatora təqdim edir, telefon sahibinin universitetdəki rolunu təsdiqləmir.
- Operator radio şifrələməsi tətbiq yolunu ucdan-uca qorumur, LMS üçün HTTPS sertifikatı yenə yoxlanır.
- Qanuni operator saxta tətbiqə daxil edilən parolu qorumur.
:::

:::reveal BYOD cihazında MDM, NAC və EAP-TLS hansı ayrı vəzifələri görür?
- EAP-TLS cihazın və ya istifadəçinin sertifikatla kimliyini yoxlayır; cihazın proqram vəziyyətini sağlam elan etmir.
- MDM profil, sertifikat və siyasət paylayır, cihaz vəziyyətini yoxlayır, idarə olunan məlumatı uzaqdan silir; EAP-TLS üçün məcburi deyil.
- NAC kimliyə və cihaz vəziyyətinə görə seqment seçir (yenilənmiş noutbuk əməkdaş roluna, uyğunsuz cihaz bərpa seqmentinə).
:::

:::reveal Kampus layihəsində yaxşı siqnalın olması niyə tutumun yetərli olduğunu göstərmir?
- Boş binada yaxşı siqnal dolu auditoriyada tutumu göstərmir: mühit paylaşılır, protokol əlavələri və təkrar ötürmələr var, müştərilər müxtəlif sürətlə işləyir.
- Məsələn, 180 tələbə × 1 Mbit/s = 180 Mbit/s tətbiq yükü radionun elan olunan sürəti ilə birbaşa müqayisə edilmir; AP sayı və kanal planı ölçmə ilə seçilir.
- Quraşdırmadan sonra site survey real cihazlarla təkrarlanır.
:::

:::reveal Access-Accept alınıb IP alınmırsa diaqnostika hansı mərhələlər üzrə aparılmalıdır?
- Qəbul cavabı həmin telefonun sessiyası ilə əlaqələndirilir.
- Dörd addımlı açar razılaşdırması, təyin olunmuş VLAN-ın kontroller və kommutatorda mövcudluğu yoxlanır.
- Sonra DHCP yolu, DNS və firewall qaydaları, ən sonda tətbiq (LMS).
- Server sertifikatı yoxlamasını söndürmək həll deyil.
:::

## Situasiya tapşırıqları

**Situasiya 1.** Kitabxanada tələbənin telefonu eduroam üçün tanınmayan server sertifikatı göstərir. Yaxınlıqdakı başqa tələbə xəbərdarlığı qəbul etməyi məsləhət görür. Ev universitetinin rəsmi profili telefonda yoxdur. Tələbə və dəstək xidməti nə etməlidir?

:::reveal Cavab
- Aktiv və pozulan xassə: tələbənin eduroam kimlik məlumatı; autentifikasiya (server kimliyi) pozula bilər.
- Səbəb: saxta AP, səhv profil və ya qanuni serverin səhv sertifikatı.
- Tədbir: tələbə xəbərdarlığı keçməməli və kimlik mübadiləsini dayandırmalıdır; rəsmi profil etibarlı kanaldan quraşdırılır, ev təşkilatının server adı yoxlanır.
- Yoxlama: təhlükəsizlik qrupu radio müşahidəsini inventarla tutuşdurur; məlumat artıq təqdim edilibsə istifadə olunan EAP üsuluna görə sızma riski qiymətləndirilir, parol və sessiyalar üçün tədbir görülür.
:::

**Situasiya 2.** Kafedra noutbuku oğurlanıb. Cihaz EAP-TLS ilə qoşulurdu. PKI administratoru sertifikatı ləğv edib, amma kontroller noutbukun sessiyasını hələ aktiv göstərir. Sertifikat ləğvi niyə kifayət etməyib?

:::reveal Cavab
- Aktiv: kafedra noutbukunun şəbəkə girişi; pozulan xassə avtorizasiya və məxfilik.
- Səbəb: ləğv qərarı növbəti yoxlamaya təsir edir, artıq yaradılmış sessiya və keş ayrıca qala bilər.
- Tədbir: kontrollerdə sessiya kəsilir, uyğun keş siyasəti tətbiq olunur; tətbiq tokenləri və başqa kimlik məlumatları ayrıca ləğv edilir; disk şifrələməsi və MDM tədbirləri qiymətləndirilir.
- Yoxlama: RADIUS-un aktual CRL və ya OCSP nəticəsini həqiqətən yoxladığı təsdiqlənir.
:::

**Situasiya 3.** Universitetin RADIUS qeydi tələbə üçün Access-Accept göstərir. Telefon isə IP ala bilmir. Dəstək əməkdaşı server sertifikatı yoxlamasını söndürməyi təklif edir. Bu təklifin əvəzinə hansı yoxlamalar aparılmalıdır?

:::reveal Cavab
- Qəbul cavabı həmin telefonun sessiyası ilə əlaqələndirilir.
- Dörd addımlı açar razılaşdırması, təyin olunmuş VLAN-ın kontroller və kommutatorda mövcudluğu, DHCP yolu və firewall qaydaları yoxlanır.
- Sertifikat mərhələsi artıq uğurludur; yoxlamanı söndürmək sonrakı məlumat yolu səhvini düzəltmir və saxta server riskini artırır.
- Diaqnostika uğurun dayandığı mərhələdən davam edir.
:::

**Situasiya 4.** WIDS yataqxananın yanında inventarda olmayan AP aşkarlayıb. AP universitetin SSID-sini yayımlamır. İdarəçi avtomatik radio ayırmasını açmaq istəyir. Eyni vaxtda bir tələbənin otağında kabel rozetkasına şəxsi router qoşulduğu bildirilir. Hadisələr necə araşdırılmalıdır?

:::reveal Cavab
- Naməlum AP qonşu qanuni şəbəkə də ola bilər; radio xəbərdarlığı kabel routeri ilə dərhal eyniləşdirilmir.
- Yer, kanal və kabel portu qeydləri tutuşdurulur, fiziki baxış aparılır.
- Universitetin portuna icazəsiz qoşulma təsdiqlənərsə həmin port məhdudlaşdırılır.
- Səlahiyyət xaricindəki AP-yə radio müdaxiləsi edilmir.
- Təkrarın qarşısı üçün port nəzarəti və istifadə siyasəti düzəldilir.
:::

**Situasiya 5.** Kitabxananın qonaq şəbəkəsi açıqdır və istifadəçidən HTTPS portalında şərtləri qəbul etməyi istəyir. Portal açıldıqdan sonra rəhbərlik bütün Wi-Fi trafikinin şifrələndiyini düşünür. Hansı dəyişiklik və izah lazımdır?

:::reveal Cavab
- HTTPS portal bağlantısını qoruyur, açıq radio bağlantısını bütövlükdə şifrələmir (məxfilik pozula bilər).
- Uyğun cihazlar üçün OWE qiymətləndirilir; onun AP sahibini tanıtmadığı izah edilir.
- Qonaq seqmenti daxili resurslardan firewall ilə ayrılır, müştəri izolyasiyası sınanır.
- Tətbiqlər HTTPS istifadə etməlidir; əsas əməkdaş parolunu qonaq portalında toplamaq vərdişi yaradılmır.
:::

**Situasiya 6.** Universitetin PEAP-MSCHAPv2 şəbəkəsinə keçidində LDAP kataloqu ilə sadə parol yoxlaması işləyir, amma Wi-Fi autentifikasiyası alınmır. Komanda bütün parolları açıq formada saxlamağı təklif edir. Düzgün qərar necə verilməlidir?

:::reveal Cavab
- LDAP bind uğuru MSCHAPv2 üçün lazım olan yoxlama imkanını sübut etmir.
- Uyğun domen mexanizmi və ya tələb olunan parol törəmələrinin təhlükəsiz mövcudluğu araşdırılır.
- Parollar açıq saxlanılmır.
- EAP-TLS və ya kataloqla təhlükəsiz uyğunlaşan başqa üsul qiymətləndirilir; profil və server sertifikatının yoxlanması saxlanılır.
- Seçim platforma dəstəyi ilə birlikdə pilotda sınanır.
:::

**Situasiya 7.** Universitet kontrolleri ənənəvi RADIUS istifadə edir. Təhlükəsizlik qrupu Blast-RADIUS xəbərindən sonra yalnız ortaq sirri uzadıb işi bitmiş sayır. Federasiya proksisinə gedən əlaqə də eyni nəqliyyatdadır. Hansı tədbirlər çatışmır?

:::reveal Cavab
- Çatışmır: server və kontroller düzəlişləri, Message-Authenticator tələbi və yoxlanması, bütün RADIUS istifadə yollarının inventarı.
- EAP və başqa xidmətlərin qorunması ayrıca qiymətləndirilir.
- İdarəetmə yolu məhdudlaşdırılır; dəstəklənən tərəflər arasında sertifikatları düzgün yoxlanan RadSec planlaşdırılır.
- Uzun sirr protokol düzəlişini əvəz etmir.
- Keçid uyğunluq sınaqları ilə aparılır.
:::

**Situasiya 8.** Kafedranın Bluetooth ekranı daim cütləşmə rejimindədir. Bir əməkdaş şəxsi telefonunu qoşub və telefon kontaktların paylaşılmasını da təklif edir. Ekranın Wi-Fi-ı təhlükəsiz olduğundan əlavə risk olmadığı iddia edilir. Nə dəyişməlidir?

:::reveal Cavab
- Bluetooth ayrıca giriş səthidir; Wi-Fi autentifikasiyasının gücü Bluetooth xidmətinin səlahiyyətini müəyyən etmir.
- Cütləşmə fiziki nəzarət altında və uyğun autentifikasiya üsulu ilə aparılır, qeydiyyat pəncərəsi məhdudlaşdırılır.
- Ekran üçün lazım olmayan kontakt və fayl paylaşılması rədd edilir.
- Köhnə cütləşmələr silinir, proqram təminatı yenilənir.
:::

## Konspektdən situasiyalar

**Situasiya 1.** Tələbə yeməkxanada "eduroam"-a qoşulmaq istəyəndə telefon "Bu serverin sertifikatı etibarlı deyil" xəbərdarlığı verir. Dostu deyir: "Qəbul et, həmişə belə olur." Nə baş verə bilər və tələbə nə etməlidir?

:::reveal Cavab
- Bu, evil twin əlaməti ola bilər: kimsə "eduroam" adlı saxta AP qurub. SSID heç nəyi sübut etmir, həqiqiliyi yalnız RADIUS serverinin sertifikatı göstərir.
- Tələbə saxta sertifikatı qəbul etsə, hücumçu istifadəçi adını və MSCHAPv2 challenge-response məlumatını ələ keçirib parolu offline sındırmağa çalışa bilər.
- Tədbir: qoşulmamalı, universitetin rəsmi eduroam profilini (geteduroam/CAT) quraşdırmalı və İT xidmətinə xəbər verməlidir.
- Universitet WIPS ilə saxta AP-ni axtarmalıdır.
:::

**Situasiya 2.** Müəllimin noutbuku oğurlanıb. Kafedra Wi-Fi-ı WPA2-PSK ilə qurulub, parol noutbukda saxlanıb. Digər korpusda isə əməkdaş şəbəkəsi EAP-TLS ilə işləyir və noutbukda sertifikat var. Hər iki şəbəkə üçün nə etmək lazımdır?

:::reveal Cavab
- PSK şəbəkəsində bir cihazı ayırmaq mümkün deyil: parolu dəyişib kafedranın bütün cihazlarına yenidən yazmaq lazımdır.
- EAP-TLS şəbəkəsində yalnız həmin cihazın sertifikatı ləğv edilir (RADIUS ləğv siyahısını yoxlamalıdır), aktiv sessiya kəsilir, digər istifadəçilərə heç nə olmur. Bu fərq Enterprise rejimin əsas üstünlüyüdür.
- Əlavə: müəllimin hesab parolu dəyişdirilir; məlumatın qorunması disk şifrələməsindən və cihazın oğurlananda söndürülmüş, yoxsa yuxu rejimində olmasından asılıdır; MDM ilə uzaqdan silmə edilir.
:::

**Situasiya 3.** WIPS kitabxananın ikinci mərtəbəsində "UNI-Staff" adlı, amma universitetin inventarında olmayan BSSID-li bir AP aşkarlayır. Eyni vaxtda bir otaqda tələbənin öz routerini divardakı şəbəkə rozetkasına qoşduğu məlum olur. Bu iki hadisə eyni şeydirmi?

:::reveal Cavab
- Eyni cihazla bağlı ola bilər; kateqoriyalar bir-birini istisna etmir.
- Tələbənin kabel şəbəkəsinə icazəsiz qoşduğu router rogue AP-dir: niyyət pis olmasa da, daxili şəbəkəyə nəzarətsiz simsiz giriş açır. Universitetin SSID-sini təqlid edib istifadəçiləri aldatmaq üçün qurulan AP isə evil twindir.
- Hansı olduğunu müəyyən etmək üçün cihazın şəbəkəyə necə qoşulduğu və davranışı araşdırılır.
- Evil twin üçün: server sertifikatının yoxlanması, WIPS ilə yerinin tapılması və söndürülməsi. Rogue AP üçün: kabel portlarında 802.1X/NAC, istifadə olunmayan rozetkaların söndürülməsi və məqbul istifadə siyasəti.
:::

## Ehtimal olunan əlavə suallar

:::reveal Personal və Enterprise rejimlərini müqayisə edin.
- Personal (WPA2-PSK / WPA3-SAE): hamı ortaq parolu bilir, kimin qoşulduğu bilinmir, bir nəfəri çıxarmaq üçün parol hamı üçün dəyişir; WPA2-də hamı üçün eyni PMK. Ev, kiçik ofis, IoT seqmenti üçün uyğundur.
- Enterprise (802.1X/EAP): hər kəs öz hesabı və ya sertifikatı ilə girir, hər qoşulma şəxsə bağlıdır, hesabı bloklamaq və ya sertifikatı ləğv etmək kifayətdir, hər istifadəçiyə ayrıca PMK. Universitet, şirkət, xəstəxana üçündür.
- Bədəl: Enterprise AAA, PKI və profil idarəsi tələb edir.
:::

:::reveal EAP nədir və EAP üsulu ilə fərqi nədir?
- EAP (Extensible Authentication Protocol) autentifikasiya üçün mesaj çərçivəsidir; özü nə sertifikat, nə parol, nə güclü qarşılıqlı autentifikasiya vəd edir.
- Konkret üsulu EAP metodu (EAP-TLS, PEAP, EAP-TTLS, TEAP) müəyyən edir.
- Üsul seçilərkən kriptoqrafik xüsusiyyətlər, cihaz dəstəyi və server siyasəti birlikdə qiymətləndirilir.
:::

:::reveal TEAP nədir və crypto-binding nə verir?
- Tunelli EAP (TEAP) TLS tuneli daxilində müxtəlif üsulları, o cümlədən cihaz və istifadəçi autentifikasiyasının ardıcıl yoxlanmasını dəstəkləyir (EAP-FAST-ın davamıdır).
- Kriptoqrafik bağlama (crypto-binding) daxili autentifikasiyanın açar materialını xarici TLS tuneli ilə əlaqələndirir.
- Nəticə: həm cihaz, həm istifadəçi tələb edən siyasət; server sertifikatı yoxlanması yenə saxlanılır.
:::

:::reveal Server sertifikatının hansı xüsusiyyətləri yoxlanılır?
- Etibar zənciri (kök və aralıq CA imzaları), server adı (SAN uyğunluğu), vaxt (başlama və bitmə), istifadə məqsədi (açar istifadəsi və EKU), ləğv statusu (CRL və ya OCSP), açara sahiblik (şəxsi açarla sübut).
- Biri digərini əvəz etmir; istifadəçinin xəbərdarlığı əl ilə qəbul etməsi nəzarət sayılmır.
:::

:::reveal Dayanma əlamətinə görə diaqnostika: server sertifikatı rədd edilir, Access-Reject gəlir, RADIUS cavabı yoxdur. Əvvəl nə yoxlanır, nə edilməməlidir?
- Server sertifikatı rədd edilir: ad, CA zənciri və vaxt yoxlanır; yoxlamanı söndürmək olmaz.
- Access-Reject: EAP və avtorizasiya səbəbi yoxlanır; istənilən sertifikatı qəbul etmək olmaz.
- RADIUS cavabı yoxdur: marşrut, firewall və server yoxlanır; bütün sorğuları internetə açmaq olmaz.
- Ümumi qayda: uğurun dayandığı mərhələdən başla, təhlükəsizliyi zəiflətmə.
:::

:::reveal Simsiz hücumları və uyğun tədbirləri sadalayın (evil twin, rogue AP, deauth, jamming, offline parol təxmini, WPS, KRACK, war driving).
- Evil twin: server sertifikatı yoxlaması, idarə olunan profil, WIPS.
- Rogue AP: kabel portunda 802.1X/NAC, WIDS/WIPS ilə radio skanı, icazəli AP inventarı.
- Deauth: PMF (802.11w), WPA3.
- Jamming: protokolla qorunmur; aşkarlama (WIDS, spektr analizi), fiziki axtarış, kritik sistemlər üçün kabel ehtiyatı.
- Offline parol təxmini (WPA2-PSK əl sıxmasını yazıb sınamaq): WPA3-SAE, uzun təsadüfi parol, Enterprise rejim.
- WPS PIN hücumu (8 rəqəmli PIN hissə-hissə): WPS-i söndürmək.
- KRACK (2017, açarın yenidən quraşdırılması səhvi): AP və cihaz proqramını yeniləmək; ortaq parolu dəyişmək kömək etmir.
- War driving: güclü şifrələmə, siqnalı lazım olan əraziyə uyğunlaşdırmaq; SSID gizlətmək maneə deyil.
:::

:::reveal Kampus Wi-Fi-ının təhlükəsizlik yoxlama siyahısı hansı bəndlərdən ibarətdir?
- Ayrı SSID və VLAN-lar (əməkdaş, tələbə, qonaq, IoT); ayrı SSID kifayət deyil, VLAN-lar arasında firewall qaydası lazımdır.
- Əməkdaş və tələbə üçün WPA2/WPA3-Enterprise; qonaq üçün OWE və ya captive portal + müştəri izolyasiyası.
- PMF aktiv, WPS söndürülmüş, WEP və TKIP bağlı.
- AP və kontroller proqramı yenilənir, standart admin parolları dəyişdirilib, idarəetmə ayrıca VLAN-dadır.
- WIDS/WIPS ilə rogue və evil twin axtarışı; uğursuz autentifikasiyalar loglanıb SIEM-ə göndərilir.
- Radio planlaşdırma (site survey): siqnal lazımsız çıxmasın, kanallar üst-üstə düşməsin.
:::

:::reveal Amfiteatr üçün tutum hesabını göstərin (180 tələbə, hər birinə orta 1 Mbit/s).
- Hesab: 180 × 1 Mbit/s = 180 Mbit/s tətbiq yükü.
- Bu rəqəm radionun elan olunan fiziki sürəti ilə birbaşa müqayisə edilmir: mühit paylaşılır, protokol əlavələri və təkrar ötürmələr var, müştərilər müxtəlif sürətlə işləyir.
- Hesab ilkin tutum sualını qoyur, hazır avadanlıq sifarişi vermir; AP sayı və kanal planı ölçmə (site survey) ilə seçilir.
:::

:::reveal Ortaq PSK şəbəkəsindən Enterprise rejiminə keçid necə planlaşdırılır?
- Cihaz və istifadəçi qruplarının inventarı, dəstəklənən EAP üsulları.
- RADIUS, PKI və profil paylanması sınaq mühitində; kafedranın kiçik pilot qrupu ilə düzgün qoşulma, yanlış sertifikatın rəddi və ləğv sınaqları.
- Korpus və qrup üzrə mərhələ; köhnə PSK şəbəkəsinin müddəti məhdudlaşdırılır; istisna IoT cihazları ayrıca planlanır.
- Tələbəyə sertifikat xəbərdarlığını keçmək təlimatı verilmir; köhnə şəbəkə bağlananda vacib cihazların alternativ yolu təsdiqlənir.
:::
