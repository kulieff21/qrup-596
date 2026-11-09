+++
title = "Kibermüdafiə modelləri"
unit = "qisa"
order = 5
summary = "Bütün modellər və çərçivələr bir-iki cümlə ilə: Kill Chain, UKC, Diamond, ATT&CK, Pyramid of Pain, D3FEND, CSF 2.0, çoxsəviyyəli müdafiə, sıfır etibar."
updated = 2026-11-09

[[source]]
title = "Mühazirə 5: Kibermüdafiə modelləri"
note = "Elmar Cabbarov, 2026–2027"
+++

Hücumu təsvir etmək üçün ortaq dil lazımdır: hər model hücumun, müdafiənin və ya riskin seçilmiş tərəfini göstərir, konkret məhsul deyil. Nümunələr universitetin LMS-i, tələbə bazası və daxili şəbəkəsi üzərindən verilir (şərti tədris nümunələri).

## Model, sübut və kəşfiyyat

| Anlayış | Nədir |
| --- | --- |
| Hadisə (event) | Sistemdə baş verən fəaliyyət; jurnal qeydi onun təsviridir |
| Xəbərdarlıq (alert) | Qaydanın araşdırılmalı saydığı nəticə |
| İnsident | Təhlükəsizliyi pozan və ya real təhdid edən hal |
| Təhdid kəşfiyyatı (threat intelligence) | Qərar verməyə yarayan, mənbəsi qiymətləndirilmiş məlumat (IP siyahısı təkcə kifayət deyil) |
| Kəşfiyyata əsaslanan müdafiə (intelligence-driven defense) | Tələb → toplama → təhlil → tədbir → geri əlaqə |

Sübut dörd səviyyədədir: **müşahidə** (şlüz əlavəni bloklayıb), **fərziyyə** (iki fəaliyyət əlaqəli ola bilər), **təsdiqlənmiş nəticə** (icra qeydə alınıb), **naməlum sahə** (jurnal toplanmayıb). “Əlamət yoxdur” mənbənin görmə imkanından asılıdır.

:::exam
Müşahidəni, fərziyyəni və nəticəni ayır: bloklanmış məktub yalnız çatdırılmanın bloklanmasını sübut edir, “kompüter yoluxub” fərziyyədir, “heç nə olmayıb” da sübut deyil.
:::

## Cyber Kill Chain

Lockheed Martin, 2011: hərbi hədəfləmə zənciri fikri qabaqcıl davamlı təhdidlərə (APT, advanced persistent threat) tətbiq edilir. Zəruri addım dayandırılsa, həmin yol məqsədə çatmır; kampaniya bitmir.

| Mərhələ | Nədir | Müdafiə |
| --- | --- | --- |
| 1. Kəşfiyyat (reconnaissance) | Hədəf haqqında məlumat, OSINT, skan | Açıq məlumatı azaltmaq, skanı qeyd etmək |
| 2. Silahlanma (weaponization) | Eksploit və zərərli yük birləşdirilir; hücumçunun mühitində, yerli sensor görmür | Nümunə və kəşfiyyat hesabatı |
| 3. Çatdırılma (delivery) | Fişinq, daşıyıcı, zərərli səhifə | Poçt şlüzü, proksi, SPF/DKIM/DMARC, istifadəçi bildirişi |
| 4. İstismar (exploitation) | Zəiflikdən istifadə və ya icra | Yamaq, icra məhdudiyyəti, DEP/ASLR, EDR |
| 5. Quraşdırma (installation) | Arxa qapı, davamlılıq | Minimum hüquq, icazə siyahısı, dəyişiklik monitorinqi |
| 6. Komanda və idarəetmə (command and control, C2) | Yoluxmuş sistem hücumçu serverinə qoşulur | Çıxış süzgəci, DNS, proksi, IDS, təcrid |
| 7. Məqsədə yönəlmiş hərəkətlər (actions on objectives) | Oğurluq, şifrələmə, sabotaj | DLP, seqmentasiya, qorunan nüsxə |

Sıra: Kəşfiyyat → Silahlanma → Çatdırılma → İstismar → Quraşdırma → C2 → Məqsəd.

