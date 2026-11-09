+++
title = "Simsiz şəbəkələrin əsasları və şifrələmə mexanizmləri"
unit = "suallar"
order = 8
summary = "Mühazirənin bütün nəzarət sualları və situasiya tapşırıqları cavablarla, konspektdən situasiyalar və ehtimal olunan əlavə suallar."
updated = 2026-11-09

[[source]]
title = "Mühazirə 8: Simsiz şəbəkələrin əsasları və şifrələmə mexanizmləri"
note = "Elmar Cabbarov, 2026–2027"

[[source]]
title = "Midterm konspekti, Mövzu 8"
note = "Elmar Cabbarov"
+++

Əvvəl sualı özün cavablandır, sonra cavaba bax. Cavablar mühazirənin terminologiyası ilə, imtahanda yazılı cavab üçün quruluşlu verilib. Universitet nümunələri (ünvanlar, VLAN nömrələri, parol) şərti tədris nümunəsidir.

## Nəzarət sualları

:::reveal Simsiz mühit kabel şəbəkəsindən hansı təhlükəsizlik baxımından fərqlənir?
- Kabeldə dinləmək üçün kabelə və ya kommutatora fiziki yaxınlaşmaq lazımdır; Wi-Fi-da radiosiqnal divardan keçir və hücumçu binaya girmədən trafiki qəbul edir.
- Radio mühiti ortaqdır (CSMA/CA rəqabəti idarə edir), ona görə şifrələmə seçimi daha kritikdir.
- Divar etibar sərhədi olmur; antenanın əhatəsi ilə giriş hüququ ayrıdır, siqnalı alan qanuni istifadəçi sayılmır.
- Qoruma cihazla AP arasındadır, HTTPS ayrıca qorunur: radio şifrələməsi tətbiq şifrələməsini əvəz etmir.
:::

:::reveal SSID şəbəkənin həqiqiliyini niyə sübut etmir?
- SSID (Service Set Identifier) yalnız şəbəkənin adıdır, məsələn "UNI-Staff".
- Hər kəs eyni adlı şəbəkə yarada bilər (Evil Twin).
- BSSID də kriptoqrafik kimlik sübutu deyil və saxtalaşdırıla bilər; eyni SSID təkbaşına eyni ESS demək deyil.
- Həqiqilik autentifikasiya ilə (802.1X, sertifikat yoxlaması) yoxlanır.
:::

:::reveal WEP-də 24 bitlik IV niyə problemdir?
- 24 bit cəmi 16 777 216 variantdır; IV açıq ötürülür və hər kadr üçün açarın əvvəlinə birləşdirilir.
- IV-lər müstəqil və bərabər ehtimalla seçilirsə, ad günü paradoksuna görə təxminən 5000 kadrdan sonra təkrar ehtimalı 50%-ə çatır.
- Eyni IV eyni açar axını deməkdir; iki şifrəli mətnin XOR-u iki açıq mətnin XOR-unu verir: C1 ⊕ C2 = P1 ⊕ P2.
- RC4-ün IV ilə zəif birləşməsi FMS (2001) və PTW (2007) ilə açarın trafikdən bərpasına imkan verir; parolun uzunluğu bunu dəyişmir.
:::

:::reveal CRC-32 tamlığı niyə qoruya bilmir?
- CRC təsadüfi ötürmə səhvini aşkar etmək üçündür, kriptoqrafik funksiya deyil.
- Gizli açarla hesablanmır və xətti xüsusiyyətlidir: hücumçu kadrın müəyyən bitlərini dəyişib CRC-ni uyğun düzəldə bilər, qəbuledici bunu görmür.
- CRC-nin (ICV) içəridə şifrələnməsi bunu dəyişmir; XOR-la şifrələmə də tamlıq vermir (C-nin bir biti dəyişəndə P-nin eyni biti dəyişir).
- 802.11 kadrındakı FCS də CRC-32-dir, radio səhvləri üçündür.
:::

