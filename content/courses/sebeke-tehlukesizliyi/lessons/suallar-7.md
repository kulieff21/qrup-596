+++
title = "Tələ sistemləri, proksi-serverlər və virtual özəl şəbəkələr (VPN)"
unit = "suallar"
order = 7
summary = "Mövzu 7 üzrə imtahana hazırlıq: mühazirənin nəzarət sualları və situasiya tapşırıqları cavablarla, konspektdən situasiyalar və ehtimal olunan əlavə suallar."
updated = 2026-11-09

[[source]]
title = "Mühazirə 7: Tələ sistemləri, proksi-serverlər və virtual özəl şəbəkələr (VPN)"
note = "Elmar Cabbarov, 2026–2027"

[[source]]
title = "Midterm konspekti, Mövzu 7"
note = "Elmar Cabbarov"
+++

Əvvəl cavabı özün yaz, sonra aç. Situasiya cavablarını bu ardıcıllıqla qur: aktiv, pozulan xassə, səbəb, tədbir, yoxlama.

## Nəzarət sualları

### Tələ sistemləri üzrə

:::reveal Tələ sisteminin yanlış həyəcanları niyə IDS-dən azdır?
- Tələnin heç bir iş funksiyası yoxdur, ona gələn istənilən bağlantı şübhəlidir.
- IDS milyonlarla normal paketin içindən zərərlini seçməyə çalışır və yanılır; tələdə “normal trafik” anlayışı yoxdur.
- Nəticə: yanlış həyəcan çox azdır, məlumat həcmi kiçik, amma dəyərlidir.
:::

:::reveal Aşağı, orta və yüksək qarşılıqlı əlaqəli tələləri məlumat və risk baxımından müqayisə edin.
- **Aşağı (low-interaction):** bir neçə xidmət/protokol təqlid olunur, real ƏS yoxdur; az məlumat (IP, port, giriş cəhdləri), aşağı risk; Honeyd, Dionaea.
- **Orta (medium-interaction):** hücumçu saxta fayl sistemində əmr yazır, real ƏS-də icra olunmur; orta məlumat (əmrlər, fayllar), orta risk; Cowrie shell rejimi.
- **Yüksək (high-interaction):** real ƏS və xidmətlər; ən çox məlumat, yeni zəifliklər; ən yüksək risk, hücumçu kök hüququ qazanıb tələni bazaya çevirə bilər.
- Qayda: hücumçuya nə qədər çox imkan, bir o qədər çox məlumat və risk.
:::

:::reveal Honeypot, honeynet və honeytoken arasında fərq nədir?
- **Honeypot:** tək saxta sistem.
- **Honeynet:** bir neçə tələdən ibarət saxta şəbəkə; tələlər arasında hərəkəti (lateral movement) və çoxhostlu ardıcıllığı göstərir.
- **Honeytoken:** sistem deyil, saxta məlumat parçası (hesab, “parollar.xlsx”, saxta tələbə sətri, API açarı); istifadə olunan kimi həyəcan verir, daxili sızmanı tutur.
:::

:::reveal Tədqiqat və istehsalat tələlərinin məqsədi necə fərqlənir?
- **İstehsalat (production):** təşkilatın şəbəkəsində daxilə keçmiş hücumçunu tez görmək; sadə, az resurs.
- **Tədqiqat (research):** yeni hücum üsulları, zərərli proqram, botnet davranışı; universitetlər, CERT-lər, antivirus şirkətləri; çox məlumat, amma qurulması və nəzarəti çətin.
:::

:::reveal Tələdən çıxan trafiki niyə bağlamaq lazımdır?
- Ələ keçirilmiş tələ başqalarına hücum üçün sıçrayış nöqtəsinə (pivot) çevrilə bilər.
- Hücum universitetin IP ünvanından gəlmiş kimi görünər, məsuliyyət məsələsi yaranar.
- Çıxış firewall ilə kəsilir; yalnız log serverinə yol açıq qalır.
:::

:::reveal Logları niyə tələnin özündə saxlamaq olmaz?
- Hücumçu tələdə kök hüququ alıb izini silə bilər, qeydlər etibarsız olar.
- Loglar dərhal kənar serverə (SIEM) göndərilir.
- Əlavə: şəbəkə və hipervizor səviyyəsində müstəqil trafik yazısı, sübut üçün sinxron vaxt və chain of custody.
:::

:::reveal Data control, data capture və data collection nə deməkdir?
- **Data control:** ələ keçirilmiş tələnin başqalarına ziyan vurmasının qarşısını alır.
- **Data capture:** hücumçunun hər şeyini, o xəbər tutmadan qeydə alır.
- **Data collection:** bir neçə tələnin qeydlərini mərkəzdə birləşdirir.
- Bunlar Honeynet Layihəsinin tələ arxitekturasına tələbləridir.
:::

