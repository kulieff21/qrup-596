+++
title = "Son qurğuların təhlükəsizliyi və sistemlərin mühafizəsinin gücləndirilməsi"
unit = "suallar"
order = 11
summary = "Mühazirənin bütün nəzarət sualları, situasiya tapşırıqları, konspektdən situasiyalar və ehtimal olunan əlavə suallar imtahan üslubunda cavablarla."
updated = 2026-11-09

[[source]]
title = "Mühazirə 11: Son qurğuların təhlükəsizliyi və sistemlərin mühafizəsinin gücləndirilməsi"
note = "Elmar Cabbarov, 2026–2027"

[[source]]
title = "Midterm konspekti, Mövzu 11"
note = "Elmar Cabbarov"
+++

İmtahan yazılı açıq suallardan ibarətdir. Əvvəl cavabı özün yaz, sonra aşağıdakı nümunə ilə tutuşdur. Situasiya cavabında ardıcıllıq: **aktiv, pozulan xassə, səbəb, tədbir, yoxlama**.

## Nəzarət sualları

:::reveal Son qurğunun tərifi niyə antivirus quraşdırılan cihazlarla məhdudlaşmır?
- Son qurğu məlumatı qəbul edən, emal edən və ya saxlayan cihazdır: iş stansiyası, noutbuk, smartfon, planşet, server, printer, kamera, ağıllı lövhə, ölçü cihazı.
- Bunların çoxuna masaüstü antivirus qurmaq mümkün deyil, amma onlar şəbəkənin son nöqtəsidir.
- Tərif ilə konkret məhsulun dəstəklədiyi cihaz siyahısı fərqli məsələlərdir.
- Müdafiə cihazı, məlumatı və giriş imkanlarını (sessiya, token) əhatə edir.
:::

:::reveal Hücum səthini proqram, hesab, interfeys və fiziki giriş üzrə necə müəyyən etmək olar?
- Hücum səthi müdaxilə üçün istifadə oluna bilən proqram, xidmət, interfeys və giriş imkanlarının cəmidir.
- Proqram: quraşdırılmış proqramlar, makrolar, brauzer əlavələri; xidmət və şəbəkə: açıq portlar, işləyən xidmətlər, uzaqdan yardım agenti.
- Hesab: lokal administrator və admin hesabları; interfeys: USB.
- Fiziki giriş: cihaza birbaşa çatma; İnternetdən əlçatmaz cihazın səthi də sıfır deyil.
- Hardening ilə lazımsız imkanlar azaldılır və təsir sistemdə yoxlanır.
:::

:::reveal Fişinq, oğurlanmış sessiya və proqram zəifliyi hansı fərqli giriş yollarını yaradır?
- **Fişinq:** istifadəçini aldadır (məsələn, makro aktivləşdirən sənəd); proqram istifadəçinin hüquqları ilə işləyir.
- **Oğurlanmış hesab/sessiya:** zərərli fayl olmaya bilər; parol, kuki və ya token istifadə olunur. MFA kömək edir, sessiya oğurluğunu tam həll etmir.
- **Proqram zəifliyi:** yenilənməmiş komponent (məsələn, LMS) istismar olunur; tədbir prioritetli yamaq və giriş məhdudiyyətidir.
- Müşahidə: sənəddən proses başlaması, giriş/ixrac qeydləri, versiya və istismar əlaməti.
:::

:::reveal EPP, EDR, XDR və MDR funksiyası və məsuliyyəti baxımından necə fərqlənir?
- **EPP:** zərərli icranı önləyir (imza, evristika, davranış); məhdudiyyət: bütün hücumları tanımır.
- **EDR:** proses, fayl, reyestr, şəbəkə telemetriyası, araşdırma, karantin, təcrid; analitik və sazlama tələb edir.
- **XDR:** qurğu, poçt, kimlik, şəbəkə və bulud siqnallarını əlaqələndirir; inteqrasiya əhatəsi məhsuldan asılıdır.
- **MDR:** xidmət modeli; xarici komanda izləyir və cavab verir; səlahiyyət və cavab vaxtı müqavilədə yazılır.
:::

