+++
title = "Simsiz şəbəkələrin əsasları və şifrələmə mexanizmləri"
unit = "orta"
order = 8
summary = "Radio mühiti, 802.11 kadrları və qoşulma, WEP-dən WPA3-ə şifrələmə, 4 addımlı əl sıxma, hücumlar və kampus siyasəti: hər anlayış izah və əsas cədvəllərlə."
updated = 2026-11-09

[[source]]
title = "Mühazirə 8: Simsiz şəbəkələrin əsasları və şifrələmə mexanizmləri"
note = "Elmar Cabbarov, 2026–2027"
+++

Kabeldə trafiki dinləmək üçün kabelə və ya kommutatora fiziki yaxınlaşmaq lazımdır. Wi-Fi-da radiosiqnal divardan keçib korpusun qarşısındakı dayanacağa qədər çatır və hücumçu binaya girmədən trafiki qəbul edə bilir. Ona görə simsiz şəbəkədə şifrələmə seçimi kabel şəbəkəsinə nisbətən daha kritikdir. Mühazirədəki universitet topologiyası, ünvanlar və VLAN nömrələri şərti tədris nümunəsidir.

## Simsiz mühitin xüsusiyyətləri

Radio mühiti ortaqdır: CSMA/CA kanal uğrunda rəqabəti idarə edir, uyğun OFDMA ötürməsində isə resurslar cihazlar arasında bölünür.

| Anlayış | İzah |
| --- | --- |
| AP (Access Point) | Simsiz cihazları kabel şəbəkəsinə bağlayan qurğu |
| WLAN kontrolleri | Kampusdakı yüzlərlə AP-ni mərkəzdən idarə edir |
| SSID | Şəbəkənin adı ("UNI-Staff"). Həqiqiliyi sübut etmir: hər kəs eyni adlı şəbəkə yarada bilər |
| BSS, BSSID | Basic Service Set: bir AP ilə əlaqəli cihazlar qrupu; BSSID onun MAC formatlı identifikatorudur. Bir AP bir neçə virtual BSS elan edə bilər; BSSID saxtalaşdırıla bilər |
| ESS | Paylama sistemi (Distribution System, DS) ilə birləşən BSS-lər; telefon korpusda gəzəndə AP dəyişir (roaming). Eyni SSID təkbaşına eyni ESS demək deyil |
| İş rejimləri | İnfrastruktur (AP vasitəsilə), ad hoc (birbaşa), mesh (AP-lər bir-biri ilə simsiz bağlıdır) |

Simsiz lokal şəbəkə (Wireless Local Area Network, WLAN) məhdud ərazidə radio ilə məlumat mübadiləsidir. Divar etibar sərhədi olmur: antenanın əhatəsi ilə giriş hüququ ayrıdır, siqnalı alan şəxs qanuni istifadəçi sayılmır. Dörd anlayışı ayırmaq lazımdır: autentifikasiya (authentication) kimliyi yoxlayır, avtorizasiya (authorization) hansı resursa çatmağı müəyyənləşdirir (şəbəkəyə girmək qiymət dəyişmək hüququ vermir), şifrələmə məzmunu gizlədir, kriptoqrafik tamlıq saxtalaşdırmanı aşkar edir; təkrar ötürmədən qoruma köhnə kadrın yenidən qəbulunu dayandırır.

Wi-Fi qoruması cihaz ilə AP arasındadır; HTTPS ayrıca qorunur, ona görə radio şifrələməsi tətbiq şifrələməsini əvəz etmir. Rouminq-də növbəti AP-ni əsasən müştəri seçir; 802.11k qonşu məlumatı, 802.11v keçid təklifi, 802.11r sürətli keçid üçün açar mexanizmləri verir, amma heç biri ən yaxın AP-yə keçməyə zəmanət deyil.

## Standartlar və tezliklər

