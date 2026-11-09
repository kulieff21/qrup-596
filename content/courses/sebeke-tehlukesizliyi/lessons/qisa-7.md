+++
title = "Tələ sistemləri, proksi-serverlər və virtual özəl şəbəkələr (VPN)"
unit = "qisa"
order = 7
summary = "Mövzunun skeleti: hər anlayış bir-iki sətirdə. Tələ sistemləri, düz və tərs proksi, VPN, IPsec, WireGuard, köhnəlmiş protokollar və ZTNA."
updated = 2026-11-09

[[source]]
title = "Mühazirə 7: Tələ sistemləri, proksi-serverlər və virtual özəl şəbəkələr (VPN)"
note = "Elmar Cabbarov, 2026–2027"
+++

Üç alət: **tələ sistemi** hücumçunu aldadıb izləyir, **proksi** trafikin arasına vasitəçi qoyur, **VPN** etibarsız şəbəkə üzərindən qorunan kanal qurur. Hər anlayış bir-iki sətirdə; izahlı variant orta və uzun səviyyədədir. Universitet nümunələri şərtidir.

## Tələ sistemləri

### Anlayış və tarix

Tələ sistemi (honeypot) hücumçunu cəlb edib hərəkətlərini qeydə almaq üçün qurulmuş saxta resursdur; iş funksiyası olmadığından ona gələn hər bağlantı şübhəlidir və yanlış həyəcan çox azdır. Lens Spitsner (Lance Spitzner) onu “dəyəri icazəsiz istifadədən gələn resurs” adlandırır. IDS görür və imza ilə axtarır, IPS yolda dayandırır, tələ isə yalnız cəlb edib qeydə alır.

| Hadisə | Mənası |
| --- | --- |
| Clifford Stoll, 1986, *The Cuckoo's Egg* | Saxta hərbi sənədlərlə hücumçunu xəttdə saxladı |
| Bill Cheswick, 1991, *Berferd* | Saxta sistemlə hücumçunu aylarla müşahidə etdi |
| Fred Cohen, Deception Toolkit | Açıq yayımlanan ilk alətlərdən |
| The Honeynet Project, 1999 | “Know Your Enemy” silsiləsi, honeynet termini |

### Təsnifat

| Ölçü | Növlər |
| --- | --- |
| Məqsəd | İstehsalat tələsi (production honeypot): daxili erkən xəbərdarlıq. Tədqiqat tələsi (research honeypot): yeni üsul və zərərli proqram öyrənmək |
| Rol | Server tələsi gözləyir; müştəri tələsi (client honeypot) özü zərərli saytı gəzir |
| Qarşılıqlı əlaqə | **Aşağı (low-interaction):** bir neçə xidmət təqlidi, az məlumat, aşağı risk (Honeyd, Dionaea). **Orta (medium-interaction):** saxta fayl sistemi, əmrlər yazılır, real ƏS-də icra olunmur (Cowrie shell rejimi). **Yüksək (high-interaction):** real ƏS, ən çox məlumat, ən yüksək risk (Cowrie proxy rejimi ilə real sistem) |

Xüsusi tələlər: Conpot sənaye sistemlərini (ICS/SCADA), Dionaea SMB, HTTP, FTP protokollarını təqlid edir.

### Honeynet, honeytoken, deception

- **Honeynet:** bir neçə tələdən ibarət saxta şəbəkə; tələlər arası hərəkəti (lateral movement) göstərir.
- **Honeytoken:** sistem yox, saxta məlumat (hesab, “parollar.xlsx”, API açarı); istifadə olunanda həyəcan verir, daxili sızmanı tutur. Canarytokens belə tokenlər yaradır.
- **Aldatma (deception):** tələ və tokenlərin kütləvi, avtomatik yayılması; MITRE Engage bunu sistemləşdirir.

### Yerləşdirmə və məlumat

