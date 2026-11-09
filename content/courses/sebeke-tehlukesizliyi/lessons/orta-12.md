+++
title = "SIEM və istifadəçi davranışlarının təhlili (UEBA)"
unit = "orta"
order = 12
summary = "Hər anlayış izahlı: SIEM-in məlumat axını, log mənbələri və formatları, əsas Windows/Linux qeydləri, korrelyasiya növləri və qaydalar, UEBA, SOAR/XDR/SOC, ölçülər, tutum hesabı, məxfilik və praktiki iş."
updated = 2026-11-09

[[source]]
title = "Mühazirə 12: SIEM və istifadəçi davranışlarının təhlili (UEBA)"
note = "Elmar Cabbarov, 2026–2027"
+++

SIEM müxtəlif sistemlərin qeydlərini bir yerə yığır və əlaqələndirir, UEBA isə hər istifadəçi və cihaz üçün "normal"ı öyrənib ondan kənara çıxanları göstərir. Universitet nümunələri, ünvanlar, vaxtlar və saylar şərti tədris nümunəsidir.

:::exam Bu mövzudan sonra bacarmalısan
SIEM-in iş axınını (toplama → normallaşdırma → korrelyasiya → xəbərdarlıq) izah etmək; hadisə, xəbərdarlıq və insidenti ayırmaq; dörd korrelyasiya növünə nümunə qurmaq; SIEM-i UEBA, SOAR, EDR ilə fərqləndirmək; UBA ilə UEBA-nı ayırmaq; baza profili və z-balı ilə anomaliyanı qiymətləndirmək; dəqiqlik və tutma faizini və tutumu hesablamaq.
:::

## SIEM nədir

**SIEM** (*Security Information and Event Management*) müxtəlif sistemlərin qeydlərini toplayan, vahid formaya gətirən, əlaqələndirən, xəbərdarlıq yaradan və araşdırma üçün saxlayan sistemdir. Termini 2005-ci ildə **Gartner** analitikləri işlədib. O, iki əvvəlki sinfin birləşməsidir: **SIM** (uzunmüddətli saxlama, axtarış, hesabat) və **SEM** (real vaxt monitorinq, korrelyasiya). Nümunələr: Splunk, Microsoft Sentinel, IBM QRadar, Elastic Security, açıq mənbəli Wazuh.

Hücum nadir halda bir sistemdə tam görünür: VPN uğursuz girişləri görür, Active Directory yeni admini, baza ixracı, proksi isə xaricə yüklənməni. Hər biri tək adi görünə bilər; SIEM onları bir hesab və bir vaxt xətti üzərində birləşdirir.

![figure](m12-1.png)

SIEM təhlükəsizliyi özü-özlüyündə təmin etmir; onu **SOC** (Təhlükəsizlik Əməliyyatları Mərkəzi) işlədir. Sazlanmamış SIEM bahalı log arxividir.

:::example Target, 2013
ABŞ-ın Target şirkətində hücumçular kassa sistemlərinə zərərli proqram yerləşdirdilər. Təhlükəsizlik vasitəsi xəbərdarlıq yaratmışdı, komanda isə vaxtında hərəkət etmədi; 40 milyon bank kartının məlumatı oğurlandı. Xəbərdarlığın olması ilə ona reaksiya verilməsi ayrı məsələlərdir.
:::

## Əsas anlayışlar

| Anlayış | İzah | Nümunə |
| --- | --- | --- |
| Hadisə (event) | Qeydə alınan fəaliyyət | İstifadəçinin hesaba girişi |
| Jurnal qeydi (log entry) | Hadisəni təsvir edən saxlanılmış sətir | Vaxt, hesab, IP, nəticə |
| Xəbərdarlıq (alert) | Aşkarlama məntiqinin araşdırılmalı saydığı nəticə | 10 dəqiqədə 20 uğursuz giriş |
| İnsident (incident) | Təhlükəsizliyi pozan və ya real təhdid edən hadisə | Oğurlanmış hesabla məlumatın çıxarılması |

Nəticələr dörd kateqoriyadadır: hücum var və SIEM xəbərdarlıq verib: **TP**; hücum yoxdur, xəbərdarlıq var: **FP** (analitikin vaxtını alır); hücum var, SIEM susub: **FN** (ən təhlükəlisi, çünki heç kim xəbər tutmur); hücum yoxdur, SIEM susub: **TN**.

## SIEM arxitekturası

![figure](m12-2.png)

