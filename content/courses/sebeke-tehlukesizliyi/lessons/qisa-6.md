+++
title = "Seqmentasiya, şəbəkələrarası ekranlar və IDS/IPS"
unit = "qisa"
order = 6
summary = "Mühazirənin bütün anlayışları bir-iki cümləlik cədvəllərdə: seqmentasiya, VLAN, DMZ, mikroseqmentasiya, firewall növləri, NAT, IPv6, VPN, IDS/IPS, yanlış nəticələr, jurnal və insident cavabı."
updated = 2026-11-09

[[source]]
title = "Mühazirə 6: Seqmentasiya, şəbəkələrarası ekranlar və IDS/IPS"
note = "Elmar Cabbarov, 2026–2027"
+++

Üç vasitə üç suala cavab verir: **seqmentasiya** şəbəkəni hansı hissələrə bölək, **firewall** hissələr arasında hansı trafik keçə bilər, **IDS/IPS** keçən trafikin içində hücum varmı. Universitet topologiyası, VLAN nömrələri və saylar şərti tədris nümunəsidir.

## Müdafiə arxitekturası

| Anlayış | Nədir |
| --- | --- |
| Məxfilik, bütövlük, əlçatanlıq | İcazəsiz oxunma, icazəsiz dəyişmə olmaması; qanuni istifadəçinin xidmətə çıxışı. Eyni tətbiqin ayrı məlumatlarına fərqli siyasət lazım ola bilər |
| Təhdid modeli | Hücumçu, başlanğıc imkanı, hədəf və yollar (yoluxmuş kompüter, oğurlanmış hesab, açıq LMS) |
| Hücumlar | Fişinq (hesab), zərərli proqram və fidyə proqramı, man-in-the-middle (əlaqəyə müdaxilə), SQL inyeksiyası (sorğu qüsuru), yanlış paylaşımla sızma |
| Çoxqatlı müdafiə (defense in depth) | Ayrı tədbirlər müxtəlif səhvləri tutur: seqmentasiya, firewall, IDS, IPS, host və tətbiq nəzarəti |
| Şimal–cənub (north–south) və şərq–qərb (east–west) | Xarici və daxili trafik; hücumlar içəridə şərq–qərb yayılır, perimetr firewall-u onu görmür |
| Yanal hərəkət (lateral movement) | Hücumçunun bir cihazdan başqa sistemə keçməsi |

IDS görür, IPS yol üzərində dayandıra bilir; firewall sərhəddə qərar verir; seqmentasiya yolları azaldır. Hamısı tətbiq avtorizasiyasını əvəz etmir. Paket yolunu bilmədən nəzarət seçmək olmaz.

## Seqmentasiya, VLAN, alt şəbəkə, ACL

| Anlayış | Nədir |
| --- | --- |
| Şəbəkə seqmentasiyası (network segmentation) | Şəbəkəni hissələrə bölüb aralarını siyasətlə məhdudlaşdırmaq; yayılmanı çətinləşdirir, dayandırmır |
| Yastı şəbəkə (flat network) | Seqmentasiyasız şəbəkə: hər cihaz hər cihazı görür |
| Fiziki / məntiqi | Ayrı kabel və kommutator; VLAN, VRF, virtual firewall |
| Makro / mikroseqmentasiya | Böyük zonalar; iş yükünə görə qayda. Bu meyar miqyasdır, fiziki/məntiqi isə qurulma üsuludur |
| Air gap | Tam fiziki ayrılma; USB və xidmət noutbuku ilə aşıla bilər (Stuxnet) |
| Karantin zonası | Şübhəli cihaz yalnız bərpa xidmətlərinə çıxır |
| VLAN | L2 yayım domeni; kommutator VLAN-lar arasında yayımı ötürmür |
| IP alt şəbəkəsi | L3 ünvan və marşrut sərhədi (10.10.30.0/24 = 256 ünvan, 254 host); özü heç nəyi qorumur |
| Access port / trunk / native VLAN | Bir VLAN-lı son cihaz portu; çox VLAN daşıyan əlaqə (802.1Q teq); işarəsiz kadrın VLAN-ı, iki tərəfdə uyğun olmalıdır |
| ACL | Başlıq meyarlarına görə icazə və ya qadağa; sessiya cədvəli saxlamır, istiqaməti interfeysə nəzərən yazılır |
| Eyni VLAN trafiki | Şlüzə getmir; host firewall, port izolyasiyası, private VLAN, simsiz müştəri izolyasiyası lazımdır |

:::exam
VLAN təkbaşına sərhəd deyil: L3 kommutator VLAN-lar arasında qaydasız marşrutlaşdırırsa, tələbə VLAN-ı maliyyə VLAN-ını görür. Alt şəbəkənin sərhədini dəyişmək yayım domenini kiçiltmir. VLAN nömrəsi parol deyil.
:::

