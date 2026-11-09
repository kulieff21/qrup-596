+++
title = "Seqmentasiya, şəbəkələrarası ekranlar və IDS/IPS"
unit = "orta"
order = 6
summary = "Hər anlayış izahla: seqmentasiya və VLAN, DMZ və ünvan planı, mikroseqmentasiya, firewall növləri və qayda ardıcıllığı, NAT, IPv6, VPN, IDS/IPS, Suricata qaydası, precision və recall, jurnal və insident cavabı."
updated = 2026-11-09

[[source]]
title = "Mühazirə 6: Seqmentasiya, şəbəkələrarası ekranlar və IDS/IPS"
note = "Elmar Cabbarov, 2026–2027"
+++

Üç vasitə üç suala cavab verir: **seqmentasiya** şəbəkəni hansı hissələrə bölək, **firewall** hissələr arasında hansı trafik keçə bilər, **IDS/IPS** keçən trafikin içində hücum varmı. Universitet topologiyası, VLAN nömrələri, ünvanlar və saylar şərti tədris nümunəsidir.

## Müdafiə arxitekturası

Dərs platforması (LMS), tələbə bazası, maliyyə sistemi və yataqxana Wi-Fi şəbəkəsi eyni infrastrukturda ola bilər, lakin riskləri fərqlidir. Məxfilik, bütövlük və əlçatanlıq üçün eyni tətbiqin ayrı məlumatlarına fərqli siyasət lazım ola bilər (kataloq axtarışı açıqdır, oxucunun kitab tarixçəsi isə yox), ona görə şəbəkə sərhədi ilə yanaşı tətbiq avtorizasiyası da işləməlidir.

**Təhdid modeli** hücumçunu, başlanğıc imkanını (yoluxmuş laboratoriya kompüteri, oğurlanmış hesab, açıq LMS), hədəfini və yollarını təsvir edir. Hücum növləri: fişinq (hesab və ilkin giriş), zərərli proqram və fidyə proqramı, man-in-the-middle (əlaqəyə müdaxilə), SQL inyeksiyası (tətbiqin sorğu qurmasındakı qüsur), yanlış paylaşımla sızma.

**Çoxqatlı müdafiədə (defense in depth)** ayrı tədbirlər müxtəlif səhvləri məhdudlaşdırır:

| Tədbir | Vəzifə | Özbaşına həll etmir |
| --- | --- | --- |
| Seqmentasiya | Laboratoriyadan maliyyəyə yolları azaltmaq | İcazəli tətbiqdə oğurlanmış hesabı |
| Firewall | Bazaya yalnız tətbiqdən bağlantı buraxmaq | Qanuni sessiyadakı zərərli sorğunu |
| IDS | Daxili skanı bildirmək | Trafiki saxlamağı |
| IPS | Tanınmış zərərli sorğunu yolda kəsmək | Tanımadığı hücumu |
| Host və tətbiq nəzarəti | Proses, fayl, istifadəçi hüquqları | İnternet xəttinin doldurulmasını |

Şimal–cənub (north–south) trafiki xarici şəbəkə ilə, şərq–qərb (east–west) trafiki daxili sistemlər arasındadır. Perimetr firewall-u yalnız birincini görür, hücumlar isə içəridə şərq–qərb yayılır. Hücumçunun bir cihazdan başqasına keçməsi **yanal hərəkətdir (lateral movement)**. Paket yolunu çəkmədən nəzarət seçmək olmaz: qayda düzgün olsa da, paket həmin qurğudan keçməyə bilər.

## Seqmentasiya, VLAN, alt şəbəkə və ACL

Şəbəkə seqmentasiyası (network segmentation) şəbəkəni hissələrə bölüb aralarındakı əlaqəni siyasətlə məhdudlaşdırır. Seqmentasiyasız şəbəkə **yastı şəbəkədir (flat network)**: yoluxmuş noutbuk maliyyə serverini birbaşa yoxlaya bilər. Seqmentasiya yayılmanı çətinləşdirir, amma zəmanət vermir: icazəli bağlantı, səhv qayda və ya ələ keçirilmiş idarəetmə hesabı sərhədi aşa bilər.