:::reveal Təcrübəli hücumçu tələni hansı əlamətlərdən tanıya bilər?
- Standart SSH banner-i.
- Cavab vaxtının qeyri-təbiiliyi.
- Virtualizasiya izləri.
- Həmişə eyni görünən saxta fayl sistemi.
- Shodan kimi axtarış sistemlərinin etiketi. Həll: standart parametrlər işlətməmək, host adı, fayl sistemi və xidmətləri real serverlərə oxşatmaq.
:::

:::reveal Tələ sistemi hansı halda heç bir hücumu görməyəcək?
- Hücumçu tələyə toxunmayıb başqa sistemə (məsələn, birbaşa LMS serverinə) gedəndə.
- Tələ yalnız ona gələn trafiki görür, ona görə IDS və SIEM-i əvəz etmir, onları tamamlayır.
- İnternetə açıq tələ daxili hücumu da görmür.
:::

:::reveal Daxili tələ ilə İnternetə açıq tələnin göstəricilərini müqayisə edin.
- **İnternetə açıq:** gündə minlərlə skan, ümumi hücum mənzərəsi; çox “internet səs-küyü”; göstərici: unikal mənbə sayı, ən çox sınanan parollar, yeni fayl heşləri, hədəflənən protokollar.
- **Daxili:** hər bağlantı demək olar ki, insidentdir (skan, yoluxmuş cihaz, daxili pozucu); göstərici: pentest toxunanda xəbərdarlığın SOC-a çatma vaxtı və cihazın tapılma vaxtı; sıfır xəbərdarlıq yaxşı işarə ola bilər.
:::

### Proksi-serverlər üzrə

:::reveal Düz və tərs proksi kimi təmsil edir? Hərəsinə bir universitet nümunəsi deyin.
- **Düz proksi müştərini təmsil edir:** tələbə və işçi kompüterləri Squid vasitəsilə çıxır, sayt proksinin IP-sini görür.
- **Tərs proksi serveri təmsil edir:** DMZ-dəki Nginx universitet portalının qarşısındadır, müştəri yalnız proksini görür, backend ünvanını bilmir.
:::

:::reveal Proksi niyə iki ayrı bağlantı qurur və bu ona nə imkan verir?
- Müştəri–proksi və proksi–server ayrı bağlantılardır (UDP/QUIC-də də ayrı əlaqələr).
- Proksi ortada dayandığı üçün tətbiq səviyyəsində məlumatı oxuya, dəyişdirə, keşləyə və qadağan edə bilir.
- İstifadəçiyə, URL-ə, məzmuna görə qərar verə bilir.
:::

:::reveal Proksi ilə NAT arasında üç fərq deyin.
- NAT paket başlığındakı IP və portu dəyişir; proksi iki ayrı bağlantı qurur (NAT-da bağlantı birdir).
- NAT 3–4 səviyyədə, proksi 5–7 səviyyədə işləyir.
- NAT məzmuna baxmır, istifadəçiyə/URL-ə görə qərar vermir; proksi autentifikasiya edir, domen siyasəti tətbiq edir, faylları yoxlayır və tətbiq səviyyəli qeyd verir.
- Hər ikisi daxili ünvanı gizlədir, amma eyni şey deyil.
:::

:::reveal CONNECT tuneli zamanı proksi nəyi görür, nəyi görmür?
- **Görür:** domen adı (CONNECT sətri və SNI), port, vaxt, ötürülən həcm.
- **Görmür:** URL yolunu, səhifə məzmununu, parolları, faylları, çünki TLS brauzerlə sayt arasındadır.
- ECH SNI-ni də şifrələyəcək.
:::

:::reveal TLS yoxlaması üçün müştəri kompüterində nə edilməlidir və bu hansı riskləri yaradır?
- Proksi iki ayrı TLS qurur; sertifikatı təşkilatın CA-sı imzalayır və CA müştəriyə etibarlı kimi yüklənməlidir.
- Riskler: razılaşdırılmış MITM, proksi parolları, tibbi və bank məlumatını görür; proksi ələ keçirilsə, bütün şifrəli trafik açılır; pinning edən tətbiqlər işləməyə bilər.
- Tədbirlər: bank, səhiyyə, dövlət kateqoriyalarını çıxarmaq, istifadəçiləri xəbərdar etmək, CA açarını HSM-də saxlamaq.
:::

