+++
title = "SIEM və istifadəçi davranışlarının təhlili (UEBA)"
unit = "uzun"
order = 12
summary = "Tam mühazirə: SIEM-in məlumat axını, log formatları və ayrışdırma, Windows/Linux qeydləri, korrelyasiya qaydaları (SPL, KQL, Sigma), UEBA statistikası və maşın öyrənməsi, SOAR/XDR/SOC, ölçülər, tutum hesabı, məxfilik və praktiki iş."
updated = 2026-11-09

[[source]]
title = "Mühazirə 12: SIEM və istifadəçi davranışlarının təhlili (UEBA)"
note = "Elmar Cabbarov, 2026–2027"
+++

Universitetdə gündə milyonlarla log yaranır: girişlər, firewall qeydləri, VPN qoşulmaları. SIEM onları bir yerə yığıb əlaqələndirir, UEBA isə hər istifadəçi (və cihaz) üçün "normal"ı öyrənib ondan kənara çıxanları göstərir. Aşağıdakı universitet nümunələrindəki ünvan, hesab, vaxt, say və ballar şərti tədris nümunəsidir.

Mühazirənin planı: SIEM və SOC-da yeri; hadisə, xəbərdarlıq, insident; arxitektura və məlumat axını; log mənbələri, formatlar, ayrışdırma, vahid sxemlər; Windows və Linux qeydləri; korrelyasiya; UEBA; SOAR, XDR, SOC prosesləri; ölçülər və tutum; tipik səhvlər; məxfilik və SIEM-in qorunması; praktiki iş.

:::exam Bu mövzudan sonra bacarmalısan
- SIEM-in məlumat axınını mərhələlərlə izah etmək (toplama → normallaşdırma → korrelyasiya → xəbərdarlıq).
- Hadisəni, xəbərdarlığı və insidenti ayırmaq; korrelyasiya qaydası yazmaq; dörd korrelyasiya növünə nümunə qurmaq.
- SIEM-in UEBA, SOAR və EDR ilə fərqini göstərmək; UBA ilə UEBA-nı ayırmaq.
- Baza profili və z-balı ilə anomaliyanı qiymətləndirmək; dəqiqlik və tutma (tamlıq) faizini hesablamaq; tutumu hesablamaq.
:::

## SIEM nədir

**SIEM** (*Security Information and Event Management*, təhlükəsizlik məlumatları və hadisələrinin idarə edilməsi) müxtəlif sistemlərin qeydlərini toplayan, vahid formaya gətirən, əlaqələndirən, xəbərdarlıq yaradan və araşdırma üçün saxlayan sistemdir. Termini 2005-ci ildə **Gartner** analitikləri Mark Nikolet və Amrit Uilyams işlədib. O, iki əvvəlki sinfin birləşməsidir:

| Sinif | Nə edir |
| --- | --- |
| **SIM** (Security Information Management) | uzunmüddətli saxlama, axtarış, hesabat |
| **SEM** (Security Event Management) | real vaxt monitorinq (*real vaxtda təhlil*), korrelyasiya, xəbərdarlıq |

Nümunələr: Splunk Enterprise Security, Microsoft Sentinel, IBM QRadar, Elastic Security, Wazuh (açıq mənbə).

Hücum nadir halda bir sistemdə tam görünür. VPN uğursuz girişləri görür, Active Directory yeni admini, baza ixracı, proksi isə xaricə yüklənməni. Hər biri ayrılıqda adi görünə bilər. SIEM bunları bir hesab və bir vaxt xətti üzərində birləşdirir.

![figure](m12-1.png)

Şəkil 1. Beş ayrı mənbədən gələn hadisələrin bir hücuma birləşdirilməsi (şərti nümunə): 02:11 VPN 14 uğursuz giriş, 02:13 yeni ölkədən uğurlu giriş, 02:21 AD EventID 4732 admin qrupuna əlavə, 02:34 baza 2 GB ixrac, 02:41 proksidə naməlum sayta yükləmə.

SIEM təhlükəsizliyi özü-özlüyündə təmin etmir. Onu **Təhlükəsizlik Əməliyyatları Mərkəzi (SOC)** işlədir. Yaxşı sazlanmamış SIEM yalnız bahalı log arxividir.

:::example Target, 2013
2013-cü ildə ABŞ-ın Target şirkətində hücumçular kassa sistemlərinə zərərli proqram yerləşdirdilər. Şirkətin təhlükəsizlik vasitəsi xəbərdarlıq yaratmışdı, amma komanda onun üzərində vaxtında hərəkət etmədi. Nəticədə 40 milyon bank kartının məlumatı oğurlandı. Dərs: xəbərdarlığın olması ilə ona reaksiya verilməsi ayrı məsələlərdir.
:::

## Əsas anlayışlar

| Anlayış | İzah | Nümunə |
| --- | --- | --- |
| Hadisə (event) | Sistemdə baş verən və qeydə alınan fəaliyyət | İstifadəçinin hesaba girişi |
| Jurnal qeydi (log entry) | Hadisəni təsvir edən saxlanılmış sətir | Vaxt, hesab, IP, nəticə |
| Xəbərdarlıq (alert) | Aşkarlama məntiqinin araşdırılmalı saydığı nəticə | 10 dəqiqədə 20 uğursuz giriş |
| İnsident (incident) | Təhlükəsizliyi pozan və ya real təhdid edən hadisə | Oğurlanmış hesabla məlumatın çıxarılması |

Aşkarlama sisteminin nəticələri dörd kateqoriyada qiymətləndirilir. Yaranmış xəbərdarlıq TP və ya FP ola bilər, FN və TN isə xəbərdarlıq yaranmayan hallardır:

| Real vəziyyət | SIEM xəbərdarlıq verdi | SIEM susdu |
| --- | --- | --- |
| Hücum var | Həqiqi müsbət (TP) | Yanlış mənfi (FN), ən təhlükəlisi |
| Hücum yoxdur | Yanlış müsbət (FP), analitikin vaxtını alır | Həqiqi mənfi (TN) |

:::note Sadə dillə
FN-in təhlükəli olmasının səbəbi: hücum olub, amma heç kim xəbər tutmayıb. FP isə analitikin vaxtını alır, ancaq hücumu gizlətmir.
:::

## SIEM arxitekturası

![figure](m12-2.png)

Şəkil 2. SIEM-də məlumat axını: mənbələr (Firewall/VPN, AD/IAM, serverlər/EDR, DNS/proksi, bulud/tətbiqlər) → toplama → normallaşdırma → zənginləşdirmə → korrelyasiya (qaydalar, UEBA) → xəbərdarlıq (SOC, SOAR); normallaşdırmadan isti və soyuq saxlamaya (axtarış, audit, sübut) yol ayrılır, araşdırma sorğuları saxlama ilə xəbərdarlıq arasında gedib-gəlir.

Məlumat mənbədən analitikin ekranına qədər bir neçə mərhələdən keçir. Hər mərhələdə səhv növbəti mərhələni korlayır: düzgün ayrışdırılmayan log korrelyasiyaya düşmür.

:::steps SIEM-in iş axını
[[step]]
title = "Toplama"
body = "Qeydlər agent (Wazuh agent, Splunk Universal Forwarder), syslog, API (bulud xidmətləri) və ya kolektor vasitəsilə gəlir. Ötürmə qorunmalı (TLS üzərindən syslog, TCP 6514), şəbəkə kəsiləndə qeydlər buferlənməlidir. Mənbənin susması ayrıca izlənir: hadisənin gəlməməsi həm sakit sistem, həm də dayanmış agent mənasına gələ bilər."

[[step]]
title = "Ayrışdırma (parsing)"
body = "Xam sətirdən sahələr çıxarılır: IP, istifadəçi, əməl."

[[step]]
title = "Normallaşdırma"
body = "Fərqli mənbələrin eyni mənalı sahələri vahid sxemə salınır. Məsələn, `src_ip`, `srcaddr`, `IpAddress` bir sahəyə gətirilir. Elastic Common Schema (ECS) və Open Cybersecurity Schema Framework (OCSF) bu məqsəd üçün yaradılıb."

[[step]]
title = "Vaxtın sinxronlaşdırılması"
body = "Bütün mənbələr NTP ilə sinxron olmalı, UTC-də saxlanmalıdır. Hadisənin baş vermə və SIEM-ə çatma vaxtı ayrıca saxlanılır. Hadisə gecikəndə beş dəqiqəlik korrelyasiya pəncərəsi onu buraxa bilər."

[[step]]
title = "Zənginləşdirmə"
body = "Hadisəyə kontekst əlavə edilir: hesabın rolu, cihazın sahibi, resursun həssaslığı, IP-nin ölkəsi, təhdid kəşfiyyatı. «Yeni cihazdan giriş» ümumi siqnaldır; «imtiyazlı hesabla, idarə olunmayan cihazdan, gecə giriş» isə başqa dərəcədir."

[[step]]
title = "Korrelyasiya və xəbərdarlıq"
body = "Qaydalar və modellər işləyir, nəticə SOC-a düşür."

[[step]]
title = "Saxlama"
body = "İsti qat tez axtarış üçün, soyuq qat audit və sübut üçündür. Vahid universal müddət yoxdur: PCI DSS tətbiq olunan mühitdə audit jurnalları üçün ən azı 12 aylıq tarixçə, son 3 ay üçün dərhal əlçatanlıq tələb olunur. Bu tələb avtomatik olaraq universitetin bütün sistemlərinə aid edilmir. Qeydlər dəyişdirilməkdən və silinməkdən qorunur."
:::

:::note Sadə dillə: normallaşdırma, vaxt, zənginləşdirmə
Firewall mənbə ünvanını `src`, Windows `IpAddress`, VPN `client_ip` adlandırır; normallaşdırma onları vahid sahəyə (`source.ip`) gətirir ki, bir qayda bütün mənbələri əhatə etsin. Hadisə vaxtı (baş verdiyi an) ilə qəbul vaxtı (SIEM-ə çatdığı an) fərqlidir; saat qurşaqları, NTP sinxronsuzluğu və gecikən loglar korrelyasiyanı pozur. Zənginləşdirmədən əvvəl log yalnız "user=a.mammadova logged in from 85.x.x.x" deyir; sonra: "maliyyə şöbəsi, kritik hesab; IP Almaniyadan, təhdid feed-ində yoxdur; təsdiqlənmiş texniki xidmət pəncərəsi yoxdur." Analitik qərarı bu kontekstlə verir.
:::

:::tip Logların qorunması
Loglar dəyişdirilməkdən və silinməkdən qorunmalı (hücumçu izini silməyə çalışır), giriş məhdud olmalı, saxlama müddəti qanun və risk əsasında təyin edilməlidir. Universal müddət yoxdur.
:::

Məhsullar: **Splunk** (2024-cü ildə Cisco alıb), **Microsoft Sentinel** (bulud), **IBM QRadar** (bulud biznesini 2024-də Palo Alto Networks alıb), Elastic Security, açıq mənbəli Wazuh geniş yayılıb.

### Yerləşdirmə modelləri və komponentlər

Yerləşdirmə qərarı məlumatın harada qalacağından başlayır. Universitetin öz infrastrukturunda qurulan SIEM-də (**on-premises**) serverləri, disk massivini, yeniləmələri və ehtiyat nüsxələri İT komandası idarə edir. Bulud üçün qurulmuş SIEM-də (**cloud-native**) xidmətin saxlama və hesablama qatlarının bir hissəsini provayder idarə edir. **Hibrid** modeldə kampus kolektorları ilə bulud analitikası birlikdə işləyir. Bulud xidməti seçmək mənbələrdə auditin açılması, hesabların qorunması və qaydaların yoxlanması məsuliyyətini aradan qaldırmır.

