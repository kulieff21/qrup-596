+++
title = "Kibertəhlükəsizlik təhdidləri; təhdid məlumatları və analitikası"
unit = "suallar"
order = 2
summary = "Mühazirənin nəzarət sualları cavablarla, situasiya tapşırıqları, konspektdən situasiyalar və ehtimal olunan əlavə suallar."
updated = 2026-11-09

[[source]]
title = "Mühazirə 2: Kibertəhlükəsizlik təhdidləri; təhdid məlumatları və analitikası"
note = "Elmar Cabbarov, 2026–2027"

[[source]]
title = "Midterm konspekti, Mövzu 2"
note = "Elmar Cabbarov"
+++

İmtahan yazılı açıq suallardır, ona görə hər cavab əvvəl anlayışı təyin etməli, sonra səbəbi və tədbiri göstərməlidir. Nümunələr şərti tədris nümunəsidir.

## Nəzarət sualları

:::reveal Aktiv, təhdid, zəiflik, hücum, risk və insident anlayışları eyni ssenaridə necə fərqlənir?
- Ssenari: keçmiş əməkdaşın VPN hesabı açıq qalıb.
- **Aktiv**: qorunan resurs, burada tələbə bazası.
- **Zəiflik**: hesabın vaxtında bağlanmaması.
- **Təhdid**: hesabdan məlumat oğurlamaq istəyən tərəf (mənbə).
- **Hücum**: oğurlanmış parolla giriş cəhdi.
- **İnsident**: tələbə bazasının ixracı.
- **Risk**: şəxsi məlumatın yayılması, qeydiyyatın dayanması, etimad itkisi ehtimalı və ağırlığı.
:::

:::reveal Məxfilik, tamlıq, əlçatanlıq və autentiklik üçün universitetdən nümunələr verin.
- Məxfilik: şəxsi məlumatı yalnız səlahiyyətli şəxs görür (tələbə bazası).
- Tamlıq: qiymət və status icazəsiz dəyişmir.
- Əlçatanlıq: imtahan vaxtı LMS dayanmır, qeydiyyatda sorğular işləyir.
- Autentiklik: məlumatın və ya tərəfin iddia olunan mənşəyə uyğunluğu; saxta ödəniş təsdiqi buna zərbədir.
- Məxfilik, tamlıq, əlçatanlıq CIA üçlüyüdür; model hesabatlılığı, imtinanın qarşısının alınmasını və etibarlılığı da əhatə edir.
:::

:::reveal Passiv və aktiv hücum bölgüsü təsirə görə dördlü təsnifatla necə əlaqələnir?
- X.800: passiv hücum məzmunu ələ keçirir və trafik analizi aparır; aktiv hücum bürünmə, replay, dəyişdirmə və xidmətdən imtinadır.
- Təsirə görə dördlük: kəsmə (əlçatanlıq, adətən aktiv), ələ keçirmə (məxfilik, passiv ola bilər), dəyişdirmə (tamlıq, aktiv), saxtalaşdırma (autentiklik, aktiv).
- İki bölgü ayrı suallara cavab verir: hansı xassə pozulur, fəaliyyət passivdirmi.
- Dördünü birlikdə "aktiv" adlandırmaq düzgün deyil; bir insidentdə bir neçə xassə pozula bilər.
:::

:::reveal Hücum aktorunun motivini yalnız görünən IP-dən müəyyən etmək niyə düzgün deyil?
- Motiv davranışa əsaslanan fərziyyədir.
- Xarici IP dövlət mənsubiyyətinin sübutu deyil: infrastruktur icarəyə götürülə və ya ələ keçirilə bilər.
- Siyasi şüar haktivist sübutu deyil, başqa fəaliyyəti gizlədə bilər.
- Atributlaşdırma alternativ izahları və sübutun etibarlılığını yoxlamağı tələb edir.
:::