:::reveal WPA2-də PMK, PTK və GTK nə üçündür?
- PMK (Pairwise Master Key): Personal-da paroldan və SSID-dən (PBKDF2-HMAC-SHA1, 4096 iterasiya, 256 bit), Enterprise-da 802.1X-dən alınır; trafikin özünü şifrələmir, PTK-nın mənbəyidir.
- PTK (Pairwise Transient Key): PMK, iki nonce və iki MAC-dan hesablanır, hər qoşulmada yenidir; cihaz-AP arasındakı şəxsi trafiki şifrələyir. KCK MIC üçün, KEK GTK-nın şifrələnməsi üçün, TK məlumat üçündür.
- GTK (Group Temporal Key): broadcast və multicast trafiki üçün ortaq açar; istifadəçi kimliyini sübut etmir.
- MIC mesajın doğru açarla göndərildiyini sübut edir.
:::

:::reveal 4 addımlı əl sıxmanın mesajlarını izah edin.
- M1 (AP-dən cihaza): ANonce və replay counter; cihaz bundan sonra PTK hesablaya bilir.
- M2 (cihazdan AP-yə): SNonce, MIC (KCK ilə) və RSN məlumatı; AP eyni PTK-nı qurub MIC-i yoxlayır.
- M3 (AP-dən cihaza): ANonce, MIC, artmış sayğac, KEK ilə şifrələnmiş GTK; cihaz yoxlayıb açarları quraşdırır.
- M4 (cihazdan AP-yə): M3-ün qəbulunun təsdiqi (EAPOL-Key mesajıdır, radio ACK-ı deyil).
- Parol ötürülmür; yalnız eyni PMK-dan alınan açarların doğruluğu yoxlanır. Əl sıxma açarların düzgün tutulmasını yoxlayır, avtorizasiya qərarı ayrıca qalır.
:::

:::reveal Oflayn lüğət hücumu niyə AP-nin görə bilmədiyi hücumdur?
- Hücumçu əl sıxmasını havadan yazır (lazım gəlsə cihazı deauth ilə atıb yenidən qoşulmağa məcbur edir).
- Sonra öz kompüterində hər parol namizədindən PMK, PTK hesablayıb MIC-i tutuşdurur (Hashcat).
- Şəbəkəyə bir dəfə də qoşulmaq lazım olmadığı üçün AP cəhdləri görmür və məhdudlaşdıra bilmir.
- PMKID hücumunda (Steube, 2018) bəzi AP-lərin M1-ə qoyduğu PMKID kifayətdir.
- Müdafiə: SAE (hər təxmin canlı əlaqə tələb edir), 802.1X, 20 simvoldan uzun təsadüfi parol.
:::

:::reveal SAE PSK-dan nə ilə fərqlənir?
- PSK-da yazılmış əl sıxması oflayn lüğət hücumuna imkan verir; SAE-də (Simultaneous Authentication of Equals, "Dragonfly") hər parol təxmini üçün AP ilə canlı əlaqə lazımdır, AP uğursuz cəhdləri görüb məhdudlaşdırır.
- PSK-da parol sabit PMK verir; SAE-də Commit/Confirm mübadiləsi hər dəfə təzə PMK yaradır, sessiya açarları ayrıdır və parol sonradan məlum olsa köhnə trafik açılmır (irəli məxfilik).
- Ortaq PSK ilə əl sıxmasını yazan istifadəçi başqasının PTK-sını hesablaya bilir; SAE bunu aradan qaldırır.
- SAE yalnız PMK-nı qurur, trafik açarları yenə 4 addımlı əl sıxma ilə gəlir.
:::

:::reveal PMF nəyi qoruyur, nəyi qorumur?
- Qoruyur: açarlar qurulduqdan sonra deauthentication, disassociation və müəyyən robust action kadrlarının saxtalaşdırılmasını və təkrarını (qrup kadrları üçün BIP və IGTK).
- Qorumur: beacon, probe və ilkin assosiasiya kadrlarını, yəni saxta AP-nin yaradılmasını.
- Radio basdırma (jamming), kanalın dolması və AP-nin enerjisinin kəsilməsi də PMF ilə dayanmır.
- WPA2-də istəyə bağlıdır, WPA3-də məcburidir; Required rejimdə PMF dəstəkləməyən cihaz qoşulmur.
:::