:::reveal TLS-in proksidə dayandırılması nə deməkdir?
- Tərs proksi TLS-i özündə bitirir: sertifikat və şifrələmə bir yerdə idarə olunur, hər tətbiq serverində sertifikat lazım olmur.
- Risk: proksi ilə tətbiq arasındakı trafik açıq gedə bilər; “saytda HTTPS var” daxili şifrələmə demək deyil.
- Həll: re-encryption və backend sertifikatının, host adının yoxlanması (`proxy_ssl_verify on`).
:::

:::reveal X-Forwarded-For başlığına niyə kor-koranə etibar etmək olmaz?
- Başlığı hücumçu sorğusuna əvvəlcədən yaza bilər (məsələn, `10.0.0.1`), siyahının sol tərəfini müştəri yazır.
- Nəticə: IP məhdudiyyətindən, sürət limitindən yan keçmə, qeydlərin saxtalaşdırılması.
- Həll: kənar proksi başlığı üzərinə yazır; siyahı sağdan oxunur, etibarlı proksilər çıxılır.
:::

:::reveal SOCKS proksi HTTP proksidən nə ilə fərqlənir?
- **HTTP proksi** HTTP-ni başa düşür: URL, başlıq, metod üzrə qərar verir.
- **SOCKS (SOCKS5)** sessiya səviyyəsindədir, istənilən TCP/UDP trafikini ötürür, məzmunu şərh etmir və şifrələmə vermir.
:::

:::reveal Açıq proksi niyə təhlükəlidir?
- Hər kəsə xidmət edən səhv sazlanmış və ya qəsdən açılmış proksidir.
- Spam, hücum və blokdan yan keçmək üçün istifadə olunur; hücumçular izi itirmək üçün işlədir.
- Giriş siyahısı olmayan Squid-də universitetin IP-si qara siyahıya düşür. Həll: son qayda `http_access deny all`.
:::

:::reveal Şəffaf proksi müştəri tərəfində nəyi tələb etmir?
- Brauzerdə və ya sistemdə heç bir sazlama tələb etmir.
- Marşrutlaşdırıcı və ya firewall HTTP trafikini proksiyə yönəldir; qonaq Wi-Fi və provayderlərdə işlədilir.
:::

### VPN üzrə

:::reveal VPN hansı üç təhlükəsizlik xidmətini verir?
- **Məxfilik:** tuneldəki məlumat yolda oxunmur.
- **Tamlıq:** yolda dəyişdirmə aşkar edilir.
- **Autentifikasiya:** tərəflər bir-birinin kimliyini yoxlayır.
- IPsec-də buna təkrar göndərmədən qorunma (anti-replay) da əlavə olunur.
:::

:::reveal VPN nəyi qorumur? İki nümunə deyin.
- Tunelin ucundan o yana yolu, məsələn VPN şlüzündən veb saytına qədər.
- İstifadəçinin yoluxmuş kompüterini: zərərli proqramlı noutbuk VPN-ə qoşulanda zərərli proqram da tunellə şirkət şəbəkəsinə girir.
- VPN etibarsız şəbəkə üzərindən qorunan kanal qurur, şəbəkənin özü etibarsız qalır.
:::

:::reveal Secure və trusted VPN arasında fərq nədir? MPLS hansına aiddir?
- **Secure VPN:** kriptoqrafiya ilə qoruyur (IPsec, OpenVPN, WireGuard).
- **Trusted VPN:** provayderin trafiki öz şəbəkəsində ayırmasına güvənir.
- **MPLS VPN trusted sinfinə aiddir:** məntiqi ayırır, şifrələmir.
- PPTP tarixən “secure” verilsə də, sındırılıb; L2TP tək başına şifrələmir.
:::

:::reveal AH niyə NAT ilə işləmir?
- AH xarici IP başlığını da qoruyur (tamlıq yoxlayır).
- NAT həmin başlığı dəyişir, ona görə yoxlama pozulur.
- AH şifrələmə də vermir; praktikada ESP işlədilir və NAT olanda NAT-T (UDP 4500).
:::

:::reveal Nəqliyyat və tunel rejimlərində orijinal IP başlığına nə olur?
- **Nəqliyyat rejimi:** yalnız faydalı yük qorunur, orijinal IP başlığı açıq qalır (iki host arası).
- **Tunel rejimi:** bütöv orijinal paket şifrələnir, yeni IP başlığı əlavə olunur, daxili ünvanlar görünmür (saytdan sayta).
- Xarici IP başlığı hər iki rejimdə açıqdır.
:::

:::reveal IKEv2-də IKE_SA_INIT və IKE_AUTH nə edir?
- **IKE_SA_INIT:** alqoritmlər razılaşdırılır, Diffie-Hellman açıq dəyərləri və təsadüfi ədədlər mübadilə edilir; IKE SA yaranır, sonrakı mesajlar şifrələnir.
- **IKE_AUTH:** tərəflər sertifikat, EAP və ya PSK ilə autentifikasiya olunur; ilk Child SA, yəni ESP tuneli yaradılır.
- Üçüncü mübadilə CREATE_CHILD_SA əlavə tunel və açar yeniləməsi üçündür (cəmi dörd mesajla tunel).
:::