:::reveal APT hansı xüsusiyyətlərlə təsvir olunur və niyə həmişə zero-day tələb etmir?
- Advanced Persistent Threat: uzun müddət fəaliyyət göstərən, imkanlarını uyğunlaşdıran, girişini saxlayan rəqib.
- Dövlət mənsubiyyətinin sinonimi deyil.
- Hücumçu məqsədinə oğurlanmış parol və standart idarəetmə aləti ilə çatırsa, bahalı naməlum zəifliyə ehtiyac yoxdur.
- Davamlılıq: ilkin hesab bağlansa, alternativ girişdən qayıda bilər.
- Cavab: ələ keçirilən hesab, sessiya və açarlar araşdırılır, məxfi seqment ayrılır.
:::

:::reveal Fişinq, BEC, vişinq və QR fişinqində hansı etibar mexanizmi sui-istifadə olunur?
- Fişinq: tələskənlik və problem hissi; saxta məktub mövcud vəziyyətə uyğun görünür (məsələn, "hesabınız bağlanacaq").
- BEC: tanınmış tədarükçünün və ya rəhbərin real poçt hesabına etibar; məktub poçt yoxlamasından keçə bilər.
- Vişinq: telefonda texniki dəstək kimi təqdim olunan şəxsə etibar.
- QR fişinqi (quishing): QR kodun arxasındakı ünvanın görünməməsi, elana yapışdırılmış koda etibar.
- Ümumi qayda: tələb olunan əməliyyatı universitetin həqiqi prosesi ilə yoxlamaq.
:::

:::reveal Parol püskürtməsi ilə sızmış hesab cütlərinin sınanması necə fərqlənir?
- Password spraying: az sayda parol çoxlu hesaba yayılır, hesab üzrə hədd aşılmır.
- Credential stuffing: başqa xidmətdən sızmış istifadəçi adı və parol cütləri sınanır.
- Aşkarlama: hesab üzrə cəhdlərlə yanaşı mənbə üzrə fərqli hesablar da sayılır; yalnız IP həddi ortaq NAT-ı bloklaya və hücumçunu buraxa bilər.
:::

:::reveal MFA olan hesabın sessiyası hansı hallarda yenə risk altında qala bilər?
- MFA yorğunluğu: təkrar təsdiq bildirişləri istifadəçini birini qəbul etməyə məcbur edir.
- Aralıq proksi ilə fişinq sessiya tokenini oğurlayır.
- Parol dəyişəndə köhnə sessiyanın avtomatik bağlanacağı fərz edilmir.
- FIDO2/WebAuthn fişinqə daha davamlıdır, amma cihaz və bərpa yolunun qorunmasını əvəz etmir.
:::

:::reveal DDoS zamanı kampus firewall-ı niyə xarici kanalın dolmasını həll etməyə bilər?
- Kanal firewall-a çatmamış operatorun xəttində dolur, qanuni sorğular da orada itir.
- Süzmə operator və ya yuxarı şəbəkə səviyyəsində aparılmalıdır.
- Nümunə: kanal 1 Gbit/s, hücum axını 3 Gbit/s.
- Əvvəlcədən hazırlıq: operatorla əlaqə, trafik təmizləmə, xidmət prioriteti, alternativ xəbər kanalı; tətbiqdə sürət limiti, keş, WAF.
:::

:::reveal SQL inyeksiyası, XSS, CSRF və SSRF-də hansı tərəf hansı məlumatı etibarlı sayır?
- SQL inyeksiyası: verilənlər bazası istifadəçi girişini sorğu əmri kimi qəbul edir.
- XSS: brauzer etibarsız məzmunu proqram kimi icra edir.
- CSRF: sayt brauzerin avtomatik göndərdiyi sessiyaya etibar edir (sui-istifadə obyekti brauzer sessiyasıdır).
- SSRF: server istifadəçi təsirli ünvana sorğu göndərir (sui-istifadə obyekti serverin şəbəkə çıxışıdır).
- Tədbirlər: parametrli sorğu, kontekstə uyğun kodlaşdırma, CSRF tokeni/SameSite, çıxışı və ünvanları məhdudlaşdırmaq.
:::