| Model | Universitet nümunəsi | Üstünlük | Məhdudiyyət |
| --- | --- | --- | --- |
| Öz infrastrukturunda | Tələbə bazasının auditi kampusda qalır | Məlumat və şəbəkə üzərində birbaşa nəzarət | Disk, yeniləmə və növbətçilik tələb edir |
| Bulud üçün qurulmuş | Bulud poçtu və IAM auditləri xidmətə ötürülür | Resursların artırılması asanlaşır | Ötürmə, sorğu və saxlama xərci izlənməlidir |
| Hibrid | Yataqxana kolektoru, kampus arxivi, bulud analitikası | Mənbələri mərhələlərlə birləşdirmək olur | İki mühitdə kimlik və nasazlıq idarəsi çətinləşir |

![figure](m12-3.png)

Şəkil 3. Kampus kolektorlarından indeksləmə və axtarış qatlarına məlumat axını; hibrid yerləşdirmə nümunəsi (VPN/IAM və LMS/baza qeydləri → kolektorlar və yerli disk növbəsi → TLS → indeksləyicilər; axtarış qovşağı indeksləyicilərlə işləyir; dəyişməz arxiv ayrıdır).

- **Kolektor (collector)** qeydləri qəbul edir, yerli növbəyə yazır və ötürür.
- **İndeksləyici (indexer)** qeydləri axtarış üçün təşkil edir; sahələr və vaxt üzrə indekslər saxlayır.
- **Axtarış qovşağı (search head)** analitikin sorğusunu uyğun indekslərə göndərir və nəticələri birləşdirir.

Bu adlar xüsusən Splunk arxitekturasında işlənir; başqa məhsullarda eyni funksiyalar fərqli xidmətlər arasında bölünə bilər. Sınaq quruluşunda bir serverdə birləşir, geniş sistemdə ayrıca böyüdülür.

**Bufer hesabı.** Yataqxana ilə kampus arasındakı kanal kəsiləndə kolektor hadisələri disk növbəsində saxlamalıdır. Şərti olaraq saniyədə 200 hadisə, hər hadisədə 500 bayt və iki saatlıq fasilə üçün xam bufer 200 × 500 × 7 200 = 720 MB-dır. Bu rəqəmə növbə metadatası və ehtiyat payı əlavə edilir. Bufer dolanda hansı qeydlərin itəcəyi, nə qədər itkinin qəbul ediləcəyi və kimin xəbər alacağı əvvəlcədən yazılır. Sadəcə TCP bağlantısının olması tətbiqin qeydi diskə etibarlı yazdığını sübut etmir.

**Təkrar və deduplikasiya.** Agentin son oxuduğu mövqe, API-nin davam göstəricisi və ötürmə təsdiqi yenidən başlamadan sonra saxlanmalıdır. Bir qeydin təkrar gəlməsi mümkündür. Təkil hadisə identifikatoru varsa, deduplikasiya ona əsaslanır; yoxdursa, mənbə, vaxt, məzmun heşi və əlavə identifikatorlardan istifadə edilir. Yalnız saniyə və istifadəçi adı ilə təkrarı silmək real, bir-birinə oxşar girişləri itirə bilər. Səhv ayrışdırılan qeydlər ayrıca növbəyə düşür və xam mətn saxlanılır.

### Vaxtın üç səviyyəsi

Hadisə vaxtı (**event time**), kolektorun müşahidə vaxtı və platformanın qəbul vaxtı ayrı anlayışlardır. Şərti olaraq VPN qeydi 10:00-da yaranır, kolektor onu 10:01-də görür, SIEM isə 10:07-də indeksləşdirir. Birinci fərq mənbə və ötürmə kanalını, ikinci fərq növbə və indeksləmə yükünü yoxlamağa kömək edir. Bütün vaxtlar UTC-yə çevrilir, ilkin saat qurşağı da saxlanılır. Bakı vaxtı ilə 14:00, UTC ilə 10:00 eyni andır; vaxtı sadəcə dörd saat geri yazmaq əvəzinə qurşaq məlumatını tanıyan tarix emalı seçilir.

NTP mənbələri nəzarət altında olmalı, saat fərqi ayrıca ölçülməlidir. Tarixdə il və qurşaq yoxdursa, parserin hansı fərziyyə ilə onları tamamladığı sənədləşdirilir. Gələcək tarixə düşən hadisə aşkarlama pəncərəsindən kənarda qala bilər. Gecikmənin orta qiyməti ilə kifayətlənmək olmaz: şərti olaraq orta gecikmə bir dəqiqə olsa da, hadisələrin bir hissəsi on dəqiqə gecikirsə, həmin hissə üçün qayda işləməyəcək.

Geriyə baxış intervalı ilə ardıcıllığın vaxt şərti fərqlidir. Uğursuz girişdən sonra beş dəqiqədə uğurlu giriş axtaran qayda gecikməyə görə son iyirmi dəqiqənin məlumatını oxuya bilər; yenə də iki hadisə arasındakı məsafəni beş dəqiqə ilə məhdudlaşdırır. Təkrar icrada eyni xəbərdarlığı yaratmamaq üçün qayda identifikatoru, hesab və başlanğıc hadisə identifikatorundan xəbərdarlıq açarı qurulur.

### Saxlama qatları və dəyişməzlik

**İsti (hot)** qat tez-tez sorğulanan və aşağı gecikmə tələb edən məlumat üçündür. **İlıq (warm)** qatda məlumat daha ucuz resursda qalır və adətən axtarılır. **Soyuq (cold)** qat uzunmüddətli arxivdir; sorğu üçün məlumatı əvvəlcə bərpa etmək lazım gələ bilər. Müqavilədə axtarışa açılma müddəti yoxlanır.

| Qat | İş nümunəsi | Yoxlanmalı tələb | Unudulan xərc |
| --- | --- | --- | --- |
| İsti | Davam edən LMS insidenti | Sorğunun cavab vaxtı | Sürətli disk və indekslər |
| İlıq | Əvvəlki ay üzrə axtarış | İndeksin əlçatanlığı | Hesablama və replika |
| Soyuq | Uzunmüddətli audit | Bərpa vaxtı və bütövlük | Bərpa əməliyyatı və trafik |

**WORM** (*Write Once Read Many*, bir dəfə yazılıb çox dəfə oxunan saxlama) müəyyən edilmiş müddətdə obyektin dəyişdirilməsini və silinməsini məhdudlaşdırır. Sadə «yalnız oxu» fayl icazəsi WORM deyil: inzibatçı həmin icazəni geri dəyişə bilər. Dəyişməz arxiv üçün saxlama siyasəti, imtiyazların ayrılması və vaxtından əvvəl silinməyə nəzarət birlikdə qurulur. Sınaqda təsdiqlənməlidir ki, SIEM inzibatçısı arxivi təkbaşına məhv edə bilmir.

**Heş zənciri (hash chain).** Hər qeyd əvvəlkinin heşini də daxil edir: H_i = SHA-256(H_(i−1) || qeyd_i). Birləşdirilən sahələrin kodlaşdırılması və sərhədləri dəqiq olmalıdır. Bir sətir dəyişəndə sonrakı heşlər uyğun gəlmir. Lakin hücumçu bütün arxivi və ilk etibar nöqtəsini dəyişə bilirsə, zənciri yenidən hesablaya bilər. Buna görə blokların son heşləri ayrıca qorunan, imzalanmış manifestdə saxlanılır. Heş məzmunun sonradan dəyişməsini göstərir; mənbənin əvvəlcə doğru məlumat yazdığını sübut etmir.

**Sübut saxlanması.** Araşdırmada xam qeyd, emal edilmiş surət, sorğu mətni və ixracın heşi birlikdə saxlanılır. Sübutun ötürülmə zəncirində kimin, nə vaxt, hansı faylı aldığı və haraya köçürdüyü yazılır. Sübut qovluğuna bütün SOC əməkdaşlarına yox, iş üzrə giriş verilir. Şifrələmə disk oğurlanmasına qarşı tədbirdir; dəyişməzlik və giriş auditi isə ayrıca tələbdir.

## Log mənbələri və formatları

| Mənbə | Nə verir | Hansı suala cavabdır |
| --- | --- | --- |
| Firewall, VPN | Bağlantılar, sessiyalar | Kim hara qoşulub? |
| AD, IAM | Giriş, MFA, qrup dəyişiklikləri | Hesab ələ keçirilibmi? |
| Əməliyyat sistemi | Proseslər, xidmətlər | Host-da nə işə düşüb? |
| EDR | Proses və fayl davranışı | Zərərli fəaliyyət varmı? |
| DNS, proksi | Domenlər, URL-lər | C2 və məlumat çıxarılması varmı? |
| Verilənlər bazası | Girişlər, sorğular | Həssas məlumat oxunubmu? |
| Bulud (CloudTrail və s.) | API əməliyyatları | Bulud hesabından sui-istifadə varmı? |
| DLP | Məlumat ötürülməsi siqnalları | Məlumat çıxırmı? |
| Tələ sistemi (honeypot) | Tələyə bağlantılar | Daxili skan varmı? |

Hər şeyi toplamaq səhv yanaşmadır. Mənbə konkret aşkarlama sualına cavab verməlidir, əks halda xərc artır, analitik isə səs-küy içində qalır.

**Syslog (RFC 5424)** geniş işlədilən jurnal formatıdır. Başındakı PRI dəyəri 8 × facility + severity düsturu ilə hesablanır:

```text
<37>1 2026-10-14T02:11:09Z vpn01 sshd 2211 - - Failed password for ali from 198.51.100.23 port 51122
```

Burada 37 = 8 × 4 + 5, yəni facility 4 (auth), severity 5 (notice). **CEF** (ArcSight) və **LEEF** (QRadar) formatları isə sahələri standartlaşdırır:

```text
CEF:0|Vendor|VPN|7.4|1001|VPN login failed|5|src=198.51.100.23 suser=ali
```

### Ayrışdırmanın addım-addım nümunəsi

Məqsəd şərti VPN sətrindən uğursuz autentifikasiyanın vaxtını, hesabını və mənbəyini çıxarmaqdır. Sintaksis tədris üçün qurulub, konkret cihazın formatı deyil.

```text
2026-10-14T02:11:09Z vpn01 user=ali src=198.51.100.23 result=failed
```

Müntəzəm ifadə (**regular expression**, regex) bütöv sətri yoxlayır. Adlandırılmış qruplar çıxarılan sahələrdir; `fullmatch` formatdan kənar qalan hissəni səssiz ötürmür.

```python
import re
line = ("2026-10-14T02:11:09Z vpn01 user=ali "
        "src=198.51.100.23 result=failed")
pattern = (r"(?P<ts>\S+) (?P<host>\S+) user=(?P<user>\S+) "
           r"src=(?P<src>\S+) result=(?P<result>success|failed)")
m = re.fullmatch(pattern, line)
assert m is not None
assert m["src"] == "198.51.100.23"
assert m["result"] == "failed"
```

Bu şablonun `src` qrupu istənilən boşluqsuz mətnə uyğun gəlir: sahənin çıxarılması ünvanın düzgünlüyü demək deyil. Növbəti mərhələdə IP ünvanı uyğun kitabxana ilə yoxlanır, vaxt tarix tipinə çevrilir, nəticə dəyəri normallaşdırılır (`failed` vahid sxemdə `failure` olur). `user=ali` yazılmayan sətir, IPv6 ünvanı və naməlum nəticə dəyəri üçün ayrıca test hazırlanır. Yanlış sətir atılmır, səhv səbəbi ilə ayrılır.

**Grok** adlandırılmış hazır regex şablonlarından istifadə edir. Aşağıdakı Logstash filtri eyni sətri emal edir; `date` filtri mənbə vaxtını `@timestamp` sahəsinə yazır.

