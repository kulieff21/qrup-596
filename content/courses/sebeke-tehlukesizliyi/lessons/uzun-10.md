+++
title = "Zərərli proqram təminatı və kompromitasiya indikatorları (IoC)"
unit = "uzun"
order = 10
summary = "Mühazirə tam həcmdə: zərərli proqram növləri, yoluxma yolları, davamlılıq və gizlənmə, C2 və ikiqat şantaj, artefakt-IoC-IoA, Ağrı piramidası, indikatorun həyat dövrü, statik/dinamik/yaddaş təhlili, YARA və Sigma, vasitələrdə tətbiq, insidentə cavab və WannaCry, NotPetya, Emotet dərsləri."
updated = 2026-11-09

[[source]]
title = "Mühazirə 10: Zərərli proqram təminatı və kompromitasiya indikatorları (IoC)"
note = "Elmar Cabbarov, 2026–2027"
+++

Zərərli proqram necə yayılır, sistemdə nə edir və arxasında hansı izləri qoyur? Bu izlər (IoC) həm yoluxmanı aşkarlamaq, həm də başqa təşkilatları xəbərdar etmək üçün işlədilir. Mühazirə bunu universitet nümunəsi üzərində qurur: anlayışlar, növlər, yoluxma yolu, davamlılıq, C2, indikatorlar, təhlil, qaydalar, vasitələr, cavab və üç real hadisə.

:::note Şərti tədris nümunəsi
Universitet topologiyası, cihaz və domen adları (`update-campus.example`, `sync-campus.example`), ünvanlar, tarixlər, xəbərdarlıq sayları və hesablar **şərti tədris nümunəsidir**. Komandalar yalnız oxuma üçündür, qaydalar tədris məqsədlidir.
:::

## Zərərli proqram və təhlükəsizliyin pozulması

### Zərərli proqram nədir

Zərərli proqram təminatı (malware) məlumatı oğurlamaq, icazəsiz dəyişiklik etmək, xidmətin işini pozmaq və ya hesablama resurslarından sahibinin razılığı olmadan istifadə etmək üçün hazırlanmış və ya uyğunlaşdırılmış koddur. İcraolunan fayl, skript, sənəddəki makro və yaddaşa yerləşdirilmiş kod bu anlayışa daxil ola bilər. Faylın uzantısı və ölçüsü onun zərərli olub-olmadığını müəyyən etmir: qısa skript tələbə bazasının ehtiyat nüsxəsini silə, böyük quraşdırma paketi isə tam qanuni ola bilər.

Universitetin tədrisi idarəetmə sistemi (Learning Management System, LMS) üzərindən dərs materialları paylaşılır, tələbə bazasında qeydiyyat və qiymətlər saxlanılır, kitabxanada elektron resurslara giriş verilir. Eyni yoluxma fərqli nəticələr yaradır:

| Hücum | Pozulan xassə |
| --- | --- |
| Parol oğurlayan proqram LMS hesabına girir | Məxfilik |
| Qiymət cədvəlini dəyişən kod | Bütövlük |
| Fayl serverini şifrələyən proqram | Əlçatanlıq |

Bir hücum bu xassələrin bir neçəsinə zərər vura bilər.

Üç ehtiyatlı müşahidə:

- Zərərli proqramın işləməsi həmişə ekranda görünmür: hücumçu cihazı sıradan çıxarmaq əvəzinə aylarla giriş məlumatı toplaya bilər.
- Kompüterin yavaş işləməsi yoluxmanın sübutu deyil; diskin dolması, səhv yenilənmə və elmi hesablama da eyni əlaməti yaradır. Analitik istifadəçinin müşahidəsini başlanğıc məlumat sayır, sonra prosesləri, faylları, şəbəkə əlaqələrini və hesab fəaliyyətini yoxlayır.
- Qanuni alətdən zərərli istifadə ilə xüsusi zərərli proqram fərqlidir. Administrator uzaqdan yardım proqramı ilə kafedra kompüterini sazlayırsa, bu icazəli fəaliyyətdir; hücumçu eyni proqramı əməkdaşın xəbəri olmadan quraşdırıb sənədləri çıxarırsa, alət hücum vasitəsidir. Məhsulun adı kifayət etmir; icazə, istifadəçi, vaxt və görülən əməl araşdırılır.

### Aktivdən kompromitasiyaya qədər

İnformasiya aktivi təşkilat üçün dəyəri olan məlumat, xidmət və ya resursdur. Təhdid aktivə zərər vurmaq potensialıdır. Zəiflik təhdidin reallaşmasına şərait yaradan çatışmazlıqdır: kod səhvi, həm də yoxlanılmamış proqram quraşdırmağa icazə verən iş qaydası. Aktivin olması və zəifliyin tapılması avtomatik olaraq uğurlu hücum demək deyil.

Eksploit (exploit) zəiflikdən istifadə edən kod və ya üsuldur; istismar (exploitation) həmin imkanın istifadə edilməsidir. Zərərli yük (payload) hücumun məqsədini yerinə yetirən hissədir. LMS plaginindəki zəiflik əmr icrasına yol açırsa, eksploit giriş yaradır, sonradan işləyən məlumat oğurlayan komponent yükdür. Fişinqdən endirilmiş proqramı istifadəçi özü başladanda ayrıca proqram zəifliyinin istismarı tələb olunmaya bilər, yəni hər yoluxmada eksploit olmur.

Kompromitasiya sistemin, hesabın və ya məlumatın təhlükəsizliyinin pozulmasıdır. Oğurlanmış parolla kitabxana portalına giriş də kompromitasiyadır, serverdə zərərli fayl olmasa belə. Buna görə insident araşdırması yalnız antivirusun tapdığı obyektlərlə məhdudlaşmır: hesabların, sessiyaların, bulud icazələrinin və məlumat ixracının vəziyyəti ayrıca yoxlanır.

:::tip Düstur
Aktiv + Zəiflik + Təhdid → Eksploit → Zərərli yük → Komprometasiya. Eksploit zəiflikdən istifadə edib qapını açan hissədir, zərərli yük içəri girəndən sonra ziyan vuran hissədir (şifrələmə, oğurluq). Komprometasiya həmişə zərərli proqramla olmur: oğurlanmış parolla giriş də komprometasiyadır.
:::

| Anlayış | Dəqiq məna | Universitet nümunəsi |
| --- | --- | --- |
| Aktiv | Qorunan məlumat, xidmət və ya resurs | Tələbə bazası və bazanın ehtiyat nüsxəsi |
| Zəiflik | İstismara şərait yaradan çatışmazlıq | Yamaqlanmamış LMS plagini |
| Təhdid | Zərər yaratmaq potensialı | İnternetdən gələn istismar cəhdi |
| Eksploit | Zəiflikdən istifadə edən kod və ya üsul | Plagində icazəsiz əmr icrası yaradan sorğu |
| Zərərli yük | Hücumun funksiyasını yerinə yetirən komponent | Tələbə məlumatını çıxaran proqram |
| Kompromitasiya | Təhlükəsizliyin faktiki pozulması | İcazəsiz məlumat oxunması və hesab nəzarəti |

### Hadisə, xəbərdarlıq və insident

- **Hadisə (event)**: sistemdə baş verən fəaliyyət. Jurnal qeydi hadisənin saxlanılmış təsviridir.
- **Xəbərdarlıq (alert)**: aşkarlama qaydasının araşdırılmalı saydığı nəticə.
- **İnsident (incident)**: təhlükəsizliyi pozan və ya ona real təhlükə yaradan, cavab tədbiri tələb edən vəziyyət.

Gecə kafedra kompüterindən giriş hadisədir; həmin girişin şübhəli sayılması xəbərdarlıq yaradır; oğurlanmış hesabla sənədlərin çıxarıldığı təsdiqlənəndə insident açılır.

Telemetriya (telemetry) sistem və təhlükəsizlik vasitələrinin topladığı texniki müşahidələrdir: prosesin yolu, valideyn prosesi, istifadəçi, fayl heşi, şəbəkə istiqaməti. Toplanmayan məlumatı sonradan IoC siyahısı ilə bərpa etmək mümkün deyil. Universitet yalnız uğursuz girişləri saxlayırsa, uğurlu girişdən sonra tələbə bazasının kimə ixrac edildiyini həmin jurnaldan öyrənə bilməyəcək.

## Zərərli proqram növləri

### Təsnifatın məntiqi

Növlər eyni suala cavab vermir: virus və qurd çoxalma üsulunu, troyan aldadıcı təqdimatı, ransomware məqsədi, rootkit gizlənmə mexanizmini bildirir. Ona görə nümunəni yalnız bir xanaya yerləşdirmək düzgün deyil. Növlər bir-birini istisna etmir: sənəd əlavəsi ilə gələn troyan yükləyici başlada, yükləyici casus komponent quraşdıra, hücumçu sonradan şifrələyici işlədə bilər. Bir nümunə eyni anda troyan (maskalanma), bot (idarəetmə) və ransomware (məqsəd) ola bilər. Nümunələr: Emotet = troyan + yayılma + yükləyici; WannaCry = qurd + şifrələyici.

Çoxmərhələli hücumda komponentlərin işi ayrılır: birinci komponent qısa müddət yaşayır, ikinci əlaqə yaradır, üçüncü məlumat toplayır. Kitabxana kompüterində tapılmış ilk faylın silinməsi zəncirin digər hissələrinin də silindiyini göstərmir; ikinci yük, davamlılıq mexanizmi və oğurlanmış hesablar qala bilər. Təsnifatın əməliyyat dəyəri hansı əlavə izləri axtarmaq lazım olduğunu göstərməsidir.

| Növ | Onu fərqləndirən xüsusiyyət | Universitet nümunəsi |
| --- | --- | --- |
| Virus | Kodunu başqa obyektə əlavə edərək çoxalır | Yoluxmuş laboratoriya proqramı digər icraolunan faylları dəyişir |
| Qurd (worm) | Özünü çoxaldaraq sistemlər arasında yayıla bilir | Yoluxmuş cihaz açıq şəbəkə xidmətindən başqa cihazlara keçir |
| Troyan (Trojan) | Faydalı görünüş altında zərərli funksiya gizlədir | Saxta statistik proqram quraşdırıcısı parol oğurlayır |
| Ransomware | Girişi məhdudlaşdırıb və ya məlumatı şifrələyib fidyə istəyir | Kafedranın ortaq qovluqları açılmır |
| Spyware | İstifadəçini və fəaliyyəti gizli izləyir | İşçi kompüterində ekran və yazışmalar toplanır |
| Rootkit | Özünü və başqa zərərli fəaliyyəti gizlədir | Yoxlama aləti bəzi prosesləri göstərmir |
| Bootkit | Yükləmə zəncirinə yerləşir | Kod əməliyyat sistemindən əvvəl işə düşür |
| Bot və botnet | Uzaqdan tapşırıq alan düyün və belə düyünlər toplusu | Yataqxana cihazları eyni hücum üçün idarə olunur |
| Faylsız fəaliyyət | Əsas icra yaddaş və mövcud sistem alətləri üzərində qurulur | Skript mühiti yaddaşda zərərli kod işlədir |
| Wiper | Məlumatı və ya sistem strukturlarını dağıdır | İmtahan arxivinin faylları korlanır |
| Kriptocəker (cryptojacker) | Resursları icazəsiz kriptovalyuta hasilatına sərf edir | Elmi hesablama serverində gizli hasilat gedir |
| RAT | Gizli uzaqdan idarəetmə funksiyaları verir | Hücumçu dekanlıq cihazında əmr işlədir |
| Yükləyici (loader) | Başqa yükü icraya hazırlayıb işə salır | İlkin komponent yaddaşda ikinci modulu başladır |

