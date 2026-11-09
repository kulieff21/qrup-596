+++
title = "Tələ sistemləri, proksi-serverlər və virtual özəl şəbəkələr (VPN)"
unit = "uzun"
order = 7
summary = "Tam mühazirə: tələ sistemləri (honeypot), düz və tərs proksi, VPN, IPsec, WireGuard, köhnəlmiş protokollar, sərtləşdirmə və ZTNA; bütün cədvəllər, rəqəmlər, hadisələr və situasiyalar."
updated = 2026-11-09

[[source]]
title = "Mühazirə 7: Tələ sistemləri, proksi-serverlər və virtual özəl şəbəkələr (VPN)"
note = "Elmar Cabbarov, 2026–2027"
+++

Bu üç texnologiya şəbəkənin fərqli nöqtələrində işləyir. **Tələ sistemi** hücumçunu aldadıb izləyir, **proksi** trafikin arasına vasitəçi qoyur, **VPN** isə etibarsız şəbəkə üzərindən qorunan kanal qurur. Mövzudan sonra bacarmalısan: tələnin az yanlış həyəcanını və təhlükəsiz yerləşdirilməsini izah etmək; düz və tərs proksini, proksi ilə NAT-ı ayırmaq; VPN-in nəyi qoruduğunu və qorumadığını demək, IPsec rejimlərini göstərmək, işlək və köhnəlmiş protokolları seçmək. Universitet topologiyası, ünvanlar, VLAN nömrələri və saylar şərti tədris nümunəsidir.

## I hissə. Tələ sistemləri

### Tələ sistemi nədir

Tələ sistemi (honeypot, hərfən “bal küpü”) hücumçunu cəlb etmək, hərəkətlərini qeydə almaq və öyrənmək üçün qəsdən qurulmuş saxta resursdur. Lens Spitsner (Lance Spitzner) 2002-ci il kitabında honeypot-u “dəyəri icazəsiz istifadədən gələn informasiya resursu” kimi təsvir edir: adi serverin dəyəri gördüyü işdədir, tələnin dəyəri isə kiminsə ona toxunmasındadır.

Tələnin heç bir iş funksiyası yoxdur, onu nə tələbə, nə müəllim, nə tətbiq işlətməlidir. Ona görə tələyə gələn istənilən bağlantı ən azı şübhəlidir. IDS milyonlarla normal paketin içindən zərərlini seçməyə çalışır və tez-tez yanılır; tələdə isə “normal trafik” anlayışı yoxdur. Yanlış həyəcanın azlığı buradan gəlir.

:::note Sadə dillə
Mağaza vitrininə izləmə cihazı olan saxta qızıl saat qoyulub. Onu götürən həm özünü ifşa edir, həm hansı yolla girdiyini və hara getdiyini göstərir. Real saatlar seyfdə qalır. (Mühazirənin versiyası: kitabxananın vitrinində izləyici cihazlı saxta nadir kitab; əsl kitablar seyfdədir.)
:::

Tələyə üç vəzifə verilir: hücumu **erkən aşkar etmək**, hücumçunun **üsullarını öyrənmək**, onun vaxtını **real sistemlərdən uzaqda sərf etdirmək**. Tələ hücumun qarşısını almır: firewall, yamaq və giriş nəzarəti olmayan şəbəkədə yalnız hücumu izləməyə imkan verir.

| Meyar | Firewall | IDS/IPS | Tələ sistemi |
| --- | --- | --- | --- |
| Əsas vəzifə | Trafiki qaydalara görə buraxır/bloklayır | Hücum əlamətlərini tapır; IPS həm də dayandırır | Hücumçunu cəlb edir, davranışını qeydə alır |
| Baxdığı trafik | Sərhəddən keçən hamısı | Sensorun gördüyü hamısı | Yalnız tələyə gələn |
| Yanlış həyəcan | Tətbiq olunmur | Çox ola bilər | Çox az |
| Məlumat həcmi | Çox böyük | Çox böyük | Kiçik, amma dəyərli |
| Naməlum hücumu görmə | Qaydadan asılıdır | İmzalı IDS üçün çətin | Davranış qeydə alındığı üçün görə bilir |
| Zəif cəhəti | İcazəli portdan keçən hücumu görmür | Şifrəli trafikdə məhduddur | Ona gəlməyən hücumdan xəbəri yoxdur |

### Yaranma tarixi

- **1986:** Lawrence Berkeley Laboratoriyasının astronomu və sistem administratoru Klifford Stoll hesabat sistemində 75 sentlik uyğunsuzluğu araşdırarkən icazəsiz girən adamı tapdı; onu xəttdə saxlamaq üçün saxta hərbi layihə sənədləri yaratdı. 1989-da “The Cuckoo's Egg” kitabında təsvir etdi.
- **1991:** AT&T Bell Labs-da Bill Çesvik (Bill Cheswick) saxta sistem quraraq hücumçunu bir neçə ay müşahidə etdi. “An Evening with Berferd” məqaləsi tələ yanaşmasının ilk akademik təsvirlərindən sayılır.
- **1990-cı illərin sonu:** Fred Koen (Fred Cohen) açıq yayımlanan Deception Toolkit alətini hazırladı.
- **1999:** tədqiqatçı könüllülər The Honeynet Project təşəbbüsünü yaratdılar; “Know Your Enemy” məqalələr silsiləsi və “honeynet” termini ondan yayılıb.

### Tələ sistemlərinin təsnifatı

### Məqsədə görə

- **İstehsalat tələsi (production honeypot):** təşkilatın öz şəbəkəsindədir, məqsəd daxilə keçmiş hücumçunu tez görməkdir; sadədir, az resurs tələb edir. Nümunə: universitetin daxili şəbəkəsində saxta “maliyyə-arxiv” fayl serveri.
- **Tədqiqat tələsi (research honeypot):** yeni hücum üsullarını, zərərli proqram nümunələrini, botnet davranışını öyrənmək üçündür; universitetlər, CERT komandaları, antivirus şirkətləri işlədir. Çox məlumat toplayır, amma qurulması və nəzarəti çətindir.

### Qarşılıqlı əlaqə səviyyəsinə görə

İmtahanda ən çox soruşulan bölgüdür. Tələ hücumçuya nə qədər çox imkan verirsə, bir o qədər çox məlumat toplayır və bir o qədər təhlükəli olur.

| Səviyyə | Necə işləyir | Toplanan məlumat | Risk | Nümunə |
| --- | --- | --- | --- | --- |
| Aşağı (low-interaction) | Yalnız bir neçə xidmət/protokol təqlid olunur; real ƏS açılmır | Az: IP, port, giriş cəhdləri, bəzən zərərli fayl | Aşağı | Honeyd, Dionaea |
| Orta (medium-interaction) | İnandırıcı təqlid: hücumçu saxta fayl sistemində əmr yazır, real ƏS-də icra olunmur | Orta: daxil edilən əmrlər, endirilən fayllar | Orta | Cowrie (shell rejimi) |
| Yüksək (high-interaction) | Real ƏS və real xidmətlər | Çox: bütün davranış, yeni zəifliklərdən istifadə | Yüksək | Real Linux VM; Cowrie (proxy rejimi) arxasında real sistem |

Aşağı səviyyəli tələni bir server dəqiqələrə qaldırır; real ƏS interfeysi verməməsi riski azaldır. Lakin tələ proqramındakı və ya onu işlədən mühitdəki zəifliklərlə sistem ələ keçirilə bilər, ona görə izolyasiya və yeniləmə yenə vacibdir. Yüksək səviyyəli tələdə hücumçu real kök hüququ qazana bilər; nəzarətsiz buraxmaq ona növbəti hücumlar üçün hazır baza verməkdir.

### Rolu və hədəfinə görə

- **Server tələsi** gələn hücumu gözləyir (SSH, veb, verilənlər bazası tələləri).
- **Müştəri tələsi (client honeypot)** özü zərərli saytları gəzir və brauzerə yönəlmiş hücumları aşkar edir.
- **Xüsusi tələlər:** Conpot sənaye idarəetmə sistemlərini (ICS/SCADA), Dionaea isə zərərli proqramların yayıldığı SMB, HTTP, FTP protokollarını təqlid edir.

Tələ fiziki və ya virtual maşında işləyə bilər; virtual tələni bir əmrlə təmiz vəziyyətə qaytarmaq olur, ona görə demək olar ki, hamısı virtual və ya konteynerdədir. Mənfi tərəf: təcrübəli hücumçu virtuallaşdırma izlərini görüb sistemi şübhəli sayır.

### Honeynet, honeytoken və aldatma texnologiyası

**Honeynet** bir neçə tələdən ibarət bütöv saxta şəbəkədir (iş stansiyası, server, domen nəzarətçisi təqlidi). Tək tələ yalnız həmin resurs üzərində girişdən sonrakı fəaliyyəti göstərir; honeynet isə tələlər arasında hərəkəti (lateral movement), hansı sistemin birinci axtarıldığını və çoxhostlu hücum ardıcıllığını göstərir.

**Honeytoken** sistem deyil, məlumat parçasıdır: heç kimin işlətməməli olduğu saxta istifadəçi hesabı, “parollar.xlsx” faylı, bazadakı saxta tələbə sətri, kodda qalmış kimi görünən saxta API açarı. İstifadə olunan kimi həyəcan siqnalı gəlir. Thinkst şirkətinin pulsuz Canarytokens xidməti açılanda xəbər verən Word sənədləri, keçidlər və saxta AWS açarları yaradır.