## Ünvan planı və DMZ

| Anlayış | Nədir |
| --- | --- |
| Aktiv inventarı | Sahib, xidmət, həssaslıq, ünvan, asılılıq; DHCP qeydləri ilə əlaqələndirilir |
| Ünvan planı | Hər zonaya VLAN və /24 (10 tələbə, 20 kafedra, 30 maliyyə, 40 tətbiq, 50 qonaq, 60 idarəetmə, 70 DMZ, 80 baza, 90 infrastruktur, 100 yataqxana, 110 kitabxana, 120 karantin; VPN hovuzu 10.10.130.0/24); .1 şlüzdür |
| DMZ (demilitarized zone) | Xarici xidmətlər üçün bufer zona; TCP 443 (HTTPS) ilə giriş serveri, ondan tətbiq, ondan baza (TCP 5432); DMZ-dən bazaya birbaşa yol yoxdur |
| Tək və ya iki firewall | Tək qurğu sadədir, ortaq nasazlıq nöqtəsidir; iki qurğuda xarici firewall İnternet-DMZ, daxili DMZ-daxili keçidi süzür |
| Tərs proksi (reverse proxy) | DMZ giriş serveri, iki ayrı bağlantı qurur; NAT deyil |
| Keçid hostu (jump host) | Administratorun yeganə nəzarətli yolu; yüksək riskli aktiv, sessiyalar yazılır |

## Mikroseqmentasiya, Zero Trust, bulud, konteyner

| Anlayış | Nədir |
| --- | --- |
| Mikroseqmentasiya (microsegmentation) | Qayda iş yükünə qədər: LMS tətbiqi yalnız öz bazasına; hər şeyi bağlamır, yalnız lazım olanı açır |
| Tətbiq yeri | Hipervizor kommutatoru, paylanmış firewall, host agenti; agent quraşdırılıb ilə siyasət tətbiq olunur ayrı yoxlamadır |
| Zero Trust | Daxili şəbəkədə olmaq etibar vermir; qərar identiklik, cihaz, resurs və əməliyyata görə |
| Etiket riski | Etiket dəyişmək hüququ inzibati sayılır və audit edilir |
| VPC | Bulud alt şəbəkələri, marşrutlar, qaydalar; public subnet ad olaraq əlçatan demək deyil |
| AWS security group / network ACL | Stateful, yalnız icazə, qruplar birləşir / alt şəbəkədə stateless, nömrələnmiş qaydalar |
| Kubernetes NetworkPolicy | Namespace özü izolyasiya vermir; plagin lazımdır, default deny DNS-i də kəsir |
| Service mesh | Xidmət kimliyini yoxlayır, məlumat oxumaq hüququ vermir |

## Firewall növləri

Firewall (şəbəkələrarası ekran) trafiki qaydaya görə buraxır və ya dayandırır. Yerləşməyə görə: şəbəkə firewall-u, host firewall (Windows Defender Firewall), virtual və bulud firewall-u (AWS Security Group, Azure NSG).

| Növ | Nəyə baxır | Zəif cəhət |
| --- | --- | --- |
| Paket süzgəci (packet filter, stateless) | L3–L4: IP, port, protokol; hər paketə ayrıca | Cavab üçün geniş qayda; saxta paketi ayırmır |
| Stateful inspection | L3–L4 + sessiya cədvəli; cavabı buraxır, gözlənilməyəni atır | Məzmunu görmür, şifrəli məzmunu açmır |
| Tətbiq proksisi (application-level gateway) | L7, müştəri ilə server arasında vasitəçi (HTTP, FTP, SMTP) | Yavaş, hər protokola ayrıca |
| NGFW (next-generation firewall) | Stateful + tətbiq tanıma + istifadəçi + IPS + TLS yoxlaması | Baha; funksiyalar açılanda sürət düşür |
| WAF (Web Application Firewall) | HTTP sorğu: SQL inyeksiyası, XSS | Yalnız veb; avtorizasiya və şəbəkə firewall-u əvəzi deyil |

UDP üçün stateful vaxt həddi və portlarla izləyir; sessiya cədvəli tutumludur, asimmetrik marşrut cavabı tanıdamır.

:::exam
Stateful inspection ayrıca «seans səviyyəli firewall» deyil, L3–L4 süzgəcin sessiya cədvəli ilə formasıdır. Paket süzgəci IP (L3) və portlara (L4) baxır.
:::

## İcazə matrisi və qayda ardıcıllığı

