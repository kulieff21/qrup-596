+++
title = "Simsiz şəbəkələrin əsasları və şifrələmə mexanizmləri"
unit = "qisa"
order = 8
summary = "Simsiz şəbəkənin bütün anlayışları, WEP-dən WPA3-ə şifrələmə, əl sıxma, hücumlar və kampus siyasəti ən qısa formada."
updated = 2026-11-09

[[source]]
title = "Mühazirə 8: Simsiz şəbəkələrin əsasları və şifrələmə mexanizmləri"
note = "Elmar Cabbarov, 2026–2027"
+++

Kabeldə dinləmək üçün fiziki qoşulmaq lazımdır, Wi-Fi-da isə radiosiqnal divardan keçir; hücumçu binaya girmədən trafiki qəbul edə bilir. Ona görə simsiz şəbəkədə şifrələmə seçimi kabeldən daha kritikdir. Universitet nümunələri (ünvanlar, VLAN nömrələri) şərti tədris nümunəsidir.

## Simsiz mühitin xüsusiyyətləri

Radio mühiti ortaqdır: CSMA/CA kanal uğrunda rəqabəti idarə edir, OFDMA-da resurslar cihazlar arasında bölünür. Antenanın əhatəsi ilə giriş hüququ ayrı şeylərdir: siqnalı alan qanuni istifadəçi sayılmır.

| Anlayış | Nədir |
| --- | --- |
| AP (Access Point) | Simsiz cihazları kabel şəbəkəsinə bağlayan qurğu |
| WLAN kontrolleri | Yüzlərlə AP-ni mərkəzdən idarə edir; faydası: tələbə hərəkətdə LMS sessiyasını davam etdirir |
| WLAN (Wireless Local Area Network) | Məhdud ərazidə radio ilə lokal şəbəkə |
| SSID | Şəbəkənin adı; həqiqiliyi sübut etmir, hər kəs eyni adlı şəbəkə yarada bilər |
| BSS (Basic Service Set), BSSID | BSS bir AP ilə əlaqəli cihazlar qrupudur; BSSID onun MAC formatlı identifikatorudur (saxtalaşdırıla bilər) |
| ESS (Extended Service Set) | Paylama sistemi (DS) ilə birləşən BSS-lər; cihaz bir AP-dən digərinə keçir (roaming) |
| İş rejimləri | İnfrastruktur (AP ilə), ad hoc (birbaşa), mesh (AP-lər simsiz bağlıdır) |
| authentication / authorization | Kimliyi yoxlamaq / hansı resursa çatacağını müəyyənləşdirmək |

Şifrələmə məzmunu gizlədir, kriptoqrafik tamlıq saxtalaşdırmanı aşkar edir, təkrar ötürmədən qoruma köhnə kadrın yenidən qəbulunu dayandırır. Wi-Fi qoruması cihaz ilə AP arasındadır, HTTPS isə ayrıca qorunur: radio şifrələməsi tətbiq şifrələməsini əvəz etmir. Roaming-də AP-ni əsasən müştəri seçir; 802.11k, v, r qonşu məlumatı, keçid təklifi və sürətli keçid verir.

## Standartlar və tezliklər

IEEE 802.11b/a/g (1999–2003) tarixidir; 802.11n (Wi-Fi 4, 2009) MIMO, 802.11ac (Wi-Fi 5, 2013) geniş kanallar, 802.11ax (Wi-Fi 6 və 6E, 2021) sıx mühitdə səmərəli, 802.11be (Wi-Fi 7, 2024) MLO ilə eyni anda bir neçə diapazon verir.

- **2,4 GHz** divarlardan yaxşı keçir, amma az kanal var (üst-üstə düşməyən 1, 6, 11); Bluetooth və mikrodalğalı soba müdaxilə yaradır.
- **5 və 6 GHz** çox kanal və sürət verir, divardan pis keçir; DFS müəyyən 5 GHz kanallarında radarı qoruyur və kanal dəyişdirə bilər.

:::exam
Wi-Fi 6 təhlükəsizlik standartı deyil, sürət texnologiyasıdır; Wi-Fi 6 routerdə WPA2 də seçilə bilər. Yalnız 6 GHz-də WPA3 və ya OWE məcburidir.
:::