### Virus, qurd və troyan

**Virus.** Çoxalması üçün yoluxdurduğu obyektin kodu icra edilməli və ya aktiv məzmunu uyğun proqramda emal olunmalıdır. Obyekt proqram faylı, makrolu sənəd və ya yükləmə sahəsi ola bilər. Aktivləşmə mütləq istifadəçinin əl ilə klik etməsini tələb etmir: yoluxmuş yükləmə kodu sistem başlayanda işləyə bilər. Laboratoriyadakı bir proqram virusla yoluxubsa, digər dəyişdirilmiş obyektlər də tapılmalıdır; yalnız ilk xəbərdarlıq verilən faylı silmək yetərli olmaya bilər.

**Qurd.** Başqa proqram faylına yapışmadan özünü çoxaldıb yayılır. Şəbəkə xidmətinin zəifliyi, zəif autentifikasiya və açıq paylaşım yayılmaya yol aça bilər. İlkin nümunənin işə düşməsi istifadəçi hərəkətindən asılı olsa da, sonrakı yayılma avtomatlaşdırıla bilər. Bir tələbə laboratoriyasının yoluxması server seqmentinə avtomatik yol açmamalıdır: seqmentasiya və xidmətlərə dar giriş qaydaları qurdun hərəkət sahəsini azaldır.

**Troyan.** Meyar aldadıcı təqdimatdır. Tələbə lisenziyasız mühəndislik proqramı yükləyir, quraşdırıcı isə əlavə casus komponent başladır. Troyanın özünü çoxaltması tələb olunmur. Etibarlı görünən interfeys, işləyən əsas proqram və rəqəmsal imza da gizli funksiyanın olmadığını sübut etmir. Quraşdırıcının mənbəyi, paket bütövlüyü və davranışı birlikdə yoxlanır.

### Məlumat oğurlayan və idarəetmə verən komponentlər

Casus proqramın (spyware) məqsədi gizli müşahidədir. Klaviatura yazılarını toplayan komponent keylogger adlanır. Məlumat oğurlayan proqram (infostealer) parollara, brauzer kukilərinə, sessiya tokenlərinə, saxlanılmış açarlara yönəlir. Qruplar kəsişə bilər, amma hər casus proqram yalnız parol oğurlamır və hər infostealer klaviaturanı izləmir.

Sessiya tokeni istifadəçinin artıq autentifikasiyadan keçdiyini xidmətə göstərən məlumatdır. Tokenin növündən və xidmətin nəzarətlərindən asılı olaraq oğurlanması parol və çoxamilli autentifikasiya addımını təkrar keçmədən giriş verə bilər. Əməkdaş yoluxmuş cihazda parolunu dəyişəndə iki risk qalır: yeni parol yenidən oğurlana bilər, əvvəlki sessiya isə qüvvədə qala bilər. Təmiz cihaz, sessiyaların ləğvi və hesab dəyişikliklərinin yoxlanması birlikdə lazımdır.

Arxa qapı (backdoor) gözlənilən giriş nəzarətindən yan keçən gizli giriş yoludur. Uzaqdan giriş troyanı (Remote Access Trojan, RAT) əmr icrası, fayl ötürməsi və bəzən ekran müşahidəsi imkanı verir. RAT arxa qapı yarada bilər, amma arxa qapı həmişə tam RAT deyil: kitabxana serverinə əlavə edilmiş gizli hesab ayrıca RAT olmadan geri qayıtmaq imkanı yaradır.

Bot verilən tapşırıqları uzaqdan alan proqram və ya yoluxmuş düyündür; botnet belə düyünlərin idarə olunan toplusudur. Yataqxana şəbəkəsindəki yoluxmuş cihazlar spam göndərmək, parol sınaqları aparmaq və ya paylanmış xidmət hücumu üçün işlədilə bilər. RAT daha çox bir cihaz üzərində interaktiv nəzarəti, botnet çoxsaylı düyünün koordinasiyasını təsvir edir; eyni proqram hər iki xüsusiyyəti daşıya bilər.

### Gizlədən, dağıdan və resurs işlədən növlər

**Rootkit** faylları, prosesləri, bağlantıları və başqa izləri gizlətmək üçün sistemin müşahidə mexanizmlərinə müdaxilə edən komponentlər toplusudur; istifadəçi məkanında da, nüvə səviyyəsində də işləyə bilər. **Bootkit** yükləmə zəncirinə yerləşir və əməliyyat sistemi tam başlamazdan əvvəl işə düşə bilər. Hər rootkit bootkit deyil. Belə müdaxilədə yoluxmuş sistemin verdiyi siyahıya tam etibar etmək olmaz; etibarlı kənar mühitdən yoxlama və sistemin yenidən qurulması lazım gələ bilər.

**Wiper** məlumatı və ya fayl sistemi kimi strukturları dağıtmağa yönəlir (NotPetya buna nümunədir). Ransomware fidyə üçün istifadəni məhdudlaşdırır; mesajları oxşar olsa da, bərpa imkanı və məqsədləri fərqlənə bilər. Hücumçu dağıdıcı proqramı şifrələyici kimi təqdim edə bilər: imtahan arxivində fidyə qeydi tapılması faylların açarla geri qaytarılacağını sübut etmir. Texniki təhlil olmadan ödəniş mesajından bərpa nəticəsi çıxarmaq olmaz.

**Kriptocəker** universitetin CPU, GPU və ya bulud resurslarını icazəsiz hasilata sərf edir. Qanuni tədqiqat hesablaması da yüksək yük yaradır, ona görə analitik prosesi, sahibi olan hesabı, işin sifarişini, konteyner təsvirini və xarici əlaqələri yoxlayır. **Məntiqi bomba (logic bomb)** müəyyən vaxt və ya şərt ödənəndə işə düşən zərərli məntiqdir (məsələn, kafedranın arxivini müəyyən tarixdə silən gizli funksiya); yayılma qabiliyyəti olması tələb edilmir.

**Dropper** daxilində daşıdığı yükü mühitə yerləşdirir. **Endirici (downloader)** yükü şəbəkədən alır. **Yükləyici (loader)** yükü icraya hazırlayır, yaddaşa yerləşdirə və başlada bilər. Adlandırma praktikada kəsişir: bir komponent həm endirə, həm aça, həm də icra edə bilər. Analitik ad üzərində dayanmaq əvəzinə hansı faylın haradan gəldiyini, hara yazıldığını və hansı prosesdə işlədiyini sənədləşdirir.

## Yoluxma yolları və hücumun ardıcıllığı

### İlkin girişin mənbələri

İlkin giriş (initial access) hücumçunun sistemə ilk çıxışıdır. Yoluxma vektoru (infection vector) zərərli kodun çatdırıldığı və ya icraya gətirildiyi yoldur. Bunlar tam eyni deyil: oğurlanmış VPN hesabı ilkin giriş verə bilər, zərərli proqram sonradan yerləşdirilər; fişinq məktubu parol oğurlaya bilər və cihazda heç bir kod işlətməyə bilər.

| Vektor | Universitetdə mümkün yol | Tədbir və məhdudiyyət |
| --- | --- | --- |
| Fişinq əlavəsi | Dekanlığa saxta qiymət cədvəli gəlir | Əlavə təhlili, aktiv məzmun məhdudiyyəti, istifadəçi bildirişi |
| Keçid və saxta yenilənmə | Kitabxana səhifəsi əvəzinə saxta quraşdırıcı açılır | Veb nəzarəti və rəsmi proqram mənbəyi; domen görünüşü kifayət etmir |
| Zəif xidmət | Yamaqlanmamış LMS komponenti istismar olunur | Aktiv inventarı, yamaq, xarici girişin daraldılması |
| Etibarsız paket | Laboratoriya üçün krek və ya dəyişdirilmiş kitabxana alınır | Təsdiqli repozitoriya və paket yoxlaması |
| Çıxarılan daşıyıcı | Laboratoriyaya yoluxmuş USB gətirilir | Daşıyıcı siyasəti və icra nəzarəti; qoşulma həmişə yoluxma deyil |
| Oğurlanmış hesab | Hücumçu VPN-dən daxil olub yük yerləşdirir | MFA, cihaz nəzarəti, sessiya monitorinqi |
| Təchizat zənciri | Etibar edilən yenilənmə və ya asılılıq dəyişdirilir | Mənbə, imza, qurma prosesi və sonrakı davranışın yoxlanması |

Fişinqin uğuru işin kontekstinə bağlıdır (semestr sonunda qiymət cədvəli, qəbul dövründə qeydiyyat sənədi, lisenziya yenilənməsi). Müdafiə istifadəçidən hər texniki detalı tanımağı gözləməməlidir: təhlükəli aktiv məzmunun məhdudlaşdırılması, faylların açılmadan yoxlanması və şübhəli məktubu bildirmək üçün sadə kanal istifadəçi səhvinin təsirini azaldır.

Təchizat zənciri hücumunda etibar edilən məhsul, yenilənmə, asılılıq və ya paylama kanalı dəyişdirilir. Rəsmi mənbə şərti yoxlamadır, mütləq zəmanət deyil. LMS üçün plagin seçəndə onun tələb etdiyi icazələr, yenilənmə yolu və işlədiyi hesab da yoxlanmalıdır. İmzalanmış paketdə zərərli kod varsa, düzgün imza həmin kodu təhlükəsiz etmir.

### İcra və proses ağacı

Proses ağacı (process tree) hansı prosesin hansını başlatdığını göstərir. Sənədi açan `winword.exe`-nin ardınca `powershell.exe` başlaması araşdırma səbəbidir. Ən güclü aşkarlama siqnallarından biri gözlənilməyən proses ağacıdır: Word, Excel və ya PDF oxuyucusunun `cmd.exe`, `powershell.exe`, `wscript.exe` başlatması normal iş axınında demək olar olmur. Bu əlaqə təkbaşına hökm deyil: bəzi təsdiqli iş axınları skript işlədə bilər, ona görə sənədin mənbəyi, əmr sətri, yaranan fayl, hesab və xarici bağlantı birlikdə yoxlanır.

