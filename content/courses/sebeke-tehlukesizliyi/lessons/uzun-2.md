+++
title = "Kibertəhlükəsizlik təhdidləri; təhdid məlumatları və analitikası"
unit = "uzun"
order = 2
summary = "Tam mühazirə: aktivlər və risk, təhdid aktorları və APT, hücumların təsnifatı, sosial mühəndislik, şəbəkə və veb hücumları, CVE/CWE/CVSS/EPSS/KEV, standartlar və siyasət, təhdid kəşfiyyatı (CTI), həyat dövrü, IoC/IoA/TTP, ATT&CK, OSINT, STIX/TAXII/TLP/MISP."
updated = 2026-11-09

[[source]]
title = "Mühazirə 2: Kibertəhlükəsizlik təhdidləri; təhdid məlumatları və analitikası"
note = "Elmar Cabbarov, 2026–2027"
+++

Mövzu iki hissədən ibarətdir: təhdidlərin xəritəsi (kim hücum edir, niyə və hansı üsullarla) və təhdid kəşfiyyatı (bu biliyi müdafiəyə necə çeviririk). Universitetin LMS-i, tələbə bazası, kitabxanası və yataqxana şəbəkəsi, bütün adlar, rəqəmlər və ssenarilər şərti tədris nümunəsidir.

:::note Bu mövzudan sonra bacarmalısan
- Təhdidi zəiflikdən və riskdən ayırmağı; hücumçu növlərini motiv və imkanına görə fərqləndirməyi.
- Sosial mühəndislik, parol, şəbəkə və tətbiq hücumlarının mexanizmini izah etməyi.
- CVE, CWE, CVSS, EPSS və KEV ilə düzəliş prioriteti seçməyi.
- Xam müşahidəni yoxlanmış analitik nəticəyə çevirməyi; kəşfiyyatı auditoriyaya və TLP etiketinə görə təqdim etməyi.
- Universitetin LMS-i, tələbə bazası, kitabxanası və yataqxana şəbəkəsi üçün aşkarlama, cavab və bərpa tədbirlərini əsaslandırmağı.
:::

## Nəyi qoruyuruq: sistem, informasiya və risk

### İnformasiya sistemi və aktivlər

İnformasiya sistemi məlumatı toplayan, saxlayan, emal edən və qərar üçün təqdim edən əlaqəli komponentlər məcmusudur. Aparat və proqramla yanaşı insanlar, iş qaydaları və məlumatın özü də sistemə daxildir. LMS (Learning Management System, tədrisin idarə edilməsi sistemi) yalnız veb server deyil: tələbənin hesabı, qiymətləndirmə qaydası, verilənlər bazası, ehtiyat nüsxə və imtahan nəticəsini təsdiqləyən əməkdaş eyni prosesin hissələridir.

Aktiv (asset) təşkilat üçün dəyəri olan resursdur. Dəyər satınalma qiyməti ilə məhdudlaşmır: qiymət cədvəlinin kiçik faylı böyük serverdən həssas ola bilər, çünki icazəsiz dəyişiklik diplomun verilməsinə təsir edər. Açıq kitabxana kataloqunun məxfiliyi aşağıdır, amma kataloq işləməsə tələbələr resurs tapa bilmirlər. Hər aktiv üçün sahib, istifadə məqsədi, həssaslıq, asılı xidmətlər və bərpa tələbi müəyyən edilir.

İnformasiyanın keyfiyyəti də qərara təsir edir: düzgün, amma keçən semestrə aid tələbə siyahısı cari hüquqları yoxlamağa yaramır; dəqiq vaxtı olmayan jurnal qeydi hücum ardıcıllığını səhv göstərə bilər. Analitik məlumatın düzgünlüyünü, aktuallığını, dolğunluğunu və suala uyğunluğunu ayrıca yoxlayır. Çox məlumat avtomatik yaxşı qərar demək deyil.

| Aktiv | Məxfilik | Tamlıq | Əlçatanlıq |
| --- | --- | --- | --- |
| Tələbə bazası | Şəxsi məlumatı yalnız səlahiyyətli şəxs görür | Qiymət və status icazəsiz dəyişmir | Qeydiyyat zamanı sorğular işləyir |
| LMS | Qapalı kurs materialları qorunur | Tapşırıq və nəticələr düzgün saxlanır | İmtahan vaxtı xidmət dayanmaz |
| Kitabxana kataloqu | Açıq kataloqda məhdud tələb var | Kitabın mövcudluğu düzgün göstərilir | Axtarış xidməti işləyir |
| Yataqxana Wi-Fi-si | İstifadəçi trafiki və hesabları qorunur | Şəbəkə sazlamaları dəyişdirilmir | Qanuni istifadəçi qoşulur |

### Təhlükəsizlik xassələri və anlayışların fərqi

Məxfilik (confidentiality) məlumatın icazəsiz tərəfə açılmamasıdır. Tamlıq (integrity) məlumatın və emalın icazəsiz dəyişiklikdən qorunmasıdır. Əlçatanlıq (availability) səlahiyyətli istifadəçinin tələb olunan vaxtda resursdan yararlanmasıdır. Bu üçlük CIA adlanır. Bütöv model autentiklik, hesabatlılıq, əməliyyatdan imtinanın qarşısının alınması, etibarlılıq və insanın fiziki təhlükəsizliyini də nəzərə alır.

- **Autentiklik**: məlumatın və ya tərəfin iddia edilən mənşəyə uyğunluğu.
- **Hesabatlılıq (accountability)**: əməliyyatı konkret subyektə bağlamaq imkanı; ortaq administrator hesabı bunu zəiflədir.
- **İmtinanın qarşısının alınması (non-repudiation)**: əməliyyatın mənşəyi və ya qəbuluna dair yoxlanıla bilən sübut. Bu "təxirəsalınmazlıq" deyil. Rəqəmsal imza sübutun bir hissəsidir, amma açarın idarəsi və prosedurlar da etibarlı olmalıdır.

Altı anlayış ayrılır:

| Anlayış | Mənası |
| --- | --- |
| Təhdid (threat) | Arzuolunmaz nəticəyə səbəb ola bilən şərait və ya hadisə |
| Zəiflik (vulnerability) | Sistemdə, prosedurda və ya nəzarətdə istifadə oluna bilən boşluq |
| Hücum (attack) | Həmin boşluqdan və ya başqa imkandan qəsdən istifadə cəhdi |
| Risk | Təhdidin baş vermə ehtimalı və nəticəsinin ağırlığı ilə bağlı qeyri-müəyyənlik |
| İnsident | Təhlükəsizliyi pozan və ya real şəkildə təhlükəyə atan hadisə |
| Aktiv (asset) | Təşkilat üçün dəyəri olan resurs |

:::example Eyni ssenarida altı anlayış (şərti ssenari)
Keçmiş əməkdaşın VPN hesabı açıq qalıb: hesabın vaxtında bağlanmaması **zəiflikdir**. Hesabdan məlumat oğurlamaq istəyən tərəf **təhdid mənbəyidir**. Oğurlanmış parolla giriş cəhdi **hücumdur**. Tələbə bazasının ixrac edilməsi **insidentdir**. Şəxsi məlumatın yayılması, qeydiyyatın dayanması və etimad itkisi **riskin** mümkün nəticələridir. Qorunan **aktiv** tələbə bazasıdır.
:::

Risk üçün bəzən ehtimal ilə zərərin hasili hesablanır; bu yalnız ölçülərin mənası və fərziyyələr aydın olduqda faydalıdır. Şərti: illik ehtimal 0,1, bir hadisənin zərəri 50 000 manat, gözlənilən illik itki 5 000 manat. Nəticə gələcək xərcin zəmanətli proqnozu deyil: ehtimallar qeyri-dəqiq ola bilər, məxfilik pozuntusunun nəticəsi pulla tam ifadə edilməyə bilər. Rəhbərlik fərziyyələri və qeyri-müəyyənliyi də görməlidir.

## Təhdid aktorları və onların məqsədləri

### Aktorun motivi və imkanları

Təhdid aktoru (threat actor) zərərli fəaliyyət göstərən şəxs, qrup və ya təşkilatdır. Təhdid mənbəyi daha geniş anlayışdır: yanğın, enerji kəsilməsi və təsadüfi səhv də zərər verə bilər. Serverin disk nasazlığı ilə dayanması əlçatanlıq insidentidir, amma qəsdən hücum olduğunu göstərmir.

Aktorları yaşına və təhsilinə görə təsnif etmək düzgün deyil: hazır alətdən istifadə edən tələbə də, işçi də ola bilər. Haker sözü avtomatik cinayətkar demək deyil: yazılı icazə və müəyyən sərhədlər daxilində sınaq aparan etik haker (pentester) zəifliklərin aradan qaldırılmasına kömək edir. Eyni skanın hüquqi və təşkilati mənası icazədən asılıdır.

| Aktor | Motiv | İmkan | Şərti universitet nümunəsi |
| --- | --- | --- | --- |
| Həvəskar hücumçu (skript-kiddi) | Maraq, nüfuz | Aşağı: hazır alətlər, dəyişən bacarıq | Açıq laboratoriya serverini skan edir |
| Haktivist (hacktivist) | Siyasi və ideoloji mesaj | Aşağı–orta: ictimai görünürlüyə yönəlir | Saytın məzmununu dəyişir, DDoS edir |
| Cinayətkar qrup | Pul və satıla bilən giriş | Orta–yüksək: ixtisaslaşmış xidmətlərdən yararlanır | Maliyyə hesabını ələ keçirib ödənişi yönləndirir |
| Dövlət dəstəkli qrup | Casusluq, təsir, sabotaj | Çox yüksək: uzunmüddətli resurs | Tədqiqat layihəsinin sənədlərini toplayır |
| Daxili pozucu (insider) | Pul, narazılıq, şəxsi maraq, səhlənkarlıq | Qanuni giriş və daxili bilik | Tələbə bazasını icazəsiz çıxarır |
| Kommersiya rəqibi | İqtisadi üstünlük | Orta: vasitəçi və daxili mənbə axtara bilər | Ödənişli tədqiqat nəticələrini əldə edir |

:::tip Aktoru davranışından tanı
Situasiya sualında hücumçunun kim olduğu verilmirsə, davranışa bax: fidyə tələb edən cinayətkardır, saytın üzünə siyasi şüar yazan haktivistdir, aylarla səssiz oturub sənəd oğurlayan isə çox güman ki dövlət dəstəkli qrupdur.
:::

Eyni motiv müxtəlif vasitələrlə gerçəkləşə bilər: pul istəyən qrup faylları şifrələyə, məlumatı yaymaqla hədələyə və ya saxta hesab-faktura göndərə bilər. Fidyə proqramının xidmət kimi satılması (Ransomware-as-a-Service, RaaS) modelində proqramı hazırlayan, ilkin giriş satan vasitəçi, məlumat çıxaran və danışıqları aparan tərəflər ayrı ola bilər.

Motiv barədə nəticə davranışa əsaslanan fərziyyədir. Siyasi şüar yazılması hücumçunun mütləq haktivist olduğunu sübut etmir; o, başqa fəaliyyəti gizlədə bilər. Xarici IP ünvanı dövlət mənsubiyyətinin sübutu deyil: infrastruktur icarəyə götürülə və ya əvvəlcə ələ keçirilə bilər. Atributlaşdırma (attribution), yəni fəaliyyəti konkret aktora bağlamaq, alternativ izahları və sübutun etibarlılığını yoxlamağı tələb edir.

### APT və davamlı hədəfləmə