| Standart | Ticari ad | İl | Diapazon | Qeyd |
| --- | --- | --- | --- | --- |
| IEEE 802.11b / a / g | — | 1999–2003 | 2,4 / 5 / 2,4 GHz | Tarixi, 11–54 Mbit/s |
| 802.11n | Wi-Fi 4 | 2009 | 2,4 və 5 GHz | MIMO |
| 802.11ac | Wi-Fi 5 | 2013 | 5 GHz | Geniş kanallar |
| 802.11ax | Wi-Fi 6, 6E | 2021 | 2,4, 5, 6 GHz | Sıx mühitdə səmərəli |
| 802.11be | Wi-Fi 7 | 2024 | 2,4, 5, 6 GHz | MLO: eyni anda bir neçə diapazon |

2,4 GHz divarlardan yaxşı keçir və uzağa çatır, amma kanal azdır (üst-üstə düşməyən 1, 6, 11); mikrodalğalı soba və Bluetooth müdaxilə yaradır. 5 və 6 GHz daha çox spektr verir, amma divardan pis keçir, böyük auditoriyada çox AP lazım gəlir.

:::exam
Wi-Fi 6 təhlükəsizlik standartı deyil. Sürət texnologiyasıdır, Wi-Fi 6 routerdə WPA2 də seçilə bilər; təhlükəsizliyi WPA2 və WPA3 müəyyən edir. Yalnız 6 GHz-də (Wi-Fi 6E və 7) WPA3 və ya OWE məcburidir.
:::

**Siqnal.** Dalğa uzunluğu lambda = c / f: 2,4 GHz üçün təxminən 12,5 sm, 5 GHz üçün 6 sm (əhatə radiusu deyil). Kanal eni 20 MHz-dən 80 MHz-ə artanda sərbəst spektr azalır və geniş kanal zəif siqnalı düzəltmir. Siqnal dBm ilə ölçülür (−55 dBm −75 dBm-dən güclüdür). SNR (Signal-to-Noise Ratio) siqnal ilə küyün fərqidir: −60 dBm siqnal və −90 dBm küy 30 dB verir, küy −70 dBm-ə qalxanda SNR 10 dB-dir. RSSI avadanlığın verdiyi siqnal göstəricisidir, istehsalçılar arasında birbaşa müqayisə edilmir.

**Radio vaxtı.**

- OFDM məlumatı çoxlu dar alt daşıyıcıya bölür; OFDMA onları resurs vahidlərinə (RU) ayırıb AP-yə bir mübadilədə müxtəlif cihazlara fərqli RU verməyə imkan verir. Yəni OFDMA tezlik üzrə, MU-MIMO məkan üzrə bölür; MIMO isə çox antenna ilə məkan axınları deməkdir.
- CSMA/CA (Carrier Sense Multiple Access with Collision Avoidance) ötürmədən əvvəl kanalı dinləyir, təsadüfi geri sayma tətbiq edir, unicast kadrdan sonra ACK gözləyir; radio bütün toqquşmaları aşkarlaya bilmir, ona görə toqquşmadan yayınır.
- Gizli düyün (hidden node): AP-ni eşidən iki cihaz bir-birini eşitmir və eyni anda göndərir. RTS/CTS və NAV ayrılmış vaxtı bildirib bəzi toqquşmaları azaldır, amma hər paketdən əvvəl əlavə radio vaxtı tutur; universal həll deyil.

**Kampus planı.** 2,4 GHz-də 20 MHz və 1/6/11, 5 GHz-də qonşu hüceyrələrdə ayrı kanallar, 6 GHz-də WPA3 və ya OWE. DFS müəyyən 5 GHz kanallarında radarı qoruyur, radar aşkarlananda AP kanalı dəyişir (dərsdə qısa fasilə hücum deyil). Kanalın icazəli olması ölkənin radio qaydalarından asılıdır. Tutum hesabı: şərti 180 tələbədən 120-si eyni anda 1 Mbit/s tələb edirsə ən azı 120 Mbit/s tətbiq yükü olur, fiziki sürət bundan yüksək olmalıdır. AP sayını ölçmə olmadan artırmaq tutumu artırmır.

## Kadrlar və qoşulma

802.11-də üç kadr növü var: idarəetmə (beacon, probe, autentifikasiya, assosiasiya, deauthentication), nəzarət (RTS, CTS, ACK) və məlumat kadrları.