:::steps SIEM-in iş axını
[[step]]
title = "Toplama"
body = "Agent (Wazuh agent, Splunk Universal Forwarder), syslog, API (bulud) və ya kolektor. Ötürmə qorunur (TLS üzərindən syslog, TCP 6514), şəbəkə kəsiləndə qeydlər buferlənir. Mənbənin susması ayrıca izlənir: hadisənin gəlməməsi sakit sistem də ola bilər, dayanmış agent də."

[[step]]
title = "Ayrışdırma (parsing) və normallaşdırma"
body = "Xam sətirdən sahələr çıxarılır (IP, istifadəçi, əməl), fərqli mənbələrin eyni mənalı sahələri vahid sxemə salınır (`src_ip`, `srcaddr`, `IpAddress` → bir sahə). Bunun üçün Elastic Common Schema (ECS) və Open Cybersecurity Schema Framework (OCSF) yaradılıb."

[[step]]
title = "Vaxtın sinxronlaşdırılması"
body = "Mənbələr NTP ilə sinxron olur, vaxt UTC-də saxlanır. Hadisənin baş vermə və SIEM-ə çatma vaxtı ayrıca saxlanılır; gecikən hadisəni beş dəqiqəlik pəncərə buraxa bilər."

[[step]]
title = "Zənginləşdirmə"
body = "Hesabın rolu, cihazın sahibi, resursun həssaslığı, IP ölkəsi, təhdid kəşfiyyatı əlavə olunur: «yeni cihazdan giriş» ümumi siqnaldır, «imtiyazlı hesabla, idarə olunmayan cihazdan, gecə giriş» isə başqa dərəcədir."

[[step]]
title = "Korrelyasiya, xəbərdarlıq, saxlama"
body = "Qaydalar və modellər işləyir, nəticə SOC-a düşür. İsti qat tez axtarış, soyuq qat audit və sübut üçündür; qeydlər dəyişdirilməkdən və silinməkdən qorunur. Universal müddət yoxdur: PCI DSS tətbiq olunan mühitdə audit jurnalları üçün ən azı 12 aylıq tarixçə (son 3 ay dərhal əlçatan) tələb olunur, bu isə universitetin bütün sistemlərinə avtomatik aid deyil."
:::

### Yerləşdirmə və komponentlər

- **On-premises:** İT komandası serveri, diski, yeniləməni idarə edir; birbaşa nəzarət var, amma növbətçilik tələb olunur.
- **Cloud-native:** saxlama və hesablamanın bir hissəsini provayder idarə edir, genişləndirmək asandır; ötürmə, sorğu və saxlama xərci izlənir. Bulud seçmək mənbələrdə auditin açılması və hesabların qorunması məsuliyyətini aradan qaldırmır.
- **Hibrid:** kampus kolektorları və bulud analitikası birlikdə işləyir; iki mühitdə kimlik və nasazlıq idarəsi çətinləşir.

**Kolektor (collector)** qeydləri qəbul edib yerli növbəyə yazır və ötürür; **indeksləyici (indexer)** qeydləri axtarış üçün təşkil edir; **axtarış qovşağı (search head)** sorğunu indekslərə göndərib nəticəni birləşdirir (adlar Splunk-dandır). Bufer hesabı: 200 hadisə/s × 500 bayt × 7 200 s (iki saat fasilə) = 720 MB xam bufer, üstünə metadata və ehtiyat. Təkrar gələn qeyd üçün deduplikasiya təkil hadisə identifikatoruna əsaslanır; yalnız saniyə və istifadəçi adı ilə silmək fərqli girişləri itirə bilər.

### Vaxt və saxlama

Hadisə vaxtı (**event time**), kolektorun müşahidə vaxtı və qəbul vaxtı ayrıdır: məsələn 10:00, 10:01 və 10:07. Hamısı UTC-yə çevrilir, ilkin qurşaq saxlanır. Gecikmənin orta qiyməti aldadır: orta bir dəqiqə, amma bir hissə on dəqiqə gecikirsə, həmin hissə üçün qayda işləməyəcək. Geriyə baxış intervalı ardıcıllığın vaxt şərtindən fərqlidir: qayda son 20 dəqiqəni oxuya bilər, amma hadisələr arasında yenə 5 dəqiqə tələb edir; təkrar xəbərdarlığı qayda identifikatoru, hesab və başlanğıc hadisədən qurulmuş xəbərdarlıq açarı önləyir.