İnkişaf etmiş davamlı təhdid (Advanced Persistent Threat, APT) müəyyən məqsəd üçün uzun müddət fəaliyyət göstərə, imkanlarını uyğunlaşdıra və girişini saxlaya bilən rəqibdir. Dövlət dəstəkli qruplar çox vaxt APT olur, amma APT dövlət mənsubiyyətinin sinonimi deyil. Mürəkkəblik hər mərhələdə naməlum zəiflikdən (zero-day) istifadə də demək deyil: hücumçu məqsədinə oğurlanmış parol və standart idarəetmə aləti ilə çatırsa, daha bahalı üsula ehtiyac duymur.

Şərti ssenari: rəqib universitetin enerji tədqiqatlarını istəyir. Layihənin açıq iştirakçı siyahısını öyrənir, tədqiqatçıya saxta konfrans məktubu göndərir, hesab əldə edib daxili fayl paylaşmalarını araşdırır, başqa giriş yolu saxlayır və sənədləri hissələrlə çıxarır. İlkin hesab bağlansa, alternativ girişdən qayıda bilər: davamlılıq eyni bağlantının fasiləsiz açıq qalması demək deyil.

Cavab yalnız zərərli domeni bloklamaqla bitmir. Hansı hesabların, sessiyaların və açarların ələ keçirildiyi, hansı sistemlərə keçid olduğu araşdırılır; məxfi tədqiqat seqmenti tələbə laboratoriyasından ayrılır, imtiyazlı girişlərə ayrıca nəzarət qoyulur. APT adı üçün günlərin müəyyən sayı yoxdur: məqsəd, resurs, uyğunlaşma və müşahidə olunan davranış birlikdə qiymətləndirilir.

## Hücumların təsnifatı və hücum səthi

### Passiv və aktiv hücumlar

ITU-T X.800 təhlükəsizlik arxitekturasında **passiv hücumlara** mesaj məzmununun əldə edilməsi və trafik analizi daxildir. Passiv müşahidə məlumatı dəyişdirmir, ona görə aşkarlamaq çətindir. Şifrələnmiş yataqxana trafikində məzmun oxunmasa da, bağlantı vaxtı və həcmi fəaliyyət barədə məlumat verə bilər: şifrələmə trafik analizinin bütün imkanlarını aradan qaldırmır.

**Aktiv hücumda** rəqib sistemin işinə və ya məlumat axınına müdaxilə edir: başqasının kimliyinə bürünmə (masquerade), əvvəlki mesajın təkrar göndərilməsi (replay), mesajın dəyişdirilməsi və xidmətdən imtina. Tutulmuş kitabxana giriş sorğusunu yenidən göndərmək replay hücumudur; sorğuda birdəfəlik dəyər, vaxt məhdudiyyəti və uyğun sessiya nəzarəti varsa, əvvəlki sorğu rədd edilə bilər.

Təsirə görə dördlü bölgü pozulan xassəni göstərir:

| Forma | Pozulan xassə | Şərti nümunə | Təsnifat qeydi |
| --- | --- | --- | --- |
| Kəsmə (interruption) | Əlçatanlıq | LMS-in resursları tükənir | Adətən aktiv |
| Ələ keçirmə (interception) | Məxfilik | Şifrələnməmiş sorğu dinlənir | Passiv ola bilər |
| Dəyişdirmə (modification) | Tamlıq | Qiymət bazada dəyişdirilir | Aktiv |
| Saxtalaşdırma (fabrication) | Autentiklik | Saxta ödəniş təsdiqi yaradılır | Aktiv |

:::exam
Bu dörd təsir formasını bütövlükdə "aktiv hücum" adlandırmaq düzgün deyil, çünki ələ keçirmə passiv ola bilər. Təsirə görə bölgü (hansı xassə pozulur) ilə fəaliyyətə görə bölgü (passiv/aktiv) ayrı suallara cavab verir. Eyni insidentdə bir neçə xassə pozula bilər: əvvəlcə məlumat çıxarılır, sonra şifrələnir və xidmət dayanır.
:::

### Hücum vektoru və etibar sərhədi

Hücum vektoru (attack vector) rəqibin hədəfə çatdığı yol və vasitədir. Hücum səthi (attack surface) istifadə edilə bilən giriş nöqtələrinin məcmusudur: açıq VPN, LMS əlavəsi, əməkdaş poçtu, USB girişi, bulud API açarı və server otağının qapısı. Yalnız İnternetdən görünən portları saymaq daxili və fiziki yolları kənarda qoyur.

Etibar sərhədi müxtəlif təhlükəsizlik fərziyyələri olan zonaları ayırır. Yataqxana cihazının idarəetmə serverinə birbaşa çata bilməsi sərhədin zəif qurulduğunu göstərir. İstifadəçi autentifikasiya keçsə də, bütün universitet resurslarına etibar qazanmır: hər sorğunun obyekti və tələb olunan əməliyyatı ayrıca yoxlanmalıdır.

Vektor təhlili addım-addım aparılır: aktiv seçilir, ona çatan interfeyslər müəyyən edilir, həmin interfeyslərdə kimlik və giriş yoxlamaları nəzərdən keçirilir, uğurlu girişdən sonra mümkün keçidlər araşdırılır. Şərti `lms.unec.example` üçün bu, veb girişindən başlayıb tətbiqin verilənlər bazası hesabına və ehtiyat nüsxə anbarına qədər davam edir. Görünməyən xidmət asılılığı da hücum yolunun hissəsidir.

## Sosial mühəndislik və hesab hücumları

### İnsan, proses və aldadıcı ssenari

Sosial mühəndislik (social engineering) insanın etibarından, tələskənliyindən və ya təşkilati qaydanı yanlış anlamasından istifadə edərək məlumat və ya əməliyyat əldə etməkdir. İnsan həmişə ən zəif halqa deyil: işçi fişinqi ilk aşkar edən ola bilər, düzgün layihələndirilməmiş parol bərpası isə təcrübəli işçini də aldada bilər.

Aldadıcı məktubun gücü texniki mürəkkəblikdən gəlmir: hücumçu qeydiyyat tarixini açıq təqvimdən öyrənib həmin gün "hesabınız bağlanacaq" göndərir, tələbə mövcud problemə uyğun izah gördüyü üçün keçidi açır. Qrammatik düzgünlük etibar sübutu deyil; əsas yoxlama tələb olunan əməliyyatın və ünvanın universitetin həqiqi prosesi ilə uyğunluğudur.

| Forma | Mexanizm | Şərti universitet nümunəsi |
| --- | --- | --- |
| Fişinq (phishing) | Kütləvi saxta məktub və keçid | Bütün tələbələrə saxta kvota xəbərdarlığı |
| Hədəfli fişinq (spear phishing) | Şəxsə uyğun məlumatla inandırma | Kafedra əməkdaşına saxta məqalə rəyi |
| Rəhbərə yönəlmiş fişinq (whaling) | Yüksək səlahiyyətli şəxsi hədəfləmə | Rektorluğa saxta müqavilə sənədi |
| Vişinq (vishing) | Telefonla aldatma | Özünü texniki dəstək kimi təqdim etmə |
| Smişinq (smishing) | SMS ilə aldatma | Saxta yataqxana ödəniş keçidi |
| QR fişinqi (quishing) | QR kodla gizlənən ünvan | Elan üzərinə saxta qeydiyyat kodu yapışdırma |
| BEC (Business Email Compromise) | İşgüzar yazışmadan ödəniş və ya məlumat üçün sui-istifadə | Tədarükçünün bank hesabını dəyişmək tələbi |
| Uydurma bəhanə (pretexting) | İnandırıcı rol və hadisə qurma | "Audit gedir, giriş kodunu deyin" zəngi |
| Arxadan keçmə (tailgating) | Səlahiyyətli şəxslə qapıdan keçmə | Kartı olmayan şəxsin server otağına daxil olması |
| Cəlbedici yem (baiting) | Maraq doğuran obyekt təklif etmə | Tapılmış USB-də "təqaüd siyahısı" faylı |

BEC üçün zərərli əlavə və ya texniki istismar şərt deyil. Ələ keçirilmiş real poçt hesabından yazılmış ödəniş tələbi poçt autentifikasiyası yoxlamalarından keçə bilər. Maliyyə şöbəsi hesab rekvizitinin dəyişməsini əvvəldən qeydə alınmış nömrə ilə ayrıca təsdiqləməlidir; məktubda verilən nömrəyə zəng eyni saxta ssenarini davam etdirə bilər.

Süni yaradılmış səs və video (deepfake) rəhbərin danışığını təqlid edə bilər. Ekrandakı tanış üz və səs ödəniş səlahiyyətinin sübutu deyil; iki nəfərin təsdiqi, əvvəlcədən müəyyən edilmiş əlaqə kanalı və əməliyyat limitləri daha etibarlıdır. Təlim eyni qaydanı möhkəmləndirməlidir: işçi səhvi gizlətmədən tez bildirə bilməlidir, cəzalandırıcı fişinq sınaqları bildiriş verməyi azalda bilər.

### Parol, sessiya və MFA hücumları

| Hücum | Mexanizm |
| --- | --- |
| Kobud güc (brute force) | Çoxlu namizəd parolun sınanması |
| Lüğət hücumu | Daha ehtimallı söz və variantların seçilməsi |
| Parol püskürtməsi (password spraying) | Az sayda parolun çoxlu hesaba yayılması |
| Sızmış hesab cütlərinin sınanması (credential stuffing) | Başqa xidmətdən əldə edilmiş istifadəçi adı və parol cütlərindən istifadə |

Aşkarlama üçün hesab üzrə cəhdlərlə yanaşı mənbə üzrə fərqli hesablar da sayılmalıdır. Şərti nümunə: bir mənbədən 60 tələbə hesabının hər birinə bir uğursuz giriş gəlir. Hər hesab üçün beş cəhd həddi işləməz; mənbə, cihaz xüsusiyyətləri, vaxt və hədəf hesablar birlikdə baxıldıqda püskürtmə ehtimalı yaranır. Paylanmış hücumda IP-lər də dəyişə bilər; yalnız IP həddi ilə müdafiə universitetin ortaq NAT ünvanını bloklaya və hücumçunu buraxa bilər.

Çoxfaktorlu autentifikasiya (Multi-Factor Authentication, MFA) müxtəlif faktor kateqoriyalarını birləşdirir. Parol və PIN hər ikisi bilik faktorudur. Təhlükəsizlik açarı sahiblik, biometrik xüsusiyyət insanın özünə aid faktordur. Kriptoqrafik açar öz-özlüyündə əzbər parol sayılmır. Barmaq izi bir çox qurğuda yerli açarı serverə göndərilmədən açır; biometrika dəyişdirilməsi çətin məlumatdır və məxfilik tələb edir.

MFA yorğunluğunda hücumçu təkrar təsdiq bildirişləri göndərərək istifadəçinin birini qəbul etməsinə çalışır. Aralıq proksi ilə fişinq sessiya tokenini də oğurlaya bilər. Domenə bağlanan FIDO2/WebAuthn əsaslı autentifikasiya fişinqə daha davamlıdır, amma cihazın və bərpa yolunun qorunmasını əvəz etmir. Parol dəyişəndə əvvəldən açılmış sessiyanın avtomatik bağlanacağı da fərz edilməməlidir.

NIST SP 800-63-4 2025-ci ilin iyulunda yekunlaşıb və əvvəlki 800-63-3 sənədini əvəz edir. Bu ailənin autentifikasiya tövsiyələrinə görə əsas istiqamət uzun, unikal parollar, sızmış parolların yoxlanması və cəhdlərin məhdudlaşdırılmasıdır. Pozuntu əlaməti olmadan təqvim üzrə məcburi parol dəyişikliyi və qarışıq simvol tələbi etibarlılığın ümumi zəmanəti deyil. Universitet parol meneceri, MFA və qorunan bərpa prosesi ilə istifadəçinin yükünü azaltmalıdır.