:::figure
src = "m08-1.png"
alt = "Cihazın şəbəkəyə qoşulma mərhələləri: skan, 802.11 autentifikasiya, assosiasiya, 802.1X/EAP (yalnız Enterprise), 4 addımlı əl sıxma, şifrəli trafik."
caption = "Qoşulma mərhələləri. WPA3-Personal-da SAE 802.11 autentifikasiya mərhələsində işləyir."
wide = true
:::

Kadrın sahələri: Frame Control (növ, To DS/From DS, Retry, Protected bitləri), Duration/ID, ünvanlar, Sequence Control, faydalı yük və FCS (4 bayt, radio səhvləri üçün CRC-32, kriptoqrafik deyil). Ünvan rolları: RA (Receiver Address), TA (Transmitter Address), SA (Source Address), DA (Destination Address). Tələbə LMS-ə paket göndərəndə birinci radio qəbuledicisi AP-dir. To DS 1, From DS 0 olanda noutbukdan DS-ə gedən kadrda Address 1 AP, Address 2 noutbuk olur (şərti MAC-lar).

AP beacon və probe cavablarında RSN elementi (Robust Security Network element) ilə şifr dəstlərini, AKM (Authentication and Key Management) üsullarını və PMF imkanlarını elan edir; eyni SSID-nin görünməsi cihazın həmin siyasətlə qoşulduğunu göstərmir, seçilmiş AKM yoxlanmalıdır.

:::steps Qoşulma ardıcıllığı
[[step]]
title = "Kəşf"
body = "AP beacon yayır, cihaz probe göndərir."

[[step]]
title = "802.11 autentifikasiya"
body = "Açıq sistemdə (Open System) yoxlama yoxdur, yalnız protokol addımıdır. WPA3-Personal-da burada SAE işləyir."

[[step]]
title = "Assosiasiya və Enterprise"
body = "Cihaz AP-yə bağlanır; yalnız Enterprise-da 802.1X/EAP mübadiləsi gəlir."

[[step]]
title = "4 addımlı əl sıxma və trafik"
body = "Şifrələmə açarları qurulur, sonra DHCP ünvanı alınır (IP). EAPOL uğurlu olub DHCP cavabı gəlməyəndə problemi parol və ya AES zəifliyi sayma."
:::

**PMF** (Protected Management Frames, 802.11w) açarlar qurulduqdan sonra deauthentication, disassociation və bəzi action kadrlarının saxtalaşdırılmasını məhdudlaşdırır: WPA2-də istəyə bağlıdır, WPA3-də məcburidir. Beacon, probe və ilkin assosiasiya qorunmur, ona görə saxta AP-yə qarşı kömək etmir; radio basdırmanı (jamming) də dayandırmır. Rejimlər: Disabled, Capable/optional (köhnə cihazlar qalanda hamı qorunmur), Required (uyğun olmayan cihaz qoşulmur, WPA3 üçün tələb).

## WEP

WEP (Wired Equivalent Privacy, 1997) kabelə ekvivalent məxfilik vəd etdi, yerinə yetirmədi. O, RC4 axın şifri (stream cipher) işlədir: hər kadr üçün 24 bitlik IV (Initialization Vector) gizli açarın əvvəlinə birləşir, RC4 açar axını yaradır, axın XOR ilə məlumata tətbiq olunur; tamlıq üçün CRC-32 və ICV (Integrity Check Value) var. XOR (exclusive OR) bitlər fərqli olanda 1, eyni olanda 0 verir və eyni axınla ikinci tətbiq məlumatı qaytarır (C = P ⊕ Z, P = C ⊕ Z). Eyni axın təkrar işlənsə, C1 ⊕ C2 = P1 ⊕ P2 olur və hücumçu açarsız açıq mətnlər arasında əlaqə qurur. XOR özü tamlıq vermir: C-nin bir biti dəyişəndə P-nin eyni biti dəyişir.

Üç zəiflik:

- **IV qısadır**: 24 bit 16 777 216 variantdır; ad günü paradoksuna görə təxminən 5000 kadrdan sonra təkrar ehtimalı 50%-dir (Pr ≈ 1 − exp(−n(n−1)/(2N)), n ≈ 4823; fərziyyə: IV-lər müstəqil və bərabər ehtimalla seçilir). Bu açarın mütləq bərpası demək deyil, toqquşmanın tez yarandığını göstərir.
- **RC4-ün IV ilə birləşməsi zəifdir**: Fluhrer, Mantin və Şamir (FMS, 2001) açarı trafikdən bərpa etməyin mümkünlüyünü göstərdilər (aircrack-ng); PTW (2007) bunu sürətləndirdi.
- **CRC-32 kriptoqrafik deyil**: hücumçu bitləri dəyişib CRC-ni düzəldir, qəbuledici görmür.

Kadr hazırlanması: CRC-32 hesablanıb ICV əlavə olunur, IV açarla birləşib RC4-ə verilir, məlumat və ICV axınla XOR edilir; IV açıq, məlumat və ICV şifrəli gedir. Reklamdakı 64 və 128 bit açara açıq 24 bitlik IV-ni əlavə edir.

:::exam
Parolun uzunluğu WEP-i qurtarmır: zəiflik protokoldadır. 26 onaltılıq simvoldan ibarət 104 bitlik açar da kifayət qədər trafikdə bərpa olunur. Konspekt "bir neçə dəqiqə" deyir, mühazirə isə sabit dəqiqə sayı vermir.
:::

## WPA və TKIP

WPA (2003) müvəqqəti həll idi: WEP avadanlığı proqram yeniləməsi ilə qorunsun deyə RC4 saxlandı. TKIP (Temporal Key Integrity Protocol) hər paket üçün açarı qarışdırır (müvəqqəti açar, ötürənin MAC-ı və TKIP ardıcıllıq sayğacı TSC ilə), 48 bitlik sayğac tətbiq edir, CRC-32 əsaslı ICV-ni saxlayır və Michael MIC (Message Integrity Code) əlavə edir. Michael yüngül hazırlanıb və güclü MAC deyil, MIC səhvlərinə qarşı əks tədbirlər xidmətin kəsilməsinə səbəb ola bilər. 2008-ci ildə Beck və Tews TKIP-ə məhdud hücum göstərdilər. WPA və TKIP işlədilməməlidir; yalnız TKIP bilən printer kabelə keçirilir və ya dəyişdirilir, qarışıq TKIP/CCMP rejimi bütün istifadəçilərə köhnə seçimi saxlayır. Seqmentasiya TKIP-in zəifliyini düzəltmir.

## WPA2 və CCMP

WPA2 (2004, 802.11i) RC4-ü AES (Advanced Encryption Standard) ilə əvəz etdi. AES 128 bitlik blok şifridir (AES-128, 192, 256 açarın uzunluğudur; blok həmişə 128 bit). AES təkbaşına kadrın necə şifrələnəcəyini həll etmir, bunu iş rejimi edir:

- **CTR** (Counter mode): hər blok üçün sayğacdan axın parçası Z_i = AES_K(A_i) alınır, C_i = P_i ⊕ Z_i.
- **CBC-MAC** (Cipher Block Chaining Message Authentication Code): məlumatı blok-blok zəncirləyib tamlıq kodu verir.
- **CCM** (Counter with CBC-MAC) ikisini birləşdirir; AAD (Additional Authenticated Data) şifrələnməyən, amma dəyişməməli başlıq hissələridir. **CCMP** (AES-CCMP) WPA2-nin bu rejimidir və WEP-dəki CRC-dən fərqli, açarlı yoxlama verir.
- **GCMP** AES-CTR-i Galois sahəsində GHASH autentifikasiyası ilə birləşdirir, aparatda paralelləşməsi asandır, Wi-Fi 6 və 7-də üstünlük verilir.

Müqayisə: CCMP-128-də açar 128 bit, PN 48 bit, nonce 13 bayt, teq 8 bayt, başlıq 8 bayt (tamlıq CBC-MAC); GCMP-128 və GCMP-256-da nonce 12 bayt, teq 16 bayt, tamlıq GHASH. PN gizli və təsadüfi deyil; qəbuledici köhnə PN-li kadrı atır. Əsas tələb eyni açar altında nonce-un təkrarlanmamasıdır.