**Fəaliyyət variantları matrisi (courses of action matrix)** hər mərhələ üçün altı təsir verir: aşkarla (detect), rədd et (deny), poz (disrupt), zəiflət (degrade), aldat (deceive), məhv et (destroy). Hamısı hər mərhələdə məcburi deyil; “məhv et” kənar sistemlərə cavab hücumu deyil, sübut üçün nüsxə və heş (hash) əvvəl qorunur.

Məhdudiyyət: model xəttidir, daxili hərəkəti ümumiləşdirir; oğurlanmış parolla giriş, daxili sui-istifadə və sistemin qanuni alətlərindən istifadə (living off the land) sığmır.

:::exam
“İstənilən həlqəni qırmaq hücumu dayandırır” klassik fərziyyədir, qanun deyil: hücumçu mərhələ buraxa, başqa yol seçə, yenidən cəhd edə bilər.
:::

## Unified Kill Chain

Paul Pols, 2017: Kill Chain-i ATT&CK ilə birləşdirən UKC içəri girdikdən sonrakı fəaliyyəti ətraflı göstərir (Kill Chain ilə Diamond-un birləşməsi deyil). 18 faza üç hissədədir.

| Hissə | Fazalar |
| --- | --- |
| In (ilkin dayaq) | Kəşfiyyat, Resurs hazırlığı (Resource Development), Çatdırılma, Sosial mühəndislik (Social Engineering), İstismar, Davamlılıq (Persistence), Müdafiədən yayınma (Defense Evasion), C2 |
| Through (daxildə yayılma) | Körpü yaratma (Pivoting), Kəşf (Discovery), İmtiyaz artırma (Privilege Escalation), İcra, Kimlik məlumatlarına giriş (Credential Access), Yanal hərəkət (Lateral Movement) |
| Out (hədəfə çatma) | Toplama, Məlumatın çıxarılması (Exfiltration), Təsir (Impact), Məqsədlər |

Fazalar təkrarlana və ya buraxıla bilər; 2-ci faza “Resurs hazırlığı”dır (köhnə “Silahlanma”), köhnə “Target Manipulation” isə “Impact” olub. Pivoting ələ keçirilmiş sistemi körpü edib başqa şəbəkəyə çıxmaqdır (tunel); yanal hərəkət başqa sistemə keçiddir (məsələn, RDP ilə).

:::exam
İki “pivot”: UKC-də pivoting şəbəkə körpüsüdür, Diamond-da analitik pivot məlum faktdan (domen, IP) əlaqəli faktlara keçən təhlil üsuludur.
:::

## Diamond Model

Caltagirone, Pendergast, Betz, 2013. Əsas vahid hadisədir: rəqib infrastrukturdan istifadə edib imkanını qurbana qarşı tətbiq edir.

| Təpə | Nədir |
| --- | --- |
| Rəqib (adversary) | Şəxs və ya qrup, adı məlum olmaya bilər |
| İnfrastruktur (infrastructure) | Domen, IP, server, C2, poçt hesabı |
| İmkan (capability) | Alət, zərərli proqram, texnika |
| Qurban (victim) | Şəxs, hesab, cihaz, təşkilat |

**Meta-xüsusiyyətlər (meta-features):** vaxt möhürü (timestamp), mərhələ (phase), nəticə (result), istiqamət (direction), metodologiya (methodology), resurslar (resources). Rəqib–qurban oxu sosial-siyasi, imkan–infrastruktur oxu texnoloji əlaqədir.

**Analitik keçid** bir faktdan əlaqəli hadisələrə keçməkdir. Zaman və səbəb əlaqəli hadisələr **fəaliyyət zənciri (activity thread)**, oxşarları **fəaliyyət qrupu (activity group)** olur; qrupu konkret təşkilata aid etmək ayrıca atribusiya (attribution) iddiasıdır.

:::exam
Eyni bulud IP-si eyni qrupun sübutu deyil (ünvanlar paylaşılır), yoxlanmalı fərziyyədir. Gücləndirən pivotlar: eyni domen qeydiyyatçısı, TLS sertifikatı, kod xüsusiyyətləri, iş saatları, TTP; tapılmasa hadisələr ayrı qeyd edilir, məlumat TLP:GREEN ilə paylaşılır.
:::