:::reveal Baza konfiqurasiyası hazırlananda CIS Benchmarks və STIG necə istifadə edilməlidir?
- Baza konfiqurasiyası cihaz qrupu (noutbuk, terminal, server) üçün təsdiqlənmiş minimum sazlamadır.
- CIS Benchmarks məhsul və buraxılış üçün təhlükəsiz sazlama tövsiyəsidir; sərt profil iş proqramlarına təsir edə bilər.
- STIG (DISA) texniki tələb və yoxlama qaydalarını verir; ABŞ müdafiə mühiti üçündür, universitetdə avtomatik hüquqi tələb deyil.
- Hər ikisi yoxlanmış başlanğıc nöqtəsidir, tətbiq tələblərini əvəz etmir; sınaqdan, fərqin ölçülməsindən və istisnaların qeydindən sonra tətbiq olunur.
:::

:::reveal Konfiqurasiyanın bazadan yayınması nədir və müddətli istisna hansı sahələri daşımalıdır?
- Configuration drift: konfiqurasiyanın zamanla bazadan uzaqlaşması (genişlənmiş firewall qaydası, quraşdırıcının açdığı xidmət, brauzer əlavəsi).
- Group Policy, MDM və Ansible fərqi tapıb siyasəti yaymağa kömək edir; avtomatik bərpadan əvvəl qanuni dəyişiklik araşdırılır.
- İstisna: cihazlar, konkret tələb, risk, kompensasiyaedici tədbir, məsul şəxs, bitmə tarixi.
- Müddət bitəndə istisna bağlanır və ya yenidən qiymətləndirilir; bütün fakültə üçün nəzarət söndürülmür.
:::

:::reveal Minimum səlahiyyət hücumun hansı təsirlərini azaldır, hansını dayandırmır?
- Azaldır: səlahiyyət artırma, sistem fayllarının və xidmətlərin dəyişdirilməsi, yan keçid, ziyanın miqyası.
- Dayandırmır: adi hesabın oxuya bildiyi sənədlərin oğurlanmasını, sessiya və token oğurluğunu.
- Gündəlik və inzibati hesab ayrılır, imtiyaz müddətli verilir (just-in-time), iş bitəndə geri alınır; UAC ayrıca hesabı əvəz etmir.
:::

:::reveal LAPS ortaq lokal administrator parolu problemini necə azaldır və hansı sərhədləri var?
- LAPS idarə olunan Windows cihazlarında unikal lokal admin parolu yaradır, dövri dəyişir, Active Directory və ya Entra ID-də saxlayır.
- Bir cihazdan alınan parol başqalarına keçid vermir.
- Sərhəd: domen admin parolunu idarə etmir, lokal admin hesabını zərərsiz etmir; oxuma hüququ olan hesab ələ keçsə, çox cihaz risk altındadır.
- Saxlama yeri, oxucu qruplar, audit və istifadədən sonra dəyişmə qorunmalıdır.
:::

:::reveal Yamaq idarəsinin beş mərhələsi hansıdır? Son mərhələ niyə ayrıca sübut tələb edir?
- Aşkarla, prioritet ver, sına (pilot qrup), mərhələli quraşdır, yoxla.
- Yamağın göndərilməsi onun quraşdırıldığını sübut etmir.
- Son mərhələdə versiya, faktiki quraşdırma, yenidən başlatma və xidmətin işləməsi təsdiqlənir; uğursuz cihazlar ayrıca işlənir.
:::

:::reveal CVSS, KEV, əlçatanlıq və sistemin kritikliyi birlikdə necə qiymətləndirilir?
- CVSS texniki ağırlıqdır, təşkilat riskini göstərmir.
- KEV (CISA) real istismarı məlum zəiflikləri verir; kataloqda olmamaq istismarsızlıq deyil. EPSS gələcək ehtimaldır, faktiki istismar sübutu deyil.
- İnternetə açıqlıq, işlək istismar vasitəsi, istifadəçi müdaxiləsi tələbi və sistemin funksiyası qərara daxildir.
- Nümunə: İnternetə açıq VPN şlüzündə aktiv istismar olunan CVSS 7,5 zəiflik daxili cihazdakı CVSS 9,8-dən əvvəl yamanır.
:::

