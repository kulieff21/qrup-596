+++
title = "Kibermüdafiə modelləri"
unit = "orta"
order = 5
summary = "Hər model və çərçivə 1–3 cümlə ilə: mərhələlər, mexanizmlər, əsas fərqlər və qısa nümunələr."
updated = 2026-11-09

[[source]]
title = "Mühazirə 5: Kibermüdafiə modelləri"
note = "Elmar Cabbarov, 2026–2027"
+++

Hücumu təsvir etmək üçün ortaq dil lazımdır: Cyber Kill Chain hücumun mərhələlərini, Unified Kill Chain içəri girdikdən sonrakıları, Diamond Model iştirakçılar arasındakı əlaqələri, ATT&CK konkret davranışı göstərir. Məqsəd adları əzbərləmək deyil, hansı modelin hansı suala cavab verdiyini bilmək və seçilən tədbiri yoxlama üsulu ilə birlikdə təqdim etməkdir.

## Kibermüdafiə modelinə nə üçün ehtiyac var

Kibermüdafiə modeli hücumun, müdafiənin və ya riskin seçilmiş tərəflərini göstərən anlayışlar sistemidir; konkret məhsul (antivirus, firewall) deyil. O, hansı məlumatı axtarmağı, hadisələri necə əlaqələndirməyi və qərarı necə əsaslandırmağı istiqamətləndirir. Hər model bəzi detalları saxlayır, digərlərini atır; bu, həm faydası, həm məhdudiyyətidir. Birini o birinin əvəzinə işlətmək səhv sual verməyə səbəb olur: ATT&CK cədvəlindən büdcə və məsul şəxs çıxmır, CSF funksiyasından konkret aşkarlama qaydası çıxmır.

Təhlil dörd səviyyədə aparılır: **strateji** (hansı zərəri qəbul edə bilərik?), **əməliyyat** (hansı fəaliyyət yolu izlənir?), **taktiki və texniki** (hansı üsul və sübut var?), **arxitektura** (keçidi hansı sərhəd dayandırmalıdır?).

### Sübut, fərziyyə və kəşfiyyat

- **Hadisə (event)** sistemdə baş verən fəaliyyətdir; jurnal qeydi onun saxlanmış təsviridir.
- **Xəbərdarlıq (alert)** qaydanın araşdırılmalı saydığı nəticədir.
- **İnsident** təhlükəsizliyi pozan və ya real təhdid edən haldır.

**Təhdid kəşfiyyatı (threat intelligence)** qərar verməyə yarayan, mənbəsi və məhdudiyyətləri qiymətləndirilmiş məlumatdır; sadəcə IP siyahısı deyil. Köhnəlmiş ünvanı bloklamaq kitabxananın qanuni xidmətini dayandıra bilər. Nümunələr universitetin LMS-i, tələbə bazası və daxili şəbəkəsi üzərindən verilir (şərti tədris nümunələri). **Kəşfiyyata əsaslanan müdafiə (intelligence-driven defense)** əvvəl məlumat tələbini müəyyən edir, mənbələri toplayıb təhlil edir, nəticəni tədbirə çevirir və geri əlaqə ilə tələbi yeniləyir.

| Səviyyə | Nümunə | Nəticə |
| --- | --- | --- |
| Müşahidə | Şlüz əlavəni karantinə alıb | Bu nüsxənin çatdırılması bloklanıb |
| Fərziyyə | Eyni hesabda yad giriş cəhdi | İki fəaliyyət əlaqəli ola bilər |
| Təsdiqlənmiş nəticə | Açılma və proses qeydə alınıb | Həmin cihazda icra baş verib |
| Naməlum sahə | Cihaz jurnalı toplanmayıb | İcra müəyyən edilməyib |

“Əlamət yoxdur” mənbənin görmə imkanına bağlıdır: audit açılmayıbsa, qeydin olmaması arxayınlıq vermir. Vaxt da yoxlanır (şlüzün saatı irəlidə ola bilər); hadisə vaxtı, qəbul vaxtı, mənbə və vaxt qurşağı saxlanır.

## Cyber Kill Chain