| Meyar | Növlər |
| --- | --- |
| Necə qurulur | Fiziki (ayrı kabel, kommutator; ekstremal hal air gap, USB və xidmət noutbuku ilə aşıla bilər, Stuxnet) / məntiqi (VLAN, VRF, virtual firewall; bir sazlama səhvi ayrılmanı sıfırlayır) |
| Miqyas | Makroseqmentasiya (böyük zonalar, zona daxilində yanal hərəkət qalır) / mikroseqmentasiya (iş yükünə görə qayda) |
| Əsas | Funksiya, risk, identiklik |

Bu meyarlar bir-birini istisna etmir. **Karantin zonası** şübhəli cihazı yalnız bərpa xidmətlərinə çıxarır.

**VLAN** ikinci səviyyədə (L2) ayrıca yayım domenidir; **IP alt şəbəkəsi** üçüncü səviyyədə (L3) ünvan və marşrutlaşdırma sərhədidir. Praktikada bir VLAN-a bir alt şəbəkə verilir, amma anlayışlar eyni deyil: eyni yayım domenində iki prefiks L2 izolyasiyası yaratmır. Yayım domenini VLAN və ya marşrutlaşdırılan interfeys bölür, alt şəbəkə sərhədini dəyişmək onu kiçiltmir. 10.10.30.0/24 üçün 32 − 24 = 8 host biti, yəni 256 ünvan, .0 və .255 xaric 254 host.

Access port son cihazı bir VLAN-a bağlayır; trunk bir neçə VLAN daşıyır (IEEE 802.1Q teqi); işarəsiz kadrın düşdüyü native VLAN iki tərəfdə uyğun qurulmalıdır. Sərtləşdirmə: istifadə olunmayan port bağlanır, son cihaz portunda trunk söndürülür, yalnız lazımi VLAN-lar daşınır, idarəetmə VLAN-ı istifadəçiyə verilmir. VLAN nömrəsi parol deyil. Wi-Fi-da ayrıca SSID kifayət etmir, onun VLAN-a və firewall siyasətinə bağlanması yoxlanır.

Girişə nəzarət siyahısı (ACL) başlıq meyarlarına (mənbə, təyinat, protokol, port) görə icazə verir və ya qadağan edir, tam sessiya cədvəli saxlamır; istiqaməti konkret interfeysə nəzərən yazılır. Tələbə VLAN-ından maliyyəyə paketi şlüz (məsələn, L3 kommutator) qərarlaşdırır, İnternet firewall-u yox. Eyni VLAN-dakı cihazlar şlüzə getmədən əlaqə qurur, bunun üçün host firewall, port izolyasiyası, private VLAN və simsiz müştəri izolyasiyası lazımdır.

:::exam VLAN təkbaşına sərhəd deyil
L3 kommutator VLAN-lar arasında hər şeyi marşrutlaşdırırsa və ACL yoxdursa, tələbə VLAN-ı ilə maliyyə VLAN-ı bir-birini görür. Seqmentasiya yalnız zonalar arasında qayda tətbiq edən nöqtə (firewall, ACL) olanda işləyir.
:::

## Ünvan planı və DMZ

Plandan əvvəl aktiv inventarı hazırlanır: sahib, xidmət, məlumat həssaslığı, ünvan, asılılıq. Dinamik ünvanlar DHCP qeydləri ilə əlaqələndirilir. Nümunə plan: VLAN 10 tələbə, 20 kafedra, 30 maliyyə, 40 tətbiqlər, 50 qonaq Wi-Fi, 60 idarəetmə, 70 DMZ, 80 bazalar, 90 infrastruktur (DNS, vaxt, jurnal, yeniləmə), 100 yataqxana, 110 kitabxana, 120 karantin; hər biri 10.10.N.0/24, .1 şlüz, DHCP .100–.230. VPN hovuzu (10.10.130.0/24) Ethernet VLAN-ı deyil. Sabit ünvanlar: ictimai LMS 203.0.113.10, DMZ giriş 10.10.70.10, LMS tətbiqi 10.10.40.10, LMS bazası 10.10.80.10 (TCP 5432), keçid hostu 10.10.60.10, DNS 10.10.90.53, NTP 10.10.90.123, jurnal 10.10.90.20, yeniləmə 10.10.90.30. Kataloq ilə oxu zalı eyni VLAN-dadır, host firewall lazımdır.