:::reveal CVE və CWE hansı fərqli təsvir səviyyələrinə aiddir?
- CVE konkret ictimai zəifliyi adlandırır (CVE-2021-44228, Log4Shell); düzəlişi izləməyə kömək edir.
- CWE zəiflik növünü təsnif edir (CWE-89, SQL inyeksiyası); səhvin təkrarlanma səbəbini öyrənməyə kömək edir.
- Bir CWE sinfinə çoxlu CVE uyğun gələ bilər; daxili tətbiqdə CVE olmasa da CWE tipli səhv ola bilər.
:::

:::reveal CVSS v4.0 qrupları nəyi göstərir, EPSS və KEV hansı əlavə sualları cavablandırır?
- Base: hücum yolu, mürəkkəblik, imtiyaz, istifadəçi iştirakı, təsir; Threat: təhdid göstəriciləri; Environmental: mühit; Supplemental: kontekst, yekun bala təsir etmir. Bal 0–10.
- EPSS: yaxın 30 gündə istismarın müşahidə olunma ehtimalı (0,20 = 20 faiz, universitetin sındırılma ehtimalı deyil).
- KEV: real istismarı məlum zəifliyin CISA kataloqunda olub-olmaması; olmamaq zəmanət deyil.
- CVSS texniki ciddiliyi, EPSS ehtimalı, KEV isə real istismarı göstərir.
:::

:::reveal Şəbəkəyə açıq zəiflik ilə təcrid edilmiş yüksəkballı zəiflik arasında prioritet necə seçilir?
- Əvvəl inventar: məhsul və versiya varmı, funksiya açıqdırmı, hansı hüquqlara çıxış verir.
- Sonra istismar sübutu, CVSS, EPSS, aktivin dəyəri, müvəqqəti tədbirlər.
- İnternetə açıq, KEV-də olan 8,1 ballı şlüz təcili; təcrid edilmiş 9,8 ballı VM-in izolyasiyası yoxlanır, düzəliş planlanır.
- Yamaq artıq daxil olmuş hücumçunun sessiyasını və hesabını silmir, kompromitasiya yoxlanır.
:::

:::reveal Təhlükəsizlik siyasəti, prosedur və texniki sazlama bir-birinə necə bağlanır?
- Siyasət nəyin qorunduğunu, məsulları, qəbul edilən riski və yoxlamanı müəyyən edir; üç səviyyə: rəhbərlik məqsədləri, LMS/poçt/uzaq giriş qaydaları, konkret sazlamalar və təlimatlar.
- Prosedur konkret addımları, texniki vasitə yoxlamanı və məhdudiyyəti həyata keçirir.
- Nümunə: "qiyməti yalnız səlahiyyətli şəxs dəyişir" siyasəti varsa, tətbiqdə yoxlama, təsdiq prosesi və audit qeydi də olmalıdır.
- Siyasəti rəhbərlik təsdiqləyir, çatdırır və yeniləyir.
:::

:::reveal CTI-nin dörd səviyyəsi eyni kampaniya haqqında necə fərqli məhsullar yaradır?
- Strateji: rektorluq və İT rəhbəri; tədqiqat hesablarının itirilməsinin nəticələri; qərar MFA və seqmentləşdirməyə resurs ayırmaq.
- Əməliyyat: CSIRT və növbətçilər; konfrans dəvəti adı ilə konkret kampaniya; əhatəni və cavab hazırlığını müəyyən etmək.
- Taktiki: aşkarlama mühəndisi; poçtdan sonra skript və kənar əlaqə ardıcıllığı; davranış qaydası.
- Texniki: SOC və müdafiə sistemləri; domen, URL, heş, vaxt və etibar; uyğunluğu axtarmaq, əsaslı halda bloklamaq.
:::

:::reveal Kəşfiyyatın həyat dövründə əks-əlaqə niyə tələb mərhələsinə qayıdır?
- Dövr: tələblər, toplama, emal, təhlil, yayma, əks-əlaqə.
- Əks-əlaqədə məlumatın hansı qərarı dəyişdiyi, tədbirin işləyib-işləmədiyi, yanlış müsbətlərin sayı, çatışmayan sahə soruşulur.
- Nəticə yeni və dəqiqləşmiş tələblərə çevrilir (məsələn, köhnə IP kitabxananı bloklayıbsa, etibarlılıq müddəti və bloklama prosesi düzəldilir).
:::