:::reveal KRACK hücumu parolu tapırmı? Nə ilə düzəldilir?
- Yox. KRACK (Key Reinstallation Attack, Vanhoef, 2017) protokolun vəziyyət maşınından istifadə edir.
- Hücumçu M3-ü təkrar göndərir; cihaz eyni açarı yenidən quraşdırır və paket sayğacını (PN) sıfırlayır.
- Nəticədə eyni açar axını təkrarlanır və trafik açıla bilir (nonce təkrarı).
- Həll parolu dəyişmək deyil, cihazı yeniləməkdir: təhlükəsiz tətbiq M3-ə cavab verə bilər, amma quraşdırılmış açarı yenidən quraşdırmır.
:::

:::reveal OWE ilə WPA3-SAE-nin fərqi nədir?
- OWE (Wi-Fi Enhanced Open, RFC 8110) parolsuz şəbəkədə Diffie–Hellman ilə hər cihaz üçün ayrı açarla şifrələmə verir; qonşu cihaz trafiki oxuya bilmir.
- OWE AP-nin həqiqiliyini yoxlamır: saxta AP və aktiv vasitəçi riski qalır.
- WPA3-SAE paroldan istifadə edən autentifikasiyalı açar mübadiləsidir (PAKE): həm şifrələmə, həm parol bilməyin sübutu, oflayn lüğət hücumuna davamlıdır.
- İstifadə: qonaq şəbəkəsində OWE və ya SAE (ayrı VLAN, müştəri izolyasiyası ilə).
:::

:::reveal MAC süzgəci niyə təhlükəsizlik tədbiri sayılmır?
- MAC ünvanı və SSID havada açıq görünür.
- Saxtalaşdırılan ünvan güclü autentifikasiya əvəzi deyil (MAC saxtalaşdırması captive portaldan keçmiş cihazı təqlid edir).
- MAC siyahısı yalnız əlavə uçot vasitəsi ola bilər; SSID gizlətmək də qorumur.
- Real qoruma: WPA3/802.1X, sertifikat yoxlaması, PMF.
:::

:::reveal OFDM ilə OFDMA arasında resurs bölgüsü baxımından fərq nədir?
- OFDM məlumatı çoxlu dar alt daşıyıcıya bölür və çoxşüalı yayılmaya davamlıdır; ənənəvi istifadədə bir ötürmə kanalın resurslarını müəyyən müddət tutur.
- OFDMA alt daşıyıcı qruplarını resurs vahidlərinə (RU) ayırır; AP bir planlaşdırılmış mübadilədə müxtəlif cihazlara fərqli RU verir (məsələn, LMS testində çoxlu kiçik cavab paketi).
- MU-MIMO məkan üzrə, OFDMA tezlik üzrə bölgü aparır.
- OFDMA kanal uğrunda rəqabəti və idarəetmə xərclərini aradan qaldırmır.
:::

:::reveal Gizli düyün hansı şəraitdə yaranır və RTS/CTS-in xərci nədir?
- Gizli düyün: eyni AP-ni eşidən iki cihaz bir-birini eşitmir (auditoriyanın iki küncü), kanalı boş sayıb eyni anda göndərir və AP-də toqquşma olur.
- RTS/CTS və NAV (virtual daşıyıcı hissiyyatı) ayrılmış vaxtı qonşulara bildirib bəzi toqquşmaları azaldır.
- Xərc: hər kiçik paketdən əvvəl əlavə radio vaxtı tutur; universal həll deyil.
- Əvvəl antenna yerləşməsi və hüceyrə ölçüsü yoxlanır.
:::

