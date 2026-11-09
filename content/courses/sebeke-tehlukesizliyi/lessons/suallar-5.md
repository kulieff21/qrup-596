+++
title = "Kibermüdafiə modelləri"
unit = "suallar"
order = 5
summary = "Mühazirənin nəzarət sualları və situasiya tapşırıqları, konspektdən situasiyalar və ehtimal olunan əlavə suallar, hazır cavablarla."
updated = 2026-11-09

[[source]]
title = "Mühazirə 5: Kibermüdafiə modelləri"
note = "Elmar Cabbarov, 2026–2027"

[[source]]
title = "Midterm konspekti, Mövzu 5"
note = "Elmar Cabbarov"
+++

İmtahan açıq suallardan ibarətdir və cavab yazılı verilir. Hər sualı əvvəl özün cavablandır, sonra cavaba bax. Situasiya suallarında ardıcıllıq: aktiv, pozulan xassə, səbəb, tədbir, yoxlama; müşahidəni, fərziyyəni və təsdiqlənmiş nəticəni ayır.

## Nəzarət sualları

:::reveal Kibermüdafiə modeli ilə konkret təhlükəsizlik məhsulu arasında hansı fərq var?
- Kibermüdafiə modeli hücumun, müdafiənin və ya riskin seçilmiş tərəflərini göstərən anlayışlar sistemidir.
- Məhsul (antivirus, firewall) konkret nəzarətdir; model isə hansı məlumatı axtarmağı, hadisələri necə əlaqələndirməyi və qərarı necə əsaslandırmağı istiqamətləndirir.
- Hər model bəzi detalları saxlayır, digərlərini atır; bu, həm faydası, həm məhdudiyyətidir.
- Birini digərinin əvəzinə işlətmək səhv sual verməyə səbəb olur: ATT&CK-dan büdcə və məsul çıxmır, CSF-dən aşkarlama qaydası çıxmır.
:::

:::reveal Hadisə, jurnal qeydi, xəbərdarlıq və insident necə ayrılır?
- Hadisə (event): sistemdə baş verən fəaliyyət.
- Jurnal qeydi: həmin fəaliyyətin saxlanmış təsviri.
- Xəbərdarlıq (alert): bir qaydanın araşdırılmalı saydığı nəticə.
- İnsident: təhlükəsizliyi pozan və ya real təhdid edən hal.
- Poçt şlüzünün xəbərdarlığı araşdırmaya başlamaq üçün əsasdır, amma kompüterdə zərərli proqramın işlədiyini öz-özünə sübut etmir.
:::

:::reveal Cyber Kill Chain-in yeddi mərhələsini sıra ilə sadalayın və hər biri üçün universitet nümunəsi verin.
1. Kəşfiyyat: açıq LMS xidmətinin skanı (müdafiə: lazımsız xidməti bağlamaq).
2. Silahlanma: universitetə uyğun saxta seminar sənədi (müdafiə: təhlil edilmiş nümunələrdən öyrənmək, icra imkanını azaltmaq).
3. Çatdırılma: saxta təqaüd məktubu (poçt süzgəci, əlavə siyasəti, karantin).
4. İstismar: sənəd açıldıqdan sonra icazəsiz icra (yamaq, icra məhdudiyyəti, EDR).
5. Quraşdırma: icazəsiz tapşırıq və ya xidmət (minimum hüquq, icazə siyahısı).
6. Komanda və idarəetmə (C2): LMS administratorunun cihazından xarici ünvana periodik sorğular (nəzarətli çıxış, proksi, təcrid).
7. Məqsədə yönəlmiş hərəkətlər: kütləvi ixrac və fayl dəyişməsi (DLP, seqmentasiya, nüsxə, bərpa).
:::

:::reveal Silahlanma mərhələsi niyə çox vaxt yerli sensorlara görünmür?
- Hazırlıq adətən hücumçunun öz mühitində gedir; universitetin şəbəkə sensoru onu birbaşa görmür.
- Müdafiəçi təhlil edilmiş nümunələrdən, etibarlı kəşfiyyat hesabatlarından və özündə tapılmış fayldan hazırlığın xüsusiyyətlərini öyrənə bilər.
- Sonradan əldə edilmiş fayl onun nə vaxt hazırlandığını göstərmir.
- Ona görə bu mərhələ üçün yerli aşkarlama imkanı varmış kimi göstərilmir.
:::