- **SNR** (Signal-to-Noise Ratio) siqnalla küyün fərqidir (desibel); **RSSI** (Received Signal Strength Indicator) avadanlığın verdiyi siqnal göstəricisidir, istehsalçılar arasında müqayisə edilmir. Geniş kanal zəif siqnalı düzəltmir.
- **OFDM** məlumatı dar alt daşıyıcılara bölür; **OFDMA** alt daşıyıcıları resurs vahidlərinə (RU) bölüb bir mübadilədə müxtəlif cihazlara verir.
- **CSMA/CA** (Carrier Sense Multiple Access with Collision Avoidance) göndərməzdən əvvəl kanalı dinləyir, ACK gözləyir.
- **Gizli düyün (hidden node)**: iki cihaz AP-ni eşidir, bir-birini eşitmir və toqquşur; RTS/CTS və NAV bunu azaldır, amma əlavə radio vaxtı aparır.
- **MIMO** çox antenna ilə məkan axınları, **MU-MIMO** bunu istifadəçilərə bölür.
- Kampusda 1/6/11 planı, 20 MHz ilə başlamaq; AP sayını yalnız hesabla yox, ölçmə ilə seçmək.

## Kadrlar və qoşulma

802.11-də üç kadr növü var: idarəetmə (beacon, probe, autentifikasiya, assosiasiya, deauthentication), nəzarət (RTS, CTS, ACK) və məlumat. Kadrda Frame Control, Duration/ID, ünvanlar, Sequence Control, faydalı yük və FCS (CRC-32, kriptoqrafik deyil) var. Ünvan rolları: RA (Receiver Address), TA (Transmitter Address), SA (Source Address), DA (Destination Address); To DS və From DS bitləri hansı ünvanın nə olduğunu müəyyən edir.

Qoşulma ardıcıllığı: kəşf (beacon, probe), 802.11 autentifikasiya (açıq sistemdə yalnız formal addım; WPA3-Personal-da SAE), assosiasiya, yalnız Enterprise-da 802.1X/EAP, 4 addımlı əl sıxma, sonra DHCP və IP. AP beacon-da RSN elementi (Robust Security Network element) ilə şifr dəstlərini, AKM (Authentication and Key Management) üsullarını və PMF imkanlarını elan edir.

**PMF** (Protected Management Frames) deauthentication kimi idarəetmə kadrlarını qoruyur: WPA2-də istəyə bağlı, WPA3-də məcburi. Beacon və probe qorunmur, ona görə saxta AP-yə qarşı kömək etmir.

## WEP

WEP (Wired Equivalent Privacy, 1997) RC4 axın şifri (stream cipher) işlədir: hər kadr üçün 24 bitlik IV (Initialization Vector) açarın əvvəlinə birləşir, RC4 axını XOR ilə məlumatla toplanır, tamlıq üçün CRC-32 və ICV (Integrity Check Value) işlənir. XOR (exclusive OR) eyni axınla iki dəfə tətbiq olunanda məlumatı qaytarır, ona görə axının təkrarı təhlükəlidir. Üç zəiflik:

- **IV qısadır** (16 777 216 variant); ad günü paradoksuna görə təxminən 5000 kadrdan sonra təkrar ehtimalı 50% olur, təkrar isə eyni açar axını deməkdir.
- **RC4-ün IV ilə birləşməsi zəifdir**: FMS (2001) və PTW (2007) hücumları açarı trafikdən bərpa edir (aircrack-ng).
- **CRC-32 kriptoqrafik deyil**: hücumçu kadrı dəyişib CRC-ni düzəldə bilər.

:::exam
Parolun uzunluğu WEP-i qurtarmır: zəiflik parolda yox, protokoldadır.
:::

## WPA və TKIP

WPA (2003) müvəqqəti həll idi: WEP avadanlığı proqram yeniləməsi ilə qorunsun deyə RC4 saxlandı. TKIP (Temporal Key Integrity Protocol) hər paketə ayrı açar qarışdırır, 48 bitlik TKIP ardıcıllıq sayğacı (TSC) işlədir, CRC-32 əsaslı ICV-ni saxlayır və Michael MIC (Message Integrity Code) əlavə edir. Bu WEP-dən yaxşıdır, amma RC4 irsi qalır; Beck və Tews (2008) TKIP-ə məhdud hücum göstərdilər. WPA və TKIP işlədilməməlidir; TKIP-li köhnə cihaz kabelə keçirilir və ya dəyişdirilir.

## WPA2 və CCMP

WPA2 (2004, 802.11i) RC4-ü AES (Advanced Encryption Standard) ilə əvəz etdi. CCMP rejimi (AES-CCMP) AES-CTR (Counter mode) ilə şifrələyir və CBC-MAC (Cipher Block Chaining Message Authentication Code) ilə tamlığı yoxlayır; birlikdə CCM (Counter with CBC-MAC) adlanır. Əlavə autentifikasiya məlumatı (AAD) şifrələnməyən başlıq hissələrini qoruyur. GCMP şifrələməni Galois sahəsində GHASH autentifikasiyası ilə birləşdirir, Wi-Fi 6 və 7-də üstünlük verilir; hər ikisində paket nömrəsi (PN, 48 bit) təkrar qəbuldan qoruyur.