:::reveal IoC, IoA və TTP anlayışları hansı hallarda bir-birini tamamlayır?
- IoC: heş, domen, IP kimi texniki əlamət; sadə və sürətli, amma tez köhnəlir.
- IoA: davranış ardıcıllığı (sənəddən skript, kənar əlaqə, avtomatik başlanğıc); dəyişən ünvanlara davamlıdır, qanuni avtomatlaşdırma ilə qarışa bilər.
- TTP: məqsəd, üsul, icra forması; davranışı ümumiləşdirir, keyfiyyətli xəritələmə və görünürlük tələb edir.
- Birlikdə: IoC cari nümunələri tutur, IoA/TTP kampaniya dəyişəndə də işləyir.
:::

:::reveal Ağrı piramidasının yuxarı pillələri niyə daha çox müdafiə əməyi tələb edir?
- Aşağıdan yuxarı: heş, IP, domen, artefakt, alət, TTP.
- Aşağıda bloklamaq ucuzdur, amma hücumçu heşi bir baytla, IP-ni dəqiqələrlə dəyişir.
- Yuxarıda hücumçunu bütün iş üsulunu dəyişməyə məcbur edir.
- Müdafiəçi üçün davranış qaydasının sınağı, yanlış müsbətlərin təhlili və sensorların işləməsi daha çox əmək tələb edir. Yuxarı pillə aşağıları ləğv etmir.
:::

:::reveal Mənbə etibarlılığı, məlumatın doğruluğu, ehtimal və etibar dərəcəsi necə ayrılır?
- Mənbənin etibarlılığı ilə konkret məlumatın doğruluğu ayrı qiymətləndirilir: etibarlı tərəfdaş səhv edə bilər.
- Ehtimal hadisənin baş vermə qiymətləndirməsidir.
- Etibar dərəcəsi həmin qiymətləndirmənin sübut gücünü bildirir; yüksək ehtimal aşağı etibarla yanaşı ola bilər.
- Hesabat bunları bir "risk yüksəkdir" cümləsinə sıxışdırmamalıdır.
:::

:::reveal STIX, TAXII və MISP eyni mübadilə prosesində hansı fərqli işləri görür?
- STIX 2.1: məlumatın maşınla emal olunan formatı (indikator, kampaniya, əlaqə obyektləri).
- TAXII 2.1: HTTPS üzərindən ötürmə protokolu (API kökü, kolleksiyalar).
- MISP: hadisə, atribut, obyekt, taksonomiya və paylaşma qrupları ilə işləyən platforma; MISP formatı STIX ilə eyni deyil.
- STIX TAXII olmadan da ötürülə bilər; TAXII-dən almaq etibarlılığı təsdiqləmir.
:::

:::reveal TLP:AMBER, TLP:AMBER+STRICT və TLP:GREEN arasında paylaşma fərqi nədir?
- AMBER+STRICT: yalnız öz təşkilatı daxilində, bilməli olanlarla.
- AMBER: təşkilat və onun müştəriləri, müdafiə üçün bilməli olduqları qədər; bütün tərəfdaşlara sərbəst göndərmək deyil.
- GREEN: öz icması daxilində (digər universitetlər, AzScienceCERT icması), açıq kanalda deyil.
- TLP texniki giriş nəzarəti və hüquqi təsnifat deyil.
:::

:::reveal Universitetdə CTI-nin faydasını yalnız indikator sayına görə ölçmək niyə yanlışdır?
- Çox indikator keyfiyyət deyil: əsas ölçülər tələbə uyğunluq, tədbirə çevrilmə vaxtı, indikatorun aktuallığı, xəbərdarlıq dəqiqliyi, aşkarlama örtüyü, qərara təsirdir.
- Dəqiqlik: 40 uyğunluğun 10-u təsdiqlənibsə 10/40 = 25 faiz; bu, hücumların dörddə birinin tapıldığını göstərmir, çünki aşkarlanmayanlar məlum deyil.
- Az xəbərdarlıq sakit mühit və ya işləməyən toplama demək ola bilər.
:::

## Situasiya tapşırıqları