:::reveal Bloklanmış bir əlavədən bütün kampaniyanın dayandığı nəticəsi niyə çıxmır?
- Zəncirin qırılması yalnız həmin hücum yolunu dayandırır.
- Hücumçu başqa hesab, başqa məktub və başqa xidmət sınaya bilər.
- Bloklanmış məktub yalnız həmin çatdırılma yolunun nəticəsidir; eyni məktubun başqa nüsxələri, hesab girişləri və cihaz fəaliyyəti yoxlanmalıdır.
- “Hər həlqəni qırmaq hücumu dayandırır” klassik modelin fərziyyəsidir, qanun deyil.
:::

:::reveal Fəaliyyət variantları matrisində rədd etmə, pozma və aldatma necə fərqlənir?
- Rədd et (deny): tələb olunan imkanı verməmək; məsələn, poçtda zərərli əlavəni buraxmamaq.
- Poz (disrupt): davam edən fəaliyyəti kəsmək; məsələn, yoluxmuş cihazı təcrid etmək.
- Aldat (deceive): saxta resursla davranışı üzə çıxarmaq; məsələn, istifadə olunmayan tələ hesabına cəhdi görmək (saxta resurs ayrıca izolyasiya olunur).
- Matrisdə daha üç təsir var: aşkarla (detect), zəiflət (degrade), məhv et (destroy). Hər hüceyrəni doldurmaq məcburi deyil.
:::

:::reveal UKC-nin In, Through və Out hissələrinə hansı fazalar daxildir?
- **In** (ilkin dayaq): kəşfiyyat, resurs hazırlığı, çatdırılma, sosial mühəndislik, istismar, davamlılıq, müdafiədən yayınma, komanda və idarəetmə (1–8).
- **Through** (daxildə yayılma): körpü yaratma, daxili kəşf, imtiyazların artırılması, icra, kimlik məlumatlarına giriş, yanal hərəkət (9–14).
- **Out** (hədəfə çatma): toplama, məlumatın çıxarılması, təsir, məqsədlər (15–18).
- Bölgü fiziki girmə-çıxma demək deyil və sıra məcburi deyil.
:::

:::reveal UKC-də körpü yaratma ilə yanal hərəkəti və Diamond Model-də analitik keçidi fərqləndirin.
- Körpü yaratma (pivoting): ələ keçirilmiş sistemdən başqa şəbəkə və resurslara çıxış, çox vaxt tunel.
- Yanal hərəkət: həmin yoldan istifadə edib başqa sistemdə mövqe əldə etmək; tunelsiz də ola bilər.
- Analitik keçid (Diamond): məlum faktdan (məsələn, domen) əlaqəli məktublara, hesablara keçərək araşdırmanı genişləndirən təhlil üsulu.
- Birincisində hücumçu sistemlər arasında yol açır, ikincisində analitik faktlar arasında hərəkət edir; hesabatda “şəbəkə körpüsü” və ya “analitik keçid” deyə dəqiqləşdirilir.
:::

:::reveal Diamond Model-in dörd əsas xüsusiyyəti və altı meta-xüsusiyyəti nədir?
- Dörd əsas: rəqib (adversary), infrastruktur (infrastructure), imkan (capability), qurban (victim). Rəqib infrastrukturdan istifadə edib imkanını qurbana qarşı tətbiq edir.
- Altı meta-xüsusiyyət: vaxt möhürü, mərhələ, nəticə, istiqamət, metodologiya, resurslar.
- Rəqib–qurban oxu sosial-siyasi, imkan–infrastruktur oxu texnoloji əlaqədir.
- Naməlum təpə modelin istifadəsinə mane olmur; “rəqib məlum deyil” əsassız qrup adından yaxşıdır.
:::

:::reveal Fəaliyyət zənciri və fəaliyyət qrupu hansı əsaslarla qurulur?
- Fəaliyyət zənciri (activity thread): zaman və səbəb əlaqələri ilə birləşdirilmiş hadisələr (məktub, keçidin açılması, hesabdan giriş, bazadan ixrac).
- Fəaliyyət qrupu (activity group): oxşar xüsusiyyətli hadisə və zəncirlərin analitik klasteri.
- Hər əlaqə ölçülə bilən xüsusiyyətlərlə (eyni gün, eyni keçid, eyni əlavə məzmunu) və alternativ izahla sənədləşdirilir.
- Qrupun konkret təşkilata və ya dövlətə aid edilməsi ayrıca atribusiya iddiasıdır.
:::