| Anlayış | Nədir |
| --- | --- |
| Minimal səlahiyyət (least privilege) və default deny | Yalnız lazım olan açılır; icazəsiz hər şey dayanır |
| İcazə matrisi | Mənbə, təyinat, xidmət, məqsəd, məsul: İnternet-203.0.113.10 TCP 443, DMZ-LMS TCP 443, LMS-baza TCP 5432, keçid hostu TCP 22, DNS 53, vaxt UDP 123, jurnal TCP 6514, yeniləmə TCP 443 |
| Qayda ardıcıllığı | Yuxarıdan aşağı, ilk uyğun yekundur; anti-spoof, etibarsız paket, established cavab, dar icazələr, ən sonda default deny |
| Kölgədə qalmış qayda (rule shadowing) | Əvvəlki geniş qayda sonrakını işlətmir: 3-cü sətir «hamıdan printerə 9100 icazə», 15-ci «qonaqdan daxilə qadağa» |
| nftables | Nümunədə policy drop, ct state, interfeys və ünvan icazələri, log məhdudlaşdırılır; `inet` IPv6-ya `ip` meyarı ilə baxmır |
| Çıxış trafiki (egress) | Çıxan trafik də süzülür (C2 və sızma); domen icazəsi də risksizdir demək deyil |

:::exam
«Qayda var, amma işləmir» → əvvəl sıraya bax.
:::

## NAT, IPv6, VPN

| Anlayış | Nədir |
| --- | --- |
| NAT (Network Address Translation) | Ünvan sahəsini dəyişir; şifrələmə, autentifikasiya, proksi və icazə deyil |
| SNAT / DNAT | Çıxan paketin mənbəsi / gələnin təyinatı; DNAT də ayrıca firewall icazəsi tələb edir |
| Hairpin NAT | Daxili istifadəçi ictimai ada çıxanda; daxili DNS 10.10.70.10-a həll edir |
| IPv6, dual stack | IPv4 qadağası IPv6 qadağası deyil; eyni minimal siyasət hər iki ailədə |
| ICMPv6, RA Guard | ICMPv6 bütövlükdə bloklanmır; saxta marşrut elanlarına qarşı RA Guard |
| VPN yolu | Xarici sensor tunelin içini görmür; nəzarət tunel sonluğundan sonra: rol, cihaz vəziyyəti, hədəf. MPLS və L2TP özü şifrələmir, PPTP təhlükəsizdir sayılmır |
| Bölünmüş tunel (split tunnel) | Trafikin bir hissəsi birbaşa İnternetə; IPv6 və DNS yolları ayrıca yoxlanır |
| Alternativ yollar | İkinci şəbəkə, ehtiyat marşrut, bulud peering, şəxsi tunel nəzarəti yan keçə bilər |

## Firewall auditi

Audit planı faktiki konfiqurasiya ilə müqayisə edir. Tipik səhvlər: yuxarıda geniş icazə, köhnə ünvan obyekti, VLAN-lararası sərbəst routing, müddətsiz istisna, açıq idarəetmə interfeysi, yalnız IPv4 audit, nəzarətsiz ehtiyat yol, jurnal və saat (NTP) problemi. Dəyişiklikdən əvvəl sınaq, geri dönüş və ayrıca idarəetmə yolu; sıfır sayğac qaydanın lazımsız olduğunu sübut etmir.

## IDS və IPS

| Anlayış | Nədir |
| --- | --- |
| IDS (Intrusion Detection System) | Şübhəli hadisədə xəbərdarlıq verir; icazəsiz girişə aiddir, müəllif hüququna yox |
| IPS (Intrusion Prevention System) | Yol üzərində dayandıra bilir, yalnız düzgün yerləşdirildikdə və bloklama açıq olduqda |
| NIDS / NIPS | Paket və axınlara baxır (Snort, Suricata) |
| HIDS / HIPS | Host jurnalı, fayl, proses (Wazuh, OSSEC) |
| WIDS / WIPS | Simsiz şəbəkədə saxta giriş nöqtəsi |
| NBA | Axın (NetFlow) davranış analizi |
| EDR | HIDS-dən geniş son nöqtə telemetriyası və cavab |
| Out-of-band | SPAN portu və ya TAP-dan nüsxə; passiv, itki ola bilər |
| Inline | Paketin yolunda; qərar verir, amma nasaz olsa və ya səhv bloklasa xidməti dayandırır |
| Fail-open / fail-closed | Nasazlıqda trafik yoxlamasız keçir (əlçatanlıq) / dayanır (təhlükəsizlik) |
| Yerləşmə | Firewall-dan əvvəl bloklananı da görür, sonra buraxılanı; daxili baza sərhədi yanal hərəkəti görür |