**Situasiya 1.** Universitet maliyyə şöbəsinə tanınmış tədarükçünün real hesabından məktub gəlir. Bank rekvizitinin dəyişdiyi deyilir. Poçt autentifikasiyası yoxlamaları uğurludur. Ödəniş göndərilməlidirmi?

:::reveal Cavab
- Ssenari: BEC (Business Email Compromise). Pozulan: pul və tamlıq (ödənişin düzgün təyinatı).
- Səbəb: real hesab ələ keçirilə bilər; poçt yoxlaması göstərişin qanuniliyini təsdiqləmir.
- Tədbir: dəyişikliyi əvvəldən qeydə alınmış əlaqə kanalı ilə yoxla, ikinci səlahiyyətli şəxs təsdiq etsin; məktubdakı telefona etibar etmə.
- Şübhə qalarsa ödəniş saxlanılır, məktub sübut kimi qorunur.
:::

**Situasiya 2.** Şərti universitetdə uzaq giriş şlüzünün zəifliyi CVSS 8,1 bal alıb və KEV-dədir. Ayrı sınaq şəbəkəsindəki VM-də 9,8 ballı zəiflik var. Administrator əvvəlcə böyük balı düzəltmək istəyir. Qərarı qiymətləndirin.

:::reveal Cavab
- Əvvəl məhsul və versiya uyğunluğu təsdiqlənir.
- Şlüz İnternetə açıqdır və real istismarı məlumdur (KEV): təcili üstünlük; onun hesab və daxili şəbəkəyə təsiri yoxlanılır.
- Sınaq VM-inin izolyasiyası təsdiqlənir, düzəliş planlaşdırılır.
- Şlüz üçün yamaqla yanaşı əvvəlki kompromitasiya əlamətləri araşdırılır.
- Nəticə: tək CVSS sıralaması yetərli deyil.
:::

**Situasiya 3.** CTI axınındakı IP bloklandıqdan sonra tələbələr elektron kitabxanaya girə bilmirlər. İndikatorun son müşahidəsi iki il əvvələ aiddir və ünvan paylaşılan hostinqdədir. Hansı proses dəyişməlidir?

:::reveal Cavab
- Səhv: köhnəlmə, ortaq infrastruktur və xidmətə təsir yoxlanmayıb (pozulan: əlçatanlıq).
- Bloklama geri qiymətləndirilir, təhlükəsiz dar alternativ (domen, URL və ya monitorinq) seçilir, qərar qeydə alınır.
- İndikatora yenidən baxılma vaxtı əlavə olunur, avtomatik ixracdan əvvəl kontekst yoxlanır.
- Səhv paylaşılmışsa, düzəliş digər alıcılara da çatdırılır.
:::

**Situasiya 4.** Yataqxana şəbəkəsindən DNS-də zərərli domen uyğunluğu tapılıb. Poçt sistemi həmin keçidi avtomatik yoxlayır, cihazda isə EDR yoxdur. Analitik "tələbənin kompüteri yoluxub" yazır. Bu nəticə əsaslıdırmı?

:::reveal Cavab
- Əsaslı deyil: DNS uyğunluğu sorğunu təsdiqləyir, yoluxmanı təsdiqləmir.
- Mənbə cihazı, avtomatik yoxlayıcı, proksi bağlantısı, giriş və istifadəçi məlumatı araşdırılır.
- EDR görünürlüyünün olmaması hesabatın məhdudiyyəti kimi yazılır.
- Yoluxma fərziyyəsi saxlanılır, amma digər izahlar yoxlanmadan təsdiqlənmiş fakt elan edilmir.
:::

**Situasiya 5.** Tərəfdaş universitet TLP:AMBER+STRICT ilə hesabat göndərib. Yerli əməkdaş mənbə adını silib onu bütün universitetlər üçün açıq kanala yerləşdirmək istəyir. Bu addımı qiymətləndirin.

:::reveal Cavab
- Etiket paylaşmanı alıcının təşkilatı daxilində, bilməli olan şəxslərlə məhdudlaşdırır.
- Mənbənin anonimləşdirilməsi bu sərhədi götürmür.
- Açıq yayım üçün mənbənin icazəsi alınmalı, şəxsi məlumat ayrıca yoxlanmalıdır.
- TLP texniki giriş nəzarəti deyil: paylaşma qrupu və ixrac qaydası məhdudiyyəti tətbiq etməlidir.
:::