| Anlayış | Nədir |
| --- | --- |
| Yer | Xaricdə (internet səs-küyü), DMZ yanında ayrıca seqmentdə, daxili şəbəkədə (ən çox fayda: hər bağlantı insidentdir) |
| Beş qayda | Ayrıca VLAN; çıxış firewall ilə kəsilir, yoxsa tələ sıçrayış nöqtəsinə (pivot) çevrilir; real məlumat yoxdur; loglar kənar serverə; yüksək səviyyə snapshot-dan bərpa olunur |
| Data control | Ələ keçirilmiş tələnin ziyan verməsinin qarşısı |
| Data capture | Hücumçunun hər addımının gizli qeydi |
| Data collection | Tələlərin qeydlərinin mərkəzdə birləşməsi |
| SIEM | Tələyə hər bağlantı yüksək dərəcəli xəbərdarlıq verir |
| IoC | Qeydlərdən IP, parol, əmr, skript ünvanı və heş çıxır; MITRE ATT&CK-a bağlanır |
| chain of custody | Hüquqi iş üçün sübutun ötürülmə zənciri |
| Cyber Kill Chain | Tələ kəşfiyyat, çatdırılma, istismar, C2 və daxili hərəkəti görür; silahlanmanı görmür |

Alətlər: Cowrie (SSH/Telnet), Dionaea, Honeyd, Conpot, OpenCanary (daxili şəbəkə), T-Pot (iyirmidən çox tələ konteynerdə) və Canarytokens.

### Risklər

- Dar görmə: yalnız ona gələn hücumu görür, IDS və SIEM-i əvəz etmir; “serverlərimiz təhlükəsizdir” nəticəsi çıxmır.
- Təcrübəli hücumçu tələni tanıya bilər; Shodan bəzilərini etiketləyir, standart parametr işlətmə.
- Ələ keçirilmə və pivot: hücum universitetin IP-sindən görünər.
- Hüquqi: passiv gözləmək, təhrik etməmək, fərdi məlumat qanunu, hüquq xidməti ilə razılaşma; əks hücum (hack-back) icazəsiz girişdir.

:::exam
Honeypot qarşısını alma vasitəsi deyil, aşkarlama və öyrənmə vasitəsidir: “tələ qurduq, deməli, qorunuruq” səhvdir.
:::

## Proksi-serverlər

### Əsas anlayış

Proksi müştəri ilə server arasında vasitəçidir və **iki ayrı bağlantı** qurur; buna görə tətbiq səviyyəsində məzmunu oxuya, süzə, keşləyə bilir. HTTP standartı (RFC 9110) üç forma deyir: proxy, gateway (tərs proksi) və tunnel (CONNECT). **Düz (forward) proksi müştərini, tərs (reverse) proksi serveri təmsil edir.**

| Növ | Nə edir |
| --- | --- |
| Düz proksi (Squid, TCP 3128) | İstifadəçilərin çıxışını süzür, autentifikasiya edir, qeyd edir, keşləyir, antivirusdan keçirir (ICAP), DLP ilə birləşir, IP gizlədir; məcburi çıxış nöqtəsidir |
| Tərs proksi (Nginx, HAProxy, Cloudflare) | TLS-i dayandırır (termination), yük paylayır, WAF (ModSecurity, Coraza) işlədir, keşləyir, sürət məhdudlaşdırır, serveri gizlədir, DDoS-u udur |

Müştəri proksiyə dörd yolla yönəlir: birbaşa sazlama (explicit proxy), PAC faylı (Proxy Auto-Configuration), WPAD (riskli: saxta PAC verilə bilər) və şəffaf proksi (transparent proxy, müştəri heç nə sazlamır). Proksi 407 (öz autentifikasiyası) qaytarır, 401 isə saytındır.

### HTTPS

- **CONNECT tuneli:** proksi yalnız domeni (SNI, CONNECT sətri), portu, vaxtı və həcmi görür; URL yolunu, məzmunu yox. ECH (Encrypted Client Hello) SNI-ni şifrələyəcək.
- **TLS inspection:** proksi iki ayrı TLS qurur, təşkilatın CA sertifikatı müştəriyə yüklənməlidir. Bu, razılaşdırılmış MITM-dir: HSM-də CA açarı, bank/səhiyyə istisnası, pinning edən tətbiqlər işləməyə bilər.
- Proksidə TLS bitirsə, arxa tərəf açıq qalır: re-encryption və backend sertifikatının yoxlanması lazımdır.