**DMZ** (demilitarized zone) xaricdən əlçatan xidmətlər üçün bufer zonadır. Üçpilləli yol: İnternet DMZ giriş serverinə TCP 443 (HTTPS) ilə, giriş serveri LMS tətbiqinə ayrıca bağlantı ilə, tətbiq bazaya TCP 5432 ilə gedir; DMZ-dən bazaya birbaşa yol yoxdur.

:::figure
src = "m06-1.png"
alt = "Sxem: İnternet xarici firewall-dan keçib DMZ-dəki tərs proksiyə TCP 443 ilə gəlir; daxili firewall tətbiq və baza zonalarına seçilmiş yollar açır; zonalar arasında default deny."
caption = "Xarici sərhəd, DMZ və daxili zonalar; zonalar arasında default deny."
:::

DMZ tək çoxinterfeysli firewall (sadə, amma ortaq nasazlıq nöqtəsi) və ya iki firewall (xarici İnternet-DMZ, daxili DMZ-daxili) ilə qurulur; eyni geniş icazə hər ikisindədirsə, say qorumanı artırmır. DMZ serveri ələ keçsə də, daxiliyə birbaşa yol olmamalıdır; DMZ-dən daxilə açılan TCP 443 də risksiz deyil. Tərs proksi (reverse proxy) iki ayrı bağlantı qurur və NAT deyil. İdarəetmə üçün İnternetdən SSH açılmır: administrator güclü autentifikasiya ilə keçid hostuna (jump host) girir, oradan təyin olunmuş serverə keçir; keçid hostu yüksək riskli aktivdir, sessiyaları yazılır.

## Mikroseqmentasiya, Zero Trust, bulud, konteyner

Mikroseqmentasiya (microsegmentation) qaydanı iş yükünə (server, virtual maşın, konteyner, xidmət) qədər endirir. Məqsəd hər şeyi bağlamaq deyil: LMS tətbiqi yalnız öz bazasına (TCP 5432), maliyyə bazasına yox; keçid hostu seçilmiş serverlərə TCP 22. Tətbiq yeri: hipervizorun virtual kommutatoru, paylanmış firewall və ya host agenti. Agent quraşdırılıb ilə siyasət indi tətbiq olunur ayrı yoxlamalardır.

**Zero Trust** daxili şəbəkədə olmağa görə etibar vermir; qərar identiklik, cihaz vəziyyəti, resurs və əməliyyata əsaslanır, mikroseqmentasiya onun vasitələrindən biridir. TCP 443 icazəsi tələbəyə başqa tələbənin qiymətini dəyişmək hüququ vermir, tətbiq hər sorğuda avtorizasiya yoxlamalıdır. Etiket əsaslı qaydada etiketi dəyişmək hüququ inzibati sayılır və audit edilir; asılılıqlar əvvəl müşahidə olunur, xidmət sahibi ilə yoxlanır, sonra dar qaydaya çevrilir.

| Mühit | Qeyd |
| --- | --- |
| VPC (Virtual Private Cloud) | Alt şəbəkə, marşrut cədvəli, qaydalar birlikdə; public subnet adı əlçatanlıq demək deyil |
| AWS security group | Resurs interfeysində, stateful, yalnız icazə qaydaları, qrupların icazələri birləşir (birinci uyğun qadağa yoxdur) |
| Network ACL | Alt şəbəkədə, stateless, nömrələnmiş qaydalar, müvəqqəti portlar ayrıca |
| Kubernetes NetworkPolicy | Namespace özü izolyasiya vermir; NetworkPolicy-ni tətbiq edən plagin lazımdır; default deny DNS və asılılıqları da kəsir, hər iki istiqamət nəzərə alınır |
| Service mesh | Xidmət kimliyini yoxlayır, məlumat oxumaq hüququ vermir |