**Situasiya 6.** Universitet hər gün fərqli heşli faylları bloklayır, amma eyni kampaniya davam edir. Son qurğu qeydlərində sənəd proqramından skript interpretatoru başlayır və sonra xarici əlaqə yaranır. Müdafiə necə genişləndirilməlidir?

:::reveal Cavab
- Heş nəzarəti saxlanılır, amma heş Ağrı piramidasının aşağısıdır.
- Sənəd–skript–əlaqə ardıcıllığı üçün davranış qaydası (IoA/TTP) hazırlanır və qanuni avtomatlaşdırma ilə sınaqdan keçirilir.
- Dəstəkləyici qeydlər və ATT&CK xəritələməsi sənədləşdirilir.
- İnternetdən gələn faylların icra məhdudiyyətləri və istifadəçi hüquqları yoxlanır.
- Bu, piramidada davranışa doğru keçiddir.
:::

**Situasiya 7.** Şərti imtahan günü LMS-ə trafik üç dəfə artıb. Komanda bunu DDoS sayaraq yataqxananın çıxış IP-sini bloklamaq istəyir. Hansı məlumatlar qərarı dəyişə bilər?

:::reveal Cavab
- Yoxlanır: imtahan təqvimi, uğurlu autentifikasiya, fərqli hesabların normal fəaliyyət payı, sorğu yolları, serverin resursları.
- Ortaq NAT arxasında çoxlu qanuni tələbə ola bilər; IP-ni bloklamaq tədrisi dayandırar (əlçatanlıq).
- Hücum təsdiqlənərsə: dar tətbiq qaydası və operator dəstəyi.
- Normal tələb artımıdırsa: tutum və tətbiq səmərəliliyi düzəldilir.
:::

**Situasiya 8.** Dil modeli açıq hesabatdan universitet üçün indikator siyahısı çıxarıb. Siyahıda olmayan CVE-yə istinad və "bütün domeni bloklayın" göstərişi var. Analitik nəticəni avtomatik tətbiq etməlidirmi?

:::reveal Cavab
- Xeyr: model çıxışı ilkin mənbə ilə yoxlanır, CVE qeydi və domenin konteksti ayrıca təsdiqlənir.
- Hesabatdakı göstəriş etibarlı əməliyyat təlimatı sayılmır (hücumçu mətnə göstəriş yerləşdirə bilər).
- Uydurulmuş əlaqələr çıxarılır, paylaşma hüququ və xidmətə təsir yoxlanır.
- Avtomatlaşdırma yalnız əvvəlcədən səlahiyyət verilmiş, yoxlanmış şərtlərlə işləməlidir.
:::

## Konspektdən situasiyalar

**Situasiya 1.** Universitetə dörd sənəd gəlir: (a) Cənubi Qafqazda geosiyasi gərginlik fonunda təhsil sektoruna hücumların artacağı barədə hesabat; (b) konkret qrupun ilkin giriş üçün saxta "imtahan cədvəli" PDF-ləri, sonra PowerShell işlətdiyini təsvir edən analiz; (c) bu qrupun gələn həftə Bakı universitetlərinə qarşı kampaniya hazırladığı barədə xəbərdarlıq; (d) 20 zərərli domen və 5 fayl heşi siyahısı. Hər birini təsnif et və kimə verilməli olduğunu de.

:::reveal Cavab
- (a) Strateji: rektorluğa və İT direktoruna, büdcə və prioritet qərarları üçün.
- (b) Taktiki (TTP): SOC rəhbəri və sistem adminlərinə; zərərli PDF-ləri süzmək, PDF oxuyucularını yeniləmək, PowerShell loglamasını açmaq üçün.
- (c) Əməliyyat: insidentə cavab komandasına; növbətçiliyi gücləndirmək və işçiləri xəbərdar etmək üçün.
- (d) Texniki (IoC): SIEM, firewall, e-poçt şlüzü və EDR-ə avtomatik yükləmək üçün.
- Açar: auditoriya və qərar.
:::