Saxlama qatları: **isti (hot)** tez sorğu, **ilıq (warm)** daha ucuz amma axtarılan, **soyuq (cold)** uzunmüddətli arxiv (bərpa lazım ola bilər). **WORM** (bir dəfə yaz, çox oxu) müddət ərzində silinməni və dəyişdirməni məhdudlaşdırır; sadə «yalnız oxu» icazəsi WORM deyil, çünki admin onu geri dəyişir. **Heş zənciri (hash chain):** H_i = SHA-256(H_(i−1) || qeyd_i); bir sətir dəyişsə, sonrakı heşlər uyğun gəlmir. Hücumçu bütün arxivi dəyişə bilirsə zənciri yenidən hesablayar, ona görə son heşlər imzalanmış manifestdə saxlanır. Heş sonradan dəyişməni göstərir, mənbənin əvvəlcə doğru yazdığını yox. Sübutda xam qeyd, emal surəti, sorğu və ixracın heşi birlikdə saxlanır, ötürülmə zənciri yazılır.

## Log mənbələri və formatları

| Mənbə | Cavab verdiyi sual |
| --- | --- |
| Firewall, VPN | Kim hara qoşulub? |
| AD, IAM | Hesab ələ keçirilibmi? (giriş, MFA, qrup dəyişikliyi) |
| Əməliyyat sistemi | Host-da nə işə düşüb? |
| EDR | Zərərli proses/fayl davranışı varmı? |
| DNS, proksi | C2 və məlumat çıxarılması varmı? |
| Verilənlər bazası | Həssas məlumat oxunubmu? |
| Bulud (CloudTrail) | Bulud hesabından sui-istifadə varmı? |
| DLP | Məlumat çıxırmı? |
| Tələ sistemi (honeypot) | Daxili skan varmı? |

Hər şeyi toplamaq səhvdir: mənbə konkret aşkarlama sualına cavab verməlidir, əks halda xərc artır, analitik səs-küydə itir.

**Syslog (RFC 5424)** geniş yayılıb; PRI = 8 × facility + severity, məsələn `<37>`: 37 = 8 × 4 + 5, facility 4 (auth), severity 5 (notice). **CEF** (ArcSight) və **LEEF** (QRadar) sahələri standartlaşdırır.

**Ayrışdırma.** Müntəzəm ifadə (**regular expression**) bütöv sətri yoxlayır, adlandırılmış qruplar sahələrdir (`user`, `src`, `result`), `fullmatch` kənar qalan hissəni səssiz buraxmır. Ancaq `src` qrupu istənilən boşluqsuz mətnə uyğun gəlir: sahənin çıxarılması ünvanın düzgünlüyü demək deyil, IP ayrıca yoxlanır, `failed` sözü `failure` kimi normallaşır. **Grok** adlandırılmış hazır regex şablonlarıdır (Logstash). Grok uğuru semantik yoxlamanı əvəz etmir; VPN yenilənib `result` əvəzinə `status` yazsa, qayda boş qalır, ona görə tələb olunan sahələrin doluluq faizi izlənir. Yanlış sətir atılmır, səhv səbəbi ilə ayrılır.

**ECS və OCSF** sahə adları və mənalarını təyin edir (OCSF: hadisə sinifləri, atributlar); ötürmə protokolu deyillər, syslog ilə gələn hadisə onlara uyğunlaşdırılır. Sadəcə sahə adını dəyişmək semantik uyğunluğu həmişə saxlamır. Nümunə: `ts` → `@timestamp`, `src` → `source.ip`, `result=failed` → `event.outcome: failure`, xam sətir → `event.original`. İstifadəçi adı dəyişməz identifikatoru əvəz etmir (`ali`, `UNEC\ali`, `ali@kampus.example` eyni hesab ola bilər); IAM-in dəyişməz identifikatoru götürülür, silinmiş hesabın adı başqasına veriləndə köhnə profil ona keçməməlidir. **NAT** arxasında yüzlərlə tələbə eyni xarici IP ilə görünür; şəxsi tapmaq üçün **DHCP** icarəsi hadisə vaxtı üzrə lazımdır (cari cədvəl dünənki hadisəyə tətbiq edilmir), olmasa nəticə «mənbə şəbəkə müəyyən edildi» səviyyəsində qalır.

## Ən vacib qeydlər

| Event ID | Məna | Niyə vacib |
| --- | --- | --- |
| 4624 | Uğurlu giriş | Logon Type 3 şəbəkə, 10 RDP |
| 4625 | Uğursuz giriş | Kobud güc, parol püskürtməsi |
| 4648 | Ayrıca kimlik məlumatı ilə giriş cəhdi | Daxili hərəkət; uğurun təsdiqi deyil |
| 4672 | Xüsusi imtiyazlar təyin edildi | Admin girişləri |
| 4688 | Yeni proses | Komanda sətri audit ilə dəyərlidir |
| 4720 | Hesab yaradıldı | Dayaqlanma (persistence) |
| 4728, 4732 | Qrupa üzv əlavə edildi | İmtiyaz artımı |
| 4768, 4769 | Kerberos bileti | Kerberoasting |
| 1102 | Audit jurnalı təmizləndi | İzlərin silinməsi |
| 7045 | Yeni xidmət | PsExec, dayaqlanma |