## Şəbəkə hücumları və xidmətdən imtina

### Dinləmə, saxtalaşdırma və aralıq müdaxilə

**Trafikin dinlənməsi (sniffing)** paketlərin müşahidəsi və təhlilidir. Şifrələnməmiş protokolda parol və məzmun açıla bilər. Kommutatorlu şəbəkədə hər cihaz bütün trafiki avtomatik görmür; görünürlük bağlantı yerindən və sazlamadan asılıdır. Güzgü portu, ələ keçirilmiş şəbəkə qurğusu və ya aralıq müdaxilə müşahidə sahəsini genişləndirə bilər.

**Saxtalaşdırma (spoofing)** müxtəlif səviyyələrdə mümkündür:

- IP saxtalaşdırması: paketə başqa mənbə ünvanı yazılır, lakin cavabı almaq və tam TCP sessiyası qurmaq imkanı verməyə bilər.
- ARP saxtalaşdırması: yerli IPv4 seqmentində yanlış IP–MAC uyğunluğu yayılır.
- DNS cavabının saxtalaşdırılması: istifadəçi səhv ünvana yönələ bilər.

Hamısını "IP dəyişmək" kimi izah etmək mexanizmi gizlədir.

**Aralıq hücumda (Man-in-the-Middle, MITM; on-path attack)** rəqib iki tərəf arasında yerləşərək rabitəni izləyir və bəzən dəyişir. Şərti yataqxana nümunəsində saxta giriş nöqtəsi həqiqi Wi-Fi adını təqlid edir, cihaz qoşulduqda trafik hücumçunun idarə etdiyi şəbəkədən keçir. Düzgün yoxlanan TLS sertifikatı veb məzmununu qoruyur, amma istifadəçi sertifikat xəbərdarlığını keçərsə bu yoxlama zəifləyir. VPN də əvvəlcədən etibarlı qurulmalıdır.

| Hücum və ya risk | Uyğun tədbir | Tədbirin sərhədi |
| --- | --- | --- |
| Şifrələnməmiş trafik | TLS və qorunan uzaq giriş | Son qurğu ələ keçirilibsə məzmun yenə açıla bilər |
| Yerli ARP saxtalaşdırması | Seqmentləşdirmə, uyğun ARP yoxlaması | Qurğunun dəstəyi və düzgün etibar portları tələb olunur |
| Saxta Wi-Fi | İdarə olunan profil, server sertifikatının yoxlanması | İstifadəçinin yoxlamanı keçməsinə icazə verilməməlidir |
| Mənbə IP saxtalaşdırması | Giriş və çıxış trafikinin ünvan üzrə süzülməsi | Bütün İnternetdə eyni nəzarət yoxdur |
| DNS manipulyasiyası | Etibarlı resolver, uyğun DNSSEC yoxlaması | DNSSEC məzmunu şifrələmir və bütün zonalar imzalanmayıb |

TLS bağlantısının olması veb xidmətin təhlükəsiz proqramlaşdırıldığını göstərmir. Hücumçu öz domeni üçün etibarlı sertifikat ala bilər: `lms-yardim.example` ünvanında kilid işarəsi həmin domenlə şifrəli rabitəni göstərir, domenin universitetə aid olduğunu təsdiqləmir.

### DoS və DDoS mexanizmləri

Xidmətdən imtina (Denial of Service, DoS) qanuni istifadəçiyə xidməti əlçatmaz etməyə yönəlir. Paylanmış xidmətdən imtina (Distributed Denial of Service, DDoS) çoxlu mənbədən aparılır. Botnet idarə olunan yoluxmuş cihazlar şəbəkəsidir, amma DDoS üçün hər mənbənin yoluxmuş olması şərt deyil: açıq xidmətlər əks etdirmədə istifadə edilə bilər.

- **Həcm hücumu**: universitetin xarici rabitə kanalı dolur.
- **Protokol vəziyyətinə yönəlmiş hücum**: qurğunun sessiya cədvəli və ya bağlantı emalı tükənir.
- **Tətbiq səviyyəsi**: az trafiklə bahalı əməliyyat təkrar tələb edilir. Kitabxanada mürəkkəb axtarış sorğusu verilənlər bazasını yükləyirsə, yalnız saniyədə bayt sayına baxan monitor hücumu görməyə bilər.

Əks etdirmədə (reflection) hücumçu sorğunu qurbanın saxtalaşdırılmış mənbə ünvanı ilə üçüncü tərəfə göndərir, cavab qurbana gedir. Cavab sorğudan böyükdürsə, gücləndirmə (amplification) yaranır. Şərti: 100 baytlıq sorğu 2 000 baytlıq cavab doğurursa, həcm nisbəti 20-dir. Protokol, sorğu və cavab dəyişdikcə nisbət də dəyişir; bu, bütün DNS və ya UDP trafiki üçün sabit göstərici deyil.

:::example Kampus firewall-ı niyə kömək etmir
Xarici kanal 1 Gbit/s, gələn hücum axını 3 Gbit/s. Firewall bütün zərərli paketləri atsın deyə sazlanıb, amma qanuni sorğuların bir hissəsi firewall-a çatmamış operatorun xəttində itir. Süzmə operator və ya yuxarı şəbəkə səviyyəsində aparılmalıdır; kampus daxilindəki cihaz artıq dolmuş xarici kanalı boşalda bilmir.
:::

DDoS-a cavab əvvəlcədən razılaşdırılır: operatorla əlaqə, trafik təmizləmə imkanı, xidmətin prioriteti və alternativ xəbər kanalı. Tətbiqdə sürət məhdudiyyəti, keş, sorğu xərci limiti və uyğun WAF qaydaları işlədilir. Bir IP-yə sərt limit yataqxananın ortaq çıxışından gələn qanuni tələbələri də kəsə bilər. CAPTCHA bütün protokol hücumlarını dayandırmır və əlçatanlıq problemi yarada bilər.

İmtahan vaxtı çoxlu qanuni girişlə hücum arasında fərq ölçülməlidir: hesabların çoxu normal autentifikasiya keçir və müxtəlif kurslara baxırsa, tələb artımıdır; eyni bahalı yola təkrar sorğular, qeyri-adi sessiyalar və uğursuz nəticələr başqa izaha işarə edir. Tək göstərici ilə hamını bloklamaq tədrisi dayandıra bilər.

## Veb, zərərli proqram və təchizat zənciri hücumları

### Veb tətbiqində giriş və etibar səhvləri

**SQL inyeksiyasında (SQL injection)** etibarsız giriş sorğunun əmrlərindən ayrılmadığı üçün verilənlər bazası sorğusunun məntiqinə təsir edir. Kitab axtarışında istifadəçi mətnini birbaşa SQL sətrinə birləşdirmək buna şərait yaradır. Parametrli sorğu məlumatı əmrdən ayırır; baza hesabına artıq hüquq verilməməsi isə uğurlu istismarın zərərini məhdudlaşdırır. Aşağıdakı Python nümunəsi SQLite üçün parametrli sorğudur (cədvəl və sahə adları şərtidir). Parametr işarəsi sürücüyə görə dəyişə bilər; girişi əvvəlcədən dırnaqlamaq təhlükəsiz parametr bağlamasının əvəzi deyil.

```python
query = "SELECT title FROM books WHERE author = ?"
rows = connection.execute(query, (author_name,)).fetchall()
```

**Saytlararası skript (Cross-Site Scripting, XSS)** etibarsız məzmunun brauzerdə proqram kimi işlənməsidir. LMS forumunda yazı düzgün kodlaşdırılmadan göstərilərsə, başqa istifadəçinin sessiyası daxilində istənməyən əməliyyat baş verə bilər. Çıxışın göstərildiyi kontekstə uyğun kodlaşdırılması vacibdir: HTML mətni, atribut və JavaScript üçün eyni qayda yetərli deyil. HttpOnly kukini skriptlə oxumağı məhdudlaşdırır, lakin bütün XSS təsirlərini aradan qaldırmır.

| Hücum | Əsas mexanizm | Universitetdə tədbir |
| --- | --- | --- |
| SQL inyeksiyası | Giriş sorğu əmrinə qarışır | Parametrli sorğu və məhdud baza hüquqları |
| XSS | Etibarsız məzmun brauzerdə icra olunur | Kontekstə uyğun kodlaşdırma və uyğun məzmun siyasəti |
| CSRF | Başqa sayt istifadəçinin sessiyası ilə sorğu doğurur | CSRF tokeni, uyğun SameSite sazlaması, mənbə yoxlaması |
| Giriş nəzarətinin pozulması | Obyektə icazə serverdə yoxlanmır | Hər sorğuda hesab və obyekt hüququnu yoxlamaq |
| SSRF | Server istifadəçi təsirli ünvana sorğu edir | Çıxışları məhdudlaşdırmaq, ünvan və yönləndirmələri yoxlamaq |
| Fayl yükləmə sui-istifadəsi | Yüklənmiş fayl icra və ya zərərli emal doğurur | İcradan ayrı saxlama, tip və ölçü yoxlaması |

CSRF (Cross-Site Request Forgery) zamanı hücumçu brauzerin hədəfə uyğun sessiya məlumatını avtomatik göndərməsindən istifadə edir. SSRF (Server-Side Request Forgery) zamanı isə sorğunu server göndərir. Portalda "URL-dən şəkil gətir" funksiyası daxili idarəetmə ünvanlarına çata bilirsə, SSRF üçün yol yaranır. Birinci halda sui-istifadə obyekti brauzerin sessiyası, ikincidə serverin şəbəkə çıxışıdır.

Obyekt identifikatorunu dəyişməklə başqa tələbənin sənədinin açılması ayrıca izah tələb edir: istifadəçi sistemə uğurla daxil olub, amma sənəd ona aid deyil. Problem autentifikasiyada yox, avtorizasiyadadır. OWASP Top 10:2025-də A01 Broken Access Control bu risk sinfini əhatə edir. Təsadüfi identifikator hücumçunun təxminini çətinləşdirə bilər, serverdə hüquq yoxlamasını əvəz etmir.

### Zərərli proqram, fidyə və təchizat zənciri

Virus adətən başqa fayl və ya daşıyıcı ilə yayılmağa bağlanır; soxulcan (worm) şəbəkə vasitəsilə özünü yayma qabiliyyətinə malikdir. Troyan (Trojan) faydalı proqram görüntüsü altında zərərli funksiya daşıyır. Casus proqram məlumat toplayır, açarbasma qeydedicisi daxil edilən simvolları izləyir. Kateqoriyalar kəsişə bilər: eyni proqram həm parol oğurlaya, həm modul endirə bilər.

Fidyə proqramı (ransomware) məlumatı və ya xidməti əlçatmaz etməklə ödəniş tələb edə bilər. Məlumatın əvvəlcədən çıxarılıb yayılmaqla hədələnməsi bərpa nüsxəsi olan universitetə də zərər verir: ehtiyat nüsxə məxfilik pozuntusunu geri qaytarmır. Nüsxə əsas sistemlə eyni administrator hesabına bağlıdırsa, hücumçu onu da silə bilər. Bərpa sınağı və ayrıca qorunan nüsxələr buna görə tələb olunur.