## Aşkarlama üsulları

| Üsul | Mahiyyət | Zəiflik |
| --- | --- | --- |
| İmza əsaslı (signature-based detection) | Məlum nümunə; yanlış həyəcan azdır | Yeni (zero-day) hücum və variantlar |
| Anomaliya əsaslı (anomaly-based detection) | Normal profildən kənarlaşma | Çox yanlış həyəcan; norma dəyişir |
| Protokol vəziyyəti analizi (stateful protocol analysis) | Protokolun gözlənilən ardıcıllığı | Parser fərqi, natamam axın |
| Şifrəli trafik | TLS məzmunu passiv sensora görünmür; TLS yoxlaması və ya HIDS/EDR | TLS yoxlaması özü həssasdır |
| Yayınma (evasion) | Fraqment, seqment, kodlaşdırma, asimmetrik yol, yavaş davranış | Axını yığmaq, normallaşdırmaq |

## Suricata qaydası

Suricata və Snort oxşardır, amma qaydalar yoxlanmadan köçürülmür. Nümunə: `alert http 10.10.10.0/24 any -> 10.10.40.15 80` və seçimlər: `msg` mətn, `flow:to_server,established` qurulmuş axın, `http.method` və `http.uri` (normallaşdırılmış URI) ilə `content`, `startswith`, `sid` lokal identifikator, `rev` dəyişiklik nömrəsi. Bu görünürlük testidir, hücum imzası deyil. Yoxlama: `-T` konfiqurasiyanı, `-r` ilə PCAP oflayn; TLS içində susması gözlənilir. HOME_NET və EXTERNAL_NET tərifi yoxlanır.

## Yanlış nəticələr

| Anlayış | Nədir |
| --- | --- |
| TP / TN | Hücum tutuldu / normal hadisədə susdu |
| FP | Boş həyəcan; IPS-də qanuni istifadəçi bloklanır; çox olsa analitik yorulur (alert fatigue) |
| FN | Qaçırılmış hücum, daha təhlükəli |
| Qarışıqlıq matrisi (confusion matrix) | Real vəziyyət × sistem qərarı cədvəli |
| Precision / recall | TP/(TP+FP) və TP/(TP+FN); 50 hücum, 30 tutuldu, 40 xəbərdarlıq: 30/40 = 75% və 30/50 = 60% |
| Tənzimləmə (tuning) | Qaydanı dar istisnayla dəqiqləşdirmək; yeni qayda əvvəl aşkarlama rejimində |

TN verilmədiyindən ümumi düzgünlük hesablanmır; susan sensor aldadıcı yüksək düzgünlük göstərir.

## Jurnal və insident cavabı

| Anlayış | Nədir |
| --- | --- |
| Hadisə, qeyd, xəbərdarlıq, insident | Baş verən fəaliyyət; saxlanılan təsvir; qaydanın nəticəsi; CIA pozan hadisə |
| Jurnal təhlili | Saat sinxronu, DHCP və inventarla sahibin tapılması, NAT-dan əvvəl və sonra ünvanlar |
| SIEM | Mənbələri toplayır, normallaşdırır, əlaqələndirir: Splunk, QRadar, Sentinel, Elastic, OSSIM |
| Alətlər | Zeek (protokol jurnalları), Wazuh (host), ServiceNow (insident işi), Graylog və ELK (log mühiti) |
| SOAR | Cavab addımlarının avtomatlaşdırılması (Cortex XSOAR); səlahiyyət məhduddur |
| İş axını | Qəbul, çeşidləmə, sübut, təsir dairəsi, məhdudlaşdırma (karantin), aradan qaldırma, bərpa, bağlanma |
| NIST SP 800-61 Rev. 3 və CSF 2.0 | Cavab riskin idarəsi ilə bağlı; funksiyalar Govern, Identify, Protect, Detect, Respond, Recover |
| CERT, CSIRT | İnsident qəbulu və əlaqə komandası; cert.az, cert.gov.az, sciencecert.az |
| VirusTotal | Heş məlumatı kömək edir; həssas faylı yükləmək sızmadır |
| DDoS (Distributed Denial of Service) | Xətti doldurur; operator və təmizləmə xidməti (Cloudflare, Akamai); yük balanslaşdırma filtr deyil |

## Kompleks sınaq

Ən azı beş əlaqə, iki nəzarət nöqtəsi, bir müsbət və iki mənfi sınaq, sübut kimi qayda ID-li jurnal. `nc` uğursuzluğu təkbaşına sübut deyil; IPv6, VPN və ehtiyat keçid də sınanır. Rubrika 20 bal: zonalar 5, matris 5, yerləşdirmə 4, sübut 4, davamlılıq 2.
