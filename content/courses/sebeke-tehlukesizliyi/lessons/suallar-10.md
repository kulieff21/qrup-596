+++
title = "Zərərli proqram təminatı və kompromitasiya indikatorları (IoC)"
unit = "suallar"
order = 10
summary = "Mühazirənin bütün nəzarət sualları, situasiya tapşırıqları, konspektdəki üç situasiya və ehtimal olunan əlavə suallar: hər biri imtahana hazır cavabla."
updated = 2026-11-09

[[source]]
title = "Mühazirə 10: Zərərli proqram təminatı və kompromitasiya indikatorları (IoC)"
note = "Elmar Cabbarov, 2026–2027"

[[source]]
title = "Midterm konspekti, Mövzu 10"
note = "Elmar Cabbarov"
+++

İmtahanda açıq suallar çıxır və cavab yazılı verilir. Hər sualı əvvəlcə özün cavabla, sonra aç. Universitet nümunələri şərtidir.

## Nəzarət sualları

:::reveal Zərərli proqramla kompromitasiya arasındakı əlaqəni və fərqi universitet nümunəsi ilə izah edin.
- Zərərli proqram (malware) kod, skript, makro və ya yaddaşdakı koddur; kompromitasiya sistemin, hesabın və ya məlumatın təhlükəsizliyinin faktiki pozulmasıdır.
- Zərərli proqram kompromitasiyaya səbəb ola bilər, amma kompromitasiya onsuz da olur: oğurlanmış parolla kitabxana portalına giriş serverdə zərərli fayl olmasa da kompromitasiyadır.
- Əksinə, karantinə düşmüş fayl hələ kompromitasiya deyil.
- Ona görə araşdırma yalnız antivirusun tapdıqları ilə bitmir: hesab, sessiya, bulud icazələri və məlumat ixracı ayrıca yoxlanır.
:::

:::reveal Eksploit və zərərli yük hansı ayrı vəzifələri görür? Hər yoluxmada eksploit tələb olunurmu?
- Eksploit zəiflikdən istifadə edib giriş yaradır (məs. LMS plaginində icazəsiz əmr icrası).
- Zərərli yük (payload) içəri girəndən sonra məqsədi yerinə yetirir (məlumat oğurlama, şifrələmə).
- Düstur: Aktiv + Zəiflik + Təhdid → Eksploit → Zərərli yük → Komprometasiya.
- Hər yoluxmada eksploit tələb olunmur: fişinqdən endirilmiş proqramı istifadəçi özü başladanda ayrıca zəifliyin istismarı lazım olmaya bilər.
:::

:::reveal Virusun, qurdun və troyanın fərqləndirici meyarları nədir?
- **Virus:** kodunu başqa obyektə (proqram faylı, makrolu sənəd, yükləmə sahəsi) əlavə edərək çoxalır; yoluxmuş kod icra olunmalıdır, amma istifadəçi klikləməsi məcburi deyil (yükləmə kodu sistem başlayanda işləyə bilər).
- **Qurd (worm):** fayla yapışmadan, şəbəkə xidməti zəifliyi, zəif autentifikasiya və ya açıq paylaşım vasitəsilə özü yayılır; ilk işə düşmə istifadəçidən asılı ola bilər, sonrakı yayılma avtomatikdir. Seqmentasiya hərəkət sahəsini azaldır.
- **Troyan:** meyar aldadıcı təqdimatdır (krek, saxta quraşdırıcı); özünü çoxaltması tələb olunmur, imza və işləyən əsas proqram gizli funksiyanın olmamasını sübut etmir.
:::

:::reveal Bir proqram niyə eyni vaxtda RAT, loader və troyan sayıla bilər?
- Növlər eyni suala cavab vermir: troyan maskalanmanı, RAT uzaqdan idarəetməni, loader yükün icraya hazırlanmasını bildirir.
- Sənəd əlavəsi ilə gələn troyan yükləyici başladır, yükləyici casus komponent quraşdırır, sonra şifrələyici işləyə bilər.
- Ona görə nümunəni bir xanaya yerləşdirmək düzgün deyil; təsnifatın dəyəri hansı əlavə izləri axtarmaq lazım olduğunu göstərməsidir (Emotet: troyan + yayılma + yükləyici; WannaCry: qurd + şifrələyici).
:::