:::reveal Eyni bulud IP-si niyə eyni aktor üçün yetərli sübut deyil?
- Bulud ünvanları minlərlə müştəri arasında paylaşılır və vaxtla başqa müştəriyə keçə bilər.
- Yalnız bir təpə (infrastruktur) üst-üstə düşür; bu zəif əlaqədir, fərziyyədir.
- Əlavə yoxlama: müşahidə vaxtı, domen, xidmət ayrıntıları, imkanlar, TTP-lər.
- Müşahidə, fərziyyə və təsdiqlənmiş nəticə ayrılır.
:::

:::reveal ATT&CK-da taktika, texnika, alt-texnika və prosedur necə fərqlənir?
- Taktika (tactic): fəaliyyətin niyə edildiyi, yaxın məqsəd (məsələn, İcra).
- Texnika (technique): məqsədə necə çatıldığı (T1059, əmr və skript interpretatorları).
- Alt-texnika (sub-technique): üsulun dar növü (T1059.001, PowerShell).
- Prosedur (procedure): konkret aktorun və ya proqramın tətbiqi (kafedra cihazında icazəsiz PowerShell skripti).
- Texnika bir neçə taktikaya aid ola bilər; ATT&CK zəiflik kataloqu deyil.
:::

:::reveal ATT&CK v19-da Defense Evasion və Windows jurnal təmizlənməsi ilə bağlı hansı dəyişikliklər var?
- 28 aprel 2026 tarixli v19-da Enterprise sahəsində Defense Evasion taktikasının məzmunu Stealth (TA0005) və Defense Impairment (TA0112) üzrə ayrılıb.
- Windows hadisə jurnallarının təmizlənməsi əvvəl T1070.001 idi, v19-da T1685.005 işlənir.
- Windows Security 1102 yalnız həmin jurnalın təmizləndiyini göstərir, bütün kanalların silindiyini yox.
- Köhnə qaydanı köçürəndə ilkin etiket, yeni etiket və çevirmə qeydi saxlanır; versiya sahəsi reyestrdə yazılır.
:::

:::reveal Navigator qatında yaşıl xananın mənası niyə sənədləşdirilməlidir?
- Rəngin mənası göstərilməzsə, eyni yaşıl xana biri üçün “məlumat var”, digəri üçün “hücum bloklanır” ola bilər.
- Qatın mənbəsi, ATT&CK versiyası, rəng şkalası və yenilənmə tarixi də yazılır.
- Rəngli matris təkbaşına müdafiə zəmanəti vermir.
:::

:::reveal Telemetriya, aşkarlama və cavab örtüyünü niyə ayrı ölçmək lazımdır?
- Sensorun quraşdırılması məlumatın toplandığını, toplanan məlumat qaydanın işlədiyini, qayda isə real şəraitdə vaxtında xəbərdarlıq verdiyini göstərmir.
- Hər seçilmiş davranış üçün üç status ayrı saxlanır; “məhsul dəstəkləyir” yoxlanmış örtük deyil.
- Nümunə: 12 davranışdan 8-i üçün telemetriya, 5-i üçün yoxlanmış aşkarlama, 3-ü üçün yoxlanmış cavab; aşkarlama örtüyü 5/12-dir və bütün ATT&CK-ın örtüldüyü demək deyil.
:::

:::reveal Pyramid of Pain-in altı səviyyəsi nədir və sıra hansı çətinliyi təsvir edir?
- Aşağıdan yuxarı: heşlər, IP ünvanları, domen adları, şəbəkə və host artefaktları, alətlər, TTP.
- Sıra hücumçunun həmin elementi dəyişməsinin çətinliyini (uyğunlaşma yükünü) göstərir; müdafiəçinin xərcini yox.
- Heş dəqiqdir amma dəyişmək asandır; TTP dayanıqlıdır.
- Sıra mütləq xərc qanunu deyil, keyfiyyətcə qiymətləndirilir.
:::