:::example
Tələbə bazasına “Məmmədov Tural Sənan” adlı saxta tələbə sətri əlavə edilir, poçt ünvanı yalnız təhlükəsizlik komandasına gedir. O ünvana məktub gəlirsə, bazanın sızdığı və ya icazəsiz ixrac edildiyi dərhal bəlli olur; heç bir server tələsi bu daxili sızmanı göstərə bilməzdi. Məhdudiyyət: honeytoken-in xəbər verməsi kənar əlaqədən asılı ola bilər; hücumçu bu əlaqəni bloklayırsa, səssizlik faylın açılmadığını sübut etmir.
:::

**Aldatma texnologiyası (deception)** tələləri, honeytoken-ləri və saxta kimlik məlumatlarını şəbəkəyə kütləvi və avtomatik yayır. MITRE Engage çərçivəsi bu üsulları sistemləşdirib: hücumçunu aşkar etmək, ona saxta mühit göstərmək, davranışını öyrənmək. Məsələn, hücumçunun yaddaşdan parol oğurladığı iş stansiyalarında saxta administrator kimlik məlumatı saxlanır; həmin hesabla ilk giriş cəhdi hücumu dərhal göstərir.

### Şəbəkədə yerləşdirmə

| Yer | Nəyi göstərir | Üstünlüyü | Çatışmazlığı |
| --- | --- | --- | --- |
| Xarici firewall-dan kənar (İnternetə açıq) | Ümumi skan və kütləvi hücum mənzərəsi | Çox məlumat, real şəbəkəyə toxunmur | Həyəcanların çoxu adi “internet səs-küyüdür” |
| DMZ yaxınlığı, ayrıca seqment | Təşkilatın açıq xidmətlərinə hücumlar | Xidmətlərə yönəlmiş hücumları göstərir | Real DMZ serverlərindən ciddi ayrılmalıdır |
| Daxili şəbəkə | Daxilə keçmiş hücumçu, yoluxmuş cihaz, daxili pozucu | Hər bağlantı demək olar ki, insidentdir | Kənardan gələn hücumu görmür |

Təşkilat üçün ən çox fayda daxili şəbəkədədir: İnternetə açıq tələ gündə minlərlə skan görür, daxili tələyə bağlantı gəlirsə, kimsə şəbəkəni skan edir və ya orada olmamalı sistemi axtarır.

:::figure
src = "m07-1.png"
alt = "Hücumçu İnternetdən firewall-a gəlir; firewall DMZ-dəki real portala (TCP 443), daxili şəbəkəyə və ayrıca tələ seqmentinə (VLAN 99) yol verir. Tələ seqmentindən çıxış bağlıdır, yalnız log serverinə log gedir."
caption = "Tələ seqmentinin universitet şəbəkəsində yeri (şərti nümunə): tələdən yalnız log serverinə yol açıqdır."
wide = true
:::

:::tip Yadda saxla: tələni təhlükəsiz yerləşdirmək
Beş qayda:
- Tələ ayrıca, izolyasiya olunmuş seqmentdə (VLAN) qurulur; real serverlərlə eyni alt şəbəkədə olmaz.
- Tələdən çıxan trafik firewall ilə kəsilir; əks halda ələ keçirilmiş tələ sıçrayış nöqtəsinə (pivot) çevrilir.
- Tələdə real məlumat, parol, açar saxlanmır.
- Loglar dərhal kənar serverə göndərilir, çünki hücumçu onları tələnin özündə silə bilər.
- Yüksək səviyyəli tələ snapshot-dan bərpa olunan virtual maşında işləyir və vaxtaşırı təmizlənir.
:::

### Məlumatın toplanması və SIEM ilə əlaqə

Honeynet Layihəsi tələ arxitekturasına üç tələb qoyur:

| Tələb | Mənası |
| --- | --- |
| Məlumatın idarəsi (data control) | Ələ keçirilmiş tələnin başqalarına ziyan vurmasının qarşısını alır |
| Məlumatın tutulması (data capture) | Hücumçunun etdiyi hər şeyi, o xəbər tutmadan qeydə alır |
| Məlumatın yığılması (data collection) | Bir neçə tələnin qeydlərini mərkəzdə birləşdirir |

Tələ hadisələri SIEM-ə göndərilir. Tələ SIEM üçün ən etibarlı mənbələrdən biridir: bir qayda kifayətdir, “tələyə bağlantı gəlibsə, xəbərdarlıq yarat”. Cowrie SSH tələsinin JSON qeydləri (IP və parollar şərti nümunədir):

```
{"eventid":"cowrie.login.failed","src_ip":"198.51.100.23","username":"root","password":"123456","session":"a1b2c3d4"}
{"eventid":"cowrie.login.success","src_ip":"198.51.100.23","username":"root","password":"admin2024","session":"a1b2c3d4"}
{"eventid":"cowrie.command.input","input":"uname -a; cat /proc/cpuinfo","session":"a1b2c3d4"}
{"eventid":"cowrie.session.file_download","url":"http://198.51.100.77/x.sh","shasum":"e3b0c4...","session":"a1b2c3d4"}
```

Bu dörd sətirdən hücumçunun IP-si, parol lüğəti, sistemi tanımaq üçün yazdığı əmrlər, zərərli skriptin ünvanı və faylın heş dəyəri bəlli olur. Bunlar kompromitasiya indikatorlarıdır (IoC); firewall-a, EDR-ə və təhdid kəşfiyyatı platformasına ötürülür. Əmrlər MITRE ATT&CK texnikalarına bağlanır: `uname -a` sistem məlumatının toplanması (T1082), parol sınaqları kobud güc hücumudur (T1110).

Hücumçu tələdə kök hüququ alırsa, tələnin öz qeydləri etibarlı sayılmır. Ona görə şəbəkə və hipervizor səviyyəsində müstəqil trafik yazısı aparılır, idarəetmə girişi ayrı kanaldan olur. Tutulan zərərli faylların heşi götürülür, onlar parollu arxivdə və təcrid olunmuş mühitdə saxlanılır. Qeydlər hüquqi iş üçün lazım ola bilərsə, sinxron vaxt və sübutun ötürülmə zənciri (chain of custody) qorunur.

Toplanan məlumat hücumçunun bu tələyə qarşı etdiyini göstərir, təşkilatın real zəifliklərini yox: “ən çox bu protokola hücum olunur” kimi ümumi nəticə çıxar, amma “serverlərimiz təhlükəsizdir” nəticəsi çıxmaz.

### Tələ və Cyber Kill Chain

| Mərhələ | Tələdə nə görünür | Dəyəri |
| --- | --- | --- |
| Kəşfiyyat | Port skanı, banner sorğuları, parol sınaqları | Yüksək |
| Silahlanma | Hücumçunun öz kompüterində baş verir | Yoxdur |
| Çatdırılma | Zərərli faylın yüklənməsi, endirmə keçidi | Yüksək |
| İstismar | Exploit, əmr yeridilməsi | Yüksək, xüsusən yeni zəifliklərdə |
| Quraşdırma | Skriptin yazılması, cron tapşırığı, SSH açarı əlavəsi | Orta və yüksək səviyyəli tələdə |
| İdarəetmə (C2) | Xarici serverə qoşulma cəhdi: firewall kəsir, cəhd qeydə düşür | Yüksək: C2 ünvanı öyrənilir |
| Hədəfə çatma | Daxili skan, parol axtarışı, məlumat toplama | Daxili tələdə çox yüksək |

### Tələnin növünü necə seçmək

Seçim məqsəddən başlayır; komandanın gücü, vaxt və risk həddi nəzərə alınır.

| Məqsəd | Uyğun seçim | Səviyyə |
| --- | --- | --- |
| Daxili skanı erkən görmək | OpenCanary, saxta fayl serveri | Aşağı |
| SSH parol lüğətlərini və botları öyrənmək | Cowrie, İnternetə açıq, ayrıca ünvanda | Orta |
| Yeni zərərli proqram nümunələri toplamaq | Dionaea, izolyasiya olunmuş sandbox analizi ilə | Aşağı |
| Sənaye avadanlığına maraq göstərənləri izləmək | Conpot | Aşağı və orta |
| Hücumçunun tam iş metodunu öyrənmək | Real ƏS, honeynet, ciddi çıxış nəzarəti | Yüksək |
| Bazanın/faylların sızmasını aşkar etmək | Honeytoken | Sistem tələb etmir |

Kiçik İT komandası üçün tədqiqat səviyyəli honeynet çox vaxt düzgün seçim deyil: hər gün izlənilməyən yüksək səviyyəli tələ faydadan çox risk gətirir. Bir neçə saxta xidmət və yaxşı yerləşdirilmiş honeytoken-lər daha sürətli nəticə verir.

### Nəticələri necə ölçmək

Tələnin faydası xəbərdarlıq sayı ilə ölçülmür; daxili tələdə həftədə sıfır xəbərdarlıq yaxşı işarə ola bilər. Əvəzinə test edilir: pentest və ya daxili yoxlama tələyə toxunanda xəbərdarlıq SOC-a neçə dəqiqəyə çatır, analitik mənbə cihazı neçə dəqiqəyə tapır. İnternetə açıq tələlərdə unikal mənbə sayı, ən çox sınanan parollar, yeni fayl heşləri və hədəflənən protokollar statistikası aparılır.