**Situasiya 2.** SOC analitiki təhdid feed-indən gələn bir IP-ni firewall-da bloklayır. Ertəsi gün universitetin bütün tələbələri onlayn kitabxanaya girə bilmir. Məlum olur ki, həmin IP iki il əvvəl zərərli imiş, indi isə böyük bulud provayderinin paylaşılan ünvanıdır və kitabxana xidməti də orada yerləşir. Hansı səhvlər edilib?

:::reveal Cavab
- IoC köhnəlmişdi (IP-lər tez sahibini dəyişir) və paylaşılan infrastrukturda idi.
- Analitik IoC-ni kontekstsiz tətbiq edib: son görülmə tarixinə, etibar dərəcəsinə və IP-nin kimə aid olduğuna (zənginləşdirmə) baxmayıb.
- Bloklama biznes təsiri yoxlanmadan edilib (pozulan xassə: əlçatanlıq).
- Düzgün yanaşma: IoC-lərin müddəti olsun, bloklamadan əvvəl zənginləşdirilsin, paylaşılan IP üçün tam bloklama əvəzinə monitorinq və ya daha dar qayda (konkret domen, URL) seçilsin.
- Bu, IP-nin piramidanın aşağı pilləsində olduğunu göstərir.
:::

**Situasiya 3.** Universitetin İT təhlükəsizlik komandası bir ransomware qrupunun yeni nümunələrinin heşlərini hər gün antivirus və e-poçt şlüzündə bloklayır, amma qrup hər dəfə faylın heşini dəyişib onu müəllimlərə yenidən göndərir. Strategiyanı necə dəyişmək olar?

:::reveal Cavab
- Heşlər Ağrı piramidasının ən aşağısındadır: hücumçu bir baytı dəyişməklə yeniləyir.
- Diqqət yuxarı pillələrə keçirilir: qrupun alətləri (məs. eyni yükləyici) və davranışları (TTP: Word-ün PowerShell başlatması, kölgə nüsxələrin silinməsi, kütləvi fayl adı dəyişikliyi) üçün EDR və SIEM qaydaları.
- Qaydalar MITRE ATT&CK texnikalarına bağlanır.
- Office makroları İnternetdən gələn fayllarda bloklanır.
- Hücumçu faylı dəyişsə də, davranışı tutulacaq.
:::

## Ehtimal olunan əlavə suallar

:::reveal İdentifikasiya, autentifikasiya və avtorizasiya arasındakı fərq nədir?
- İdentifikasiya: subyektin özünü adlandırması.
- Autentifikasiya: bu iddianın yoxlanması.
- Avtorizasiya: yoxlanmış subyektə hansı əməliyyatın icazəli olduğunu müəyyən etmək.
- Nümunə: obyekt identifikatorunu dəyişib başqa tələbənin sənədini açmaq autentifikasiya yox, avtorizasiya (giriş nəzarəti) problemidir (OWASP A01 Broken Access Control).
:::

:::reveal Taktiki və texniki kəşfiyyatı necə ayırmaq olar?
- Taktiki: hücumçunun TTP-ləri (taktika, texnika, prosedur); SOC rəhbəri və müdafiə arxitektorları üçün; müdafiə qaydasına bağlanır.
- Texniki: IoC-lər (IP, domen, URL, heş, imza); SOC analitikləri, firewall, SIEM, EDR üçün; tez köhnəlir.
- Tələ: bəzi sertifikat proqramları (CompTIA) IoC-ləri taktiki sayır; imtahanda müəllimin bölgüsü işlədilir. Ən etibarlı açar auditoriyadır.
:::

:::reveal Zero-day anlayışını izah edin və niyə dəqiq vəziyyət yazılmalıdır?
- Mənbələrdə sərhəd fərqlidir: istehsalçının bilmədiyi zəiflik və ya istismar zamanı düzəlişi olmayan zəiflik.
- Hesabatda dəqiq yazılır: "istismar müşahidə ediləndə istehsalçı düzəlişi mövcud deyildi".
- Universitetin yeniləməni quraşdırmadığı, çoxdan düzəldilmiş zəifliyi zero-day adlandırmaq düzgün deyil.
:::