:::figure
src = "m10-1.png"
alt = "Sxem: winword.exe (Qiymet_yekun.docm) bir oxla splwow64.exe (adi, çap) prosesinə, başqa oxla powershell.exe (şübhəli skript) prosesinə gedir; powershell.exe profilə fayl yazır, schtasks ilə yeni tapşırıq yaradır və update-campus.example domeninə qoşulur."
caption = "Şəkil 1. Sənədin açılmasından sonrakı adi və şübhəli proses əlaqələri; hər iki budaq şərti nümunədir."
:::

Şərti zəncirdə dekanlıq əməkdaşı `Qiymet_yekun.docm` açır. Sənəd proqramı skript mühiti başladır, skript istifadəçi profilinə fayl yazır, yeni planlaşdırılmış tapşırıq yaranır və proses `update-campus.example` domeninə qoşulmağa çalışır. Bunlar xam müşahidələrdir; əlaqələr təsdiqlənəndə çoxmərhələli yoluxma fərziyyəsi güclənir.

Faylın diskə gəlməsi, prosesin başlaması və yükün uğurlu işləməsi ayrı faktlardır. Poçt sistemi əlavəni çatdırıb, antivirus isə icradan əvvəl karantinə ala bilər; onda məktubu alan hər əməkdaş yoluxmuş sayılmır. Analitik çatdırılmanı, açılmanı, proses yaradılmasını və sonrakı davranışı ayırır, çünki insidentin əhatəsi şişirdilməməlidir.

### Mərhələlər və səbəb əlaqəsi

Tipik ardıcıllıq: ilkin giriş (fişinq məktubu, zəif proqram, krek, flaş kart, oğurlanmış hesab, təchizat zənciri) → icra → davamlılıq (xidmət, reyestrin Run açarı, planlaşdırılmış tapşırıq, ATT&CK T1053) → imtiyazların artırılması → daxili hərəkət → idarəetmə (C2) → məlumatın çıxarılması və ya şifrələmə (təsir). Lakin bu məcburi və dəyişməz sıra deyil: hücumçu davamlılıq qurmadan məlumat çıxara, artıq imtiyazlı hesabla girdiyinə görə səlahiyyət artırmanı keçə və C2 olmadan əvvəlcədən verilmiş tapşırığı icra edə bilər. Müdafiə xəritəsi real müşahidəyə əsaslanmalıdır.

İmtiyazların artırılması (privilege escalation) mövcud girişdən daha yüksək səlahiyyət almaqdır. Daxili yan hərəkət (lateral movement) bir sistemdən başqasına keçməkdir. Kafedra kompüterində administrator olmaq birinciyə, oradan fayl serverinə oğurlanmış hesabla giriş ikinciyə nümunədir. Adi tələbə hesabı ilə bir neçə xidmətə giriş mümkündürsə, yan hərəkət üçün yerli administrator səlahiyyəti şərt deyil.

MITRE ATT&CK taktikanı hücumçunun məqsədi, texnikanı məqsədə çatma üsulu kimi təsvir edir. Planlaşdırılmış tapşırıqdan istifadə T1053 texnikası ilə əlaqələndirilə bilər; müşahidənin daha dəqiq alttexnikaya uyğunluğu ayrıca yoxlanır. Eyni üsul müxtəlif qruplarda görünür, ona görə texnika uyğunluğu hücumçunun kimliyini, ölkəsini və ya niyyətinin bütün detallarını müəyyən etmir.

ATT&CK xəritəsi yazılarkən versiya saxlanılmalıdır. 28 aprel 2026-cı il tarixli v19-da əvvəlki Enterprise Defense Evasion bölgüsü Stealth (TA0005) və Defense Impairment (TA0112) kimi ayrılıb. Windows hadisə jurnallarının təmizlənməsi T1685.005 altında göstərilir; köhnə mənbələrdə T1070.001 nömrəsi qalır. Köhnə qaydaları yeniləyərkən davranışın özü ilə dəyişən təsnifat identifikatoru qarışdırılmamalıdır.

## Davamlılıq və gizlənmə

### Windows-da davamlılıq

Davamlılıq (persistence) proqram bağlandıqdan, istifadəçi hesabdan çıxdıqdan və ya sistem yenidən başladıqdan sonra hücumçunun giriş və icra imkanını saxlamaq üsuludur. Yeni xidmət və ya tapşırıq tapılması avtomatik yoluxma demək deyil (ehtiyat nüsxə agenti də belə işləyir): yaranma vaxtı, yaradan hesab, başladılan fayl və təsdiqli dəyişiklik sifarişi tutuşdurulur.

Run açarları uyğun istifadəçi daxil olanda proqram başladır; xidmətlər sistem başlanğıcında və başqa şərtlərlə işləyir; planlaşdırılmış tapşırıqlar giriş, vaxt və hadisə kimi tətikləyicilərdən istifadə edir; başlanğıc qovluqları və WMI hadisə abunələri də araşdırıla bilər. İstifadəçi səviyyəsində qurulan mexanizm üçün həmişə administrator hüququ lazım deyil; təsir dairəsi və tələb olunan icazələr ayrıca qiymətləndirilir.

| Mexanizm | Yoxlanılan məlumat | Şübhəni artıran kontekst |
| --- | --- | --- |
| Run və RunOnce açarları | Dəyər, tam yol, istifadəçi, dəyişmə vaxtı | Poçt əlavəsindən sonra profil qovluğuna işarə yaranır |
| Planlaşdırılmış tapşırıq | Əməl, tətikləyici, hesab, yaradılma izi | Təsdiqsiz skript qeyri-adi vaxtda başlayır |
| Xidmət | İcra yolu, başlama rejimi, hesab | Yazıla bilən müvəqqəti qovluqdan icra var |
| Başlanğıc qovluğu | Qısayolun hədəfi və faylın mənbəyi | İstifadəçi tanımadığı proqramı girişdə başladır |
| WMI abunəsi | Filtr, istehlakçı və onların əlaqəsi | Sənəd açıldıqdan sonra gizli skript icrası qurulur |

Oxuma üçün nümunə əmrlər (davamlılıq yaratmır, yalnız səlahiyyətli araşdırma üçündür; çıxışda istifadəçi adları və həssas yollar ola bilər, saxlandığı yer də sübut kimi qorunur):

```powershell
reg query HKCU\Software\Microsoft\Windows\CurrentVersion\Run
schtasks /query /fo LIST /v
Get-CimInstance Win32_Service | Select-Object Name, StartMode, PathName, StartName
```

Birinci əmr yalnız cari istifadəçinin açarını göstərir; digər profillər və sistem səviyyəsindəki açarlar ayrıca yoxlanmalıdır. Tapşırığın təsadüfi görünən adı hökm üçün yetmir: analitik göstərdiyi faylın mövcudluğunu, heşini, imzasını və proses əlaqəsini yoxlayır. İcra yolu silinmiş fayla gedirsə, əvvəlki telemetriya boşluğu doldura bilər.

### Linux-da davamlılıq

Linux-da systemd xidmətləri və taymerləri, cron tapşırıqları, istifadəçi başlanğıc faylları və SSH açarları araşdırılır. LMS serverində tətbiqin xidmət hesabı ələ keçirilibsə, hücumçu həmin hesabın yaza bildiyi konfiqurasiyadan yararlana bilər. Sistem səviyyəsində xidmət yaratmaq ilə istifadəçinin öz xidmətini dəyişmək eyni səlahiyyət tələb etmir.

| Mexanizm | Araşdırılan obyekt | Universitetdə yoxlama sualı |
| --- | --- | --- |
| systemd | Sistem və istifadəçi vahidləri, ExecStart yolu | Bu xidmət LMS paketinə aiddirmi? |
| cron və taymer | Cədvəl, icra hesabı, göstərilən skript | Gecə başlayan skript təsdiqli ehtiyat nüsxədirmi? |
| SSH authorized_keys | Əlavə açar, fayl sahibi, vaxt izləri | Kafedra serverinin sahibi bu açarı tanıyırmı? |
| Shell başlanğıcı | `.profile` və uyğun shell sazlamaları | İnzibatçı daxil olanda əlavə kod başlayırmı? |
| Tətbiq əlavəsi | Plagin, modul, veb tətbiq faylları | Yenilənmədən kənar dəyişiklik varmı? |

```bash
systemctl list-unit-files --type=service
systemctl list-timers --all
systemctl --user list-unit-files --type=service
crontab -l
journalctl -u lms.service --since '2026-11-01 00:00:00'
```

`crontab -l` yalnız cari hesabın cədvəlini göstərir; başqa hesabların, sistem cədvəllərinin və konteynerlərin yoxlanması ayrıca səlahiyyət və əhatə tələb edir. Xidmət adı və tarix şərti nümunədir. Xidmət faylında görünən proqram qanuni olsa da, arqumenti və mühiti dəyişdirilmiş ola bilər: kitabxana serverində qanuni arxiv alətinin yad qovluğu kənara çıxarması buna nümunədir. Yalnız proqram adını icazəli siyahı ilə müqayisə etmək belə sui-istifadəni qaçıra bilər.

### Obfuskasiya və faylsız fəaliyyət

Obfuskasiya (obfuscation) kodun mənasını oxumağı çətinləşdirir. Paketləmə (packing) icraolunan məzmunu sıxılmış və ya çevrilmiş formada saxlayıb icra zamanı açmağa imkan verir. Hər ikisindən qanuni proqram da istifadə edə bilər. Faylda yüksək entropiya paketləmə ehtimalını artırır, amma sıxılmış arxiv və şifrələnmiş resurs da oxşar nəticə verir; tək ölçü əsasında zərərli hökmü çıxarılmır.

**Polimorf** yanaşmada nüsxələr arasında şifrələnmiş (kodlaşdırılmış) görünüş və onu açan hissə dəyişə bilər (hər nüsxədə şifrələnmə dəyişir). **Metamorf** yanaşmada funksiyanı saxlayan kodun quruluşu yenidən yazılır. Hər iki halda konkret baytlara və heşə əsaslanan aşkarlama məhdudlaşır. Laboratoriya proqramının müxtəlif zərərli variantları ayrı heşlər versə də, eyni icazəsiz xidmət yaratması davranış əsasında görünə bilər.

Faylsız (fileless) fəaliyyətdə icranın əsas hissəsi yaddaşda və mövcud sistem vasitələri üzərində qurulur; PowerShell və Windows Management Instrumentation (WMI) cəlb edilə bilər, diskə ənənəvi exe yazılmır. Termin bütün zəncir boyu diskdə heç nə olmadığını bildirmir: reyestr dəyəri, skript jurnalı, planlaşdırılmış tapşırıq və yaddaş səhifəsi iz saxlaya bilər. Kafedra kompüterində ayrıca zərərli exe tapılmaması araşdırmanı bağlamaq üçün əsas deyil.

## Komanda-idarəetmə və ikiqat şantaj

### C2 əlaqəsi necə qurulur

Komanda-idarəetmə (Command and Control, C2) yoluxmuş sistemə tapşırıq göndərmək və nəticə almaq mexanizmidir. Daxildən başlayan bağlantı hücumçu üçün əlverişlidir: firewall veb çıxışına icazə verə bilər, kənardan yeni girişə isə icazə verməz. Bu səbəbdən yalnız daxil olan trafikin yoxlanması RAT və bot fəaliyyətini görməyə kifayət etmir.