İki rejim: **Personal rejim (PSK/SAE)** ortaq paroldur; **Enterprise (802.1X)** hər istifadəçini RADIUS serverindən fərdi hesabla keçirir.

| Açar | Nədir |
| --- | --- |
| PMK (Pairwise Master Key) | Personal-da paroldan və SSID-dən (PBKDF2, 4096 iterasiya, salt kimi SSID) hesablanır; Enterprise-da 802.1X-dən gəlir |
| ANonce, SNonce | AP-nin və cihazın təsadüfi ədədləri |
| PTK (Pairwise Transient Key) | PMK, iki nonce və iki MAC-dan; hər qoşulmada yenidir; KCK (Key Confirmation Key, MIC üçün), KEK (Key Encryption Key, GTK-nı qorumaq üçün), TK (Temporal Key, məlumat üçün) |
| GTK (Group Temporal Key) | Broadcast trafiki üçün ortaq açar; IGTK qrup idarəetmə kadrları üçündür (BIP ilə qorunur) |
| MIC | Mesajın doğru açarla göndərildiyini sübut edir |

**4 addımlı əl sıxma** (EAPOL-Key mesajları): M1 AP ANonce göndərir; M2 cihaz SNonce və MIC göndərir; M3 AP MIC-i yoxlayıb şifrəli GTK göndərir; M4 cihaz təsdiq edir. Parol şəbəkədə ötürülmür, yalnız eyni PMK-dan alınan açarların doğruluğu yoxlanır.

- **Oflayn lüğət hücumu**: hücumçu əl sıxmasını yazır (lazım olsa deauth ilə cihazı atıb yenidən qoşdurur), parolları öz kompüterində sınayır (Hashcat); AP heç nə görmür. PMKID hücumu (Steube, 2018) bəzi AP-lərdə qoşulan cihaz olmadan işləyir. Uzun təsadüfi parol (20+ simvol) və SAE/Enterprise müdafiə edir; 8 simvolluq hərf-rəqəm parol şərti saniyədə 1 milyon cəhdlə təxminən 7 ilə yoxlanır.
- **KRACK** (Key Reinstallation Attack, Vanhoef, 2017): M3 təkrar göndərilir, cihaz açarı yenidən quraşdırıb PN-ni sıfırlayır, açar axını təkrarlanır. Parolu tapmır; həlli cihazı yeniləməkdir.
- Personal-da kimi bilməmək və bir nəfəri ayıra bilməmək də problemdir; Enterprise-da bir hesab bloklanır.

## WPA3

WPA3 (2018): **SAE** (Simultaneous Authentication of Equals, "Dragonfly") PSK əvəzinə işləyir; hər parol təxmini üçün AP ilə canlı əlaqə lazımdır, oflayn lüğət hücumu mümkün deyil, hər sessiyanın açarı ayrıdır (irəli məxfilik, forward secrecy). PMF məcburidir; WPA3-Enterprise-ın 192 bitlik rejimi GCMP-256 işlədir.

- SAE parola əsaslı açar mübadiləsidir (PAKE, Password-Authenticated Key Exchange): iki tərəf bərabərdir, parol elementi (PWE) əlaqəli Commit mesajları açıq dəyərləri, Confirm mesajları eyni sirri bildiklərini mübadilə edir; anti-clogging token yükü azaldır. Nəticədə PMK qurulur, trafik açarları yenə 4 addımlı əl sıxma ilə.
- **H2E** (Hash-to-Element) parolu qrup elementinə yan kanal riski olmadan xəritələyir (köhnə hunting-and-pecking əvəzinə); 6 GHz-də məcburidir.
- **Dragonblood** (Vanhoef və Ronen, 2019): yan kanal və endirmə (downgrade) hücumları. WPA2/WPA3 keçid rejimi (transition mode) cihazı WPA2-yə endirməyə imkan verir; ayrı SSID ilə və müvəqqəti saxlanmalıdır.
- **OWE** (Wi-Fi Enhanced Open) parolsuz şəbəkədə hər cihaza ayrı açar verir (Diffie–Hellman), amma AP-nin həqiqiliyini yoxlamır. **Captive portal** yalnız qeydiyyatdır, şifrələmə vermir.
- **PMF rejimləri**: Disabled, Capable/optional, Required. PMF jamming-i və saxta AP-ni dayandırmır.
- **MLO** (Multi-Link Operation) Wi-Fi 7-də MLD (Multi-Link Device) ilə bir neçə radio bağlantısını koordinasiya edir; açar və PN konteksti hər link üçün düzgün saxlanmalıdır.