Linux: `/var/log/auth.log` (RHEL-də `/var/log/secure`), **journald**, **auditd**. **Sysmon** Windows-da əlavə detal verir: Event ID 1 proses, 3 şəbəkə bağlantısı, 11 fayl yaradılması. 4688 Security, 7045 System jurnalındadır, Sysmon ayrı kanaldadır; hər biri ayrıca toplanmalıdır. 4732-də həm edən (Subject), həm əlavə olunan üzv (MemberSid) var, qayda düzgün sahəyə baxmalıdır. Bu qeydlər defolt yazılmır: 4688-də komanda sətri əlavə siyasətlə açılır.

Oxuma qaydaları: 4624 şəbəkə girişini göstərir, amma istifadəçinin MFA keçdiyini sübut etmir; 4769-un çoxalması təkbaşına Kerberoasting deyil. Firewall `action=allow` yalnız siyasətin tətbiqidir, `bytes_out` mənası sənəddə yoxlanır (cəm, yoxsa interval fərqi), aralıq cəmləri toplamaq həcmi şişirdir. Proksi CONNECT 200 tunelin açıldığını bildirir, içindəki sorğunun nəticəsini yox; TLS yoxlaması olmadan URL görünməyə bilər. DNS tunelləmədə uzun adlar, tezlik, cavablar və klient prosesi birlikdə yoxlanır. CloudTrail-də `errorCode` ayrıca yoxlanır; əməliyyatı edənlə açar yaradılan hesab fərqli ola bilər. Boş auditd nəticəsi prosesin işləmədiyini göstərmir.

## Korrelyasiya

| Növ | Məntiq | Nümunə |
| --- | --- | --- |
| Hədd əsaslı (threshold) | Pəncərədə say həddi keçir | 10 dəqiqədə 20 uğursuz giriş |
| Ardıcıllıq (sequence) | A-dan sonra B | Uğursuz girişlər, sonra uğurlu giriş |
| Çoxmənbəli | Mənbələr birləşir | VPN girişi, sonra bazadan ixrac |
| Kontekst əsaslı | Aktiv/rol ilə yoxlanır | Tələbə hesabı maliyyə serverinə girir |
| Təhdid kəşfiyyatı | IoC siyahısı ilə tutuşdurulur | Bilinən C2 ünvanına bağlantı |
| Yoxluq (absence) | Gözlənilən hadisə baş vermir | Agent 30 dəqiqə susur |
| Statistik, davranış | Normadan kənarlaşma | İxrac 15 dəfə artıb |

Konspekt həmçinin zaman korrelyasiyasını verir (müəllim hesabı gecə 03:00-da qiymətləri kütləvi dəyişir). Çoxmənbəli zəncir: VPN girişi → imtiyazlı rol (Entra ID) → tələbə bazasının ixracı (DB) → xaricə böyük yükləmə (proksi); heç bir mənbə tək bunu görmür. Etibarlı hesabın sui-istifadəsi ATT&CK-da T1078 (Valid Accounts): uğurlu giriş təhlükəsiz demək deyil.

:::exam Tələ: brute force və password spraying
"Bir hesabda 10 uğursuz giriş" qaydası brute force-u (kobud güc) tutur, password spraying-i (parol püskürtməsi, MITRE ATT&CK T1110.003) isə tutmur: hücumçu 2 000 hesabın hər birində 1–2 parol sınayır. Lazım olan qayda: bir mənbə IP-dən qısa müddətdə **çox fərqli hesaba** uğursuz giriş.
:::

Nümunə (Splunk SPL; KQL-də `dcount`, `summarize`, `bin`): 10 dəqiqəlik pəncərədə `EventCode=4625`, hər IP üçün cəhd sayı > 20 **və** fərqli hesab sayı > 10. Rəqəmlər tədrisdir, real hədlər mühitə görə tənzimlənir. Qaydalar **Sigma** formatında yazılıb konkret SIEM dilinə çevrilə bilər (çevrilmiş sorğu yoxlanmadan tətbiq edilmir; `status: test` yoxlanmış sayılmır; `level: high` prioritetdir, hücum faktı deyil).