C2 birbaşa serverə, vasitəçi düyünə və ya qanuni xidmət üzərindən qurula bilər. Tapşırıq almaq üçün dövri müraciət **beacon** adlanır. Hücumçu aralıqları təsadüfiləşdirə bilər; bu dəyişkənlik **jitter**dir. Tam sabit dövr olmaması C2-ni istisna etmir. Eyni şəkildə, kitabxananın yenilənmə agentinin dövri əlaqəsi də zərərli deyil; məqsəd ünvanı ilə prosesi birləşdirməkdir.

| Üsul | Görünə bilən məlumat | Aşkarlamanın sərhədi |
| --- | --- | --- |
| HTTP və HTTPS | İstiqamət, vaxt, həcm, mümkün proksi məlumatı | Şifrələnmiş məzmun açıq görünmür |
| DNS üzərindən əlaqə | Sorğu adları, tezlik, uzun subdomenlər | CDN və təhlükəsizlik alətləri də mürəkkəb adlardan istifadə edir |
| Qanuni bulud xidməti | Tətbiq prosesi, tenant və hesab konteksti | Xidmət domeninin özü ümumi bloklama üçün zəif seçimdir |
| Birbaşa IP əlaqəsi | Proses, port, istiqamət, sessiya müddəti | Portun adi olması fəaliyyəti qanuni etmir |
| Həmyaşıd şəbəkə (P2P) | Çoxsaylı düyünlə əlaqə və topologiya | Mərkəzi domeni bloklamaq əlaqəni tam kəsməyə bilər |
| Domen yaratma alqoritmi (DGA) | Çoxsaylı mümkün domen, uğursuz sorğular | Hər təsadüfi görünən domen DGA deyil |

DNS qeydləri ilə DNS sorğu jurnalları ayrılmalıdır. A və AAAA qeydləri adın ünvanla əlaqəsini göstərir; onları görmək konkret cihazın həmin ada müraciət etdiyini sübut etmir. Bunun üçün müştəri ünvanı, sorğu adı və vaxtı saxlayan sorğu jurnalı lazımdır. Cihaz alternativ və ya şifrələnmiş resolver istifadə edirsə, universitetin yerli resolverində sorğu olmaya bilər.

Şərti nümunədə `192.0.2.25` cihazından `sync-campus.example` domeninə müntəzəm kiçik HTTPS bağlantıları görünür. Proksi jurnalında bu əlaqəni tədqiqat proqramı da yarada bilər. EDR eyni əlaqəni yeni və imzasız prosesə bağlayır, proses də şübhəli sənəddən yaranıbsa, fərziyyə güclənir. Sertifikat, port və domen ayrı-ayrılıqda hücumun məqsədini sübut etmir.

### Məlumatın çıxarılması ilə əlaqə

Məlumatın icazəsiz çıxarılması (exfiltration) nəzarət etdiyiniz mühitdən həssas məlumatın kənara ötürülməsidir. C2 ilə eyni kanaldan istifadə edə bilər, amma bu məcburi deyil: hücumçu tapşırığı bir domendən alıb tələbə siyahısını başqa saxlama xidmətinə göndərə bilər. C2 bloklandıqdan sonra əvvəlcədən verilmiş çıxarma tapşırığı da davam edə bilər.

Həcmə əsaslanan xəbərdarlıq böyük arxivləri tapmağa kömək edir, lakin kiçik sızma da ağır ola bilər: administrator açarı və ya sessiya tokeni böyük fayl deyil. Kitabxana serverinin az trafik göndərməsi məxfiliyin qorunduğunu göstərmir. Fayla giriş, arxiv yaradılması, hesab hüququ və şəbəkə ötürməsi arasındakı əlaqə araşdırılır.

### Ransomware və ikiqat şantaj

İkiqat şantajda (double extortion) hücumçu həm işin dayanması, həm də oğurlanmış məlumatın yayılması ilə təzyiq göstərir. Tipik ssenari: giriş əldə edilir, hesablar və şəbəkə öyrənilir, həssas məlumat seçilib çıxarılır, bərpa imkanları zəiflədilir, sonra şifrələmə və tələb mesajı gəlir. Kampaniyalarda sıra və komponentlər dəyişə bilər. Hər ransomware hücumunda məlumat oğurlandığını fərz etmək də, oğurluq olmadığını qəbul etmək də səhvdir (çox vaxt əvvəlcə məlumat oğurlanır, amma məcburi deyil).

:::figure
src = "m10-2.png"
alt = "Sxem: ilkin giriş (VPN, fişinq), yayılma (hüquq artımı), məlumatın çıxarılması, şifrələmə (ehtiyat silinir) ardıcıl gedir; çıxarılmadan məlumatın yayılması təhdidi (hüquq, bildiriş, sızma araşdırması), şifrələmədən xidmətin dayanması (təcrid, təmiz ehtiyatdan bərpa) qolu ayrılır."
caption = "Şəkil 2. İkiqat şantajda xidmətin dayanması və məlumatın yayılması riskləri ayrı cavab tələb edir."
:::

Şərti ssenaridə hücumçu tələbə qeydiyyatı bazasının ixracını çıxarır, sonra fayl serverini şifrələyir. Təcrid edilmiş ehtiyat nüsxə sayəsində LMS geri qayıdır, çıxarılmış siyahı isə hücumçuda qala bilər. Bərpa komandası xidməti qaytarır, məxfilik araşdırması hansı məlumatın, kimin hesabı ilə və nə vaxt çıxarıldığını müəyyən edir. Bir işin bitməsi o birini bağlamır.

| İstiqamət | Yoxlanılan məsələ | Uyğun cavab |
| --- | --- | --- |
| Əlçatanlıq | Hansı xidmət və fayllar istifadə olunmur? | Təcrid, təmiz qurulum, yoxlanmış nüsxədən bərpa |
| Məxfilik | Hansı məlumat kənara ötürülüb və ya əlçatan olub? | Giriş və ötürmə təhlili, sessiyaların ləğvi, bildiriş qərarı |
| Bütövlük | Baza, konfiqurasiya və ehtiyat nüsxə dəyişdirilibmi? | Etibarlı nüsxə ilə müqayisə, tətbiq səviyyəsində yoxlama |

Bərpa nüsxələrinin idarəetmə hesabları istehsal domenindən asılı olmamalıdır. Nüsxə dəyişdirilməz saxlamada olsa da, bərpa üsulu və açarları sınaqdan keçirilməyibsə, böhran zamanı yararsız qala bilər. Tələbə bazası üçün uğurlu sınaq faylın açılması ilə bitmir: bazanın ardıcıllığı, tətbiqin işə düşməsi və lazımi məlumatın mövcudluğu yoxlanır. Fidyə ödəmək açarın işləməsinə və oğurlanmış məlumatın silinməsinə zəmanət vermir.

## Artefakt, IoC və IoA

### Müşahidədən indikatoradək

Artefakt (artifact) fəaliyyətin yaratdığı texniki izdir: yeni fayl, reyestr dəyəri, DNS sorğusu, giriş qeydi. Kompromitasiya indikatoru (Indicator of Compromise, IoC) zərərli fəaliyyətlə əlaqələndirilmiş müşahidə olunan iz və ya xüsusiyyətdir; dəyəri ilə birlikdə əlaqənin sübutu, vaxtı və etibarlılıq dərəcəsi də saxlanılır. Sadə domen siyahısı bu konteksti itirə bilər.

Hücum indikatoru (Indicator of Attack, IoA) hücumun gedişini göstərən davranışa yönəlir: sənədin skript başlatması, sonra davamlılıq yaratması və naməlum istiqamətə qoşulması IoA yönümlü məntiqdir. Terminlərin sərhədi bütün mənbələrdə eyni deyil; davranış IoC-si anlayışı da işlənir. Praktik fərq qaydanın konkret dəyəri axtarması ilə hərəkət əlaqəsini axtarması arasındadır.

| Meyar | Artefakt | IoC | IoA |
| --- | --- | --- | --- |
| Əsas sual | Nə müşahidə olunub? | Hansı iz zərərli fəaliyyətlə bağlıdır? | Hansı şübhəli davranış baş verir? |
| Nümunə | Profil qovluğunda fayl var | Fayl təsdiqlənmiş zərərli nümunə ilə eyni SHA-256 verir | Sənəd skript başladır və davamlılıq yaradır |
| Qərar dəyəri | Araşdırmanın xam materialı | Uyğunluq axtarışı və məhdudlaşdırma üçün yararlı | Variant dəyişsə də ardıcıllığı göstərə bilər |
| Məhdudiyyət | Zərərli əlaqə hələ sübut olunmayıb | Dəyər dəyişə və ya kontekst köhnələ bilər | Qanuni avtomatlaşdırma oxşar görünə bilər |

IoC yalnız insidentdən sonra istifadə edilmir: əvvəlki araşdırmadan məlum zərərli domen bloklananda növbəti yoluxma məhdudlaşdırıla bilər. IoA da həmişə hadisəni qabaqlamır; onu qurmaq üçün artıq baş vermiş davranış lazım ola bilər. Vaxt fərqi yerinə aşkarlama məntiqinin hansı sübuta söykəndiyini izah etmək daha dəqiqdir.

### İndikatorların qrupları

Obyektə görə fayl, şəbəkə, sistem, proses, hesab və poçt indikatorları ayrılır. Eyni indikator bir neçə mənbədə görünə bilər: poçt əlavəsinin heşi fayl indikatorudur, amma onu poçt şlüzü və EDR ayrı mərhələlərdə müşahidə edir. Analitik uyğunluqları birləşdirib çatdırılmadan icraya keçidi yoxlayır.

| Qrup | Dəyər və ya xüsusiyyət | Ehtiyatlı şərh |
| --- | --- | --- |
| Fayl | Heş (SHA-256), ad, ölçü, tam yol, imza | Ad asan dəyişir, heş konkret məzmuna bağlıdır |
| Şəbəkə | IP, domen, URL, protokol izi, qeyri-adi port, DNS sorğuları, müntəzəm beacon bağlantıları | Eyni infrastrukturdan qanuni istifadəçilər də yararlana bilər |
| Sistem | Xidmət, tapşırıq, reyestr dəyişikliyi | Qanuni quraşdırma ilə tutuşdurulmalıdır |
| Proses | Valideyn, övlad, əmr sətri, icra hesabı | PID yenidən istifadə oluna bilər |
| Hesab | Yeni (admin) hesab, imtiyaz, sessiya fəaliyyəti, qeyri-adi giriş | Dəyişiklik sifarişi və istifadəçinin işi yoxlanır |
| Poçt | Başlıqlar, əlavə heşi, keçid, cavab ünvanı, saxta göndərici | Görünən göndərən adı həqiqi mənbəni sübut etmir |