Lockheed Martin tədqiqatçıları (Hutchins, Cloppert, Amin) 2011-ci ildə hərbi hədəfləmə zənciri fikrini kompüter müdaxiləsinə tətbiq etdilər; ilkin diqqət qabaqcıl davamlı təhdidlərə (advanced persistent threat, APT) idi. Əsas fikir: konkret hücum yolu üçün zəruri addım dayandırılsa, həmin yol məqsədə çatmır. Bu, kampaniyanın bitməsi demək deyil: hücumçu başqa hesab, məktub, xidmət sınaya bilər.

:::figure
src = "m05-1.png"
alt = "Cyber Kill Chain-in yeddi mərhələsi oxlarla bağlı; aşağıda Unified Kill Chain-in In, Through, Out hissələri."
caption = "Cyber Kill Chain və Unified Kill Chain. Real fəaliyyətdə təkrarlar mümkündür."
wide = true
:::

| Mərhələ | Nədir | Müdafiə |
| --- | --- | --- |
| 1. Kəşfiyyat (reconnaissance) | Hədəf haqqında məlumat toplanır; açıq mənbə kəşfiyyatı (OSINT) çox vaxt jurnala düşmür | Açıq məlumatı azaltmaq, xidmət inventarı, skanı qeyd etmək |
| 2. Silahlanma (weaponization) | Eksploit zərərli yüklə birləşdirilir; hücumçunun mühitində gedir, yerli sensor görmür | Nümunə və kəşfiyyat hesabatlarından öyrənmək |
| 3. Çatdırılma (delivery) | Fişinq, daşıyıcı, zərərli səhifə | Poçt şlüzü, veb proksi, SPF/DKIM/DMARC (qismən), istifadəçi bildirişi |
| 4. İstismar (exploitation) | Zəiflikdən istifadə və ya istifadəçi icrası | Yamaq, icra məhdudiyyəti, DEP/ASLR, EDR |
| 5. Quraşdırma (installation) | Arxa qapı, davamlılıq (xidmət, tapşırıq) | Minimum hüquq, icazə siyahısı, dəyişiklik monitorinqi |
| 6. Komanda və idarəetmə (command and control, C2) | Yoluxmuş sistem hücumçu serverinə qoşulur | Çıxış süzgəci, DNS, proksi, IDS, cihaz təcridi |
| 7. Məqsədə yönəlmiş hərəkətlər (actions on objectives) | Məlumat oğurluğu, şifrələmə, sabotaj | DLP, seqmentasiya, qorunan nüsxə, insidentə cavab |

Praktik qeydlər: SPF, DKIM və DMARC domen saxtalaşdırmasını azaldır, amma qanuni hesabdan gələn zərərli məktubu dayandırmır. Hər istifadəçi icrası proqram zəifliyinin istismarı deyil, konkret səbəb müəyyən edilməlidir. Faylın diskə yazılması, prosesin işləməsi və yenidən başladıqdan sonra qalması fərqli sübutlardır. HTTPS C2-ni qanuni etmir; istiqamət, vaxt, proses faydalıdır. Ehtiyat nüsxə məxfiliyi bərpa etmir: oğurlanmış məlumat artıq kənardadır.

:::tip Sıra
Kəşfiyyat → Silahlanma → Çatdırılma → İstismar → Quraşdırma → C2 → Məqsəd. Nə qədər erkən dayandırsan, ziyan az olur.
:::

### Fəaliyyət variantları matrisi

Fəaliyyət variantları matrisi (courses of action matrix) mərhələ ilə təsir növünü kəsişdirir; hüceyrələri doldurmaq məcburi deyil (öz sensorun görmədiyi mərhələ üçün aşkarlama iddia etmək olmaz).

| Variant | Mənası | Nümunə |
| --- | --- | --- |
| Aşkarla (detect) | Tanımaq | Şübhəli C2 əlaqəsini tapmaq |
| Rədd et (deny) | İmkanı verməmək | Zərərli əlavəni buraxmamaq |
| Poz (disrupt) | Davam edəni kəsmək | Yoluxmuş cihazı təcrid etmək |
| Zəiflət (degrade) | Səmərəni azaltmaq | İxracın sürətini məhdudlaşdırmaq |
| Aldat (deceive) | Saxta resursla üzə çıxarmaq | Tələ hesabına cəhdi görmək |
| Məhv et (destroy) | Zərərli imkanı aradan qaldırmaq | Öz sistemində zərərli yükü silmək |