:::reveal SA və SPI nədir?
- **SA (Security Association):** bir istiqamətdə trafik üçün razılaşdırılmış alqoritm, açar və ömür parametrləri; ikitərəfli rabitə üçün ən azı iki SA.
- **SPI (Security Parameter Index):** paketdə qəbul edənə hansı SA-nı işlədəcəyini göstərir.
- SAD mövcud SA-ları, SPD qorunacaq trafikin siyasətini saxlayır.
:::

:::reveal Niyə PPTP işlədilməməlidir?
- MS-CHAPv2 sındırılıb: tutulmuş mübadilə bir DES açarının (2⁵⁶ variant) axtarışına gətirilir (2012, Marlinspike və Hulton).
- Zəiflik parolun uzunluğundan asılı deyil.
- Microsoft 2024-də RRAS üçün PPTP və L2TP-ni köhnəlmiş elan edib; Windows Server 2025-də yeni quraşdırmada qəbul edilmir.
:::

:::reveal Tam tunel ilə bölünmüş tunelin üstünlük və çatışmazlıqlarını deyin.
- **Tam tunel:** bütün trafik şlüzdən keçir, təhlükəsizlik vasitələri hamısını görür; çatışmazlıq: kanalın yüklənməsi.
- **Bölünmüş tunel:** yalnız təşkilat trafiki tunelə düşür, sürətlidir; çatışmazlıq: İnternet trafiki proksidən və DLP-dən keçmir.
:::

:::reveal DNS sızması nədir və necə qarşısı alınır?
- Tunel olsa da, DNS sorğuları yerli provayderə gedir və sayt adları yolda görünür.
- Həll: VPN müştərisində daxili DNS təyin etmək və marşrutu tuneldən keçirmək; tuneldənkənar DNS-i məhdudlaşdırmaq; IPv4, IPv6 və tətbiqlərin DNS/DoH parametrlərini yoxlamaq; kill switch açmaq.
:::

:::reveal ZTNA VPN-dən hansı məntiqlə fərqlənir?
- Ənənəvi VPN “içəridəsənsə, etibarlısan” məntiqindədir: qoşulan şəbəkənin böyük hissəsini görür, etimad bir dəfə verilir.
- ZTNA (NIST SP 800-207) etimadı şəbəkədəki yerə görə vermir: istifadəçini yalnız icazəli tətbiqə qoşur, kimlik və cihaz vəziyyəti hər dəfə yoxlanır, daxili hərəkət məhduddur, tətbiqlər İnternetdən görünmür.
- ZTNA VPN-in tam əvəzi deyil: saytdan sayta IPsec qalır.
:::

## Situasiya tapşırıqları

**Situasiya 1.** İnformatika fakültəsi SSH hücumlarını öyrənmək üçün universitet saytının serverləri ilə eyni DMZ alt şəbəkəsində tam Linux qurub və ona İnternet çıxışı verib. Loglar həmin Linux-un özündə saxlanılır. Hansı səhvlər var?

:::reveal Cavab
- **Aktiv/nəyə aiddir:** yüksək qarşılıqlı əlaqəli tələ.
- **Səhv 1:** real serverlərlə eyni seqmentdədir, hücumçu oradan universitet saytına keçə bilər (pivot).
- **Səhv 2:** çıxış trafiki açıqdır, tələdən başqalarına hücum edə bilər; hücum universitetin IP-sindən görünər.
- **Səhv 3:** loglar yerindədir, hücumçu izini silə bilər.
- **Düzgünü:** ayrıca izolyasiya olunmuş VLAN, çıxışın bağlanması, logların kənar serverə göndərilməsi, mümkünsə orta səviyyəli Cowrie.
:::

**Situasiya 2.** Təhlükəsizlik mütəxəssisi deyir: “Tələ sistemi həftədə cəmi 3 xəbərdarlıq verir, IDS isə 40 000. Deməli, IDS-i söndürüb yalnız tələ saxlayaq.” Bu qərar düzgündürmü?

:::reveal Cavab
- **Düzgün deyil.**
- Tələ az xəbərdarlıq verir, çünki yalnız ona gələn trafiki görür; LMS-ə, poçta, real veb portala yönəlmiş hücumu görmür.
- IDS-in çoxlu xəbərdarlığı qaydaların tənzimlənməsi məsələsidir.
- **Doğru yanaşma:** tələni əlavə, etibarlı siqnal kimi saxlamaq və IDS-i tənzimləmək.
:::