:::reveal Risk dəyərini kəmiyyətlə necə hesablamaq olar və məhdudiyyəti nədir?
- Ehtimal ilə zərərin hasili: illik ehtimal 0,1 × zərər 50 000 manat = 5 000 manat gözlənilən illik itki.
- Yalnız ölçülərin mənası və fərziyyələr aydın olduqda faydalıdır.
- Nəticə zəmanətli proqnoz deyil; ehtimallar qeyri-dəqiq ola bilər, məxfilik pozuntusunun nəticəsi pulla tam ifadə edilməyə bilər.
:::

:::reveal Kəşfiyyatla xam məlumat arasındakı fərq nədir?
- Xam məlumat müşahidədir: "bu IP-dən bağlantı gəldi".
- Kəşfiyyat (CTI) yoxlanmış, kontekstləşdirilmiş, qərara yarayan bilikdir: "bu bağlantı təsdiqlənmiş zərərli domenlə əlaqəlidir, serverdə naməlum proses başlayıb, ayırmaq araşdırılmalıdır".
- Mənbə yalnız İnternet deyil: daxili jurnallar, insident araşdırması, zərərli proqram analizi, tərəfdaşlarla mübadilə (NIST SP 800-150).
- Məqsəd yalnız qarşısını almaq deyil, aşkarlama və insidentə cavabdır.
:::

:::reveal Analitik qərəzləri sadalayın və qarşı tədbirləri deyin.
- Təsdiqləmə qərəzi: ilkin fikrə uyğun faktları seçmək; qarşı tədbir: hər fərziyyəni zəiflədən sübutu ayrıca yazmaq.
- Lövbərlənmə: ilk IP və ya qrup adına bağlanmaq; qarşı tədbir: hesab, cihaz, zaman əlaqələrini qurmaq.
- Əlçatanlıq qərəzi: son oxunan hadisəni hər insidentə tətbiq etmək; qarşı tədbir: qrup adından əvvəl müşahidəni təsvir etmək.
- Avtomatlaşdırmaya etibar və seçmə qərəzi (yalnız EDR-li cihazlar).
:::

:::reveal Sosial mühəndislik formalarını sadalayın və mexanizmlərini deyin.
- Fişinq (kütləvi), spear phishing (şəxsə uyğun), whaling (rəhbərlər).
- Vişinq (telefon), smişinq (SMS), quishing (QR kod).
- BEC (ödəniş və ya rekvizit tələbi), pretexting (uydurma ssenari), tailgating (qapıdan keçmə), baiting (cəlbedici yem).
- Deepfake rəhbərin səsini və üzünü təqlid edir; iki nəfərin təsdiqi və əvvəlcədən müəyyən kanal daha etibarlıdır.
:::

:::reveal Yalnız CVSS-ə əsaslanmaq niyə yanlışdır və düzgün prioritet necə seçilir?
- CVSS texniki ciddiliyi göstərir, bu gün hücum olunma ehtimalını və universitetdəki istismarı yox.
- Əlavə siqnallar: EPSS (30 gündə istismar ehtimalı), KEV (real istismar).
- Düzgün prioritet: real istismar olunurmu, sistem İnternetə açıqdırmı, aktiv nə qədər kritikdir (inventarla birlikdə).
- "Ən böyük balı əvvəl yamaq" bu əlaqələri itirir.
:::

:::reveal Kəşfiyyat tələbi (PIR) nədir və yaxşı tələbi pisindən necə ayırmaq olar?
- PIR (Priority Intelligence Requirement) qərar üçün hansı biliyin çatışmadığını ifadə edir.
- "Bütün hücumları izləmək" yoxlanıla bilən tələb deyil.
- Yaxşı tələb: "Semestr qeydiyyatı zamanı tələbə hesablarının ələ keçirilməsində hansı giriş yolları bizim mühitdə işləyə bilər?"
- Alıcı, qərarın vaxtı və istifadə ediləcək tədbir əvvəlcədən yazılır.
:::