Təchizat zənciri hücumunda (supply chain attack) etibar edilən təchizatçı, proqram asılılığı, qurma prosesi və ya yeniləmə kanalı vasitə olur. Şərti: universitet kitabxana əlavəsini rəsmi kanaldan quraşdırır, lakin həmin kanalın hesabı ələ keçirilib. Paketdə rəqəmsal imza olması zərərli funksiyanın olmadığını göstərmir: imza açarı və ya qanuni qurma prosesi sui-istifadə oluna bilər. OWASP Top 10:2025-də A03 Software Supply Chain Failures bu sahəyə aiddir. Konspektdə nümunə kimi SolarWinds (2020) və 3CX (2023) hallarının adı çəkilir.

Müdafiə: asılılıqlar inventarı, proqram komponentləri siyahısı (Software Bill of Materials, SBOM), təsdiqlənmiş paket mənbələri, qurma hesablarının qorunması və yeniləmənin mərhələli sınağı. SBOM komponentin mövcudluğunu göstərə bilər; həmin komponentin işlədilən funksiyasının istismar oluna bildiyini ayrıca yoxlamaq lazımdır. Təchizatçıdan gələn xəbərdarlıq yerli inventarla tutuşdurulmasa, universitet öz riskini müəyyən edə bilməz.

## Zəifliklər və düzəliş prioriteti

### CVE və CWE nəyi adlandırır

CVE (Common Vulnerabilities and Exposures) ictimai məlum zəiflik qeydlərinə identifikator verir. CVE-2021-44228 Apache Log4j ilə bağlı Log4Shell zəifliyinin identifikatorudur. CVE nömrəsi qarışıqlığı azaldır; təhlükə balı və ya universitetdə istismar olunduğunun sübutu deyil. Hər konfiqurasiya səhvinə və hər məlum zəifliyə CVE verilməyə bilər; qeydin vəziyyəti və təsirlənən versiyalar da yoxlanır.

CWE (Common Weakness Enumeration) konkret məhsuldakı hadisədən çox zəiflik **növünü** təsnif edir. CWE-89 SQL inyeksiyası ilə bağlı zəiflik sinfidir; eyni CWE sinfinə müxtəlif məhsullarda çoxlu CVE uyğun gələ bilər. Kafedranın daxili tətbiqində CVE olmasa da CWE tipli proqramlaşdırma səhvi tapıla bilər. CVE düzəlişi izləməyə, CWE isə səhvin təkrarlanma səbəbini öyrənməyə kömək edir.

Sıfırıncı gün zəifliyi (zero-day) açıqlanma və müdafiənin hazırlanması kontekstində işlənir. Mənbələrdə sərhəd fərqlidir: bəzən istehsalçının bilmədiyi zəiflik, bəzən istismar zamanı düzəlişi olmayan zəiflik. Ona görə hesabatda dəqiq vəziyyət yazılmalıdır: "istismar müşahidə ediləndə istehsalçı düzəlişi mövcud deyildi". Universitetin yeniləməni quraşdırmadığı, çoxdan düzəldilmiş zəifliyi zero-day adlandırmaq düzgün deyil.

### CVSS v4.0, EPSS və KEV

CVSS v4.0 (Common Vulnerability Scoring System) zəifliyin texniki ciddiliyini strukturlaşdırır. Dörd göstərici qrupu var: əsas (Base), təhdid (Threat), mühit (Environmental) və əlavə (Supplemental). Əsas qrup hücum yolu, mürəkkəblik, tələb olunan imtiyaz, istifadəçi iştirakı və təsirləri qiymətləndirir; zəif sistemə təsirlə sonrakı sistemlərə təsir ayrıca nəzərə alınır. Əlavə göstəricilər yekun bala təsir etmir.

Bal 0-dan 10-a qədərdir; vektor sətri balın hansı fərziyyələrlə yarandığını göstərir. Şəbəkədən uzaqdan istismar oluna bilən zəiflik ilə yerli imtiyaz tələb edən zəiflik eyni şəraitdə deyil. CVSS-B əsas göstəriciləri, CVSS-BT təhdid göstəricilərini də, CVSS-BE mühit göstəricilərini də əhatə edir; CVSS-BTE hər üçünü birləşdirir. İki bal müqayisə ediləndə versiya və istifadə olunan qruplar bilinməlidir.

EPSS (Exploit Prediction Scoring System) CVE üzrə növbəti 30 gündə istismarın müşahidə olunması ehtimalını modelləşdirir. Şərti 0,20 qiyməti həmin modeldə 20 faiz ehtimaldır; universitet serverinin 20 faiz ehtimalla sındırılacağı demək deyil. Persentil nisbi sıralamadır: 90-cı persentil 90 faiz istismar ehtimalı demək deyil. Qiymət zamanla dəyişir, ona görə hesabatda götürülmə tarixi saxlanılır.

CISA KEV (Known Exploited Vulnerabilities) real istismarı məlum zəifliklərin kataloqudur. Siyahıda olma qərarı sürətləndirən güclü siqnaldır; olmamaq təhlükəsizlik zəmanəti vermir. Kataloqdakı təşkilati icra tarixləri bütün dünya universitetləri üçün avtomatik hüquqi müddət sayılmır: universitet öz düzəliş müddətini qanuni tələblər, müqavilələr və risk əsasında müəyyən edir.

| Göstərici | Cavab verdiyi sual | Cavab vermədiyi sual |
| --- | --- | --- |
| CVE | Hansı konkret ictimai zəiflikdən danışılır? | Universitetdə istismar baş veribmi? |
| CWE | Səhvin ümumi növü nədir? | Hansı məhsul versiyası düzəldilib? |
| CVSS v4.0 | Texniki ciddilik hansı şərtlərlə nə qədərdir? | Bu gün hücum olunma ehtimalı neçədir? |
| EPSS | Yaxın 30 gündə təbiətdə istismar müşahidəsi ehtimalı nədir? | Bu universitetdə insident ehtimalı neçədir? |
| CISA KEV | Real istismarı məlum zəiflik kataloqdadırmı? | Kataloqda yoxdursa istismar mümkünsüzdürmü? |

:::exam
Yalnız CVSS-ə baxmaq səhvdir. Düzgün prioritet üç sualdan çıxır: real istismar olunurmu (KEV, EPSS), sistem İnternetə açıqdırmı, aktiv nə qədər kritikdir. Hər məlum zəifliyin CVE-si olmur.
:::

### Universitet üçün qərarın hesablanması

Prioritet inventarla başlayır: məhsul və versiya həqiqətən varmı, zəif funksiya açıqdırmı, İnternetdən əlçatandırmı, hansı məlumat və hüquqlara çıxış verir? Sonra istismar sübutu, CVSS, EPSS, aktivin dəyəri və müvəqqəti tədbirlər qiymətləndirilir. "Ən böyük balı əvvəl yamaq" qaydası bu əlaqələri itirir.

| Aktiv | CVSS | İstismar məlumatı | Əlçatanlıq | Qərar |
| --- | --- | --- | --- | --- |
| Uzaq giriş şlüzü | 8,1 | KEV-dədir | İnternetə açıq | Təcili düzəliş və kompromitasiya yoxlaması |
| Təcrid edilmiş sınaq VM-i | 9,8 | Məlum yerli sübut yoxdur | Yalnız məhdud sınaq zonası | İzolyasiyanı yoxla, planlı düzəliş et |
| Tələbə bazası tətbiqi | 6,5 | Daxildə istifadə əlaməti var | Əməkdaş şəbəkəsi | İnsident araşdırması və təcili məhdudlaşdırma |

Təcili tədbir mütləq istehsal sistemini birbaşa yeniləmək olmaya bilər: təhlükəli funksiyanı söndürmək, girişi daraltmaq və ya xidməti müvəqqəti ayırmaq mümkündür; kompensasiyaedici tədbirin nəyi kəsdiyi sınaqla təsdiqlənməlidir. Hücumçu artıq daxil olubsa, yamaq əvvəlki sessiyanı, oğurlanmış açarı və əlavə edilmiş hesabı aradan qaldırmır.

Düzəlişdən sonra yalnız paket versiyası kifayət deyil: xidmətin yenilənmiş kodla işlədiyi, yenidən başlatmanın edildiyi və zəif konfiqurasiyanın qalmadığı yoxlanır; LMS-də tələbənin giriş, tapşırıq təqdimetmə və nəticə görmə axınları da sınanır. Dəyişiklik qeydi sübut, məsul şəxs və bağlanma tarixini saxlayır.

## Tədbirlər, siyasət və müdafiə prinsipləri

### İnsan, proses və texnologiyanın əlaqəsi

Müdafiə hüquqi, təşkilati, prosedur və proqram-texniki tədbirləri birləşdirir: hüquqi tədbir məlumatla rəftarın sərhədini, təşkilati tədbir məsuliyyəti, prosedur konkret addımları, texniki vasitə yoxlamanı və məhdudiyyəti müəyyən edir. "Qiyməti yalnız səlahiyyətli şəxs dəyişir" siyasəti varsa, tətbiqdə həmin yoxlama, təsdiq prosesi və audit qeydi də olmalıdır.

İşə qəbulda hesab və rol verilir, vəzifə dəyişəndə hüquqlar yenilənir, işdən çıxanda hesablar, sessiyalar, kartlar və açarlar ləğv olunur. Fiziki mühafizə server otağına girişə, daşıyıcıların uçotuna və avadanlığın təhlükəsiz çıxarılmasına nəzarət edir. İstismarda ehtiyat nüsxələr, texniki xidmət, sənədləşdirmə və tutum planı tələb olunur. Köhnə diskin nəzarətsiz atılması şəbəkə müdafiəsindən yan keçən məlumat sızmasıdır.

İnsidentə cavab komandası sübutu qoruyur, yayılmanı məhdudlaşdırır, səbəbi aradan qaldırır və bərpanı əlaqələndirir. CERT və CSIRT adları bu funksiyanı görən komandalarda işlədilir. Texniki işçilərlə yanaşı rəhbərlik, hüquq və kommunikasiya üzrə əlaqələndiricilər müəyyən edilməlidir; xarici CERT/CSIRT ilə əlaqə kanalları əvvəlcədən təsdiqlənir.

### İdentifikasiya, avtorizasiya və audit

İdentifikasiya subyektin özünü adlandırmasıdır; autentifikasiya bu iddianın yoxlanmasıdır; avtorizasiya yoxlanmış subyektə hansı əməliyyatın icazəli olduğunu müəyyən edir. Elektron pasport və biometrik sistem şəxsiyyət yoxlamasında istifadə oluna bilər, lakin avtomatik LMS administratoru hüququ vermir. Universitet identifikasiya məlumatının hansı məqsədlə toplandığını və kimə açıldığını ayrıca müəyyən etməlidir.

| Subyekt | Öz nəticəsi | Başqa tələbənin nəticəsi | Qiymət dəyişikliyi |
| --- | --- | --- | --- |
| Tələbə | Oxuma | Qadağa | Qadağa |
| Kurs üzrə səlahiyyətli əməkdaş | İş üçün uyğun məlumat | Yalnız təyin olunmuş kurs | Təsdiqlənmiş proseslə |
| Texniki administrator | Standart qaydada ehtiyac yoxdur | Fövqəladə giriş ayrıca qeydə alınır | Akademik səlahiyyət vermir |
| Audit əməkdaşı | Yoxlama çərçivəsində oxuma | Yoxlama çərçivəsində oxuma | Qadağa |

Jurnallaşdırma hadisənin yazılması, audit isə qeydlərin və nəzarətin məqsədə uyğun yoxlanmasıdır. Uğurlu və uğursuz girişlər, çıxışlar, uzaq müraciətlər, həssas fayl əməliyyatları və imtiyaz dəyişiklikləri seçilmiş məqsədlə toplanır. Vaxt, subyekt, obyekt, əməliyyat və nəticə hadisəni bərpa etməyə kömək edir. Parol və sessiya tokeni jurnala yazılmamalıdır; qeydlərin özünə də giriş və tamlıq nəzarəti qoyulur.