:::reveal D3FEND-də rəqəmsal artefakt anlayışı tədbir seçiminə necə kömək edir?
- Artefakt proses, fayl, şəbəkə trafiki, hesab kimi müşahidə və müdaxilə obyektidir.
- Fayl, proses və trafik təhlili müxtəlif artefaktları görür, trafik süzülməsi isə bağlantıya təsir edir; hamısını “antivirus var” cümləsinə yığmaq boşluqları gizlədir.
- Hücum müşahidəsi artefaktla, artefakt isə konkret müdafiə üsulu ilə əlaqələndirilir və hər tədbir öz testi ilə yoxlanır.
:::

:::reveal CSF 2.0 funksiyaları, cari profil, hədəf profil və Tiers nəyi göstərir?
- Altı funksiya: Govern, Identify, Protect, Detect, Respond, Recover.
- Cari profil mövcud, hədəf profil çatmaq istənilən vəziyyətdir; aradakı fərq fəaliyyət planına çevrilir.
- Tiers (Partial, Risk Informed, Repeatable, Adaptive) risk idarəsinin nə dərəcədə təşkil edildiyini göstərir; sertifikat balı deyil və ən yüksək səviyyə məcburi deyil.
:::

:::reveal Çoxsəviyyəli müdafiədə ortaq uğursuzluq səbəbi nədir?
- İki vasitənin olması müstəqil qat demək deyil.
- Eyni admin hesabı serveri, nüsxəni və jurnal arxivini idarə edirsə, bir hesabın ələ keçirilməsi bütün qatlara təsir edir; eyni telemetriyadan asılı iki qayda mənbə susanda birlikdə korlaşır.
- Qatlar seçilərkən ortaq uğursuzluq səbəbləri ayrıca araşdırılır.
:::

:::reveal Sıfır etibarda autentifikasiya, avtorizasiya və sessiyanın yenidən qiymətləndirilməsi necə əlaqələnir?
- Autentifikasiya kimliyi yoxlayır, avtorizasiya həmin kimliyə konkret əməl verir.
- Giriş və sessiya siyasət əsasında qiymətləndirilir; risk və cihaz vəziyyəti dəyişəndə qərar yenilənir.
- “Həmişə yoxla” hər paketdə parol soruşmaq deyil.
- Rollar: siyasət mühərriki qərar verir, administrator əlaqəni idarə edir, icra nöqtəsi (PEP) tətbiq edir.
:::

:::reveal Fidyə proqramından bərpa məlumat sızması riskini niyə aradan qaldırmır?
- Nüsxə əlçatanlığı bərpa edir, məxfiliyi yox: oğurlanmış məlumat artıq kənardadır.
- Şifrələmə ilə məlumat çıxarılması ayrıca araşdırılır (arxiv oxunması ilə böyük ötürmənin əlaqəsi).
- Hesabatda təsdiqlənən məzmun, ehtimal olunan çıxış və müəyyən edilə bilməyən hissə ayrılır.
:::

:::reveal Şərti qaydanın bir laboratoriya sınağından keçməsi hansı nəticələri deməyə əsas vermir?
- Bütün prosedurların, bütün mühitlərin və real şəraitin tutulduğunu.
- Bir tapşırığın tutulması bu üsulun bütün tətbiqlərinin görüldüyünü göstərmir; 10 sınaqdan 8-i xəbər verirsə, “tam örtük” deyil.
- Əməliyyat sistemi, audit sazlaması və hüquqlar dəyişəndə nəticə də dəyişir; yanlış müsbətlər və mənbə susması ayrıca yoxlanır.
:::

## Situasiya tapşırıqları

**Situasiya 1.** Şərti universitetdə saat 09:10-da mühasibatlıq əməkdaşına zərərli əlavə göndərilir, şlüz onu bloklayır. 09:25-də eyni hesaba uğursuz giriş cəhdi var. Cihazda xəbərdarlıq görünmür. Analitik “kompüter yoluxub, amma hücum bitib” yazır. Bu nəticəni düzəldin.

:::reveal Cavab
- **Təsdiqlənən:** əlavənin çatdırılma yolunda bloklanması.
- **Sübut yoxdur:** icra və yoluxma; kampaniyanın bitdiyi də məlum deyil.
- **Uğursuz giriş** ayrıca müşahidədir, məktubla əlaqəsi yoxlanmalıdır.
- **Yoxlama:** eyni məktubun digər nüsxələri, hesabın uğurlu sessiyaları, cihaz telemetriyası, mənbələrin işləkliyi.
- Cyber Kill Chain mərhələni, Diamond isə mümkün əlaqələri göstərir.
:::