**Sabit və sürüşən pəncərə.** Sabit pəncərə (**tumbling window**) vaxtı üst-üstə düşməyən hissələrə bölür (09:50–10:00, 10:00–10:10); sürüşən pəncərə (**sliding window**) hər qiymətləndirmə anından əvvəlki intervalı götürür. 09:58-də 12, 10:03-də 12 cəhd olarsa, sabit pəncərələrin heç birində 20-dən çox yoxdur, 10:03-də bitən 10 dəqiqəlik sürüşən pəncərə isə 24 cəhdi görür. Xərci: daha çox vəziyyət saxlama və təkrar qiymətləndirmə.

![figure](m12-4.png)

**Uğursuz girişdən sonra uğurlu giriş** ssenarisi SPL-də `streamstats time_window=5m`, KQL-də `join` ilə yazılır: eyni hesab və IP üçün əvvəlki 5 dəqiqədə ≥10 uğursuz giriş, sonra uğurlu giriş. `join` böyük cədvəldə bahalıdır (əvvəl süzmək lazımdır), təkrar qəbul sayı şişirir (deduplikasiya), bir hesabın bütün IP-lərini birləşdirmək başqa ssenaridir.

**Hazır ssenarilər.** Kobud güc (T1110.001, 4625 bir hesaba); parol püskürtməsi (T1110.003); **mümkünsüz səyahət** (*impossible travel*, T1078: iki uzaq ölkədən qısa fasilə ilə giriş; yanlış müsbət: korporativ VPN çıxışı); imtiyaz artımı (T1098, 4728/4732); izlərin silinməsi (1102; T1685.005, köhnə T1070.001); yeni xidmət (T1543.003, 7045); DNS tunelləmə (T1071.004, uzun yüksək entropiyalı subdomenlər); C2 ilə məlumat çıxarılması (T1041). MITRE ATT&CK v19 (28 aprel 2026) Defense Evasion-ı Stealth (TA0005) və Defense Impairment (TA0112) taktikalarına ayırıb.

**Qaydanın həyatı.** Hər qaydanın sənədi var: ssenari, ATT&CK texnikası, mənbələr, yanlış müsbət səbəbləri, analitik üçün yoxlama, sahib. «Xidmət hesabını qaydadan çıxardıq» hücumçu üçün hazır boşluqdur. **Aşkarlamanın kodla idarəsi (detection as code):** qayda versiyalanır, nəzərdən keçirilir, sınaqdan keçir (ssenari, mənbə müqaviləsi, sintaksis, müsbət/mənfi, sərhəd testi, **kölgə rejimi**, buraxılış və geri qaytarma). FP-ni sıfırlamaq üçün qaydanı söndürmək FN-ni artırır. ATT&CK örtüyü «texnikaya qayda bağlandı» ilə yox, mənbə, parser, aktiv qayda və sınaqla təsdiqlənir: 20 prioritet ssenaridən 12-si tam yoxlanıbsa, örtük 12 / 20 = 60%-dir (bütün hücumların 60%-i demək deyil).

**Xəbərdarlığın araşdırılması** (mümkünsüz səyahət): qeydlərə bax, IP-ni yoxla (VPN çıxışı?), MFA nəticəsi, cihaz, girişdən sonrakı fəaliyyət, istifadəçi ilə ayrı kanaldan əlaqə, qərar (FP, dar istisna və ya insident), sübutu yaz.

## UEBA

Qayda əvvəlcədən yazılmış şərti yoxlayır; **UEBA** (*User and Entity Behavior Analytics*) fəaliyyətin normadan nə qədər fərqləndiyini ölçür. **UBA** yalnız istifadəçiləri, UEBA həm də serverləri, cihazları, tətbiqləri, xidmət hesablarını izləyir (yoluxmuş server, sui-istifadə olunan xidmət hesabı). Fərq alqoritmdə yox, izlənən obyektlərin dairəsindədir; maşın öyrənməsini UBA da işlədir.

![figure](m12-5.png)

Hər ikisi əvvəlcə **baza profili (baseline)** qurur: iş saatları, tipik IP və cihazlar, tətbiqlər, məlumat həcmi (30–90 günlük tarixçə tez-tez seçilir, amma universal deyil). Müqayisə üç səviyyədə: şəxsin öz tarixçəsi, **oxşar qrup (peer group)**, təşkilat. Yeni işçidə profil yoxdur, qrup müqayisəsi işləyir.