:::reveal To DS və From DS bitlərinə görə dörd ünvanın mənasını izah edin.
- To DS 0, From DS 0: Address 1 = DA və RA, Address 2 = SA və TA, Address 3 = BSSID; dördüncü ünvan yoxdur.
- To DS 1, From DS 0: Address 1 = BSSID və RA, Address 2 = SA və TA, Address 3 = DA.
- To DS 0, From DS 1: Address 1 = DA və RA, Address 2 = BSSID və TA, Address 3 = SA.
- To DS 1, From DS 1: Address 1 = RA, Address 2 = TA, Address 3 = DA, Address 4 = SA (dördünvanlı paylama bağlantısı).
- RA radio qəbuledicisi, TA radio ötürən, SA ilkin mənbə, DA son təyinatdır; birinci radio qəbuledicisi AP-dir, serverin MAC-ı radio hopunun RA-sı deyil.
:::

:::reveal WEP üçün 50 faiz IV təkrarı ehtimalını hesablayın. Fərziyyə nədir?
- Fərziyyə: IV-lər N = 2²⁴ = 16 777 216 dəyərdən müstəqil və bərabər ehtimalla seçilir, n N-dən xeyli kiçikdir.
- Yaxınlaşma: Pr(təkrar) ≈ 1 − exp(−n(n − 1) / (2N)).
- Pr = 0,5 üçün n ≈ sqrt(2N ln 2) ≈ 4823; n = 5000 üçün Pr ≈ 0,525.
- Bu açarın mütləq bərpası demək deyil; IV toqquşması, eyni açar axını və statistik açar bərpası (FMS, PTW) əlaqəli, amma fərqli hadisələrdir.
- Ardıcıl sayğac təsadüfi modelə uyğun gəlmir; 1000 kadr/s-də 24 bitlik məkan təxminən 4,66 saata tükənir (şərti hesab).
:::

:::reveal CCMP nonce-u, PN və EAPOL-Key replay counter nə ilə fərqlənir?
- PN (Packet Number): 48 bitlik sayğac, qorunan məlumat kadrlarının təkrar qəbul edilməməsini idarə edir; gizli deyil.
- CCMP nonce-u 13 baytdır: prioritet baytı, ötürənin 6 baytlıq ünvanı və 6 baytlıq PN; eyni TK ilə təkrarlanmamalıdır (GCMP-də 12 bayt).
- EAPOL-Key replay counter açar mübadiləsinin təzəliyini və sorğu-cavab uyğunluğunu idarə edir (M2 M1-ə, M4 M3-ə uyğun sayğacı qaytarır).
- Yəni PN məlumat kadrları, replay counter açar mübadiləsi üçündür; eyni sayğac deyil.
:::

:::reveal M3 təkrarlananda təhlükəsiz cihaz hansı vəziyyəti saxlamalıdır?
- Paket itkisinə görə M3 yenidən gələ bilər; təhlükəsiz cihaz cavab (təsdiq) verə bilər.
- Amma artıq quraşdırılmış açarı yenidən quraşdırmamalı və PN-ni sıfırlamamalıdır, məlumat sayğacı əvvəlki vəziyyətdə qalır.
- Açarın yenidən quraşdırılması və nonce vəziyyətinin geri qaytarılması KRACK qüsurunun səbəbidir; təkrar M3 təkbaşına KRACK sübutu deyil.
:::

:::reveal SAE Commit, Confirm və H2E hansı məsələləri həll edir?
- Commit: tərəflər paroldan əldə etdikləri parol elementi (PWE) və təsadüfi ədədlərlə scalar və element kimi açıq dəyərləri mübadilə edir (parolun heşi deyil).
- Confirm: açarlı təsdiqlə tərəflərin eyni ortaq sirri bildiyini sübut edir; bundan PMK alınır. Passiv müşahidəçi yazılardan oflayn parol yoxlaması qura bilməməlidir.
- Anti-clogging token hücum yükünə qarşıdır, kimlik sənədi deyil.
- H2E (Hash-to-Element) parolu qrup elementinə standartlaşdırılmış xəritələyir; köhnə hunting-and-pecking-in məlumatdan asılı davranışı yan kanal riski yaradırdı (Dragonblood). 6 GHz-də məcburidir.
:::