Firewall şəbəkələr və zonalar arasındakı trafiki qaydalarla məhdudlaşdırır: şəbəkə və nəqliyyat səviyyəsində ünvan, port və sessiya vəziyyəti, tətbiq səviyyəsində protokol xüsusiyyətləri yoxlana bilər. Şifrəli trafikdə görünürlük yerləşdirmədən asılıdır. Antivirus və EDR fayl, proses və davranışı yoxlayır; poçt süzgəci spam və zərərli məzmunu azaldır. Heç biri düzgün giriş nəzarəti və yeniləməni əvəz etmir.

Şifrələmə məzmunu açarsız oxunmaz edir: simmetrik üsul eyni gizli açarla, asimmetrik üsul əlaqəli açıq və gizli açarlarla işləyir. Rəqəmsal imza mənşə və tamlığı yoxlayır, faylı məxfi etmir. Steqanoqrafiya məlumatın mövcudluğunu gizlətməyə çalışır; şəkildə gizlənmiş mətn ayrıca şifrələnməyibsə, tapıldıqdan sonra oxuna bilər. "Süni intellekt şifrələməsi" standart kriptoqrafik sinif deyil.

### Qanunvericilik və standartların yeri

Universitetin məlumatla rəftarı hüquq və azadlıqlara, şəxsi həyatın qorunmasına və qanuni məqsədə uyğun olmalıdır. Azərbaycan Respublikasının "İnformasiya, informasiyalaşdırma və informasiyanın mühafizəsi haqqında", "Fərdi məlumatlar haqqında", "İnformasiya əldə etmək haqqında" və "Elektron imza və elektron sənəd haqqında" qanunları bu mövzuda istinad edilən aktlardır. "Dövlət sirri haqqında", "Kommersiya sirri haqqında" və "Biometrik informasiya haqqında" qanunların tətbiqi işlənən məlumatdan və fəaliyyətdən asılıdır. Konkret öhdəlik üçün qüvvədə olan mətn əsas götürülür.

Bu çərçivə monitorinqin sərhədini də müəyyən edir: yataqxana şəbəkəsinin təhlükəsizliyi üçün hər şəxsin bütün yazışmasını toplamaq avtomatik əsaslı sayılmır. Məqsəd, zəruri sahələr, saxlanma müddəti, giriş səlahiyyəti və silinmə yazılı müəyyən edilir. Təhdid kəşfiyyatı adı icazəsiz girişə və ya sərhədsiz şəxsi məlumat toplamağa icazə vermir.

| Sənəd | Əsas istiqamət | Universitetdə istifadə |
| --- | --- | --- |
| ISO/IEC 27001:2022 | İnformasiya təhlükəsizliyinin idarə edilməsi sisteminə tələblər | Məsuliyyət, risk və davamlı yoxlama |
| ISO/IEC 27002:2022 | 93 tədbir üzrə tövsiyələr, dörd mövzu qrupu | Təşkilati, insan, fiziki və texnoloji tədbirlər |
| ISO/IEC 27005:2022 | İnformasiya təhlükəsizliyi risklərinin idarəsi | Aktiv, ssenari və qalıq risk təhlili |
| NIST CSF 2.0, 2024 | Govern, Identify, Protect, Detect, Respond, Recover | İdarəetmədən bərpaya qədər nəticələrin planı |
| NIST SP 800-61 Rev. 3, 2025 | İnsidentə cavabın risk idarəsinə bağlanması | Hazırlıq, aşkarlama, cavab və bərpa əlaqəsi |
| CIS Controls v8.1 | Prioritet müdafiə tədbirləri | İnventar, konfiqurasiya və hesab nəzarəti |
| ISO/IEC 15408 | Məhsulun təhlükəsizlik qiymətləndirilməsi | Satınalmada qiymətləndirmə sərhədini anlamaq |

1985-ci ilin Trusted Computer System Evaluation Criteria (TCSEC) sənədi "Narıncı kitab" adı ilə tanınır. Tarixi D, C, B və A bölgüləri məhdud müdafiədən ixtiyari və mandatlı giriş nəzarətinə, sonra yoxlanmış layihələndirməyə doğru tələbləri göstərirdi. Bu bölgülər cari universitet şəbəkəsi üçün tam təhlükəsizlik ölçüsü deyil. Onu bütün informasiya təhlükəsizliyi standartlarının başlanğıcı və ya bugünkü universal sertifikatlaşdırma üsulu adlandırmaq dəqiq olmaz.

Common Criteria (Ümumi meyarlar) funksional tələbləri və zəmanət tələblərini ayırır: funksional tələb məhsulun nə etməli olduğunu, zəmanət tələbi isə bu iddiaya niyə etibar edilə biləcəyini soruşur. Klassik funksional siniflər:

| Sinif | Sahə |
| --- | --- |
| FAU | audit |
| FIA | identifikasiya və autentifikasiya |
| FRU | resurs istifadəsi |
| FCO | rabitədə imtinanın qarşısı |
| FPR | məxfilik |
| FDP | istifadəçi məlumatının mühafizəsi |
| FPT | təhlükəsizlik funksiyalarının mühafizəsi |
| FCS | kriptoqrafik dəstək |
| FMT | idarəetmə |
| FTA | giriş |
| FTP | etibarlı kanal |

Ailə və komponent sayları nəşrdən asılıdır. Qiymətləndirmə konkret məhsula, versiyaya, funksiyaya və fərziyyələrə aiddir; bütöv universitetin təhlükəsizliyini təsdiqləmir.

### Siyasət və müdafiənin qurulma prinsipləri

Təhlükəsizlik siyasəti nəyin qorunduğunu, kimlərin məsul olduğunu, hansı riskin qəbul edilə biləcəyini və qaydaların necə yoxlanacağını müəyyən edir. Yuxarı səviyyədə rəhbərliyin məqsəd və risk qərarları, orta səviyyədə LMS, poçt və uzaq giriş üzrə qaydalar, aşağı səviyyədə konkret sazlamalar və əməliyyat təlimatları olur. Siyasəti rəhbərlik təsdiqləyir, aidiyyəti şəxslərə çatdırır və dəyişiklik olduqda yeniləyir.

| Prinsip | Mənası |
| --- | --- |
| Sadəlik | İstifadəçi qaydanı başa düşür və düzgün əməliyyatı asan seçir |
| Sistemlilik | Məlumat, hesab, şəbəkə və insan əlaqələri birlikdə qiymətləndirilir |
| Komplekslik və dərinlik üzrə müdafiə | Müxtəlif qatlar bir-birini tamamlayır: poçt süzgəci keçilsə, EDR, seqmentləşdirmə və audit yenə işləməlidir. Bütün qatlar eyni hesabdan idarə olunursa, müstəqillik zəifləyir |
| Fasiləsizlik | Layihələndirmədən istismara, dəyişiklikdən istismardan çıxarmaya qədər nəzarət davam edir; heç vaxt insident olmayacağı vədi deyil |
| Düşünülmüş kafilik | Tədbirin xərci, istifadə çətinliyi və mümkün zərər müqayisə edilir. Hücumçunun xərcini artırmaq faydalıdır, amma dövlət dəstəkli rəqib üçün sadə mənfəət hesabı yetərli olmaya bilər |
| Uyğunlaşma | Dəyişən təhdidə görə qaydanı yeniləmək |
| Mexanizmin açıqlığı | Alqoritm məlum olsa da, açar və səlahiyyətlər qorunduqda müdafiə işlək qalır |

## Təhdid kəşfiyyatı və qərarın səviyyəsi

### Müşahidədən biliyə

Kibertəhdid kəşfiyyatı (Cyber Threat Intelligence, CTI) rəqib, onun məqsədi, imkanları, infrastrukturu və davranışı barədə yoxlanmış, kontekstləşdirilmiş və qərara yarayan bilikdir. Xam məlumatın çoxluğu kəşfiyyat deyil. "198.51.100.24 ünvanından bağlantı gəldi" müşahidədir. "Bu bağlantı əvvəl təsdiqlənmiş zərərli domenlə əlaqəlidir, kitabxana serverində həmin vaxt naməlum proses başlayıb, serverin ayrılması araşdırılmalıdır" isə sübuta bağlı analitik nəticədir (ünvan və hadisə şərtidir).

:::note Köhnə slaydlarla fərq: kəşfiyyatın tərifi
Mühazirə slaydında kəşfiyyat "onlayn məlumatların toplanması və təhlili" kimi verilib; bu dar tərifdir. Kəşfiyyat həm də daxili mənbələrdən gəlir: öz loglarımız, insident araşdırmaları, zərərli proqram analizi və tərəfdaşlarla etibarlı mübadilə (NIST SP 800-150). O, yalnız qarşısını almaq üçün yox, aşkarlama və insidentə cavab üçün də işlədilir.
:::

Mənbə yalnız İnternet deyil: giriş jurnalları, poçt şlüzü, insident araşdırması, zərərli proqram analizi və tərəfdaşdan məhdud paylaşılmış xəbərdarlıq da mənbədir. Məhsul hücumu önləmək, aşkarlamaq, araşdırmanı yönəltmək və bərpada təkrar yoluxmanı azaltmaq üçün işlədilir. Heç bir analitik qrup bütün gələcək hücumları əvvəlcədən bilmir.

Faydalı nəticə konkret sualı cavablandırır. Rəhbərliyin "kitabxananın buluda köçürülməsində hansı təhdidlərə hazırlaşaq?" sualı ilə növbətçi analitikin "bu domenə bağlantı edən cihazı ayıraqmı?" sualı eyni məhsulla həll edilmir: birincidə asılılıq, məlumatın dəyəri və investisiya, ikincidə vaxt, indikatorun etibarı və yerli sübutlar lazımdır.

### Dörd kəşfiyyat səviyyəsi

| Səviyyə | Məzmun | Kimin üçün | Nümunə |
| --- | --- | --- | --- |
| Strateji | Uzunmüddətli trendlər, geosiyasət, sektor üzrə risklər; texniki detal azdır | Rəhbərlik, direktorlar şurası | "Regionda universitet və tədqiqat mərkəzlərinə dövlət dəstəkli hücumlar artıb, təhlükəsizlik büdcəsini artırmaq lazımdır" |
| Əməliyyat | Konkret kampaniya: kim, nə vaxt, kimə qarşı, hansı məqsədlə | İnsidentə cavab komandası, təhdid ovçuları | "Qış sessiyası ərəfəsində tələbələrə saxta 'imtahan nəticələri' fişinqi planlaşdırılır" |
| Taktiki | Hücumçunun TTP-ləri: taktika, texnika, prosedur; müdafiə qaydasına bağlanır | SOC rəhbəri, müdafiə arxitektorları | "Qrup müəllimlərə saxta konfrans dəvəti göndərir, sonra PowerShell işlədir" |
| Texniki | IoC-lər: IP, domen, URL, fayl heşləri, imzalar; maşınla tutuşdurulur, tez köhnəlir | SOC analitikləri, firewall, SIEM, EDR | "Bu 15 IP və 3 SHA-256 heşi bloklayın" |

Bölgü auditoriya və qərar əsasında qurulur. Eyni şərti kampaniyadan dörd məhsul çıxır: strateji (rektorluq və İT rəhbəri; MFA və seqmentləşdirməyə resurs ayırmaq), əməliyyat (CSIRT və növbətçi heyət; əhatəni və cavab hazırlığını müəyyən etmək), taktiki (aşkarlama mühəndisi; poçtdan sonra skript və kənar əlaqə ardıcıllığı üçün davranış qaydası), texniki (SOC və müdafiə sistemləri; domen, URL, heş, vaxt və etibar sahələri, uyğunluğu axtarmaq, əsaslı halda bloklamaq).