“Məhv et” kənar sistemlərə cavab hücumu demək deyil; sübut üçün nüsxə və heş (hash) əvvəl qorunur, tələ real məlumat hesabına qurulmur.

### Tənqid

Gücü sadə ünsiyyətdir (rəhbərliyə izah asandır). Zəifliyi: daxili fəaliyyəti ümumiləşdirir, xəttidir, oğurlanmış VPN hesabı, daxili sui-istifadə və sistemin qanuni alətlərindən istifadə (living off the land) sığmır. Erkən müdaxilə həmişə ən ucuz deyil: həddən artıq sərt poçt qaydası imtahan sənədlərini də saxlaya bilər.

:::exam
“Bütün mərhələlərdən keçməlidir, istənilən həlqəni qırmaq hücumu dayandırır” klassik modelin fərziyyəsidir, qanun deyil. Bloklanmış məktub yalnız həmin yolun nəticəsidir; EDR-in susması da sübut deyil.
:::

## Unified Kill Chain

Paul Pols 2017-ci ildə Unified Kill Chain-i (UKC) təqdim etdi: Cyber Kill Chain-i ATT&CK davranış detalları ilə birləşdirir və genişləndirir. Onu Kill Chain ilə Diamond-un birləşməsi adlandırmaq dəqiq deyil. 18 faza üç hissədədir:

| Hissə | Mənası | Fazalar |
| --- | --- | --- |
| In | ilkin dayaq | Kəşfiyyat, Resurs hazırlığı (Resource Development), Çatdırılma, Sosial mühəndislik (Social Engineering), İstismar, Davamlılıq (Persistence), Müdafiədən yayınma (Defense Evasion), C2 |
| Through | daxildə yayılma | Körpü yaratma (Pivoting), Daxili kəşf (Discovery), İmtiyaz artırma (Privilege Escalation), İcra, Kimlik məlumatlarına giriş (Credential Access), Yanal hərəkət (Lateral Movement) |
| Out | hədəfə çatma | Toplama, Məlumatın çıxarılması (Exfiltration), Təsir (Impact), Məqsədlər |

Bölgü fiziki “girmə və çıxma” demək deyil (Out-dakı təsir daxildə qalan bazanın pozulması ola bilər) və məcburi sıra deyil: icra imtiyaz artımından əvvəl də ola bilər, kəşf təkrarlana bilər. Sıra nömrəsi hadisənin vaxtı ilə qarışdırılmır. 2-ci faza “Resurs hazırlığı” adlanır (köhnə “Silahlanma”); köhnə “Target Manipulation” isə “Impact” olub.

Araşdırma: **In**-də ilkin girişin baş verib-verməməsi sual edilir (keçidin göndərilməsi, açılması, yad girişi üç ayrı nəticədir). **Through**-da bir cihazdan bütün mühitə baxılır (xidmət hesabı başqa serverdə də keçərlidirsə, yoluxma genişlənir). **Out**-da hər nəticə ayrıca sübut istəyir: arxiv yaratmaq çıxarılma deyil, fidyə tələbi ödənişi sübut etmir.

### İki fərqli pivot

UKC-də körpü yaratma (pivoting) ələ keçirilmiş sistemdən başqa şəbəkəyə çıxış, çox vaxt tunel deməkdir. Yanal hərəkət həmin yoldan başqa sistemə keçiddir; tunelsiz də (məsələn, RDP ilə admin parolu) baş verə bilər. Diamond-dakı analitik pivot isə tam başqadır: məlum faktdan (domen) əlaqəli faktlara keçən təhlil üsuludur. UKC kiçik xəbərdarlıq üçün artıq ağırdır, çoxhostlu insident üçün faydalıdır.

:::exam
UKC-ni “strateji”, ATT&CK-ı “necə” adlandırmaq sadələşdirmədir: ATT&CK-da taktika niyə, texnika necə sualına cavab verir.
:::

## Diamond Model