**Situasiya 3.** Daxili tələyə gecə saat 3-də tələbə laboratoriyasındakı kompüterdən SMB bağlantısı gəlib, ardınca bir neçə administrator parolu sınanıb. Laboratoriya gecə bağlıdır. Komanda nə etməlidir?

:::reveal Cavab
- **Qiymət:** ciddi siqnaldır, çünki tələyə normal yol yoxdur.
- IP ünvanının hansı cihaza aid olduğunu DHCP və NAC qeydlərindən tapmaq.
- Cihazı şəbəkədən ayırmaq, yaddaş və disk surəti götürmək.
- Sınanan parolların real sistemlərdə də işlədilib-işlədilmədiyini SIEM-də yoxlamaq, parolları dəyişmək.
- Laboratoriya kompüteri yoluxmuş ola bilər: eyni zəifliyə malik qonşu cihazlar da yoxlanır.
:::

**Situasiya 4.** Universitet hücumçunu tutmaq üçün İT forumunda “portal bazasının açıq ehtiyat nüsxəsi var” deyə elan yerləşdirib tələyə keçid verməyi planlaşdırır. Hansı problemlər yarana bilər?

:::reveal Cavab
- Passiv gözləmədən aktiv təhrikə keçid: hüquqi risk yaradır.
- Toplanan sübutun etibarlılığı mübahisəli olar.
- Nüfuza zərər: həqiqətən bazanın sızdığı barədə xəbər yayıla bilər.
- **Düzgünü:** tələ daxili şəbəkədə və ya İnternetə açıq ünvanda passiv gözləməli, qurulmazdan əvvəl hüquq xidməti ilə razılaşdırılmalıdır.
:::

**Situasiya 5.** Universitetin İT şöbəsi tələbələrin internetdə hansı URL-lərə daxil olduğunu tam görmək üçün düz proksi quraşdırıb. Amma qeydlərdə yalnız domen adları görünür, səhifə yolları yoxdur. Səbəb nədir və nə etmək olar?

:::reveal Cavab
- **Səbəb:** trafik HTTPS-dir, brauzer CONNECT tunelindən istifadə edir; proksi yalnız domen, vaxt və həcmi görür.
- **Həll:** tam URL üçün TLS yoxlaması: təşkilatın CA-sı müştəri kompüterlərinə yüklənməlidir.
- Tələbələrin şəxsi cihazlarına CA yükləmək məcburi deyil və düzgün deyil.
- Qərar məxfilik, hüquq və riski nəzərə alaraq verilir; bank və səhiyyə kateqoriyaları yoxlamadan çıxarılır.
- Təhlükəsizlik üçün çox vaxt domen səviyyəli qeydlər kifayət edir.
:::

**Situasiya 6.** Portal Nginx tərs proksisinin arxasındadır, amma hücumçu veb tətbiqinin WAF qaydalarından asanlıqla yan keçir. Araşdırma göstərir ki, portal serverinin 8080 portu İnternetdən də açıqdır. Problem və həll nədir?

:::reveal Cavab
- **Problem:** tətbiq serveri birbaşa əlçatandır, hücumçu proksini və WAF-ı tam keçir.
- **Həll:** firewall-da 8080 yalnız DMZ-dəki proksinin ünvanından icazəli olmalıdır, server İnternetdən görünməməlidir.
- Əlavə: tətbiq proksidən gəldiyini mTLS və ya gizli başlıqla yoxlaya bilər.
:::

**Situasiya 7.** Portala giriş limiti var: bir IP ünvanından dəqiqədə 5 giriş cəhdi. Hücumçu hər sorğuda fərqli X-Forwarded-For dəyəri göndərib minlərlə parol sınayır. Niyə alınır və necə düzəldilir?

:::reveal Cavab
- **Səbəb:** tətbiq limit üçün müştərinin göndərdiyi başlığa inanır.
- **Həll:** kənar proksi başlığı real `$remote_addr` dəyəri ilə üzərindən yazır, tətbiq başlığı yalnız etibarlı proksidən qəbul edir.
- Limit IP ilə yanaşı hesab üzrə də qoyulur və MFA tətbiq edilir.
:::

**Situasiya 8.** Sistem administratoru deyir: “Bizdə NAT var, deməli, proksi lazım deyil, ikisi eyni işi görür.” Bu fikrə münasibət bildirin.

:::reveal Cavab
- **Fikir səhvdir.**
- NAT yalnız başlığı dəyişir, məzmunu görmür, istifadəçi adına və URL-ə görə qərar vermir, qeydləri tətbiq səviyyəsində deyil.
- Proksi istifadəçini autentifikasiya edir, domen siyasəti tətbiq edir, zərərli faylları yoxlayır və SIEM üçün tətbiq səviyyəli qeyd verir.
- Bir-birini əvəz etmir, adətən birlikdə işləyir.
:::

