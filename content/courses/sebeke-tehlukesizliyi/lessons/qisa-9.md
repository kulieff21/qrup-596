+++
title = "Simsiz autentifikasiya və simsiz rabitənin təhlükəsizliyi"
unit = "qisa"
order = 9
summary = "Mövzunun skeleti: hər anlayış bir-iki sətirdə. Simsiz sərhəd, Personal və Enterprise, 802.1X və EAP üsulları, sertifikat, RADIUS, RadSec, eduroam, hücumlar, WIDS/WIPS, Bluetooth, BYOD/MDM və kampus layihəsi."
updated = 2026-11-09

[[source]]
title = "Mühazirə 9: Simsiz autentifikasiya və simsiz rabitənin təhlükəsizliyi"
note = "Elmar Cabbarov, 2026–2027"
+++

Hər anlayış qısa verilir; izahlı variant orta və uzun səviyyədədir. Universitet topologiyası, ünvanlar və VLAN nömrələri şərti tədris nümunəsidir.

## Simsiz rabitədə təhlükəsizlik sərhədi

| Anlayış | Nədir / nə üçün vacibdir |
| --- | --- |
| WLAN, AP | Simsiz lokal şəbəkə (wireless local area network); cihazlar giriş nöqtəsinə (access point, AP) qoşulur |
| Radio sərhədi | Siqnal divardan kənara çıxır, ona görə radio sərhədi bina sərhədi ilə üst-üstə düşmür; fiziki mühafizə kifayət deyil |
| SSID | Şəbəkə adı (service set identifier); universitetə məxsusluğu sübut etmir, hücumçu eyni adı yayımlaya bilər |
| BSSID | Konkret radio xidmət dəstinin identifikatoru (basic service set identifier), adətən MAC ünvanı; o da kriptoqrafik sübut deyil |
| Məxfilik, bütövlük, əlçatanlıq | Oxunmamaq, dəyişikliyin aşkarlanması, xidmətin işləməsi; simsizdə qarşılıqlı autentifikasiya, avtorizasiya və izlənə bilmə əlavə olunur |
| AAA | Autentifikasiya (kimlik yoxlaması), avtorizasiya (verilən hüquq), istifadə uçotu (accounting: sessiyanın qeydi) |

Wi-Fi şifrələməsi tətbiq qorumasını əvəz etmir: LMS üçün HTTPS saxlanılır. Cihaz kimliyi insan kimliyi deyil: sertifikat noutbuku tanıyır, kimin oturduğunu yox.

## Giriş rejiminin seçilməsi

- **Personal**: ortaq parol. WPA2-Personal əvvəlcədən paylaşılmış açar (pre-shared key, PSK) işlədir, WPA3-Personal SAE. Bir cihazı ayırmaq üçün parol hamı üçün dəyişməlidir; kimin qoşulduğu bilinmir.
- **Enterprise**: hər şəxsə və ya cihaza ayrı kimlik (hesab və ya sertifikat). İtən cihazın kimliyi ləğv edilir, digərləri işləyir; əvəzində AAA, sertifikat infrastrukturu (PKI) və dəstək lazımdır.

| Rejim | Mənası |
| --- | --- |
| WPA2-Enterprise | 802.1X və EAP; məlumat AES əsaslı CCMP ilə qorunur (WEP və TKIP qəbul edilmir) |
| WPA3-Enterprise | 802.1X/EAP və qorunan idarəetmə kadrları (protected management frames, PMF); 192 bit rejim daha sərtdir |
| OWE | Fürsətçi şifrələmə (opportunistic wireless encryption): açıq şəbəkədə parolsuz radio şifrələməsi, AP sahibini autentifikasiya etmir |
| Açıq şəbəkə | Wi-Fi səviyyəsində məxfilik yoxdur |

## IEEE 802.1X: rollar və mesaj axını

- **Supplicant**: cihazdakı 802.1X müştərisi.
- **Authenticator**: AP və ya kontroller; EAP-ı ötürür, nəticəni tətbiq edir (qərar vermir).
- **Autentifikasiya serveri**: qərarı verir, çox vaxt RADIUS.
- **EAPOL**: müştəri ilə autentifikator arasında EAP over LAN; IP lazım deyil. Autentifikatorla RADIUS arasında EAP mesajları RADIUS atributlarında daşınır.

Ardıcıllıq: ilkin 802.11 qoşulması (Open System authentication istifadəçi yoxlaması deyil) → port yalnız EAPOL buraxır → Identity → Access-Request → EAP mübadiləsi → Access-Accept və ya Access-Reject → açar materialı → dörd addımlı açar razılaşdırması → VLAN, DHCP, DNS, HTTPS. Access-Accept internetin işlədiyini sübut etmir.

EAP-ın baş sessiya açarı (master session key, MSK) paketi qoruyan seans açarı deyil; MSK-dən cüt baş açar (pairwise master key, PMK) materialı alınır. Sertifikat ləğvi aktiv sessiyanı avtomatik kəsmir; sessiya kontrollerdə ayrıca dayandırılır.