Caltagirone, Pendergast və Betz 2013-cü ildə modeli dərc etdilər. Əsas vahid müdaxilə hadisəsidir: **rəqib (adversary)** **infrastrukturdan (infrastructure)** istifadə edərək **imkanını (capability)** **qurbana (victim)** qarşı tətbiq edir.

| Təpə | Nədir |
| --- | --- |
| Rəqib | şəxs və ya qrup (adı məlum olmaya bilər) |
| İnfrastruktur | domen, IP, server, C2, poçt hesabı |
| İmkan | alət, zərərli proqram, texnika, eksploit |
| Qurban | şəxs, hesab, cihaz, təşkilat (bir neçə səviyyədə) |

Rəqib–qurban oxu sosial-siyasi, imkan–infrastruktur oxu texnoloji əlaqədir. “Rəqib məlum deyil” əsassız qrup adından yaxşıdır; infrastruktur sahibi hücumçu sayılmır.

:::figure
src = "m05-2.png"
alt = "Diamond Model: rəqib, imkan, infrastruktur, qurban təpələri; infrastrukturdan domen üzərindən əlaqəli hadisələrə pivot."
caption = "Diamond Model və domendən analitik keçid."
wide = true
:::

**Meta-xüsusiyyətlər (meta-features):** vaxt möhürü (timestamp), mərhələ (phase), nəticə (result), istiqamət (direction), metodologiya (methodology), resurslar (resources). Bilinməyən sahənin səbəbi yazılır; “uğurlu” sözünün obyekti göstərilir (məktubun çatması hesabın ələ keçməsi deyil).

**Analitik keçid:** məlum xüsusiyyətdən (məsələn, domen) əlaqəli məlumata keçmək; hər keçiddə alternativ izah saxlanır. **Fəaliyyət zənciri (activity thread)** zaman və səbəb əlaqəli hadisələrdir; **fəaliyyət qrupu (activity group)** oxşar hadisə və zəncirlərin analitik klasteridir. Onu konkret təşkilata aid etmək ayrıca atribusiya (attribution) iddiasıdır.

| Ortaq xüsusiyyət | Alternativ izah |
| --- | --- |
| Eyni bulud IP-si | Ünvan paylaşılır |
| Eyni fayl heşi | Hazır nümunə müxtəlif aktorlarda |
| Eyni TTP | Üsul geniş yayılıb |
| Eyni hesab | Qanuni istifadə və hücum qarışıb |

:::exam
Eyni bulud IP-si eyni qrup üçün sübut deyil: bulud ünvanları minlərlə müştəri arasında paylaşılır. Bu fərziyyədir; fərziyyəni gücləndirən pivotlar eyni domen qeydiyyatçısı, TLS sertifikatı, kod xüsusiyyətləri, iş saatları və TTP-lərdir. Tapılmasa, hadisələr ayrı qeyd edilir və məlumat TLP:GREEN ilə paylaşılır.
:::

## MITRE ATT&CK

MITRE ATT&CK real müşahidələrə əsaslanan hücumçu davranışları bilik bazasıdır (Adversarial Tactics, Techniques, and Common Knowledge). Zəiflik kataloqu deyil: CVE zəifliyi, ATT&CK davranışı təsvir edir; bir CVE müxtəlif yollarda, bir texnika CVE olmadan işlənə bilər.

| Anlayış | Məna | Nümunə |
| --- | --- | --- |
| Taktika (tactic) | niyə | İcra (Execution) |
| Texnika (technique) | necə | T1059 |
| Alt-texnika (sub-technique) | dar növ | T1059.001, PowerShell |
| Prosedur (procedure) | konkret tətbiq | Kafedra cihazında icazəsiz PowerShell skripti |

Bir texnika bir neçə taktikaya aid ola bilər (T1078, etibarlı hesab). Hər uğurlu girişə T1078 yazmaq düzgün deyil. Sahələr: Enterprise, Mobile, ICS; platforma da seçilir.

**Versiya.** Hesabatda versiya və tarix saxlanır. 28 aprel 2026 tarixli v19-da Defense Evasion taktikasının məzmunu Stealth (TA0005) və Defense Impairment (TA0112) üzrə ayrılıb; jurnal təmizlənməsi T1070.001-dən T1685.005-ə keçib. Windows Security 1102 yalnız həmin jurnalın təmizləndiyini göstərir. Köhnə qaydanı köçürəndə yalnız başlığı dəyişmək kifayət deyil; ilkin etiket, yeni etiket və çevirmə qeydi saxlanır.