**Situasiya 9.** Universitet VPN qapısı yalnız parolla işləyir. Müəllimlərdən birinin parolu başqa saytın sızıntısında tapılıb. Bir gecə həmin hesabla xarici ölkədən VPN-ə giriş olur, daxili fayl serverindən 3 GB məlumat çıxarılır. Hansı nəzarətlər çatışmır?

:::reveal Cavab
- **MFA yoxdur:** tək parol kifayət edib (məxfilik pozulub).
- **Minimum imtiyaz:** pozulub-pozulmadığını müəyyən etmək üçün hesabın iş ehtiyacı ilə faktiki şəbəkə və fayl icazələri müqayisə edilməlidir; 3 GB ötürmə bunu təkbaşına sübut etmir.
- **İzləmə:** coğrafiya, vaxt və həcm anomaliyası SIEM-də xəbərdarlıq yaratmayıb.
- **Hadisədən sonra:** hesab bağlanır, parol dəyişdirilir, sessiyalar kəsilir, MFA tətbiq edilir, sızmış parollar siyahısı ilə yoxlama qurulur, çıxarılan məlumatlar araşdırılır.
:::

**Situasiya 10.** İki kampus arasında IPsec tuneli qurulub. Administrator AH və tunel rejimi seçib, tunel isə NAT arxasında qurulmur. Üstəlik trafikin şifrələndiyini düşünür. Səhvləri izah edin.

:::reveal Cavab
- **Səhv 1:** AH şifrələmə vermir, yalnız tamlıq və autentifikasiya verir; məlumat açıq gedir.
- **Səhv 2:** AH xarici IP başlığını da qoruyur, NAT isə onu dəyişir; yoxlama pozulur.
- **Düzgünü:** ESP tunel rejimi seçilməli, NAT olduğu üçün NAT-T (UDP 4500) açıq olmalıdır.
:::

**Situasiya 11.** Şirkət uzaqdan işləyənlər üçün bölünmüş tunelə keçib. Bir müddət sonra zərərli proqram işçinin noutbukuna İnternetdən endirilib, proksi və DLP bundan xəbər tutmayıb. Niyə baş verdi və nə etmək olar?

:::reveal Cavab
- **Səbəb:** bölünmüş tuneldə İnternet trafiki birbaşa gedir, təşkilatın proksisindən keçmir.
- **Həll yolları:** tam tunelə qayıtmaq; buludda təhlükəsizlik xidməti (SWG/SSE) ilə İnternet trafikini yoxlamaq; cihazda EDR; zərərli domenlər üçün DNS səviyyəsində süzmə.
- Seçim riskə və kanal tutumuna görə verilir.
:::

**Situasiya 12.** Kafedra ofisində köhnə routerdə PPTP VPN işləyir. Administrator deyir: “Parol 20 simvoldur, sındırmaq olmaz.” Doğrudurmu?

:::reveal Cavab
- **Doğru deyil.**
- MS-CHAPv2-nin zəifliyi parolun uzunluğundan asılı deyil: tutulmuş mübadilə bir DES açarının tapılmasına gətirilir, 2⁵⁶ açar sahəsi xüsusi aparatla təxminən bir günə yoxlanır.
- **Həll:** protokolu dəyişmək. IKEv2 MFA dəstəkləyən autentifikasiya ilə seçilə bilər; WireGuard seçilərsə, MFA ayrıca idarəetmə və giriş qatı ilə tətbiq edilməlidir, adi WireGuard konfiqurasiyası bunu təmin etmir.
:::

## Konspektdən situasiyalar

**Situasiya 1.** Universitetin İnformatika fakültəsi SSH hücumlarını öyrənmək üçün DMZ-də, universitet saytının serverlərinin yanında, tam Linux qurulmuş bir honeypot yerləşdirir. Honeypot-un İnternetə çıxışı məhdudlaşdırılmayıb, logları da özündə saxlanır. Hansı risklər var?

:::reveal Cavab
- Bu, yüksək qarşılıqlı əlaqəli honeypot-dur və real serverlərlə eyni seqmentdədir.
- **Pivot:** hücumçu onu ələ keçirsə, DMZ-dəki universitet saytına keçə bilər.
- **Çıxış açıq:** honeypot-dan başqalarına hücum edə bilər; hücum universitetin IP-sindən görünər.
- **Loglar özündədir:** hücumçu onları silər.
- **Düzgünü:** ayrıca izolyasiya olunmuş seqment, çıxan trafiki bağlamaq, logları kənar serverə göndərmək.
- Məqsəd yalnız giriş cəhdlərini saymaqdırsa, aşağı səviyyəli emulyator kifayətdir; əmrləri də yazmaq lazımdırsa, Cowrie kimi orta səviyyəli honeypot.
:::