:::exam
Mənbələr "taktiki" və "texniki" kəşfiyyatı fərqli təsvir edir: bəzi sertifikat proqramlarında (məs. CompTIA) IoC-lər "taktiki" sayılır. İmtahanda müəllimin bölgüsünü işlət: **taktiki = TTP, texniki = IoC**. Ən etibarlı açar auditoriyadır: rəhbər üçün olan strateji, maşına yüklənən texnikidir.
:::

İdarəetmənin strateji, taktiki və operativ səviyyələri ilə CTI-nin dörd səviyyəsi qarışdırılmamalıdır: idarəetmə səviyyəsi qərarın təşkilati yerini, CTI səviyyəsi məhsulun məzmununu və istifadə formasını təsvir edir. SOC rəhbəri strateji hesabatdan da istifadə edə bilər; səviyyə sənədin məcburi ünvan siyahısı deyil.

## Kəşfiyyatın həyat dövrü

### Tələblər, toplama və emal

Dövr tələblərin müəyyən edilməsindən başlayır. Prioritet kəşfiyyat tələbi (Priority Intelligence Requirement, PIR) qərar üçün hansı biliyin çatışmadığını ifadə edir. "Bütün hücumları izləmək" yoxlanıla bilən tələb deyil; "Semestr qeydiyyatı zamanı tələbə hesablarının ələ keçirilməsində hansı giriş yolları bizim mühitdə işləyə bilər?" daha məqsədyönlüdür. Alıcı, qərarın vaxtı və istifadə ediləcək tədbir əvvəlcədən yazılır.

Toplama planı hər sualın mənbəyini müəyyən edir: hesab oğurluğu üçün poçt şlüzü və identifikasiya platforması, kənar idarəetmə üçün DNS və proksi, yerli icra üçün son qurğu qeydləri. Mənbənin niyə lazım olduğu izah edilə bilmirsə, onu toplamağın xərc və məxfilik təsiri yenidən qiymətləndirilir.

Emal mərhələsində formatlar uyğunlaşdırılır, dublikatlar müəyyən edilir, vaxtlar vahidləşdirilir və obyektlər ayrılır. Domen adı, IP və URL eyni obyekt deyil; bütün URL-ləri yalnız domenə endirmək konkret zərərli yolu itirə bilər. Üç platformanın eyni hesabatdan götürdüyü indikator üç müstəqil təsdiq sayılmır.

:::figure
src = "m02-1.png"
alt = "Kəşfiyyatın həyat dövrünün altı mərhələsi və əks-əlaqə oxu."
caption = "Kəşfiyyatın həyat dövrü. Əks-əlaqə tələblərin yenilənməsinə qayıdır."
:::

### Təhlil, yayma və əks-əlaqə

Təhlil müşahidələrdən əsaslandırılmış nəticə çıxarır: nə baş verdi, hansı izahlar mümkündür, universitet üçün hansı qərar lazımdır. Mənbənin etibarlılığı ilə konkret məlumatın doğruluğu ayrı qiymətləndirilir: etibarlı tərəfdaş səhv edə bilər, az tanınan mənbənin müşahidəsi texniki sübutla təsdiqlənə bilər.

Şərti nümunə: bir domen haqqında xarici xəbərdarlıq gəlib, daxili DNS-də uyğunluq tapılıb. Bu, cihazın domeni soruşduğunu göstərir. Sonra proksi qeydi bağlantının baş tutmadığını göstərir. Deməli, "kompüter yoluxub" nəticəsi erkəndir. Məktubun avtomatik keçid yoxlayıcısı, istifadəçi klikləməsi və zərərli proses alternativ izahlardır; EDR və poçt qeydləri bu fərziyyələri ayırmağa kömək edir.

Yayma alıcıya uyğun formada aparılır: rəhbərliyə təsir, seçim və qeyri-müəyyənlik; SOC-a indikator, şərt, mənbə və araşdırma addımları. Məhsulun hazırlanma vaxtı ilə müşahidənin vaxtı ayrı göstərilir: "bu gün yayımlandı" məlumatın bu gün müşahidə edildiyini bildirmir. Müddəti keçmiş indikator yenilənmiş hesabatın içində də qala bilər.

| Sahə | Məzmun | Şərti nümunə |
| --- | --- | --- |
| Sual və əhatə | Nə araşdırılır, nə daxil deyil? | LMS hesablarına yönəlmiş məktublar |
| Müşahidə | Birbaşa qeydə alınmış fakt | Poçt şlüzündə saxta giriş keçidi |
| Qiymətləndirmə | Sübuta əsaslanan izah | Hesab oğurluğu cəhdi ehtimalı |
| Etibar dərəcəsi | Sübutun gücü və boşluqlar | Orta, son qurğu qeydləri çatışmır |
| Tədbir | Kim nə etməlidir? | SOC sessiya və cihazları yoxlayır |
| Vaxt və paylaşma | Aktuallıq və yayma sərhədi | Yenidən baxılma vaxtı, TLP etiketi |

Etibar dərəcəsi ilə ehtimal ayrı anlayışlardır. Hadisənin baş verməsini yüksək ehtimallı saymaq olar, amma mənbələrin zəifliyinə görə bu qiymətləndirməyə etibar aşağı ola bilər; "yüksək etibar" gələcək hadisənin mütləq baş verəcəyi demək deyil. Hesabat bunları bir qeyri-müəyyən "risk yüksəkdir" cümləsinə sıxışdırmamalıdır.

Əks-əlaqədə alıcıdan konkret nəticə alınır: məlumat hansı qərarı dəyişdi, tədbir işlədimi, yanlış müsbət nə qədər oldu, hansı sahə çatmadı? Kitabxananı bloklayan köhnə IP aşkarlanıbsa, yalnız IP silinmir, etibarlılıq müddəti və bloklama prosesi də düzəldilir. Dövr həmin düzəlişlə növbəti tələblərə qayıdır.

## IoC, IoA, TTP və davranışın təsviri

### İndikatorun mənası və ömrü

Kompromitasiya indikatoru (Indicator of Compromise, IoC) zərərli fəaliyyət və ya mümkün kompromitasiya ilə əlaqəli texniki əlamətdir: fayl heşi, domen, IP, reyestr yolu, sertifikat xüsusiyyəti, C2 serverinin IP-si. Sadə müşahidə olunan obyekt hələ zərərli indikator deyil: IP-yə zərərli kontekst və aşkarlama şərti əlavə edilməlidir. Uyğunluq araşdırmaya başlanğıc verir, uğurlu sındırılmanı təkbaşına sübut etmir.

Hücum indikatoru (Indicator of Attack, IoA) davranışın və niyyətə uyğun ardıcıllığın əlamətidir: məsələn, ofis sənədindən skript interpretatorunun başlaması, ardınca xarici ünvana əlaqə və avtomatik başlanğıc mexanizminin əlavə edilməsi. Bu termin üçün bütün platformalarda eyni sərhəd yoxdur; universitet öz qayda sənədində hansı hadisələri və əlaqəni nəzərdə tutduğunu açıq yazmalıdır.

TTP (Tactics, Techniques and Procedures) taktika, texnika və prosedurlardır. Taktika məqsədi, texnika üsulu, prosedur konkret icra formasını göstərir: "ilkin giriş əldə etmək" məqsəd, "fişinqdən istifadə etmək" texnika, "saxta konfrans səhifəsinə aparan məktub göndərmək" prosedur. Eyni texnika müxtəlif domen və proqramlarla icra edilə bilər.

| Təsvir | Şərti nümunə | Güclü cəhət | Məhdudiyyət |
| --- | --- | --- | --- |
| IoC | `konfrans-giris.example` domeni | Sadə və sürətli tutuşdurma | Domen dəyişə və ya köhnələ bilər |
| IoA | Sənəd, skript və xarici əlaqə ardıcıllığı | Dəyişən ünvanlara davamlılıq | Qanuni avtomatlaşdırma ilə qarışa bilər |
| TTP | Fişinqdən sonra oğurlanmış hesabdan istifadə | Davranışı ümumiləşdirmək | Keyfiyyətli xəritələmə və görünürlük tələb edir |

İndikatorla ilk və son müşahidə vaxtı, mənbə, etibar, əlaqəli kampaniya və yenidən baxılma vaxtı saxlanılır. IP-lər başqa istifadəçiyə keçə bilər: paylaşılan bulud ünvanının bütövlükdə bloklanması onlayn kitabxananı da kəsə bilər; dar domen və URL qaydası və ya yalnız monitorinq bəzən daha uyğundur. Heş uzun müddət eyni faylı tanıya bilər, amma hücumçu başqa fayl göndərə bilər.

### Ağrı piramidası

David Bianco-nun 2013-cü ildə təqdim etdiyi Ağrı piramidası (Pyramid of Pain) müdafiənin müxtəlif əlamətlərə söykənəndə hücumçuya yaratdığı dəyişiklik xərcini göstərir. Aşağıdan yuxarı: heş dəyərləri, IP ünvanları, domen adları, şəbəkə və host artefaktları, alətlər, TTP-lər. Model statistik qanun və ya istənilən mühit üçün dəqiq qiymət cədvəli deyil.

:::figure
src = "m02-2.png"
alt = "Ağrı piramidası: aşağıdan yuxarı heş, IP, domen, artefakt, alət, TTP."
caption = "Ağrı piramidası. Yuxarı səviyyələrdə aşkarlama hücumçunun iş üsulunu dəyişməsini tələb edə bilər."
:::

- **Aşağıda**: heşi dəyişmək üçün faylda bir bayt (mənasız dəyişiklik) kifayət edə bilər, IP-ni bir dəqiqəyə dəyişmək olur. Bu IoC-ləri bloklamaq ucuzdur, amma hücumçunu dayandırmır.
- **Yuxarıda**: hücumçunun alətlərini və davranışını (məs. "Word sənədi PowerShell başladır") aşkarlamaq çətindir, amma onu bütün iş üsulunu dəyişməyə məcbur edir.

Nüanslar: imzalı faylda dəyişiklik imzanı poza bilər, başqa müdafiə qatları yenə işləyə bilər; IP və domen dəyişmək bəzən asandır, bəzən etibarlı infrastruktur qurmaq vaxt tələb edir. Piramidanın mənası yalnız bir ünvan siyahısına bağlı qalmamaqdır. Gündəlik dəyişən fişinq heşlərini bloklamaq cari nümunələri saxlayır; eyni vaxtda sənəddən skript başlamasını və sonrakı qeyri-adi əlaqəni aşkarlamaq davranışa nəzarəti gücləndirir. Yuxarı pilləyə keçmək aşağıları ləğv etmir; davranış qaydasının sınağı, yanlış müsbətlərin təhlili və sensorların işləməsi daha çox əmək tələb edir.

### ATT&CK və hücum zənciri

MITRE ATT&CK müşahidə olunmuş rəqib davranışlarını taktika və texnikalarla təsvir edən bilik bazasıdır. Taktika hücumçunun məqsədini (niyə: ilkin giriş, davamlılıq, məlumat çıxarma), texnika üsulunu (necə) göstərir: T1566 fişinqi, T1078 etibarlı hesablardan istifadəni, T1110.003 parol püskürtməsini təsvir edir. Texnikanın xəritədə rənglənməsi aşkarlamanın işlədiyini sübut etmir: universitet həmin davranışı hansı jurnal sahəsi və hansı sınaqla görə bildiyini göstərməlidir.