İki rejim: **Personal rejim (PSK)** ortaq paroldur; **Enterprise (802.1X)** hər istifadəçini RADIUS serverindən fərdi hesabla keçirir.

| Meyar | Personal (PSK/SAE) | Enterprise (802.1X) |
| --- | --- | --- |
| Kimlik | Ortaq parol | Hesab və ya sertifikat |
| Server | Yoxdur | RADIUS |
| İstifadəçini ayırmaq | Parolu hamı üçün dəyişmək | Bir hesab bloklanır |
| Uyğun yer | Ev, kiçik ofis | Universitet, şirkət |

### Açarlar və 4 addımlı əl sıxma

:::figure
src = "m08-3.png"
alt = "WPA2 4 addımlı əl sıxması: M1 ANonce, M2 SNonce və MIC, M3 şifrəli GTK və MIC, M4 təsdiq."
caption = "WPA2 4 addımlı əl sıxması (Personal rejim)."
wide = true
:::

| Açar | İzah |
| --- | --- |
| PMK | Pairwise Master Key. Personal-da paroldan və SSID-dən PBKDF2-HMAC-SHA1, 4096 iterasiya, 256 bit ilə (salt = SSID). Enterprise-da 802.1X-dən |
| ANonce, SNonce | AP-nin və cihazın təsadüfi ədədləri |
| PTK | Pairwise Transient Key: PMK, iki nonce və iki MAC-dan; hər qoşulmada yenidir. KCK (Key Confirmation Key, MIC üçün), KEK (Key Encryption Key, GTK-nın şifrələnməsi üçün), TK (Temporal Key, məlumat üçün); CCMP-128-də 48 bayt |
| GTK | Group Temporal Key: broadcast trafiki üçün ortaq açar, istifadəçi kimliyini sübut etmir; PMF üçün ayrıca IGTK (BIP ilə) var |
| MIC | Mesajın doğru açarla göndərildiyini sübut edir |

Mesajlar (EAPOL-Key): **M1** AP ANonce və replay counter göndərir. **M2** cihaz SNonce-u yaradıb PTK hesablayır, SNonce və MIC göndərir. **M3** AP eyni PTK ilə MIC-i yoxlayır, şifrəli GTK göndərir. **M4** cihaz təsdiq edir, hər iki tərəf açarları quraşdırır (M4 radio ACK-ı deyil). Parol şəbəkədə ötürülmür, yalnız eyni PMK-ya sahib olmaq sübut edilir. PMK ilə PTK fərqlidir: PMK trafiki şifrələmir, ondan PTK törəyir. EAPOL-Key replay counter açar mübadiləsinin təzəliyini, PN isə məlumat kadrlarının təkrar qəbulunu idarə edir; ikisi eyni sayğac deyil.

### Oflayn lüğət hücumu

WPA2-Personal-ın əsas zəifliyi budur. Hücumçu əl sıxmasını yazır (lazım olsa cihazı deauth ilə atıb yenidən qoşulmağa məcbur edir), sonra öz kompüterində (Hashcat) hər namizəddən PMK, PTK hesablayıb MIC-i tutuşdurur. Şəbəkəyə qoşulmaq lazım olmadığına görə AP heç bir cəhd görmür və məhdudlaşdıra bilmir. "Universitet2024" kimi parol lüğətdə tez tapılır. PMKID hücumu (Jens Steube, 2018) bəzi AP-lərin M1-ə qoyduğu PMKID-dən qoşulan cihaz olmadan işləyir. Ortaq parol başqa fəsad da yaradır: parolu bilən və əl sıxmasını yazan istifadəçi başqa cihazın PTK-sını hesablaya bilir.