### Tərs proksinin detalları

- **Yük alqoritmləri:** round robin, çəkili, ən az bağlantı (least connections), IP heş.
- **health check** serverləri yoxlayır; sticky session sessiyanı eyni serverdə saxlayır, yaxşısı ortaq saxlamadır.
- **X-Forwarded-For** müştəri ünvanını ötürür; sağdan oxunur, sol tərəf saxtalaşdırıla bilər.

### Digər növlər və müqayisə

| Növ | Xüsusiyyət |
| --- | --- |
| Anonim proksi | Müştəri IP-sini gizlədir |
| Açıq proksi (open proxy) | Hər kəsə xidmət edir; spam və hücumda istifadə olunur |
| HTTP proksi / SOCKS (SOCKS5) | HTTP-ni başa düşür / istənilən TCP/UDP-ni məzmunsuz ötürür |
| Tətbiq proksisi (application proxy) | SMTP, FTP, DNS kimi protokolu tam şərh edir |
| Zəncirvari proksi | Bir neçə proksi; Tor |

**Proksi NAT deyil:** NAT başlıqdakı IP və portu dəyişir, bağlantı birdir, məzmuna baxılmır (OSI 3–4); proksi iki bağlantı qurur və 5–7 səviyyədə istifadəçiyə, URL-ə qərar verir. Stateful firewall və L4 yük balanslayıcısı da məzmunu görmür; müasir NGFW proksi funksiyası da daşıyır. Meyar: neçə ayrı bağlantı və hansı səviyyədə qərar.

### Hücumlar və səhvlər

- **X-Forwarded-For saxtalaşdırma:** IP limitindən yan keçmə; kənar proksi başlığı üzərinə yazır.
- **HTTP Request Smuggling:** proksi ilə server sorğunun sonunu fərqli görür.
- **Keşin zəhərlənməsi (cache poisoning):** keş açarına daxil olmayan başlıqla zərərli cavab keşlənir.
- **SSRF:** proksi daxili/metadata ünvanlarına çıxır; **açıq proksi**; serverin proksisiz əlçatan qalması; yol normallaşdırma fərqi; HTTP/3 (QUIC) ilə yan keçmə; tək nasazlıq nöqtəsi (iki qovşaq, active/passive); loglarda token.
- Konfiqurasiya: Squid-də son qayda `http_access deny all`, Nginx-də `X-Forwarded-For` real ünvanla əvəzlənir.

## Virtual özəl şəbəkələr (VPN)

### Anlayış

VPN (Virtual Private Network) etibarsız şəbəkə üzərində tunelləmə (inkapsulyasiya) ilə qorunan kanal qurur və üç xidmət verir: məxfilik, tamlıq, autentifikasiya (IPsec-də anti-replay də). **VPN şlüzdən sonrakı yolu və yoluxmuş cihazı qorumur**; şəbəkə etibarsız qalır.

| Təsnifat | Növlər |
| --- | --- |
| Model | Secure VPN (kriptoqrafiya: IPsec, OpenVPN, WireGuard); trusted VPN (provayder ayırır, MPLS VPN) |
| Arxitektura | Intranet (site-to-site), uzaqdan giriş (remote access), extranet (tərəfdaş) |
| Reallaşdırma | Router, firewall, proqram, VPN konsentrator |
| OSI | L2 VPN (L2TP) kadr daşıyır; L3 VPN (IPsec, WireGuard) IP paketi; TLS VPN portal və ya tunel rejimində |

### IPsec

IPsec (Internet Protocol Security) saytdan sayta standartdır.