**Xəritələmə (mapping).** Əvvəl davranış yazılır (proses, valideyn, hesab, fayl, istiqamət), sonra texnika seçilir; məhsulun xəbərdarlıq adı ilə xəritələmək səhv etiket çoxaldır. Cədvəldə texnikalar “mümkün”dür: PowerShell inzibati işdə də işlənir.

| Müşahidə | Texnika |
| --- | --- |
| Zərərli əlavə ilə fişinq | T1566.001 |
| İstifadəçi faylı açıb | T1204.002 |
| PowerShell icrası | T1059.001 |
| Planlaşdırılmış tapşırıq | T1053.005 |
| SMB ilə giriş | T1021.002 |
| Arxivə yığma | T1560.001 |
| Şifrələmə | T1486 |
| Bərpaya zərər | T1490 |

**Navigator və örtük.** ATT&CK Navigator qatlar (layers) üzərində rəngləmə və qeyd imkanı verir; qatın mənbəsi, versiyası, rəng mənası və tarixi sənədləşdirilir. Örtük (coverage) üç ayrı səviyyədir: telemetriya (məlumat gəlir?), aşkarlama (qayda var və işləyir?), cavab. “Məhsul dəstəkləyir” yoxlanmış örtük deyil.

:::figure
src = "m05-3.png"
alt = "Davranış, telemetriya, aşkarlama, sınaq, cavab: beş qutu, hər birinin məsulu ilə."
caption = "Davranışdan yoxlanmış müdafiəyə keçid."
wide = true
:::

:::example
12 prioritet davranışdan 8-i üçün telemetriya, 5-i üçün yoxlanmış aşkarlama var: aşkarlama örtüyü 5/12-dir. Bu, bütün ATT&CK-ın örtüldüyü demək deyil; bir proseduru sınamaq bütün tətbiqləri sübut etmir.
:::

## Pyramid of Pain

David Bianco (2013) indikatorları hücumçunun onları dəyişməsinin çətinliyinə görə sıralayır; “ağrı” hücumçunun uyğunlaşma yüküdür, müdafiəçinin xərci deyil. Kompromitasiya indikatoru (indicator of compromise, IoC) fayl heşi, domen, IP kimi göstəricidir; TTP geniş davranışdır. Heş dəqiqdir, TTP dayanıqlıdır.

| Səviyyə (aşağıdan yuxarı) | Müdafiə qərarı |
| --- | --- |
| Heşlər (hash values) | Məlum nümunəni tez bloklamaq |
| IP ünvanları | Vaxtı yoxlanmış ünvanı bloklamaq |
| Domen adları | DNS və poçt axtarışı |
| Şəbəkə və host artefaktları | Bir neçə əlamətli qayda |
| Alətlər (tools) | Davranışı müxtəlif nümunələrlə yoxlamaq |
| TTP | Hesab, icra və yanal hərəkəti əlaqələndirmək |

Sıra mütləq xərc qanunu deyil. Paylaşılan IP-ni bloklamaq hücumçuya az, qanuni xidmətə çox təsir edə bilər. Praktikada: əvvəl heş hesablanır (`sha256sum`) və eyni nüsxə axtarılır, sonra domen/IP, sonra davranış qaydası; yuxarı pillələr aşağıları ləğv etmir. Hər indikator üçün mənbə, müşahidə vaxtları, etibarlılıq, tədbir və yenidən baxma tarixi yazılır.

## MITRE D3FEND

D3FEND müdafiə üsullarını rəqəmsal obyektlərlə əlaqələndirən bilik bazası və ontologiyadır (ontology). ATT&CK hücumçunun davranışını adlandırır, D3FEND müdafiənin texniki təsirini; hazır məhsul siyahısı deyil. Başlanğıc **rəqəmsal artefaktdır (digital artifact)**: proses, fayl, şəbəkə trafiki, hesab.