:::reveal Rootkit ilə bootkit, dropper ilə downloader necə fərqlənir?
- **Rootkit** fayl, proses, bağlantı izlərini gizlətmək üçün sistemin müşahidə mexanizmlərinə müdaxilə edir (istifadəçi məkanı və ya nüvə); **bootkit** yükləmə zəncirinə yerləşir və OS tam başlamazdan əvvəl işə düşə bilər. Hər rootkit bootkit deyil. Belə halda sistemin verdiyi siyahıya etibar etmək olmaz, kənar mühitdən yoxlama və yenidən qurma lazım gələ bilər.
- **Dropper** yükü içində daşıyıb mühitə yerləşdirir; **downloader** yükü şəbəkədən alır; **loader** yükü icraya hazırlayıb yaddaşa yerləşdirir və başladır. Adlandırma praktikada kəsişir, ona görə faylın haradan gəldiyi, hara yazıldığı, hansı prosesdə işlədiyi sənədləşdirilir.
:::

:::reveal Faylsız fəaliyyət hansı izləri saxlaya bilər? Diskdə fayl tapılmaması nəyi sübut etmir?
- Faylsız (fileless) fəaliyyət yaddaşda və mövcud sistem alətləri (PowerShell, WMI) üzərində qurulur.
- İz saxlaya bilər: reyestr dəyəri, skript jurnalı, planlaşdırılmış tapşırıq, yaddaş səhifəsi.
- Ayrıca zərərli exe tapılmaması araşdırmanı bağlamaq üçün əsas deyil; termin bütün zəncir boyu diskdə heç nə olmadığını bildirmir.
- Faylsız hücumları tapmaq üçün yaddaş təhlili (Volatility) vacibdir.
:::

:::reveal Windows və Linux-da davamlılıq araşdırması üçün hansı obyektlər yoxlanır?
- **Windows:** Run və RunOnce açarları, planlaşdırılmış tapşırıqlar, xidmətlər, başlanğıc qovluqları, WMI hadisə abunələri.
- **Linux:** systemd xidmətləri və taymerləri, cron tapşırıqları, istifadəçi başlanğıc faylları (`.profile`), SSH `authorized_keys`, tətbiq əlavələri (plagin, modul).
- Hər birində yaranma vaxtı, yaradan hesab, başladılan fayl (heş, imza), təsdiqli dəyişiklik sifarişi və proses əlaqəsi tutuşdurulur; yeni xidmət özü yoluxma deyil.
- Qanuni proqramın arqumenti dəyişdirilmiş ola bilər, ona görə yalnız adı icazəli siyahı ilə müqayisə etmək yetmir.
:::

:::reveal İmtiyazların artırılması ilə daxili yan hərəkət arasındakı fərq nədir?
- İmtiyazların artırılması (privilege escalation) mövcud girişdən daha yüksək səlahiyyət almaqdır (kafedra kompüterində administrator olmaq).
- Daxili yan hərəkət (lateral movement) bir sistemdən başqasına keçməkdir (oradan oğurlanmış hesabla fayl serverinə giriş).
- Adi tələbə hesabı ilə bir neçə xidmətə giriş mümkündürsə, yan hərəkət üçün yerli administrator səlahiyyəti şərt deyil.
- Hücum mərhələləri məcburi sıra deyil: hücumçu bəzən səlahiyyət artırmanı və ya davamlılığı keçir.
:::

:::reveal C2 beacon-u ilə qanuni yenilənmə agentinin əlaqəsini necə ayırmaq olar?
- Beacon tapşırıq almaq üçün dövri müraciətdir, jitter aralıqların təsadüfiləşdirilməsidir; tam sabit dövr olmaması C2-ni istisna etmir, yenilənmə agentinin dövri əlaqəsi də zərərli deyil.
- Ayırmaq üçün ünvan prosesə bağlanır: EDR əlaqənin yeni, imzasız, şübhəli sənəddən yaranmış prosesə aid olduğunu göstərirsə, fərziyyə güclənir.
- Sertifikat, port və domen ayrı-ayrılıqda hücumun məqsədini sübut etmir.
- Proksi jurnalında eyni əlaqəni tədqiqat proqramı da yarada bilər.
:::