```text
filter {
  grok {
    pattern_definitions => {
      "HEAD" => "%{TIMESTAMP_ISO8601:ts} %{HOSTNAME:host}"
      "USR"  => "user=%{NOTSPACE:user}"
      "SRC"  => "src=%{IP:src}"
      "RES"  => "result=%{WORD:result}"
    }
    match => { "message" => "^%{HEAD} %{USR} %{SRC} %{RES}$" }
  }
  date { match => [ "ts", "ISO8601" ] }
}
```

Grok uğuru nəticə sahəsinin semantik yoxlanmasını əvəz etmir: `WORD` şablonu gözlənilməyən nəticə sözünə də uyğun gələ bilər. Parser uğuru, IP yoxlaması və vaxt çevrilməsi ayrıca izlənir. Universitet VPN proqramını yeniləyəndən sonra `result` əvəzinə `status` yazılarsa, autentifikasiya qaydası boş nəticə verə bilər. Hadisələrin sayı ilə yanaşı tələb olunan sahələrin doluluq faizi izlənəndə bu nasazlıq görünür.

### ECS, OCSF və kimlik uyğunlaşdırması

**ECS** sahələrin adlarını və mənalarını müəyyən edən sxemdir. **OCSF** hadisə sinifləri, kateqoriyalar və atributlarla təhlükəsizlik hadisələrini təsvir edir. Bunlar ötürmə protokolu deyil: syslog ilə gələn hadisə ECS-ə və ya OCSF-ə uyğunlaşdırıla bilər. OCSF üçün autentifikasiya sinfi seçilir, istifadəçi və mənbə endpoint obyektləri doldurulur; dəqiq atribut yolu və enum dəyərləri seçilən sxem versiyasına görə yoxlanır. İki sxem arasında yalnız sahə adlarını dəyişmək semantik uyğunluğu həmişə saxlamır.

| Xam sahə | ECS sahəsi | Çevrilmə |
| --- | --- | --- |
| ts | `@timestamp` | ISO 8601 vaxtını UTC-yə çevir |
| host | `host.name` | Hadisəni yazan hostu göstər |
| user | `user.name` | Hesab adını saxla |
| src | `source.ip` | Ünvan tipini yoxla |
| result=failed | `event.outcome` | `failure` dəyərinə uyğunlaşdır |
| VPN girişi | `event.category` | `authentication` kateqoriyasına uyğunlaşdır |
| İlkin sətir | `event.original` | Xam qeydi qorunan formada saxla |

ECS-də kateqoriya sahəsinin tipi də saxlanmalıdır; məhsulun sxemi massiv tələb edirsə, tək mətn yazılmır. İstifadəçi adı sahəsi dəyişməz şəxs identifikatorunu əvəz etmir: `ali`, `UNEC\ali` və `ali@kampus.example` eyni hesab ola bilər, amma yalnız ad oxşarlığı ilə birləşdirilməməlidir. IAM-in dəyişməz identifikatoru və domen məlumatı əsas götürülür. Silinmiş hesabın adı başqa şəxsə veriləndə köhnə davranış profili avtomatik ona keçməməlidir.

**NAT** arxasında yüzlərlə tələbə eyni xarici IP-dən görünə bilər. Yataqxana Wi-Fi hadisəsini şəxsə bağlamaq üçün **DHCP** icarəsinin vaxtı, simsiz sessiya və autentifikasiya identifikatoru tələb oluna bilər. Cari DHCP cədvəlini dünənki hadisəyə tətbiq etmək səhvdir: hadisə vaxtındakı uyğunluq saxlanılır. Bu zəncir yoxdursa, analitik nəticəni «şəxs müəyyən edildi» əvəzinə «mənbə şəbəkə müəyyən edildi» səviyyəsində məhdudlaşdırır.

## Ən vacib qeydlər

| Event ID | Məna | Niyə vacibdir |
| --- | --- | --- |
| 4624 | Uğurlu giriş | Logon Type 3 şəbəkə, 10 RDP-dir |
| 4625 | Uğursuz giriş | Kobud güc, parol püskürtməsi |
| 4648 | Ayrıca göstərilmiş kimlik məlumatları ilə giriş cəhdi (runas, planlaşdırılmış tapşırıq) | Daxili hərəkət. Uğurlu girişin təsdiqi deyil |
| 4672 | Xüsusi imtiyazlar təyin edildi | Admin girişləri |
| 4688 | Yeni proses yaradıldı | Komanda sətri audit ilə çox dəyərlidir |
| 4720 | Hesab yaradıldı | Dayaqlanma (persistence) |
| 4728, 4732 | Qrupa üzv əlavə edildi | İmtiyaz artımı |
| 4768, 4769 | Kerberos bileti | Kerberoasting |
| 1102 | Audit jurnalı təmizləndi | İzlərin silinməsi |
| 7045 | Yeni xidmət quraşdırıldı | PsExec və dayaqlanma |

Linux-da `/var/log/auth.log` (RHEL-də `/var/log/secure`), **journald** və **auditd** əsas mənbələrdir. **Sysmon** isə Windows-da əlavə detal verir: Event ID 1 proses, 3 şəbəkə bağlantısı, 11 fayl yaradılması.

Hadisələrin jurnalı da fərqlidir: 4688 Security, 7045 System jurnalında, Sysmon isə ayrıca kanaldadır, hər biri ayrıca toplanmalıdır. 4732-də həm əməliyyatı edən (Subject), həm qrupa əlavə olunan üzv (MemberSid) var; qayda düzgün sahəyə baxmalıdır.

:::warning Qeydlər defolt yazılmır
4688-də komanda sətri əlavə siyasətlə açılır; audit qaydaları sazlanmayan yerdə SIEM-ə məlumat gəlmir.
:::

### Müxtəlif mənbələrdən oxunan nümunələr

Ünvanlar, hesablar, həcm və vaxtlar şərtidir; JSON blokları sadələşdirilmişdir. Windows 4624:

```json
{"EventID":4624,"Computer":"lms01","TimeCreated":"2026-10-14T02:13:00Z","TargetUserName":"ali","LogonType":3,"IpAddress":"198.51.100.23","TargetLogonId":"0x91a"}
```

Qeyd şəbəkə girişinin uğurlu olduğunu göstərir; istifadəçinin klaviatura qarşısında oturduğunu və MFA keçdiyini sübut etmir. `TargetLogonId` yalnız host daxilində əlaqə qurur, qlobal sessiya identifikatoru deyil. **Kerberos** 4769-un çoxalması təkbaşına Kerberoasting sübutu deyil: xidmət hesabları, sorğu edən hesab, bilet parametrləri və adi fəaliyyət müqayisə edilir.

Linux SSH-da açar ilə giriş və imtiyaz istifadəsi ayrı qeydlərdir:

```text
sshd[2401]: Accepted publickey for ali from 198.51.100.23
sudo[2410]: ali : TTY=pts/0 ; PWD=/home/ali ; USER=root ; COMMAND=/usr/bin/id
```

auditd proses icrasını daha ətraflı göstərir, lakin qaydaları və həcm hədləri əvvəlcədən sazlanmalıdır. Laboratoriyada oxumaq üçün:

```bash
journalctl -u sshd --since '2026-10-14 02:00:00 UTC' --utc
ausearch -m EXECVE -ts recent -i
```

SSH xidmətinin adı distributivdə `ssh` ola bilər. Birinci əmr jurnalı sorğulayır, ikinci auditd-də proses arqumentlərini axtarır. Audit qaydası olmayan sistemdə boş nəticə prosesin işləmədiyini sübut etmir; komanda sətri parol və token saxlaya bildiyindən məzmun yoxlanmalıdır.

**Firewall** qeydi bağlantının buraxıldığını bildirir; tamamlanmasını və baytı bilmək üçün sessiyanın son qeydi lazımdır:

```text
ts=2026-10-14T02:41:00Z action=allow proto=tcp src=10.20.14.8 sport=52144 dst=203.0.113.70 dport=443 session=fw-81 bytes_out=2147483648
```

`bytes_out` mənası sənəddə yoxlanır: bəzi cihazlar sessiyanın cəmini, bəziləri son intervalın fərqini yazır; aralıq qeydlərdə yığılmış cəmi toplamaq həcmi şişirdər. NAT olduqda ilkin və çevrilmiş ünvanlar, imkan varsa portlar qorunur. `allow` «təhlükəsiz trafik» demək deyil, firewall sadəcə siyasəti tətbiq edib.

Proksi və DNS qeydləri sessiyaya ad və tətbiq konteksti əlavə edir:

```json
{"user":"ali","src":"10.20.14.8","method":"CONNECT","host":"paylasim.example:443","status":200}
{"client":"10.20.14.8","qname":"paylasim.example","qtype":"A","answer":"203.0.113.70"}
```

CONNECT-in 200 cavabı tunelin açıldığını bildirir, içindəki HTTPS sorğusunun nəticəsini yox. TLS məzmun yoxlaması yoxdursa, fayl adı və tam URL görünməyə bilər. DNS cavabı əlaqə qurulduğunu sübut etmir. DNS tunelləmə araşdırmasında uzun adlar, sorğu tezliyi, cavablar və klient prosesi birlikdə yoxlanır; kitabxananın qanuni axtarış xidməti uzun subdomenlər yarada bilər.

**CloudTrail** tipli bulud auditində API əməliyyatı görünür; `errorCode` kimi nəticə sahəsi ayrıca yoxlanır, əməliyyat adı uğuru bildirmir.

```json
{"eventSource":"iam.amazonaws.com","eventName":"CreateAccessKey","userIdentity":{"userName":"lab-admin"},"sourceIPAddress":"198.51.100.23","requestParameters":{"userName":"lab-service"}}
```

Əməliyyatı edənlə açar yaradılan hesab fərqlənə bilər (Windows qrup dəyişikliyində də eyni). İdarəetmə hadisələrinin toplanması bütün obyekt oxumalarının auditə düşməsi demək deyil; məlumat səviyyəli əməliyyatlar üçün ayrıca audit sazlaması lazımdır. Hər mənbə üçün «nəyi görmürük?» sualı mənbə pasportunda cavablandırılır.

## Korrelyasiya

Korrelyasiya hadisələr arasında vaxt, hesab, cihaz və IP əlaqəsi qurmaqdır. Ayrı-ayrılıqda zərərsiz görünən hadisələr birlikdə hücumu göstərə bilər.

| Növ | Məntiq | Nümunə |
| --- | --- | --- |
| Hədd əsaslı (threshold) | Pəncərədə sayı həddi keçir | 10 dəqiqədə 20 uğursuz giriş |
| Ardıcıllıq (sequence) | A-dan sonra B baş verir | Uğursuz girişlər, sonra uğurlu giriş |
| Çoxmənbəli | Müxtəlif mənbələr birləşir | VPN girişi, sonra bazadan ixrac |
| Kontekst əsaslı | Hadisə aktiv və ya rol ilə yoxlanır | Tələbə hesabı maliyyə serverinə giriş edir |
| Təhdid kəşfiyyatı | IP, domen, heş IoC siyahısı ilə tutuşdurulur | Bilinən C2 ünvanına bağlantı |
| Yoxluq (absence) | Gözlənilən hadisə baş vermir | Agent 30 dəqiqədir susur |
| Statistik, davranış | Normadan kənarlaşma | Gündəlik ixracın 15 dəfə artması |

:::note Konspektdəki dörd növ
Konspekt hədd, ardıcıllıq, zaman (müəllim hesabı gecə 03:00-da qiymətləri kütləvi dəyişir) və kontekst əsaslı (adi giriş, amma IP təhdid feed-indədir və hesab admin roludur) növlərini verir; ardıcıllıq nümunəsi: 10 uğursuz giriş → 15 dəqiqə ərzində uğurlu giriş → yeni cihaz → qiymət bazasına müraciət.
:::