| Müşahidə | Artefakt | Müdafiə üsulu |
| --- | --- | --- |
| Zərərli sənəd | Fayl, poçt əlavəsi | Fayl təhlili, məzmun məhdudiyyəti |
| İcazəsiz skript | Proses, əmr sətri | Proses təhlili, icra nəzarəti |
| C2 əlaqəsi | Şəbəkə trafiki | Trafik təhlili və süzülməsi |
| Ələ keçirilmiş hesab | Kimlik, sessiya | Kimlik məlumatlarının sərtləşdirilməsi |
| Yanal keçid | Şəbəkə yolu | Təcrid, seqmentlərarası nəzarət |

Əlaqənin tapılması universal bloklama sübutu deyil; nəzarət platformaya və sazlamaya bağlıdır. Seçim: qorunacaq obyekt → müşahidə → müdaxilə; yalnız IP bloklamaq kampus proksisi arxasındakı qanuni istifadəçiləri də dayandırar. Test həm icazəsiz sorğunun rəddini, həm icazəli sorğunun işləməsini yoxlayır. D3FEND riski və hüquqi qərarı təyin etmir: idarəetmə üçün CSF, texniki təsir üçün D3FEND, davranış üçün ATT&CK.

## NIST CSF 2.0

NIST CSF 2.0 (2024, fevral) kiberriski nəticələr üzrə altı funksiya altında təşkil edir; məhsul seçmir. Funksiyalar bir dəfəlik mərhələlər deyil, davamlı işlərdir.

| Funksiya | Nə edir |
| --- | --- |
| Govern (idarəetmə, 2.0-da əlavə) | risk həddi, məsuliyyət, təchizatçı tələbləri |
| Identify | aktiv, asılılıq, risk |
| Protect | MFA, minimum hüquq, yamaq, nüsxə |
| Detect | hesab, cihaz, çıxış izləmə |
| Respond | təcrid, əhatə təhlili, əlaqələndirmə |
| Recover | təmiz mühitdə bərpa |

Govern əvvəlcədən müəyyən edir ki, tələbə bazasını kim dayandıra bilər; yoxsa SOC hücum zamanı gözləyər. **Nüvə (Core)** funksiya, kateqoriya və altkateqoriyalardır. **Təşkilati profil (Organizational Profile)** cari və hədəf vəziyyəti göstərir; fərq fəaliyyət planıdır. **Səviyyələr (Tiers)**: Partial, Risk Informed, Repeatable, Adaptive; sertifikat balı deyil və ən yüksək səviyyə məcburi deyil. NIST SP 800-61 Rev. 3 (2025, aprel) insidentə cavabı CSF 2.0-a bağlayır.

## Çoxsəviyyəli müdafiə və sıfır etibar

**Çoxsəviyyəli müdafiə (defense in depth)** bir tədbir uğursuz olanda digərlərinin hücumu məhdudlaşdırmasıdır: insan, kimlik, cihaz, şəbəkə, tətbiq/məlumat, bərpa qatları. İki vasitə müstəqil qat demək deyil: eyni admin hesabı üç sistemi idarə edirsə, bu ortaq uğursuzluq səbəbidir. Hər qatın uğursuzluq ssenarisi yazılır (MFA token oğurluğunu, seqmentasiya icazəli yolda sui-istifadəni, EDR idarə olunmayan cihazı həll etmir; nüsxə məxfiliyi qaytarmır).

**Sıfır etibar (zero trust)** (NIST SP 800-207): “heç vaxt etibar etmə, həmişə yoxla”. Şəbəkədəki yer etibar vermir; hər sorğuda kimlik, cihaz vəziyyəti və kontekst yoxlanır, minimum hüquq verilir. “Həmişə yoxla” hər paketdə parol demək deyil: autentifikasiya kimliyi, avtorizasiya konkret əməli yoxlayır, risk dəyişəndə qərar yenilənir. Üç məntiqi rol: **siyasət mühərriki (policy engine)** qərar verir, **siyasət administratoru (policy administrator)** əlaqəni idarə edir, **icra nöqtəsi (policy enforcement point, PEP)** tətbiq edir; yan keçid yol qalarsa, siyasət kağızda qalır.