:::reveal Windows 10 üçün ümumi dəstək və ESU fərqi universitetin qərarına necə təsir edir?
- Ümumi dəstək 14 oktyabr 2025-də bitib; ESU uyğun cihazlar üçün 14 oktyabr 2028-ə qədər təhlükəsizlik yenilənməsi verə bilər.
- Bu bütün buraxılışlara və avtomatik şəkildə şamil olunmur.
- Universitet hər cihazın buraxılışını, lisenziya uyğunluğunu və faktiki yenilənməsini uçota almalıdır.
- Dəstəksiz sistemdə antivirus yamağı əvəz etmir: ayrıca zona, məhdud çıxış, müddətli istisna, əvəzləmə planı.
:::

:::reveal Secure Boot, measured boot və TPM arasında hansı fərq var?
- **Secure Boot** imza siyasəti tətbiq edir: yalnız imzalı yükləyici və nüvə işləyir.
- **Measured boot** komponentlərin ölçmələrini PCR registrlərinə yazır; bloklamır, vəziyyət barədə sübut verir.
- **TPM** açar əməliyyatları və ölçmələr üçün aparat modulu (ayrı çip, inteqrə və ya firmware).
- Disk açarı PCR vəziyyətinə bağlıdırsa, yükləmə dəyişəndə açar verilmir və bərpa açarı lazımdır.
:::

:::reveal BitLocker və LUKS işləyən sessiyadakı məlumat oğurluğunu niyə tam dayandırmır?
- Şifrələmə söndürülmüş cihaz və ya başqa kompüterə qoşulmuş disk üçündür.
- Şifrəli həcm açılıbsa, icazəli istifadəçi və onun hüquqları ilə işləyən zərərli proqram məlumatı oxuya bilər.
- İşləyən və ya yuxu rejimindəki cihazda açarlar yaddaşda qalır; ekran kilidi bunu təmin etmir.
- Şifrələmə fayl icazəsini və sessiya mühafizəsini əvəz etmir.
:::

:::reveal Tətbiq nəzarətində heş, imza və yol qaydalarının üstünlük və məhdudiyyətləri nədir?
- **İmza:** yenilənməyə uyğunlaşır; etibarlı imzalı proqram da sui-istifadə oluna bilər.
- **Heş:** konkret faylı dəqiq tanıyır; hər dəyişiklik heşi dəyişir (sabit dərs aləti üçün).
- **Yol:** idarəsi sadədir; istifadəçi həmin yola yaza bilərsə zəifdir.
- Skript qaydası interpretatorun özünü tam məhdudlaşdırmır. Əvvəl audit rejimi, sonra bloklama; EDR ilə tamamlanır.
:::

:::reveal Qurğu firewall-u kampus sərhədindəki firewall-u necə tamamlayır?
- Sərhəd firewall-u eyni VLAN daxilindəki cihazlararası trafiki görməyə bilər.
- Qurğu firewall-u cihazın gələn və çıxan bağlantılarını proqram, mənbə şəbəkə, port və profilə görə süzür.
- Yoluxmuş qonşu kompüterdən girişə əlavə maneədir; ev və universitet şəbəkəsinə eyni geniş istisna verilmir.
:::

:::reveal Linux-da SSH sazlaması dəyişdirilərkən girişin itirilməməsi necə yoxlanır?
- Açar əsaslı giriş hazırlanır; yeni açarla giriş yoxlanmamış parol girişi bağlanmır.
- Mövcud sessiya açıq saxlanır, konsol çıxışı hazırlanır.
- `sshd -t` sintaksisi, `sshd -T` effektiv sazlamanı göstərir; Include və Match blokları nəzərə alınır.
- Dəyişiklikdən sonra ayrıca yeni sessiyada giriş sınanır; sintaksis düzgünlüyü girişin işlədiyini sübut etmir.
:::

:::reveal BYOD mühitində seçici silmə ilə tam silmə hansı məsuliyyət fərqini yaradır?
- Seçici silmə yalnız universitet məlumatını silir (iş profili, MAM); şəxsi şəkillərə toxunmur.
- Tam silmə şəxsi məlumatı da itirə bilər; cihaz şəxsin mülkiyyətidir.
- Texniki imkan təşkilati səlahiyyət demək deyil: qeydiyyat modeli və səlahiyyət sərhədi əvvəlcədən açıqlanır.
- Uzaqdan silmə cihaz oflayn olanda icra olunmaya bilər; əmrin yaranması silinmə demək deyil.
:::