| Komponent | Vəzifə |
| --- | --- |
| AH (Authentication Header) | Tamlıq və autentifikasiya, şifrələmə yox; NAT ilə işləmir |
| ESP (Encapsulating Security Payload) | Şifrələmə, tamlıq, autentifikasiya; praktikada həmişə |
| IKE (Internet Key Exchange) | Autentifikasiya, açar razılaşması, SA idarəsi; UDP 500, NAT varsa NAT-T ilə 4500 |
| SA (Security Association) | Bir istiqamətdə razılaşdırılmış alqoritm, açar, ömür; SPI (Security Parameter Index) onu göstərir |

- **Nəqliyyat rejimi:** yalnız faydalı yük şifrələnir, orijinal IP başlığı açıq qalır (host-host). **Tunel rejimi:** bütöv paket şifrələnir, yeni IP başlığı əlavə olunur (saytdan sayta). Xarici IP başlığı hər ikisində açıqdır.
- **IKEv2:** IKE_SA_INIT (alqoritm, Diffie-Hellman) → IKE_AUTH (sertifikat, EAP, PSK; ilk Child SA) → CREATE_CHILD_SA (əlavə tunel, açar yeniləmə). IKEv1 köhnəlmişdir; Aggressive Mode PSK heşini açıq verir.
- **Alqoritmlər:** AES-GCM, ChaCha20-Poly1305, HMAC-SHA-2, Diffie-Hellman ECP və Curve25519 qrupları, sertifikat və ya uzun PSK uyğundur; DES, 3DES, MD5, SHA-1, zəif DH qrupları və qısa/ortaq PSK yox. Anti-replay ardıcıllıq nömrəsi və sürüşən pəncərə ilə işləyir.

### TLS VPN, OpenVPN, WireGuard

| Protokol | Xüsusiyyət |
| --- | --- |
| TLS (SSL) VPN | Portal və ya tunel rejimi; TCP 443 asan keçir, amma qapı İnternetə açıq tətbiqdir |
| OpenVPN | İdarəetmə TLS ilə; UDP 1194, TCP-də TCP meltdown riski |
| WireGuard | Kiçik kod (təxminən 4000 sətir), sabit alqoritmlər (Curve25519, ChaCha20-Poly1305, BLAKE2s), `AllowedIPs` marşrut və icazədir; FIPS siyahısında yox, istifadəçi idarəetməsi yox |

### Status

| Protokol | Status |
| --- | --- |
| IPsec/IKEv2, WireGuard, OpenVPN/TLS VPN | Aktual |
| L2TP/IPsec | Köhnəlir: L2TP özü şifrələmir |
| PPTP | Etibarsız: MS-CHAPv2 sındırılıb, bir DES açarına gətirilir (parol uzunluğu fərq etmir) |
| MPLS VPN | Fərqli sinif: ayırır, şifrələmir |

### Tunel rejimi və sərtləşdirmə

- **Tam tunel (full tunnel):** bütün trafik şirkətdən keçir, kanal yüklənir. **Bölünmüş tunel (split tunnel):** yalnız şirkət trafiki; İnternet trafiki proksi və DLP-dən keçmir.
- **DNS sızması:** daxili DNS, kənar DNS-in məhdudlaşdırılması, kill switch. **MTU** azalır: ICMP bağlanmır, MSS clamping.
- **Hadisələr:** Colonial Pipeline (köhnə hesab, MFA yox); Pulse Secure, Fortinet, Ivanti qapı zəiflikləri.
- **Sərtləşdirmə:** MFA, sertifikat, köhnə hesabların söndürülməsi, yamaq prioriteti, minimum imtiyaz, idarəetmə interfeysi bağlı, cihaz yoxlaması, SIEM.
- **ZTNA (Zero Trust Network Access):** şəbəkəyə yox, konkret tətbiqə qoşur, etimad hər dəfə yoxlanır (NIST SP 800-207); IPsec saytdan sayta qalır.

:::warning
Mühazirənin köhnə slaydında proksi “NAT” adlanıb, PPTP “müdafiə olunan VPN” sayılıb: ikisi də səhvdir.
:::