**Situasiya 2.** Universitetin İT direktoru deyir: “Kampus routerində NAT var, deməli tələbələrin hansı saytlara girdiyini izləyə və zərərli faylları bloklaya bilərik.” Bu fikir doğrudurmu? Nə lazımdır?

:::reveal Cavab
- **Doğru deyil.** NAT yalnız ünvanları çevirir, istifadəçini tanımır, URL-ə və məzmuna baxmır.
- **Lazım olan:** istifadəçi autentifikasiyası olan düz (forward) proksi (və ya URL süzgəcli NGFW / SWG).
- HTTPS saytların məzmununu yoxlamaq üçün əlavə olaraq TLS yoxlaması qurulmalıdır.
- Tələbə və əməkdaşlar bu barədə məqbul istifadə siyasəti ilə məlumatlandırılmalıdır, çünki məxfilik məsələsi yaranır.
:::

**Situasiya 3.** Universitetin qiymət sisteminə xidmət göstərən podratçı şirkətin mütəxəssisi bir serverə baxmaq üçün VPN alır. Qoşulduqdan sonra o, universitetin bütün alt şəbəkələrini, o cümlədən mühasibat və kadrlar serverlərini görür. VPN köhnə PPTP ilə qurulub. Nə dəyişdirilməlidir?

:::reveal Cavab
- **Protokol:** PPTP etibarsızdır; IKEv2/IPsec, WireGuard və ya TLS VPN-ə keçmək.
- **Minimal səlahiyyət pozulub:** podratçıya yalnız qiymət sisteminin serverinə, konkret porta marşrut və firewall qaydası verilməlidir; daha yaxşısı ZTNA və ya jump host.
- **Nəzarət:** MFA, işin müddəti ilə məhdud hesab, bütün sessiyaların loglanması.
:::

## Ehtimal olunan əlavə suallar

:::reveal Tələ sisteminin (honeypot) tərifi və vəzifələri nədir?
- Hücumçunu cəlb etmək, hərəkətlərini qeydə almaq və öyrənmək üçün qəsdən qurulmuş saxta resurs; Spitzner: dəyəri icazəsiz istifadədən gələn informasiya resursu.
- Vəzifələr: hücumu erkən aşkar etmək, üsulları öyrənmək, hücumçunun vaxtını real sistemlərdən uzaqda sərf etdirmək.
- Hücumun qarşısını almır: aşkarlama və öyrənmə vasitəsidir.
:::

:::reveal Tələ, firewall və IDS/IPS arasında fərq nədir?
- **Firewall:** sərhəddən keçən trafiki qaydalarla buraxır/bloklayır; icazəli portdan keçən hücumu görmür.
- **IDS/IPS:** hücum əlamətlərini tapır (IPS dayandırır); çox yanlış həyəcan, şifrəli trafikdə məhduddur.
- **Tələ:** yalnız ona gələn trafiki qeydə alır; çox az yanlış həyəcan, kiçik amma dəyərli məlumat, davranış qeydə alındığı üçün naməlum hücumu da görə bilir.
:::

:::reveal Tələni şəbəkədə hansı yerlərdə yerləşdirmək olar?
- **Xarici firewall-dan kənar:** ümumi skan mənzərəsi, çox “səs-küy”.
- **DMZ yaxınlığında ayrıca seqment:** açıq xidmətlərə hücumlar; real serverlərdən ciddi ayrılmalıdır.
- **Daxili şəbəkə:** daxilə keçmiş hücumçu, yoluxmuş cihaz; hər bağlantı insidentdir, ən çox fayda; kənardan gələni görmür.
:::

:::reveal Tələ Cyber Kill Chain-in hansı mərhələlərini görür?
- Kəşfiyyat (skan, parol sınaqları), çatdırılma, istismar, C2 cəhdi və daxili tələdə hədəfə çatma yüksək dəyərlidir.
- Quraşdırma orta və yüksək səviyyəli tələdə görünür.
- Silahlanma hücumçunun öz kompüterində baş verir, görünmür.
:::

:::reveal Düz proksinin funksiyaları və tərs proksinin funksiyaları hansılardır?
- **Düz proksi:** məzmun süzmə, autentifikasiya, qeydiyyat, keşləmə, antivirus yoxlaması (ICAP), DLP ilə sızmanın qarşısı, IP gizlətmə; məcburi çıxış nöqtəsi.
- **Tərs proksi:** TLS-in dayandırılması, yük balanslaşdırma, WAF, keşləmə və sıxılma, sürət məhdudlaşdırma, serverin gizlədilməsi, DDoS-a dözümlülük, yol üzrə marşrutlaşdırma.
:::