:::exam Mikroseqmentasiya hər şeyi bağlamır
«Mikroseqmentasiyada hər qovşaq tamamilə izolyasiya olunur» səhvdir, yalnız lazım olan bağlantılara icazə verilir. Seqmentasiya yayılmanı məhdudlaşdırır və çətinləşdirir, tam dayandırmır.
:::

## Firewall növləri

Şəbəkələrarası ekran (firewall) trafiki siyasətə görə buraxır və ya dayandırır. Yerləşməyə görə: şəbəkə firewall-u (sərhəddə), host firewall (məs. Windows Defender Firewall, çıxış qaydaları da ola bilər), virtual və bulud firewall-u (AWS Security Group, Azure NSG). «Aparat firewall» ifadəsi yoxlama dərinliyini göstərmir.

| Növ | Nəyə baxır | Məhdudiyyət |
| --- | --- | --- |
| Paket süzgəci (packet filter, stateless) | L3–L4: IP, protokol, port; hər paketə ayrıca | Cavab üçün geniş port diapazonu; saxta paketi ayırmır |
| Stateful inspection | Başlıq + sessiya cədvəli; cavabı buraxır, gözlənilməyəni atır | Şifrəli məzmunu açmır; sessiya içindəki zərərli sorğunu yoxlamır |
| Tətbiq proksisi (application-level gateway) | L7, protokol əmrləri (HTTP, FTP, SMTP), iki ayrı bağlantı | Yavaş; hər protokola ayrıca; mənbə IP-nin ötürülməsi ayrıca qurulur |
| NGFW (next-generation firewall) | Stateful + tətbiq tanıma + istifadəçi + IPS + TLS yoxlaması | Standart yoxdur; baha; funksiyalar açıq olanda sürət düşür |
| WAF (Web Application Firewall) | HTTP metod, URI, başlıq, gövdə: SQL inyeksiyası, XSS | Yalnız veb; avtorizasiya və şəbəkə firewall-unu əvəz etmir |

WAF üçün proqramlaşdırma dərsində SQL mətni qanuni cavab ola bilər; obyekt identifikatoru ilə başqa tələbənin sənədini oxumaq normal HTTP sorğusu görünür, tətbiq avtorizasiyası lazımdır. UDP-də stateful qurğu ünvan, port və vaxt həddi ilə izləyir; ICMP-də tip və kod nəzərə alınır. Sessiya cədvəlinin tutumu məhduddur; asimmetrik marşrutda cavab tanınmaya bilər, ehtiyat qurğular sessiya sinxronluğu tələb edir. Firewall seçərkən sürət bütün yoxlamalar açıq ölçülür.

:::exam Köhnə OSI təsnifatı
Paket süzgəci IP (L3) və portlara (L4) baxır. Stateful inspection ayrıca «seans səviyyəli firewall» deyil, L3–L4 süzgəcin sessiya cədvəli ilə formasıdır.
:::

## İcazə matrisi və qayda ardıcıllığı

Minimal səlahiyyət (least privilege) yalnız lazım olanı açır, standart qadağa (default deny) qalanını dayandırır. «Kafedra serverlərə çıxsın» yoxlana bilməz; «kafedra cihazları DMZ girişinin TCP 443 xidmətinə çıxsın» konkretdir. İcazə matrisi mənbə, təyinat, xidmət, məqsəd və məsulu yazır: İnternet-203.0.113.10 TCP 443; VLAN 10 və 20-DMZ TCP 443; DMZ-LMS TCP 443; LMS-baza TCP 5432; keçid hostu-serverlər TCP 22; DNS UDP və TCP 53; vaxt UDP 123; jurnal TCP 6514 (TLS üzərindən syslog); yeniləmə və kataloq TCP 443. Qonaq və yataqxana şlüzdəki məhdud resolverə çıxır; karantin yalnız ünvan, məhdud DNS və yeniləməyə.