| Parol tipi | Variant sayı | Tam yoxlama (saniyədə 1 milyon) |
| --- | --- | --- |
| 8 rəqəm | 10⁸ | 100 saniyə |
| 8 kiçik hərf | 26⁸ ≈ 2,1 × 10¹¹ | təxminən 58 saat |
| 8 simvol, hərf və rəqəm | 62⁸ ≈ 2,2 × 10¹⁴ | təxminən 7 il |
| 12 simvol, hərf və rəqəm | 62¹² ≈ 3,2 × 10²¹ | 100 milyon ildən çox |
| 20 təsadüfi simvol | 62²⁰ ≈ 7 × 10³⁵ | praktiki mümkün deyil |

Real hücum lüğət və qaydalarla işləyir, insan parolu təsadüfi deyil. Praktiki tövsiyə 20 simvoldan uzun təsadüfi paroldur.

### KRACK

2017-ci ildə Mathy Vanhoef KRACK (Key Reinstallation Attack) hücumunu dərc etdi. Hücumçu M3-ü təkrar göndərir, cihaz eyni açarı yenidən quraşdırır və paket sayğacını sıfırlayır, açar axını təkrarlanır, trafik açıla bilir. KRACK parolu tapmır, protokolun vəziyyət maşınından istifadə edir; həlli cihazı yeniləməkdir. Təhlükəsiz tətbiq M3-ü təkrar cavablandıra bilər, amma artıq quraşdırılmış açarı yenidən quraşdırmamalıdır. Təkrar M3-ün görünməsi təkbaşına KRACK sübutu deyil.

## WPA3

WPA3 2018-ci ildə elan olundu. Yenilikləri:

- **SAE** (Simultaneous Authentication of Equals, "Dragonfly") PSK əvəzinə işləyir: hər parol təxmini üçün AP ilə canlı əlaqə lazımdır, oflayn lüğət hücumu mümkün deyil; hər sessiyanın açarı ayrıdır və parol sonradan məlum olsa köhnə trafik açılmır (irəli məxfilik, forward secrecy).
- **PMF məcburidir.**
- **WPA3-Enterprise 192 bit rejimi** GCMP-256 və güclü dəst işlədir.

SAE parola əsaslı açar mübadiləsidir (PAKE, Password-Authenticated Key Exchange). İki tərəf bərabərdir: hər biri paroldan parol elementi (Password Element, PWE) alır, Commit mesajları ilə təsadüfi açıq dəyərləri, Confirm mesajları ilə eyni sirri bildiklərini mübadilə edir. Yazılan mübadilədən parolu oflayn yoxlamaq olmur, AP uğursuz cəhdləri görüb məhdudlaşdırır; anti-clogging token hücum yükünü azaldır. SAE yalnız PMK-nı qurur, trafik açarları üçün yenə 4 addımlı əl sıxma işləyir.

**H2E** (Hash-to-Element) parolun qrup elementinə standartlaşdırılmış xəritələnməsidir; köhnə hunting-and-pecking yanaşmasının məlumatdan asılı davranışı yan kanal riski yaradırdı. 6 GHz-də məcburidir.

**Dragonblood** (Vanhoef və Ronen, 2019) WPA3-ə yan kanal və endirmə (downgrade) hücumlarıdır. Köhnə cihazlar üçün WPA2/WPA3 keçid rejimi (transition mode) hücumçuya cihazı WPA2-yə endirməyə imkan verir; PSK ilə qoşulan cihaz WPA2 xüsusiyyətlərini saxlayır, H2E bunu dəyişmir. Keçid rejimi ayrı SSID ilə və müvəqqəti saxlanır, kontrollerdə hər cihazın AKM-i yoxlanır.

**OWE** (Wi-Fi Enhanced Open, RFC 8110) WPA3-dən ayrı, əlaqəli proqramdır: parolsuz şəbəkədə Diffie–Hellman ilə hər cihaz üçün ayrı açar verir, qonşu unicast trafiki oxuya bilmir. OWE AP-nin həqiqiliyini yoxlamır, saxta AP riski qalır. Captive portal yalnız qeydiyyatdır və radioda heç nəyi şifrələmir.