### Alətlər

| Alət | Sinif | Qısa izah |
| --- | --- | --- |
| Cowrie | Orta və yüksək | SSH və Telnet tələsi. Shell rejimində UNIX-i Python-da təqlid edir; proxy rejimində bağlantını real sistemə ötürüb müşahidə edir |
| Dionaea | Aşağı | Zərərli proqramları tutmaq üçün SMB, HTTP, FTP və s. təqlid edir |
| Honeyd | Aşağı | Niels Provos-un virtual hostlar çərçivəsi; bir kompüterdə minlərlə saxta IP və xidmət göstərir |
| Conpot | Sənaye tələsi | PLC və SCADA avadanlığını, Modbus və S7 protokollarını təqlid edir |
| OpenCanary | Daxili şəbəkə tələsi | Yüngül çoxxidmətli tələ; bağlantı olanda bildiriş göndərir |
| T-Pot | Platforma | Deutsche Telekom layihəsi; iyirmidən çox tələni konteynerlərdə işlədir, nəticələri Elastic Stack panellərində göstərir |
| Canarytokens | Honeytoken xidməti | Açılanda/işlədiləndə xəbər verən saxta fayl, keçid və açarlar yaradır |

### Risklər, məhdudiyyətlər və hüquqi məsələlər

1. **Dar görmə sahəsi.** Tələ yalnız ona gələn hücumu görür; hücumçu birbaşa LMS serverinə gedirsə, susur. O, IDS və SIEM-in yerini tutmur, onları tamamlayır.
2. **Tanınma.** Təcrübəli hücumçu standart SSH banner-indən, qeyri-təbii cavab vaxtından, virtual maşın izlərindən və ya həmişə eyni fayl sistemindən tələni tanıya bilər. Shodan kimi axtarış sistemləri İnternetdəki tələlərin bir hissəsini etiketləyir. Tələ standart parametrlərlə qurulmur: host adı, fayl sistemi, açıq xidmətlər real serverlərə oxşadılır.
3. **Ələ keçirilmə və pivot.** Yaxşı izolyasiya olunmayan yüksək səviyyəli tələdən hücumçu real sistemlərə keçə və ya başqa təşkilatlara hücum edə bilər; hücum universitetin IP ünvanından gəlmiş kimi görünəcək, məsuliyyət məsələsi yaranacaq.
4. **Hüquqi tərəf.** Tələ passiv gözləməlidir; insanı cinayətə təhrik etmək (forumda “açıq verilənlər bazası” reklamı) hüquqi problem yarada bilər. Hücumçunun IP-si və daxil etdiyi məlumat şəxsi məlumat sayıla bildiyi üçün “Fərdi məlumatlar haqqında” Azərbaycan Respublikası Qanununa və daxili siyasətə uyğun saxlanmalıdır; tələni işə salmazdan əvvəl hüquq xidməti ilə razılaşdırılır. Əks hücum (hack-back), yəni hücumçunun sisteminə geri “girmək” icazəsiz girişdir və yeni problem gətirir.

:::warning
Honeypot qarşısını alma vasitəsi deyil, aşkarlama və öyrənmə vasitəsidir. “Tələ qurduq, deməli, qorunuruq” fikri səhvdir; tələ əsas nəzarət vasitələri artıq işləyən şəbəkəyə əlavə olunur.
:::

### Universitet şəbəkəsində tələnin qurulması

İT şöbəsi daxili hərəkəti erkən görmək istəyir. Addımlar:

:::steps Universitetdə tələ qurma ardıcıllığı
[[step]]
title = "Məqsəd"
body = "Daxili şəbəkədə skanı və parol sınaqlarını aşkar etmək. Bu istehsalat tələsidir; aşağı və ya orta səviyyə kifayətdir."

[[step]]
title = "Yerləşdirmə və adlar"
body = "Tələbə kompüter laboratoriyası, inzibati şəbəkə və server zonası üçün üç tələ, hər biri öz zonasında görünən, amma ayrıca nəzarət olunan ünvanda. İnandırıcı adlar verilir (fin-arxiv01, lms-backup), açıq xidmətlər zonaya uyğun seçilir: SMB, SSH, RDP."

[[step]]
title = "Firewall"
body = "Tələdən bütün çıxış qadağandır; yalnız log serverinə TCP 6514 (TLS üzərindən syslog) açıqdır."

[[step]]
title = "SIEM qaydası və istisnalar"
body = "Tələyə istənilən uğurlu və ya uğursuz bağlantı yüksək dərəcəli xəbərdarlıq yaradır. Zəiflik skanerlərinin və inventar alətlərinin IP ünvanları istisna siyahısına salınır, yoxsa hər həftə eyni yanlış həyəcan gələcək."

[[step]]
title = "Reaksiya qaydası"
body = "Tələdə qeydə alınan IP hansı cihazdır, kimə məxsusdur, cihaz şəbəkədən necə ayrılır: əvvəlcədən yazılır."

[[step]]
title = "Rüblük yoxlama"
body = "Pentest komandası tələyə toxunur, xəbərdarlığın neçə dəqiqəyə gəldiyi ölçülür."
:::

## II hissə. Proksi-serverlər: düz (forward) və tərs (reverse) proksi

### Proksi-server nədir

Proksi-server müştəri ilə server arasında duran vasitəçidir. Müştəri sorğunu birbaşa serverə deyil, proksiyə göndərir; proksi onu öz adından serverə ötürür, cavabı alıb müştəriyə qaytarır. Əsas məqam bağlantıların sayıdır: müştəri–proksi arasında bir, proksi–server arasında tamamilə ayrı ikinci TCP bağlantısı. Bu, TCP əsaslı HTTP üçün belədir; UDP və QUIC proksiləməsində də tərəflər ayrı rabitə əlaqələri qurur, amma TCP bağlantısından danışmaq olmur. Proksi iki əlaqənin ortasında dayandığı üçün tətbiq səviyyəsində məlumatı oxuya, dəyişdirə, keşləyə və qadağan edə bilir.

HTTP standartı (RFC 9110) vasitəçilərin üç formasını göstərir:

| Forma | Mənası |
| --- | --- |
| proxy | Müştərinin özü seçdiyi, sorğunu onun əvəzinə göndərən vasitəçi |
| gateway | Əsas serverin qarşısında duran, müştəriyə elə server kimi görünən vasitəçi; gündəlik dildə “reverse proxy” |
| tunnel | İki əlaqə arasında baytları dəyişmədən ötürür; CONNECT rejimi buna nümunədir |

**Bir cümləlik fərq: düz proksi müştərini, tərs proksi serveri təmsil edir.**

:::figure
src = "m07-2.png"
alt = "Yuxarıda düz proksi: tələbə və işçi kompüterləri sorğunu Squid-ə göndərir, o, öz adından İnternet saytlarına gedir. Aşağıda tərs proksi: İnternet istifadəçilərinin HTTPS sorğusu DMZ-dəki Nginx-ə gəlir, o, Portal 1 və Portal 2-yə yönəldir."
caption = "Düz proksi müştərini təmsil edir: sayt proksinin IP-sini görür. Tərs proksi serveri təmsil edir: müştəri yalnız proksini görür."
wide = true
:::

:::note Sadə dillə
Düz proksi tələbənin kitabxanadan kitab istəmək üçün göndərdiyi nümayəndədir: kitabxana yalnız nümayəndəni tanıyır, tələbəni görmür. Tərs proksi universitetin qəbul otağıdır: qonaq qəbul işçisi ilə danışır, sənədin hansı kabinetdə işləndiyini bilmir.
:::

### Düz (forward) proksi

Düz proksi təşkilatın daxili istifadəçiləri ilə İnternet arasındadır. İstifadəçi sayta birbaşa çıxmır, bütün sorğuları proksi göndərir; sayt tələbənin yox, proksinin ünvanını görür. Ən çox işlədilən açıq mənbəli düz proksi **Squid**-dir, standart portu TCP 3128.

### Funksiyalar

| Funksiya | İzah |
| --- | --- |
| Məzmunun süzülməsi | Domen, URL və ya kateqoriya siyahılarına görə giriş qadağan olunur (zərərli saytlar, qumar) |
| Autentifikasiya | Kerberos, NTLM və ya LDAP ilə domenə bağlanır; qeydlərdə IP ilə yanaşı istifadəçi adı görünür |
| Qeydiyyat | Kim, nə vaxt, hansı domenə, nə qədər məlumat göndərib; SIEM üçün əsas mənbələrdən biri |
| Keşləmə | Tez-tez istənilən obyektlər saxlanır, kanal yükü azalır; HTTPS yayıldıqca faydası azalıb |
| Zərərli proqram yoxlaması | Endirilən fayllar antivirus motoruna göndərilir (ICAP protokolu ilə) |
| Məlumat sızmasının qarşısı | DLP sistemi ilə birlikdə kənara gedən faylları yoxlayır |
| IP gizlətmə | Daxili ünvanlar kənardakı sayta görünmür |