**Z-balı:** z = (x − μ) / σ. Müəllim adətən gündə μ = 200 MB, σ = 50 MB yükləyir, bu gün 500 MB: z = (500 − 200) / 50 = 6. Şəkildəki ayrı nümunədə μ ≈ 202, σ ≈ 29, x = 650 → z ≈ 15 (iki nümunəni qarışdırma). Z-balı standartlaşdırılmış məsafədir; ondan ehtimal çıxarmaq normal paylanma fərziyyəsi tələb edir; dövrilik, sıfır dispersiya və əyri paylanma yanıldır. **Persentil** (95-ci persentil həddi) və **MAD** (median əsaslı, böyük sıçrayışa davamlı) alternativlərdir; MAD sıfır olarsa «kifayət qədər dəyişkən tarixçə yoxdur» deyilir. **Mövsümilik (seasonality):** imtahan həftəsi adi həftə ilə müqayisə edilmir; cari gün təlimə qatılmır (test məlumatını təlimdə işlətmək sızmadır).

:::exam Anomaliya risk deyil
Anomaliya araşdırma səbəbidir, insident yox: imtahan həftəsində müəllim bütün işləri yükləyə bilər. Risk balı anomaliyanı kontekstlə birləşdirir: **R = 0,4A + 0,35K + 0,25S** (A anomaliya, K təhlükə konteksti, S məlumatın həssaslığı; hər biri 0–100). A = 80, K = 60, S = 90 → R = 32 + 21 + 22,5 = 75,5. Risk balı ehtimal deyil, prioritetdir; eyni hadisədən yaranan siqnallar (yeni ölkə + mümkünsüz səyahət + nadir IP) iki dəfə sayılmır (qrup limiti, maksimum bal). Bal zamanla azalır (40 → 20 → 10), açıq insident isə yalnız vaxt keçdiyi üçün bağlanmır.
:::

**Anomaliya növləri:** nöqtə (200 MB əvəzinə 650 MB), kontekst (gecə 03:00-da yükləmə), kollektiv (bir cihazdan ardıcıl 50 tələbə hesabına giriş). Konspektdə: zaman, cihaz, həcm, resurs, ardıcıllıq və coğrafi (bir saatda Bakı və Frankfurt); VPN, mobil şəbəkə, proksi coğrafi təyini çaşdırır.

**Maşın öyrənməsi.** Nəzarətsiz (*unsupervised*): klasterləşmə (**k-means**: qrup sayı seçilir, nöqtələr mərkəzlərə təyin olunur; **DBSCAN** sıxlığa əsaslanır), **Isolation Forest** (təsadüfi bölünmələrlə ayırır, uzaq nöqtə az bölünmə ilə ayrılır; kənar nöqtə «hücum etiketi» deyil). Nəzarətli üsul etiketli keçmiş insident tələb edir, real hücum nümunəsi azdır; bileti bağlamaq etibarlı etiket deyil, ümumi düzgünlük yanıldır. Qraf təhlilində hesab, cihaz, resurs düyündür, giriş əlaqədir; kimlik uyğunlaşdırma səhvi saxta əlaqə yaradır. İzah olunmayan model SOC-da etibar qazanmır.

**Konseptin sürüşməsi (concept drift).** Normal davranış dəyişir (yeni semestr, yeni vəzifə). Model yavaş uyğunlaşsa yanlış həyəcan artır; çox tez uyğunlaşsa hücumçu fəaliyyəti tədricən artıraraq normanı dəyişir (**low and slow**). Ona görə baseline nəzarətli yenilənir, təsdiqlənmiş insident dövrləri təlimdən çıxarılır, model namizədi kölgə rejimində yoxlanır. UEBA-nın zəifliyi: hücumçu «normal» mərhələdə artıq şəbəkədədirsə, davranışı norma kimi öyrənilir.

**DLP** (*Data Loss Prevention*) həssas məlumatın icazəsiz çıxmasını aşkar edir və dayandırır (SIEM üçün mənbədir, ayrı sistemdir). Növlər: şəbəkə DLP (hərəkətdə: poçt, veb), son qurğu DLP (istifadədə: USB, çap), saxlama/bulud DLP (sükunətdə). Üsullar: regex, rəqəmsal barmaq izi, etiketlər, maşın öyrənməsi. TLS yoxlaması olmadan şifrəli trafikdə məhduddur; əvvəlcə izləmə rejimində başlanır.

## SOAR, XDR və SOC

| Sistem | Vəzifə | SIEM-dən fərqi |
| --- | --- | --- |
| EDR | Son qurğuda davranışı izləyib cavab verir | Yalnız qurğu, amma daha dərin |
| XDR | Bir neçə qatın telemetriyasını və cavabını birləşdirir | Çox vaxt ekosistemə bağlıdır |
| UEBA | Davranış anomaliyası | SIEM-in modulu/məlumat qatı |
| SOAR | Playbook ilə araşdırma və cavabı avtomatlaşdırır | Əsas iş axınıdır |
| SOC | İnsanlar və proseslər | Texnologiya yox, komanda |