**Çoxmənbəli ardıcıllıq** nümunəsi: VPN girişi (VPN logu) → hesaba imtiyazlı rol verilməsi (Entra ID logu) → tələbə bazasının ixracı (DB logu) → xarici serverə böyük həcmdə yükləmə (proksi logu). Heç bir mənbə təkbaşına bu zənciri görmür. Etibarlı hesabın sui-istifadəsi ATT&CK-da T1078 (Valid Accounts) texnikasıdır: uğurlu giriş avtomatik təhlükəsiz demək deyil.

### Qayda nümunəsi: parol püskürtməsi

Parol püskürtməsində (*password spraying*, MITRE ATT&CK T1110.003) bir parol çoxlu hesaba sınanır. Hesab üzrə hədd burada işləmir, çünki hər hesaba bir-iki cəhd gəlir. Qayda mənbə IP üzrə fərqli hesabların sayını götürməlidir.

:::exam Tələ: brute force və password spraying
"Bir hesabda 10 uğursuz giriş" qaydası brute force-u (kobud güc) tutur, amma password spraying-i tutmur: hücumçu 2 000 tələbə hesabının hər birində yalnız 1–2 parol sınayır. Bunun üçün "bir IP-dən qısa müddətdə çox fərqli hesaba uğursuz giriş" qaydası lazımdır.
:::

Splunk SPL:

```text
index=wineventlog EventCode=4625
| bin _time span=10m
| stats count AS cehd, dc(TargetUserName) AS hesab BY _time, IpAddress
| where cehd > 20 AND hesab > 10
```

Microsoft Sentinel KQL:

```text
SecurityEvent
| where TimeGenerated > ago(1h) and EventID == 4625
| summarize cehd = count(), hesab = dcount(TargetAccount)
    by IpAddress, bin(TimeGenerated, 10m)
| where cehd > 20 and hesab > 10
```

Rəqəmlər tədris üçündür, real hədlər mühitin normal göstəricilərinə görə tənzimlənir. `bin` vaxtı sabit 10 dəqiqəlik parçalara bölür: 09:58-dən 10:03-ə qədər gedən hücum iki parçaya düşür və hər birində say həddən aşağı qala bilər. Sürüşən pəncərə bu problemi həll edir. Gecikmiş və təkrarlanan hadisələr də qayda planlaşdırılarkən nəzərə alınır. Vendor asılılığını azaltmaq üçün qaydalar **Sigma** formatında yazılıb konkret SIEM dilinə çevrilə bilər.

### Qaydanın həyat dövrü

Hər qaydanın sənədi olmalıdır: hansı ssenarini tutur, hansı ATT&CK texnikasına uyğundur, hansı mənbələri tələb edir, məlum yanlış müsbət səbəbləri nədir, analitik nəyi yoxlamalıdır, sahibi kimdir. Qayda test mühitində yoxlanır, işə salınır, müntəzəm tənzimlənir. İstisna əlavə edilərkən diqqətli olmaq lazımdır: «xidmət hesabını qaydadan çıxardıq» hücumçu üçün hazır boşluqdur.

MITRE ATT&CK ilə örtük xəritəsi hansı texnikaların görünmədiyini göstərir. Məsələn, T1078 (Valid Accounts) üçün yalnız uğursuz girişlərə baxmaq kifayət deyil, uğurlu girişdən sonrakı fəaliyyət yoxlanmalıdır.

### Hazır ssenarilər

| Ssenari | ATT&CK | Mənbələr və məntiq | Yanlış müsbət səbəbi |
| --- | --- | --- | --- |
| Kobud güc | T1110.001 | 4625, bir hesaba çoxlu cəhd | Köhnə parol saxlayan tətbiq |
| Parol püskürtməsi | T1110.003 | 4625, bir IP-dən çoxlu hesaba | Səhv sazlanmış xidmət |
| Mümkünsüz səyahət (*impossible travel*) | T1078 | VPN/IAM, iki uzaq ölkədən qısa fasilə ilə giriş | Korporativ VPN çıxışı |
| İmtiyaz artımı | T1098 | 4728, 4732, plansız admin qrupuna əlavə | Dəyişiklik sifarişi |
| İzlərin silinməsi | T1685.005 (köhnə nömrəsi T1070.001) | 1102 | Texniki xidmət |
| Yeni xidmət | T1543.003 | 7045, qeyri-adi yoldan fayl | Proqram quraşdırılması |
| DNS tunelləmə | T1071.004 | Uzun, yüksək entropiyalı subdomenlər | CDN və antivirus sorğuları |
| C2 kanalı ilə məlumat çıxarılması | T1041 | Əvvəldən müəyyən edilmiş C2 kanalı üzərindən ötürmə: proksi, DLP, həcm anomaliyası | Bulud yedəkləmə |

### Xəbərdarlığın araşdırılması

Analitik «mümkünsüz səyahət» xəbərdarlığını belə araşdırır:

1. Xəbərdarlığın hansı qeydlərə əsaslandığına baxır: iki giriş də həqiqətən eyni hesabındırmı?
2. IP ünvanlarını yoxlayır: biri universitetin VPN çıxışıdırsa, səyahət yalançıdır.
3. MFA nəticəsinə baxır: MFA keçibmi, yoxsa köhnə protokol ilə giriş olub?
4. Cihazı müəyyən edir: yeni və idarə olunmayan cihazdır?
5. Girişdən sonrakı fəaliyyəti zaman xəttinə düzür: poçt qaydaları, fayl yükləmələri, parol dəyişikliyi.
6. İstifadəçi ilə ayrı kanaldan əlaqə saxlayır.
7. Qərar verir: FP kimi bağlayır, qaydaya dar istisna təklif edir və ya insident açır.
8. Sübutları qeyd edir ki, sonrakı analitik eyni işi təkrar etməsin.

### Sabit və sürüşən pəncərələr

**Sabit pəncərə (tumbling window)** vaxtı üst-üstə düşməyən hissələrə bölür: 09:50–10:00, 10:00–10:10. **Sürüşən pəncərə (sliding window)** isə hər qiymətləndirmə anından əvvəlki intervalı götürür. Şərti hücumda 09:58-də on iki, 10:03-də on iki cəhd olarsa, sabit pəncərələrin heç birində iyirmidən çox cəhd yoxdur. 10:03-də bitən on dəqiqəlik sürüşən pəncərə isə iyirmi dörd cəhdi birlikdə görür. Bu fərq qaydanın təhlükə məntiqini dəyişir.

![figure](m12-4.png)

Şəkil 4. Sabit pəncərənin sərhədində bölünən cəhdlər (A və B pəncərəsində 12 cəhd, hədd keçilmir) və onları birlikdə görən sürüşən pəncərə (09:53–10:03, 24 cəhd, hədd > 20); saylar şərtidir.

Sürüşən pəncərənin də xərci var: daha çox vəziyyət saxlanılır və eyni hadisələr bir neçə dəfə qiymətləndirilir. Planlaşdırılmış qaydanın hər beş dəqiqədə son on dəqiqəni oxuması üst-üstə düşən axtarışdır, bütün mümkün sürüşən pəncərələrin hesablanması deyil. Hücum daha qısa intervalda və icralar arasında baş verirsə, zəif seçilmiş addım yenə boşluq yarada bilər.

SPL-də hadisə əsasında sürüşən pəncərə nümunəsi (hədlər şərtidir; qayda son bir saatı oxuyur, hər IP üçün on dəqiqəlik cəhdləri və fərqli hesabları hesablayır; `max_stream_window` və yaddaş məhdudiyyətləri həcmlə sınaqdan keçirilməlidir):

```text
index=wineventlog earliest=-1h EventCode=4625
| where isnotnull(IpAddress) AND IpAddress!="-"
| sort 0 _time
| streamstats time_window=10m count AS cehd dc(TargetUserName) AS hesab BY IpAddress
| where cehd > 20 AND hesab > 10
| stats earliest(_time) AS ilk latest(_time) AS son max(cehd) AS cehd max(hesab) AS hesab BY IpAddress
```

Son `stats` bir icrada IP üzrə nəticələri yığır. Növbəti icrada həmin hücum yenə görünə bilər; xəbərdarlıq açarı və məhdud müddətli birləşdirmə tələb olunur. Universitetin NAT çıxışını qeyd-şərtsiz istisna etmək olmaz: idarə olunan cihaz, istifadəçi agenti və sessiya identifikatoru əlavə ölçü ola bilər. Paylanmış püskürtmə müxtəlif IP-lərdən gəlirsə, hesablar və zaman üzrə daha geniş davranış qaydası tələb olunur.

### Uğursuz girişdən sonrakı uğurlu giriş

İki qayda eyni ssenarini fərqli dillərdə təsvir edir: eyni hesab və mənbə IP üçün əvvəlki beş dəqiqədə ən azı on uğursuz girişdən sonra uğurlu giriş. Say və intervallar şərtidir. SecurityEvent cədvəlində `TargetAccount` və `IpAddress`, SPL-də isə `TargetUserName` və `IpAddress` sahələrinin dolu olduğu fərz edilir; sahə adları kollektorun sxeminə uyğunlaşdırılır, mənbələrdə fərqli yazılan hesab adları əvvəlcə normallaşdırılmalıdır.

```text
index=wineventlog earliest=-30m (EventCode=4624 OR EventCode=4625)
| where isnotnull(TargetUserName) AND isnotnull(IpAddress)
| eval fail=if(EventCode=4625,1,0)
| sort 0 _time
| streamstats time_window=5m sum(fail) AS failures BY TargetUserName IpAddress
| where EventCode=4624 AND failures>=10
| table _time TargetUserName IpAddress failures
```

Bu SPL cəhdlərin cari uğurlu hadisədən əvvəlki intervalda olmasını hadisə sırası ilə yoxlayır. Eyni vaxt damğalı hadisələrdə sıra qeyri-müəyyən qala bilər; mənbə ardıcıllıq nömrəsi varsa, o işlədilir. Bir hesabın bütün IP-lərini birləşdirmək başqa ssenaridir: kampusdakı səhv parol cəhdləri ilə uzaqdakı qanuni girişi qarışdıra bilər. Qaydanın əlaqələndirmə açarı buna görə əsaslandırılır.

```text
let F = SecurityEvent
  | where TimeGenerated > ago(30m) and EventID == 4625
  | project U=TargetAccount, IP=IpAddress, FTime=TimeGenerated;
let S = SecurityEvent
  | where TimeGenerated > ago(30m) and EventID == 4624
  | project U=TargetAccount, IP=IpAddress, STime=TimeGenerated, EventKey=_ItemId;
S
| join kind=inner F on U, IP
| where FTime < STime and FTime >= STime - 5m
| summarize failures=count(), firstFail=min(FTime) by U, IP, STime, EventKey
| where failures >= 10
```

KQL nümunəsi hər uğurlu hadisəni özündən əvvəlki cəhdlərlə birləşdirir. `_ItemId` platformanın qeyd identifikatorudur; başqa cədvəldə həmin məqsəd üçün mənbənin təkil identifikatoru seçilir. Eyni uğursuz qeydin təkrar qəbulu sayı şişirdə bilər, buna görə giriş qatında deduplikasiya yoxlanır. `join` böyük cədvəllərdə bahalıdır: əvvəl vaxt, hadisə tipi və lazım olan sahələr üzrə azaltma aparılır. Geniş mühitdə vəziyyət saxlayan mexanizm daha uyğundur.

### Audit jurnalının təmizlənməsi və Sigma

1102 hadisəsi yüksək diqqət tələb edir: audit jurnalının təmizləndiyini göstərir. Lakin həmin hadisəni görmək üçün audit kanalının özü toplanmalıdır. Aşağıdakı KQL qaydası hər qeydi qaytarır; təsdiqlənmiş texniki iş sonradan kontekst kimi əlavə olunur. İstisna həm icra edən hesabı, həm hostu, həm də qüvvədə olan dəyişiklik vaxtını əhatə etməlidir.