**Situasiya 2.** Şərti ssenaridə universitetin sızmış VPN hesabı ilə giriş var. Hücumçu serverləri axtarır, başqa hesabın sirrini tapır, fayl serverinə keçir və sənədləri arxivləyir. Analitik bütün yeddi klassik mərhələnin baş verdiyini yazmaq istəyir. Hansı xəritə daha əsaslıdır?

:::reveal Cavab
- UKC xəritəsi müşahidəyə uyğundur: ilkin giriş, daxili kəşf, kimlik məlumatlarına giriş, yanal hərəkət, toplama.
- Arxivin yaranması məlumatın çıxarıldığını sübut etmir.
- Çatdırılma, ayrıca istismar, körpü tuneli və davamlılıq üçün sübut yoxdur.
- ATT&CK texnikaları detallı qeydlərə görə seçilir.
- **Tədbir:** VPN-də uyğun MFA, hesabların ayrılması, serverə resurs əsaslı giriş nəzarəti.
:::

**Situasiya 3.** İki universitetə göndərilmiş şübhəli məktublarda eyni bulud IP-si görünür. Birində saxta giriş səhifəsi, digərində zərərli əlavə var. Analitik bu faktla hücumçu qrupunun kimliyini təsdiqlədiyini bildirir. Diamond Model əsasında cavab verin.

:::reveal Cavab
- Ortaq infrastruktur mümkün əlaqədir, aktorun kimliyinə yetərli sübut deyil.
- Ünvanın paylaşılması və vaxtla başqa müştəriyə keçməsi yoxlanır.
- Məktub məzmunu, domenlər, vaxtlar, imkanlar və prosedurlar üzrə əlavə analitik keçid aparılır.
- Hadisələr ilkin olaraq ayrı saxlanır, əlaqə fərziyyə kimi yazılır.
- Fəaliyyət qrupu qurulsa belə, bu, hüquqi kimlik atribusiyasını avtomatik vermir.
:::

**Situasiya 4.** Universitetin Navigator qatında bütün seçilmiş texnikalar yaşıl rəngdədir. Təchizatçı EDR-in onları dəstəklədiyini deyir. Yoxlamada kafedra cihazlarından proses məlumatının gəlmədiyi aşkarlanır. Yaşıl xəritəni necə qiymətləndirmək lazımdır?

:::reveal Cavab
- Təchizatçı imkanının göstərilməsi universitetdə yoxlanmış örtük demək deyil.
- Telemetriya, qayda, test və cavab ayrı statuslarla yazılmalıdır.
- Məlumat gəlməyən cihazlarda aşkarlama örtüyü təsdiqlənməyib.
- **Tədbir:** mənbə sağlamlığını düzəltmək, uyğun prosedurları sınamaq, rəng şkalasını və tarixçəni yeniləmək.
- Test edilməyən sahələr yaşıl nəticə kimi təqdim olunmur.
:::

**Situasiya 5.** Kitabxanada zərərli faylın heşi bloklanır. Sonra eyni davranışlı, başqa heşli fayl aşkarlanır. Komanda heş siyahısını tam dayandırıb yalnız davranış qaydalarına keçmək təklif edir. Pyramid of Pain baxımından qərar necə verilməlidir?

:::reveal Cavab
- Fayl dəyişəndə heşin dəyişməsi gözlənilən haldır.
- Təsdiqlənmiş heşlərin sürətli bloklama və axtarış dəyəri qalır.
- Paralel olaraq proses, tapşırıq və əlaqə ardıcıllığı üçün daha dayanıqlı qaydalar hazırlanır və qanuni kitabxana avtomatlaşdırması ilə yoxlanır.
- Piramida aşağı pillələri ləğv etmək göstərişi deyil; müxtəlif müddətdə fayda verən tədbirləri uyğunlaşdırmağa kömək edir.
:::

**Situasiya 6.** Universitetdə istehsalat serveri, nüsxə sistemi və jurnal arxivi eyni admin hesabı ilə idarə olunur. Kampus VPN-inə girən həmin hesab bütün üç sistemə çatır. İdarəçi bunu “üçqat müdafiə və sıfır etibar” adlandırır. Problemi müəyyən edin.