:::reveal Audit hadisəsi, xəbərdarlıq və insident necə ayrılır? Susan sensor necə izlənir?
- Jurnal qeydi (hadisə) baş vermiş əməliyyatın təsviridir, adi də ola bilər.
- Xəbərdarlıq aşkarlama qaydasının araşdırılmalı saydığı nəticədir.
- İnsident təhlükəsizliyi pozan və ya real təhdid edən vəziyyətdir (planlı admin hesabı hadisədir, icazəsiz yaradılıb ixrac üçün işlədilsə insidentdir).
- Susan agent və uzun görünməyən noutbuk ayrıca xəbərdarlıq yaradır; sensorun son əlaqə vaxtı izlənir; sakit konsol təhlükəsizlik demək deyil.
:::

:::reveal Təkrarlayıcı, SFP+, PoE injektor, PDU və patch panelin dəqiq funksiyası nədir?
- Təkrarlayıcı siqnalı bərpa edir (aktiv).
- SFP+ 10 Gigabit Ethernet üçün dəyişdirilə bilən ötürücü moduldur (SFP Gigabit üçün).
- PoE injektor məlumat kabelinə elektrik enerjisi əlavə edir (IEEE 802.3af/at/bt).
- PDU elektrik enerjisini paylayır, trafik yox; idarə olunan PDU-nun interfeysi qorunmalıdır.
- Patch panel (passiv) xətləri təşkil edir.
:::

:::reveal Optik kabelin fiziki xüsusiyyətləri niyə şifrələməyə ehtiyacı aradan qaldırmır?
- Optik siqnal elektromaqnit müdaxilədən təsirlənmir, amma bu məxfilik zəmanəti deyil.
- Lifi bölücü və ya fiziki müdaxilə ilə dinləmək mümkündür.
- Optik kanal itkisizdir demək də yanlışdır (itki və optik büdcə var).
- Binalar arasında tələbə məlumatı ötürülürsə, uyğun şifrələmə tətbiq olunur.
:::

:::reveal Agent qəbul etməyən ölçü cihazı üçün kompensasiyaedici tədbirlər necə seçilir?
- Nəzarət şəbəkə sərhədinə, hesab idarəsinə və firmware uçotuna keçir.
- Ayrıca VLAN və zona, çıxışın daraldılması, təsdiqlənmiş vasitəçi kompüter, fərqli parol, kommutator səviyyəsində müşahidə.
- Müddətli istisna və əvəzləmə planı; zəiflik cihazda qala bilər.
- Aktiv skandan əvvəl istehsalçı və laboratoriya məsulu ilə razılaşılır; ölçmə nəticəsinin bütövlüyü yoxlanır.
:::

:::reveal Bərpa sınağının uğuru RPO, RTO və istifadəçi əməliyyatı ilə necə ölçülür?
- RPO qəbul edilən məlumat itkisi intervalı, RTO xidmətin bərpası üçün hədəf vaxtdır (şərti LMS: dörd saat və altı saat).
- Nüsxələmə tezliyi və real sınaq bu hədəflərə uyğun olmalıdır.
- Sınaq ayrıca mühitdə istifadəçi işini tamamlamalıdır: daxil ol, material aç, tapşırıq göndər; faylın arxivdən çıxması kifayət deyil.
- Ehtiyat nüsxə əsas sistemlə eyni hesabla silinə bilməməlidir.
:::

## Situasiya tapşırıqları

**Situasiya 1.** Şərti universitet laboratoriyasında 40 kompüterin hamısında tələbə hesabı lokal administratordur. Dərs alətlərinin quraşdırılması əsas gətirilir. EDR bir neçə cihazda icazəsiz hesablama proqramı tapıb. Dərsi dayandırmadan hansı ardıcıllıq seçilməlidir?