Təqdimat üsuluna görə üç tip fərqləndirmək faydalıdır. **Atomar (atomic)** indikator müqayisə üçün ayrıca dəyərdir: domen, IP və ya poçt ünvanı. **Hesablanmış (computed)** indikator məlumat üzərində əməliyyatdan alınır; fayl heşi buna nümunədir. **Davranış (behavioral)** indikatoru hadisələr arasındakı münasibəti təsvir edir. Bu bölgü bütün məhsullara məcburi sxem deyil, izah və layihələndirmə üsuludur.

### Heşlər və onların sərhədləri

Kriptoqrafik heş (cryptographic hash) dəyişən ölçülü məlumatdan sabit uzunluqlu nəticə hesablayır. SHA-256 nəticəsi 256 bitdir və adətən 64 onaltılıq simvolla yazılır. Eyni bayt ardıcıllığı eyni heş verir. Faylın yalnız adının dəyişməsi heşi dəyişmir; məzmun dəyişikliyi (içində bir bayt belə) praktikada fərqli nəticə yaradır. Bu eyni nümunəni tapmağa və sübutun ötürülmə zamanı dəyişmədiyini yoxlamağa kömək edir.

Heş faylın təhlükəsizliyini özü müəyyən etmir: qanuni proqramın da heşi var. Zərərli nümunənin heşinə uyğunluq həmin məzmunun mövcudluğunu göstərir, icrasını göstərmir. Karantin anbarında fayl tapılması ilə işçi kompüterində proses kimi işləməsi ayrı qiymətləndirilir. Paketlənmiş nümunənin başqa variantını tapmaq üçün tək heş yetərli deyil.

MD5 və SHA-1 üçün toqquşmaya davamlılıq zəifləyib: fərqli məzmunlar üçün eyni heş yaratmaq mümkün olan hücumlar məlumdur. Buna görə düşmənin qəsdən məzmun hazırlaya bildiyi şəraitdə güclü identifikasiya və bütövlük yoxlaması üçün SHA-256 üstün tutulur. Toqquşma hücumu hər hansı hazır zərərli fayl üçün dərhal qanuni əvəz yaratmaq demək deyil; bu, ikinci ilkin təsvir hücumu ilə eyni məsələ deyil. Köhnə heşlə uyğunluq axtarışı faydasız olmur, amma etibarlı bütövlük hökmü üçün zəif əsasdır.

| Məsələ | Heş nə verir? | Nəyi vermir? |
| --- | --- | --- |
| Eyni nümunənin axtarışı | Tam məzmun uyğunluğunu müqayisə edir | Bütün ailə və variantları tapmır |
| Sübutun ötürülməsi | Dəyişiklik olub-olmadığını yoxlamağa kömək edir | İlkin götürülmənin düzgünlüyünü sübut etmir |
| Reputasiya yoxlaması | Məlum nəticə ilə əlaqə yaradır | Bazadakı qeydin doğruluğuna zəmanət vermir |
| Faylın icrası | İcra olunan fayl telemetriyası ilə əlaqələnə bilər | Diskdəki uyğunluq icra sübutu deyil |

### Ağrı piramidası

David Biankonun Ağrı piramidası (Pyramid of Pain) indikator bloklananda hücumçunun onu dəyişmək üçün çəkdiyi çətinliyi izah edir. Aşağıdan yuxarı: heşlər, IP ünvanları, domen adları, şəbəkə və host artefaktları, alətlər, taktika, texnika və prosedurlar (Tactics, Techniques and Procedures, TTP). Bu, indikatorun riyazi etibarlılıq balı və ya bütün hallara aid xərc ölçüsü deyil.

:::figure
src = "m10-3.png"
alt = "Altı pilləli piramida; aşağıdan yuxarı: heş dəyərləri, IP ünvanları, domen adları, artefaktlar (şəbəkə və host izləri), alətlər, TTP (iş üsulu). Yanda yuxarı ox: hücumçu üçün dəyişdirmə çətinliyi artır."
caption = "Şəkil 3. İndikatorun dəyişdirilməsi üçün hücumçuya düşən çətinliyin konseptual müqayisəsi."
:::

Hücumçu faylın baytlarını dəyişib heşdən qaça bilər; yeni domen almaq və alətini dəyişmək daha çox iş tələb edə bilər. Universitet tək domenə əlavə olaraq sənəddən başlayan skript, davamlılıq və məlumat çıxarma ardıcıllığını görürsə, hücumçu iş üsulunu dəyişməlidir. Yuxarı səviyyədə aşkarlama daha zəngin telemetriya və diqqətli sazlama tələb edir. Konkret heşlər sürətli məhdudlaşdırma üçün yenə faydalıdır; piramida onları atmağı tələb etmir.

## İndikatorların keyfiyyəti və həyat dövrü

### Dəyərdən qərara keçid

İndikatorun keyfiyyəti onun nə qədər tez bloklandığı ilə ölçülmür. Qiymətləndirilir: mənbənin etibarlılığı, zərərli əlaqənin gücü, zaman uyğunluğu, seçicilik və tətbiqin nəticəsi. Yüksək əminliklə zərərli sayılan IP paylaşılan xidmətə aid ola bilər; bütöv IP-ni bloklamaq kitabxananın qanuni resurslarını da bağlaya bilər. Daha dar URL, domen, hesab və ya proses səviyyəsində tədbir seçilir.

Etibarlılıq dərəcəsi (confidence) iddianı dəstəkləyən sübutun gücüdür. Təsir isə əlaqəli aktivə mümkün zərərdir. Prioritet qərarı bunların ikisindən və cari fəaliyyətin olub-olmamasından asılıdır: köhnə, etibarlı heş arxivdə tapılıbsa, təcili xidmət dayandırmaq lazım olmaya bilər; zəif əminlikli siqnal tələbə bazasında aktiv məlumat çıxarma ilə yanaşı görünürsə, təcili araşdırma tələb edir.

| Sahə | Saxlanılan məlumat | Nəyə görə lazımdır? |
| --- | --- | --- |
| Növ və dəyər | Domen, heş, yol və ya başqa xüsusiyyət | Düzgün müqayisə üsulu seçilir |
| Mənbə və mənşə | İnsident, analiz, ilkin hesabat | Təkrar yayılan bir mənbə çox təsdiq sayılmır |
| İlk və son müşahidə | Fəaliyyətin zaman sərhədləri | Tarixi uyğunluq cari uyğunluqdan ayrılır |
| Etibarlılıq və əsas | Sübut və qiymətləndirmə izahı | Analitik nəticəni yenidən yoxlaya bilir |
| Əlaqəli fəaliyyət | Proses, ailə, müşahidə olunmuş texnika | Kontekst saxlanılır |
| Tədbir və sahibi | İzləmə, araşdırma, bloklama, məsul şəxs | Qərar nəzarətsiz qalmır |
| Baxış və bitmə vaxtı | Təkrar yoxlama və aktiv tətbiq sərhədi | Köhnə bloklar yığılmır |
| Paylaşma məhdudiyyəti | TLP və məlumat sahibinin şərtləri | Məxfi kontekst təsadüfən yayılmır |

Şərti kartda `sync-campus.example` domeni daxili insidentdən götürülüb, EDR əlaqəsi və laboratoriya təhlili ilə təsdiqlənib. Universitet onu bloklamağı, mövcud qeydlərdə axtarmağı və müəyyən baxış tarixində yenidən qiymətləndirməyi qərara alır. Domenlə birlikdə tələbənin şəxsi adı və sənədi paylaşılmır: faydalı texniki siqnalın paylaşılması bütün sübut paketinin paylaşılması demək deyil.

### Toplama, normallaşdırma və zənginləşdirmə

Toplama daxili insidentdən, zərərli proqram təhlilindən, tələ sistemindən, təhlükəsizlik jurnallarından və etibarlı hesabatdan başlaya bilər. Xarici indikator axınının (feed) böyük olması yaxşı örtük demək deyil. Üç platformada eyni hesabatın təkrarlanması üç müstəqil təsdiq yaratmır; mənbə zənciri saxlanılmasa, eyni yanlış məlumat çoxsaylı sübut kimi görünə bilər.

Normallaşdırma müqayisə üçün formaları uyğunlaşdırır. Heşin onaltılıq yazılışında böyük və kiçik hərf eyni dəyəri göstərə bilər; domen adlarında hərf registri fərq yaratmır, URL yolunda fərq əhəmiyyətli ola bilər; Linux fayl yolunu kor-koranə kiçik hərfə çevirmək müqayisəni korlaya bilər. Xam və normallaşdırılmış dəyər ayrı saxlananda audit asanlaşır.

Zənginləşdirmə (enrichment) indikatorun kontekstini artırır: domenin hansı dövrdə hansı IP-yə açıldığı, ünvanın paylaşılan xidmətə aid olub-olmadığı, faylın imzası və müşahidə olunan davranış. Cari DNS cavabı keçmiş hücum vaxtındakı ünvanı mütləq göstərmir; əvvəlki domen bağlantısını araşdıranda həmin vaxtın jurnalı və tarixi əlaqələr lazımdır.

Nümunə və sənədləri açıq təhlil xidmətinə yükləmək ayrıca sızma yarada bilər (tələbə siyahısı içindəki makro şübhəsində sənəd bütövlükdə həssasdır); əvvəlcə heş sorğusu və daxili təhlil seçilə bilər. Heş sorğusu da xarici xidmətə məlumat ötürür, ona görə hansı xidmətə nə çıxacağı əvvəlcədən müəyyən edilir.

### Ömür, köhnəlmə və mübadilə

İndikatorun ömrü (lifetime) onun müəyyən qərar üçün yararlı qaldığı müddətdir. Heş eyni faylı illər sonra da tanıya bilər, amma ailənin dəyişmiş variantını tutmaya bilər; IP başqa müştəriyə verilə bilər; domen ələ keçirilmiş qanuni sayta aid olub sonradan təmizlənə bilər. Bütün indikatorlara eyni bitmə müddəti verilsə, bu fərqlər itir. IoC-nin dəyəri zamanla azalır.

Aktiv bloklamadan çıxarılan indikator tarixi araşdırmadan silinməyə bilər: keçmiş semestrin insidentini araşdırarkən köhnə domen bağlantısı yenə müqayisə edilir, amma həmin domenə bu gün avtomatik blok qoyulmur. Son görülmə vaxtı, yeni təsdiq, yanlış uyğunluqlar və sahiblik dəyişməsi baxış qərarına daxildir. Ömür yalnız təqvimlə deyil, kontekstlə idarə olunur.

:::figure
src = "m10-4.png"
alt = "Dövri sxem: toplama (insident, lent), təsdiq (mənbə, kontekst), zənginləşdirmə (TTP, son tarix), tətbiq (SIEM, EDR, DNS), qiymətləndirmə (FP, fayda), köhnəlmə (çıxarılma), sonra yenidən toplamaya qayıdış."
caption = "Şəkil 4. İndikatorun toplanmasından tətbiqinə və təkrar qiymətləndirilməsinə qədər iş axını."
:::