:::reveal Cavab
- Eyni hesab ortaq uğursuzluq səbəbidir: ələ keçsə, üç sistemə də təsir mümkündür.
- Nüsxə və jurnal idarəsi ayrılmalı, minimum hüquq və ayrıca giriş yolları qurulmalıdır.
- VPN girişi bütün resurslara avtomatik icazə verməməlidir.
- Sıfır etibar konkret resurs, əməl, kimlik və cihaz üçün qərar tələb edir.
- CSF profilində bu boşluğa məsul və yoxlanacaq hədəf nəticə yazılır.
:::

**Situasiya 7.** Şərti universitet insidentində fayllar nüsxədən bərpa olunub. Proksi xaricə böyük ötürmə göstərir, amma məzmun saxlanmayıb. Rəhbərliyə “bütün risk aradan qalxıb” yazmaq təklif edilir. Hesabat necə olmalıdır?

:::reveal Cavab
- Əlçatanlığın bərpası ilə məxfiliyin qiymətləndirilməsi ayrılır.
- Hansı faylların bərpa edildiyi, hansı sirrlərin dəyişdirildiyi, hansı girişlərin bağlandığı göstərilir.
- Böyük ötürmə ilə arxiv oxunmasının əlaqəsi araşdırılır; çıxarılan həcm və məzmun təsdiqlənməyibsə, bu məhdudiyyət yazılır.
- Recover nəticəsi yaxşılaşa bilər, amma Respond və risk qiymətləndirilməsi üzrə açıq işlər qalır.
:::

## Konspektdən situasiyalar

**Situasiya K1.** Saat 09:10-da universitet mühasibatlığının əməkdaşına “Faktura_Noyabr.docm” əlavəli məktub gəlir, 09:12-də e-poçt şlüzü əlavəni bloklayır. 09:25-də həmin əməkdaşın hesabına uğursuz giriş cəhdi qeydə alınır, əməkdaş bunu etmədiyini deyir. EDR-də heç bir xəbərdarlıq yoxdur. Kill Chain-ə görə hücum hansı mərhələyə çatıb? “Kompüter yoluxub” demək olarmı?

:::reveal Cavab
- Təsdiqlənən mərhələ **çatdırılma cəhdidir**: zərərli əlavə göndərilib və şlüzdə bloklanıb.
- Bu əlavə ilə istismar baş verdiyinə dair sübut yoxdur; kəşfiyyatın necə aparıldığı (ünvan haradan tapılıb) məlum deyil.
- Uğursuz giriş ayrıca hesab hücumudur (parol təxmini və ya sızmış parolla cəhd).
- “Kompüter yoluxub” demək üçün sübut yoxdur, bu yalnız fərziyyədir; EDR-in susması “heç nə olmayıb” demək deyil, yalnız görünən əlamət yoxdur.
- **Növbəti addımlar:** eyni məktubun kimlərə getdiyini yoxlamaq, hesabın giriş tarixçəsinə baxmaq, parolu dəyişib MFA-nı yoxlamaq, göndəricinin domenini bloklamaq.
:::

**Situasiya K2.** Hücumçu sızmış VPN parolu ilə universitet şəbəkəsinə daxil olur, şəbəkəni skan edir, bir serverdə admin parollarını yaddaşdan çıxarır, RDP ilə tələbə məlumat sisteminin serverinə keçir, 40 GB tələbə məlumatını arxivləyib xarici serverə yükləyir. Bunu hansı model daha yaxşı təsvir edir? Mərhələləri adlandır.

:::reveal Cavab
- **Unified Kill Chain** daha uyğundur: zərərli fayl çatdırılması və istismar yoxdur, hücumun əsas hissəsi içəridə gedir.
- **Mərhələlər:** etibarlı hesabla ilkin giriş (In), kəşf (skan), kimlik məlumatlarına giriş (yaddaşdan parol), yanal hərəkət (RDP), toplama (arxivləmə), məlumatın çıxarılması (Out).
- Klassik Kill Chain bu ardıcıllığın böyük hissəsini “7. Məqsədə çatma” içində itirərdi.
- **Müdafiə:** VPN-də MFA, admin hesablarının ayrılması (PAM), tələbə məlumat sistemini ayrıca seqmentə almaq, çıxan trafikin həcminə nəzarət.
:::