:::reveal Cavab
- **Aktiv və pozulma:** laboratoriya kompüterləri; tamlıq və əlçatanlıq (icazəsiz hesablama proqramı).
- **Səbəb:** tələbə hesabları lokal administratordur, quraşdırma və icra ehtiyacı ayrılmayıb.
- **Tədbir:** yoluxmuş cihazlar təcrid edilir, əlaqəli hesablar və yayılma əhatəsi araşdırılır; quraşdırma gündəlik icradan ayrılır, təsdiqlənmiş paketlər mərkəzdən yayılır; tələbələr adi hesaba keçirilir, lazım olan inzibati iş müddətli icazə ilə; tətbiq nəzarəti əvvəl audit rejimində, proqram yazan dərslər üçün ayrıca mühit; inzibati sistemlərə yol kəsilir; tələbə işləri silinmədən qorunan yerə köçürülür.
- **Yoxlama:** təmiz obrazdan qurulan cihazlarda sensor və xəbərdarlıq axını yoxlanır.
:::

**Situasiya 2.** Kafedra rəhbərinin şifrəli noutbuku nəqliyyatda itir. Son məlum vəziyyət yuxu rejimidir. İdarəetmə panelində BitLocker aktiv görünür. Hadisəni məlumat itkisi riski olmadan bağlamaq olarmı?

:::reveal Cavab
- **Aktiv və xassə:** noutbuk, sessiya və məlumat; məxfilik.
- **Səbəb:** BitLocker-in aktivliyi kifayət sübut deyil; yuxu rejimində açar yaddaşda ola bilər, sessiya və fiziki müdaxilə riski var.
- **Tədbir:** etibarlı cihazdan hesab sessiyaları və riskli tokenlər ləğv edilir, cihaz sertifikatları qiymətləndirilir, uzaqdan kilidləmə və uyğun silmə əmri verilir.
- **Yoxlama:** əmrin icra vəziyyəti izlənir.
- **Gələcək:** qısa ekran kilidi, uyğun yükləmə PIN-i, qorunan hibernasiya, mərkəzi bərpa açarı idarəsi.
:::

**Situasiya 3.** İmtahan həftəsində LMS serverinin açıq komponentində real istismarı təsdiqlənmiş zəiflik aşkarlanır. Yamağın tətbiqlə uyğunluğu hələ sınanmayıb. Sistemə toxunmamaq təklif olunur. Qərar necə verilməlidir?

:::reveal Cavab
- **Aktiv və xassə:** LMS serveri; əlçatanlıq (imtahan) ilə məxfilik/tamlıq riski toqquşur.
- **Səbəb:** aktiv istismar və açıq komponent; yamaq sınanmayıb.
- **Tədbir:** zəif funksiya məhdudlaşdırılır, uyğun qoruyucu qayda və ya giriş məhdudiyyəti tətbiq olunur, istismar əlamətləri axtarılır; paralel sınaqda yamaq, bərpa və geri qaytarma yolu yoxlanır; qısa texniki pəncərədə yamaq quraşdırılır.
- **Yoxlama:** versiya və əsas LMS əməliyyatı təsdiqlənir.
- Müvəqqəti istisnanın məsulu və bitmə vaxtı olur; təkcə monitorinq yamağın əvəzi deyil.
:::

**Situasiya 4.** Əməkdaş şəxsi telefonundan universitet poçtuna daxil olur. Telefon itəndə texnik tam silmə əmri vermək istəyir. Cihazda iş profili var. Hansı məlumat və səlahiyyət sərhədi yoxlanmalıdır?

:::reveal Cavab
- Qeydiyyat modeli, razılaşdırılmış idarəetmə hüququ və seçici silmə imkanı yoxlanır.
- Prioritet: iş məlumatının silinməsi, sessiya və sertifikatların ləğvi.
- Şəxsi şəkillərin silinməsi üçün texniki imkan təşkilati səlahiyyət demək deyil.
- Cihaz oflayndırsa, əmr gözləyir; tamamlanmış silmə kimi hesabat verilmir.
- Gələcək qeydiyyatda istifadəçiyə universitetin gördüyü məlumat və edə bildiyi əməliyyatlar açıqlanır.
:::

**Situasiya 5.** Kitabxana Linux serverində texnik SSH parol girişini bağlayıb, açar girişini isə yoxlamayıb. Mövcud sessiya hələ açıqdır. Tətbiqin nasazlığına görə SELinux-u da tam söndürmək istəyir. Düzgün düzəliş nədir?