:::figure
src = "m05-4.png"
alt = "İstifadəçi və cihaz icra nöqtəsi (PEP) vasitəsilə resursa çatır, qərar nöqtəsi kimlik, cihaz və risk üzrə qərar verir; altda müstəqil qatlar."
caption = "Resursa görə giriş qərarı və müstəqil qatlar."
wide = true
:::

İkisi bir-birini əvəz etmir: sıfır etibar etibar qərarının harada və hansı əsasla verildiyini dəqiqləşdirir, çoxsəviyyəli müdafiə uğursuzluqdan sonra təsiri azaldır. Keçid ən həssas resursdan başlayır, imtahan vaxtı kimlik xidməti dayananda davranış əvvəlcədən razılaşdırılır, fövqəladə hesablar gündəlik işlədilmir.

## Modellərin müqayisəsi

| Model | Əsas sual | Məhdudiyyət |
| --- | --- | --- |
| Cyber Kill Chain | Hansı mərhələ? | Daxili fəaliyyət ümumiləşir |
| Unified Kill Chain | Girişdən məqsədə nə var? | 18 faza əlavə iş |
| Diamond Model | Kim, hansı imkanla, kimə? | Təqvim ayrıca lazımdır |
| ATT&CK | Hansı davranış? | Ardıcıllıq və risk balı yoxdur |
| Pyramid of Pain | Nəyi dəyişmək hücumçuya ağırdır? | Keyfiyyətcə |
| D3FEND | Hansı artefakta hansı müdafiə? | Real mühitdə test istəyir |
| NIST CSF 2.0 | Risk necə idarə olunur? | Aşkarlama qaydası vermir |
| Çoxsəviyyəli müdafiə | Bir qat keçilsə nə qalır? | Ortaq asılılıq |
| Sıfır etibar | Bu kimliyə bu əməl verilməlidirmi? | Yanlış siyasət, görünməyən cihaz |

Seçim sualdan başlayır: rektorluğa izah üçün Kill Chain və CSF, serverlər arası keçid üçün UKC və ATT&CK, eyni kampaniyanı başqa kafedralarda axtarmaq üçün Diamond. Eyni müşahidənin bir neçə modeldə etiketlənməsi yeni sübut deyil.

## Fidyə proqramı insidenti: bütün modellərlə

Ssenari tədris üçün şərtidir (UTC+04:00). Kafedra cihazı 10.20.5.24, fayl serveri 10.30.0.12; svc-arxiv xidmət hesabının geniş yazma hüququ var və sirri köhnə skriptdə saxlanır.

:::steps Vaxt xətti
[[step]]
title = "09:10–09:14: giriş"
body = "Cədvəl.zip məktubu çatır, istifadəçi Cədvəl.exe açır, PowerShell başlayır, icazəsiz tapşırıq yaranır, xarici HTTPS əlaqəsi qurulur."

[[step]]
title = "09:20–09:28: yayılma"
body = "Paylaşmalar axtarılır, skriptdən svc-arxiv sirri oxunur, həmin hesabla files.uni.example üzərində SMB sessiyası açılır."

[[step]]
title = "09:32–09:44: nəticə"
body = "Sənədlər arxivə yığılır, böyük xarici ötürmə var, fayl serverində kütləvi şifrələmə və fidyə qeydi."

[[step]]
title = "09:46–10:05: cavab"
body = "SOC cihazı və serveri təcrid edir, sessiyaları kəsir. 10:05 cəhdin baş vermə vaxtı deyil, müəyyən edilmə vaxtıdır: tələbə bazasına keçid cəhdi rədd edilib."
:::