**Situasiya K3.** Bakıda iki universitetə qarşı fişinq kampaniyasında eyni bulud provayderinə aid bir IP ünvanı görünür, amma zərərli proqramlar və hədəf qruplar (birində müəllimlər, digərində mühasibat) fərqlidir. Analitik “bu, eyni qrupdur” yazır. Diamond modeli baxımından bu nəticəni qiymətləndir.

:::reveal Cavab
- Yalnız bir təpə (infrastruktur) üst-üstə düşür; imkan və qurban təpələri fərqlidir.
- Bulud IP-ləri paylaşılır: zəif əlaqədir, yalnız fərziyyə ola bilər.
- Gücləndirmək üçün analitik pivotlar: eyni domen qeydiyyatçısı, eyni TLS sertifikatı, kodda eyni xüsusiyyətlər, eyni iş saatları, eyni TTP-lər.
- Tapılmasa, kampaniyalar ayrı-ayrı qeydə alınır; iki universitet məlumatı TLP:GREEN ilə bir-biri ilə paylaşır.
:::

## Ehtimal olunan əlavə suallar

:::reveal Cyber Kill Chain, Unified Kill Chain, Diamond Model və ATT&CK hansı suala cavab verir və necə tamamlayır?
- Cyber Kill Chain: hücum hansı mərhələdədir, harada qırmaq olar? Güclü: sadə, rəhbərliyə izah asan. Zəif: xəttidir, daxili hərəkəti zəif göstərir.
- Unified Kill Chain: girişdən hədəfə nə baş verdi? Güclü: içəri girdikdən sonrakı ətraflı mərhələlər. Zəif: 18 faza mürəkkəbdir.
- Diamond Model: kim, hansı imkan və infrastrukturla, kimə qarşı? Güclü: əlaqələr və kampaniyalar. Zəif: zaman ardıcıllığı zəif görünür.
- ATT&CK: hansı texnika işlənib? Güclü: ən ətraflı davranış bazası, aşkarlama qaydaları onunla yazılır. Zəif: böyükdür, mərhələ ardıcıllığı vermir.
- Kill Chain və UKC mərhələni, Diamond əlaqələri, ATT&CK texnikanı təsvir edir; bir insident hesabatında üçü birlikdə işlədilə bilər. Eyni müşahidənin bir neçə modeldə etiketlənməsi yeni müstəqil sübut deyil.
:::

:::reveal UKC ilə Kill Chain arasındakı fərq nədir? UKC-ni “Kill Chain və Diamond-un inteqrasiyası” adlandırmaq niyə düzgün deyil?
- Klassik Kill Chain hazırlıqdan məqsədə qədər bütün hücumu təsvir edir, amma içəri girdikdən sonrakıları bir-iki mərhələdə ümumiləşdirir; UKC 18 faza ilə “evin içini” ətraflı bölür.
- Oğurlanmış VPN parolu ilə girən hücumçu çatdırılma və istismarı keçib birbaşa kəşf, kimlik məlumatları və yanal hərəkətə keçir; UKC bunu təsvir edə bilir.
- UKC əsasən Kill Chain və ATT&CK-ı birləşdirir; Diamond ayrıca modeldir.
- 2-ci faza “Silahlanma” deyil, “Resurs hazırlığı”dır (köhnə “Target Manipulation” isə “Impact” olub).
:::

:::reveal Müşahidə, fərziyyə, təsdiqlənmiş nəticə və naməlum sahə nümunələrlə izah edin.
- Müşahidə: şlüz əlavəni karantinə alıb; yazıla bilən: bu nüsxənin çatdırılması bloklanıb.
- Fərziyyə: eyni hesab üzrə yad giriş cəhdi var; iki fəaliyyət əlaqəli ola bilər.
- Təsdiqlənmiş nəticə: əlavənin açılması və yaratdığı proses qeydə alınıb; həmin cihazda icra baş verib.
- Naməlum sahə: cihaz jurnalı toplanmayıb; icranın olub-olmadığı müəyyən edilməyib.
- “Əlamət yoxdur” mənbənin görmə imkanına bağlıdır; vaxt (saat, qurşaq, qəbul vaxtı) da yoxlanır.
:::