**Wi-Fi 7 və MLO.** MLO (Multi-Link Operation) çoxbağlantılı cihazın (Multi-Link Device, MLD) bir neçə radio bağlantısını koordinasiya etməsidir; avtomatik ikiqat sürət və ya iki VPN deyil. Açar, nonce/PN konteksti və replay yoxlaması hər link üçün düzgün olmalıdır; 6 GHz-dən 5 GHz-ə keçid öz-özünə endirmə hücumu deyil, AKM və siyasət yoxlanır.

| Meyar | WEP | WPA | WPA2 | WPA3 |
| --- | --- | --- | --- | --- |
| Şifrələmə | RC4 | RC4 + TKIP | AES-CCMP | AES-CCMP, GCMP-256 |
| Tamlıq | CRC-32 | Michael MIC | CBC-MAC | CCMP/GCMP, PMF |
| Personal | Paylaşılan açar | PSK | PSK | SAE |
| Enterprise | Dinamik WEP, təhlükəsiz deyil | 802.1X | 802.1X | 802.1X, istəyə görə 192 bit |
| Əsas zəiflik | IV təkrarı, açar bərpası | RC4 irsi | Oflayn lüğət, PMF məcburi deyil | Keçid rejimində endirmə |
| Status | Qadağan | Qadağan | Qəbul edilir | Tövsiyə olunur |

**SAE PSK-dan nə ilə fərqlənir?** PSK-da yazılmış əl sıxması oflayn lüğət hücumuna imkan verir. SAE-də parol sabit PSK kimi işlənmir, qarşılıqlı mübadilə hər sessiya üçün PMK yaradır; hər təxmin canlı AP ilə əlaqə tələb edir (AP məhdudlaşdırır) və irəli məxfilik var.

## Simsiz şəbəkə hücumları

| Hücum | Mahiyyəti | Qorunma |
| --- | --- | --- |
| Evil Twin | Eyni SSID-li saxta AP | 802.1X, sertifikat yoxlaması, WIPS |
| Rogue AP | İcazəsiz AP şəbəkəyə qoşulur (işçinin "rahatlıq üçün" routeri) | 802.1X port nəzarəti, NAC, simsiz skan |
| Deauthentication | Saxta kadrla cihaz atılır | PMF |
| Oflayn parol hücumu | Əl sıxması və ya PMKID yazılır | WPA3-SAE, 802.1X, uzun parol |
| WPS PIN | 8 rəqəmli PIN praktiki 11 000 cəhdə enir (Viehböck, 2011) | WPS-i söndürmək |
| Karma, probe | Cihazın axtardığı şəbəkəyə AP "mən oyam" deyir | Köhnə SSID-ləri silmək, avtomatik qoşulmanı söndürmək |
| MAC saxtalaşdırması | Portaldan keçmiş MAC təqlid olunur | Portal əvəzinə 802.1X |
| Radio basdırma (jamming) | Mühit küylə doldurulur | Kriptoqrafik həll yoxdur, fiziki aşkarlama |

:::exam
MAC süzgəci və SSID-nin gizlədilməsi təhlükəsizlik tədbiri deyil: ikisi havada açıq görünür. WPS PIN-də 8 rəqəmin sonuncusu yoxlama rəqəmidir, hissələrin ayrıca yoxlanması 10⁴ + 10³ = 11 000 cəhd verir.
:::

WIDS (Wireless Intrusion Detection System) radio mühitini izləyir; WIPS avtomatik tədbir də görə bilir, amma yanlış qərar qanuni bağlantını kəsə bilər. Naməlum BSSID onun kabel şəbəkəsinə qoşulduğunu sübut etmir (qonşu AP, hotspot, icazəsiz AP fərqləndirilir). Wireshark süzgəcləri: `wlan.fc.type == 0` (idarəetmə), `wlan.fc.type_subtype == 0x08` (beacon), `0x0c` (deauthentication), `0x0a` (disassociation), `eapol`, `wlan.fc.retry == 1`, `wlan.fc.protected == 1`; monitor rejimi və düzgün kanal lazımdır. Hadisə araşdırması: vaxt, auditoriya, BSSID, deauth sayı, reason code (iddia, diaqnoz deyil), kanal doluluğu, DFS. SIEM qaydası MAC-a kor-koranə bağlanmır, çünki cihazlar təsadüfi MAC işlədə bilər.