## MITRE ATT&CK

Real müşahidələrə əsaslanan hücumçu davranışları bazasıdır; zəiflik kataloqu deyil (CVE zəifliyi, ATT&CK davranışı təsvir edir). Sahələri: Enterprise, Mobile, ICS.

| Anlayış | Sual | Nümunə |
| --- | --- | --- |
| Taktika (tactic) | Niyə | İcra |
| Texnika (technique) | Necə | T1059 |
| Alt-texnika (sub-technique) | Dar növ | T1059.001, PowerShell |
| Prosedur (procedure) | Konkret tətbiq | Kafedra cihazında icazəsiz skript |

Bir texnika bir neçə taktikaya aid ola bilər; hər uğurlu girişə T1078 (etibarlı hesab) yazılmır. **Versiya:** v19-da (28 aprel 2026) Defense Evasion məzmunu Stealth (TA0005) və Defense Impairment (TA0112) üzrə ayrılıb; jurnal təmizlənməsi T1070.001-dən T1685.005-ə keçib. Hesabatda versiya saxlanır.

**Xəritələmə (mapping):** əvvəl davranış (proses, hesab, fayl), sonra texnika; məhsulun xəbərdarlıq adı ilə xəritələmək səhvdir. **Navigator** qatlar (layers) üzərində rəngləmə vasitəsidir; rəngin mənası sənədləşdirilir. **Örtük (coverage)** üç ayrı ölçülür: telemetriya, aşkarlama, cavab; “məhsul dəstəkləyir” yoxlanmış örtük deyil. Məsələn, 12 davranışdan 5-i üçün yoxlanmış aşkarlama varsa, örtük 5/12-dir.

## Pyramid of Pain

David Bianco, 2013: indikatorlar hücumçunun dəyişməsinin çətinliyinə görə sıralanır (“ağrı” hücumçunun yüküdür). Kompromitasiya indikatoru (indicator of compromise, IoC) heş, domen, IP kimi göstəricidir; TTP geniş davranışdır.

Aşağıdan yuxarı: heşlər (hash values) → IP ünvanları → domen adları → şəbəkə və host artefaktları → alətlər (tools) → TTP. Heş dəqiqdir, tez bloklanır, amma dəyişmək asandır; TTP dayanıqlıdır, qayda qurmaq vaxt istəyir. Sıra mütləq xərc qanunu deyil; yuxarı pillələr aşağıları ləğv etmir, paylaşılan IP-ni bloklamaq qanuni xidmətə zərər verə bilər.

## MITRE D3FEND

Müdafiə üsullarını rəqəmsal obyektlərlə əlaqələndirən bilik bazası və ontologiyadır (ontology); ATT&CK hücumu adlandırır, D3FEND müdafiənin texniki təsirini. Başlanğıc **rəqəmsal artefaktdır (digital artifact)**: proses, fayl, trafik, hesab.

| Müşahidə | Müdafiə üsulu |
| --- | --- |
| Zərərli sənəd | Fayl təhlili, məzmun məhdudiyyəti |
| İcazəsiz skript | Proses təhlili, icra nəzarəti |
| C2 əlaqəsi | Trafik təhlili və süzülməsi |
| Ələ keçirilmiş hesab | Kimlik məlumatlarının sərtləşdirilməsi |
| Yanal keçid | Təcrid, seqmentlərarası nəzarət |

D3FEND hazır məhsul siyahısı deyil və riski, hüquqi qərarı təyin etmir. Test həm icazəsiz sorğunun rəddini, həm icazəli sorğunun işləməsini yoxlamalıdır.

## NIST CSF 2.0

2024, fevral. Kiberriski nəticələr üzrə altı funksiyada təşkil edir; məhsul seçmir, davamlı işlərdir.

| Funksiya | Nə edir |
| --- | --- |
| Govern | İdarəetmə: risk həddi, məsuliyyət (2.0-da əlavə) |
| Identify | Aktiv, asılılıq, risk |
| Protect | MFA, minimum hüquq, yamaq, nüsxə |
| Detect | Şübhəli davranışı tapmaq |
| Respond | Təcrid, əhatə təhlili |
| Recover | Təmiz mühitdə bərpa |