:::reveal Cyber Kill Chain-də hər mərhələdə hansı müdafiə tədbirləri tətbiq olunur?
- Kəşfiyyat: açıq məlumatı azaltmaq, skanları qeyd etmək.
- Silahlanma: birbaşa görünmür; nümunə təhlili və kəşfiyyat.
- Çatdırılma: e-poçt süzgəci, veb proksi, USB qadağası, işçi təlimi; SPF, DKIM, DMARC qismən kömək edir.
- İstismar: yamaq, makroların bloklanması, EDR, DEP/ASLR.
- Quraşdırma: tətbiqlərə nəzarət (allowlisting), minimum hüquq, dəyişiklik monitorinqi.
- C2: çıxan trafikin süzülməsi, DNS süzgəci, IDS, proksi.
- Məqsəd: DLP, seqmentasiya, ehtiyat nüsxə, insidentə cavab.
:::

:::reveal Indicator of compromise ilə TTP arasındakı fərq nədir və bu, Pyramid of Pain ilə necə bağlıdır?
- IoC: baş vermiş və ya ehtimal olunan təhlükəli fəaliyyətlə əlaqəli müşahidə edilə bilən göstərici (heş, domen, IP).
- TTP: taktika, texnika və prosedurlar, yəni geniş davranış.
- Heş konkret obyektə çox dəqiq işarə edir, TTP müxtəlif alət və ünvanlarla təkrarlana bilər; dəqiqlik və dayanıqlılıq eyni meyar deyil.
- Piramidanın aşağısında heş (dəyişmək asan, tez bloklanır), yuxarısında TTP (dəyişmək ağrılı, qayda qurmaq vaxt istəyir).
:::

:::reveal ATT&CK ilə D3FEND və CSF arasındakı iş bölgüsü nədir?
- ATT&CK müşahidə olunan hücum davranışına ümumi ad verir (taktika, texnika).
- D3FEND müdafiənin texniki təsirini rəqəmsal artefaktlar üzərindən təsvir edir.
- CSF 2.0 riskin, məsuliyyətin və prioritetin idarəsini təşkil edir (funksiyalar, profillər).
- Birini digərinin əvəzinə işlətmək səhvdir: ATT&CK-dan büdcə, CSF-dən aşkarlama qaydası çıxmır.
:::

:::reveal Çoxsəviyyəli müdafiə ilə sıfır etibar arasındakı fərq nədir?
- Çoxsəviyyəli müdafiə: bir tədbir uğursuz olanda digərləri təsiri məhdudlaşdırır (müstəqil qatlar).
- Sıfır etibar: şəbəkədəki yerə etibar yoxdur, hər sorğuda kimlik, cihaz və kontekst yoxlanır, minimum hüquq verilir (NIST SP 800-207).
- Sıfır etibar seqmentasiyanı və ehtiyat nüsxəni əvəz etmir; çoxsəviyyəli müdafiə isə uğursuzluqdan sonra təsiri azaldır.
- İkisi bir arxitekturada işləyir.
:::

:::reveal RTO və RPO nədir? Şərti hədəflər RTO 6 saat, RPO 4 saatdırsa, nəyi müqayisə edirik?
- RTO: xidmətin bərpası üçün hədəf vaxt.
- RPO: qəbul edilən məlumat itkisinə uyğun bərpa nöqtəsi hədəfi.
- Faktiki dayanma müddəti 6 saatla, itən dəyişiklik intervalı 4 saatla müqayisə edilir.
- Nüsxənin mövcudluğu bu hədəflərə çatıldığını göstərmir.
:::

:::reveal Aşkarlama qaydası (detection engineering) necə hazırlanır və yoxlanır?
- Fərziyyə: istifadəçi cihazında planlaşdırılmış tapşırıqla PowerShell başlaması.
- Mənbə: audit siyasəti açıq olanda Windows Security 4698 tapşırığın yaradılmasını göstərir; tapşırıq məzmunu kollektora gəlməlidir.
- Qayda: tədris Sigma nümunəsi EventID 4698 və TaskContent-də powershell.exe axtarır; sahib, mənbə, cavab addımları və kor nöqtələr sənədləşir.
- Kontekst: hesab, cihaz rolu, skript yolu, imza, dəyişiklik qeydi; istisna konkret tapşırığa, qrupa və müddətə daraldılır.
- Yoxlama: ayrı laboratoriyada zərərsiz test və qanuni inzibati tapşırıq; yanlış müsbətlər, gecikmə, aşkarlamadan təcridə vaxt, mənbə susması. 10 sınaqdan 8-i xəbər verirsə, “tam örtük” deyil.
:::