- **Cyber Kill Chain:** çatdırılma, icra (zəiflik sübut olunmayıb), quraşdırma, C2 təsdiqlənib; kəşfiyyat və silahlanmanın necə getdiyi məlum deyil; daxili hərəkət son mərhələyə yığılır.
- **UKC:** 18 fazadan hər biri üçün sübut və ya açıq məsələ yazılır: təsdiqlənənlər çatdırılma, sosial mühəndislik, davamlılıq, C2, kəşf, kimlik məlumatlarına giriş, yanal hərəkət, toplama, təsir; çıxarılma əlaqəlidir, məzmun tam təsdiqlənməyib; körpü, yayınma, imtiyaz artımı sübut olunmayıb; məqsəd olaraq yalnız fidyə tələbi var.
- **Diamond:** iki hadisə (qurban əməkdaş, sonra fayl serveri); eyni cihaz əvvəl qurban, sonra infrastruktur olur. Heş, domen, xidmət hesabı üzrə pivotlar əlavə təsirlənənləri axtarır; aktorun hüquqi kimliyi göstərilmir.
- **ATT&CK:** T1566.001, T1204.002, T1059.001, T1053.005, T1021.002, T1560.001, T1486, hesab sui-istifadəsi üçün T1078; çıxarılma üçün kanal dəqiqləşməyincə T1041 yazılmır.
- **Pyramid of Pain:** əvvəl heş və domen, sonra davranış (istifadəçi faylından interpretator, tapşırıq, yeni hesab sessiyası); test edilməyən qayda dərhal sərt bloklamaya qoyulmur.
- **D3FEND:** fayl, proses, trafik və hesab sessiyası ayrı obyektlərdir; hər tədbir öz testi ilə yoxlanır.
- **Çoxsəviyyəli müdafiə:** poçt və cihaz qatları keçilib, sirrin zəif qorunması daxili keçidi mümkün edib, bazanın sərhəddi cəhdi rədd edib, ayrı nüsxə bərpanı mümkün edib: hər qat ayrı qiymətləndirilir.
- **Sıfır etibar:** xidmət hesabı adi iş stansiyasından fayl serverinə niyə buraxılıb? Hesab yalnız müəyyən serverdən işləməli idi.
- **CSF:** Govern məsul və dayandırma səlahiyyətini, Identify sirrin işləndiyi yerləri, Protect hesabların ayrılmasını (imtiyazlı giriş idarəsi, PAM) və sirrin dəyişməsini, Detect qaydaları, Respond təcridi və sübut qorunmasını, Recover təmiz serverə nüsxə qaytarmağı müəyyən edir.

Bərpa köhnə faylları geri yazmaq deyil: davamlılıq silinir, hesablar və sirrlər yenilənir, nüsxənin hücumdan əvvəlki etibarlılığı yoxlanır. Şərti RTO 6 saat (xidmətin bərpası üçün hədəf vaxt) və RPO 4 saatdır (qəbul edilən məlumat itkisinə uyğun nöqtə); faktiki dəyərlər onlarla müqayisə edilir. Şifrələnmiş faylların açılması məxfilik problemini həll etmir.

## Aşkarlama qaydasını hazırlamaq və yoxlamaq

Aşkarlama mühəndisliyi (detection engineering) hücum fərziyyəsini işlək, yoxlanmış, idarə olunan qaydaya çevirir. Nümunə: planlaşdırılmış tapşırıqla PowerShell başlaması; audit siyasəti açıq olanda Windows Security 4698 tapşırığın yaradılmasını göstərir. Tədris Sigma qaydası EventID 4698 və TaskContent-də `powershell.exe` axtarır; SIEM-ə çevirmə və audit sazlaması ayrıca yoxlanmalıdır. Qayda hökm vermir: tapşırığı yaradan hesab, cihaz rolu, skript yolu, imza və dəyişiklik qeydi yoxlanır; istisna konkret tapşırığa, qrupa və müddətə daraldılır; sahib, mənbə, cavab addımları və kor nöqtələr saxlanır.

Yoxlama ayrı laboratoriyada, həssas məlumatsız fayllarla aparılır; zərərsiz test tapşırığı və qanuni inzibati tapşırıq birlikdə sınanır (yanlış müsbətlər üçün). 10 sınaqdan 8-i xəbərdarlıq verirsə, nəticə “tam örtük” deyil: gecikmənin harada olduğu aydınlaşdırılır, aşkarlamadan təcridə vaxt və mənbə susması izlənir. ATT&CK davranışı, UKC hadisədəki yeri, Diamond əlaqələri, D3FEND müdaxiləni, CSF məsuliyyəti göstərir.

:::reveal İki modeldə eyni müşahidənin etiketlənməsi niyə yeni sübut deyil?
Çünki hər ikisi eyni mənbəyə (məsələn, eyni EDR qeydinə) əsaslanır; etibarlılıq qiymətləndirməsində bu asılılıq nəzərə alınır.
:::