:::reveal İkiqat şantajda xidmətin bərpası niyə insidentin tam bağlanması deyil?
- İkiqat şantajda (double extortion) təzyiq həm işin dayanması (əlçatanlıq), həm oğurlanmış məlumatın yayılması (məxfilik) ilə olur.
- Təcrid edilmiş nüsxə LMS-i qaytarır, amma çıxarılmış siyahı hücumçuda qala bilər.
- Məxfilik araşdırması hansı məlumatın, kimin hesabı ilə və nə vaxt çıxarıldığını müəyyən edir; bütövlük üçün baza, konfiqurasiya və nüsxə etibarlı nüsxə ilə müqayisə olunur.
- Fidyə ödəmək açarın işləməsinə və oğurlanmış məlumatın silinməsinə zəmanət vermir.
:::

:::reveal Artefakt, IoC və IoA-nı eyni hadisə zəncirində göstərin.
- Zəncir: dekanlıq əməkdaşı `.docm` açır, Word PowerShell başladır, yeni tapşırıq yaranır, proses naməlum domenə qoşulur.
- **Artefakt:** xam texniki izlər (profil qovluğunda yeni fayl, tapşırıq, DNS sorğusu), zərərli olduğu hələ sübut olunmayıb.
- **IoC:** sənədin SHA-256 heşi məlum zərərli nümunə ilə eynidirsə və ya `update-campus.example` təsdiqlənmiş zərərli domendirsə, bu konkret dəyər uyğunluq axtarışı üçün yararlıdır.
- **IoA:** sənəd skript başladır, davamlılıq yaradır və naməlum istiqamətə qoşulur, bu davranış ardıcıllığı variant dəyişsə də işləyir.
:::

:::reveal Atomar, hesablanmış və davranış indikatorlarına hansı nümunələr vermək olar?
- **Atomar (atomic):** müqayisə üçün ayrıca dəyər: domen, IP, poçt ünvanı.
- **Hesablanmış (computed):** məlumat üzərində əməliyyatdan alınır: fayl heşi.
- **Davranış (behavioral):** hadisələr arasındakı münasibət: Word-dən PowerShell başlaması, ardınca tapşırıq yaranması.
- Bu bölgü bütün məhsullara məcburi sxem deyil, izah və layihələndirmə üsuludur.
:::

:::reveal SHA-256 uyğunluğu nəyi göstərir? MD5 və SHA-1 üçün toqquşma zəifliyi nə deməkdir?
- SHA-256 sabit 256 bit nəticə verir (64 onaltılıq simvol); eyni bayt ardıcıllığı eyni heş verir. Uyğunluq həmin məzmunun mövcudluğunu göstərir, icrasını, faylın zərərliliyini və bütün ailəni yox.
- Adı dəyişmək heşi dəyişmir, bir bayt dəyişmək dəyişir.
- MD5 və SHA-1 üçün fərqli məzmunlara eyni heş yaratmaq mümkün olan hücumlar məlumdur; düşmənin məzmun hazırlaya bildiyi şəraitdə SHA-256 üstün tutulur.
- Bu istənilən hazır zərərli fayl üçün dərhal qanuni əvəz yaratmaq demək deyil və ikinci ilkin təsvir hücumu ilə eyni deyil; köhnə heşlə axtarış faydasız olmur, amma bütövlük hökmü üçün zəifdir.
:::

:::reveal Ağrı piramidası niyə indikatorun etibarlılıq reytinqi sayılmır?
- Piramida (Pyramid of Pain) indikator bloklananda hücumçunun onu dəyişmək çətinliyini göstərir: heş, IP, domen, şəbəkə və host artefaktları, alətlər, TTP.
- Bu riyazi etibarlılıq balı və ya bütün hallara aid xərc ölçüsü deyil; etibarlılığı (confidence) mənbə, sübut və kontekst müəyyən edir.
- Heş asan dəyişir, TTP çətin; amma heşlər sürətli məhdudlaşdırma üçün yenə faydalıdır.
:::

:::reveal Köhnəlmiş indikatorun aktiv bloklamadan çıxarılması ilə tarixi bazadan silinməsi necə fərqlənir?
- Aktiv bloklamadan çıxarılan indikator tarixi araşdırmadan silinməyə bilər.
- Keçmiş semestrin insidentində köhnə domen bağlantısı yenə müqayisə olunur, amma həmin domenə bu gün avtomatik blok qoyulmur.
- Baxış qərarına son görülmə, yeni təsdiq, yanlış uyğunluqlar və sahiblik dəyişməsi daxildir; ömür təqvimlə yox, kontekstlə idarə olunur (IP başqasına verilə, domen təmizlənə bilər).
- Kartda baxış və bitmə vaxtı saxlanılır ki, köhnə bloklar yığılmasın.
:::