STIX (Structured Threat Information Expression) təhdid məlumatını obyektlər və münasibətlərlə təsvir edən modeldir; STIX 2.1-də müşahidə məlumatı ilə aşkarlama nümunəsi olan indikator ayrılır. TAXII (Trusted Automated Exchange of Intelligence Information) bu məlumatın mübadiləsi üçün protokoldur. STIX formatı səhv iddianı doğru etmir, TAXII ilə çatdırılma da indikatorun etibarlılığını sübut etmir.

Trafik işığı protokolu (Traffic Light Protocol, TLP) məlumatın kimlərlə paylaşıla biləcəyini bildirir. FIRST TLP 2.0-da CLEAR, GREEN, AMBER, AMBER+STRICT və RED işarələri işlənir; onlar zərərli olma ehtimalının rəngli balı deyil. İndikator alanda həm texniki tətbiq şərti, həm də paylaşma sərhədi saxlanılır; məxfi kontekstin açıq hesabatda görünməsi ayrıca səhvdir.

## Təhlükəsiz qəbul və təhlil üsulları

### Nümunəni təhlükəsiz qəbul etmək

Şübhəli fayl gündəlik iş kompüterində açılmır; poçt əlavəsinə iki dəfə klikləmək təhlil üsulu deyil. Faylın ilkin mənbəyi, qəbul vaxtı, ölçüsü və SHA-256 heşi qeyd edilir. Orijinal dəyişdirilmir, iş üçün nüsxə ayrılır. Zərərli proqram anbarına yalnız səlahiyyətli şəxslər daxil olmalıdır.

Parollu arxiv nümunənin təsadüfən açılmasını və bəzi ötürmə sistemlərində avtomatik emalını məhdudlaşdıra bilər, amma zərərsizləşdirmə və izolyasiya sərhədi deyil: parolu bilən şəxs faylı yenə çıxarıb işlədə bilər. Arxivlə yanaşı xəbərdarlıq, giriş nəzarəti və ayrıca analiz mühiti lazımdır. Laboratoriyada istifadə olunan bütün sənədlər, hesablar və şəbəkə məlumatları sintetik olmalıdır.

| Üsul | Cavab verdiyi sual | Məhdudiyyət |
| --- | --- | --- |
| Statik təhlil | Faylda hansı struktur və mümkün funksiyalar var? | Paketləmə və obfuskasiya məzmunu gizlədə bilər |
| Dinamik təhlil | Bu şərtlərdə proqram nə etdi? | Başqa şərtdə fərqli davranış ola bilər |
| Yaddaş təhlili | İcra zamanı hansı kod və obyektlər mövcuddur? | Görüntü müəyyən ana aiddir və həssas məlumat daşıyır |

### Statik təhlilin ardıcıllığı

Statik təhlil nümunəni icra etmədən aparılır. Əvvəlcə uzantı əvəzinə həqiqi format müəyyən edilir: Windows PE, Linux ELF, PDF və Office sənədinin quruluşu fərqlidir. `hesabat.pdf.exe` kimi ad son uzantının gizlədilməsi ilə istifadəçini aldada bilər; fayl başlığı və struktur yoxlaması məzmun haqqında addan daha əsaslı məlumat verir.

Sonra heş, rəqəmsal imza, mətn sətirləri (strings), idxal olunan funksiyalar və yerləşdirilmiş resurslar öyrənilir. İmza faylın imzalandıqdan sonra dəyişib-dəyişmədiyini və imzalayanı yoxlamağa kömək edir, amma etibarlı imza təhlükəsizlik zəmanəti deyil; imzasız kafedra skripti də avtomatik zərərli sayılmır. İmzanın vaxtı, sertifikat zənciri və real davranış ayrıca qiymətləndirilir.

Zərərsiz tədris faylı üzərində nümayiş (zərərli nümunə tələb olunmur; adın və məzmunun dəyişməsinin heşə təsiri həmin fayl üzərində göstərilə bilər):

```bash
printf '%s\n' 'UNEC_LAB_MARKER_A' > sample.txt
printf '%s\n' 'UNEC_LAB_MARKER_B' >> sample.txt
sha256sum sample.txt
file sample.txt
strings -a sample.txt
```

Sətirlər içərisində domen tapılması namizəd indikator yaradır, amma proqramın həmin domenə qoşulduğunu sübut etmir: sətir test məlumatı, istifadə olunmayan kod və ya standart kitabxananın hissəsi ola bilər. İdxal olunan şəbəkə funksiyası da zərərli əlaqəni özü göstərmir. Analitik sətirin kodda harada istifadə olunduğunu və dinamik müşahidə ilə uyğunluğunu yoxlayır.

Daha dərin təhlildə disassembler maşın kodunu təlimatlara ayırır, decompiler isə yüksək səviyyəli koda bənzər təsvir qurur; Ghidra və IDA tanınan alətlərdir. Çıxış ilkin mənbə kodunun tam bərpası sayılmır: analitik funksiyaların əlaqəsini, giriş məlumatından asılı budaqlanmanı və zərərli funksiyanın nə vaxt çağırıldığını əsaslandırmalıdır. Statik analiz alətləri etibarsız fayl emal etdiyindən onlar da ayrıca yenilənmiş mühitdə işlədilir.

### Dinamik təhlil və yayınma

Dinamik təhlil nümunənin nəzarətli mühitdə icrasını müşahidə edir. Qum qutusu (sandbox) bu məqsədlə ayrılmış təhlil mühitidir. İşə salmadan əvvəl baza vəziyyəti, sonra yaranan proseslər, dəyişən fayllar, reyestr və şəbəkə fəaliyyəti müqayisə olunur. Laboratoriyada xarici əlaqələr standart olaraq bağlı saxlanılır, lazım olan xidmətlər saxta daxili xidmətlərlə təqlid edilə bilər.

:::warning Sandbox qaydaları
Analiz mühiti istehsalat şəbəkəsindən ayrı olmalı, içində real məlumat və parol olmamalı, şəbəkə çıxışı nəzarətdə olmalı, ortaq qovluqlar və bufer (clipboard) bağlanmalıdır. Virtual maşın təkbaşına tam izolyasiya deyil: ortaq qovluq, mübadilə buferi, host diskinə çıxış və istehsal şəbəkəsinə körpü sərhədi poza bilər; hipervizorun öz zəifliyi də nəzərə alınır. Təmiz snapshot geri dönüşü asanlaşdırır, amma kənar sistemə çıxmış zərəri geri qaytarmır. Nümunəyə real C2-yə və başqa təşkilatlara sərbəst trafik göndərməyə icazə verilməməlidir.
:::

Yayınma (evasion) proqramın təhlil mühitini görüb davranışını dəyişməsidir. Virtual avadanlıq izləri, istifadəçi fəaliyyətinin azlığı, qısa müşahidə vaxtı və şəbəkə əlçatmazlığı yoxlanıla bilər; nümunə siçan hərəkəti, müəyyən sənəd və ya uzun gözləmə şərti tələb edə bilər ("yatmış" qala bilər). Qısa testdə sakit qalması təhlükəsizliyini sübut etmir. Eyni səbəbdən yalnız bir uğursuz C2 müraciətindən proqramın başqa funksiyası olmadığı nəticəsi çıxmır.

Şərti sınaqda proqram proses yaradır, amma fayl şifrələmir: analitik nəticəni müşahidə olunan fəaliyyətlə məhdud yazır, faylın zərərsiz olduğunu elan etmir; statik kodda şifrələmə funksiyası varsa, hansı şərtdə çağırıldığı araşdırılır.

### Yaddaş və sübutun mənası

Yaddaş təhlili işləyən prosesləri, yüklənmiş modulları, əlaqələri və yaddaşa yeridilmiş kod ehtimallarını araşdırır; Volatility tanınan çərçivədir. Uyğun əməliyyat sistemi məlumatı və dəstəklənən görüntü formatı tələb olunur. Alətin çıxardığı hər qeyri-adi sahə zərərli kod deyil: normal tətbiqlərdə də dinamik kod və qeyri-adi yaddaş icazələri ola bilər. Yaddaş təhlili faylsız hücumları tapmaq üçün vacibdir.

RAM görüntüsündə parollar, tokenlər, sənəd fraqmentləri və şəxsi məlumatlar ola bilər; ona disk görüntüsü qədər ciddi giriş nəzarəti tətbiq edilir. Kompüterin söndürülməsi uçucu sübutu itirə bilər, amma yaddaş götürmək də canlı sistemin vəziyyətini dəyişir. Cavab planında hansı mütəxəssisin, hansı alətlə və hansı şərtdə görüntü götürəcəyi müəyyən edilməlidir.

## YARA və Sigma qaydaları

### YARA qaydasını oxumaq

YARA fayl və ya yaddaş məzmununda mətn, bayt ardıcıllığı və məntiqi şərtlərə görə uyğunluq axtarır. Aşağıdakı qayda yalnız iki zərərsiz markeri tanıyır, real zərərli ailəyə aid deyil; yuxarıda yaradılan `sample.txt` bu şərti ödəyir.

```yara
rule UNEC_Tedris_Markerleri : tedris {
  meta:
    description = "Zerersiz laboratoriya markerleri"
    author = "UNEC laboratoriyasi"
    purpose = "Tedris, zererli proqram hokmu deyil"
  strings:
    $a = "UNEC_LAB_MARKER_A" ascii
    $b = "UNEC_LAB_MARKER_B" ascii
  condition:
    filesize < 1MB and all of them
}
```

`rule` açar sözü qaydanı başladır; `UNEC_Tedris_Markerleri` qaydanın identifikatorudur, `tedris` nəticələri qruplaşdırmaq üçün teqdir. `meta` təsviri və müəllifi uyğunluğun məntiqini dəyişmir; qaydanın mənşəyini və məqsədini izah edir, tədris qaydasında belə saxlanılır ki, başqa analitik onu zərərli proqram imzası ilə qarışdırmasın. `strings` bölməsində `$a` və `$b` adlandırılmış sətirlərdir; `ascii` modifikatoru onların ASCII baytları kimi axtarıldığını göstərir. `condition` uyğunluq üçün məcburi məntiqdir: `all of them` hər iki sətirin tapılmasını tələb edir, `filesize < 1MB` bu tədris qaydasında fayl ölçüsünü məhdudlaşdırır (hədd şərti seçimdir, ümumi zərərli fayl meyarı deyil).

| Element | Vəzifə | Səhv tətbiq riski |
| --- | --- | --- |
| Qayda adı və teq | Nəticəni tanıdır və qruplaşdırır | Adın özü zərərli olma hökmü yarada bilər |
| meta | Məqsəd və mənşə haqqında izah saxlayır | Təsvir şərtə daxil deyil |
| strings | Axtarılan məzmunu təsvir edir | Çox ümumi sətir yanlış uyğunluq yaradır |
| ascii və wide | Sətirin bayt təqdimatını müəyyən edir | Yalnız bir kodlaşdırma variantı qaça bilər |
| condition | Sətirləri və digər yoxlamaları birləşdirir | Həddindən artıq sərt şərt variantları qaçırır |
| filesize | Fayl ölçüsü üzrə məhdudiyyət qoyur | Ölçü dəyişəndə uyğun nümunə tutulmaya bilər |