:::reveal Cavab
- **Risk:** giriş itkisi (əlçatanlıq) və məcburi nəzarətin itirilməsi.
- **Tədbir:** mövcud sessiya saxlanır, konsol yolu hazırlanır, açar və fayl sahibliyi yoxlanır; `sshd -t`, effektiv siyasət və Match blokları qiymətləndirilir.
- Yeni ayrıca sessiyada giriş təsdiqlənəndən sonra əvvəlki sessiya bağlanır.
- SELinux rədd qeydi araşdırılır, tətbiqin tələb etdiyi dar icazə və düzgün kontekst seçilir; bütün məcburi nəzarəti söndürmək geniş risk yaradır.
:::

**Situasiya 6.** Kampusun iki binası optik liflə bağlanıb. Texnik optikanın dinlənmədiyini deyərək tələbə məlumatının şifrələnməsini lazımsız sayır. Eyni hesabatda RJ45 optik konnektor, PDU isə trafik paylayıcısı yazılıb. Hansı düzəlişlər tələb olunur?

:::reveal Cavab
- Optik lif fiziki müdaxilə ilə dinlənə bilər, ona görə uyğun şifrələmə saxlanılır; optik büdcə və birləşmə itkisi də ölçülür.
- RJ45 (8P8C) mis Ethernet konnektorudur, optik deyil; optikdə LC və SC kimi uclar işlənir.
- PDU elektrik enerjisini paylayır; idarə olunan PDU-nun uzaqdan idarəetməsi ayrıca qorunur.
- Tipik 10 Gigabit bağlantı üçün SFP+ seçilir.
:::

**Situasiya 7.** Universitetin ölçü cihazı dəstəyi bitmiş Windows 10 kompüterinə bağlıdır. İstehsalçı başqa sistem üçün drayver vermir. İnternetə bağlı kompüterdə antivirus aktivdir. Cihazı dərhal dəyişmək mümkün deyil. Risk necə idarə edilməlidir?

:::reveal Cavab
- Buraxılış və uyğun biznes ESU imkanı yoxlanır; ESU olsa da miqrasiya planı saxlanılır.
- Kompüter və cihaz ayrıca zonaya keçirilir, ümumi İnternet və inzibati sistemlərə yol bağlanır.
- Məlumat təsdiqlənmiş vasitəçi ilə çıxarılır, hesablar məhdudlaşdırılır, şəbəkə müşahidəsi qurulur.
- Dəyişikliklər laboratoriya məsulu ilə sınanır (təcrübə davamlılığı).
- Müddətli istisna, risk sahibi və əvəzləmə tarixi müəyyən edilir; antivirus dəstəksiz sistemin riskini aradan qaldırmır.
:::

**Situasiya 8.** Şərti hesabatda 100 idarə olunan cihazdan 95-i yamaqlanıb və nəticə 95 faiz verilib. Şəbəkə uçotu daha 25 uyğun cihaz göstərir. Onlardan məlumat alınmayıb. EDR panelində də bütün sensorlar quraşdırılmış görünür, lakin son əlaqə vaxtı yoxlanmır. Hesabat necə düzəldilməlidir?

:::reveal Cavab
- Ümumi əhatə 125 cihazdırsa, təsdiqlənmiş yamaqlanma 95/125, yəni 76 faizdir.
- Naməlum cihazlar gizlədilmir, ayrıca vəziyyət və məsul şəxslə göstərilir.
- Sensor quraşdırılması ilə sağlamlığı ayrılır; son əlaqə, siyasət versiyası və sınaq xəbərdarlığının çatması ölçülür.
- Yenilənmənin göndərilməsi faktiki quraşdırma sayılmır.
- Göstəricinin məxrəci, ölçmə anı və istisnaları hesabatda açıq yazılır.
:::

## Konspektdən situasiyalar

**Situasiya 1.** İnformatika fakültəsinin kompüter laboratoriyasında tələbələr admin hüququ ilə işləyir, çünki bəzi dərslər üçün proqram quraşdırmaq lazımdır. Son ayda üç kompüterdə kriptomayner tapılıb. Hansı tədbirləri təklif edərdin?