:::reveal Statik, dinamik və yaddaş təhlilinin nəticələrini necə birləşdirmək olar?
- **Statik:** fayl icra edilmədən format, heş, imza, sətirlər, idxal, disassembler; paketləmə gizlədə bilər.
- **Dinamik:** sandbox-da davranış (proses, fayl, reyestr, şəbəkə); yayınma səbəbindən başqa şərtdə fərqli ola bilər.
- **Yaddaş:** icra zamanı kod və obyektlər (faylsız hücum), amma görüntü bir ana aiddir.
- Birləşdirmə: statik kodda şifrələmə funksiyası varsa, dinamikdə hansı şərtdə çağırıldığı yoxlanır; sətirdəki domen dinamik müşahidə ilə təsdiqlənir. Nəticə sənədi müşahidəni, məhdudiyyəti və açıq qalan fərziyyəni göstərir.
:::

:::reveal YARA-da meta, strings və condition bölmələrinin vəzifələri nədir?
- `meta` qaydanın mənşəyini və məqsədini izah edir (təsvir, müəllif), uyğunluğun məntiqinə daxil deyil; tədris qaydasında zərərli imza ilə qarışmasın deyə saxlanılır.
- `strings` axtarılan sətirləri verir (`$a`, `$b`; `ascii`, `wide` bayt təqdimatı); çox ümumi sətir yanlış uyğunluq yaradır.
- `condition` məcburi məntiqdir (`all of them`, `filesize < 1MB`); həddindən sərt şərt variantları qaçırır.
- Uyğunluq zərərliliyi yox, şərtin ödənməsini göstərir.
:::

:::reveal Sigma qaydasının başqa SIEM-ə çevrilməsi zamanı hansı məlumat uyğunluğu yoxlanmalıdır?
- Sigma qaydası bütün SIEM-lərdə eyni nəticə vermir.
- Yoxlanır: arxa sistemə çevirmə, sahə xəritəsi (məs. `ParentImage`, `Image`), məlumat mənbəyi (`logsource`: proses telemetriyası mövcuddurmu) və qaydanın semantikası.
- Saat fərqi və yanlış sahə xəritəsi SIEM-də korrelyasiyanı korlayır.
- Qayda yalnız birbaşa valideyni Word olan prosesi tutur, ona görə proses ağacı ilə tamamlanır.
:::

:::reveal DNS qeydi ilə DNS sorğu jurnalının verdiyi sübut niyə fərqlidir?
- A və AAAA qeydləri adın ünvanla əlaqəsini göstərir, konkret cihazın həmin ada müraciət etdiyini sübut etmir.
- Sorğu jurnalı müştəri ünvanını, sorğu adını və vaxtı saxlayır; sübut məhz odur.
- Cihaz alternativ və ya şifrələnmiş resolver istifadə edirsə, yerli resolverdə sorğu olmaya bilər.
- DNS sorğusu da bağlantının uğurlu olduğunu, bağlantı isə oğurluğu təkbaşına sübut etmir.
:::

:::reveal Təcrid, sübutun qorunması, hesab bərpası və xidmətin geri açılması necə əlaqələnir?
- Əvvəlcə əhatə (cihaz, hesab, ikinci yük, məlumat), sonra təcrid: EDR ilə və ya kommutator/firewall ilə; dərhal söndürmə uçucu sübutu itirir (aktiv dağıntıda istisna).
- Sübut (yaddaş və disk görüntüsü, loglar, heş, chain of custody) təmizləmədən əvvəl qorunur.
- Aradan qaldırma: zəiflik, davamlılıq, ikinci yüklər, icazəsiz hesablar; bütövlüyə şübhə varsa sıfırdan qurmaq.
- Hesablar: parol təmiz cihazdan, tokenlərin ləğvi, icazə, poçt yönləndirmələri, SSH açarları yoxlanır.
- Xidmət yalnız yoxlanmış etibarlı nüsxədən və bağlanmış zəiflikdən sonra açılır, sonra müşahidə gedir.
:::

## Situasiya tapşırıqları

**Situasiya 1.** Dekanlıq əməkdaşı qiymət cədvəli kimi təqdim edilən sənədi açır. Word-dən PowerShell başlayır, yeni tapşırıq yaranır və xarici domenə dövri bağlantı görünür. Bütün hadisələr şərtidir. Hansı izlər toplanmalı və ilk tədbirlər necə seçilməlidir?