:::reveal 6 GHz və MLO üçün uyğunluqla təhlükəsizlik necə yoxlanılır?
- 6 GHz-də WPA3 və ya OWE məcburidir; SAE üçün H2E tələbi var. Sürücü, qurğu və yerli spektr icazəsi birlikdə yoxlanır (menyuda kanalın görünməsi icazə deyil).
- MLO-da (Wi-Fi 7) MLD kimliyi ilə link ünvanları əlaqələndirilir; açar, nonce/PN konteksti və replay yoxlaması MLO qaydalarına uyğun olmalıdır, bir link ayrılıb qoşulanda digərinin sayğacı sıfırlanmamalıdır.
- 6 GHz-dən 5 GHz-ə keçid öz-özünə endirmə hücumu deyil; AKM, qoruma səviyyəsi və siyasət yoxlanır.
- Hər linkin kanalı, PN/replay xətaları və keçid vaxtı ayrıca izlənir; MLO avtomatik ikiqat sürət və ya iki VPN deyil.
:::

## Situasiya tapşırıqları

**Situasiya 1.** Kitabxananın köhnə routeri WEP ilə işləyir, çünki kataloq terminalları WPA2-ni dəstəkləmir. İT işçisi deyir: "Parol 26 simvoldur, sındırmaq olmaz." Doğrudurmu?

:::reveal Cavab
- **Aktiv və pozulan xassə:** radio trafikinin məxfiliyi və tamlığı.
- **Səbəb:** zəiflik parolda deyil, protokoldadır: IV tez təkrarlanır, kifayət qədər trafik yığılanda açar uzunluğundan asılı olmayaraq bərpa olunur.
- **Tədbir:** WPA2-AES və ya WPA3-ə keçmək; terminalları kabelə qoşmaq və ya dəyişdirmək.
- **Yoxlama:** terminalları ayrı, İnternetsiz seqmentdə saxlamaq yalnız yayılma riskini azaldır, radio trafikinin məxfiliyini qorumur.
:::

**Situasiya 2.** Korpusda "UNI-Staff" WPA2-Personal ilə işləyir, bütün əməkdaşların parolu "Universitet2024"-dür. Yataqxanadan bir tələbə əl sıxmasını yazıb parolu tapır. Bu necə mümkün oldu və nə dəyişdirilməlidir?

:::reveal Cavab
- **Necə mümkün oldu:** WPA2-PSK-da yazılmış əl sıxması ilə parol namizədləri oflayn yoxlanır; proqnozlaşdırılan parol lüğətdə tez tapılır.
- **Əlavə problem:** ortaq parol olduğu üçün kimin qoşulduğunu bilmək və bir nəfəri ayırmaq mümkün deyil.
- **Tədbir:** şəbəkəni WPA2/WPA3-Enterprise-a keçirmək, fərdi hesab və sertifikat işlətmək, PMF-i açmaq.
- **Yoxlama:** parol dəyişdirilməlidir, çünki artıq məlumdur.
:::

**Situasiya 3.** Qonaq Wi-Fi-ı parolsuz, captive portal ilə işləyir. Rəhbərlik deyir: "Portalda telefon nömrəsi ilə qeydiyyat var, deməli, trafik qorunur." Konfransda bir iştirakçı başqalarının şifrəsiz HTTP trafikini görür. Niyə?

:::reveal Cavab
- **Səbəb:** captive portal qeydiyyat mexanizmidir, radio səviyyəsində şifrələmə vermir; açıq şəbəkədə hər kəs havadakı şifrəsiz trafiki görə bilir.
- **Tədbir:** OWE və ya WPA3-SAE; müştəri izolyasiyası; qonaq şəbəkəsinin daxili şəbəkədən tam ayrılması.
:::

**Situasiya 4.** Əməkdaşlar imtahan günü Wi-Fi-dan tez-tez düşür, loglarda çoxlu deauthentication kadrı var. WPA2 işləyir, PMF sönülüdür. Hansı hücum ola bilər və nə etmək lazımdır?