YARA quraşdırılmış ayrıca laboratoriyada qayda `marker.yar` faylına yazıldıqdan sonra `yara marker.yar sample.txt` ilə yoxlanır. Hər iki marker olan fayl uyğun gəlməlidir, biri olmayan gəlməməlidir, böyük fayl ölçü şərtindən keçməməlidir. Bunlar məntiqin testləridir; qaydanın real zərərli proqramı tapdığını göstərmir. Qaydaya uyğunluq faylın zərərli olduğunu yox, yalnız şərtin ödəndiyini göstərir.

Real qayda bir təsadüfi domen sətirindən qurulmamalıdır. Paket açıldıqdan sonra sabit qalan kod və konfiqurasiya xüsusiyyətləri seçilə bilər, lakin qanuni proqram dəsti üzərində yanlış uyğunluqlar da ölçülür. Sınaq nümunələri ilə yoxlama nümunələrinin tam eyni olması qaydanın yalnız əzbərlədiyi faylları tutmasına səbəb ola bilər. Uyğunluq hesabatında qayda versiyası, fayl heşi və tapılan xüsusiyyət saxlanılır.

### Sigma ilə hadisə aşkarlaması

Sigma jurnal məlumatları üçün paylaşılabilən aşkarlama qaydası təsviridir. YARA məzmunu yoxlayır, Sigma hadisə sahələri və şərtləri üzərində işləyir. Sigma qaydası bütün SIEM-lərdə eyni nəticə vermir: arxa sistemə çevirmə, sahə xəritəsi, məlumat mənbəyi və qaydanın semantikası uyğunlaşdırılmalıdır.

Qayda Windows proses hadisəsində Word-dən PowerShell başlanmasını axtarır; tədris üçündür, sınaq statusundadır, tarix və identifikator şərtidir. YAML siyahısındakı iki `Image` dəyəri alternativdir, valideyn şərti isə həmin seçimlə birlikdə ödənməlidir.

```yaml
title: Word Starts PowerShell - Teaching Example
id: 7a35e4b2-9a11-4b4d-8df2-a561d0c86e12
status: test
description: Teaching rule requiring local validation
author: UNEC laboratory
date: 2026-11-08
logsource:
  category: process_creation
  product: windows
detection:
  selection:
    ParentImage|endswith: '\WINWORD.EXE'
    Image|endswith:
      - '\powershell.exe'
      - '\pwsh.exe'
  condition: selection
falsepositives:
  - Approved document automation
level: medium
```

`logsource` tələb olunan mənbəni təsvir edir; uyğun proses telemetriyası yoxdursa qayda nəticə verə bilməz. `selection` sahə şərtlərini toplayır. `endswith` fayl yolunun son hissəsini müqayisə edən modifikatordur. `condition` seçimin necə istifadə olunduğunu bildirir. `falsepositives` mümkün qanuni səbəbləri sənədləşdirir, avtomatik istisna yaratmır. `level` ilkin ciddilik işarəsidir, hadisənin sübut edilmiş insident olması deyil.

Bu qayda yalnız birbaşa valideyni Word olan PowerShell prosesini tutur; araya `cmd.exe` girirsə, uyğunluq olmaya bilər, hücumçu başqa skript mühiti də işlədə bilər. Ona görə qayda proses ağacının daha geniş əlaqələri və ardıcıl hadisələrlə tamamlanır. İstisna lazım olanda bütöv kafedra hesabını kənarlaşdırmaq əvəzinə təsdiqli tətbiq, yol və iş şərti üzrə dar seçim qurulur.

## İndikatorların təhlükəsizlik vasitələrində tətbiqi

### Alətlərin vəzifələrini ayırmaq

Antivirus faylları və fəaliyyəti imza, evristika və davranış üsulları ilə qiymətləndirə bilər. Son nöqtələrdə aşkarlama və cavab sistemi (Endpoint Detection and Response, EDR) proses, fayl və hesab telemetriyasını araşdırmağa, məhsulun imkanına görə cihazı təcrid etməyə kömək edir. Heş üzrə qadağa konkret faylı məhdudlaşdıra bilər, amma oğurlanmış sessiyanı avtomatik ləğv etmir; cavab həm cihaz, həm kimlik səviyyəsində planlaşdırılır.

Şəbəkə müdaxiləsini aşkarlayan sistem (Intrusion Detection System, IDS) xəbərdarlıq yaradır. Qarşısını alan sistem (Intrusion Prevention System, IPS) uyğun yerləşmə və qayda olduqda trafiki dayandıra bilər. Firewall ünvan və digər dəstəklənən xüsusiyyətlər üzrə əlaqəni məhdudlaşdırır, proksi veb sorğusu haqqında kontekst verir. Şifrələnmiş trafikin məzmunu sensor üçün açıq olmaya bilər; şəbəkə və son nöqtə müşahidələri birləşdirilir.

Təhlükəsizlik məlumatlarının və hadisələrinin idarə edilməsi sistemi (Security Information and Event Management, SIEM) müxtəlif mənbələri birləşdirir. SOAR (Security Orchestration, Automation and Response) alətlərarası təkrarlanan cavab işlərini əlaqələndirir və avtomatlaşdırır: indikatorun normallaşdırılması və araşdırma kartının açılması avtomatlaşdırıla bilər. Kritik tələbə bazasına girişin kəsilməsi üçün isə əvvəlcədən təsdiqlənmiş səlahiyyət, əhatə və geri dönüş qaydası olmalıdır.

| Vasitə | Uyğun tətbiq | Kor nöqtə və ya risk |
| --- | --- | --- |
| Antivirus | Məlum nümunənin yoxlanması və karantin | Ailənin başqa variantı və hesab oğurluğu qala bilər |
| EDR | Proses əlaqəsi və cihaz təcridi | Agent olmayan və ya telemetriyası itmiş cihaz görünməyə bilər |
| DNS nəzarəti | Zərərli domenə sorğunun məhdudlaşdırılması | Alternativ resolver və birbaşa IP əlaqəsi qala bilər |
| Proksi və firewall | Uyğun URL, domen və əlaqə qaydası | Paylaşılan ünvanın bloklanması qanuni xidməti poza bilər |
| IDS və IPS | Şəbəkə nümunəsinə uyğunluq | Şifrələmə və sensorun yeri görünüşü məhdudlaşdırır |
| SIEM | Mənbələrarası axtarış və korrelyasiya | Yanlış sahə xəritəsi və saat fərqi əlaqəni korlayır |
| SOAR | Yoxlama, kart açma və səlahiyyətli cavab axını | Yanlış nəticə çox sistemə sürətlə yayıla bilər |

### Sysmon və hadisə əlaqələri

Microsoft Sysmon Windows-da əlavə telemetriya yaradır; konfiqurasiya hansı hadisələrin yazılacağını müəyyən edir. Şəbəkə bağlantısı hadisəsi standart olaraq aktiv deyil, qayda yazmazdan əvvəl real məlumat axını yoxlanmalıdır. Sysmon jurnalının gəlməsi antivirus kimi zərərli hökm vermək demək deyil, analitik üçün daha zəngin müşahidədir.

| Event ID | Məzmun | Araşdırmada istifadə |
| --- | --- | --- |
| 1 | Proses yaradılması | Valideyn, əmr sətri və proses identifikatorları əlaqələndirilir |
| 3 | Şəbəkə bağlantısı | Prosesin hansı ünvana qoşulduğu araşdırılır |
| 11 | Fayl yaradılması və ya üzərinə yazılması | Yükün yazıldığı yer və proses tapılır |
| 13 | Reyestr dəyərinin dəyişməsi | Avtomatik başlama və başqa konfiqurasiya dəyişiklikləri yoxlanır |
| 22 | DNS sorğusu | Sorğu adı proses və cihazla əlaqələndirilir |

Aşağıdakı qeydlər Sysmon ixracının tam formatı deyil, seçilmiş sahələrin sadələşdirilmiş təqdimatıdır; vaxtlar, identifikator, cihaz və ünvanlar şərtidir. `ProcessGuid` eyni prosesin hadisələrini əlaqələndirir; yalnız PID istifadə etmək onun sonradan başqa prosesə verilməsi səbəbindən səhv yarada bilər.

```text
Time=2026-11-08T06:10:00Z Host=dekanliq-01 EventID=1 Image=C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe ParentImage=C:\Program Files\Office\WINWORD.EXE ProcessGuid={G1}
Time=2026-11-08T06:10:04Z Host=dekanliq-01 EventID=22 QueryName=sync-campus.example ProcessGuid={G1}
Time=2026-11-08T06:10:06Z Host=dekanliq-01 EventID=3 DestinationIp=203.0.113.44 DestinationPort=443 ProcessGuid={G1}
```

Korrelyasiya eyni cihazda və eyni proseslə bağlı sənəd, skript, DNS və bağlantı hadisələrini birləşdirir. Hadisənin baş vermə vaxtı ilə SIEM-ə çatma vaxtı ayrıca saxlanılır; gecikmə düzgün ardıcıllığı itirə bilər. DNS sorğusu bağlantının uğurlu olduğunu, bağlantı isə məlumatın oğurlandığını təkbaşına sübut etmir; ixrac qeydi, fayla giriş və ötürmənin məzmununa dair əlavə sübut axtarılır.

### Keyfiyyəti ölçmək

Uyğunluq həqiqi zərərli fəaliyyəti göstərirsə həqiqi müsbət (true positive, TP), qanuni fəaliyyəti səhv tutursa yanlış müsbət (false positive, FP) sayılır. Buraxılmış hücum yanlış mənfidir (false negative, FN). Şərti sınaqda qayda 40 xəbərdarlıq yaradır, onların 10-u zərərli hadisədir: dəqiqlik 10 / 40 = 25%. Bu rəqəm qaydanın bütün hücumların hansı hissəsini tapdığını göstərmir.

Tamlıq (recall) TP / (TP + FN) ilə hesablanır. FN real həyatda tam bilinməyə bilər; idarə olunan zərərsiz sınaqlar örtüyü yoxlamağa kömək edir. Qaydanın neçə uyğunluq verdiyi ilə yanaşı analitikin neçə uyğunluğu araşdırdığı və cavabın nə qədər gecikdiyi də izlənir. Sensorun susması ayrıca xəbərdarlıq yaratmalıdır: sıfır nəticə həm sakit mühit, həm işləməyən toplama mənasına gələ bilər.

## Zərərli proqram insidentinə cavab və bərpa

### Hazırlıq və ilkin qərar

NIST SP 800-61 Rev. 3 aprel 2025-ci ildə dərc olunub və insidentə cavabı NIST CSF 2.0 ilə əlaqələndirir. CSF 2.0-ın altı funksiyası: Govern, Identify, Protect, Detect, Respond və Recover. Hazırlıq yalnız proqram almaqla bitmir: məsul şəxslər, aktiv inventarı, ehtiyat nüsxələr, jurnal toplama, əlaqə kanalı və qərar səlahiyyətləri əvvəlcədən müəyyən edilir. Köhnə mərhələ adları praktik planlarda qala bilər, amma cavab ümumi risk idarəetməsindən ayrılmır.