ATT&CK v19 28 aprel 2026-cı ildə Enterprise matrisində əvvəlki Defense Evasion sahəsini Stealth (TA0005) və Defense Impairment (TA0112) kimi ayırıb. Windows hadisə jurnallarının təmizlənməsi üçün əvvəlki T1070.001 identifikatoru T1685.005 olub. Köhnə mənbələr əvvəlki ad və nömrələrdən istifadə edir; analitik qaydada ATT&CK versiyasını saxlamaq və keçidləri izləmək uyğunsuzluğun qarşısını alır.

Cyber Kill Chain modeli kəşfiyyat, silahlanma, çatdırılma, istismar, quraşdırma, idarəetmə və məqsədə çatma mərhələlərini ayırır. Model hücumun harada kəsilə biləcəyini düşünmək üçün faydalıdır, amma hər real hadisə bu xətti bir dəfə və eyni sıra ilə keçmir: oğurlanmış bulud hesabında ayrıca zərərli proqram quraşdırılmaya bilər. ATT&CK də məcburi ardıcıllıq sxemi deyil.

:::figure
src = "m02-3.png"
alt = "Hesab oğurluğu zənciri: fişinqdən məlumat çıxarılmasına qədər beş addım və hər birinin altında müdafiə tədbiri."
caption = "Hesab oğurluğundan məlumat çıxarılmasına qədər müşahidələr və müdafiə nöqtələri (şərti nümunə)."
:::

## Mənbələr, OSINT və analitik səhvlər

### Mənbəni suala görə seçmək

Açıq mənbə kəşfiyyatı (Open-Source Intelligence, OSINT) ictimai əlçatan məlumatdan analitik bilik çıxarmaqdır: açıq hesabatlar, istehsalçı xəbərdarlıqları, sertifikat şəffaflığı qeydləri, domen məlumatı, açıq kod anbarları, tədqiqat məqalələri (konspektdə həmçinin xəbərlər, bloqlar, VirusTotal, AbuseIPDB). Açıq olması düzgün, aktual və sərbəst yenidən yayıla bilən olduğunu göstərmir; mənbənin lisenziyası, şəxsi məlumat və paylaşma şərti yoxlanılır.

Daxili mənbələr universitetə aid uyğunluğu göstərir. Xarici hesabat müəyyən əlavədə istismar olduğunu deyə bilər, amma universitetin həmin əlavəni işlədib-işlətmədiyini inventar müəyyən edir. Kommersiya məlumat axını (feed) daha çox obyekt verə bilər, lakin keyfiyyət müqavilədəki obyekt sayı ilə ölçülmür. Milli və sektor CERT/CSIRT-ləri, tədqiqat şəbəkələri və etibarlı tərəfdaşlar kontekstli xəbərdarlıq verə bilər.

| Mənbə | Alınan bilik | Yoxlama sualı |
| --- | --- | --- |
| İstehsalçı bildirişi | Təsirlənən versiya və düzəliş | Bizdəki versiya və sazlama uyğundurmu? |
| Daxili jurnallar | Yerli müşahidə və zaman xətti | Sensor işləyibmi, vaxt düzgündürmü? |
| İctimai hesabat | Kampaniya və davranış təsviri | İlkin sübut və müşahidə tarixi varmı? |
| Kommersiya feed-i | İndikatorlar və zənginləşdirmə | Təkrar mənbə və köhnəlmə necə idarə olunur? |
| Tərəfdaş universitet | Oxşar mühitdə yerli təcrübə | Paylaşma icazəsi və texniki uyğunluq varmı? |
| Passiv DNS və sertifikat qeydləri | İnfrastruktur əlaqələri | Ortaq hostinq yanlış əlaqə yaradırmı? |

Şərti OSINT işi: analitik universiteti təqlid edən `unec-hesab.example` domeni haqqında bildiriş alır. Əvvəlcə adın oxşarlığını, müşahidə tarixini və açıq sertifikat məlumatını yoxlayır, sonra universitetin DNS və poçt qeydlərində həmin domeni axtarır. Adın oxşarlığı fişinq şübhəsi yaradır, lakin məzmun və istifadə barədə sübut olmadan konkret cinayətkar qrupa bağlamağa əsas vermir.

Şübhəli saytı birbaşa iş kompüterindən açmaq rəqibə ünvanı göstərə, xüsusi keçidi aktivləşdirə və zərərli məzmuna məruz qoya bilər. Təhlükəsiz yanaşmada əvvəlcə mövcud qeydlər və passiv mənbələr araşdırılır; aktiv yoxlama üçün ayrıca səlahiyyət və təcrid olunmuş mühit lazımdır. Qapalı forum və sızmış bazalarla iş əlavə hüquqi və etik suallar doğurur; CTI ehtiyacı həmin məlumatı qanunsuz əldə etməyə əsas deyil.

Fayl reputasiyası xidmətinə sənəd yükləmək də paylaşmadır: müqavilə, imtahan sualları və şəxsi məlumat olan fayl ictimai analiz xidmətinə göndərilməməlidir. Yerli heş hesabı məzmunu ötürmədən müqayisəyə imkan verir (heş sorğusunun xarici xidmətə ünvanlandığı da nəzərə alınır). Şərti yerli faylın heşini və yerli DNS qeydində uyğunluğu yoxlayan əmrlər:

```bash
sha256sum numune.bin
rg -n 'unec-hesab\.example' dns.log
```

Bu əmrlər faylı icra etmir və şəbəkə sorğusu göndərmir. Heşin xarici siyahıda olmaması faylın zərərsiz olduğunu göstərmir; `rg` uyğunluğu yalnız həmin faylda müşahidə olduğunu bildirir, qeydin mənbəsi ayrıca oxunmalıdır.

### Analitik qərəzlər və sübutun gücü

- **Təsdiqləmə qərəzi (confirmation bias)**: ilkin fikri dəstəkləyən faktları seçib zidd sübutu zəiflətmək.
- **Lövbərlənmə (anchoring)**: ilk IP və ya ilk qrup adına həddən çox bağlanmaq.
- **Əlçatanlıq qərəzi (availability bias)**: son oxunan məşhur hadisəni hər yeni insidentə tətbiq etmək. Hər gecə girişini APT ilə izah etmək adi ehtiyat nüsxə tapşırığını nəzərdən qaçıra bilər.

| Qərəz | Şərti yanlış nəticə | Qarşı tədbir |
| --- | --- | --- |
| Təsdiqləmə | Fişinq fərziyyəsinə uyğun olmayan proksi qeydi nəzərə alınmır | Hər fərziyyəni zəiflədən sübutu ayrıca yazmaq |
| Lövbərlənmə | İlk görünən IP bütün insidentin mərkəzi sayılır | Hesab, cihaz və zaman əlaqələrini də qurmaq |
| Əlçatanlıq | Hər fayl şifrələnməsi son oxunan qrupla bağlanır | Qrup adından əvvəl müşahidəni təsvir etmək |
| Avtomatlaşdırmaya etibar | Modelin yüksək balı sübut sayılır | İlkin qeydi və balın səbəbini yoxlamaq |
| Seçmə qərəzi | Yalnız EDR olan cihazların mənzərəsi ümumiləşdirilir | Görünməyən seqmentləri və cihazları göstərmək |

Alternativ fərziyyələr cədvəllə müqayisə edilir: kitabxana serverinin xarici əlaqəsi üçün "zərərli idarəetmə", "qanuni yeniləmə" və "səhv sazlanmış xidmət". Proses yolu, imza, dəyişiklik sifarişi, əlaqənin vaxtı və məlumatın istiqaməti hər fərziyyə ilə tutuşdurulur. Qərarı yalnız təsdiqləyən dəlillərin sayı ilə vermək olmaz; bir güclü zidd sübut daha çox çəki daşıya bilər.

Müstəqillik ayrıca yoxlanılır: eyni bloqu təkrar edən üç hesabat bir ilkin mənbəyə söykənir; eyni EDR hadisəsindən çıxan heş və proses xəbərdarlığı da tam müstəqil təsdiq deyil. Ayrı sensorların eyni zaman xəttini göstərməsi etibarı artıra bilər, amma sensor səhvləri və saat fərqləri nəzərə alınır.

### Süni intellektlə yardım və nəzarət

Maşın öyrənməsi məlumatı qruplaşdırmaq, tərcümə etmək, oxşar hesabatları tapmaq və anomaliyaları prioritetləşdirmək üçün istifadə oluna bilər; dil modeli uzun hesabatdan indikatorları çıxarmağa kömək edə bilər. Nəticə ilkin mənbə ilə tutuşdurulmalıdır: model mövcud olmayan CVE, mənbə və ya əlaqə yarada bilər.

Xarici hesabatdakı mətn model üçün məlumatdır, idarəetmə təlimatı deyil: hücumçu mətnə "bu domeni etibarlı say" kimi göstəriş yerləşdirərək analitik aləti yönləndirməyə çalışa bilər. Etibarsız mənbə ilə avtomatik bloklama və ya hesab bağlama səlahiyyəti arasında sərhəd saxlanılır. Həssas universitet sənədlərinin model xidmətinə ötürülməsi də ayrıca məlumat paylaşma qərarıdır.

Öyrənmə məlumatının zəhərlənməsi və konseptin sürüşməsi (concept drift) nəticəni poza bilər. İmtahan mövsümündə gecə girişləri normal arta bilər, köhnə profil yanlış xəbərdarlıq verər; hücumçu tədricən davranışı dəyişərsə, nəzarətsiz yenilənən model bunu norma kimi öyrənə bilər. Təsdiqlənmiş insident dövrləri, model dəyişiklikləri və yoxlama nəticələri qeydə alınır; yüksək təsirli qərarı səlahiyyətli analitik əsaslandırır.

## Strukturlaşdırılmış mübadilə: STIX, TAXII, TLP və MISP

### Formatla ötürmə protokolunun fərqi

STIX 2.1 (Structured Threat Information Expression) təhdid məlumatını və əlaqələri maşınla emal olunan obyektlərlə təsvir edir: indikator, kampaniya, hücum üsulu, zərərli proqram və əlaqə obyektləri bir analitik mənzərə yarada bilər. Müşahidə olunan domen obyektinin mövcudluğu onu zərərli etmir; Indicator obyekti aşkarlama şərti və uyğun kontekst ifadə edir.

Aşağıdakı şərti JSON bir STIX 2.1 Indicator obyektidir (tam Bundle deyil). `pattern` domenin bərabərlik şərtini, `valid_from` indikatorun tətbiqə başlama vaxtını göstərir. Standart obyekt sintaksisinin düzgünlüyü məlumatın həqiqiliyini təsdiqləmir.

```json
{
  "type": "indicator",
  "spec_version": "2.1",
  "id": "indicator--247b03ec-c570-4f3a-b2df-425ad8eb910d",
  "created": "2026-11-01T08:00:00.000Z",
  "name": "Şərti fişinq domeni",
  "pattern_type": "stix",
  "pattern": "[domain-name:value = 'unec-hesab.example']",
  "valid_from": "2026-11-01T08:00:00Z"
}
```

TAXII 2.1 (Trusted Automated Exchange of Intelligence Information) təhdid məlumatının HTTPS üzərindən mübadiləsi üçün tətbiq protokoludur; API kökü, kolleksiyalar və obyektlərin alınması mexanizmlərindən istifadə edir. **STIX məlumatın necə ifadə olunduğunu, TAXII onun necə ötürüldüyünü təsvir edir.** STIX faylı TAXII olmadan da ötürülə bilər; TAXII serverindən alınması indikatorun etibarlılığını təsdiqləmir.

