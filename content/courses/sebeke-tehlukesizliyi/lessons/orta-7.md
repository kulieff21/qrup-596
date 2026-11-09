+++
title = "Tələ sistemləri, proksi-serverlər və virtual özəl şəbəkələr (VPN)"
unit = "orta"
order = 7
summary = "Hər anlayış 1–3 cümlədə: tələ sistemlərinin növləri və yerləşdirilməsi, düz və tərs proksi, HTTPS-də proksi, VPN, IPsec, WireGuard, köhnəlmiş protokollar, sərtləşdirmə və ZTNA."
updated = 2026-11-09

[[source]]
title = "Mühazirə 7: Tələ sistemləri, proksi-serverlər və virtual özəl şəbəkələr (VPN)"
note = "Elmar Cabbarov, 2026–2027"
+++

Bu üç texnologiya şəbəkənin fərqli nöqtələrində işləyir: **tələ sistemi** hücumçunu aldadıb izləyir, **proksi** trafikin arasına vasitəçi qoyur, **VPN** etibarsız şəbəkə üzərindən qorunan kanal qurur. Universitet topologiyası və saylar şərti tədris nümunəsidir.

## Tələ sistemləri

### Tələ sistemi nədir

Tələ sistemi (honeypot, “bal küpü”) hücumçunu cəlb etmək, hərəkətlərini qeydə almaq və öyrənmək üçün qəsdən qurulmuş saxta resursdur. Lens Spitsner (Lance Spitzner) onu dəyəri icazəsiz istifadədən gələn informasiya resursu adlandırır: adi serverin dəyəri gördüyü işdədir, tələnin dəyəri kiminsə ona toxunmasındadır. Heç bir iş funksiyası olmadığı üçün ona gələn istənilən bağlantı şübhəlidir; IDS isə milyonlarla normal paketin içindən zərərlini seçməyə çalışıb yanılır. Tələnin vəzifələri: hücumu erkən aşkar etmək, üsulları öyrənmək, hücumçunun vaxtını real sistemlərdən uzaqda itirtmək. O, hücumun qarşısını almır.

| Meyar | Firewall | IDS/IPS | Tələ |
| --- | --- | --- | --- |
| Vəzifə | Qaydalarla buraxır/bloklayır | Hücum əlaməti tapır; IPS dayandırır | Cəlb edir, davranışı qeydə alır |
| Baxdığı trafik | Sərhəddən keçən hamısı | Sensorun gördüyü hamısı | Yalnız tələyə gələn |
| Yanlış həyəcan | – | Çox | Çox az |
| Zəif cəhəti | İcazəli portdan keçən hücum | Şifrəli trafik | Ona gəlməyən hücumu görmür |