:::reveal Cavab
- **Hücum:** əlamətlər saxta deauthentication hücumuna uyğundur, amma səbəb trafik və kontroller qeydləri ilə təsdiqlənməlidir.
- **Məqsəd:** xidməti pozmaq, cihazları yenidən qoşulmağa məcbur edib əl sıxmasını yazmaq, yaxud saxta AP-yə çəkmək.
- **Tədbir:** PMF açılmalı, mümkünsə WPA3-ə keçilməli, WIPS ilə mənbə aşkar edilməlidir.
- **Qeyd:** jamming olsa PMF kömək etməz, fiziki aşkarlama lazımdır.
:::

**Situasiya 5.** Universitetin şərti 180 nəfərlik auditoriyasında üç AP eyni 80 MHz kanalda işləyir. Siqnal güclüdür, LMS testi zamanı cavablar gecikir. Dördüncü AP əlavə etmək təklif edilir. Nə yoxlanmalıdır?

:::reveal Cavab
- Kanal doluluğu, təkrar ötürmələr və gizli düyün ehtimalı ölçülür.
- Eyni kanaldakı AP-lər radio vaxtını paylaşır; daha dar, qonşuluqda ayrılmış kanallar, güc və yerləşdirmə planı yoxlanır.
- Müştəri imkanları, uplink və LMS serverinin yükü də qiymətləndirilir.
- AP artırmaq ölçməsiz həll deyil.
:::

**Situasiya 6.** Kitabxanada WPA3 aktivdir, amma bəzi noutbuklar PSK ilə qoşulur. Eyni parol bütün cihazlarda saxlanır. Administrator H2E-nin bütün parol hücumlarını dayandırdığını deyir. Qiymətləndirin.

:::reveal Cavab
- Keçid rejimində PSK bağlantısı WPA2 xüsusiyyətlərini saxlayır; eyni parol iki yolda işlənirsə zəif yol güclü yolun sirrini də ifşa edir.
- H2E SAE elementinin alınmasına aiddir, PSK mübadiləsini dəyişmir.
- Kontrollerdə hər cihazın AKM-i yoxlanır, uyğun cihazlar SAE-only siyasətinə keçirilir.
- Köhnə cihazlara məhdud və çıxarılma tarixi olan ayrı giriş verilir.
:::

## Konspektdən situasiyalar

**Situasiya 1 (konspekt).** Universitet kitabxanasının köhnə routeri hələ də WEP ilə işləyir, çünki bir neçə köhnə kataloq terminalı WPA2-ni dəstəkləmir. İT işçisi deyir: "Parol 26 simvoldur, uzundur, problem yoxdur." Bu doğrudurmu?

:::reveal Cavab
- Doğru deyil. WEP-in zəifliyi parolun uzunluğunda deyil, protokolun özündədir.
- 24 bitlik IV tez təkrarlanır və kifayət qədər trafik yığılanda açar parolun uzunluğundan asılı olmayaraq bərpa olunur (aircrack-ng); konspekt bunu "bir neçə dəqiqə" adlandırır, mühazirə isə sabit dəqiqə sayı vermir.
- Həll: şəbəkəni WPA2-AES və ya WPA3-ə keçirmək; terminalları kabelə qoşmaq və ya dəyişdirmək.
- Onları müvəqqəti ayrı, İnternetsiz seqmentdə saxlamaq yalnız yayılma riskini azaldır, radio trafikinin məxfiliyini qorumur.
:::

**Situasiya 2 (konspekt).** Korpusda "UNI-Staff" şəbəkəsi WPA2-Personal ilə qurulub, parol "Universitet2024" və bütün əməkdaşlar üçün eynidir. Bir tələbə yataqxanadan bu şəbəkənin əl sıxmasını yazıb parolu tapır. Bu necə mümkün oldu və nə dəyişdirilməlidir?

:::reveal Cavab
- WPA2-PSK-da əl sıxmasını yazan hücumçu parolu oflayn lüğət hücumu ilə yoxlaya bilir; "Universitet2024" kimi proqnozlaşdırıla bilən parol lüğətdə tez tapılır.
- Ortaq parol olduğu üçün kimin qoşulduğunu bilmək və bir nəfəri ayırmaq da mümkün deyil.
- Həll: əməkdaşlar şəbəkəsini WPA2/WPA3-Enterprise-a (802.1X, fərdi hesab və ya sertifikat) keçirmək; mümkün deyilsə, ən azı WPA3-SAE və uzun təsadüfi parol; PMF-i aktivləşdirmək.
:::