**SOAR** (*Security Orchestration, Automation and Response*) təkrarlanan işi görür: IP-ni zənginləşdirmək, bilet açmaq, hesabı müvəqqəti bloklamaq. Fişinq playbook-u: keçid və heşi yoxla, eyni məktubu alanları tap, zərərlisə bütün qutulardan sil, açanlara parol sıfırlaması və sessiya ləğvi. Dağıdıcı addımlar (hesab bloklama, cihaz təcridi) üçün hədd, təsdiq və geri qaytarma planı olmalıdır, yoxsa yanlış həyəcan bütün kafedranı işsiz qoya bilər. Əməliyyat idempotent olmalıdır (idempotentlik); API vaxt aşımı cavabın icra edilmədiyini sübut etmir. Xarici xidmətə tələbə sənədi və tam URL göndərilmir.

**SOC:** **L1** ilkin baxış (triage), **L2** dərin araşdırma, **L3** təhdid ovu (**threat hunting**), mürəkkəb insidentlər və yeni qaydalar. LMS hesabı araşdırması: yeni cihazdan VPN girişi (02:10) → həssas qovluq (02:14) → kütləvi endirmə (02:18) → xarici ötürmə (02:25); L1 qayda versiyasını, xam qeydləri, hesab uyğunluğunu yoxlayır («MFA var, təhlükə yoxdur» demir: token oğurluğu mümkündür), L2 mənbələri birləşdirir, DLP fayl izi sızma fərziyyəsini gücləndirir; faktı, fərziyyəni və çatışmayan sübutu ayrı yazmaq lazımdır. Parol dəyişməsi bütün tokenləri etibarsız etməyə bilər, sessiya ləğvi ayrıca təsdiqlənir.

**NIST.** İnsidentlə işləmə NIST SP 800-61 əsasındadır; Rev. 3 (aprel 2025) onu NIST CSF 2.0 funksiyalarına bağlayır (Govern, Identify, Protect, Detect, Respond, Recover). Konspektdəki dörd mərhələ (hazırlıq, aşkarlama və təhlil, məhdudlaşdırma/aradan qaldırma/bərpa, dərslər) **Rev. 2**-yə aiddir, onu Rev. 3-ün mərhələsi kimi vermək düzgün deyil. Jurnal idarəetməsi üçün əsas mənbə NIST SP 800-92 (layihə 2023).

:::note Köhnə slaydlarla fərq
Slaydda z-balı (200/50/500 → 6) düzgündür, yanındakı qrafikdə isə başqa verilənlər var; qarışdırma. FPR = FP / (FP + TN), xəbərdarlıqların boş payı isə FP / (TP + FP): fərqli göstəricilər. "Azure Sentinel" köhnə addır, indi Microsoft Sentinel.
:::

## Ölçülər və tutum

| Göstərici | Məna | Məqsəd |
| --- | --- | --- |
| MTTD | Hücumun başlanğıcından aşkarlanmaya orta vaxt | Azalmalı |
| MTTR | Aşkarlanmadan aradan qaldırılmaya orta vaxt | Azalmalı |
| Dəqiqlik (precision) | TP / (TP + FP) | Artmalı |
| Tamlıq (recall) | TP / (TP + FN) | Artmalı |
| ATT&CK örtüyü | Aşkarlanan texnikaların payı | Artmalı |
| Mənbə sağlamlığı | Vaxtında gələn mənbələrin faizi | 100%-ə yaxın |

**Dəqiqlik və tamlıq.** Qayda ayda 100 xəbərdarlıq verib: 20 TP, 80 FP, 5 hücum qaçıb (FN). Dəqiqlik 20 / 100 = 20%, tamlıq 20 / (20 + 5) = 80%. **FPR = FP / (FP + TN)**; TN məlum deyilsə, hesablanmır (TN = 920 olsa, 80 / 1 000 = 8%). Xəbərdarlıqların boş payı FP / (TP + FP) = 80%, FPR ilə eyni deyil. Başqa nümunə: 200 xəbərdarlıq, 30-u real → dəqiqlik 15%. Buradan **xəbərdarlıq yorğunluğu** başlayır: analitik öyrəşir və real hücumu qaçırır. Dəqiqliyi qaydanı sərtləşdirib artırmaq tamlığı azalda bilər; balans qurulur. Tamlığı ölçmək çətindir (aşkarlanmayan hücumların sayı bilinmir), ona görə idarə olunan testlər (**purple team**, **Atomic Red Team**) aparılır.