Ən dəyərli xüsusiyyət **məcburi çıxış nöqtəsi** olmasıdır: firewall yalnız proksinin İnternetə çıxmasına icazə verirsə, yoluxmuş kompüter hücumçunun serveri ilə birbaşa əlaqə qura bilmir; zərərli proqram proksidən keçməyə məcbur olur və əlaqə qeydlərdə görünür.

### Müştərini proksiyə yönəltmə üsulları

1. **Müştərini birbaşa sazlama (explicit proxy):** brauzer/sistem parametrlərində proksi ünvanı yazılır.
2. **PAC faylı (Proxy Auto-Configuration):** kiçik JavaScript faylı hər URL üçün proksi işlənib-işlənməyəcəyini deyir.
3. **WPAD:** brauzer PAC faylını DHCP və ya DNS vasitəsilə özü tapır. Rahatdır, amma riskli sayılır: yerli şəbəkədəki hücumçu saxta PAC faylı verib bütün trafiki öz üzərindən keçirə bilir.
4. **Şəffaf proksi:** istifadəçi heç nə sazlamır, marşrutlaşdırıcı və ya firewall HTTP trafikini proksiyə yönəldir.

### Bir sorğunun yolu

Brauzerdə proksi sazlıdırsa, serverə adətən yalnız yol yazılır (`GET /cedvel.html`), proksiyə isə tam ünvan göndərilir:

```
GET http://kitabxana.example/cedvel.html HTTP/1.1
Host: kitabxana.example
Proxy-Authorization: Negotiate YII...
```

1. Bağlantının hansı IP-dən gəldiyi və icazəli şəbəkəyə aid olub-olmadığı yoxlanır.
2. İstifadəçi autentifikasiya edilir; lazım olsa **407 Proxy Authentication Required** qaytarılır (bu, proksinin tələbidir; 401 saytın tələb etdiyi autentifikasiyadır).
3. Domen və URL siyasətlə tutuşdurulur; qadağandırsa, 403 və ya məlumat səhifəsi verilir.
4. Obyekt keşdə varsa və müddəti bitməyibsə, serverə getmədən cavab verilir.
5. Proksi serverlə öz TCP bağlantısını açır, sorğunu `GET /cedvel.html` formasında göndərir, adətən Via başlığı əlavə edir.
6. Cavab alınır, lazım olsa antivirus yoxlamasından keçir, müştəriyə qaytarılır.
7. Vaxt, IP, istifadəçi, URL, nəticə kodu, bayt sayı qeydə yazılır.

Squid qeyd sətri (tələbə `ali` keşdə olmayan səhifəni açıb):

```
1794066180.312  87 10.20.14.8 TCP_MISS/200 5120 GET http://kitabxana.example/cedvel.html ali HIER_DIRECT/203.0.113.40 text/html
```

### Proksi və HTTPS

HTTPS-də düz proksinin imkanları ciddi dəyişir; iki rejim var.

:::figure
src = "m07-3.png"
alt = "a) CONNECT tuneli: brauzer proksiyə CONNECT lms.example:443 göndərir, sonra brauzer ilə sayt arasında proksidən keçən bir TLS sessiyası qurulur; proksi yalnız domeni, vaxtı və həcmi bilir. b) TLS yoxlaması: proksi iki ayrı TLS sessiyası qurur, biri işçi ilə (proksi sertifikatı), biri sayt ilə (sayt sertifikatı)."
caption = "HTTPS trafikində düz proksinin iki iş rejimi."
wide = true
:::

### CONNECT tuneli

Brauzer proksiyə `CONNECT lms.example:443` göndərir. Proksi hədəflə TCP bağlantısı qurur və baytları dəyişmədən ötürür. TLS sessiyası brauzerlə sayt arasındadır, ona görə proksi URL yolunu, məzmunu, parolları, faylları görmür. Görə bildiyi: domen adı, port, vaxt, ötürülən həcm (məsələn, “tələbə 14:03-də lms.example saytına qoşulub, 2 MB məlumat alıb”, amma hansı fənn səhifəsini açdığı məlum deyil).

Domen iki yerdən görünür: CONNECT sətrindən və TLS ClientHello-dakı SNI sahəsindən. RFC 9849 ilə standartlaşmış **Encrypted Client Hello (ECH)** SNI-ni şifrələyir, ona görə SNI əsaslı süzgəclərin imkanları gələcəkdə azalacaq.

### TLS yoxlaması (TLS inspection)

Məzmunu görmək üçün proksi TLS-i açmalıdır: saytla öz TLS sessiyasını qurur, müştəriyə isə həmin sayt üçün yerindəcə yaratdığı sertifikatı təqdim edir. Sertifikatı təşkilatın öz CA-sı imzalayır; müştəri kompüterinə bu CA əvvəlcədən etibarlı kimi yüklənməlidir, əks halda brauzer xəbərdarlıq verəcək.

:::warning TLS yoxlaması razılaşdırılmış MITM-dir
Proksi hər kəsin parolunu, tibbi və bank məlumatını açıq görür; proksinin özü ələ keçirilsə, hücumçu şifrələnmiş bütün trafikə çıxış qazanır. Ona görə bank, səhiyyə, dövlət xidmətləri kateqoriyaları adətən yoxlamadan çıxarılır, istifadəçilərə siyasət barədə bildiriş verilir, CA açarı aparat modulunda (HSM) saxlanır. Sertifikat bağlaması (pinning) işlədən mobil tətbiqlər bu rejimdə işləməyə bilər.
:::

:::exam Tələ: HTTPS və proksi
Düz proksi HTTPS sayt üçün adətən yalnız domen adını görür, səhifə məzmununu yox. Məzmun üçün TLS yoxlaması lazımdır: şirkətin öz sertifikatı işçi kompüterlərinə etibarlı kimi yüklənir. Bu, həm texniki, həm məxfilik baxımından ayrıca qərar tələb edir.
:::

### Tərs (reverse) proksi

Tərs proksi serverlərin qarşısındadır. İnternetdən gələn sorğular əvvəl ona çatır, o, daxildəki uyğun serverə ötürür; müştəri backend-ə birbaşa qoşulmur, ünvanını görmür. Versiya və daxili ünvan sızmaları üçün cavab başlıqları, məzmun və yönləndirmələr ayrıca yoxlanır. Geniş yayılmışlar: Nginx, HAProxy, Apache HTTP Server, Traefik, Envoy; bulud xidməti kimi Cloudflare və AWS CloudFront.

| Funksiya | İzah |
| --- | --- |
| TLS-in dayandırılması (termination) | Sertifikat və şifrələmə bir yerdə idarə olunur; hər tətbiq serverində ayrıca sertifikat lazım olmur |
| Yük balanslaşdırması | Sorğular bir neçə serverə paylanır, sıradan çıxan server avtomatik kənarlaşdırılır |
| WAF | SQL inyeksiyası, XSS kimi veb hücumlarını tətbiqə çatmadan süzür (ModSecurity, Coraza) |
| Keşləmə və sıxılma | Statik fayllar proksidən verilir, serverin yükü azalır |
| Sürət məhdudlaşdırması | Bir IP-dən dəqiqədə icazəli sorğu sayı; giriş səhifəsinə kobud güc hücumunu zəiflədir |
| Serverin gizlədilməsi | Müştəri backend ünvanını görmür; başlıq və məzmundakı sızmalar ayrıca yoxlanır |
| DDoS-a qarşı dözümlülük | Böyük buludlu tərs proksi hücum trafikini serverə çatmamış udur |
| Yol üzrə marşrutlaşdırma | /lms bir serverə, /kitabxana başqasına yönəldilir |

Tərs proksi DMZ-də, tətbiq serverləri daxili zonada, baza ayrıca zonada olur; hücumçu İnternetdən yalnız proksi ilə danışa bilir.

:::figure
src = "m07-4.png"
alt = "İnternet, xarici firewall, DMZ-dəki tərs proksi və WAF (10.10.70.10), daxili firewall, tətbiq zonasında portal tətbiqi (10.10.80.20:8080) və baza zonasında PostgreSQL (10.10.90.30:5432)."
caption = "Universitet portalı üçün tərs proksi ilə üç zonalı arxitektura (şərti nümunə)."
wide = true
:::

İnternetdən yalnız DMZ-dəki proksinin TCP 443 portu açıqdır. Proksi yalnız portal tətbiqinin 8080 portuna gedə bilir; tətbiq yalnız baza zonasındakı PostgreSQL-in 5432 portuna çıxır. Hücumçu proksini ələ keçirsə belə, bazaya birbaşa yolu yoxdur.

:::warning TLS proksidə bitirsə, arxa tərəf açıq ola bilər
“Saytda HTTPS var” cümləsi daxili seqmentin şifrələndiyini bildirmir. Daxili zona etibarlı sayılmırsa, proksi ilə tətbiq arasında da TLS qurulur (re-encryption). Proksi bu zaman backend sertifikatını və host adını da yoxlamalıdır (Nginx-də `proxy_ssl_verify on`), əks halda daxili TLS MITM-ə açıq qalır.
:::

### Yükün paylanması alqoritmləri

| Alqoritm | İş prinsipi | Harada uyğundur |
| --- | --- | --- |
| Round robin | Sorğular növbə ilə paylanır | Eyni gücdə serverlər |
| Çəkili round robin | Güclü serverə daha çox sorğu | Fərqli gücdə serverlər |
| Ən az bağlantı (least connections) | Yeni sorğu ən az aktiv bağlantılı serverə gedir | Uzun sessiyalar |
| IP heş | Müştərinin IP-si eyni serverə bağlanır | Sessiya yaddaşı serverdədirsə |