## EAP üsulları

Genişləndirilə bilən autentifikasiya protokolu (Extensible Authentication Protocol, EAP) yalnız mesaj çərçivəsidir; üsul ayrıca seçilir.

| Üsul | Mahiyyət | Risk |
| --- | --- | --- |
| EAP-TLS | Qarşılıqlı sertifikat, parol yoxdur; ən güclü | PKI və açarın qorunması tələb olunur |
| PEAP | Qorunan EAP (Protected EAP): server sertifikatlı TLS tuneli, içində MSCHAPv2 challenge-response | Server yoxlanmasa saxta AP parol törəməsini alır |
| EAP-TTLS | Tunellənmiş TLS, daxili üsul PAP, CHAP, MSCHAPv2 və s. | TTLS-PAP-də saxta serverə parolun özü sızır |
| TEAP | Tunnel Extensible Authentication Protocol: cihaz və istifadəçi yoxlamasını birləşdirir; kriptoqrafik bağlama (crypto-binding) daxili açarı tunellə əlaqələndirir | Pilotda sınanır |
| EAP-MD5, LEAP | Köhnə üsullar | İşlədilməməlidir |

EAP-TLS cihazın proqram vəziyyətini sağlam elan etmir. PEAP üçün LDAP bind kifayət etmir; MSCHAPv2 uyğun parol törəməsi tələb edir. Üsulu dəyişmək platforma dəstəyi və pilot tələb edir.

## Sertifikat yoxlaması və kimliyin həyat dövrü

| Yoxlama | Nə |
| --- | --- |
| Zəncir | İmza etibarlı sertifikatlaşdırma mərkəzinə (certificate authority, CA) bağlanır |
| Server adı | Profildəki gözlənilən adla uyğunluq |
| Vaxt | Müddət keçməyib, saat düzgündür |
| Məqsəd | Açar istifadəsi uyğundur |
| Ləğv | Ləğv siyahısı (certificate revocation list, CRL) və ya OCSP (onlayn status protokolu) |
| Açara sahiblik | Sertifikat faylı yox, şəxsi açar sübutu |

Bu yoxlamalar bir-birini əvəz etmir; istifadəçinin xəbərdarlığı əl ilə qəbul etməsi nəzarət sayılmır. İlkin qeydiyyat (onboarding) etibarlı kanalla aparılır; hər cihaza ayrı sertifikat verilir; əməkdaş ayrılanda hesab, sertifikat və sessiya birlikdə bağlanır.

## RADIUS xidməti

RADIUS müştərisi AP və ya kontrollerdir (telefon yox). Ənənəvi portlar: UDP 1812 autentifikasiya, UDP 1813 uçot. Paketlər: Access-Request, Access-Challenge, Access-Accept, Access-Reject. Bütün paket şifrələnmir.

- Əsas atributlar: User-Name, NAS-IP-Address, Calling-Station-Id (adətən MAC), Message-Authenticator (bütövlük yoxlaması), Tunnel-Private-Group-Id (dinamik VLAN).
- RADIUS rol qaytarır (məsələn, tələbə VLAN 10, əməkdaş VLAN 20); firewall qaydasını özü yaratmır.
- FreeRADIUS-da `clients.conf` (hər kontrollerə ayrı sirr), EAP modulu və `check_crl`; `radiusd -XC` yalnız sintaksisi yoxlayır, `radtest` tam EAP sınağı deyil.

## RADIUS nəqliyyatının qorunması

- **Blast-RADIUS** (CVE-2024-3596): ənənəvi RADIUS-da MD5 toqquşması ilə cavabı dəyişdirmə riski. Tədbir: düzəlişli versiya, Message-Authenticator tələbi və yoxlanması; uzun sirr kifayət deyil.
- **RadSec**: TLS üzərindən RADIUS (RFC 6614, TCP 2083). EAP-TLS cihazın ev serveri ilə kimlik mübadiləsidir, RadSec isə RADIUS tərəfləri arasındakı nəqliyyatı qoruyur.

## eduroam federasiyası

eduroam-da kimliyi ev təşkilatı yoxlayır, radio xidmətini qonaq kampus verir. İstifadəçi adındakı realm (məsələn, uni.example) sorğunun marşrutunu göstərir. Etibarlı server adı ev təşkilatının profilindədir (CAT, geteduroam). Proksilər marşrut və metadata görə bilər; eduroam uğuru tətbiq səlahiyyəti vermir.

## MAC filtrləməsi, gizli SSID və captive portal

- **MAC filtri**: MAC dəyişdirilə bilər, kimlik sübutu deyil. MAC təsadüfiləşdirilməsi inventarı pozur.
- **Gizli SSID**: beacon-da ad yayılmır, amma kriptoqrafik nəzarət deyil.
- **Captive portal**: brauzerdə qeydiyyat; şifrələmə və AP kimliyi vermir.
- Müştəri izolyasiyası bütün yolları bağlamır; qonaq üçün firewall qaydası lazımdır.