:::reveal Cavab
- **Təsnif:** proses əlaqəsi və davamlılıqla birləşən dövri əlaqə IoA yönümlü şübhə yaradır.
- **Toplanır:** sənədin və əlavə yükün SHA-256 heşləri, tapşırıq əməlinin tam yolu, domen, vaxt, proses identifikatorları.
- **Tədbir:** cihaz səlahiyyətli üsulla təcrid edilir, sübut qorunur, eyni məktubu alanlar və əlaqəli davranışlar axtarılır.
- Domenin zərərli əlaqəsi təsdiqlənirsə, uyğun dar blok tətbiq edilir; hesab və sessiyalar ayrıca qiymətləndirilir.
:::

**Situasiya 2.** Tələbə lisenziyasız elmi proqram quraşdırıb. Sonra universitet poçtundan tanımadığı məktublar göndərilir. Parolu dəyişəndən sonra fəaliyyət davam edir. Yalnız parolu yenidən dəyişmək kifayətdirmi?

:::reveal Cavab
- **Yox.** İnfostealer və oğurlanmış sessiya ehtimalı araşdırılır, amma bu fərziyyə sübutsuz fakt sayılmır.
- **Səbəb:** yoluxmuş cihaz yeni parolu təkrar oğurlaya bilər, köhnə sessiya isə qüvvədə qala bilər.
- **Tədbir:** cihaz təcrid və təhlil edilir, hesab təmiz cihazdan bərpa olunur, sessiyalar ləğv edilir, tətbiq icazələri və poçt yönləndirmələri yoxlanır.
- Göndərilmiş məktubların alıcıları da əhatəyə daxil edilir.
:::

**Situasiya 3.** Kitabxananın elektron resursu açılmır. Məlum olur ki, xarici feed-dən alınmış IP firewall-da bütöv bloklanıb, eyni ünvanda qanuni xidmət də yerləşir. Təhlükəsizliyi zəiflətmədən səhv necə düzəldilməlidir?

:::reveal Cavab
- İndikatorun mənbəyi, vaxtı və zərərli resursun dəqiq ünvanı yoxlanır.
- Paylaşılan IP əvəzinə mümkün qədər konkret domen, URL və ya son nöqtə davranışı üzrə tədbir seçilir.
- Əsassız geniş blok nəzarətlə geri götürülür, qanuni giriş yoxlanır, dəyişiklik sənədləşdirilir.
- Xarici axına gələn hər dəyəri eyni etibarlılıqla avtomatik bloklayan qayda yenidən qurulur.
:::

**Situasiya 4.** Universitet laboratoriyasında şübhəli fayl qum qutusunda qısa müddət işlədilir, görünən zərər baş vermir. Hesabatda faylın təhlükəsiz olduğu yazılır. Bu hökm necə düzəldilməlidir?

:::reveal Cavab
- Hökm müşahidənin sərhədini aşır: nəticədə yalnız verilən mühit və müddətdə hansı davranışın görüldüyü yazılmalıdır.
- Nəzərə alınır: gözləmə şərti, istifadəçi hərəkəti, virtual mühit yoxlaması, C2 əlçatmazlığı (yayınma).
- Fərziyyə statik təhlil, uyğun əlavə sınaq və lazım gəldikdə yaddaş təhlili ilə yoxlanır.
- Real şəbəkəyə sərbəst çıxış açmaq yayınmanı yoxlamaq üçün məqbul qısa yol deyil.
:::

**Situasiya 5.** Kafedranın fayl serveri şifrələnib. Ayrı saxlanan ehtiyat nüsxə işləyir, lakin hadisədən əvvəl tələbə sənədlərinin böyük arxivi kənara göndərilib. Serveri bərpa edən komanda işi bağlamaq istəyir. Hansı iş qalır?

:::reveal Cavab
- **Əlçatanlıq** bərpa olunub, **məxfilik** pozulub: bərpa məxfilik araşdırmasını bitirmir.
- Arxivin məzmunu, onu yaradan hesab, ötürmə istiqaməti və sübutların etibarlılığı müəyyən edilir.
- Hesablar, sessiyalar və qalıq giriş yolları yoxlanır, aidiyyəti bölmələr məlumatlandırılır, bildiriş qərarı tətbiq edilən qaydalara uyğun verilir.
- Girişə səbəb olan zəiflik bağlanmadan xidmət açılmamalıdır.
:::