## Digər simsiz texnologiyalar

| Texnologiya | Məsafə, istifadə | Əsas risklər |
| --- | --- | --- |
| Bluetooth, BLE | Tipik 10 m; qulaqlıq, klaviatura, IoT | Bluejacking (istənməyən mesaj), bluesnarfing (məlumat oğurluğu), zəif cütləşmə |
| NFC | Bir neçə sm; ödəniş, kartlar | Yaxın məsafədə dinləmə, relay hücumu |
| RFID | Sm-dən metrlərə; tələbə kartları, kitabxana | Köhnə kartların (MIFARE Classic) klonlanması |
| Mobil (4G/5G) | Km; telefon, modem | Saxta baza stansiyası (IMSI catcher), SIM-swap |

Bluetooth-da cütləşmə (pairing) açar razılaşması, bonding açarların saxlanmasıdır; Just Works rejimi vasitəçi hücumuna qarşı zəifdir, aşkarlanma rejimi söndürülür. Qısa məsafə NFC relay hücumunu dayandırmır. Yalnız açıq UID-yə əsaslanan RFID avtorizasiyası kopyalanır. Korporativ cihazlarda profil GPO və ya MDM ilə yayılır və RADIUS sertifikat adı yazılır; yoxlanmasa saxta serverin sertifikatı qəbul oluna bilər. EAP-TTLS/PAP parolu verə, PEAP-MSCHAPv2 oflayn yoxlanan cavabı verə bilər, EAP-TLS-də parol göndərilmir.

## Kampus şəbəkəsi üçün tövsiyələr

- Əməkdaşlar və tələbələr: WPA2/WPA3-Enterprise, fərdi hesab, sertifikat yoxlaması.
- Qonaqlar: ayrı VLAN, OWE və ya WPA3-SAE, müştəri izolyasiyası (client isolation), daxili şəbəkəyə giriş yoxdur.
- IoT və köhnə avadanlıq: ayrı SSID və VLAN, ciddi firewall qaydaları.
- WEP, WPA və TKIP söndürülür, WPS bağlanır.
- PMF ən azı Capable, WPA3 üçün Required.
- WIPS və ya radio skanı ilə icazəsiz AP aşkarlanır; firmware yenilənir, idarəetmə interfeysi ayrı şəbəkədədir.

| Qrup | Seqment (şərti) | Radio qoruması | İcazəli xidmət |
| --- | --- | --- | --- |
| Əməkdaş | VLAN 20 | Enterprise, PMF siyasəti | LMS, kitabxana, rola uyğun tətbiqlər |
| Tələbə | VLAN 30 | Fərdi Enterprise | Tədris resursları, İnternet |
| Qonaq | VLAN 40 | OWE, müştəri izolyasiyası | Yalnız İnternet |
| IoT | VLAN 50 | Güclü dəst, ayrıca siyasət | Yalnız öz idarəetmə xidməti |
| AP idarəetməsi | VLAN 60 | Ayrı idarəetmə bağlantısı | Yalnız administrator və log serveri |

SSID ilə VLAN uyğunlaşdırılır, aradakı trafik firewall-dan keçir (IPv4 və IPv6); SSID-lər eyni daxili şəbəkəyə məhdudiyyətsiz bağlanırsa real seqmentasiya yoxdur. Müştəri izolyasiyası qonaqlar arası yolu bağlayır, DNS və DHCP təsdiqli olmalıdır. Laboratoriya hostapd nümunəsində `wpa_key_mgmt=SAE`, `ieee80211w=2` (PMF tələb edir), `sae_pwe=1` (H2E) və `wps_state=0` birlikdə oxunur; `wpa=2` təkbaşına WPA3 demək deyil. Dəyişiklik əvvəl laboratoriyada yoxlanır. İtmiş noutbukda sertifikat və ya hesab ləğv edilir; ortaq PSK işlənibsə həmin sirr itmiş cihazda sayılır və dəyişdirilir.