**Situasiya 3 (konspekt).** Universitet qonaq Wi-Fi-ını parolsuz, captive portal ilə qurub və deyir: "Qonaqlar portalda telefon nömrəsi ilə qeydiyyatdan keçir, deməli trafik qorunur." Konfrans zamanı bir iştirakçı başqalarının şifrəsiz HTTP trafikini görür. Niyə?

:::reveal Cavab
- Captive portal yalnız qeydiyyat və qaydaların qəbuludur, radio səviyyəsində şifrələmə vermir; açıq şəbəkədə hər kəs havadakı şifrəsiz trafiki dinləyə bilir.
- Həll: qonaq şəbəkəsində OWE (Enhanced Open) və ya WPA3-SAE; müştəri izolyasiyasını (client isolation) açmaq ki, qonaqlar bir-birinin cihazına çata bilməsin; qonaq şəbəkəsini daxili şəbəkədən tam ayırmaq.
- İstifadəçilər üçün HTTPS və VPN tövsiyəsi əlavə qatdır.
:::

## Ehtimal olunan əlavə suallar

:::reveal WEP, WPA, WPA2 və WPA3-ü şifrələmə, tamlıq, Personal autentifikasiya və status baxımından müqayisə edin.
- WEP: RC4, CRC-32, paylaşılan açar, əsas zəiflik IV təkrarı və açar bərpası; qadağan.
- WPA: RC4 + TKIP, Michael MIC, PSK, əsas zəiflik RC4 irsi; qadağan.
- WPA2: AES-CCMP, CBC-MAC, PSK, əsas zəiflik oflayn lüğət hücumu və məcburi olmayan PMF (KRACK 2017); qəbul edilir.
- WPA3: AES-CCMP və GCMP-256, CCMP/GCMP və PMF, SAE, əsas zəiflik keçid rejimində endirmə (Dragonblood); tövsiyə olunur.
- Enterprise: WEP-də dinamik WEP (təhlükəsiz deyil), WPA/WPA2-də 802.1X, WPA3-də 802.1X və istəyə görə 192 bit rejim.
:::

:::reveal Personal və Enterprise rejimlərinin fərqi nədir?
- Kimlik: Personal-da ortaq parol, Enterprise-da hər istifadəçinin hesabı və ya sertifikatı.
- Server: Personal-da yoxdur, Enterprise-da RADIUS.
- İstifadəçini ayırmaq: Personal-da parolu hamı üçün dəyişmək lazımdır, Enterprise-da bir hesab bloklanır.
- Qeydiyyat: tək PSK istifadəçinin kimliyini ayırmır, Enterprise-da istifadəçi adı qeydə düşür.
- PMK: Personal-da paroldan və ya SAE mübadiləsindən, Enterprise-da autentifikasiyadan alınır.
- Yer: Personal ev və kiçik ofis, Enterprise universitet və şirkət üçündür.
:::

:::reveal Simsiz qoşulmanın mərhələlərini sadalayın.
- Kəşf: AP beacon yayır, cihaz probe göndərir.
- 802.11 autentifikasiya: açıq sistemdə formal addım; WPA3-Personal-da SAE.
- Assosiasiya: cihaz AP-yə bağlanır, imkanlar (RSN elementi: şifr dəsti, AKM, PMF) razılaşdırılır.
- Enterprise autentifikasiyası: 802.1X/EAP (Personal-da yoxdur).
- 4 addımlı əl sıxma: şifrələmə açarları yaradılır.
- Sonra şifrəli trafik: DHCP ünvanı, DNS.
- Beacon, probe, assosiasiya, deauthentication idarəetmə kadrlarıdır.
:::