```text
SecurityEvent | where TimeGenerated > ago(15m) and EventID == 1102
```

**Sigma** məhsuldan asılı olmayan aşkarlama təsviridir. Bu nümunə sadə hadisə seçir; say və ardıcıllıq korrelyasiyası tələb etmir. Sigma sahəsi backend-də düzgün Windows sahəsinə çevrilməlidir. `status: test` qaydanın istehsalda yoxlanmış sayılmadığını bildirir.

```yaml
title: Windows audit jurnalının təmizlənməsi
status: test
logsource: {product: windows, service: security}
detection:
  selection: {EventID: 1102}
  condition: selection
falsepositives: [Təsdiqlənmiş texniki xidmət]
level: high
```

Real qaydada `id` (UUID), `author` və `date` sahələri də olur. Sigma-dan çevrilən sorğu nəzərdən keçirilmədən tətbiq edilmir: səhv sahə uyğunluğu, backend-in imkanları və məlumat cədvəli nəticəni dəyişir. `high` səviyyəsi işin prioritetini bildirir, hadisənin mütləq hücum olduğunu yox. Hücumçu mənbəni söndürə bilirsə, 1102 də gəlməyə bilər; susan mənbə nəzarəti bu boşluğu qismən azaldır.

### Aşkarlamanın kodla idarəsi və ATT&CK örtüyü

**Aşkarlamanın kodla idarəsi (detection as code)** qaydanı versiyalanan, nəzərdən keçirilən və sınaqdan çıxarılan artefakt sayır. Repozitoriyada məntiq, sxem versiyası, test hadisələri, gözlənilən nəticələr və araşdırma təlimatı birlikdə qalır. Dəyişiklikdə müəllifin adı, səbəb, əvvəlki və sonrakı xəbərdarlıq yükü görünür. Qaydanı paneldə səssiz dəyişmək «bu insident niyə tutulmadı?» cavabını itirir.

| Mərhələ | Yoxlama | Universitet nümunəsi |
| --- | --- | --- |
| Ssenari | Hansı davranış axtarılır? | Qiymət bazasının plansız ixracı |
| Mənbə müqaviləsi | Sahə, vaxt və həcm məlumdurmu? | DB ixrac identifikatoru doludur |
| Sintaksis testi | Sorğu düzgün çevrilirmi? | Sigma backend uyğunluğu |
| Müsbət və mənfi test | Hücum və adi fəaliyyət ayrılırmı? | İxrac və qanuni arxivləşdirmə |
| Sərhəd testi | Vaxt və hədd necə işləyir? | Pəncərə sərhədində cəhdlər |
| Kölgə rejimi | Cavabsız müşahidədə yük nədir? | Sessiya həftəsinin səs-küyü |
| Buraxılış və geri qaytarma | Sahib və əvvəlki versiya varmı? | Yanlış bloklama olarsa bərpa |

Testlərdə həddin bir altı, özü və bir üstü yoxlanır. İstehsal ölçüləri yalnız FP sayını azaltmağa yönəlməməlidir: qaydanı söndürmək FP-ni sıfırlayır, amma FN-ni artırır. L3 analitiki ilə mənbə sahibi birlikdə qaydanın gördüyü davranışın hələ eyni mənanı daşıdığını yoxlayır.

MITRE ATT&CK v19 28 aprel 2026-cı ildə Enterprise bölməsində əvvəlki Defense Evasion taktikasını Stealth (TA0005) və Defense Impairment (TA0112) üzrə ayırıb. Windows hadisə jurnallarının təmizlənməsi əvvəlki T1070.001 əvəzinə T1685.005 identifikatoru ilə göstərilir. Köhnə mənbələr əvvəlki ad və nömrədən istifadə edir. Xəritədə ATT&CK versiyası saxlanmalı, qayda məntiqi dəyişməsə də istinadlar yenilənməlidir.

Örtük «texnikaya bir qayda bağlandı» ilə təsdiqlənmir. T1078 üçün universitet yalnız Windows girişini görür, bulud LMS girişini görmürsə, örtük qisməndir. Hər ssenari üçün tələb olunan mənbə, işlək parser, aktiv qayda və keçilmiş sınaq ayrıca qeyd edilir. Şərti olaraq seçilmiş iyirmi prioritet ssenaridən on ikisi tam yoxlanıbsa, həmin çərçivədə təsdiqlənmiş örtük 12 / 20 = 60%-dir. Bu, bütün hücumların 60%-nin tutulduğu demək deyil.

## UEBA

Qayda əvvəlcədən yazılmış şərti yoxlayır. **UEBA** (*User and Entity Behavior Analytics*) fəaliyyətin normal davranışdan nə qədər fərqləndiyini ölçür.

| | UBA (User Behavior Analytics) | UEBA (User and Entity BA) |
| --- | --- | --- |
| Kimi izləyir | Yalnız istifadəçiləri | İstifadəçilər + cihazlar, serverlər, tətbiqlər, xidmət hesabları |
| Nəyi tutur | Oğurlanmış hesab, daxili təhdid | Bunlara əlavə: yoluxmuş server, sui-istifadə olunan xidmət hesabı |

Fərq alqoritmdə yox, izlənən obyektlərin dairəsindədir. Hər ikisi əvvəlcə **baza profili (baseline)** qurur: istifadəçi adətən nə vaxt, hansı cihazdan, haradan işləyir, hansı resurslara nə qədər müraciət edir.

![figure](m12-5.png)

Şəkil 5. Gündəlik ixrac həcmində anomaliya (şərti nümunə): 13 gün 150–245 MB aralığında, orta təxminən 200 MB; 14-cü gün 650 MB.

Davranış profili üçün 30–90 günlük tarixçə tez-tez seçilir, amma bu universal tələb deyil; müddət modeldən və iş rejimindən asılıdır. Profilə bunlar daxildir: iş saatları, tipik IP və cihazlar, işlədilən tətbiqlər, məlumat həcmi. Müqayisə üç bucaqdan aparılır: şəxsin öz keçmişi, **oxşar qrup (peer group**, məsələn, eyni kafedra müəllimləri) və təşkilat ortalaması. Yeni işçilər üçün profil yoxdur, ona görə qrup müqayisəsi işlədilir.

**Z-balı** sadə statistik üsuldur: z = (x − μ) / σ. Şəkildəki nümunədə ilk 13 günün orta göstəricisi μ ≈ 202 MB, standart kənarlaşma σ ≈ 29 MB-dır. 14-cü gün x = 650 MB olduqda z ≈ (650 − 202) / 29 ≈ 15. Bu qədər böyük kənarlaşma diqqət çəkir. Z-balı standartlaşdırılmış məsafədir; ondan normal paylanmaya əsaslanan nadirlik nəticəsi çıxarmaq üçün əlavə fərziyyələr lazımdır: həftəsonu və imtahan mövsümü kimi dövrilik, sıfır dispersiya, əyri paylanma yanlış nəticə verə bilər.

:::note Konspektin z-balı nümunəsi
Müəllim adətən gündə orta 200 MB (μ), standart sapma 50 MB (σ) yükləyir. Bu gün 500 MB yükləyib: z = (500 − 200) / 50 = 6, yəni normaldan 6 standart sapma uzaqdır, bu çox nadir haldır. Bu nümunə şəkildəki (650 MB, z ≈ 15) verilənlərdən ayrıdır: qarışdırma. Amma anomaliya risk deyil: bəlkə imtahan həftəsidir və müəllim bütün işləri yükləyir. Ona görə risk balı anomaliyanı kontekstlə birləşdirir.
:::

Risk balı ayrı siqnalları toplayır və zaman keçdikcə azalır:

| Siqnal | Bal | Cəmi |
| --- | --- | --- |
| Yeni ölkədən VPN girişi | +20 | 20 |
| Gecə saatlarında giriş | +10 | 30 |
| İmtiyazlı qrupa əlavə olunma | +40 | 70 |
| Həcm anomaliyası (z ≈ 15) | +30 | 100 |
| Hədd: 80 və yuxarı olduqda SOC-a | Xəbərdarlıq | SOC-a ötürülür |

Risk balı ehtimal deyil, prioritet göstəricisidir. Eyni hadisədən yaranan oxşar siqnalları iki dəfə saymaq olmaz.

Anomaliya insident demək deyil. Müəllim ilk dəfə xaricdəki konfransdan LMS-ə girə bilər, tələbə imtahan dövründə gecə də işləyə bilər. Model yalnız diqqət yönəldir, qərarı analitik verir. Qərarın əsaslandırıla bilən olması vacibdir: analitik balın niyə yüksəldiyini görməlidir. İzləmə məxfilik və hüquq baxımından razılaşdırılır, qeydlərə giriş məhdudlaşdırılır.

UEBA-nın təbii zəifliyi də var: normal hesab edilən mərhələdə hücumçu artıq şəbəkədədirsə, onun davranışı norma kimi öyrənilir.

### Anomaliya növləri və analitik üsullar

| Növ | Mahiyyəti | Universitet nümunəsi |
| --- | --- | --- |
| Nöqtə anomaliyası | Bir qiymət normadan kəskin fərqlənir | Gündəlik 200 MB yerinə 650 MB ixrac |
| Kontekst anomaliyası | Qiymət adidir, şərait qeyri-adidir | Fayl yükləmə gündüz normaldır, gecə 03:00-da yox |
| Kollektiv anomaliya | Hər hadisə adi görünür, birlikdə qeyri-adidir | Bir cihazdan ardıcıl 50 tələbə hesabına giriş |

Konspektdə anomaliya növləri belə sadalanır: zaman (gecə girişi), cihaz (yeni cihaz), həcm (kütləvi yükləmə), resurs (heç vaxt girmədiyi qovluq), ardıcıllıq (qeyri-adi əməliyyat sırası), coğrafi (bir saat ərzində Bakı və Frankfurt, "mümkünsüz səyahət"). VPN, mobil şəbəkə və proksi coğrafi təyini çaşdıra bilər.

Statistik üsullardan başqa maşın öyrənməsi də işlədilir. **Nəzarətsiz öyrənmə** (*unsupervised learning*: klasterləşmə, Isolation Forest) etiket tələb etmir və çoxluqdan fərqlənən fəaliyyəti tapır. **Nəzarətli** üsullar keçmiş insidentlərin etiketli məlumatını tələb edir, amma real hücum nümunələri azdır. Hansı üsul seçilsə də, analitik balın səbəbini görə bilməlidir: izah olunmayan model SOC-da etibar qazanmır. Maşın öyrənməsi yalnız UEBA-ya məxsus deyil, UBA da ondan istifadə edir; fərq izlənən obyektlərdədir.

### Konseptin sürüşməsi

Normal davranış zamanla dəyişir: imtahan sessiyası, onlayn dərslərə keçid, yeni sistem, yeni semestr, yeni vəzifə. Bu, **konseptin sürüşməsidir (concept drift)**. Model yavaş uyğunlaşsa (yenilənməsə), yanlış həyəcanlar artır. Çox tez yenilənsə, hücumçu fəaliyyətini tədricən artıraraq normanı özünə uyğun dəyişə bilər (**low and slow**). Ona görə baseline nəzarətli yenilənir, təsdiqlənmiş insident dövrləri öyrənmədən çıxarılır, böyük dəyişikliklər planlı hadisələrlə tutuşdurulur.

### DLP: məlumat sızmasının qarşısının alınması

**DLP** (*Data Loss Prevention*) həssas məlumatın icazəsiz çıxmasını aşkar edir və dayandırır. SIEM üçün əhəmiyyətli mənbədir, amma ayrıca sistemdir. Məlumatı üç vəziyyətdə izləyir:

| Növ | Nəyi görür | Nümunə |
| --- | --- | --- |
| Şəbəkə DLP | Hərəkətdə olan məlumat: poçt, veb yükləmə | Tələbə siyahısı xarici poçta göndərilir |
| Son qurğu DLP | İstifadədə olan məlumat: USB, çap, kopyalama | Maaş cədvəli USB-yə köçürülür |
| Saxlama, bulud DLP | Sükunətdə olan məlumat: fayl serverləri, SaaS | Açıq paylaşılan qovluqda şəxsiyyət vəsiqələri |

Aşkarlama üsulları: müntəzəm ifadələr (FİN kod, kart nömrəsi), sənədin rəqəmsal barmaq izi, kateqoriya etiketləri, maşın öyrənməsi. DLP şifrəli trafikdə TLS yoxlaması olmadan məhduddur, yeni kanallarda (şəxsi bulud, mesajlaşma) isə əlavə sazlama tələb edir. Tək qaydanın çox sərt olması işi dayandırır, ona görə əvvəlcə izləmə rejimində başlanır, sonra bloklamaya keçilir.

### Baza profilinin qurulması və statistik seçim

Əvvəlcə müşahidə vahidi seçilir. İstifadəçi-gün sətri gündəlik endirilən baytları, fərqli resursların sayını və gecə girişlərinin payını saxlaya bilər; cihaz-saat sətri DNS sorğularını və yeni xarici ünvanların sayını. Dəqiqəlik və gündəlik həcmləri eyni cədvəldə qarışdırmaq yanlış müqayisə verir. Tarixçə azdırsa, profilin etibarlılığı da bal ilə yanaşı göstərilir.

Oxşar qrup yalnız şöbə adına görə qurulmur: vəzifə, tətbiq və səlahiyyətlər nəzərə alınır. Kafedra katibi tələbə siyahılarını müntəzəm ixrac edir, digər əməkdaş yalnız dərs materialı yerləşdirir; ortalama hər ikisini yanlış qiymətləndirə bilər. Qrup kiçikdirsə, bir böyük müşahidə həddi dəyişir; fərdi profil və daha geniş rol qrupu birlikdə yoxlanır.

Ortalama və standart kənarlaşma böyük sıçrayışlardan təsirlənir. Şərti ikinci nümunədə μ = 200 MB, σ = 50 MB, x = 500 MB olarsa, z = 6 (əvvəlki diaqramın verilənlərindən ayrıdır). Z-balı hesablamaq üçün normal paylanma şərt deyil; «bu kənarlaşma hansı ehtimalla baş verir?» sualı isə həmin modelə uyğunluq tələb edir. σ sıfırdırsa, bölmə aparılmır; ilk dəfə görünən fəaliyyət ayrıca siqnal ola bilər.

**Persentil** sıralanmış tarixçədə mövqe göstərir: yüz iş günündə həcmlərin doxsan beşi 400 MB-dan çox deyilsə, 400 MB empirik 95-ci persentil həddi ola bilər. Kvantil üsulları fərqli ara qiymətlər verə bilər, üsul sənədləşdirilir. Hədd aşılması hücumu sübut etmir; normal müşahidələrin bir hissəsinin xəbərdarlığa çevrilməsi gözlənilir.

**Median mütləq yayınma (MAD):** median, hər müşahidənin mediandan mütləq məsafəsi, bu məsafələrin medianı. Bir təsdiqlənmiş böyük arxivləşdirmə ortalamanı kəskin dəyişəndə median əsaslı hədd sabit qala bilər. MAD də sıfır ola bilər: sıfırı gizli kiçik sabitlə əvəz edib böyük risk çıxarmaq əvəzinə «kifayət qədər dəyişkən tarixçə yoxdur» nəticəsi verilir.

**Mövsümilik (seasonality)** vaxtın təkrarlanan təsiridir; imtahan həftəsini adi həftə ilə müqayisə etmək düzgün deyil. Həftənin günü, yerli iş saatı və akademik təqvim ayrıca xüsusiyyət ola bilər. Cari gün təlimə daxil edilib özünü normallaşdırmamalı, əvvəlki uyğun dövrlərlə müqayisə olunmalıdır. Test məlumatının gələcək hissəsini təlimdə işlətmək məlumat sızmasıdır, qiymətləndirməni süni yaxşılaşdırır.

| Xüsusiyyət | Universitet nümunəsi | Yoxlanmalı məhdudiyyət |
| --- | --- | --- |
| Vaxt | Gecə qiymət dəyişikliyi | Növbə və akademik təqvim |
| Cihaz | İlk dəfə görünən noutbuk | Yenidən quraşdırmadan dəyişən identifikator |
| Həcm | Kütləvi tələbə sənədi endirmə | Arxivləşdirmə və sessiya həftəsi |
| Resurs | Başqa fakültənin qovluğu | Vəzifə və layihə dəyişikliyi |
| Ardıcıllıq | Giriş, rol dəyişikliyi, ixrac | Avtomatik idarəetmə tapşırığı |
| Coğrafiya | Uzaq məkanlardan giriş | VPN, mobil şəbəkə və proksi |

### Isolation Forest, klasterləşmə və qraf təhlili

**Isolation Forest** müşahidələri təsadüfi seçilmiş xüsusiyyət və bölünmə həddi ilə ayıran ağaclar qurur. Çoxluqdan uzaq nöqtə adətən daha az bölünmə ilə ayrılır; müxtəlif ağaclardakı yol uzunluqları birləşdirilərək anomaliya göstəricisi alınır. Gecə payı, fərqli resurs sayı və ixrac həcmi birlikdə qeyri-adi olan hesab təkcə həcm həddini keçməsə də seçilə bilər. İşarələnən kənar nöqtə zərərli sinif etiketi daşımır. Modelə verilən sahələr mənalandırılır: istifadəçi adını rəqəmə çevirib aralarında məsafə hesablamaq düzgün deyil; kateqorik sahələr kodlaşdırılır, boş dəyərlər «sıfır fəaliyyət» ilə qarışdırılmır. Kənar müşahidə payı parametri məlum hücum faizi deyil. Analitikə hansı xüsusiyyətlərin şəxsin və qrupun tarixçəsindən fərqləndiyi göstərilir.

**Klasterləşmə** oxşar müşahidələri qruplaşdırır. **k-ortalar (k-means)** üsulunda qrupların sayı seçilir, nöqtələr mərkəzlərə təyin olunur, mərkəzlər yenilənir; yeni hesabın ən yaxın mərkəzdən uzaqlığı anomaliya siqnalı ola bilər. Baytlarla ölçülən həcm kiçik sayları üstələməsin deyə miqyas uyğunlaşdırılır. Fərqli ölçülü və uzunsov qruplarda məsafə fərziyyələri uyğun gəlməyə bilər. **DBSCAN** sıxlığa əsaslanan alternativdir, sıxlıq parametrlərinə həssasdır.

**Nəzarətli təsnifat** «hücum» və «adi fəaliyyət» etiketləri tələb edir. SOC-un sadəcə bileti bağlaması etibarlı etiket deyil: məlumat çatışmadığı üçün bağlanan işi «zərərsiz» öyrətmək modeli çaşdırır. Az olan hücum sinfinə görə ümumi düzgünlük göstəricisi yanıltıcıdır. Model vaxt üzrə ayrılmış testdə qiymətləndirilir, eyni insidentin yaxın surətləri həm təlimə, həm testə salınmır; insan rəyi ilə etiketlər düzəldilir, model versiyası saxlanılır.

**Qraf təhlilində** hesab, cihaz və resurs düyün, giriş isə əlaqədir. Kitabxana kompüterindən ilk dəfə maliyyə bazasına keçən hesab nadir görünə bilər; ortaq laboratoriya cihazı isə təbii olaraq çox hesabla əlaqəlidir, ona görə əlaqənin vaxtı, istiqaməti və rol konteksti saxlanılır. Kimlik uyğunlaşdırmasındakı səhv qrafda böyüyür: iki müxtəlif hesab birləşdirilibsə, saxta əlaqələr yaranır. UBA da bu üsullardan istifadə edə bilər; UEBA fərqi obyektlərin dairəsindədir.

### Risk balı, təkrar sayma və modelin yenilənməsi

Çəkili şərti model: **R = 0,4A + 0,35K + 0,25S**; A anomaliya, K təhlükə konteksti, S resursun (məlumatın) həssaslığıdır, hər biri 0–100 şkalasındadır. A = 80, K = 60, S = 90 üçün R = 32 + 21 + 22,5 = 75,5. Başqa şərti model R = 0,4A + 0,3K + 0,3V götürür; burada K aktivin kritikliyi, V təhlükə indikatorlarıdır. A = 80, K = 90, V = 70 olduqda nəticə 32 + 27 + 21 = 80-dir. Düsturların dəyişənləri qarışdırılmır və heç biri məhsul standartı deyil.

**Təkrar sayma.** Eyni VPN girişi «yeni ölkə», «mümkünsüz səyahət» və «nadir IP» siqnalları yarada bilər; bunları müstəqil sübutlar kimi toplamaq balı şişirdər. Siqnallar əsas hadisə və səbəb qrupuna bağlanır; eyni giriş konteksti üçün maksimum bal və ya qrup limiti tətbiq oluna bilər. DB ixracı ilə həmin fayla aid DLP xəbərdarlığı da eyni ötürməni təsvir edə bilər. Mənbələrin fərqli olması sübutların müstəqil olması demək deyil.

**Balın azalması.** Köhnə siqnalın həmişə hesabı yüksək riskdə saxlamasını məhdudlaşdırır. Şərti yarımparçalanma modeli ilə 40 ballıq siqnal seçilmiş müddətdən sonra 20, növbəti eyni müddətdən sonra 10 bal ola bilər. Təsdiqlənmiş açıq insident sadəcə vaxt keçdiyi üçün bağlanmır; balın azalması ilə işin statusu ayrı saxlanılır. Yeni hadisə əvvəlkinin davamıdırsa, eyni araşdırmaya əlavə olunur.

**Sürüşməyə nəzarət.** Həftəlik xüsusiyyət paylanmaları, xəbərdarlıq sayı və analitiklərin FP rəyləri müqayisə edilir. Kafedranın bütöv qrupu eyni vaxtda çox fayl endirirsə, akademik təqvim yoxlanır; tək hesabın tədricən artan ixracı isə qrup dəyişməsi kimi qəbul edilmir. Model namizədi əvvəlcə kölgə rejimində işləyir, əvvəlki versiya ilə eyni məlumatda müqayisə olunur. Təsdiqlənmiş insident intervalları və etibarsız etiketlər yenidən təlimdən çıxarılır.

## SOAR, XDR və SOC prosesləri

| Sistem | Vəzifəsi | SIEM-dən fərqi |
| --- | --- | --- |
| EDR | Son qurğuda davranışı izləyir və cavab verir | Yalnız qurğu səviyyəsidir, amma daha dərindir |
| XDR | Bir neçə təhlükəsizlik qatının telemetriyasını və cavabını birləşdirir | Çox vaxt müəyyən ekosistemə bağlıdır, açıq inteqrasiyalar da mümkündür |
| UEBA | Davranış anomaliyasını tapır | SIEM-ə modul və ya məlumat qatıdır |
| SOAR | Playbook-larla araşdırmanı və cavabı avtomatlaşdırır | Əsas vəzifəsi iş axınıdır, aşkarlama nəticələrini də emal edir |
| SOC | İnsanlar və proseslər | Texnologiya deyil, komanda |