| | WEP | WPA | WPA2 | WPA3 |
| --- | --- | --- | --- | --- |
| Şifrələmə | RC4 | RC4 + TKIP | AES-CCMP | AES-CCMP, GCMP-256 |
| Tamlıq | CRC-32 | Michael MIC | CBC-MAC | CCMP/GCMP, PMF |
| Personal | Paylaşılan açar | PSK | PSK | SAE |
| Status | Qadağan | Qadağan | Qəbul edilir | Tövsiyə olunur |

## Simsiz şəbəkə hücumları

| Hücum | Mahiyyəti | Qorunma |
| --- | --- | --- |
| Evil Twin | Eyni SSID-li saxta AP | 802.1X, sertifikat yoxlaması, WIPS |
| Rogue AP | İcazəsiz AP şəbəkəyə qoşulur | 802.1X, NAC, simsiz skan |
| Deauthentication | Saxta kadrla cihaz atılır | PMF |
| Oflayn parol hücumu | Əl sıxması və ya PMKID yazılır | SAE, 802.1X, uzun parol |
| WPS PIN | 8 rəqəmli PIN təxminən 11 000 cəhdə enir (Viehböck, 2011) | WPS-i söndürmək |
| Karma, probe | AP axtarılan şəbəkəyə "mən oyam" deyir | Köhnə SSID-ləri silmək |
| MAC saxtalaşdırması | Portaldan keçmiş MAC təqlid olunur | Portal əvəzinə 802.1X |
| Radio basdırma (jamming) | Mühit küylə doldurulur | Kriptoqrafik həll yoxdur, fiziki aşkarlama |

MAC süzgəci və SSID gizlətmək təhlükəsizlik tədbiri deyil. WIDS (Wireless Intrusion Detection System) radionu izləyir, WIPS qarşısını da ala bilir, amma yanlış qərar qanuni bağlantını kəsə bilər. Wireshark süzgəcləri (eapol, deauthentication, beacon) hadisəni təhlil edir; monitor rejimi lazımdır.

## Digər simsiz texnologiyalar

- **Bluetooth, BLE**: qısa məsafə; Bluejacking (istənməyən mesaj), bluesnarfing (məlumat oğurluğu), zəif cütləşmə (pairing); Just Works rejimi vasitəçiyə qarşı zəifdir, bonding açarların saxlanmasıdır.
- **NFC** (Near Field Communication): yaxın məsafədə dinləmə və relay hücumu.
- **RFID** (Radio Frequency Identification): köhnə kartlar (MIFARE Classic) klonlanır.
- **Mobil 4G/5G**: saxta baza stansiyası (IMSI catcher), SIM-swap.
- Korporativ cihazlarda profil GPO və ya MDM ilə yayılır; RADIUS sertifikatı yoxlanmasa saxta server qəbul edilə bilər. EAP-TTLS/PAP parolu verə, PEAP-MSCHAPv2 oflayn yoxlanan cavabı verə bilər; EAP-TLS-də parol göndərilmir.

## Kampus şəbəkəsi üçün tövsiyələr

- Əməkdaş və tələbə: WPA2/WPA3-Enterprise, fərdi hesab, sertifikat yoxlaması.
- Qonaq: ayrı VLAN, OWE və ya SAE, müştəri izolyasiyası (client isolation), daxili şəbəkəyə giriş yoxdur.
- IoT və köhnə avadanlıq: ayrı SSID və VLAN, sərt firewall.
- WEP, WPA, TKIP və WPS söndürülür; PMF Capable, WPA3 üçün Required.
- WIPS və ya radio skanı ilə icazəsiz AP aşkarlanır; firmware yenilənir, idarəetmə ayrı şəbəkədədir.
- SSID ilə VLAN uyğunlaşdırılır, aradakı trafik firewall-dan keçir (IPv6 də); şərti VLAN 20–60 matrisi bunu göstərir.
- hostapd nümunəsində `wpa_key_mgmt=SAE`, `ieee80211w=2` (PMF), `sae_pwe=1` (H2E) birgə oxunur. İtmiş cihazda sertifikat ləğv edilir.

:::exam
Situasiya cavabı: aktiv, pozulan xassə, səbəb, tədbir. Misal: WEP-də uzun parol kömək etmir (protokol zəifdir); WPA2-PSK-da əl sıxmasından oflayn parol tapılır, həll Enterprise/SAE; captive portal şifrələmir, həll OWE/SAE və müştəri izolyasiyası; deauth üçün PMF; keçid rejimində PSK WPA2-ni saxlayır, H2E bunu dəyişmir.
:::