:::reveal 802.11 kadr növlərini və PMF-in əhatəsini izah edin.
- İdarəetmə kadrları (beacon, probe, autentifikasiya, assosiasiya, deauthentication) şəbəkəni qurur; nəzarət kadrları (RTS, CTS, ACK) radioya girişi idarə edir; məlumat kadrları faydalı yükü daşıyır.
- Tarixən idarəetmə kadrları qorunmurdu: saxta deauthentication ilə istənilən cihaz atılırdı.
- PMF (802.11w) deauthentication, disassociation və bəzi action kadrlarını qoruyur; beacon, probe və ilkin assosiasiya qorunmur.
:::

:::reveal Wi-Fi 6 haqqında hansı səhv təsəvvür var? 6 GHz-də təhlükəsizlik tələbi nədir?
- "Wi-Fi 6" sürət və radio texnologiyasının adıdır (802.11ax, 2021), təhlükəsizlik standartı deyil; Wi-Fi 6 routerdə WPA2 də seçilə bilər.
- Təhlükəsizliyi WPA2 və WPA3 müəyyən edir.
- Yalnız 6 GHz diapazonunda (Wi-Fi 6E və Wi-Fi 7) WPA3 və ya OWE məcburidir.
:::

:::reveal 2,4 GHz ilə 5/6 GHz diapazonlarını müqayisə edin.
- 2,4 GHz: divarlardan yaxşı keçir, uzağa çatır, amma kanal azdır (üst-üstə düşməyən 1, 6, 11); Bluetooth və mikrodalğalı soba müdaxilə yaradır.
- 5 və 6 GHz: daha çox kanal və sürət, amma divardan pis keçir; böyük auditoriyada daha çox AP lazım gəlir.
- 5 GHz-də DFS radarı qoruyur, radar aşkarlananda AP kanalı dəyişir; bu dərhal hücum sayılmır.
:::

:::reveal Parol uzunluğu oflayn hücuma qarşı nə dərəcədə vacibdir? Hesablama göstərin.
- Şərti sürət: saniyədə 1 milyon namizəd.
- 8 rəqəm: 10⁸ variant, 100 saniyə. 8 kiçik hərf: 26⁸ ≈ 2,1 × 10¹¹, təxminən 58 saat.
- 8 simvol hərf-rəqəm: 62⁸ ≈ 2,2 × 10¹⁴, təxminən 7 il. 12 simvol: 62¹² ≈ 3,2 × 10²¹, 100 milyon ildən çox.
- 20 təsadüfi simvol: 62²⁰ ≈ 7 × 10³⁵, praktiki mümkün deyil. Praktiki tövsiyə 20 simvoldan uzun təsadüfi paroldur.
- Cədvəl tam axtarışdır; real hücumda lüğət və qaydalar işlədilir, insanın seçdiyi parol erkən tapılır; çox GPU müddəti qısaldır.
:::

:::reveal Evil Twin, Rogue AP və Karma hücumlarını fərqləndirin.
- Evil Twin: hücumçu eyni SSID-li saxta AP açır; qorunma 802.1X və sertifikat yoxlaması, WIPS.
- Rogue AP: icazəsiz AP şəbəkəyə qoşulur (işçi "rahatlıq üçün" router taxır); qorunma 802.1X port nəzarəti, NAC, simsiz skan.
- Karma (probe hücumu): cihazın axtardığı şəbəkəyə AP "mən oyam" deyir; qorunma köhnə SSID-ləri silmək və avtomatik qoşulmanı söndürmək.
:::

:::reveal TKIP WEP-dən nə ilə yaxşıdır və niyə yenə də işlədilməməlidir?
- Hər paket üçün açar qarışdırılır, 48 bitlik TKIP ardıcıllıq sayğacı (TSC) var, Michael MIC əlavə edilir.
- Amma RC4 irsi qalır, ICV yenə CRC-32-dir, Michael yüngül hazırlanıb və güclü MAC deyil; 2008-ci ildə Beck və Tews TKIP-ə məhdud hücum göstərdilər.
- Qarışıq TKIP/CCMP rejimi bütün istifadəçilərə köhnə seçimi saxlayır; yalnız TKIP bilən cihaz kabelə keçirilir və ya dəyişdirilir, məcburi istisna ayrıca seqment və çıxarılma tarixi ilə sənədləşdirilir.
:::