**SOAR** (*Security Orchestration, Automation and Response*) təkrarlanan işi öz üzərinə götürür: IP-ni zənginləşdirmək, hesabı müvəqqəti bloklamaq, bilet açmaq. Fişinq xəbərdarlığı üçün playbook belə ola bilər: məktubdakı keçidləri və heşi yoxla, eyni məktubu alan hesabları tap, keçid zərərlidirsə məktubu bütün qutulardan sil, keçidi açan hesablar üçün parol sıfırlaması və sessiya ləğvi tələb et. Hesabın bloklanması kimi yüksək təsirli addımlar analitikin təsdiqi ilə icra olunur; dağıdıcı avtomatik əməllər (hesab bloklama, cihaz təcridi) üçün hədd, icazə və geri qaytarma planı olmalıdır, yoxsa yanlış həyəcan bütün kafedranı işsiz qoya bilər.

**SOC** (Security Operations Center) xəbərdarlıqları araşdıran komandadır. Üç səviyyə: **L1** xəbərdarlıqları ilkin yoxlayır (triage) və bağlayır və ya yuxarı ötürür; **L2** insidenti dərin araşdırır; **L3** təhdid ovu (**threat hunting**) aparır, mürəkkəb insidentlərlə məşğul olur və yeni qaydalar hazırlayır.

**NIST SP 800-61 və CSF 2.0.** İnsidentlə işləmə NIST SP 800-61 tövsiyələrinə əsaslanır. Rev. 3 (aprel 2025) bu işi NIST Cybersecurity Framework 2.0 funksiyaları ilə əlaqələndirir. Hazırlıq, aşkarlama, cavab və bərpa işləri bu çərçivədə təşkil olunur, təcrübədən çıxarılan nəticələr prosesə qaytarılır. Jurnal idarəetməsi üçün isə NIST SP 800-92 əsas mənbədir, onun yeni versiyasının layihəsi 2023-cü ildə dərc olunub.

:::note Köhnə slaydlarla fərq
Konspektdəki insidentə cavab dövrü (hazırlıq → aşkarlama və təhlil → məhdudlaşdırma → aradan qaldırma və bərpa → dərslər) NIST SP 800-61 **Rev. 2**-nin dörd mərhələsidir (məhdudlaşdırma, aradan qaldırma və bərpa orada bir mərhələdir). Rev. 3-ün dəyişməz mərhələləri kimi təqdim etmək düzgün deyil. Köhnə slaydlarda üç düzəliş: (1) z-balı nümunəsi (μ = 200, σ = 50, x = 500 → z = 6) düzgündür, amma yanındakı qrafikdə başqa rəqəmlər göstərilib: qarışdırma; (2) FPR = FP / (FP + TN), xəbərdarlıqların boş payı isə FP / (TP + FP): fərqli göstəricilərdir; (3) "Azure Sentinel" məhsulun köhnə adıdır, indi Microsoft Sentinel adlanır. Maşın öyrənməsinin yalnız UEBA-ya aid olmadığı yuxarıda deyilib.
:::

### Tam araşdırma: LMS hesabından məlumat ixracına

Şərti araşdırma: ali@kampus.example hesabı üçün 02:10-da yeni cihazdan VPN girişi, 02:14-də həssas qovluğa müraciət, 02:18-də kütləvi endirmə, 02:25-də xarici xidmətə ötürmə siqnalı. Xəbərdarlıq avtomatik insident hökmü vermir. **L1** qaydanın versiyasını, xam qeydləri, vaxt çevrilməsini və hesab uyğunluğunu yoxlayır: iki hesab səhv birləşdirilibsə, qalan araşdırmanın əsası yoxdur. Soruşulur: vəzifə, cihazın idarə olunması, MFA nəticəsi, dəyişiklik sifarişi. IP ölkəsi yalnız köməkçi məlumatdır. MFA uğurlu olsa da, sessiya tokeninin oğurlanması və ya istifadəçinin aldadılaraq sorğunu təsdiqləməsi ehtimalı qalır; nəticə «MFA var, təhlükə yoxdur» ilə bağlanmır. Məlumatın həssaslığı və davam edən ötürmə səbəbindən iş **L2**-yə verilir.

L2 eyni hesabın son fəaliyyətini mənbələr üzrə toplayır: VPN-in daxili sessiya ünvanı 10.20.14.8, DB auditində istifadəçi identifikatoru hesabın IAM identifikatoru, proksidə eyni vaxtlı autentifikasiya qeydi ilə uyğun gəlir. NAT cədvəli hadisə vaxtı üzrə yoxlanır. Baza ixracı nəticə qeydi ilə təsdiqlənir; proksi tuneli ilə fayl ötürməsinin eyniliyi isə ayrıca sübut tələb edir.

| UTC vaxtı | Müşahidə | Mənbə | Çıxarılan nəticə |
| --- | --- | --- | --- |
| 02:10 | Yeni cihazdan uğurlu giriş | VPN və IAM | Sessiya mövcuddur |
| 02:14 | Həssas qovluq oxunub | Fayl auditi | Məlumat əldə edilib |
| 02:18 | İxrac tamamlanıb | DB auditi | İxrac faylı müəyyən edilib |
| 02:25 | Xarici xidmətə ötürmə | Proksi və DLP | DLP fayl izi uyğunluğunu göstərir |
| 02:29 | İstifadəçi fəaliyyəti inkar edir | Ayrı təsdiqlənmiş kanal | Hesabdan sui-istifadə ehtimalı güclənir |
| 02:32 | Sessiyalar ləğv edilib | IAM cavab auditi | Məhdudlaşdırma yoxlanmalıdır |

DLP-də ötürülən obyektin rəqəmsal izi ixracla uyğun gəlirsə, sızma fərziyyəsi güclənir; yalnız böyük bayt sayı olsaydı, «eyni fayl çıxarılıb» yazmaq olmazdı. Analitik təsdiqlənmiş faktı, fərziyyəni və çatışmayan sübutu ayrı cümlələrlə qeyd edir. İstifadəçi ilə əlaqə şübhəli poçt sessiyasından yox, əvvəlcədən tanınan kanaldan qurulur.

İnsident rəhbəri ziyanı azaltmaq üçün sessiyaların ləğvinə, riskli girişin məhdudlaşdırılmasına və lazım gələrsə cihazın təcridinə qərar verir. Əvvəl mövcud sessiya və audit məlumatları qorunur, amma sübut toplamaq davam edən sızmanı lüzumsuz uzatmır. Oğurlanmış parol dəyişdirilir, əlavə açarlar və qrup üzvlükləri yoxlanır; parol dəyişməsi bütün tokenləri avtomatik etibarsız etməyə bilər, sessiyanın ləğvi ayrıca təsdiqlənir.

Əhatə araşdırması eyni IP, cihaz və ixrac izinin başqa hesablarda olub-olmadığını axtarır. L3 hücum zəncirinin əvvəlindəki boşluğu və onu aşkar edəcək qaydanı qiymətləndirir. Bərpadan sonra hesabın fəaliyyəti izlənir. İş yalnız «hesab açıldı» ilə bağlanmır: icazəsiz giriş yolu bağlanmalı, təsirlənən məlumat müəyyənləşməli, cavab addımları yoxlanmalıdır.

### SOAR playbook-unun qurulması

SOAR iş axını giriş şərti, addımlar, qərar budaqları və geri qaytarma əməliyyatlarından ibarətdir. Başlanğıc hadisəsi həm korrelyasiya xəbərdarlığını, həm də təkil iş açarını daşıyır. İlk addımlar: avtomatik sübut toplamaq, aktivi zənginləşdirmək, bilet açmaq. Xarici reputasiya xidmətinə tələbə sənədi və ya tam URL göndərilmir; həssas parametrlər əvvəlcə çıxarılır.

| Addım | Əməl | Nəzarət |
| --- | --- | --- |
| Girişin yoxlanması | Qayda və hadisə açarını təsdiqlə | Eyni işi təkrar açma |
| Zənginləşdirmə | IAM, cihaz və dəyişiklik məlumatını al | Sorğu vaxtını və nəticəni saxla |
| Sübutların qorunması | Qeydləri heşlə və işə bağla | Giriş məhdudiyyəti qoy |
| Təsirin qiymətləndirilməsi | Aktiv sessiya və sızma varmı? | Məlumat çatmırsa analitikə ötür |
| Cavab qərarı | Sessiyanı kəs və ya hesabı məhdudlaşdır | Səlahiyyət və təsdiq tələb et |
| Nəticənin yoxlanması | Cavab API-si və faktiki girişi yoxla | Uğursuz addımı qeyd et |
| Bərpa | Müvəqqəti məhdudiyyəti geri götür | Səbəb və təsdiqi saxla |

API vaxt aşımı cavabın icra edilmədiyini sübut etmir; yenidən cəhd əvvəlki əməliyyatın statusunu yoxlamalıdır. Əməliyyat idempotent olmalıdır (idempotentlik): təkrarı əlavə ziyan yaratmır. Xidmət hesabını bloklamaq LMS-i dayandıra bilər; belə hesablar üçün ayrıca təsdiq yolu və alternativ məhdudlaşdırma seçilir. Playbook sınağında API nasazlığı, yanlış hesab uyğunluğu və analitikin əlçatan olmaması da yoxlanır.

NIST CSF 2.0-nın altı funksiyası **Govern, Identify, Protect, Detect, Respond** və **Recover**-dir. NIST SP 800-61 Rev. 3 insidentə cavabı bu çərçivədə təşkil edir: Govern qərar səlahiyyətini və siyasəti, Identify aktiv və risk kontekstini, Protect hazırlıq tədbirlərini əlaqələndirir; Detect, Respond və Recover aşkarlama, cavab və bərpanı əhatə edir. Əvvəlki nəşrin mərhələ sxemini Rev. 3-ün dəyişməz mərhələləri kimi təqdim etmək düzgün deyil.

## Effektivliyin ölçülməsi və tutum

| Göstərici | Məna | Məqsəd |
| --- | --- | --- |
| MTTD | Hücumun başlanğıcından aşkarlanmaya qədər orta vaxt | Azalmalıdır |
| MTTR | Aşkarlanmadan aradan qaldırılmaya qədər orta vaxt | Azalmalıdır |
| Dəqiqlik (precision) | TP / (TP + FP) | Artmalıdır |
| Tamlıq (recall) | TP / (TP + FN) | Artmalıdır |
| ATT&CK örtüyü | Aşkarlanan texnikaların payı | Artmalıdır |
| Mənbə sağlamlığı | Vaxtında gələn mənbələrin faizi | 100%-ə yaxın |

Konspekt MTTD-ni "orta aşkarlama vaxtı", MTTR-i "orta cavab/bərpa vaxtı" kimi verir və yanlış həyəcan faizi, kritik mənbələrin əhatəsi, gecikən və itən logları da ölçülər sırasına əlavə edir.

**Şərti hesablama.** Ay ərzində 200 xəbərdarlıq gəlib, araşdırma 30-unun həqiqi olduğunu göstərib. Dəqiqlik 30 / 200 = 15%. Xəbərdarlıqların 85%-i yanlış müsbətdir. Analitik vaxtının hansı hissəsinin onlara sərf olunduğu araşdırma müddətlərinin ayrıca ölçülməsi ilə müəyyən edilir. «**Xəbərdarlıq yorğunluğu**» buradan başlayır: analitik xəbərdarlıqlara diqqət göstərməməyə öyrəşir və real hücum nəzərdən qaçır. Qaydaları tənzimləməklə dəqiqliyi artırmaq olar, amma tamlıq aşağı düşə bilər; bu iki göstərici arasında balans qurulur. Tamlığı ölçmək çətindir, çünki aşkarlanmayan hücumların sayı bilinmir. Ona görə idarə olunan testlər (**purple team**, **Atomic Red Team**) aparılır.

Tutum **EPS**-lə (*events per second*) planlaşdırılır. Şərti universitetdə orta 2000 EPS və orta qeyd ölçüsü 500 bayt olarsa:

```text
2000 hadisə/s x 500 bayt = 1 MB/s
1 MB/s x 86 400 s = 86,4 GB/gün
86,4 GB x 90 gün = təxminən 7,8 TB (sıxılmadan)
```

Hesabda indeks və replika əlavəsi yoxdur; bunlar saxlama həcmini artırır, yekun tutum sıxılma əmsalından da asılıdır. Pik yük ortadan bir neçə dəfə yüksək ola bilər, buna görə toplama qatı ehtiyatla planlaşdırılır. Ticari SIEM çox vaxt həcmə görə qiymət aldığından mənbə seçimi büdcəyə təsir edir.

### Düsturların düzgün şərhi

Şərti sınaqda 100 xəbərdarlığın 20-si TP, 80-i FP, buraxılmış hücumların sayı (FN) 5-dir. Dəqiqlik 20 / 100 = 20%, tamlıq 20 / (20 + 5) = 20 / 25 = 80%-dir. Xəbərdarlıqların yanlış payı 80%-dir (FP / (TP + FP)). Yanlış müsbət nisbəti (**FPR**) isə FP / (FP + TN) düsturu ilə hesablanır. TN məlum deyilsə, FPR hesablana bilməz. Şərti olaraq TN = 920 olduqda FPR = 80 / 1 000 = 8%-dir: əvvəlki 80% ilə fərqli məxrəcə malik göstəricidir. Nəticə: qayda hücumların çoxunu tutur, amma xəbərdarlıqların 80%-i boş həyəcandır; sazlama lazımdır.

MTTD üçün başlanğıc və aşkarlama meyarı sabit seçilir. Şərti üç insidentdə gecikmələr 8, 12 və 25 dəqiqədirsə, MTTD = 45 / 3 = 15 dəqiqədir. Aşkarlanmadan aradan qaldırılmaya qədər müddətlər 30, 50 və 100 dəqiqədirsə, burada seçilən təriflə MTTR = 180 / 3 = 60 dəqiqədir. Başqa komandada MTTR ilk cavaba qədər vaxtı bildirə bilər; hesabatda tərif açıq yazılmalıdır. Aşkarlanma anının sistem xəbərdarlığı, yoxsa insan təsdiqi olduğu da dəqiqləşdirilir.

Orta vaxt gecikmiş kritik işi gizlədə bilər; median və yuxarı persentillər prioritet səviyyəsinə görə ayrıca göstərilir. Şərti olaraq iyirmi kritik mənbədən on səkkizi qoşulubsa, mənbə əhatəsi 90%-dir; qoşulanlardan yalnız on altısı vaxtında və düzgün sahələrlə gəlirsə, işlək əhatə 16 / 20 = 80%-dir. Təkcə konnektorun yaşıl statusuna baxmaq bu fərqi gizlədir.

:::tip FPR və yanlış pay
**FPR = FP / (FP + TN)** (bütün əsl-mənfi hadisələrin neçə faizi xəbərdarlıq verdi); **yanlış pay = FP / (TP + FP)** (xəbərdarlıqların neçə faizi boşdur). Məxrəclər fərqlidir; qarışdırma.
:::

### İndeks, replika və ehtiyat payı ilə tutum

Əvvəlki 86,4 GB/gün xam giriş nümunəsini davam etdirək (bütün əmsallar şərtidir). Xam həcmin sıxılmadan sonra 0,5 hissəsi qalır, indeks isə xam həcmin 0,3 hissəsini tutur. Əsas saxlanma 86,4 × (0,5 + 0,3) = 69,12 GB/gündür. Bir əsas və bir replika üçün ümumi nüsxə sayı ikidir: 138,24 GB/gün. 90 gün üçün 12 441,6 GB alınır. Bunun üzərinə 25% əməliyyat ehtiyatı ayrılarsa, planlanan tutum 15 552 GB, yəni təxminən 15,55 TB-dır; vahidlər onluq sistemdədir.

Replika ayrıca ehtiyat nüsxə deyil: səhv silinmə ona da yayıla bilər. Snapshot, dəyişməz arxiv və bərpa sınağı ayrıca planlaşdırılır. İsti və ilıq qatda indeks xərci ilə soyuq obyekt arxivinin xərci eyni deyil; bu nümunə bütün 90 gün üçün sadələşdirilmiş indeksli saxlama modelidir.

Şərti pik yük 8 000 EPS olarsa, 500 baytlıq qeydlər saniyədə 4 MB xam axın yaradır. Buraya TLS, nəqliyyat və növbə əlavələri daxil deyil. Tutum qəbul sınağı orta gündən başqa qeydiyyat və imtahan pikini də əhatə etməlidir.

## Tipik səhvlər

- **Məqsədsiz toplama:** hər şey yazılır, heç bir aşkarlama sualı müəyyən edilmir.
- **Saatların sinxron olmaması:** hadisələr səhv sırada görünür.
- **Yanlış ayrışdırma:** mənbə IP təyinat kimi yazılır və korrelyasiya səhv işləyir.
- **SIEM-də hesabların qorunmaması:** loglar parol və şəxsi məlumat ehtiva edə bilər, onlara giriş məhdudlaşdırılmalıdır.
- **Susan mənbələrə nəzarətin olmaması.**
- **Hazır qaydaların tənzimlənmədən işə salınması.**
- **Log silinməsinə qarşı müdafiənin olmaması:** mənbələr dərhal göndərməlidir, SIEM-də dəyişməzlik olmalıdır.

## Məxfilik, etika və SIEM-in özünün qorunması

UEBA təhlükəsizlik məqsədilə davranış məlumatı işləyir. Bu məlumat əməkdaşın məhsuldarlığını, siyasi baxışını və ya şəxsi niyyətini ölçmək üçün etibarlı əsas deyil. Davranış balını intizam qərarına avtomatik çevirmək texniki modelin sərhədini aşır: şəxsə aid qərar faktların ayrıca yoxlanmasına və səlahiyyətli insanın qiymətləndirməsinə əsaslanmalıdır.

Toplama məqsədi, baxılan sistemlər, istifadə edilən sahələr və saxlanma müddəti daxili siyasətdə aydın göstərilir. Autentifikasiya üçün parolun özünü toplamaq lazım deyil. LMS sorğusunun tam mətnində qiymət, tələbə identifikatoru və token ola bilər; məqsəd yalnız giriş tezliyidirsə, artıq məzmun çıxarılır. DLP xəbərdarlığına tam tələbə siyahısını əlavə etmək əvəzinə kateqoriya, uyğunluq sayı və qorunan sübut istinadı kifayət edə bilər.

**Psevdonimləşdirmə** şəxs identifikatorunu başqa işarə ilə əvəz edir, uyğunluq cədvəli isə ayrıca qorunur. Sadə heş anonimlik zəmanəti vermir: məhdud tələbə nömrələri siyahısını heşləyib müqayisə etmək mümkündür. Məxfi açarla **HMAC** istifadə etmək belə lüğət müqayisəsini çətinləşdirə bilər, amma əlaqələndirilən davranış yenə həssas məlumatdır. Şəxsiyyəti açmaq üçün əsas, icazə və audit izi tələb olunur.

SIEM idarəetmə hesabları MFA və ən az səlahiyyətlə qorunur. Qayda yazan, arxiv silən və sübut ixrac edən hüquqlar ayrılır. Analitikin həssas tələbə qeydlərinə baxması da audit olunur; həmin audit ayrıca qorunan yerə ötürülür. Bulud API konnektoruna yalnız oxuma səlahiyyəti kifayətdirsə, resurs dəyişdirmək hüququ verilmir. Konnektor sirləri loga yazılmır, dövri dəyişdirilir.

Log məzmunu etibarlı giriş sayılmır. Hücumçu istifadəçi adı və URL daxilinə sətirsonu, idarəetmə simvolu və ya ekranı çaşdıran mətn yaza bilər. Strukturlaşdırılmış qeyd, düzgün qaçışlama və xam mətnin təhlükəsiz göstərilməsi saxta əlavə sətirlərin həqiqi hadisə kimi oxunmasını azaldır. SIEM özü əlçatmaz olanda kolektorların nə qədər işləyəcəyi və komandanın hansı alternativ kanaldan xəbər alacağı bərpa planında yazılır.

## Praktiki iş: hesabın mümkün ələ keçirilməsi

Təlim məlumatı sintetikdir, vaxt və saylar şərtidir. nigar@kampus.example hesabının adi profili: iş günləri kampusdan, idarə olunan cihazla LMS və öz fənn qovluqlarına giriş. 10:00-dakı normal giriş sonrakı hərəkətlərin hamısını qanuni saymağa əsas vermir; eyni hesabın paralel sessiyaları ola bilər.

| UTC vaxtı | Hadisə | İlkin nəticə |
| --- | --- | --- |
| 10:00 | Tanınmış cihazdan normal giriş | Uğurlu |
| 10:05 | Eyni hesaba yeddi uğursuz cəhd | Uğursuz |
| 10:07 | Yeni cihazdan giriş | Uğurlu |
| 10:10 | Kritik fayllara qeyri-adi müraciət | Qeydə alınıb |
| 10:12 | Qeyri-adi həcmdə fayl endirmə | Qeydə alınıb |

Magistrant əvvəlcə hadisələri vahid sxemə çevirir, hadisə vaxtı ilə qəbul vaxtını ayırır; sonra hesabın dəyişməz identifikatorunu, mənbə IP-lərini və cihaz sessiyalarını uyğunlaşdırır. MFA nəticəsi, faylın həssaslığı və ötürmə istiqaməti verilməyibsə, onları fakt kimi yazmır. «Endirmə» universitetdən istifadəçiyə axındır; xarici xidmətə yükləmə ilə eyni olduğu fərz edilmir.

Bir hədd qaydası və bir ardıcıllıq qaydası hazırlanır. Şərti hədd: «beş dəqiqədə ən azı yeddi uğursuz cəhd». Ardıcıllıq: həmin cəhdlərdən sonra beş dəqiqədə uğurlu giriş, sonra həssas resurs müraciəti. Əvvəlki on cəhd həddi bu yeddi cəhdi tutmaz. Tələbə həddi əsaslandırmalı və bu kiçik nümunənin istehsal həddini öyrənmək üçün kifayət etmədiyini göstərməlidir.

UEBA təhlilində şəxsin tarixçəsi, oxşar rol qrupu və akademik təqvim müqayisə edilir. Ən azı üç alternativ izah yazılır: köhnə parollu tətbiq, cihazın dəyişdirilməsi və təsdiqlənmiş arxiv işi. Yeni cihaz naməlumluğu ilə fayl həcmində artım eyni siqnal deyil, amma eyni əsas hadisənin təkrarları ayrıca sayılmır. Mümkün cavab: əlavə autentifikasiya, sessiyanın məhdudlaşdırılması və ya təsdiqlənmiş təhlükədə bloklama.

Təhvil verilən iş: zaman xətti, iki qaydanın məntiqi, çatışmayan məlumat siyahısı və əsaslandırılmış analitik rəy. Rəydə təsdiqlənmiş müşahidə ilə fərziyyə ayrılır. Nümunə: «Hesabın mümkün ələ keçirilməsi araşdırılmalıdır; yeni sessiyanın MFA və cihaz məlumatı çatışmır. Məlumat ixracı təsdiqlənib, xarici sızma isə təqdim edilən qeydlərlə təsdiqlənmir».

| Meyar | Bal |
| --- | --- |
| Məlumatların düzgün hazırlanması | 20 |
| Korrelyasiya məntiqinin əsaslandırılması | 25 |
| Davranış profilinin və anomaliyanın təhlili | 20 |
| Alternativ izahların nəzərə alınması | 15 |
| Reaksiya qərarı və analitik rəy | 20 |
| Cəmi | 100 |