:::reveal Cavab
- Tələbələrdən admin hüququ götürülür (minimal səlahiyyət).
- Dərs proqramları mərkəzdən (Intune, SCCM) və ya laborantın müvəqqəti icazəsi ilə quraşdırılır; tətbiqlərə nəzarət (allowlisting) tanınmayan exe-ni bloklayır.
- Kompüterlər eyni baza konfiqurasiyasından qurulur (hər dərsdən sonra təmiz vəziyyətə qayıdan image ilə).
- EDR aktiv olmalı və işlədiyi yoxlanmalıdır; laboratoriya ayrıca VLAN-da olmalıdır.
- Yoluxmuş kompüterlər sıfırdan qurulur.
:::

**Situasiya 2.** Prorektorun BitLocker ilə şifrələnmiş noutbuku taksidə qalıb. Noutbuk yuxu rejimində idi, sessiya açıq idi. İT direktoru deyir: "Disk şifrələnib, narahatlığa əsas yoxdur." Razısanmı?

:::reveal Cavab
- Tam razı deyiləm: disk şifrələməsi söndürülmüş cihazı qoruyur; yuxu rejimində açar yaddaşdadır və sessiya açıqdırsa, ekran kilidi aşılsa məlumat görünə bilər.
- Tədbirlər: MDM ilə uzaqdan kilidləmə və ya silmə; prorektorun parolunu dəyişib bütün sessiya və tokenləri ləğv etmək; cihazın sertifikatlarını (VPN, Wi-Fi) ləğv etmək; BitLocker bərpa açarının harada saxlandığını yoxlamaq.
- Gələcək üçün: yuxu əvəzinə hibernasiya, qısa ekran kilidi müddəti, yükləmədən əvvəl PIN (TPM + PIN).
:::

**Situasiya 3.** Universitetin tələbə portalının veb serverində aktiv istismar olunan kritik zəiflik elan olunub, amma portal sessiyanın ortasındadır və istehsalçının yamağı ilə tətbiqin uyğunluğu yoxlanmayıb. Nə etmək lazımdır?

:::reveal Cavab
- Zəiflik KEV-dədirsə və server İnternetə açıqdırsa, risk yüksəkdir.
- Dərhal kompensasiyaedici tədbirlər: WAF-da virtual yamaq, zəif modulu və ya funksiyanı müvəqqəti söndürmək, girişi məhdudlaşdırmaq, serverdə istismar əlamətlərini (IoC) axtarmaq, monitorinqi gücləndirmək.
- Paralel olaraq yamaq test mühitində sınanır və ən qısa vaxtda, geri qaytarma planı ilə quraşdırılır.
- İstisna yazılı və qısa müddətli olmalı, rəhbərlik qalıq riski təsdiqləməlidir.
:::

## Ehtimal olunan əlavə suallar

:::reveal Antivirus, EDR və XDR-ı fərqləndirin.
- Antivirus (EPP-nin əsası) fayllara baxır (imza, evristika), məlum zərərli faylı bloklayır və karantinə alır; yeni hücumların hamısını tutmur, telemetriyası EDR-dən azdır.
- EDR cihazdakı bütün davranışa baxır (proses, şəbəkə, reyestr, yaddaş), şübhəli zənciri aşkarlayır, cihazı təcrid edir, prosesi dayandırır; analitik və sazlama tələb edir.
- XDR son qurğu, poçt, şəbəkə, bulud və kimliyi əlaqələndirir, mərkəzi cavab verir; adətən bir istehsalçının ekosisteminə bağlıdır.
:::

:::reveal Hardening-in dörd əsasını sadalayın və izah edin.
- **Uçot:** hansı cihazlar var, kimə aiddir, nə məlumat emal edir; uçotda olmayan cihaz qorunmayan sayılır.
- **Minimal səlahiyyət:** gündəlik adi hesab, admin hüququ ayrıca və müvəqqəti, LAPS.
- **Minimal funksionallıq:** lazımsız proqram, xidmət, port və protokol (SMBv1, Telnet) söndürülür.
- **Baza konfiqurasiyası:** təsdiqlənmiş standart parametrlər (CIS Benchmarks, Microsoft Security Baseline); drift mərkəzdən yoxlanır.
:::

:::reveal Disk şifrələməsi, TPM və Secure Boot nəyi qoruyur, nəyi qorumur?
- Disk şifrələməsi (BitLocker, FileVault, LUKS) söndürülmüş cihaz oğurlananda məlumatı qoruyur; işləyən və ya yuxu rejimindəki cihazda açarlar yaddaşda qalır.
- TPM açarları qoruyur və yükləmə ölçmələrini saxlayır; zəncir dəyişibsə açar vermir.
- Secure Boot yalnız imzalı yükləyici və nüvəni işlədir (bootkit); işləmə vaxtındakı hücumlara qarşı qorumur.
:::