Klassik siyasətdə qaydalar yuxarıdan aşağı yoxlanır və **ilk uyğun qayda yekundur** (AWS Security Group başqa cür işləyir). Məntiqi sıra: anti-spoof (mənbə giriş zonasına uyğun deyil), etibarsız vəziyyətli paket, icazəli sessiyanın cavabı, qonaqdan şlüz xidmətləri, ictimai LMS üçün hairpin DNAT istisnası, qonaqdan daxilə ümumi qadağa, İnternetdən DMZ-yə TCP 443, matrisdəki tətbiq əlaqələri, administrator VPN-dən keçid hostuna SSH, ortaq xidmətlər, xaricə çıxış, ən sonda default deny. Təkcə RFC 1918 bağlamaq kifayət deyil; universitetin ictimai və IPv6 prefiksləri də daxildir.

**Kölgədə qalmış qayda (rule shadowing):** 3-cü sətirdə «hamıdan printerə TCP 9100 icazə», 15-ci sətirdə «qonaqdan daxilə qadağa» varsa, qonaq trafiki 3-cüyə uyğun gəlir və 15-ə çatmır. Həll yalnız qadağanı qaldırmaq deyil, printer icazəsinin mənbəsini daraltmaqdır.

:::exam
Situasiya sualında «qayda var, amma işləmir» deyilirsə, əvvəl sıraya bax.
:::

nftables nümunəsi policy drop, `ct state invalid drop`, `established,related accept`, üç icazə (VLAN 10-DMZ 443, DMZ-tətbiq 443, tətbiq-baza 5432), sonra ayrıca məhdudlaşdırılmış log qaydası və drop göstərir. `inet` iki IP ailəsini əhatə edir, amma `ip` meyarı yalnız IPv4-dür, IPv6 üçün ayrıca icazə yazılmalıdır. **Çıxış trafiki (egress)** də süzülür: bazanın İnternetə TCP 443 açması C2 və sızma kanalıdır; təsdiqli yeniləmə serveri və DNS daha dar seçimdir.

## NAT, IPv6 və VPN

NAT (Network Address Translation) ünvan sahəsini dəyişir; şifrələmə, autentifikasiya, proksi və giriş icazəsi deyil. SNAT çıxan paketin mənbəsini, DNAT gələn paketin təyinatını dəyişir; port çevrilməsi bir ictimai ünvanı paylaşır. Nümunə: 198.51.100.25 → 203.0.113.10:443 DNAT ilə 10.10.70.10:443 olur, amma ayrıca firewall icazəsi də lazımdır; tələbə 10.10.10.25 xaricə 203.0.113.20-dən çıxır; DMZ-tətbiq bağlantısında NAT yoxdur. Linux-da DNAT prerouting-də, SNAT postrouting-də olur, filtr hansı ünvanı görür məhsuldan asılıdır və iz qeydi ilə təsdiqlənir. Daxili istifadəçi ictimai LMS adına çıxanda hairpin NAT lazım ola bilər. NAT jurnalı vaxt, protokol və portu saxlamalıdır.

İkili protokol mühitində (dual stack) IPv4 qadağası IPv6-ya keçmir; qlobal IPv6 ünvanlı bazaya ayrıca qayda yazılır (nümunə prefiks 2001:db8:6::/48). ICMPv6 bütövlükdə bloklanmır (qonşu aşkarlanması, Packet Too Big), saxta marşrut elanlarına qarşı RA Guard nəzərdən keçirilir; fraqmentlər sınanır.