**Situasiya 6.** LMS-in Linux serverində yeni systemd xidməti tapılıb. Fayl adı ehtiyat nüsxəyə bənzəyir, amma ExecStart istifadəçinin yaza bildiyi qovluqdakı skripti göstərir. Ad əsasında xidməti qanuni saymaq olarmı?

:::reveal Cavab
- **Yox**, ad yetərli deyil.
- Yoxlanır: xidməti yaradan hesab, vahid faylının yeri, yaranma vaxtı, skriptin heşi və məzmunu, jurnal izləri; təsdiqli ehtiyat nüsxə prosesi ilə tutuşdurulur.
- Skriptin əlavə yük başlatması və ya məlumat çıxarması araşdırılır.
- Sübut götürülmədən kor-koranə silinmir; paralel olaraq digər davamlılıq mexanizmləri və istifadəçi xidmətləri yoxlanır.
:::

**Situasiya 7.** Universitet SOC-u köhnə MD5 siyahısı ilə bütün zərərli ailəni tapdığını iddia edir. Bir nümunənin adı dəyişdirilir və yenə tutulur, başqa paketlənmiş variant isə tutulmur. Bu nəticə necə izah olunur?

:::reveal Cavab
- Ad dəyişikliyi məzmun heşini dəyişmir, paketləmə isə baytları dəyişir.
- Heş konkret məzmunu tanıyır və bütün ailənin örtüyünü göstərmir.
- SHA-256 əlavə edilməli, məzmun xüsusiyyətləri və davranış qaydaları ilə yoxlama tamamlanmalıdır.
- MD5-in toqquşma zəifliyi ayrıca etibar problemidir; istənilən mövcud fayla dərhal eyni heşli əvəz yaratmaqla eyniləşdirilməməlidir.
:::

**Situasiya 8.** Kitabxana kompüterində YARA tədris qaydası uyğunluq verib. Faylda yalnız laboratoriya markerləri var. SOC əməkdaşı cihazı zərərli proqramla yoluxmuş elan edir. Düzgün şərh nədir?

:::reveal Cavab
- Uyğunluq yalnız qaydadakı məntiqin ödəndiyini göstərir.
- Tədris qaydasının `meta` bölməsi və markerləri onun zərərli ailə imzası olmadığını bildirir.
- Cihaz haqqında hökm üçün faylın mənşəyi, icrası və başqa davranışlar araşdırılmalıdır.
- Dərs: qayda nəticələri ad, məqsəd və versiya ilə təqdim edilməlidir; tədris qaydası istehsal bloklama axınına qoşulmamalıdır.
:::

## Konspektdən situasiyalar

**Situasiya K1.** Dekanlıq əməkdaşı "Qiymət_cədvəli_yekun.docm" faylını açır. EDR göstərir: `winword.exe → powershell.exe -enc …`, sonra yeni planlaşdırılmış tapşırıq yaranır və kompüter hər 5 dəqiqədən bir naməlum domenə HTTPS ilə qoşulur. Bu davranışları təsnif et və ilk addımları de.

:::reveal Cavab
- **Təsnif:** Word-ün kodlaşdırılmış PowerShell başlatması icra və şübhəli proses ağacıdır (IoA); planlaşdırılmış tapşırıq davamlılıqdır (T1053); müntəzəm HTTPS digər əlamətlərlə birlikdə C2 beacon ehtimalını gücləndirir.
- **IoC kimi qeydə alınır:** faylın heşi, domen, tapşırığın adı.
- **İlk addımlar:** kompüteri EDR ilə söndürmədən təcrid etmək; domeni DNS və proksidə bloklamaq; eyni fayl və domeni SIEM-də universitetin digər kompüterlərində axtarmaq; əməkdaşın parolunu təmiz cihazdan dəyişmək; sübut toplamaq.
:::

**Situasiya K2.** Tələbə "pulsuz MATLAB" krekini yükləyir. Bir neçə gün sonra onun universitet poçtundan bütün qrupa fişinq göndərilir. Tələbə parolunu dəyişir, amma hücumçu hələ də onun hesabında fəaliyyət göstərir. Niyə və nə etmək lazımdır?