:::reveal MDM, UEM və MAM arasındakı fərq nədir?
- MDM qeydiyyatlı cihazlara ekran kilidi, şifrələmə, tətbiq və şəbəkə siyasəti, uzaqdan silmə tətbiq edir.
- UEM müxtəlif cihaz siniflərini bir idarəetmədə birləşdirir.
- MAM tətbiq və onun təşkilati məlumatına yönəlir.
- Bunlar eyni sərhədi idarə etmir; BYOD-da iş profili və ya MAM şəxsi və iş məlumatını ayırır.
:::

:::reveal Aktiv və passiv şəbəkə komponentlərini fərqləndirin, nümunələr verin.
- Aktiv: xarici enerji ilə siqnalı yaradır, qəbul edib emal edir, bərpa edir, çevirir və ya ötürməni idarə edir: kommutator, marşrutizator, giriş nöqtəsi, media çevirici, SFP, təkrarlayıcı, gücləndirici.
- Passiv: siqnalı yaratmadan fiziki yolla ötürür, birləşdirir, bölür: kabel, konnektor, passiv optik bölücü, patch panel.
- Rəf və kabel meneceri dəstək infrastrukturudur; sadə PDU enerji paylayır, idarə olunan PDU aktiv idarəetmə sistemi kimi qorunur.
:::

:::reveal Yamaq prioriteti üçün hansı faktorlar nəzərə alınır? Nümunə ilə göstərin.
- Real istismar (KEV), İnternetə açıqlıq, sistemin kritikliyi, məlumatın həssaslığı, mövcud tədbirlər; CVSS tək kifayət deyil.
- Nümunə: İnternetə açıq VPN şlüzündə aktiv istismar olunan CVSS 7,5 zəiflik daxili kompüterdəki CVSS 9,8-dən əvvəl yamanır; LMS serverində sürətli sınaq və tətbiq, daxili cihazda planlı qısa pəncərə, köhnə ölçü sistemində izolyasiya.
:::

:::reveal Yamaqlanma göstəricisini hesablayın: uçotda 200 cihaz, vaxtında yamaqlanan 180, skan daha 20 idarə olunmayan cihaz tapıb.
- Uçota görə pay 180/200 = 90 faizdir.
- Əhatə 200 + 20 = 220 cihaza genişlənəndə pay 180/220 ≈ 81,8 faizdir.
- Nəticə: uçotun tamlığı göstəricinin mənasını dəyişir; məxrəc, ölçmə anı və istisnalar açıq yazılmalıdır.
:::

:::reveal Zero Trust yanaşmasını izah edin.
- Şəbəkə daxilində olmaq avtomatik etibar üçün kifayət deyil; NIST SP 800-207 açıq yoxlama və ən az səlahiyyətə əsaslanan arxitekturanı təsvir edir.
- Qərar istifadəçi kimliyi, cihazın vəziyyəti və resursun həssaslığı ilə verilir.
- Nümunə: LMS-in açıq elanı veb girişlə, tələbə bazasının idarəsi isə idarə olunan cihaz, güclü autentifikasiya və audit tələb edir; yenilənməmiş cihaza yalnız yenilənmə xidmətinə məhdud yol verilir.
- Bu konkret məhsul deyil, qərar qurma qaydasıdır.
:::

:::reveal Uyğunluq skanı, zəiflik skanı və nəzarət sınağı necə fərqlənir?
- Uyğunluq skanı sazlamanı bazaya qarşı yoxlayır.
- Zəiflik skanı məlum zəifliyi axtarır.
- Nəzarət sınağı tədbirin gözlənilən davranışını təsdiqləyir (məsələn, adi istifadəçi inzibati qovluğa yaza bilmir, agentin susması xəbərdarlıq yaradır).
- Baza tam uyğun ola, amma yamaqlanmamış zəiflik qala bilər; qəbul zamanı texniki vəziyyət, iş funksiyası və cavab prosesi birlikdə yoxlanır.
:::