VPN-də xarici sensor tunelin içini görmür; nəzarət tunel sonluğundan sonra qurulur: rol, cihaz vəziyyəti, hədəf xidməti. 10.10.130.0/24 hovuzuna serverlərə ümumi giriş vermək oğurlanmış hesabı geniş hüquqa çevirir. VPN şifrələmə etibarsız şəbəkəni etibarlı etmir; MPLS və L2TP özü məxfilik vermir, PPTP təhlükəsiz sayılmır. Bölünmüş tunel (split tunnel) trafikin bir hissəsini birbaşa İnternetə göndərir; IPv6 və DNS yolları ayrıca yoxlanır. İkinci şəbəkəyə qoşulmuş host, ehtiyat marşrut, bulud peering və icazəsiz şəxsi tunel də nəzarəti yan keçir.

## Firewall auditi

Audit planı faktiki konfiqurasiya ilə tutuşdurur. «Sayğac sıfırdır» qaydanın lazımsız olduğunu sübut etmir (illik xidmət), silməzdən əvvəl müşahidə lazımdır. Tipik səhvlər: yuxarıda geniş icazə, köhnə ünvan obyekti (başqa serverə keçən icazə), VLAN-lararası sərbəst routing, müddətsiz test istisnası, açıq idarəetmə interfeysi (ayrı zona, MFA), yalnız IPv4 audit, nəzarətsiz ehtiyat yol, jurnal və saat (NTP) problemi. Dəyişiklik əvvəl sınanır, cari konfiqurasiya saxlanır, geri dönüş və administratorun öz yolunu bağlamamaq üçün ayrıca çıxış hazırlanır.

## IDS və IPS

Firewall «porta icazə var» deyir, amma 443-dən keçən paketin içində eksploit olub-olmadığını bilmir. **IDS** (Intrusion Detection System) şübhəli uyğunluqda xəbərdarlıq verir (söhbət icazəsiz girişdən gedir, müəllif hüququndan yox); **IPS** (Intrusion Prevention System) trafiki dayandıra bilir. Hər xəbərdarlıq uğurlu müdaxilə deyil: cəhd, ötürülmüş trafik və təsdiqlənmiş kompromitasiya ayrılır.

| Növ | Mənbə |
| --- | --- |
| NIDS və NIPS | Paket və axın (Snort, Suricata); şifrələmə, paket itkisi, görünməyən yol |
| HIDS və HIPS | Host jurnalı, fayl bütövlüyü, proses (Wazuh, OSSEC) |
| WIDS və WIPS | Simsiz şəbəkədə saxta giriş nöqtəsi; aktiv müdaxilə qonşuya toxuna bilər |
| NBA | Axın (NetFlow), həcm, əlaqə qrafı; dəyişmiş norma hücum sayıla bilər |
| EDR | HIDS-dən geniş telemetriya və cavab, eyni termin deyil |

**Out-of-band** rejimdə NIDS SPAN portundan və ya TAP-dan nüsxə alır; SPAN-ın tutumu aşıla bilər, TAP da ölçülməlidir. **Inline** rejimdə IPS paketi ötürməzdən əvvəl yoxlayıb atır; Suricata trafiki passiv oxuyursa, `drop` real paketi saxlamır. IPS yalnız trafik üzərindən keçəndə, qayda hücumu tanıyanda və bloklama açıq olanda qarşısını alır. Passiv IDS-in sonradan reaksiyası ilk zərərli sorğunu qaçıra bilər, inline IPS isə yanlış müsbətdə qanuni imtahan cavabını dayandırır.

:::figure
src = "m06-2.png"
alt = "Yuxarıda passiv IDS kommutatorun SPAN və ya TAP nüsxəsindən xəbərdarlıq verir; aşağıda inline IPS İnternet ilə server arasında yalnız buraxılan trafiki ötürür."
caption = "Passiv IDS nüsxə alır, inline IPS paketin yolunda qərar verir."
:::

Nasazlıqda **fail-open** trafikin yoxlamasız keçməsidir (əlçatanlıq qorunur), **fail-closed** dayanmasıdır (təhlükəsizlik qorunur): bank üçün fail-closed, xəstəxananın təcili sistemi üçün fail-open məntiqli ola bilər; real nasazlıq davranışı sınanır. Sensor firewall-dan əvvəl bloklananı da görür, sonra buraxılanı; daxili baza sərhədində sensor yanal hərəkəti tutur.