:::reveal Cavab
- **Səbəb:** krek troyan idi, içindəki infostealer brauzerdən parolla yanaşı sessiya kukilərini və tokenləri də oğurlayıb. Digər ehtimal: yoluxmuş kompüter yeni parolu da yenidən oğurlayır.
- Token ilə parolsuz və MFA-sız giriş mümkündür, ona görə parol dəyişmək kifayət etmir.
- **Tədbir:** bütün aktiv sessiyaları və tokenləri ləğv etmək; poçtda yaradılmış yönləndirmə qaydalarını yoxlamaq; kompüteri təmizləmək və ya sıfırdan qurmaq; parolu təmiz cihazdan dəyişmək; fişinq alan tələbələri xəbərdar etmək.
:::

**Situasiya K3.** Analitik şübhəli faylı sandbox-da işə salır, 3 dəqiqə ərzində heç bir şübhəli davranış görmür və "fayl təmizdir" yazır. Bu nəticə nə qədər etibarlıdır?

:::reveal Cavab
- **Etibarlı deyil.** Bir çox zərərli proqram virtual mühiti tanıyır, müəyyən müddət gözləyir və ya istifadəçi hərəkəti (siçan, sənədin sürüşdürülməsi) gözləyir.
- Dinamik analizin sakit keçməsi təhlükəsizlik sübutu deyil.
- Tamamlanır: statik analiz (sətirlər, paketləmə əlamətləri, imza), heşin təhdid kəşfiyyatı bazalarında yoxlanması, daha uzun və fərqli konfiqurasiyalı sandbox, lazım gəlsə yaddaş analizi.
:::

## Ehtimal olunan əlavə suallar

:::reveal Artefakt, IoC və IoA arasındakı fərqi cədvəl kimi yazın.
| Meyar | Artefakt | IoC | IoA |
| --- | --- | --- | --- |
| Sual | Nə müşahidə olunub? | Hansı məlum zərərli iz görünür? | Hansı şübhəli davranış baş verir? |
| Mahiyyət | Xam fakt, zərərliliyi sübut olunmayıb | Zərərli fəaliyyətlə əlaqələndirilmiş, etibarlılıq dərəcəsi olan iz | Davranış, yeni variantda da işləyir |
| Nümunə | Profil qovluğunda fayl | Məlum zərərli SHA-256 | Sənəd skript başladır, sonra naməlum domenə qoşulur |
| Məhdudiyyət | Zərərli əlaqə hələ sübut olunmayıb | Dəyər dəyişə, kontekst köhnələ bilər | Qanuni avtomatlaşdırma oxşar görünə bilər |
:::

:::reveal IoC qrupları hansılardır və hər birinə nümunə verin.
- **Fayl:** heş, ad, yol, ölçü, imza. **Şəbəkə:** IP, domen, URL, qeyri-adi port, DNS sorğuları, beacon bağlantıları.
- **Sistem və proses:** yeni xidmət, tapşırıq, reyestr dəyişikliyi; valideyn-övlad, əmr sətri, icra hesabı (PID təkrar işlənə bilər).
- **Hesab:** yeni admin hesabı, qeyri-adi giriş. **Poçt:** başlıqlar, əlavə heşi, keçid, saxta göndərici (görünən ad mənbəni sübut etmir).
:::

:::reveal Dəqiqlik və tamlığı hesablayın: qayda 40 xəbərdarlıq yaradıb, onların 10-u zərərlidir.
- Dəqiqlik = TP / bütün xəbərdarlıqlar = 10 / 40 = 25%.
- Bu rəqəm qaydanın bütün hücumların hansı hissəsini tapdığını göstərmir.
- Bunu tamlıq (recall) göstərir: TP / (TP + FN). FN real həyatda tam bilinməyə bilər, idarə olunan zərərsiz sınaqlar örtüyü yoxlamağa kömək edir.
- TP həqiqi müsbət, FP yanlış müsbət, FN buraxılmış hücumdur. Sensorun susması ayrıca xəbərdarlıq yaratmalıdır, çünki sıfır nəticə işləməyən toplama da ola bilər.
:::

:::reveal Hadisə, xəbərdarlıq və insident arasındakı fərq nədir?
- Hadisə (event) sistemdə baş verən fəaliyyətdir; jurnal qeydi onun saxlanılmış təsviridir.
- Xəbərdarlıq (alert) aşkarlama qaydasının araşdırılmalı saydığı nəticədir.
- İnsident (incident) təhlükəsizliyi pozan və ya real təhlükə yaradan, cavab tələb edən vəziyyətdir.
- Nümunə: gecə kafedra kompüterindən giriş hadisədir, onun şübhəli sayılması xəbərdarlıqdır, oğurlanmış hesabla sənədlərin çıxarılması təsdiqlənəndə insident açılır.
:::