Proksi serverlərin sağlamlığını yoxlayır (health check): məsələn, hər 5 saniyədən bir `/saglam` ünvanına sorğu göndərir, cavab gəlməyəndə serveri siyahıdan çıxarır. Sessiya serverdə saxlanırsa, istifadəçi eyni serverdə saxlanmalıdır (sticky session). Daha yaxşı həll sessiyanı Redis kimi ortaq yerdə saxlamaqdır: onda istənilən server istənilən sorğunu qəbul edir.

### Müştəri ünvanının zəncir boyu ötürülməsi

Sorğu bir neçə proksidən keçəndə X-Forwarded-For başlığına hər addımda ünvan əlavə olunur:

```
X-Forwarded-For: 203.0.113.7, 198.51.100.2
                 (müştəri)    (birinci proksi)
```

Serverin birbaşa gördüyü ünvan sonuncu proksidir. Siyahının sol tərəfini müştəri yaza bildiyi üçün etibarlı deyil. Düzgün üsul: siyahını **sağdan** oxumaq və etibarlı proksilərin ünvanlarını çıxmaq; etibarlı proksi olmayan ilk ünvan müştərinin real ünvanıdır.

### Proksinin digər növləri

| Növ | Xüsusiyyəti |
| --- | --- |
| Şəffaf proksi | Müştəri heç nə sazlamır, trafik şəbəkədə yönəldilir; qonaq Wi-Fi və provayderlərdə işlədilir |
| Anonim proksi | Müştəri IP-sini saytdan gizlədir; açıq anonim proksilər hücumçuların izini itirmək üçün geniş istifadə olunur |
| Açıq proksi (open proxy) | Hər kəsə xidmət edən səhv sazlanmış və ya qəsdən açılmış proksi; spam, hücum, blokdan yan keçmək üçün |
| HTTP proksi | HTTP-ni başa düşür: URL, başlıq, metod üzrə qərar verir |
| SOCKS proksi (SOCKS5, RFC 1928) | Sessiya səviyyəsində, istənilən TCP/UDP trafikini ötürür, məzmunu şərh etmir, şifrələmə vermir |
| Tətbiq proksisi (application proxy) | Konkret protokolu (SMTP, FTP, DNS) tam şərh edir; tətbiq səviyyəli firewall-ın əsasıdır |
| Zəncirvari proksi | Bir neçə proksidən ardıcıl keçid; Tor şəbəkəsi əlavə şifrələmə qatları olan xüsusi formasıdır |

### Proksi, NAT, firewall, VPN və yük balanslayıcısı

Bəzi ədəbiyyatda proksinin daxili ünvanları gizlətməsi NAT adlandırılır; bu dəqiq deyil. Hər ikisi daxili ünvanı gizlədir, amma **NAT** paketin başlığındakı IP və portu dəyişir, bağlantı birdir, məzmuna baxılmır. **Proksi** iki ayrı bağlantı qurur, tətbiq səviyyəsində işləyir, istifadəçiyə, URL-ə, məzmuna görə qərar verir.

| Texnologiya | OSI | Nə edir | Məzmunu görürmü | Şifrələyirmi |
| --- | --- | --- | --- | --- |
| NAT | 3–4 | IP və port başlığını dəyişir | Xeyr | Xeyr |
| Stateful firewall | 3–4 | Sessiyaya görə buraxır/bloklayır | Xeyr | Xeyr |
| Düz proksi | 5–7 | Müştərinin əvəzinə sorğu göndərir, süzür, qeyd edir | HTTP-də bəli, HTTPS-də yalnız TLS yoxlaması ilə | Özü şifrələmir |
| Tərs proksi | 5–7 | Serverin əvəzinə sorğu qəbul edir, paylayır, süzür | Bəli, TLS proksidə açılırsa | Müştəri tərəfində TLS verir |
| L4 yük balanslayıcısı | 4 | TCP/UDP bağlantılarını serverlərə paylayır | Xeyr | Xeyr |
| VPN | 2–4 (bəzən 7) | Bütün trafik üçün şifrəli tunel | Tətbiq məzmunu ilə işləmir | Bəli |

Praktikada sərhədlər bulanıqlaşır: müasir firewall (NGFW) proksi funksiyası da daşıyır, tərs proksi həm yük balanslayıcısı, həm WAF ola bilir. İmtahanda meyar: **“neçə ayrı bağlantı var və cihaz hansı səviyyədə qərar verir?”**

### Proksi hücumları və səhv sazlamalar

### Müştəri IP-sinin saxtalaşdırılması

Tərs proksi arxasındakı tətbiq bağlantını proksidən gəlmiş görür, ona görə real ünvan X-Forwarded-For ilə ötürülür (standart analoqu RFC 7239-dakı Forwarded başlığıdır). Hücumçu bu başlığı sorğusuna əvvəlcədən yaza bilər. Tətbiq ilk dəyərə inanırsa, IP məhdudiyyətini keçmək (`X-Forwarded-For: 10.0.0.1` ilə özünü daxili istifadəçi kimi göstərmək), qeydləri saxtalaşdırmaq, sürət məhdudiyyətindən yan keçmək olur. Həll: kənar proksi başlığı özü üzərinə yazır; tətbiq yalnız etibarlı proksidən gələn dəyərə inanır.

### HTTP Request Smuggling

Proksi və tətbiq serveri sorğunun harada bitdiyini fərqli başa düşəndə (Content-Length və Transfer-Encoding başlıqları ziddiyyət təşkil edəndə) hücumçu bir sorğunun içində ikinci, gizli sorğu göndərir; o, başqa istifadəçinin sorğusuna qoşula bilir. James Kettle 2019-da bu hücumu böyük saytlarda göstərib. Qorunma: proksi ilə server arasında HTTP/2, ziddiyyətli sorğuların rədd edilməsi, proqram təminatının yenilənməsi.

### Keşin zəhərlənməsi

Tərs proksi cavabı keşləyəndə keş açarına daxil olmayan başlıq (məsələn, X-Forwarded-Host) cavabı dəyişirsə, hücumçu zərərli skript keçidli cavabı keşə yerləşdirir və hər ziyarətçi onu alır. Qorunma: şəxsi cavablar keşlənmir (`Cache-Control: private` və ya `no-store`); cavabı dəyişən hər başlıq keş açarına əlavə edilir və ya Vary ilə bildirilir.

### Digər tipik səhvlər

- **Açıq proksi:** giriş siyahısı olmayan Squid hər kəsə xidmət edir, universitetin IP-si qara siyahıya düşür.
- **Serverin proksisiz əlçatan qalması:** tətbiq serverinin birbaşa ünvanı açıqdırsa, hücumçu WAF-dan yan keçir; tətbiq yalnız proksidən gələn bağlantıları qəbul etməlidir.
- **Proksi vasitəsilə SSRF:** proksi daxili ünvanlara sorğu göndərə bilirsə, hücumçu `http://169.254.169.254/` kimi bulud metadata ünvanlarına çıxa bilər.
- **Yol normallaşdırma fərqi:** proksi `/admin`-i qadağan edir, backend isə `/public/..%2fadmin` sorğusunu başqa cür açır və qayda keçilir.
- **HTTP/3 ilə yan keçmə:** firewall UDP 443-ü buraxırsa, brauzer QUIC ilə çıxıb TCP üzərindəki proksi siyasətindən yan keçə bilər.
- **Tək nasazlıq nöqtəsi:** bütün trafik proksidən keçdiyi üçün o dayananda xidmət dayanır; ən azı iki qovşaq (active/passive) lazımdır.
- **Qeydlərdə parol və token:** URL-də ötürülən sessiya identifikatorları loglara düşür.

### Praktiki konfiqurasiya nümunələri

Squid düz proksi qaydaları yuxarıdan aşağı oxunur, birinci uyğun gələn işləyir:

```
# /etc/squid/squid.conf
http_port 3128
acl telebe_lan src 10.20.0.0/16
acl qadagan    dstdomain .qumar.example .zererli.example
acl SSL_ports  port 443
acl Safe_ports port 80 443
acl CONNECT    method CONNECT
acl yerli_hedef dst 127.0.0.0/8 ::1/128 169.254.0.0/16 fe80::/10
acl daxili_hedef dst 10.0.0.0/8

http_access deny !Safe_ports
http_access deny CONNECT !SSL_ports
http_access deny manager
http_access deny yerli_hedef
http_access deny daxili_hedef
http_access deny qadagan
http_access allow telebe_lan
http_access deny all
```

Sonuncu sətir hamıya açıq proksinin qarşısını alır: siyahıda olmayan hər kəsə giriş qadağandır. `Safe_ports` adi sorğuların, `CONNECT !SSL_ports` tunellərin portunu məhdudlaşdırır; yalnız CONNECT-i məhdudlaşdırmaq kifayət deyil, çünki adi HTTP sorğusu ilə də təhlükəli porta müraciət etmək olar. `yerli_hedef` və `daxili_hedef` lokal xidmətlərə, bulud metadata ünvanına və daxili serverlərə çıxışı bağlayır.

Nginx tərs proksi nümunəsi:

```
server {
  listen 443 ssl;
  server_name portal.universitet.example;
  ssl_certificate     /etc/ssl/portal/fullchain.pem;
  ssl_certificate_key /etc/ssl/portal/privkey.pem;
  ssl_protocols TLSv1.2 TLSv1.3;

  location / {
    proxy_pass http://10.10.80.20:8080;
    proxy_set_header Host $host;
    proxy_set_header X-Real-IP $remote_addr;
    proxy_set_header X-Forwarded-For $remote_addr;
    proxy_set_header X-Forwarded-Proto https;
  }
}
```

`X-Forwarded-For`-a müştərinin göndərdiyi dəyər əlavə edilmir, üzərinə real ünvan yazılır; bu, kənarda duran ilk proksi üçün doğrudur. Arxada ikinci proksi varsa, zəncirin idarəsi üçün `set_real_ip_from` və etibarlı ünvanlar siyahısı işlədilir.

:::reveal Proksi niyə iki ayrı bağlantı qurur və bu ona nə imkan verir?
Müştəri–proksi və proksi–server ayrı bağlantılardır, ona görə proksi tətbiq səviyyəsində məlumatı oxuya, dəyişdirə, keşləyə və qadağan edə bilir; istifadəçiyə, URL-ə, məzmuna görə qərar verir. NAT-da isə bağlantı birdir və yalnız başlıq dəyişir.
:::

## III hissə. Virtual özəl şəbəkələr (VPN)

### VPN nədir

Virtual özəl şəbəkə (Virtual Private Network, VPN) etibarsız şəbəkə, adətən İnternet üzərindən iki nöqtə arasında qorunan məntiqi kanal qurur. “Virtual” kanalın fiziki ayrılmış kabel olmadığını, “özəl” tunelə yalnız icazəli tərəflərin qoşulduğunu bildirir.

Əsasında **tunelləmə (inkapsulyasiya)** dayanır: bir paket bütünlüklə başqa paketin içinə qoyulur. Daxili paketin ünvanları özəl ola bilər (10.10.80.5), xarici paketin ünvanları İnternetdə marşrutlaşan ictimai ünvanlardır. Tunelləmə özü məxfilik vermir: daxili paket şifrələnibsə, provayder məzmunu oxuya bilmir; şifrəsiz tuneldə inkapsulyasiya olunmuş paket də görünür.

Şifrələmə əlavə olunanda VPN üç xidmət verir:

- **Məxfilik:** tuneldəki məlumatı yolda oxumaq olmur.
- **Tamlıq:** paketin yolda dəyişdirildiyi aşkar edilir.
- **Autentifikasiya:** tərəflər bir-birinin kimliyini yoxlayır, saxta şlüzə qoşulmaq çətinləşir.

Çox IPsec həllində buna təkrar göndərmə hücumlarından qorunma da əlavə olunur (anti-replay).

:::warning VPN nəyi qorumur
VPN trafiki iki tunel ucu arasında qoruyur. Tunelin ucundan o yana (məsələn, VPN şlüzündən veb saytına qədər) yolu qorumur və istifadəçinin yoluxmuş kompüterini təmizləmir: zərərli proqramlı noutbuk VPN-ə qoşulanda zərərli proqram da tunelə daxil olur. “VPN etibarsız şəbəkəni etibarlı edir” ifadəsi dəqiq deyil; düzgünü: VPN etibarsız şəbəkə üzərindən qorunan kanal qurur, şəbəkənin özü etibarsız qalır.
:::

### VPN-lərin təsnifatı

### Təhlükəsizlik modelinə görə

- **Müdafiə olunan VPN (secure VPN):** trafiki kriptoqrafiya ilə qoruyur: IPsec, OpenVPN, WireGuard.
- **Etibarlı VPN (trusted VPN):** kriptoqrafiyaya yox, provayderin trafiki öz şəbəkəsində ayırmasına güvənir. Klassik nümunə MPLS VPN: paketlər provayder şəbəkəsində şifrələnmədən, amma məntiqi ayrılmış gedir.

İki məqam: tarixi mənbələrdə PPTP “müdafiə olunan VPN” nümunəsi kimi verilir, amma kriptoqrafiyası çoxdan sındırılıb və bu gün təhlükəsiz sayılmır. L2TP tək başına şifrələmir; onu ya provayderin etibarlı şəbəkəsində, ya IPsec ilə birlikdə işlədirlər.

### Arxitekturaya görə

| Növ | Təyinatı | Universitet nümunəsi |
| --- | --- | --- |
| Korporativ daxili (intranet, site-to-site) | Eyni təşkilatın ofislərini birləşdirir; tunel şlüzlər arasındadır | Baş korpusla filial arasında tunel |
| Uzaqdan giriş (remote access) | Ayrı-ayrı istifadəçini təşkilat şəbəkəsinə qoşur | Müəllim evdən LMS inzibati panelinə qoşulur |
| Korporativlərarası (extranet) | Tərəfdaş təşkilatlara məhdud giriş | Bank universitetin ödəniş sisteminin yalnız bir serverinə qoşulur |

:::figure
src = "m07-5.png"
alt = "Yuxarıda saytdan sayta VPN: baş korpus və filial LAN-ları arasında VPN şlüzləri və şifrəli IPsec tuneli. Aşağıda uzaqdan giriş VPN: evdəki noutbuk TLS və ya IPsec tuneli ilə universitetin VPN qapısına (MFA) qoşulur, qapı LMS və kitabxanaya yol verir."
caption = "Saytdan sayta və uzaqdan giriş VPN arxitekturaları."
wide = true
:::

### Reallaşdırma üsuluna və OSI səviyyəsinə görə

VPN marşrutlaşdırıcıda, firewall-da, serverdə proqram kimi və ya xüsusi aparat qurğusunda (VPN konsentrator) işləyə bilər; müasir təşkilatlarda ən çox firewall əsaslı və proqram əsaslı həllər görünür.

**L2 VPN** (L2TP, VXLAN-ın bəzi tətbiqləri) kadrları ötürür və uzaq ofisi eyni yerli şəbəkə kimi göstərir. **L3 VPN** (IPsec, WireGuard) IP paketlərini ötürür, marşrutlaşma ilə işləyir. TLS əsaslı VPN portal rejimində tətbiqə giriş, tunel rejimində L3 və bəzi həllərdə L2 bağlantısı verə bilər. Xarici qoruma protokolunun səviyyəsi daşınan trafikin səviyyəsini müəyyən etmir.

### IPsec

IPsec (Internet Protocol Security) IP səviyyəsində işləyən protokollar toplusudur; saytdan sayta VPN üçün bu gün də əsas standartdır. Üç hissəsi var:

| Komponent | Protokol və port | Vəzifəsi |
| --- | --- | --- |
| AH (Authentication Header) | IP protokolu 51 (RFC 4302) | Tamlıq və autentifikasiya verir, şifrələmə vermir. Xarici IP başlığını da qoruduğu üçün NAT ilə işləmir |
| ESP (Encapsulating Security Payload) | IP protokolu 50 (RFC 4303) | Şifrələmə, tamlıq, autentifikasiya. Praktikada demək olar ki, həmişə ESP işlədilir |
| IKE (Internet Key Exchange) | UDP 500, NAT varsa UDP 4500 | Tərəfləri autentifikasiya edir, açarları razılaşdırır, SA-ları idarə edir |

### Təhlükəsizlik assosiasiyası

SA (Security Association) iki tərəf arasında **bir istiqamətdə** trafik üçün razılaşdırılmış parametrlər toplusudur: alqoritm, açar, ömür müddəti. İkitərəfli rabitə üçün ən azı iki SA lazımdır. Paketdəki SPI (Security Parameter Index) qəbul edənə hansı SA-nı işlədəcəyini göstərir. SAD bazası mövcud SA-ları, SPD bazası hansı trafikin qorunacağı siyasətini saxlayır.

### Nəqliyyat və tunel rejimləri

:::figure
src = "m07-6.png"
alt = "Orijinal paket: IP, TCP, Məlumat. Nəqliyyat rejimi: IP, ESP başlığı, sonra şifrələnən TCP, Məlumat, ESP sonluq, və ICV. Tunel rejimi: Yeni IP, ESP başlığı, sonra şifrələnən Orijinal IP, TCP, Məlumat, ESP sonluq, və ICV."
caption = "ESP-nin nəqliyyat və tunel rejimlərində paket quruluşu."
wide = true
:::

- **Nəqliyyat rejimi:** yalnız faydalı yük qorunur, orijinal IP başlığı yerində qalır. İki host arasında birbaşa əlaqə üçündür (məsələn, iki server arasında verilənlər bazası replikasiyası).
- **Tunel rejimi:** bütöv orijinal paket şifrələnir və yeni IP başlığı əlavə olunur; daxili ünvanlar yolda görünmür. Saytdan sayta VPN-də işlədilir.

:::exam Yadda saxlanmalı fərq
ESP-nin nəqliyyat rejimində orijinal IP başlığı açıq qalır, tunel rejimində o da şifrələnir. Hər iki rejimdə xarici IP başlığı açıqdır.
:::

### IKEv2 mərhələləri

IKEv2 (RFC 7296) iki əsas mübadilə ilə tuneli cəmi dörd mesajda qurur:

- **IKE_SA_INIT:** tərəflər alqoritmləri razılaşdırır, Diffie-Hellman açıq dəyərlərini və təsadüfi ədədləri mübadilə edir. IKE SA yaranır, sonrakı mesajlar şifrələnir.
- **IKE_AUTH:** tərəflər bir-birini sertifikat, EAP və ya əvvəlcədən paylanmış açarla (PSK) autentifikasiya edir; ilk Child SA, yəni trafik üçün ESP tuneli yaradılır.
- **CREATE_CHILD_SA:** lazım olduqca əlavə tunel açılır və açarlar yenilənir.

Köhnə IKEv1-də “birinci/ikinci mərhələ” anlayışları, Main Mode və Aggressive Mode var idi; RFC 9395 (2023) IKEv1-i köhnəlmiş elan edir. Aggressive Mode PSK-nın heşini açıq ötürdüyü üçün oflayn sındırmaya imkan verir.

ESP-nin hər paketində ardıcıllıq nömrəsi var; qəbul edən sürüşən pəncərə saxlayır, artıq görülmüş nömrəli paketi atır, beləliklə təkrar göndərmə hücumu qarşısı alınır. NAT aşkarlananda (NAT-T) IKE UDP 4500-ə keçir, ESP paketləri də UDP 4500 içinə salınır (RFC 3948). Child SA yenilənəndə yeni Diffie-Hellman işlədilirsə, əlavə irəli məxfilik alınır.

### Alqoritm seçimi

| Vəzifə | İşlədilə bilər | İşlədilməməlidir |
| --- | --- | --- |
| Şifrələmə | AES-GCM (128/256 bit), AES-CBC + HMAC-SHA-2, ChaCha20-Poly1305 | DES, 3DES |
| Tamlıq | HMAC-SHA-256, HMAC-SHA-384 | MD5, SHA-1 |
| Diffie-Hellman | Qrup 14 (2048 bit), 19 və 20 (ECP), Curve25519 (qrup 31) | Qrup 1, 2, 5 |
| Autentifikasiya | Sertifikat, uzun təsadüfi PSK, EAP+MFA | Qısa və ya hamıda eyni PSK |

### Paketin tuneldən keçməsi

Filialdakı 192.168.20.15 kompüteri baş korpusdakı 10.10.80.20 serverinə sorğu göndərir; şlüzlərin ictimai ünvanları 203.0.113.2 (filial) və 198.51.100.1 (baş korpus).

:::steps Paketin yolu
[[step]]
title = "Adi paket"
body = "Kompüter mənbə 192.168.20.15, təyinat 10.10.80.20 olan adi paket yaradır; onun VPN-dən xəbəri yoxdur."

[[step]]
title = "SPD yoxlaması"
body = "Filial şlüzü paketi SPD ilə tutuşdurur: siyasətdə bu trafikin qorunması yazılıb."

[[step]]
title = "SA"
body = "Uyğun SA tapılır; yoxdursa, IKE ilə qurulur."

[[step]]
title = "Şifrələmə"
body = "Bütün orijinal paket AES-GCM ilə şifrələnir, ESP başlığı (SPI və ardıcıllıq nömrəsi) əlavə edilir."

[[step]]
title = "Yeni IP başlığı"
body = "Mənbə 203.0.113.2, təyinat 198.51.100.1, protokol 50. Yoldakı provayder yalnız iki şlüzün ünvanını və ESP protokolunu görür."

[[step]]
title = "Qəbul"
body = "Baş korpus şlüzü SPI-yə görə SA-nı tapır, ardıcıllıq nömrəsini təkrar göndərməyə qarşı yoxlayır, AES-GCM ilə tamlığı yoxlayıb şifrəni açır."

[[step]]
title = "Çatdırılma"
body = "Orijinal paket daxili şəbəkəyə verilir və serverə çatır."
:::

AES-GCM-də autentifikasiya yoxlaması və deşifrələmə birləşmiş əməliyyatdır; yoxlama uğursuz olsa, paket atılır və açıq mətn daxili şəbəkəyə ötürülmür.

### Tərəflərdə uyğun olmalı parametrlər

Saytdan sayta tunelində ən çox rast gəlinən nasazlıq tərəflərin parametrlərinin fərqli olmasıdır.

| Parametr | Baş korpus | Filial |
| --- | --- | --- |
| IKE versiyası | IKEv2 | IKEv2 |
| Autentifikasiya | Sertifikat | Sertifikat |
| IKE şifrələmə, heş, DH | AES-256-GCM, SHA-384, qrup 20 | Eyni |
| IKE SA ömrü | 24 saat | 24 saat |
| ESP alqoritmi | AES-256-GCM | Eyni |
| Child SA ömrü | 1 saat | 1 saat |
| Qorunan alt şəbəkə (yerli) | 10.10.80.0/24 | 192.168.20.0/24 |
| Qorunan alt şəbəkə (uzaq) | 192.168.20.0/24 | 10.10.80.0/24 |

Son iki sətir güzgü kimi olmalıdır: bir tərəfin “yerli” dəyəri o biri tərəfin “uzaq” dəyəridir. Cədvəldəki ömürlər nümunədir: IKEv2-də IKE SA və Child SA ömürlərinin eyni olması məcburi deyil, razılaşdırılmır; daha qısa müddət tətbiq edən tərəf adətən açar yeniləməsini başladır. Tunel qurulmursa, əvvəlcə UDP 500/4500 və protokol 50-nin firewall-dan keçdiyi, sonra alqoritm və identifikator uyğunluğu, sonda sertifikatın vaxtı və etibar zənciri yoxlanır.

### TLS əsaslı VPN və OpenVPN

TLS (SSL) VPN tuneli TLS üzərində qurur; iki forması var: **müştərisiz portal rejimi** (brauzerlə portala daxil olub müəyyən veb tətbiqlərinə çıxış) və **tunel rejimi** (cihazda kiçik müştəri proqramı, şəbəkə səviyyəsində giriş). Üstünlüyü firewall-dan keçmənin asanlığıdır (TCP 443 əksər şəbəkələrdə açıqdır). Çatışmazlığı: VPN qapısı İnternetə açıq mürəkkəb veb tətbiqidir; son illərin ən ciddi VPN hadisələrinin çoxu belə qapılardakı zəifliklərdən gəlib.

**OpenVPN** açıq mənbəli VPN-dir: idarəetmə kanalı TLS üzərində, məlumat kanalı öz protokolundadır. Standart portu UDP 1194, TCP 443-də də sazlana bilir (bu, firewall-un onu tanıyıb bloklamayacağına zəmanət deyil). TCP üzərində TCP daşımaq “TCP meltdown”a gətirə bilər: iki qatın təkrar göndərmə mexanizmləri bir-birini pozur, sürət kəskin düşür. Mümkün olan yerdə UDP seçilir.

### WireGuard

WireGuard müasir VPN protokoludur, 2020-ci ildə Linux 5.6 nüvəsinə daxil edilib. Kodu çox kiçikdir (təxminən 4000 sətir), audit asandır. Alqoritmlər sabitdir, danışıq aparılmır: Curve25519 (açar mübadiləsi), ChaCha20-Poly1305 (şifrələmə), BLAKE2s (heş); razılaşma olmadığı üçün zəif alqoritmə endirmə hücumu da yoxdur. Çatışmazlıqlar: alqoritmlər FIPS siyahısında deyil (dövlət tələbli təşkilatlarda işlədilməyə bilər), istifadəçi idarəetməsi və dinamik IP paylanması protokola daxil deyil.

Hər tərəfin açar cütü var. `AllowedIPs` həm marşrutlaşdırma, həm icazə rolunu daşıyır. Noutbuk konfiqurasiyası yalnız iki alt şəbəkəyə gedən trafiki tunelə salır:

```
[Interface]
Address    = 10.200.0.2/32
PrivateKey = <noutbukun gizli açarı>
DNS        = 10.10.50.53

[Peer]
PublicKey  = <VPN şlüzünün açıq açarı>
Endpoint   = vpn.universitet.example:51820
AllowedIPs = 10.10.80.0/24, 10.10.50.0/24
PersistentKeepalive = 25
```

`AllowedIPs = 0.0.0.0/0, ::/0` yazılsaydı, bütün trafik tunelə gedərdi, yəni tam tunel alınardı. Şlüz tərəfində hər peer üçün AllowedIPs yalnız onun tunel ünvanını göstərməlidir; bu dəyər həm də mənbə ünvanı süzgəcidir. Cihaz itəndə peer konfiqurasiyadan silinir.

### Protokolların müqayisəsi

| Meyar | IPsec/IKEv2 | OpenVPN | WireGuard |
| --- | --- | --- | --- |
| İş səviyyəsi | Şəbəkə, ƏS nüvəsi | İdarəetmə istifadəçi sahəsində; məlumat kanalı klassik rejimdə istifadəçi sahəsində, DCO ilə nüvədə | Şəbəkə, nüvə |
| Nəqliyyat | ESP, UDP 500/4500 | UDP 1194 və ya TCP | UDP, tez-tez 51820 |
| Alqoritm seçimi | Danışıq yolu ilə | Danışıq yolu ilə | Sabit |
| Autentifikasiya | Sertifikat, PSK, EAP | Sertifikat, parol | Açıq açarlar |
| Əsas üstünlük | Standart, aparat dəstəyi | Çevik, firewall-dan asan keçir | Sürət, kiçik kod |
| Əsas çatışmazlıq | Sazlaması mürəkkəb | Nisbətən yavaş | İstifadəçi idarəetməsi yoxdur |
| Tipik istifadə | Saytdan sayta | Uzaqdan giriş | Uzaqdan giriş, serverlərarası |