## Aşkarlama üsulları və yayınma

**İmza əsaslı aşkarlama (signature-based detection)** məlum nümunəni axtarır: yanlış həyəcan azdır, amma yeni (zero-day) hücumu və variantı qaçıra bilər («imza heç bir naməlum hücumu tutmur» də həddən artıq qətidir). **Anomaliya əsaslı aşkarlama (anomaly-based detection)** normal profildən kənarlaşmanı tapır, yeni hücumu tuta bilir, amma yanlış həyəcanı çoxdur . **Protokol vəziyyəti analizi (stateful protocol analysis)** protokolun gözlənilən ardıcıllığını yoxlayır; firewall «paket icazəli əlaqəyə aiddirmi», protokol analizi «protokol məntiqli işləyirmi» deyə soruşur.

TLS məzmununu passiv sensor oxumur (IP, port, vaxt, həcm görünür); ya TLS yoxlaması (deşifrə), ya da host sensoru (HIDS/EDR) lazımdır. DMZ-də TLS sonlansa və təkrar şifrələnsə, sensor yenə görmür; WAF, tətbiq jurnalları və host telemetriyası alternativdir. TLS yoxlaması sertifikat infrastrukturu tələb edir və özü həssas nöqtədir.

**Yayınma (evasion)** sensor ilə son sistemin fərqli oxumasına əsaslanır: IP fraqmentləşməsi və TCP seqmentləşməsi (axın yığılmalıdır), URI kodlaşdırma fərqi, asimmetrik yol (hər iki istiqamət sensora gəlməlidir), SPAN itkisi, şifrəli tunel, aşağı sürətli davranış (uzun tarixlə korrelyasiya). Sərt normallaşdırma qanuni tətbiqi poza bilər, yumşaq isə yayınmaya yol açır.

## Suricata qaydası

Suricata və Snort oxşardır, amma qaydalar yoxlanmadan köçürülmür. Nümunə: `alert http 10.10.10.0/24 any -> 10.10.40.15 80 (...)`. `alert` əməl, `http` protokol, `any` mənbə portu, `->` istiqamət. Seçimlər: `msg` analitikə mətn; `flow:to_server,established` serverə qurulmuş axın; `http.method` ilə `content:"GET"`; `http.uri` (normallaşdırılmış URI) ilə `content:"/ids-test"` və `startswith` (/ids-test-other də uyğun gələ bilər); `sid` lokal identifikator; `rev` dəyişiklik nömrəsi. Bu görünürlük testidir, hücum imzası deyil. Yoxlama: `suricata -T` konfiqurasiyanı, `-r` ilə PCAP oflayn oxunur (şəbəkəyə hücum getmir); TLS içində eyni URI-nin susması gözlənilir. HOME_NET və EXTERNAL_NET faktiki tərifi yoxlanır, yanal hərəkət üçün ayrıca qayda lazımdır.

## Yanlış nəticələr və tənzimləmə

TP real hücuma uyğun xəbərdarlıq, FP qanuni fəaliyyətə xəbərdarlıq, FN qaçırılmış hücum, TN düzgün sakitlikdir (qarışıqlıq matrisi, confusion matrix). Çox FP analitikləri yorur (alert fatigue), IPS-də isə qanuni istifadəçi bloklanır; FN daha təhlükəlidir, çünki heç kim xəbər tutmur.

**Hesab.** 50 hücumdan 30-u tutulur, 40 xəbərdarlıq var: TP = 30, FP = 40 − 30 = 10, FN = 50 − 30 = 20. Dəqiqlik (precision) = 30/40 = 75%, tamlıq (recall) = 30/50 = 60%. TN verilmədiyindən ümumi düzgünlük və FP tezliyi hesablanmır; 75% xəbərdarlıqların dəqiqliyidir, sensorun tamlığı yox.