İlkin qiymətləndirmədə xəbərdarlığın mənbəyi və təsiri yoxlanır. Fayl yalnız karantindədir, yoxsa işləyib? Cihaz laboratoriya kompüteridir, yoxsa domen idarəetmə serveridir? Məlumat şifrələnməsi davam edirmi? Tələbə bazasına çıxışı olan hesab təsirlənibmi? Cavabın sürəti ilə yanaşı yanlış tədbirin tədrisi dayandırma riski də nəzərə alınır. Aktiv dağıdıcı fəaliyyət varsa, araşdırmanın tamamlanmasını gözləmədən yayılmanı məhdudlaşdırmaq lazım gələ bilər.

### Əhatə, təcrid və sübut

Əhatə yalnız bir cihazın adı deyil: eyni faylı alan və açan hesablar, əlaqəli domenlər, ikinci yüklər, tapşırıqlar, girişlər və məlumat resursları axtarılır. IoC-lərlə keçmiş qeydlərə baxılır, davranışla dəyişmiş variantlar axtarılır. Mənfi nəticə yalnız görünən və saxlanılmış məlumatın sərhədində etibarlıdır; agent olmayan laboratoriya cihazını yoxlamadan təmiz elan etmək olmaz.

Təcrid üçün EDR əlaqəni məhdudlaşdıra və idarəetmə kanalını saxlaya bilər; məhsulun davranışı əvvəlcədən bilinməlidir. Alternativ kommutator və firewall səviyyəsində məhdudiyyətdir. Yoluxmuş kompüteri standart qayda kimi dərhal söndürmək uçucu sübutu itirə bilər. Bununla belə, aktiv dağıntını başqa yolla dayandırmaq mümkün deyilsə, təhlükəsizliyi qoruyan təcili qərar lazım ola bilər. Təcrid və söndürmə bir-birinin sinonimi deyil.

Sübutun ötürülmə zənciri (chain of custody) materialı kimin, nə vaxt, hansı üsulla götürdüyünü, kimə verdiyini və harada saxladığını qeyd edir. Disk və yaddaş görüntüsü, jurnal ixracı, poçt başlıqları və şəbəkə yazıları uyğun hallarda qorunur. SHA-256 sonrakı dəyişiklikləri yoxlamağa kömək edir, amma yanlış cihazdan götürülmüş materialı doğru sübuta çevirmir. Saat qurşağı, alət versiyası və götürmə zamanı yaranan dəyişikliklər də yazılır.

| İş | Əsas əməl | Gözlənilən nəticə |
| --- | --- | --- |
| İlkin qiymətləndirmə | İcra, təsir və davam edən fəaliyyəti yoxlamaq | Prioritet və cavab sahibi müəyyən olunur |
| Əhatə | Cihaz, hesab, yük və məlumat əlaqələrini axtarmaq | Təsirlənən və hələ yoxlanılmayan sahələr ayrılır |
| Məhdudlaşdırma | Şəbəkə, hesab və kanal üzrə təcrid | Yayılma və çıxarılma imkanları azalır |
| Sübutun qorunması | Görüntü və qeydləri sənədləşdirmək | Təkrar yoxlanılan material qalır |
| Aradan qaldırma | Kök səbəbi və bütün qalıqları təmizləmək | Etibarlı sistem vəziyyəti qurulur |
| Bərpa | Nüsxə, hesab və tətbiqi yoxlamaq | Xidmət nəzarətli qaydada geri açılır |
| Sonrakı təhlil | Boşluqları məsul şəxs və müddətə bağlamaq | Təkrar yoluxma ehtimalı azaldılır |

### Aradan qaldırma və hesabların bərpası

Aradan qaldırma tapılmış faylı silməkdən genişdir: girişə səbəb olan zəiflik bağlanır, davamlılıq mexanizmləri, ikinci yüklər və icazəsiz hesablar tapılır. Administrator səlahiyyəti ilə dərin müdaxilə və ya rootkit ehtimalında sistem bütövlüyünü sübut etmək çətin ola bilər; onda yoxlanmış quraşdırma mənbəyindən yenidən qurmaq daha əsaslı qərardır. Firmware müdaxiləsi şübhəsində adi əməliyyat sistemi qurulumu yetməyə bilər.

Parollar təmiz cihazdan dəyişdirilir. Sessiyalar və yeniləmə tokenləri xidmətin imkanlarına uyğun ləğv edilir; tətbiq icazələri, poçt yönləndirmələri, SSH açarları və xidmət sirləri yoxlanır. İnfostealer ehtimalında yalnız universitet poçtu yox, həmin cihazda işlədilmiş digər səlahiyyətli hesablar da əhatəyə daxil edilir. Yeni parolu hələ yoluxmuş cihazda yazmaq onun təkrar oğurlanmasına yol aça bilər.

### Xidməti geri açmaq

Bərpa nüsxəsi yoluxmadan əvvəlki etibarlı vəziyyətə aid olmalıdır. Tarixcə köhnə olması kifayət deyil: hücumçu əvvəldən sistemdə ola bilər. Nüsxə ayrıca mühitdə yoxlanır, zəiflik aradan qaldırılır və yalnız sonra xidmət geri açılır. Tələbə bazasında əlaqəli cədvəllərin uyğunluğu, LMS-də giriş və materialların açılması, kitabxanada lisenziyalı resurslara çıxış tətbiq səviyyəsində yoxlanılır.

Müşahidə müddətində əvvəlki indikatorlar və əlaqəli davranışlar axtarılır. Bərpa edilmiş serverin eyni C2-yə çıxış cəhdi yenidən açılmış giriş yolu və ya çirkli nüsxə ehtimalı yaradır. Məlumat sızması və bildiriş qərarları texniki sübut, daxili qayda və tətbiq edilən tələblər əsasında aidiyyəti bölmələrlə verilir. Araşdırılmamış məsələ hesabatda açıq qalır; bilmədiyimiz faktı olmadı kimi yazmaq olmaz.

Konspektdəki qısa ardıcıllıq: əhatəni müəyyən et (IoC-ləri bütün şəbəkədə axtar); təcrid et (EDR ilə, söndürmə); sübutu qoru; kök səbəbi və bütün komponentləri sil (bütövlüyə əmin deyilsənsə, sıfırdan qur); hesabları təmiz cihazdan bərpa et; yoxlanmış nüsxədən bərpa et, təkrar yoluxmanı izlə və dərsləri çıxar.

## Real hadisələrin texniki dərsləri

### WannaCry

WannaCry 2017-ci ilin mayında geniş yayılmış şifrələyici hücum idi. Windows-un SMB xidmətindəki zəiflikdən istifadə edən yayılma komponenti onun qurd xüsusiyyətini göstərirdi. Microsoft-un MS17-010 yenilənmələri uyğun zəiflikləri həmin ilin martında aradan qaldırmışdı. Buna görə onu yalnız istifadəçinin açdığı fişinq faylı ilə izah etmək yayılma mexanizmini itirir: qurd və şifrələyici təsnifatları eyni nümunədə kəsişir.

Universitet üçün dərs yamağın mövcudluğu ilə bütün aktivlərə tətbiqinin ayrı olmasıdır. Şərti laboratoriyada unudulmuş cihaz yamaqlanmırsa, digər sistemlərə çıxışı yayılma yoluna çevrilə bilər. Aktiv inventarı, SMB girişinin daraldılması, uyğun köhnə protokol imkanlarının söndürülməsi və bərpa nüsxəsi bir-birini tamamlayır. Tarixi hadisənin fayl heşini bloklamaq bu nəzarətlərin yerini vermir.

### NotPetya

NotPetya 2017-ci ilin iyununda dağıdıcı nəticələr yaratmışdı. İlkin yayılma Ukraynada istifadə edilən M.E.Doc proqramının kompromitasiya edilmiş yenilənmə mexanizmi ilə əlaqələndirilmişdi. Daxili yayılmada zəifliklərdən və oğurlanmış kimlik məlumatlarından istifadə edilirdi. Fidyə görünüşünə baxmayaraq, onu etibarlı geri açma yolu olan adi şifrələyici saymaq düzgün deyil; hadisə dağıdıcı proqram (wiper) nümunəsi kimi öyrənilir.

Universitet ssenarisində dərs təchizatçıya etibarın bütün yenilənmələrə nəzarətsiz imtiyaz verməməsidir. Şərti mühasibat proqramının yenilənməsi yoluxubsa, həmin tətbiqin hesabı tələbə bazasına və ehtiyat nüsxə idarəetməsinə avtomatik çıxış almamalıdır. Yamaq zəifliklə yayılan yolu bağlaya bilər, oğurlanmış etibarlı hesabla hərəkəti isə ayrıca məhdudlaşdırmaq lazımdır.

### Emotet

Emotet əvvəl bank məlumatlarını oğurlayan troyan kimi tanınıb, sonrakı fəaliyyətində başqa zərərli yüklərin çatdırılmasına xidmət edən modul infrastruktura çevrilib. Zərərli elektron poçt kampaniyaları ilə əlaqəsi çatdırılma tərəfini, əlavə komponentlərin yüklənməsi çoxmərhələli hücum məntiqini göstərir. Emotet-i hər vəziyyətdə son şifrələyici yükün adı kimi işlətmək düzgün deyil.

Poçtda şərti Emotet xəbərdarlığı görünəndə yalnız məktubu silmək yetməyə bilər: kimlərin əlavəni açdığı, hansı proseslərin başladığı, başqa yükün endirilib-endirilmədiyi və hesabların oğurlanması araşdırılır. Fərqli illərdəki kampaniyaların bütün detallarını eyni saymaq olmaz. Bu hadisələrdə istifadə olunan tarixi indikator cari mühitdə tətbiq edilməzdən əvvəl yenidən yoxlanır.

:::note Köhnə slaydlarla fərq
Konspektə görə mühazirədə ciddi səhv tapılmayıb. Bir ifadə dəqiqləşdirilməlidir: "DNS qeydləri cihazın hansı domenlərə müraciət etdiyini göstərir" əvəzinə **DNS sorğu logları** demək lazımdır. DNS qeydlərinin (A, MX və s.) özü hansı cihazın sorğu göndərdiyini göstərmir.
:::

## Təkrar

:::reveal Dinamik təhlildə 3 dəqiqə sakitlik niyə "fayl təmizdir" demək deyil?
Zərərli proqram virtual mühiti tanıyıb gözləyə, istifadəçi hərəkəti (siçan) gözləyə bilər. Nəticə yalnız müşahidə olunan mühit və müddətlə məhdud yazılır; statik təhlil, heşin təhdid kəşfiyyatında yoxlanması, fərqli sandbox və lazım gəlsə yaddaş analizi ilə tamamlanır.
:::