:::reveal IoC-nin həyat dövrünü və indikator kartının sahələrini yazın.
- **Dövr:** toplama (insident, xarici axın, CERT) → normallaşdırma (vahid format) → zənginləşdirmə (kontekst, etibarlılıq) → tətbiq (SIEM, EDR, firewall) → qiymətləndirmə (FP, fayda) → köhnəlmə (nəzərdən keçir, sil).
- **Kart:** növ və dəyər, mənbə, ilk və son görülmə, etibarlılıq və əsas, əlaqəli davranış, tədbir və sahibi, baxış və bitmə vaxtı, paylaşma məhdudiyyəti (TLP).
- İndikatorlar STIX formatında, TAXII ilə paylaşılır; STIX və TAXII etibarlılığı sübut etmir.
:::

:::reveal Hansı vasitə indikatoru harada tətbiq edir və kor nöqtəsi nədir?
- **Antivirus:** məlum nümunə, karantin; başqa variant və hesab oğurluğu qalır.
- **EDR:** proses əlaqəsi, cihaz təcridi; agentsiz cihaz görünmür.
- **DNS nəzarəti:** zərərli domen sorğusu; alternativ resolver və birbaşa IP qalır.
- **Proksi və firewall:** URL, domen; paylaşılan ünvanı bloklamaq qanuni xidməti poza bilər.
- **IDS və IPS:** şəbəkə nümunəsi; şifrələmə və sensorun yeri görünüşü məhdudlaşdırır.
- **SIEM:** korrelyasiya; yanlış sahə xəritəsi və saat fərqi. **SOAR:** avtomatlaşdırma; yanlış nəticə sürətlə yayılır.
:::

:::reveal Sysmon-da hansı hadisələr əsasdır və PID əvəzinə niyə ProcessGuid istifadə olunur?
- Event ID 1 proses yaradılması (valideyn ilə), 3 şəbəkə bağlantısı (konfiqurasiyada açılmalıdır), 11 fayl yaradılması, 13 reyestr dəyərinin dəyişməsi, 22 DNS sorğusu.
- ProcessGuid eyni prosesin hadisələrini əlaqələndirir; PID sonradan başqa prosesə verilə bilər.
- Korrelyasiyada hadisənin baş vermə vaxtı ilə SIEM-ə çatma vaxtı ayrıca saxlanılır.
:::

:::reveal Təhlükəsiz sandbox üçün qaydalar hansılardır?
- İstehsalat şəbəkəsindən ayrı olmalıdır; içində real məlumat və parol olmamalıdır.
- Şəbəkə çıxışı nəzarətdə (standart bağlı, lazım olanlar saxta daxili xidmətlərlə təqlid), ortaq qovluqlar və bufer bağlı.
- Virtual maşın təkbaşına tam izolyasiya deyil (host diski, körpü, hipervizor zəifliyi); snapshot kənara çıxmış zərəri geri qaytarmır.
- Şübhəli fayl iş kompüterində açılmır, SHA-256 qeyd edilir, orijinal qorunur; parollu arxiv izolyasiya deyil.
:::

:::reveal WannaCry, NotPetya və Emotet hadisələrindən hansı texniki dərslər çıxır?
- **WannaCry** (may 2017): SMB zəifliyindən istifadə edən qurd + şifrələyici; MS17-010 yamağı martda mövcud idi. Dərs: yamağın mövcudluğu ilə tətbiqi ayrıdır; aktiv inventarı, SMB girişinin daraldılması, bərpa nüsxəsi lazımdır; heşi bloklamaq kifayət deyil.
- **NotPetya** (iyun 2017): M.E.Doc yenilənməsi ilə təchizat zənciri vektoru, daxildə zəifliklər və oğurlanmış kimlik; dağıdıcı (wiper) nümunəsidir. Dərs: təchizatçı yenilənməsinə nəzarətsiz imtiyaz verməmək, oğurlanmış hesabla hərəkəti ayrıca məhdudlaşdırmaq.
- **Emotet:** bank troyanından başqa yükləri çatdıran modul infrastruktura çevrilib. Dərs: məktubu silmək yetmir; kim açdı, hansı proses və yük, hesab oğurluğu araşdırılır.
:::