**Nüvə (Core)** funksiya, kateqoriya və altkateqoriyalardır. **Təşkilati profil (Organizational Profile)** cari və hədəf vəziyyəti göstərir; fərq plana çevrilir. **Səviyyələr (Tiers)**: Partial, Risk Informed, Repeatable, Adaptive; sertifikat balı deyil. NIST SP 800-61 Rev. 3 (2025) insidentə cavabı CSF-ə bağlayır.

## Çoxsəviyyəli və sıfır etibar

**Çoxsəviyyəli müdafiə (defense in depth):** bir tədbir uğursuz olsa, digərləri təsiri məhdudlaşdırır (insan, kimlik, cihaz, şəbəkə, məlumat, bərpa qatları). İki vasitə müstəqil qat demək deyil: eyni admin hesabı, imtiyazlı giriş idarəsi (PAM) olmadan, üç sistemi idarə edirsə, bu ortaq uğursuzluq səbəbidir.

**Sıfır etibar (zero trust)**, NIST SP 800-207: “heç vaxt etibar etmə, həmişə yoxla”. Şəbəkədəki yer etibar vermir; hər sorğuda kimlik, cihaz və kontekst yoxlanır, minimum hüquq verilir. Üç rol: siyasət mühərriki (policy engine) qərar verir, siyasət administratoru (policy administrator) əlaqəni idarə edir, icra nöqtəsi (policy enforcement point, PEP) tətbiq edir. Sıfır etibar seqmentasiyanı və nüsxəni əvəz etmir; ikisi bir arxitekturada işləyir.

## Modellər: hansı suala cavab verir

| Model | Sual |
| --- | --- |
| Cyber Kill Chain | Hansı mərhələ, harada qırmaq olar? |
| Unified Kill Chain | Girişdən hədəfə nə baş verdi? |
| Diamond Model | Kim, hansı alət və infrastrukturla, kimə? |
| ATT&CK | Hansı texnika? |
| Pyramid of Pain | Hücumçu nəyi dəyişəndə çətinlik çəkər? |
| D3FEND | Hansı artefakta hansı müdafiə? |
| NIST CSF 2.0 | Risk və məsuliyyət necə idarə olunur? |
| Çoxsəviyyəli müdafiə | Bir qat keçilsə nə qalır? |
| Sıfır etibar | Bu kimliyə bu əməl verilməlidirmi? |

Modellər bir-birini tamamlayır; eyni müşahidənin bir neçə modeldə etiketlənməsi yeni sübut deyil.

## Ssenari və aşkarlama qaydası

Fidyə proqramı ssenarisində (şərti) məktub → istifadəçi icrası → tapşırıq və C2 → xidmət hesabı sirri → SMB ilə fayl serverinə keçid → arxivləmə və böyük ötürmə → şifrələmə → SOC təcridi gedir. Hər modellə: Kill Chain ilk müdaxilə fürsətini, UKC daxili fazaları, Diamond əlaqəli hadisələri, ATT&CK texnikaları (T1566.001, T1059.001, T1053.005, T1021.002, T1486), Pyramid heş və davranış qaydasını, D3FEND artefakt üzrə müdafiəni, sıfır etibar “xidmət hesabı niyə adi stansiyadan girir” sualını, CSF isə məsuliyyəti göstərir. Bərpa üçün hədəflər: RTO (xidmətin bərpası üçün hədəf vaxt) və RPO (qəbul edilən məlumat itkisinə uyğun nöqtə); nüsxə məxfiliyi qaytarmır.

**Aşkarlama mühəndisliyi (detection engineering)** fərziyyəni yoxlanmış qaydaya çevirir: məsələn, Sigma qaydası planlaşdırılmış tapşırıqda PowerShell axtarır (Windows 4698 hadisəsi). Qayda hökm vermir, kontekst yoxlanır; yoxlama təcrid olunmuş laboratoriyada, zərərsiz test və qanuni tapşırıqla aparılır; 10 sınaqdan 8-i xəbər verirsə, “tam örtük” deyil. Mənbə susması da ayrıca izlənir.