**MTTD/MTTR.** Gecikmələr 8, 12, 25 dəq → MTTD = 45 / 3 = 15 dəq; aşkarlanmadan aradan qaldırılmaya 30, 50, 100 dəq → MTTR = 180 / 3 = 60 dəq. Tərif açıq yazılmalıdır (MTTR ilk cavaba qədər də ola bilər). Orta vaxt gecikmiş kritik işi gizlədir, median və yuxarı persentillər də verilir. Mənbə əhatəsi: 20 kritik mənbədən 18 qoşulub (90%), 16-sı vaxtında və düzgün sahələrlə gəlir (işlək əhatə 80%).

**Tutum, EPS** (*events per second*). 2000 EPS × 500 bayt = 1 MB/s → 86,4 GB/gün → 90 gündə təxminən 7,8 TB sıxılmadan. İndeks və replika bura daxil deyil. Əmsallarla (sıxılma sonrası 0,5, indeks 0,3): 86,4 × 0,8 = 69,12 GB/gün; replika ilə 138,24; 90 gün 12 441,6 GB; +25% ehtiyat ≈ 15,55 TB. Replika ehtiyat nüsxə deyil (səhv silmə ona da yayılır). Pik yük (8 000 EPS → 4 MB/s) ortadan yüksək olur; imtahan pikini də sına.

## Səhvlər, məxfilik, SIEM-in qorunması

Tipik səhvlər: məqsədsiz toplama; saatların sinxron olmaması; yanlış ayrışdırma (mənbə IP təyinat kimi yazılır); SIEM-də hesabların qorunmaması (loglar parol və şəxsi məlumat saxlaya bilər); susan mənbələrə nəzarətin olmaması; hazır qaydaların tənzimsiz işə salınması; log silinməsinə qarşı müdafiənin olmaması (mənbələr dərhal göndərsin, SIEM-də dəyişməzlik olsun).

UEBA təhlükəsizlik davranışını işləyir; məhsuldarlıq, siyasi baxış və ya niyyət ölçmək üçün etibarlı deyil. Davranış balı avtomatik intizam qərarı olmaz, şəxsə aid qərar faktların yoxlanmasına və səlahiyyətli insana əsaslanır. Toplama məqsədi, sistemlər, sahələr və saxlama müddəti siyasətdə yazılır; artıq məzmun (parol, token, tam sorğu mətni) çıxarılır. **Psevdonimləşdirmə** identifikatoru işarə ilə əvəz edir (uyğunluq cədvəli ayrıca qorunur); sadə heş anonimlik vermir, məxfi açarlı **HMAC** lüğət müqayisəsini çətinləşdirir, amma davranış yenə həssasdır. SIEM idarəetmə hesabları MFA və ən az səlahiyyətlə qorunur, qayda yazan/arxiv silən/sübut ixrac edən hüquqlar ayrılır, analitikin baxışı audit olunur. Log məzmunu etibarlı giriş deyil: hücumçu sətirsonu və idarəetmə simvolu yaza bilər, ona görə strukturlaşdırılmış qeyd və qaçışlama lazımdır. SIEM özü çöksə, kolektorların bufer müddəti və alternativ xəbər kanalı bərpa planında yazılır.

## Praktiki iş

nigar@kampus.example hesabı: 10:00 tanınmış cihazdan giriş, 10:05 yeddi uğursuz cəhd, 10:07 yeni cihazdan giriş, 10:10 kritik fayllara müraciət, 10:12 qeyri-adi həcmdə endirmə. Tələbə sxemə çevirir, hadisə və qəbul vaxtını ayırır, identifikatorları uyğunlaşdırır; MFA, faylın həssaslığı və istiqamət verilməyibsə fakt kimi yazmır («endirmə» xaricə yükləmə demək deyil). Bir hədd qaydası («5 dəqiqədə ≥7 uğursuz cəhd» — köhnə 10-luq hədd bunu tutmaz) və bir ardıcıllıq qaydası yazılır, UEBA ilə ən azı üç alternativ izah verilir (köhnə parollu tətbiq, cihaz dəyişməsi, təsdiqlənmiş arxiv işi). Nəticə təsdiqlənmişi fərziyyədən ayırır. Bal: məlumat hazırlığı 20, korrelyasiya məntiqi 25, profil və anomaliya təhlili 20, alternativ izahlar 15, reaksiya və rəy 20 (cəmi 100).