Tənzimləmə (tuning): SQL mətni FP yaradırsa, bütün SQL qaydaları söndürülmür, dar mənbə və xidmət istisnası yazılır (sahib, baxış vaxtı). Yeni IPS qaydası əvvəl yalnız aşkarlama rejimində sınanır, sonra məhdud bloklama açılır, əvvəlki TP-lərin hələ tutulduğu yoxlanır.

## Jurnal və insident cavabı

Hadisə baş verən fəaliyyət, jurnal qeydi onun saxlanılan təsviri, xəbərdarlıq qaydanın nəticəsidir; insident CIA-dan birini pozan və ya real təhdid edən hadisədir (disk dolması hər ikisi ola bilər). Nümunə: firewall `drop` (10.10.10.25 → 10.10.80.10:5432), NIDS xəbərdarlığı və hostda naməlum skriptdən proses. `drop` bazaya daxil olunmadığını göstərir. Analitik DHCP və inventarla cihazın sahibini tapır, bağlantı sayını, host prosesini və dəyişiklik qeydini yoxlayır; tək IP günah sübutu deyil. Saatlar sinxron olmalı, NAT-dan əvvəl və sonra ünvanlar uyğunlaşdırılmalı, parol və token jurnala yazılmamalıdır.

**SIEM** (Security Information and Event Management) mənbələri toplayır, normallaşdırır və əlaqələndirir (Splunk, IBM QRadar, Microsoft Sentinel, Elastic, AlienVault OSSIM). Zeek protokol və əlaqə jurnalları, Wazuh host monitorinqi, ServiceNow insident işi, Graylog və ELK log axtarışı verir; heç biri tətbiq avtorizasiyasını və ya insan qiymətləndirməsini əvəz etmir. **SOAR** (Security Orchestration, Automation and Response; Cortex XSOAR) təkrarlanan cavab addımlarını avtomatlaşdırır; səlahiyyəti obyekt, müddət və geri dönüşlə məhdudlaşdırılır.

**İş axını:** qəbul və çeşidləmə (aktivin kritikliyi prioriteti təyin edir), sübut və təsir dairəsi (firewall və host qeydləri birlikdə), məhdudlaşdırma (cihaz karantini, digər qanuni giriş saxlanır), aradan qaldırma, təmiz vəziyyətdən bərpa və yoxlama, bağlanma (addımlar və boşluqlar qeyd edilir).

NIST SP 800-61 Rev. 3 insident cavabını riskin idarəsi və CSF 2.0 ilə bağlayır; CSF 2.0-nın funksiyaları Govern, Identify, Protect, Detect, Respond, Recover. CERT və ya CSIRT insident qəbulu və əlaqə komandasıdır; Azərbaycanda cert.az, cert.gov.az və sciencecert.az. VirusTotal-da heş məlumatına baxmaq kömək edir, həssas faylı yükləmək isə sızmadır.

**DDoS** (Distributed Denial of Service) xətti dolduranda arxadakı firewall kömək etmir: operator süzgəci və təmizləmə xidməti (Cloudflare, Akamai) lazımdır. Yük balanslaşdırma hücum filtri deyil; bahalı sorğular üçün sürət məhdudiyyəti və keş, qanuni kütləvi girişi ayırmaq üçün yük sınağı lazımdır.

## Kompleks sınaq

Magistrant ən azı beş əlaqəni və iki nəzarət nöqtəsini (DMZ firewall-u, baza sensoru) əsaslandırır, bir müsbət və iki mənfi sınaq aparır: LMS TCP 443 işləyir, bazaya TCP 5432 dayanır, qonaqdan kataloqa dayanır; eyni VLAN, IPv6, VPN və ehtiyat keçid də sınanır. `nc -vz` uğursuzluğu təkbaşına sübut deyil: qadağa qeydi və hədəfin işləkliyi də yoxlanır. 20 ballıq rubrika: zonalar 5, matris 5, yerləşdirmə 4, sübut 4, davamlılıq 2.