Tarixdə: 1986-da Clifford Stoll saxta hərbi sənədlərlə hücumçunu xəttdə saxladı (*The Cuckoo's Egg*, 1989); 1991-də Bill Cheswick saxta sistemlə hücumçunu aylarla izlədi (*An Evening with Berferd*); sonra Fred Cohen açıq Deception Toolkit alətini yazdı və 1999-da The Honeynet Project yarandı (“Know Your Enemy”, “honeynet” termini).

### Təsnifat

- **Məqsədə görə:** istehsalat tələsi (production honeypot) təşkilat daxilində erkən xəbərdarlıq üçündür, sadədir. Tədqiqat tələsi (research honeypot) yeni üsul, zərərli proqram və botnet davranışını öyrənir; universitetlər, CERT-lər, antivirus şirkətləri işlədir; çox məlumat verir, amma idarəsi çətindir.
- **Rola görə:** server tələsi gələn hücumu gözləyir (SSH, veb, baza); müştəri tələsi (client honeypot) özü zərərli saytları gəzib brauzer hücumlarını aşkar edir. Conpot sənaye sistemlərini (ICS/SCADA), Dionaea SMB, HTTP, FTP kimi protokolları təqlid edir. Tələlər adətən virtual və ya konteynerdədir, lakin hücumçu virtuallaşdırma izlərini görə bilər.

İmtahanda ən çox soruşulan bölgü qarşılıqlı əlaqə səviyyəsidir: tələ hücumçuya nə qədər çox imkan verirsə, bir o qədər çox məlumat toplayır və bir o qədər təhlükəlidir.

| Səviyyə | Necə işləyir | Məlumat | Risk | Nümunə |
| --- | --- | --- | --- | --- |
| Aşağı (low-interaction) | Yalnız bir neçə xidmət/protokol təqlidi, real ƏS yoxdur | Az: IP, port, giriş cəhdləri | Aşağı | Honeyd, Dionaea |
| Orta (medium-interaction) | Saxta fayl sistemində əmr yazılır, real ƏS-də icra olunmur | Orta: əmrlər, endirilən fayllar | Orta | Cowrie (shell rejimi) |
| Yüksək (high-interaction) | Real ƏS və xidmətlər | Çox: bütün davranış, yeni zəifliklər | Yüksək | Real Linux VM, Cowrie proxy rejimi |

Aşağı səviyyəli tələ də proqram zəifliyi ilə ələ keçirilə bilər; yüksək səviyyədə hücumçu real kök hüququ alır.

### Honeynet, honeytoken, deception

**Honeynet** bir neçə tələdən ibarət saxta şəbəkədir; tək tələdən fərqli olaraq tələlər arasında hərəkəti (lateral movement), hansı sistemin birinci axtarıldığını və çoxhostlu ardıcıllığı göstərir. **Honeytoken** sistem deyil, saxta məlumat parçasıdır: heç kimin işlətməməli olduğu hesab, “parollar.xlsx”, bazada saxta tələbə sətri, saxta API açarı. İstifadə olunanda həyəcan gəlir; saxta tələbənin poçtuna məktub düşürsə, baza sızıb. Məhdudiyyət: xəbər vermə kənar əlaqədən asılı ola bilər, ona görə səssizlik faylın açılmadığını sübut etmir. Thinkst Canarytokens belə tokenlər yaradır. **Aldatma texnologiyası (deception)** tələ və tokenləri kütləvi və avtomatik yayır; MITRE Engage hücumçunu aşkar etmə, saxta mühit göstərmə, öyrənmə üsullarını sistemləşdirir (məsələn, yaddaşdan parol oğurlanan stansiyalarda saxta administrator kimliyi).

### Yerləşdirmə

| Yer | Göstərir | Çatışmazlıq |
| --- | --- | --- |
| Xarici firewall-dan kənar | Kütləvi skan mənzərəsi | Çoxu internet səs-küyüdür |
| DMZ yanında ayrıca seqment | Açıq xidmətlərə hücumlar | Real serverlərdən ciddi ayrılmalıdır |
| Daxili şəbəkə | Daxilə keçmiş hücumçu, yoluxmuş cihaz | Kənardan gələni görmür; ən çox fayda, çünki hər bağlantı insidentdir |

:::figure
src = "m07-1.png"
alt = "Firewall hücumçunu DMZ-dəki real portala, daxili şəbəkəyə və ayrıca tələ seqmentinə (VLAN 99) yönəldir; tələdən çıxış bağlıdır, yalnız log serverinə log gedir."
caption = "Tələ seqmentinin yeri (şərti nümunə): tələdən yalnız log serverinə yol açıqdır."
:::

Təhlükəsiz yerləşdirmənin beş qaydası: ayrıca izolyasiya olunmuş VLAN; tələdən çıxan trafik firewall ilə kəsilir (əks halda tələ sıçrayış nöqtəsinə, pivot, çevrilir); tələdə real məlumat, parol, açar yoxdur; loglar dərhal kənar serverə gedir (hücumçu yerli logu silə bilər); yüksək səviyyəli tələ snapshot-dan bərpa olunan VM-də işləyir.

### Məlumat toplanması və SIEM

Honeynet Layihəsi üç tələb qoyur: **data control** (ələ keçirilmiş tələnin başqalarına ziyan verməsinin qarşısı), **data capture** (hücumçunun hər şeyinin gizli qeydi) və **data collection** (tələlərin qeydlərinin mərkəzdə birləşməsi). Hadisələr SIEM-ə gedir və bir qayda kifayətdir: tələyə bağlantı varsa, xəbərdarlıq. Cowrie qeydlərindən hücumçunun IP-si, parol lüğəti, əmrləri (məsələn, `uname -a`, MITRE ATT&CK T1082), skript ünvanı və fayl heşi çıxır; bunlar kompromitasiya indikatorlarıdır (IoC) və firewall-a, EDR-ə, təhdid kəşfiyyatına ötürülür. Parol sınaqları kobud güc hücumudur (T1110). Hücumçu kök hüququ alırsa, tələnin öz qeydləri etibarsızdır: şəbəkə və hipervizor səviyyəsində müstəqil yazı aparılır, faylların heşi götürülür, hüquqi iş üçün sübutun ötürülmə zənciri (chain of custody) qorunur.

**Cyber Kill Chain** üzrə tələ kəşfiyyatı, çatdırılmanı, istismarı, C2-ni (xarici qoşulma cəhdi qeydə düşür, ünvanı öyrənilir) və daxili tələdə hədəfə çatmanı yaxşı görür; quraşdırma orta səviyyədədir; silahlanma hücumçunun öz kompüterində baş verdiyi üçün görünmür.

### Alətlər və seçim

| Alət | Rolu |
| --- | --- |
| Cowrie | SSH/Telnet tələsi: shell rejimi UNIX-i təqlid edir, proxy rejimi real sistemə ötürür |
| Dionaea | Zərərli proqram tutmaq üçün SMB, HTTP, FTP təqlidi |
| Honeyd | Niels Provos çərçivəsi, bir kompüterdə minlərlə saxta host |
| Conpot | PLC/SCADA, Modbus, S7 |
| OpenCanary | Daxili şəbəkə üçün yüngül çoxxidmətli tələ |
| T-Pot | Deutsche Telekom platforması: iyirmidən çox tələ konteynerdə, Elastic Stack panelləri |
| Canarytokens | Honeytoken xidməti |

Seçim məqsəddən gedir: daxili skan üçün OpenCanary və ya saxta fayl serveri (aşağı); SSH botları üçün Cowrie (orta); zərərli proqram üçün Dionaea; tam metod üçün real ƏS və honeynet (yüksək); sızma üçün honeytoken. Kiçik İT komandası üçün honeynet çox vaxt düzgün deyil: bir neçə saxta xidmət və honeytoken sürətli nəticə verir. 

### Risklər və hüquqi məsələlər

Tələ yalnız ona gələni görür, IDS və SIEM-i əvəz etmir. Təcrübəli hücumçu standart banner, qeyri-təbii cavab vaxtı və VM izlərindən tələni tanıyır; Shodan bəzilərini etiketləyir, ona görə standart parametrlər işlədilmir. Ələ keçirilmiş tələ pivot olur və hücum universitetin IP-sindən görünür. Hüquqi tərəf: tələ passiv gözləməlidir (təhrik problem yaradır), hücumçunun IP-si fərdi məlumat sayıla bilər, qurmazdan əvvəl hüquq xidməti ilə razılaşdırılır; əks hücum (hack-back) icazəsiz girişdir.

:::exam
Honeypot qarşısını alma vasitəsi deyil, aşkarlama və öyrənmə vasitəsidir. “Tələ qurduq, deməli, qorunuruq” səhvdir; həm də az xəbərdarlıq əsasında IDS-i söndürmək olmaz.
:::

:::steps Daxili tələni universitetdə qurmaq
[[step]]
title = "Məqsəd və tələlər"
body = "Daxili skan və parol sınaqlarını görmək: istehsalat tələsi, aşağı/orta səviyyə. Laboratoriya, inzibati şəbəkə və server zonası üçün üç tələ, inandırıcı adlarla (fin-arxiv01, lms-backup) və SMB, SSH, RDP xidmətləri ilə."

[[step]]
title = "Firewall və SIEM"
body = "Tələdən çıxış qadağan, yalnız log serverinə TCP 6514 (TLS üzərindən syslog) açıq. SIEM qaydası: hər bağlantı yüksək dərəcəli xəbərdarlıq; skaner IP-ləri istisnadır."

[[step]]
title = "Reaksiya və yoxlama"
body = "IP hansı cihazdır və necə ayrılır: əvvəlcədən yazılır. Rüblük pentest xəbərdarlığın neçə dəqiqəyə gəldiyini ölçür."
:::

## Proksi-serverlər

### Proksi nədir

Proksi müştəri ilə server arasında vasitəçidir: müştəri sorğunu proksiyə göndərir, proksi onu öz adından serverə ötürüb cavabı qaytarır. **İki ayrı bağlantı** yaranır (TCP əsaslı HTTP-də; UDP/QUIC-də də ayrı əlaqələr qurulur). Ona görə proksi tətbiq səviyyəsində oxuya, dəyişdirə, keşləyə, qadağan edə bilir. HTTP standartı (RFC 9110) üç forma sayır: proxy (müştərinin seçdiyi), gateway (serverin qarşısında, gündəlik dildə tərs proksi) və tunnel (baytları dəyişmədən ötürür, CONNECT). **Düz (forward) proksi müştərini, tərs (reverse) proksi serveri təmsil edir.**

:::figure
src = "m07-2.png"
alt = "Yuxarıda düz proksi (Squid) daxili istifadəçilərin sorğularını İnternet saytlarına öz adından göndərir; aşağıda tərs proksi (Nginx, DMZ) İnternet istifadəçilərinin HTTPS sorğusunu Portal 1 və Portal 2-yə yönəldir."
caption = "Düz proksi müştərini, tərs proksi serveri təmsil edir."
:::

### Düz proksi

Daxili istifadəçilərlə İnternet arasındadır; sayt proksinin IP-sini görür. Ən məşhuru Squid (TCP 3128). Funksiyalar: məzmun süzmə (domen, URL, kateqoriya), autentifikasiya (Kerberos, NTLM, LDAP) ilə qeyddə istifadəçi adı, qeydiyyat (SIEM üçün mənbə), keşləmə (HTTPS yayıldıqca faydası azalıb), antivirus yoxlaması (ICAP), DLP ilə sızmanın qarşısı və IP gizlətmə. Ən dəyərli xüsusiyyəti məcburi çıxış nöqtəsi olmasıdır: firewall yalnız proksiyə çıxış verirsə, yoluxmuş kompüter hücumçunun serveri ilə birbaşa danışa bilmir.

Müştəri dörd yolla yönəldilir: birbaşa sazlama (explicit proxy), PAC faylı (Proxy Auto-Configuration, hər URL üçün qərar verən JavaScript), WPAD (PAC-ı DHCP/DNS ilə tapır; yerli hücumçu saxta PAC verə bildiyi üçün riskli) və şəffaf proksi (transparent proxy; müştəri heç nə sazlamır). Proksili sorğuda brauzer tam ünvanı göndərir (`GET http://host/yol`), proksi isə serverə yalnız yolu. Proksi icazəli şəbəkəni yoxlayır, autentifikasiya edir (407 proksinin, 401 saytın tələbidir), siyasəti tətbiq edir (403), keşə baxır, öz TCP bağlantısı ilə serverə gedir (Via başlığı), cavabı antivirusdan keçirir və hər şeyi qeydə yazır.

### Proksi və HTTPS

:::figure
src = "m07-3.png"
alt = "a) CONNECT tuneli: brauzer ilə sayt arasında proksidən keçən bir TLS sessiyası. b) TLS yoxlaması: proksi iki ayrı TLS sessiyası qurur, biri proksi sertifikatı, biri sayt sertifikatı ilə."
caption = "HTTPS-də düz proksinin iki rejimi."
:::

**CONNECT tuneli:** brauzer `CONNECT lms.example:443` göndərir, proksi baytları dəyişmədən ötürür. TLS brauzerlə sayt arasındadır, ona görə proksi yalnız domeni (CONNECT sətri və TLS ClientHello-dakı SNI), portu, vaxtı və həcmi görür; URL yolunu, parolu, məzmunu yox. ECH (Encrypted Client Hello, RFC 9849) SNI-ni şifrələyəcək, SNI əsaslı süzgəclər zəifləyəcək.

**TLS inspection:** məzmunu görmək üçün proksi saytla öz TLS-ini, müştəri ilə isə yerindəcə yaratdığı sertifikatla ayrı TLS qurur; sertifikatı təşkilatın CA-sı imzalayır və CA müştəriyə etibarlı kimi yüklənməlidir. Bu, razılaşdırılmış MITM-dir: proksi parolları, tibbi və bank məlumatını görür, ələ keçirilsə, bütün trafik açılır. Ona görə bank, səhiyyə, dövlət kateqoriyaları istisna olunur, istifadəçilərə bildiriş verilir, CA açarı HSM-də saxlanır; sertifikat bağlaması (pinning) edən mobil tətbiqlər işləməyə bilər. Şirkətin öz sertifikatı işçi kompüterlərinə yüklənir: bu, həm texniki, həm məxfilik qərarıdır.

### Tərs proksi

Serverlərin qarşısında durur; müştəri backend ünvanını görmür (başlıq və yönləndirmə sızmaları ayrıca yoxlanır). Nümunələr: Nginx, HAProxy, Apache HTTP Server, Traefik, Envoy, Cloudflare, AWS CloudFront. Funksiyalar: TLS-in dayandırılması (termination, sertifikat bir yerdə), yük balanslaşdırma, WAF (ModSecurity, Coraza), keşləmə və sıxılma, sürət məhdudlaşdırma (giriş səhifəsində kobud güc), serverin gizlədilməsi, DDoS-u serverə çatmamış udma və yol üzrə marşrutlaşdırma (/lms, /kitabxana). Arxitektura: tərs proksi DMZ-də, tətbiq daxili zonada, baza ayrıca zonada; İnternetdən yalnız proksinin TCP 443 portu açıqdır, proksi yalnız tətbiqin 8080, tətbiq yalnız PostgreSQL-in 5432 portuna çıxır.

:::warning
TLS proksidə bitirsə, proksi ilə tətbiq arasındakı trafik açıq gedə bilər: “saytda HTTPS var” daxili şifrələmə demək deyil. Daxili zona etibarlı deyilsə, ikinci TLS qurulur (re-encryption) və proksi backend sertifikatını və host adını yoxlayır (`proxy_ssl_verify on`).
:::

Yük alqoritmləri: round robin (eyni güclü serverlər), çəkili round robin (fərqli güclü), ən az bağlantı (least connections, uzun sessiyalar), IP heş (sessiya serverdədirsə). Proksi serverləri yoxlayır (health check, məsələn, hər 5 saniyə `/saglam`) və cavab verməyəni çıxarır. Sessiya serverdədirsə, sticky session lazımdır; daha yaxşısı sessiyanı Redis kimi ortaq yerdə saxlamaqdır. Müştəri ünvanı **X-Forwarded-For** başlığında zəncirlə ötürülür; serverin birbaşa gördüyü sonuncu proksidir, siyahının sol tərəfini müştəri yaza bildiyi üçün siyahı sağdan oxunur və etibarlı proksilər çıxılır.

### Digər növlər, NAT müqayisəsi

| Növ | Xüsusiyyət |
| --- | --- |
| Şəffaf | Müştəri sazlamır; qonaq Wi-Fi, provayder |
| Anonim | Müştəri IP-sini gizlədir |
| Açıq proksi (open proxy) | Hər kəsə xidmət edir; spam, hücum, blokdan yan keçmə |
| HTTP proksi | URL, başlıq, metod üzrə qərar |
| SOCKS (SOCKS5, RFC 1928) | Sessiya səviyyəsi, istənilən TCP/UDP, məzmunsuz, şifrələməsiz |
| Tətbiq proksisi (application proxy) | SMTP, FTP, DNS kimi protokolu tam şərh edir |
| Zəncirvari | Bir neçə proksi; Tor |

Proksi **NAT deyil**: hər ikisi daxili ünvanı gizlədir, amma NAT başlıqdakı IP və portu dəyişir, bağlantı birdir, məzmuna baxılmır (OSI 3–4). Proksi iki bağlantı qurur, 5–7 səviyyədə istifadəçi, URL, məzmun üzrə qərar verir. Stateful firewall (3–4) və L4 yük balanslayıcısı da məzmunu görmür, VPN şifrələyir və tətbiq məzmunu ilə işləmir. Müasir NGFW proksi funksiyası da daşıyır, tərs proksi həm yük balanslayıcısı, həm WAF ola bilir. Meyar: neçə ayrı bağlantı və cihaz hansı səviyyədə qərar verir.

### Hücumlar və səhv sazlamalar

- **X-Forwarded-For saxtalaşdırma:** hücumçu başlığı əvvəlcədən yazır (`10.0.0.1`), IP limitindən, qeydlərdən yan keçir. Həll: kənar proksi başlığı üzərinə yazır, tətbiq yalnız etibarlı proksiyə inanır (standart analoq: Forwarded, RFC 7239).
- **HTTP Request Smuggling:** Content-Length və Transfer-Encoding ziddiyyəti ilə proksi və server sorğunun sonunu fərqli görür, gizli ikinci sorğu başqasınınkına qoşulur (James Kettle, 2019). Qorunma: HTTP/2, ziddiyyətli sorğunu rədd, yeniləmə.
- **Keşin zəhərlənməsi (cache poisoning):** keş açarına daxil olmayan başlıq (X-Forwarded-Host) cavabı dəyişirsə, zərərli cavab keşlənir. Qorunma: şəxsi cavab keşlənmir (`private`/`no-store`), başlıq keş açarına və ya Vary-ə əlavə olunur.
- **Digər:** açıq proksi (giriş siyahısız Squid, IP qara siyahıya düşür); tətbiq serverinin proksisiz əlçatan olması (WAF-dan yan keçmə); proksi vasitəsilə SSRF (bulud metadata `169.254.169.254`); yol normallaşdırma fərqi (`/public/..%2fadmin`); HTTP/3 (QUIC) ilə TCP proksi siyasətindən yan keçmə; tək nasazlıq nöqtəsi (iki qovşaq, active/passive); URL-dəki sessiya identifikatorlarının loga düşməsi.
- **Konfiqurasiya:** Squid qaydaları yuxarıdan aşağı oxunur; təhlükəli portlar, lokal və daxili hədəflər bağlanır, sonda `http_access deny all` hamıya açıq proksinin qarşısını alır. Nginx-də `X-Forwarded-For` müştəri dəyəri ilə yox, real ünvanla əvəzlənir; ikinci proksi varsa, `set_real_ip_from` işlədilir.

:::reveal Proksi niyə iki ayrı bağlantı qurur və bu nə verir?
Müştəri–proksi və proksi–server ayrı bağlantılardır. Ona görə proksi məzmunu oxuya, süzə, keşləyə, istifadəçiyə və URL-ə görə qərar verə bilir. NAT-da bağlantı birdir və yalnız başlıq dəyişir.
:::

## Virtual özəl şəbəkələr (VPN)

### VPN nədir və nəyi qorumur

Virtual özəl şəbəkə (Virtual Private Network) etibarsız şəbəkə üzərindən iki nöqtə arasında qorunan məntiqi kanal qurur. Əsası tunelləmədir (inkapsulyasiya): paket başqa paketin içinə qoyulur; daxili ünvanlar özəl, xarici ünvanlar ictimai ola bilər. Tunelləmə özü məxfilik vermir, şifrələmə əlavə olunanda VPN üç xidmət verir: məxfilik, tamlıq, autentifikasiya (IPsec-də təkrar göndərmədən qorunma, anti-replay, də var).

:::warning
VPN iki tunel ucu arasında qoruyur; şlüzdən veb saytına qədər yolu qorumur və yoluxmuş noutbuku təmizləmir: zərərli proqram tunellə şirkət şəbəkəsinə girir. “VPN etibarsız şəbəkəni etibarlı edir” dəqiq deyil: şəbəkə etibarsız qalır.
:::

### Təsnifat

- **Model:** müdafiə olunan VPN (secure VPN) kriptoqrafiya ilə qoruyur (IPsec, OpenVPN, WireGuard); etibarlı VPN (trusted VPN) provayderin trafiki ayırmasına güvənir (MPLS VPN, şifrələmir). PPTP tarixi mənbələrdə “müdafiə olunan” verilsə də, sındırılıb; L2TP tək başına şifrələmir.
- **Arxitektura:** korporativ daxili (intranet, site-to-site, ofislər arası), uzaqdan giriş (remote access, müəllim evdən LMS-ə), korporativlərarası (extranet, bank ödəniş serverinə).
- **Reallaşdırma:** router, firewall, proqram, xüsusi aparat (VPN konsentrator); ən çox firewall və proqram əsaslıdır.
- **OSI:** L2 VPN (L2TP) kadr daşıyır; L3 VPN (IPsec, WireGuard) IP paketi; TLS VPN portal (tətbiqə giriş) və ya tunel (L3, bəzən L2) rejimindədir.

### IPsec

IPsec (Internet Protocol Security) IP səviyyəsində protokollar toplusudur, saytdan sayta standartdır.

| Komponent | Protokol | Vəzifə |
| --- | --- | --- |
| AH (Authentication Header) | IP 51 (RFC 4302) | Tamlıq, autentifikasiya, şifrələmə yox; xarici IP başlığını qoruduğu üçün NAT ilə işləmir |
| ESP (Encapsulating Security Payload) | IP 50 (RFC 4303) | Şifrələmə, tamlıq, autentifikasiya; praktikada həmişə ESP |
| IKE (Internet Key Exchange) | UDP 500, NAT-da 4500 | Autentifikasiya, açar razılaşması, SA idarəsi |

SA (Security Association) bir istiqamətdə trafik üçün razılaşdırılmış alqoritm, açar və ömürdür (iki istiqamət üçün iki SA); SPI (Security Parameter Index) qəbul edənə hansı SA-nı işlədəcəyini göstərir. SAD mövcud SA-ları, SPD qorunacaq trafikin siyasətini saxlayır.

:::figure
src = "m07-6.png"
alt = "Orijinal paket IP, TCP, Məlumat. ESP nəqliyyat rejimində IP açıq, ondan sonrakı hissə şifrələnir. Tunel rejimində yeni IP başlığı açıq, orijinal IP daxil olmaqla qalanı şifrələnir."
caption = "ESP nəqliyyat və tunel rejimləri."
:::

**Nəqliyyat rejimi** yalnız faydalı yükü qoruyur, orijinal IP başlığı açıq qalır (iki host arası, məsələn, baza replikasiyası). **Tunel rejimi** bütöv paketi şifrələyib yeni IP başlığı əlavə edir, daxili ünvanlar görünmür (saytdan sayta). Xarici IP başlığı hər ikisində açıqdır.

**IKEv2** (RFC 7296) tuneli dörd mesajda qurur: IKE_SA_INIT (alqoritmlər, Diffie-Hellman dəyərləri, sonrası şifrəli), IKE_AUTH (sertifikat, EAP və ya PSK ilə autentifikasiya, ilk Child SA, yəni ESP tuneli), CREATE_CHILD_SA (əlavə tunel, açar yeniləməsi; yeni Diffie-Hellman əlavə irəli məxfilik verir). IKEv1 RFC 9395 (2023) ilə köhnəlmişdir; Aggressive Mode PSK heşini açıq verdiyindən oflayn sındırmaya imkan yaradır. ESP ardıcıllıq nömrəsi və sürüşən pəncərə təkrar göndərməni atır. NAT aşkarlananda IKE və ESP UDP 4500-ə keçir (NAT-T, RFC 3948).

| Vəzifə | Yaxşı | Pis |
| --- | --- | --- |
| Şifrələmə | AES-GCM, AES-CBC + HMAC-SHA-2, ChaCha20-Poly1305 | DES, 3DES |
| Tamlıq | HMAC-SHA-256/384 | MD5, SHA-1 |
| Diffie-Hellman | Qrup 14, 19 və 20 (ECP), Curve25519 (qrup 31) | Qrup 1, 2, 5 |
| Autentifikasiya | Sertifikat, uzun təsadüfi PSK, EAP+MFA | Qısa və ya hamıda eyni PSK |

Paketin yolu: şlüz SPD ilə qorunmalı olduğunu görür, SA tapır, paketi AES-GCM ilə şifrələyib ESP başlığı və yeni IP başlığı (protokol 50) əlavə edir; provayder yalnız iki şlüzün ünvanını görür; qəbul edən şlüz SPI ilə SA tapıb ardıcıllığı və tamlığı yoxlayır, uğursuzdursa paketi atır. Tuneldə iki tərəfin parametrləri (versiya, alqoritm, DH, ömürlər) uyğun olmalıdır, qorunan alt şəbəkələr isə güzgü kimi (bir tərəfin “yerli”si o birinin “uzaq”ıdır). Tunel qurulmursa, əvvəl UDP 500/4500 və protokol 50 firewall-dan keçirmi, sonra alqoritm və identifikator, sonda sertifikat yoxlanır.

### TLS VPN, OpenVPN, WireGuard

TLS (SSL) VPN müştərisiz portal və ya tunel rejimindədir; TCP 443 əksər şəbəkədə açıq olduğundan asan keçir, amma VPN qapısı İnternetə açıq mürəkkəb veb tətbiqidir və ən ciddi hadisələr onun zəifliklərindən gəlib. OpenVPN idarəetməni TLS ilə, məlumatı öz protokolu ilə aparır; standart UDP 1194, TCP 443-də də sazlanır, lakin TCP üzərində TCP “TCP meltdown” yarada bilər, ona görə UDP üstündür. **WireGuard** 2020-də Linux 5.6-ya daxil olub, kodu təxminən 4000 sətirdir, alqoritmlər sabitdir (Curve25519, ChaCha20-Poly1305, BLAKE2s), danışıq olmadığı üçün endirmə hücumu yoxdur; çatışmazlıq: FIPS siyahısında deyil, istifadəçi idarəetməsi və dinamik IP protokolda yoxdur. Hər tərəfin açar cütü var; `AllowedIPs` həm marşrutlaşdırma, həm icazədir (`0.0.0.0/0` tam tunel verərdi).

| Meyar | IPsec/IKEv2 | OpenVPN | WireGuard |
| --- | --- | --- | --- |
| Üstünlük | Standart, aparat dəstəyi | Çevik, firewall-dan asan keçir | Sürət, kiçik kod |
| Çatışmazlıq | Mürəkkəb sazlama | Nisbətən yavaş | İstifadəçi idarəetməsi yox |
| İstifadə | Saytdan sayta | Uzaqdan giriş | Uzaqdan giriş, serverlərarası |

### Köhnəlmiş protokollar

IPsec/IKEv2, WireGuard və OpenVPN/TLS VPN aktualdır (TLS 1.2/1.3, vaxtında yeniləmə). L2TP/IPsec köhnəlir: L2TP özü şifrələmir, Microsoft 2024-də RRAS üçün köhnəlmiş elan edib. **PPTP etibarsızdır** (TCP 1723 və GRE): MS-CHAPv2 sındırılıb, tutulmuş mübadilə bir DES açarının (2⁵⁶) axtarışına gətirilir (Marlinspike və Hulton, 2012), parol uzunluğu fərq etmir; Microsoft 2024-ün oktyabrında PPTP və L2TP-ni RRAS üçün köhnəlmiş elan etdi, Windows Server 2025-in yeni quraşdırmasında qəbul edilmir. MPLS VPN fərqli sinifdir: məntiqi ayırır, şifrələmir.

### Tam və bölünmüş tunel

Tam tunel (full tunnel): bütün trafik təşkilat şlüzündən keçir, hamısı görünür, amma kanal yüklənir. Bölünmüş tunel (split tunnel): yalnız təşkilat trafiki tunelə düşür, İnternet trafiki birbaşa çıxır; sürətlidir, amma proksi və DLP-dən keçmir. DNS sızması (DNS sorğuları provayderə gedir) daxili DNS, tuneldənkənar DNS-in məhdudlaşdırılması, IPv4/IPv6 və DoH yoxlaması və kill switch ilə həll olunur. VPN MTU-nu azaldır: böyük fayl yüklənmir, adi sayt açılırsa, çox vaxt MTU-dur; ICMP “Fragmentation Needed” bağlanmır, şlüzdə TCP MSS azaldılır (MSS clamping).

### Hadisələr, sərtləşdirmə, ZTNA

2021-ci ilin aprelində Colonial Pipeline hücumu işlədilməyən, MFA-sız, parolu sızmış VPN hesabından başladı və kəmər günlərlə dayandı. Pulse Secure CVE-2019-11510 və Fortinet CVE-2018-13379 autentifikasiyasız kimlik sızmasına imkan verdi; Ivanti Connect Secure CVE-2023-46805 (autentifikasiyadan yan keçmə) və CVE-2024-21887 (əmr inyeksiyası) birlikdə autentifikasiyasız əmr icrası verdi. CISA və NSA 2021-də sərtləşdirmə tövsiyəsi dərc etdi. Tədbirlər: hamı üçün MFA, sertifikat PSK-dan üstündür, işlədilməyən hesabların söndürülməsi, qapı üçün yamaq prioriteti, minimum imtiyaz (ən az lazım olan alt şəbəkə), idarəetmə interfeysi bağlı, cihaz yoxlaması (ƏS, disk şifrəsi, EDR), qeydlər SIEM-də.

Ənənəvi VPN “içəridəsənsə, etibarlısan” məntiqindədir. Sıfır etimad (NIST SP 800-207) hər sorğunu ayrıca yoxlayır; **ZTNA (Zero Trust Network Access)** istifadəçini şəbəkəyə yox, icazəli tətbiqə qoşur, kimlik və cihaz vəziyyəti hər dəfə yoxlanır, daxili hərəkət məhduddur, tətbiqlər İnternetdən görünmür. ZTNA VPN-i tam əvəz etmir: saytdan sayta IPsec qalır.

:::note Köhnə slaydlarla fərq
Köhnə slaydda proksi “NAT” adlanıb, PPTP “müdafiə olunan VPN” sayılıb, “etibarlı VPN: MPLS və L2TP” qruplaşdırılıb; üçü də dəqiq deyil.
:::