## Simsiz hücumlar

| Hücum | Mahiyyət | Tədbir |
| --- | --- | --- |
| Evil twin | Etibarlı şəbəkənin adını təqlid edən saxta AP | Server sertifikatı və ad yoxlaması, idarə olunan profil |
| Rogue AP | Razılıqsız infrastrukturda qoşulmuş AP (məsələn, əməkdaşın routeri) | Kabel portunda 802.1X və şəbəkəyə girişə nəzarət (network access control, NAC), inventar |
| Deauth | Saxta ayırma kadrları | PMF |
| Radio basdırma (jamming) | Kanalı yararsız edir | Spektr analizi, kabel ehtiyatı; PMF kömək etmir |
| Parol təxmini | PSK və ya zəif EAP | Güclü sirr, uyğun üsul |
| WPS | Sadələşdirilmiş qeydiyyatın zəifliyi | Söndürmək |
| KRACK | Açarın yenidən quraşdırılması səhvi | AP və müştərini yeniləmək |
| War driving | Ərazi boyu şəbəkələri xəritələmək | Adı gizlətmək maneə deyil |

Evil twin və rogue AP eyni cihaz ola bilər.

## WIDS/WIPS

Simsiz müdaxilə aşkarlama sistemi (wireless intrusion detection system, WIDS) xəbərdarlıq verir; simsiz müdaxilənin qarşısının alınması sistemi (wireless intrusion prevention system, WIPS) cavab da verə bilər. Xəbərdarlıq hökm deyil: inventar, kontroller, kommutator və DHCP ilə tutuşdurulur, yer fiziki təsdiqlənir. Universitetin portu bağlanır; qonşu şəbəkəyə radio müdaxiləsi edilmir. Sensor susması görünməni azaldır.

## Bluetooth və mobil rabitə

- **Cütləşmə (pairing)** açar yaradır; sonrakı bağlantılar üçün saxlanması bonding adlanır. Just Works üsulu aradakı adam hücumuna qarşı autentifikasiya vermir. Daim açıq cütləşmə rejimi risklidir; xidmət səlahiyyəti ayrıca yoxlanır.
- **Mobil rabitə**: SIM və ya eSIM operatora tanıdır, universitetdəki rolu təsdiqləmir. Köhnə 2G zəifdir; saxta baza stansiyası və SIM dəyişdirmə fırıldağı ayrı risklərdir. Şəxsi hotspot kampus Wi-Fi-ını yan keçir.

## BYOD, MDM və cihaz vəziyyəti

- **BYOD** (bring your own device): şəxsi cihaz; giriş hüququ məhdud görünməyə uyğun seçilir.
- **MDM** (mobile device management): profil, sertifikat, siyasət paylayır, uzaqdan silə bilir; EAP-TLS üçün məcburi deyil.
- **NAC** cihaz vəziyyətini də nəzərə alır (uyğunsuz cihaz bərpa seqmentinə). **Zero Trust**: daxili şəbəkədə olmaq etimad üçün kifayət deyil.

## Kampus layihəsi, monitorinq və qəbul sınaqları

- İlkin ərazi ölçməsi (site survey) əhatəni və kanalları öyrənir; tutum auditoriya yükü ilə ölçülür (məsələn, 180 tələbə × 1 Mbit/s = 180 Mbit/s tətbiq yükü; AP sayı ölçmə ilə seçilir).
- Seqmentasiya: rol üzrə VLAN və firewall matrisi (tələbə, əməkdaş, qonaq, IoT, karantin); IPv6 də yoxlanır.
- Dayanıqlılıq: AP, kontroller və RADIUS ayrıca idarəetmə seqmentində; iki server ortaq dayanma nöqtəsini aradan qaldırmır; açıq şəbəkəyə avtomatik keçid olmamalıdır.
- Qeydlər: RADIUS, kontroller və DHCP saatla uyğunlaşdırılır; SIEM-də sertifikat bitmə dalğası parol hücumundan ayrılır; jurnalda parol saxlanmır.
- Miqrasiya: inventar, pilot, mərhələli keçid, köhnə PSK-nın müddətli bağlanması.
- Qəbul sınağı həm düzgün işi, həm yanlış kimliyin rəddini yoxlayır: yanlış server adı, ləğv edilmiş sertifikat, aktiv sessiyanın ləğvi, qonaqdan daxili resursa cəhd, RADIUS və sensor dayanması, dolu auditoriya.

:::exam
Üç tələ: MAC filtri və gizli SSID təhlükəsizlik vermir; Access-Accept internetin işlədiyini sübut etmir; sertifikat ləğvi aktiv sessiyanı avtomatik kəsmir. Server sertifikatının yoxlanmasını heç vaxt söndürmə.
:::