Universitet bağlantıda qarşı tərəfin autentifikasiyasını, sertifikatı, kolleksiyaya giriş hüququnu və səhifələnmiş nəticələrin tam alınmasını yoxlayır; son uğurlu sinxronlaşdırma vaxtı saxlanılır. Serverdən silinmiş və ya geri çağırılmış indikatorun müdafiə vasitələrində qalması ayrıca problemdir: mübadilə əlavə etmə ilə yanaşı dəyişdirmə və ləğvetməni də daşımalıdır.

### TLP 2.0 ilə paylaşma sərhədi

Traffic Light Protocol (TLP) məlumatı alan tərəfin onu kimə ötürə biləcəyini göstərir. TLP 2.0-da CLEAR, GREEN, AMBER və RED etiketləri, həmçinin AMBER+STRICT məhdudiyyəti var. Etiket hüquqi təsnifatı, müəllif hüququnu və girişin texniki idarəsini əvəz etmir, indikatorun zərərli olmasına etibar dərəcəsini də bildirmir.

| Etiket | Paylaşma sərhədi | Universitetdə şərti tətbiq |
| --- | --- | --- |
| TLP:RED | Yalnız konkret məlumat alıcıları (görüşdə və ya yazışmada iştirak edən şəxslər); sonrakı paylaşma yoxdur | Qapalı görüşdə adı göstərilən şəxslər |
| TLP:AMBER+STRICT | Alıcının təşkilatı daxilində, bilməli olan şəxslər | Universitetin səlahiyyətli insident heyəti |
| TLP:AMBER | Təşkilat daxilində və müştərilərlə, müdafiə üçün bilməli olduqları qədər | İcazəli daxili komanda və uyğun xidmət alıcıları |
| TLP:GREEN | Müəyyən edilmiş icma daxilində (məs. digər universitetlər, AzScienceCERT icması), açıq kanalda deyil | Razılaşdırılmış universitet təhlükəsizlik icması |
| TLP:CLEAR | TLP baxımından yayma məhdudiyyəti yoxdur (köhnə adı TLP:WHITE) | Açıq təhlükəsizlik tövsiyəsi |

TLP:AMBER bütün tərəfdaşlara sərbəst göndərmək icazəsi deyil: universitet öz tələbəsini və ya kənar qurumu avtomatik "müştəri" sayıb istənilən məlumatı paylaşmamalıdır; mənbənin nəzərdə tutduğu əhatə aydınlaşdırılır. TLP:GREEN də sosial şəbəkədə açıq yayım deyil. TLP:CLEAR əvvəlki TLP:WHITE adını əvəz edib. Daha geniş paylaşma üçün mənbədən icazə alınır.

Nümunə: başqa universitet TLP:AMBER+STRICT ilə fişinq hesabatı göndərib. Yerli analitik onu universitet daxilində ehtiyacı olan heyətə ötürə bilər, amma ümumi universitetlər qrupuna göndərə bilməz. Açıq tövsiyə üçün mənbə ilə razılaşdırma və ya həqiqətən müstəqil, paylaşılmasına icazə olan məlumat lazımdır. Mənbənin adını silmək məhdudiyyəti avtomatik ləğv etmir.

### MISP və indikatorun idarəsi

MISP açıq mənbəli təhdid məlumatı paylaşma və əməkdaşlıq platformasıdır. Hadisələrdə (event) əlaqəli atributlar və obyektlər saxlanılır: domen, IP və heş atribut, bir neçə sahəli fayl və ya şəbəkə təsviri isə obyekt şəklində verilə bilər. Taksonomiyalar və etiketlər təsnifatı, əlaqələndirmə funksiyası ortaq atributları, paylaşma qrupları isə alıcı əhatəsini idarə etməyə kömək edir.

Şərti fişinq hadisəsində mənbə, tarix, təsvir və paylaşma səviyyəsi yaradılır; domen, məktub mövzusu və fayl heşi əlavə edilir, daxili müşahidə ayrıca qeyd olunur. Aşkarlama üçün uyğun atributun `to_ids` işarəsi müəyyən edilir; bu, avtomatik "firewall-da blokla" əmri deyil. Mətnli izah və ya paylaşılan xidmət ünvanı aşkarlama ixracına uyğun olmaya bilər.

MISP-in daxili formatı ilə STIX eyni deyil: ixrac və idxalda sahələrin, obyekt əlaqələrinin və paylaşma işarələrinin necə çevrildiyi yoxlanmalıdır. Köhnəlmə modelləri və müşahidələr indikatorun aktuallığını idarə etməyə kömək edir; platforma analitik qərarı əvəz etmir. Universitet səhv məlumatı düzəldəndə düzəliş ilkin mənbəyə, həmin məlumatı göndərdiyi bütün alıcılara və ondan istifadə edən yerli sistemlərə çatdırılmalıdır.

:::figure
src = "m02-4.png"
alt = "Mənbələrdən MISP platformasına, analitik yoxlamadan sonra SIEM, EDR, DNS/proksi və firewall-a gedən təhdid məlumatı axını."
caption = "Təhdid məlumatının yoxlamadan sonra universitetin müdafiə sistemlərinə ötürülməsi."
:::

## Universitetdə CTI işinin təşkili

### Sualdan cavab tədbirinə qədər

Kiçik komanda CTI-ni böyük platforma almaqla başlamaya bilər. Əvvəlcə qorunan xidmətlər, onların sahibləri, prioritet suallar və cavab verə biləcək mənbələr müəyyən edilir; sonra alınan bilik mövcud poçt şlüzünə, SIEM-ə və EDR-ə bağlanır. İdarə olunmayan minlərlə indikator əvəzinə yerli riskə uyğun az sayda yoxlanmış məhsul daha faydalı ola bilər.

Şərti nümunə: semestr qeydiyyatından əvvəl tərəfdaş universitet saxta tələbə portalı kampaniyası haqqında məlumat göndərir. Yerli CTI məsulu paylaşma şərtini və müşahidə tarixini yoxlayır; domen təsdiqlənmiş xidmət siyahısı ilə tutuşdurulur. Poçt axtarışı keçidin əməkdaş və tələbələrə çatdığını, DNS bəzi cihazların sorğu etdiyini göstərir. Bağlantı və hesab qeydləri olmadan yoluxma sayı elan edilmir.

SIEM, yəni təhlükəsizlik məlumatı və hadisələrinin idarə edilməsi sistemi, müxtəlif mənbələrin qeydlərini əlaqələndirir: CTI ona kontekst verir, SIEM-in yerli müşahidəsi CTI qiymətləndirməsini gücləndirir. EDR proses ardıcıllığını göstərə bilər. Təhlükəsizlik əməliyyatları mərkəzi (SOC) xəbərdarlığı araşdırır, CSIRT insidentin əlaqələndirilməsini aparır.

Aşağıdakı qeydlər real məhsula aid olmayan normallaşdırılmış şərti nümunədir (vaxt UTC, IP və identifikatorlar tədris üçündür):

```text
2026-11-01T08:10:00Z mail user=s42 link=unec-hesab.example
2026-11-01T08:12:00Z dns host=lab17 q=unec-hesab.example
2026-11-01T08:18:00Z auth user=s42 src=198.51.100.24 ok=true
2026-11-01T08:21:00Z lms user=s42 action=profile_export
```

Bu ardıcıllıq əlaqəni göstərir, amma səbəb əlaqəsini hələ tam sübut etmir. Məktub açılıb, yoxsa avtomatik yoxlanıb? DNS sorğusu hansı prosesdən gəlib? Uğurlu giriş eyni cihazın VPN çıxışıdırmı? İxrac həmin hesab üçün qanunidirmi? Sualları cavablandıqca qərar daralır; yalnız saatların yaxınlığı əsasında istifadəçi günahlandırılmır.

Kompromitasiya təsdiqlənərsə, komanda sessiyaları ləğv edir, bərpa məlumatını və parolu yeniləyir, zərərli poçt qaydalarını yoxlayır, əlaqəli cihazı məhdudlaşdırır; məktubun digər alıcıları və başqa hesablardakı oxşar fəaliyyət axtarılır, çıxarılmış məlumatın əhatəsi müəyyən edilir. Aşkarlama qaydasının və giriş siyasətinin düzəlişi təkrar riski azaldır.

### Avtomatlaşdırma və keyfiyyətin ölçülməsi

Avtomatik proses aşağı təsirli və geri çevrilə bilən işlərdən başlayır: zənginləşdirmə, dublikatların tapılması, daxili axtarış, iş qeydinin açılması. Bütöv domenin bloklanması, serverin ayrılması və imtiyazlı hesabın bağlanması üçün əvvəlcədən səlahiyyət, şərt və geri qaytarma yolu yazılır. Məlumatın etibar dərəcəsi ilə tədbirin təsiri uyğunlaşdırılır.

| Göstərici | Necə ölçülür? | Yanlış şərh riski |
| --- | --- | --- |
| Tələbə uyğunluq | Məhsulun hansı prioritet suala cavab verdiyi | Məhsul sayını keyfiyyət saymaq |
| Tədbirə çevrilmə vaxtı | Məlumat qəbulundan işlək qaydaya qədər vaxt | Yoxlanmamış sürətli bloklamanı uğur saymaq |
| İndikatorun aktuallığı | Vaxtı keçmiş və geri çağırılmış qeydlərin payı | Sadəcə çox indikator toplamaq |
| Xəbərdarlıq dəqiqliyi | Təsdiqlənmiş uyğunluqların bütün araşdırılmış uyğunluqlara nisbəti | Görünməyən hücumları nəzərə almamaq |
| Aşkarlama örtüyü | Seçilmiş TTP sınaqlarının neçə hissəsi görünür? | Xəritədə rənglənməni real sınaq saymaq |
| Qərara təsir | Dəyişən nəzarət və azalan konkret boşluq | Hər dəyişiklik üçün əsassız CTI uğuru yazmaq |

Şərti ayda 40 indikator uyğunluğunun 10-u araşdırmada zərərli fəaliyyətlə əlaqəli təsdiqlənibsə, dəqiqlik 10/40 = 25 faizdir. Bu, bütün hücumların dörddə birinin tapıldığını göstərmir: aşkarlanmayanların sayı məlum deyil. Tamlığı qiymətləndirmək üçün icazəli sınaqlar və məlum hadisələr işlədilir. Az xəbərdarlıq həm sakit mühit, həm işləməyən toplama demək ola bilər.

CTI işinin davamlılığı üçün sahib, əvəzləyici şəxs və yenidən baxılma vaxtı müəyyən edilir; tələblər qeydiyyat, imtahan, layihə müdafiəsi və satınalma dövrlərinə uyğun dəyişir. Mənbə susanda, qayda işləməyəndə və ya bloklama tədris xidmətini kəsəndə məsul şəxs bunu görməlidir.

## Mühazirənin köhnə slaydlarla fərqləri

:::note Köhnə slaydlarla fərq
- **Aktorlar**: slaydda krakerlər "tələbələr", peşəkar cinayətkarlar "hakerlər" adlanıb. Yaş və təhsil növü müəyyən etmir; icazə, motiv, imkan və mənsubiyyət əsasdır.
- **"İnsan ən zəif halqadır"** şişirdilib: bəzən əsas boşluq yamanmamış sistem və ya pis arxitekturadır.
- **Statistika**: "sızmanın orta dəyəri 4,88 milyon dollar" IBM-in 2024 hesabatındandır (2025-də qlobal orta 4,44 milyon); "ransomware təşkilatların 73%-ni vurub" konkret sorğunun nəticəsidir. Rəqəmi ili və mənbəyi ilə yaz.
:::