:::reveal Yük balanslaşdırma alqoritmlərini sadalayın.
- **Round robin:** növbə ilə, eyni gücdə serverlər.
- **Çəkili round robin:** güclü serverə daha çox, fərqli gücdə serverlər.
- **Ən az bağlantı (least connections):** ən az aktiv bağlantılı serverə, uzun sessiyalar.
- **IP heş:** müştəri eyni serverə bağlanır, sessiya yaddaşı serverdədirsə.
- Əlavə: health check serveri çıxarır; sticky session və ya ortaq (Redis) sessiya yaddaşı.
:::

:::reveal Proksi hücumlarından üçünü izah edin.
- **HTTP Request Smuggling:** Content-Length və Transfer-Encoding ziddiyyəti ilə proksi və server sorğunun sonunu fərqli görür, gizli sorğu başqasının sorğusuna qoşulur; qorunma: HTTP/2, ziddiyyətli sorğunu rədd etmək, yeniləmə.
- **Keşin zəhərlənməsi:** keş açarına daxil olmayan başlıq cavabı dəyişir, zərərli cavab keşlənir; qorunma: şəxsi cavabı keşləməmək (`private`/`no-store`), başlığı keş açarına və ya Vary-ə əlavə etmək.
- **SSRF:** proksi daxili/metadata ünvanlarına (`169.254.169.254`) sorğu göndərir; qorunma: lokal və daxili hədəfləri bağlamaq.
:::

:::reveal IPsec komponentləri (AH, ESP, IKE) nə edir?
- **AH (IP 51):** tamlıq və autentifikasiya, şifrələmə yox; NAT ilə işləmir.
- **ESP (IP 50):** şifrələmə, tamlıq, autentifikasiya; praktikada həmişə işlədilir.
- **IKE (UDP 500, NAT varsa 4500):** autentifikasiya, açar razılaşması, SA idarəsi.
:::

:::reveal IPsec üçün hansı alqoritmlər tövsiyə olunur, hansılar yox?
- **Şifrələmə:** AES-GCM, AES-CBC + HMAC-SHA-2, ChaCha20-Poly1305; DES, 3DES yox.
- **Tamlıq:** HMAC-SHA-256/384; MD5, SHA-1 yox.
- **Diffie-Hellman:** qrup 14, 19, 20 (ECP), Curve25519 (qrup 31); qrup 1, 2, 5 yox.
- **Autentifikasiya:** sertifikat, uzun təsadüfi PSK, EAP+MFA; qısa və ya hamıda eyni PSK yox.
:::

:::reveal IPsec, OpenVPN və WireGuard-ı müqayisə edin.
- **IPsec/IKEv2:** standart, aparat dəstəyi; sazlaması mürəkkəb; saytdan sayta.
- **OpenVPN:** çevik, firewall-dan asan keçir (UDP 1194 və ya TCP); nisbətən yavaş; TCP üzərində TCP meltdown riski; uzaqdan giriş.
- **WireGuard:** sürət, kiçik kod (təxminən 4000 sətir), sabit alqoritmlər, endirmə hücumu yoxdur; istifadəçi idarəetməsi yoxdur, FIPS siyahısında deyil; uzaqdan giriş və serverlərarası.
:::

:::reveal VPN-lərin təsnifatını verin.
- **Təhlükəsizlik modelinə görə:** secure və trusted.
- **Arxitekturaya görə:** korporativ daxili (intranet, site-to-site), uzaqdan giriş (remote access), korporativlərarası (extranet).
- **Reallaşdırmaya görə:** router, firewall, proqram, aparat (VPN konsentrator).
- **OSI səviyyəsinə görə:** L2 VPN (L2TP) və L3 VPN (IPsec, WireGuard); TLS VPN portal və ya tunel rejimində.
:::

:::reveal VPN qapısına qarşı sərtləşdirmə tədbirləri hansılardır?
- Hamı üçün MFA; sertifikat PSK-dan üstündür.
- İşlədilməyən hesabların söndürülməsi; qapının yamaq prioriteti.
- Minimum imtiyaz; idarəetmə interfeysi İnternetdən bağlı.
- Qoşulan cihazın yoxlanması (ƏS, disk şifrəsi, EDR); qeydlərin SIEM-ə göndərilməsi.
- Nümunələr: Colonial Pipeline (köhnə, MFA-sız hesab), Pulse Secure, Fortinet, Ivanti zəifliklər.
:::