### Köhnəlmiş protokollar

| Protokol | Status | Qeyd |
| --- | --- | --- |
| IPsec/IKEv2 | Aktual | Saytdan sayta standart; düzgün alqoritmlərlə |
| WireGuard | Aktual | Sadə və sürətli; FIPS tələbi olmayan yerlərdə |
| OpenVPN, TLS VPN | Aktual | TLS 1.2/1.3 ilə sazlanmalı, qapı proqramı vaxtında yenilənməlidir |
| L2TP/IPsec | Köhnəlir | L2TP özü şifrələmir, şifrələməni IPsec verir; Microsoft 2024-də RRAS üçün L2TP-ni köhnəlmiş elan edib |
| PPTP | Etibarsız | TCP 1723 və GRE; MS-CHAPv2 sındırılıb: tutulmuş mübadilə bir DES açarının axtarışına gətirilir |
| MPLS VPN | Fərqli sinif | Provayder şəbəkəsində məntiqi ayırma; özü şifrələmir |

PPTP-nin sonunun tarixi: 2012-də Moksi Marlinspayk və David Hulton MS-CHAPv2 autentifikasiyasının bir DES açarını (2⁵⁶ variant) tapmağa gətirildiyini göstərdilər və bunu xidmət kimi təqdim etdilər. Microsoft 2024-ün oktyabrında Windows Server-də RRAS üçün PPTP və L2TP-ni köhnəlmiş elan etdi; Windows Server 2025-in yeni quraşdırılmasında bu bağlantılar standart olaraq qəbul edilmir.

### Tam və bölünmüş tunel

**Tam tunel (full tunnel):** istifadəçinin bütün trafiki təşkilat şlüzündən keçir, təhlükəsizlik vasitələri hamısını görür; çatışmazlıq kanalın yüklənməsidir. **Bölünmüş tunel (split tunnel):** yalnız təşkilat resurslarına gedən trafik tunelə düşür, qalanı birbaşa İnternetə çıxır; sürətlidir, amma həmin trafik proksidən və DLP-dən keçmir.

:::figure
src = "m07-7.png"
alt = "Solda tam tunel: noutbuk VPN şlüzünə qoşulur, şlüz həm LMS-ə, həm İnternetə yol verir. Sağda bölünmüş tunel: noutbuk VPN şlüzü vasitəsilə yalnız LMS-ə gedir, İnternetə birbaşa çıxır."
caption = "Tam və bölünmüş tunel: tam tuneldə bütün trafik şirkət nəzarətindən keçir, bölünmüşdə İnternet trafiki nəzarətdən kənarda qalır."
wide = true
:::

Seçərkən **DNS sızması** nəzərə alınır: tunel qurulsa da, DNS sorğuları yerli provayderə gedirsə, sayt adları yolda görünür. Həll:

- VPN müştərisində daxili DNS serverini təyin etmək və ona marşrutu tuneldən keçirmək;
- tuneldənkənar DNS çıxışını məhdudlaşdırmaq;
- IPv4, IPv6 və tətbiqlərin ayrıca DNS/DoH parametrlərini yoxlamaq;
- tunel kəsiləndə trafiki dayandıran mexanizmi (kill switch) açmaq.

VPN əlavə başlıq düşdüyü üçün MTU-nu azaldır: standart 1500 baytlıq paket tunelə sığmaya bilər. Böyük faylların yüklənmədiyi, amma adi saytların açıldığı hal çox vaxt MTU problemidir. Həll: ICMP “Fragmentation Needed” mesajlarını bağlamamaq və şlüzdə TCP MSS dəyərini azaltmaq (MSS clamping).

### VPN-in təhlükəsizliyi

### Hücumlar və real hadisələr

VPN qapısı hücumçu üçün cəlbedicidir: İnternetə açıqdır, daxili şəbəkəyə birbaşa gedir, yenilənməsi çox vaxt gecikir.

- **Colonial Pipeline, aprel 2021:** hücum köhnə, işlədilməyən VPN hesabından başladı. Hesabda çoxfaktorlu autentifikasiya yox idi, parolu sızmış parollar siyahısında tapılmışdı. Bir hesab ABŞ-ın şərq sahilinə yanacaq daşıyan kəmərin bir neçə gün dayanmasına gətirib çıxardı.
- **SSL VPN qapılarındakı zəifliklər:** Pulse Secure CVE-2019-11510 və Fortinet CVE-2018-13379 autentifikasiyasız həssas faylların, o cümlədən kimlik məlumatlarının sızmasına imkan verib. Ivanti Connect Secure-də CVE-2023-46805 autentifikasiyadan yan keçmədir, CVE-2024-21887 isə autentifikasiya olunmuş administrator üçün əmr inyeksiyasıdır; ikisi birləşdiriləndə autentifikasiyasız əmr icrası mümkün olur.
- CISA və NSA 2021-də uzaqdan giriş VPN-lərinin seçilməsi və sərtləşdirilməsi üzrə birgə tövsiyə dərc ediblər.

### Sərtləşdirmə tədbirləri

- Çoxfaktorlu autentifikasiya bütün istifadəçilər üçün məcburidir.
- Sertifikat əsaslı autentifikasiya PSK-dan üstündür.
- İşlədilməyən hesablar müntəzəm söndürülür.
- VPN qapısı yeniləmə prioritetinə birinci salınır.
- İstifadəçiyə ən az lazım olan alt şəbəkələr verilir (minimum imtiyaz).
- İdarəetmə interfeysi İnternetdən açıq saxlanmır.
- Qoşulan cihaz yoxlanır: ƏS yenilənibmi, disk şifrələnibmi, EDR işləyirmi.
- VPN qeydləri SIEM-ə göndərilir; qeyri-adi coğrafiya və vaxt izlənir.

### VPN və ZTNA

Ənənəvi VPN “içəridəsənsə, etibarlısan” məntiqindədir: qoşulan istifadəçi şəbəkənin böyük hissəsini görür. Sıfır etimad yanaşmasında (NIST SP 800-207) etimad şəbəkədəki yerə görə verilmir, hər sorğu ayrıca yoxlanır. **ZTNA (Zero Trust Network Access)** istifadəçini şəbəkəyə deyil, yalnız icazəli konkret tətbiqə qoşur, kimliyi və cihazın vəziyyətini hər dəfə yoxlayır.

| Meyar | Ənənəvi VPN | ZTNA |
| --- | --- | --- |
| Giriş sahəsi | Şəbəkə və ya alt şəbəkə | Konkret tətbiq |
| Etimad | Qoşulanda bir dəfə | Davamlı, kontekstə görə |
| Daxili hərəkət | Əlavə qaydalar olmasa asan | Məhduddur |
| Tətbiqlərin görünməsi | Qapı İnternetə açıqdır | Tətbiqlər İnternetdən görünmür |

ZTNA VPN-in tam əvəzi deyil: saytdan sayta rabitə üçün IPsec tunelləri işləməyə davam edir, ZTNA daha çox istifadəçi girişi üçün seçilir.

:::note Köhnə slaydlarla fərq
Lektorun köhnə slaydlarında üç yanlışlıq var: proksinin funksiyası “NAT” adlandırılıb (səhv: NAT bir bağlantı, başlıq dəyişir; proksi iki bağlantı, tətbiq səviyyəsi); PPTP IPsec və OpenVPN ilə yanaşı “müdafiə olunan VPN” kimi verilib (çoxdan etibarsızdır); “etibarlı VPN: MPLS və L2TP” qruplaşdırması çaşdırıcıdır (MPLS ayırır, şifrələmir; L2TP tunel qurur, şifrələməni IPsec verir). “VPN etibarsız şəbəkəni etibarlı edir” ifadəsi də dəqiq deyil.
:::

:::reveal VPN nəyi qorumur? İki nümunə deyin.
Tunelin ucundan o yana yolu (məsələn, VPN şlüzündən veb saytına qədər) və istifadəçinin yoluxmuş kompüterini: zərərli proqramlı noutbuk VPN-ə qoşulanda zərərli proqram da tunellə şirkət şəbəkəsinə girir.
:::

:::flashcards
[[card]]
front = "Honeypot, honeynet, honeytoken: fərq"
back = "**Honeypot** tək saxta sistem, **honeynet** bir neçə tələdən ibarət saxta şəbəkə, **honeytoken** sistem yox, saxta məlumat parçası (saxta hesab, fayl, API açarı); istifadə olunan kimi həyəcan verir."
[[card]]
front = "Düz və tərs proksi kimi təmsil edir?"
back = "Düz proksi **müştərini**, tərs proksi **serveri**."
[[card]]
front = "ESP nəqliyyat və tunel rejimi: orijinal IP başlığı?"
back = "Nəqliyyat rejimində **açıq qalır**, tunel rejimində **şifrələnir**; xarici IP başlığı hər ikisində açıqdır."
[[card]]
front = "ZTNA ənənəvi VPN-dən nə ilə fərqlənir?"
back = "İstifadəçini şəbəkəyə yox, **konkret tətbiqə** qoşur, kimlik və cihaz vəziyyəti hər dəfə yoxlanır."
:::
