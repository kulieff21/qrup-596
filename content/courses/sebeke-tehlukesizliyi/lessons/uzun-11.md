+++
title = "Son qurğuların təhlükəsizliyi və sistemlərin mühafizəsinin gücləndirilməsi"
unit = "uzun"
order = 11
summary = "Tam mühazirə: son qurğu və hücum səthi, EPP/EDR/XDR/MDR, hardening, minimum səlahiyyət, yamaqlar, Secure Boot/TPM/disk şifrələməsi, Windows və Linux bazası, mobil cihazlar, loglar, insidentə cavab, şəbəkə avadanlığı, IoT, Zero Trust və ölçmə."
updated = 2026-11-09

[[source]]
title = "Mühazirə 11: Son qurğuların təhlükəsizliyi və sistemlərin mühafizəsinin gücləndirilməsi"
note = "Elmar Cabbarov, 2026–2027"
+++

Hücumların çoxu son qurğuda başlayır: əməkdaşın noutbukunda, laboratoriya kompüterində, tələbənin telefonunda. Mövzu bu cihazları qoruyan texnologiyaları və onların hücum səthini kiçildən gücləndirmə (hardening) prosesini əhatə edir. Universitet topologiyası, cihaz adları, ünvanlar və rəqəmlər **şərti tədris nümunəsidir**, real mühit deyil.

## Son qurğu və hücum səthi

### Qorunan obyektin sərhədi

Son qurğu (endpoint) informasiya sistemində məlumatı qəbul edən, emal edən və ya saxlayan cihazdır. İş stansiyası, noutbuk, smartfon və planşet istifadəçiyə xidmət edir. Server başqa sistemlərin sorğularını emal edir, amma üzərində əməliyyat sistemi, hesablar və proqramlar olduğu üçün qurğu səviyyəsində mühafizəyə ehtiyacı var. Printer, kamera, ağıllı lövhə və laboratoriya ölçü cihazı da şəbəkənin son nöqtəsi ola bilər; onların hamısına masaüstü antivirus quraşdırmaq mümkün deyil.

Əməkdaşın noutbuku LMS-ə, poçta və kafedranın sənəd qovluğuna daxil olur. Hücumçu onu ələ keçirəndə diskdəki sənədlərlə yanaşı brauzer sessiyalarını, yaddaşdakı giriş məlumatlarını və qoşulmuş şəbəkə resurslarını da hədəfləyir. Ona görə son qurğuların təhlükəsizliyi cihazın özünü, məlumatını və istifadə etdiyi giriş imkanlarını qoruyan tədbirlərin cəmidir.

Üç xassə: **məxfilik** icazəsiz oxumaqdan, **tamlıq** icazəsiz dəyişməkdən qorumaq, **əlçatanlıq** xidmətdən vaxtında istifadədir. Tələbə bazasının ixracı məxfiliyi, qiymətin dəyişdirilməsi tamlığı pozur; imtahan vaxtı laboratoriya kompüterlərinin işləməməsi əlçatanlıq problemidir.

| Qurğu | İş funksiyası | Başlıca risk | Uyğun tədbir |
| --- | --- | --- | --- |
| Kafedra noutbuku | Sənəd və poçt işi | Oğurlanma, sessiya itkisi | Disk şifrələməsi, MFA, EDR |
| Tələbə laboratoriyası | Dərs proqramları | İcazəsiz icra, ortaq hesablar | Adi hesablar, tətbiq nəzarəti |
| LMS serveri | Tədris xidməti | Xidmət zəifliyi, məlumat itkisi | Yamaq, xidmət hesabı, bərpa |
| Kitabxana terminalı | Kataloq axtarışı | Əvvəlki istifadəçinin sessiyası | Məhdud rejim, sessiya təmizlənməsi |
| Şəbəkə printeri | Sənəd çapı | Yaddaşda sənəd, açıq idarəetmə | Ayrıca zona, yenilənmə, giriş nəzarəti |
| Ölçü cihazı | Təcrübə məlumatı | Köhnə proqram təminatı | İzolyasiya, vasitəçi kompüter |

### Hücum səthini necə müəyyən etmək olar

Hücum səthi (attack surface) müdaxilə üçün istifadə edilə bilən proqram, xidmət, interfeys və giriş imkanlarının cəmidir: açıq portlar, işləyən xidmətlər, quraşdırılmış proqramlar, admin hesabları, USB portları. Dinləyən port görünən hissədir; sənəd makrosu, brauzer əlavəsi, USB klaviatura, lokal administrator hesabı və uzaqdan yardım agenti də daxildir. İnternetdən əlçatmaz cihazda hücum səthinin sıfır olduğunu düşünmək səhvdir: zərərli fayl USB ilə gələ, hücumçu qonşu kompüterdən qoşula və ya fiziki giriş əldə edə bilər.

Sistemin mühafizəsinin gücləndirilməsi (system hardening) lazımsız imkanları azaltmaq, zəif sazlamaları dəyişmək və nəzarətləri yoxlamaq prosesidir. İstifadə edilməyən uzaqdan masaüstü xidməti bağlanırsa, bir giriş yolu azalır; proqramı silmədən yalnız menyudakı nişanı gizlətmək eyni nəticəni vermir.

Risk hücum imkanının **ehtimalını və zərərini birlikdə** qiymətləndirir. Kitabxana terminalı ilə tələbə bazasının administrator kompüteri eyni əməliyyat sistemindən istifadə etsə də, riskləri eyni deyil: ikincinin hesabları daha həssas resurslara çatır. Məqsəd bütün imkanları söndürmək deyil, qanuni işi saxlayaraq hücumun uğur ehtimalını və təsirini azaltmaqdır.

:::note Sadə dillə
Hücum səthi cihazın "qapılarının və pəncərələrinin" sayıdır. Hardening lazımsız qapıları bağlamaq, açıq qalanlara qıfıl vurmaq və qıfılın işlədiyini yoxlamaqdır.
:::

## Təhdidlər və hücumun inkişafı

### Giriş yolları

Zərərli proqram (malware) icazəsiz məqsədlə işləyən proqramdır. Virus başqa fayllara qoşulur, soxulcan şəbəkədə yayılır, troyan faydalı proqram təsiri yaradır. Şantaj proqramı (ransomware) məlumatı şifrələyir və ya yaymaqla hədələyir. Məlumat oğurlayan proqram brauzer parollarını, sessiya məlumatını və faylları toplayır.

Fişinq (phishing) istifadəçini aldadaraq fayl açdırmaq, giriş məlumatı almaq və ya əməliyyatı təsdiqlətmək üsuludur. Şərti nümunə: əməkdaşa təqaüd siyahısının düzəlişi adı ilə sənəd göndərilir, sənəd makronu aktivləşdirməyi tələb edir; istifadəçi bunu edəndə proqram onun hüquqları ilə işləyir. Adi hesab sistem fayllarını dəyişməyi məhdudlaşdıra bilər, amma həmin hesabın oxuduğu sənədlərin oğurlanmasını özbaşına dayandırmır.

Oğurlanmış hesabla girişdə zərərli fayl ümumiyyətlə olmaya bilər: hücumçu parolu, sessiya kukisini və ya giriş tokenini istifadə edir. Çoxamilli autentifikasiya (MFA) parol itkisinə qarşı əlavə maneədir, lakin bütün sessiya oğurluğunu həll etmir.

Əsas təhdidlər: zərərli proqram, fişinq, oğurlanmış parollar, yamanmamış zəifliklər, təhlükəli konfiqurasiya (standart parollar, lazımsız xidmətlər), itmiş və oğurlanmış cihazlar. İstifadəçinin gündəlik işi admin hüquqları ilə görməsi bu təhdidlərin hamısının ziyanını artırır.

| Təhdid | Universitet nümunəsi | Nə müşahidə edilir | Riskin azaldılması |
| --- | --- | --- | --- |
| Fişinq | Saxta imtahan sənədi | Sənəddən proses başlanması | Makro siyasəti, təlim, EDR |
| Proqram zəifliyi | Yenilənməmiş LMS komponenti | Versiya, istismar əlaməti | Prioritet yamaq, giriş məhdudiyyəti |
| Təhlükəli sazlama | Hamıya açıq sənəd qovluğu | Paylaşım hüquqları | Minimum giriş, müntəzəm audit |
| Oğurlanmış hesab | Kafedra hesabından gecə ixracı | Giriş və ixrac qeydləri | MFA, sessiya ləğvi, araşdırma |
| Fiziki itki | Yataqxanada itən noutbuk | Son vəziyyət, açar uçotu | Disk şifrələməsi, uzaqdan tədbir |
| Təchizat zənciri | Etibarsız quraşdırma paketi | Mənbə, imza, dəyişiklik | Təsdiqlənmiş repozitoriya |

### Hücum zəncirini parçalamaq

Hücum bir neçə sərhədi keçir: sənəd və ya hesabla ilkin giriş; sistem haqqında məlumat toplamaq; qalıcı giriş qurmaq; səlahiyyət artırmaq; başqa cihazlara keçmək; axırda məlumatı çıxarmaq və ya xidməti dayandırmaq.

Bir maneə uğursuz olanda növbətinin işləməsi üçün nəzarətlər müxtəlif sərhədlərə qoyulur: poçt filtri məktubu buraxa bilər, tətbiq nəzarəti icranı dayandırır, EDR davranışı aşkarlayır, firewall xarici əlaqəni kəsir; ehtiyat nüsxə məlumatın bərpasına xidmət edir.

Əməkdaşın xəbərdarlığa reaksiyası da texniki prosesə daxildir. Şübhəli sənədi açan şəxs hadisəni dərhal bildirməlidir; cəzalandırılmaq qorxusu xəbərverməni gecikdirirsə, təşkilat araşdırma üçün vaxt itirir.

## EPP, EDR, XDR və MDR

### Qarşısını alma və araşdırma imkanları

**EPP.** Son qurğunun mühafizə platforması (Endpoint Protection Platform, EPP) zərərli fəaliyyəti qurğuda bloklamağa yönəlmiş vasitələr toplusudur; antivirus onun əsas hissəsidir. İmza yoxlaması məlum nümunənin xüsusiyyətini axtarır, evristika şübhəli quruluşu qiymətləndirir, davranış analizi proqramın etdiklərinə baxır. Antivirusu yalnız məlum fayl heşlərini müqayisə edən vasitə saymaq dəqiq deyil; funksiyalar məhsula və sazlamaya görə dəyişir.

**EDR.** Son qurğuda aşkarlama və cavab (Endpoint Detection and Response, EDR) proseslər, fayllar, reyestr dəyişiklikləri, şəbəkə əlaqələri və yaddaş haqqında telemetriya toplayır. Analitik valideyn prosesdən törəyən proseslərə baxır, hansı faylın yazıldığını və hansı ünvana əlaqə qurulduğunu araşdırır. Məhsul dəstəkləyirsə, prosesi dayandırır, faylı karantinə alır, qurğunu şəbəkədən təcrid edir. Telemetriya bütün fəaliyyətin tam surəti deyil: sensorun əhatəsi, saxlama müddəti və platforma məhdudiyyətləri var. Zəif yeri: analitik və düzgün sazlama tələb edir.

**XDR.** Genişləndirilmiş aşkarlama və cavab (Extended Detection and Response, XDR) qurğu, poçt, kimlik, şəbəkə və bulud siqnallarını əlaqələndirir və mərkəzi cavab verir. Poçta gələn məktub, noutbukda başlayan proses və eyni hesabın bulud fayllarını endirməsi bir araşdırmada görünə bilər. Bəzi məhsullar əsasən bir istehsalçının sensorlarını birləşdirir (adətən bir ekosistemə bağlıdır), digərləri xarici mənbələr də qəbul edir. XDR adı bütün mənbələrin avtomatik və tam inteqrasiyasına zəmanət vermir.

**MDR.** İdarə olunan aşkarlama və cavab (Managed Detection and Response, MDR) **xidmət modelidir**: xarici komanda xəbərdarlıqları izləyir, araşdırır və müqavilədə razılaşdırılmış cavabı verir. Universitet EDR alıb onu heç kimin izləmədiyi vəziyyətdə saxlaya bilər; MDR insan və əməliyyat boşluğunu azaldır. Xidmətin hansı məlumatı gördüyü, gecə əlaqə qaydası və cihazı kimin təcrid edə bildiyi müqavilədə aydın olmalıdır.

| Anlayış | Əsas məqsəd | Nümunə (universitet) | Məhdudiyyət |
| --- | --- | --- | --- |
| EPP | Zərərli icranı önləmək | Laboratoriyada zərərli faylın bloklanması | Bütün hücumları tanımır |
| EDR | Qurğuda araşdırma və cavab | Sənəd, skript və bağlantı zənciri | Analitik və düzgün sazlama tələb edir |
| XDR | Mənbələrarası əlaqə | Poçt, cihaz və hesabın birləşdirilməsi | İnteqrasiya və əhatə fərqlənir |
| MDR | Aşkarlama və cavabı xidmətlə aparmaq | Növbəsiz İT şöbəsinə xarici monitorinq | Səlahiyyət və cavab vaxtı razılaşdırılır |

Məhsul nümunələri (konspektdən): antivirus — Microsoft Defender Antivirus; EDR — Defender for Endpoint, CrowdStrike Falcon, SentinelOne; XDR — Microsoft Defender XDR, Cortex XDR.

:::exam
Üçlük: antivirus **faylı** (imza, evristika), EDR cihazdakı **bütün davranışı** (proses, şəbəkə, reyestr, yaddaş), XDR **bir neçə mənbəni** (son qurğu + poçt + şəbəkə + bulud + kimlik) əlaqələndirir. Antivirus bloklayır və karantinə alır; EDR telemetriya toplayır, zənciri aşkarlayır, cihazı təcrid edir.
:::

### Bir xəbərdarlığın mənası

Şərti nümunə: `lab-17` cihazında sənəd tətbiqi skript interpretatorunu başladır, o isə `198.51.100.24` ünvanına əlaqə yaradır. EPP faylı əvvəlcədən tanımaya bilər. EDR proses ağacını göstərir. XDR eyni məktubun digər əməkdaşlara da çatdığını tapır. MDR komandası təsdiqlənmiş qaydaya görə cihazı təcrid edib universitetin məsul şəxsinə xəbər verir.

Qanuni statistik paket də skript işlədə bilər, ona görə yalnız proses adına baxıb bütün laboratoriyanı bloklamaq düzgün deyil. Faylın haradan gəldiyi, imzası, komanda sətri, istifadəçi və dəyişiklik sifarişi araşdırılır. Yanlış müsbət nəticə qanuni fəaliyyəti şübhəli sayır; yanlış mənfi nəticə hücumu buraxır. Siyasət bu iki xərci nəzərə almalıdır.

Agentin quraşdırılması onun işləməsini sübut etmir. Sensorun son əlaqə vaxtı, siyasət versiyası, müdaxilədən qorunması və xəbərdarlığın qəbul nöqtəsi yoxlanır. Laboratoriyada zərərsiz sınaq hadisəsi yaradılıb onun analitikə çatması ölçülür.

## Mühafizənin gücləndirilməsi prosesi

Konspektin dörd əsası: **uçot**, **minimal səlahiyyət**, **minimal funksionallıq**, **baza konfiqurasiyası**.

:::tip Yadda saxla
Hardening-in 4 əsası: (1) uçot, (2) minimal səlahiyyət, (3) minimal funksionallıq (lazımsız proqram, xidmət, port, protokol, məsələn SMBv1 və Telnet söndürülür), (4) baza konfiqurasiyası (CIS Benchmarks, Microsoft Security Baseline).
:::

### Uçot və məsuliyyət

Uçotda cihazın sahibi, iş funksiyası, yerləşdiyi zona, əməliyyat sistemi, proqramlar, dəstək vəziyyəti və emal etdiyi məlumat göstərilir. Şəbəkə skanı, idarəetmə agenti, satınalma qeydləri və kommutator port məlumatı tutuşdurulur; heç bir mənbə təkbaşına bütün cihazları göstərmir. Evdən işləyən noutbuk kampus skanında görünməyə, agenti olmayan printer idarəetmə siyahısında olmaya bilər.

Uçotda olmayan cihazın mütləq qorunmadığını iddia etmək olmaz, lakin qorunduğuna dair təşkilati sübut yoxdur (konspektdə: "uçotda olmayan cihaz qorunmayan cihazdır"). Kafedranın öz vəsaiti ilə aldığı ölçü kompüteri aşkarlananda əvvəlcə sahibi və funksiyası müəyyən edilir, sonra cihaz uyğun idarəetmə qrupuna daxil edilir və ya məhdud şəbəkəyə keçirilir.

| Sahə | Nə saxlanır | Hansı qərarı dəstəkləyir |
| --- | --- | --- |
| Sabit identifikator | Seriya nömrəsi, idarəetmə identifikatoru | Adı dəyişmiş cihazı tanımaq |
| Sahib və məsul şəxs | Kafedra, əlaqə ünvanı | Dəyişiklik və insident əlaqəsi |
| Sistem və proqramlar | Buraxılış, versiya, paketlər | Yamaq və uyğunluq |
| Məlumat sinfi | Açıq, daxili, məhdud məlumat | Şifrələmə və giriş səviyyəsi |
| Şəbəkə zonası | VLAN, ünvan, port | Təcrid və trafik qaydası |
| Nəzarət vəziyyəti | EDR, şifrələmə, son əlaqə | Uyğunsuzluğu aşkar etmək |
| Dəstək və istisna | Son tarix, təsdiq, əvəzləmə planı | Qalıq riskin idarəsi |

### Baza konfiqurasiyası və standartlar

Baza konfiqurasiyası (security baseline) müəyyən cihaz qrupu üçün təsdiqlənmiş minimum sazlamalardır (ekran kilidi, firewall, audit, makroların bloklanması). Kafedra noutbuku, açıq kitabxana terminalı və LMS serveri üçün ayrı baza hazırlanır: noutbukda disk şifrələməsi və ekran kilidi, terminalda sessiyanın təmizlənməsi, serverdə xidmət hesabları və inzibati giriş məhdudiyyəti daha çox diqqət tələb edir.

- **CIS Benchmarks** konkret məhsul və buraxılış üçün təhlükəsiz sazlama tövsiyələridir; profil səviyyələri həmin sənədin izahına əsasən seçilir, daha sərt profil iş proqramlarına təsir edə bilər.
- **STIG** (DISA-nın Security Technical Implementation Guide sənədləri) texniki tələbləri və yoxlama qaydalarını təsvir edir. ABŞ müdafiə mühiti üçün hazırlanır; universitetdə avtomatik hüquqi tələb sayılmır.
- Hər ikisi yoxlanmış başlanğıc nöqtəsi verə bilər, tətbiq tələblərini əvəz etmir.
- **CIS Controls** təşkilat üzrə tədbirləri qruplaşdırır (məsələn, cihaz uçotu), CIS Benchmarks isə məhsul sazlamasına daha dərindən baxır (məsələn, konkret Linux xidmətinin söndürülməsi).
- **ISO/IEC 27001:2022** idarəetmə sistemi tələblərini, **ISO/IEC 27002:2022** tədbirlərə dair rəhbərliyi verir. 27002-dəki 93 tədbir dörd mövzu üzrə qruplaşır; sənəd kor-koranə icra ediləcək skript deyil.

Gücləndirmə ardıcıllığı: funksiyanı öyrənmək, bazanı seçmək, fərqləri ölçmək, sınaq etmək, tətbiq etmək, nəticəni izləmək.

![figure](m11-1.png)

*Şəkil 1. Gücləndirmə prosesi ölçülən vəziyyətdən başlanır və təkrar yoxlama ilə davam edir: inventar → baza xətti (CIS, STIG) → tətbiq (pilot qrup) → ölçmə (uyğunluq) → sapma (izləmə) → təkrar yoxlama, istisnalar müddətli olur.*

### Bazadan yayınma və istisna

Konfiqurasiyanın bazadan yayınması (configuration drift) zamanla yaranır: texniki problemi həll etmək üçün firewall qaydası genişləndirilir, tətbiq quraşdırıcısı xidmət açır, istifadəçi brauzer əlavəsi quraşdırır. Group Policy, MDM, Intune və Ansible kimi vasitələr siyasəti yaymağa və fərqləri tapmağa kömək edir; uyğunluq mərkəzdən müntəzəm yoxlanır və bərpa edilir.

Şərti nümunə: kafedranın statistik proqramı köhnə komponent tələb edir. İstisnada cihazlar, konkret tələb, risk, kompensasiyaedici tədbir, məsul şəxs və bitmə tarixi yazılır. Bütün fakültə üçün nəzarətin söndürülməsi əsaslandırılmır; sınaqdan sonra yalnız lazım olan cihaz qrupuna dar qayda verilir. Müddət bitəndə istisna bağlanır və ya yeni sübutla yenidən qiymətləndirilir.

## Minimum səlahiyyət və hesabların qorunması

Minimum səlahiyyət (least privilege) istifadəçi və prosesə iş üçün lazım olan hüquqların verilməsidir. Tələbə dərs proqramını işlətməli, amma sistem xidmətini dəyişməməlidir.

Gündəlik hesabla inzibati hesab ayrılır: administrator poçtu adi hesabla oxuyur, xidmət sazlamasını ayrıca hesabla dəyişir. İmtiyazlı giriş müddətli verilə bilər; bu, ehtiyac anında səlahiyyət (just-in-time privilege) yanaşmasıdır. Proqram quraşdırılması üçün verilmiş səlahiyyət iş bitəndə geri alınır və əməliyyat qeydə düşür. Windows-da UAC təsdiq pəncərəsi faydalıdır, ayrıca hesab və səlahiyyət bölgüsünün tam əvəzi deyil.

**LAPS.** Lokal Administrator Parolu Həlli (Local Administrator Password Solution, LAPS) idarə olunan Windows cihazlarının lokal administrator parollarını fərqləndirməyə və dövri dəyişməyə xidmət edir. Windows LAPS siyasət və mühitdən asılı olaraq parolu Active Directory və ya Microsoft Entra ID-də ehtiyatlayır. Parolu oxumaq hüququ məhdudlaşdırılır və audit olunur. Bütün kompüterlərdə eyni lokal administrator parolu varsa, bir cihazdan alınan məlumat başqalarına keçidi asanlaşdırır; LAPS bu ortaq sirr problemini azaldır.

LAPS domen administratorunun parolunu idarə etmir və lokal administrator hesabını zərərsiz etmir. Oxuma hüququ olan hesab ələ keçirilsə, çoxlu cihazın parolu risk altına düşə bilər; ona görə parolun saxlandığı sistem, oxucu qruplar və istifadədən sonrakı dəyişmə qaydası qorunur.

| Hesab | İcazəli iş | Verilməməli hüquq | Yoxlama sübutu |
| --- | --- | --- | --- |
| Tələbə hesabı | Dərs proqramı, şəxsi qovluq | Lokal administrator | Qrup üzvlüyü |
| Laborant hesabı | Təsdiqlənmiş texniki iş | Domen üzrə tam idarə | Müddətli icazə qeydi |
| LMS xidmət hesabı | Tətbiqin tələb etdiyi resurs | İnteraktiv gündəlik giriş | Xidmət və giriş auditi |
| Şəbəkə administratoru | İdarəetmə zonasından sazlama | Adi poçtda imtiyazlı sessiya | Bastion və AAA qeydləri |
| Fövqəladə hesab | Razılaşdırılmış bərpa işi | Nəzarətsiz daimi istifadə | İstifadə xəbərdarlığı |

Xidmət hesablarının parollarını skriptin içinə yazmaq risklidir: LMS ehtiyatlama tapşırığı yalnız lazım olan qovluğu oxumalı və qorunan anbara yazmalıdır; ehtiyat nüsxələri silmək hüququ ayrıca saxlanıla bilər. İşçi işdən ayrıldıqda hesabı bağlanır, qrup üzvlükləri və verilmiş açarlar yoxlanır. Təhlükəsizlik icazə vermə mərhələsi ilə bitmir; artıq lazım olmayan hüququ geri almaq da prosesə daxildir.

## Yamaqlar və dəstək müddəti

### Yenilənmənin beş mərhələsi

Yamaq (patch) proqramdakı səhvi və ya zəifliyi aradan qaldıran dəyişiklikdir. Yenilənmə əməliyyat sistemindən başqa brauzerə, sənəd proqramına, VPN müştərisinə, drayverə və cihazın daxili proqram təminatına da aiddir. NIST SP 800-40 Rev. 4 bu işi müəssisənin planlı profilaktik texniki xidməti kimi nəzərdən keçirir. Konspektdə bu, "müəllimin 5 mərhələsi" adlanır.

:::steps Yamaq idarəsinin beş mərhələsi
[[step]]
title = "Aşkarla"
body = "Təhlükəsizlik bildirişi, proqram versiyası və skan nəticəsi tutuşdurulur; cihazın həqiqətən təsirlənib-təsirlənmədiyi yoxlanır."

[[step]]
title = "Prioritet ver"
body = "Real istismar (KEV), CVSS, əlçatanlıq, məlumatın həssaslığı və mövcud tədbirlər birlikdə qiymətləndirilir."

[[step]]
title = "Sına"
body = "Təmsilçi pilot cihaz qrupunda iş proqramı və geri qaytarma yolu yoxlanır."

[[step]]
title = "Mərhələli quraşdır"
body = "Pilot qrupdan sonra uyğun cihaz qruplarına keçilir, lazım olan yenidən başlatma planlaşdırılır."

[[step]]
title = "Yoxla"
body = "Versiya, faktiki quraşdırma, yenidən başlatma və xidmətin işləməsi təsdiqlənir; uğursuz cihazlar ayrıca işlənir."
:::

![figure](m11-2.png)

*Şəkil 2. Yamaq dövründə göndərmə ilə təsdiqlənmiş quraşdırma ayrı mərhələlərdir: "göndərildi" və "quraşdırıldı" fərqli vəziyyətlərdir, yalnız təsdiqlənmiş versiya sayılır.*

:::exam
Yamağın göndərilməsi onun quraşdırıldığını sübut etmir, ona görə 5-ci mərhələ (yoxlama) vacibdir. Prioritet təkcə CVSS balı ilə yox, real istismar faktı (CISA KEV), İnternetə açıqlıq və kritiklik ilə müəyyən olunur.
:::

CVSS zəifliyin texniki ağırlığını qiymətləndirməyə kömək edir, amma təşkilatın bütün riskini göstərmir. CISA-nın Known Exploited Vulnerabilities (KEV) kataloqunda real istismarı məlum zəifliklər verilir; kataloqda olmayan zəifliyin istismar edilmədiyi nəticəsi çıxmır. İnternetə açıqlıq, işlək istismar vasitəsi, istifadəçi müdaxiləsi tələbi və sistemin funksiyası da qərara daxildir. Gələcək istismar ehtimalını qiymətləndirən EPSS kimi göstəricilər faktiki istismar sübutu ilə qarışdırılmamalıdır.

| Sistem | Məlum vəziyyət | Qərarın səbəbi | Tədbir |
| --- | --- | --- | --- |
| Xarici VPN şlüzü | Aktiv istismar təsdiqlənib | İlkin giriş sərhədidir | Təcili məhdudiyyət və yamaq |
| LMS serveri | Zəif komponent açıqdır | Tələbə məlumatına çatır | Sürətli sınaq və tətbiq |
| Daxili tədris cihazı | Yüksək bal, xidmət bağlıdır | İstismar yolu məhduddur | Planlı qısa pəncərə |
| Köhnə ölçü sistemi | Yamaq uyğun deyil | Təcrübə dayana bilər | İzolyasiya, əvəzləmə planı |

Şərti nümunədə birinci sistemdə (İnternetə açıq VPN şlüzü) CVSS 7,5, daxili cihazda 9,8 ola bilər. Aktiv istismar və xaricdən əlçatanlıq birinci sistemin əvvəl işlənməsini əsaslandıra bilər. Məqsəd balı görməməzliyə vurmaq deyil, onu mühitin faktları ilə tamamlayaraq qərar verməkdir. Yamaq qoyula bilməyən sistemlər (köhnə laboratoriya avadanlığı) üçün kompensasiyaedici tədbirlər tətbiq edilir: seqmentasiya, xidmətin söndürülməsi, əlavə monitorinq.

### Sınaq, geri qaytarma və köhnəlmə

Pilot qrup təsadüfi seçilmir: laboratoriyada statistik paket, mühəndislik proqramı və xüsusi USB drayveri varsa, hər biri sınaqda təmsil olunur. Uğur meyarı əvvəlcədən yazılır: giriş, proqramın açılması, nümunə faylın emalı, nəticənin saxlanması. Yamaq geri qaytarıldıqda zəiflik də qayıda bilər; geri qaytarma vaxtında müvəqqəti məhdudiyyət saxlanır.

Windows 10-un ümumi dəstəyi **14 oktyabr 2025**-ci ildə bitib. Uyğun biznes cihazları üçün Extended Security Updates (ESU) proqramı **14 oktyabr 2028**-ci ilədək təhlükəsizlik yenilənmələri verə bilər. Bu, bütün Windows 10 buraxılışlarının eyni həyat dövrü olduğu və ya cihazın avtomatik ESU aldığı demək deyil; xüsusi xidmət kanallarının cədvəli ayrıca yoxlanır. Universitet hər cihazın buraxılışını, lisenziya uyğunluğunu və faktiki yenilənmə qəbulunu uçota almalıdır.

Dəstəksiz sistemə antivirus quraşdırmaq çatışmayan təhlükəsizlik düzəlişlərini əvəz etmir. Köhnə laboratoriya drayveri miqrasiyanı saxlayırsa, cihaz ayrıca zonaya keçirilir, İnternetə çıxışı məhdudlaşdırılır, yalnız lazım olan vasitəçi ilə danışır. Risk sahibi müddətli istisnanı təsdiqləyir, əvəzləmə planı hazırlanır. Müddətsiz istisna yamaq strategiyası deyil.

## Secure Boot, TPM və disk şifrələməsi

### Yüklənmədə etibarın qurulması

UEFI Secure Boot yüklənən icra komponentlərinin imzalarını etibar və ləğvetmə siyahıları ilə yoxlayır; məqsəd əməliyyat sistemi başlamazdan əvvəl icazəsiz kodun icrasını məhdudlaşdırmaqdır (yalnız imzalanmış yükləyici və nüvə işə düşür, bootkit-lərə qarşı qoruyur). Etibarlı imza kodun qüsursuz olduğunu sübut etmir: zəif imzalanmış komponentin ləğv siyahısına salınması və firmware yenilənməsi lazım ola bilər. Secure Boot işləmə vaxtındakı (runtime) hücumlara qarşı qorumur, antivirusun və əməliyyat sistemi yamaqlarının yerini tutmur.

Etibarlı Platforma Modulu (Trusted Platform Module, TPM) açar əməliyyatları və yüklənmə ölçmələri üçün aparat əsaslı təhlükəsizlik imkanları verir; ayrı çip, prosessora inteqrə edilmiş həll və ya firmware əsaslı variant ola bilər. Ölçülən yüklənmə (measured boot) komponentlərin ölçmələrini PCR registrlərində toplayır; bu özbaşına icranı bloklama qərarı deyil. **Secure Boot** imza siyasəti tətbiq edir, **ölçmələr** isə yüklənmiş vəziyyət haqqında sübut verir.

Disk açarı müəyyən PCR vəziyyətinə bağlananda gözlənilməyən yüklənmə dəyişikliyi açarın avtomatik açılmasına mane ola bilər; TPM açarı vermir və bərpa açarı tələb olunur. Hər dəyişiklik mütləq hücum deyil: qanuni firmware yenilənməsi də bərpa tələb edə bilər. TPM-in hansı ölçmələrdən istifadə etməsi siyasətə və platformaya bağlıdır; ona görə yenilənmədən əvvəl bərpa imkanı yoxlanır.

![figure](m11-3.png)

*Şəkil 3. Secure Boot hər mərhələdə (UEFI → yükləyici → nüvə → ƏS) növbətinin imzasını yoxlayır; ölçülən yüklənmə hər mərhələnin heşini TPM-in PCR registrlərinə yazır; disk açarı seçilmiş vəziyyətə bağlana bilər.*

### BitLocker və LUKS

BitLocker Windows-da disk həcmlərinin şifrələməsini idarə edir (macOS-da FileVault). Linux-da LUKS şifrəli həcm formatıdır, cryptsetup isə onun idarə vasitələrindəndir. Şifrələmə disk başqa kompüterə qoşulanda məlumatın açarsız oxunmasını çətinləşdirir, yəni söndürülmüş cihaz oğurlananda qoruyur. Şifrəli həcm işləyən sistemdə açılıbsa, icazəli istifadəçi və onun hüquqları ilə işləyən zərərli proqram məlumatı oxuya bilər. Ekran kilidi bunu təmin etmir: işləyən və ya yuxu rejimindəki cihazda açarlar yaddaşda qalır. Disk şifrələməsi fayl icazəsini və sessiya mühafizəsini əvəz etmir.

TPM ilə avtomatik açılma rahatlıq verir. Yüklənmədən əvvəl PIN əlavə etmək (TPM + PIN) fiziki itki riskini daha sərt idarə edə bilər, amma istifadəçi dəstəyi və fövqəladə giriş prosesi tələb edir. Hər iş stansiyası üçün eyni siyasət seçilmir: kampusdan çıxan inzibati noutbukla nəzarətli otaqdakı serverin fiziki riskləri fərqlidir.

| Mexanizm | Nəyi qoruyur | Nəyi həll etmir | Yoxlama |
| --- | --- | --- | --- |
| Secure Boot | İcazəsiz yükləmə koduna maneə | İşlək sessiyada fişinq | Vəziyyət və etibar siyahıları |
| TPM | Açar əməliyyatı, ölçmə | Bütün zərərli prosesləri tutmaq | Platforma və siyasət vəziyyəti |
| BitLocker və LUKS | Bağlı həcmdə məlumat | Açılmış hesabın sui-istifadəsi | Həcmin vəziyyəti, bərpa sınağı |
| Ekran kilidi | Adi interaktiv girişi məhdudlaşdırır | Diskin çıxarılıb oxunması | Avtomatik kilid siyasəti |
| Ehtiyat nüsxə | Məlumatın bərpası | Sızmış məlumatı geri almaq | Ayrı mühitdə bərpa |

Şərti nümunə: noutbuk nəqliyyatda itir və yuxu rejimindədir. Açarların yaddaşda qalması, sessiyanın vəziyyəti və fiziki müdaxilə imkanları araşdırılır; "BitLocker aktivdir" deyə hadisə bağlanmır. Hesab sessiyaları, cihaz sertifikatları və uzaqdan kilidləmə imkanları qiymətləndirilir. Hibernasiya operativ yaddaş vəziyyətini diskə yazır və söndürülmüş vəziyyətə keçir; qorunma hibernasiya faylının da şifrəli həcmdə olmasından və yenidən açılma siyasətindən asılıdır.

Bərpa açarı cihazın çantasında və ya eyni diskdə açıq faylda saxlanmır: qorunan mərkəzi anbarda (məsələn, Entra ID, AD) saxlanır, kimə verildiyi qeydə alınır, icazə yoxlanır. LUKS başlığının ehtiyatı faydalıdır, lakin həssasdır: başlığın köhnə nüsxəsi əvvəlki açar yuvalarını saxlaya bilər; başlıq ehtiyatı və parollar ayrıca qorunmalıdır. Açarı olan şifrəli ehtiyat nüsxənin bərpa sınağı olmadan şifrələməni uğurlu saymaq olmaz.

:::exam
Disk şifrələməsi **söndürülmüş** cihaz oğurlananda məlumatı qoruyur; ekran kilidi bunu təmin etmir. Secure Boot **bootkit-lərə** qarşıdır, işləmə vaxtındakı hücumlara yox. TPM bağlıdırsa və yükləmə zənciri dəyişibsə, açar verilmir, bərpa açarı lazımdır. "Disk şifrələnib, narahatlığa əsas yoxdur" cümləsi yuxu rejimində olan açıq sessiya üçün səhvdir.
:::

## Tətbiq, firewall və USB nəzarəti

### İcazəli tətbiqlərin siyahısı

Tətbiq icrasına nəzarət (application allowlisting) təsdiqlənmiş proqramların işləməsinə icazə verir; krek və tanınmayan exe faylları işə düşmür. Qayda nəşriyyatçı imzasına, fayl heşinə və ya yola bağlana bilər. Windows-da AppLocker və App Control for Business (əvvəlki adı WDAC) bu məqsədlə istifadə olunur; əməliyyat sistemi buraxılışı və dəstəklənən qayda növləri əvvəlcədən yoxlanır. Tətbiq nəzarəti quraşdırma düyməsinin bağlanması deyil: quraşdırılmadan işləyən proqram da icra edilə bilər.

| Qayda əsası | Üstünlük | Məhdudiyyət | Laboratoriya seçimi |
| --- | --- | --- | --- |
| Nəşriyyatçı imzası | Yenilənmələrə uyğunlaşır | Etibarlı imzalı proqram da sui-istifadə edilə bilər | Məhsul və versiya sərhədi |
| Fayl heşi | Konkret faylı dəqiq tanıyır | Hər dəyişiklik heşi dəyişir | Sabit dərs aləti |
| Fayl yolu | İdarəsi sadədir | İstifadəçi həmin yola yaza bilərsə zəifdir | Yazılması qorunan kataloq |
| Skript qaydası | Dəstəklənən skript fayllarına siyasət tətbiq edir | Interpretatorun özünü və interaktiv kodu tam məhdudlaşdırmır | Skript və interpretator nəzarəti ayrıca sınanır |

Əvvəl audit rejimində qanuni iş izlənir, çatışmayan proqramlar müəyyən edilir, sonra bloklama tətbiq olunur. Kompüter elmləri dərsində tələbə özü kod yazırsa, bütün naməlum faylları qadağan edən qayda dərsi dayandırar; belə iş üçün ayrıca virtual mühit, qorunan əsas sistem və inzibati zonaya çıxışı olmayan laboratoriya seqmenti seçilə bilər. Nəzarət tədrisin funksiyasına uyğun qurulur.

Makrolar, brauzer əlavələri və skript interpretatorları ayrıca nəzərə alınır. İcazəli proqramın hücum üçün işlədilməsi mümkündür; siyahıda olmaq fəaliyyətin həmişə qanuni olması demək deyil. Tətbiq nəzarəti ilə EDR buna görə bir-birini tamamlayır.

### Qurğu firewall-u və məlumat nəzarəti

Qurğu firewall-u (host firewall) həmin cihazın gələn və çıxan bağlantılarını qaydalara görə süzür. Kampus sərhədindəki firewall eyni VLAN daxilindəki cihazlararası trafiki görməyə bilər; qurğu firewall-u yoluxmuş qonşudan girişə əlavə maneə yaradır. İcazə proqram, mənbə şəbəkə, port və profilə görə məhdudlaşdırılır; ev şəbəkəsi ilə universitet şəbəkəsinə eyni geniş istisnanı vermək risklidir.

Məlumat sızmasının qarşısının alınması (Data Loss Prevention, DLP) həssas məlumatın (məsələn, tələbələrin şəxsi məlumatları) USB-yə, şəxsi poçta, buluda, çap növbəsinə və başqa kanallara çıxmasını aşkarlaya və məhdudlaşdıra bilər. Qaydaya məlumat növləri və sənəd etiketləri daxil edilir. DLP-nin nəticəsi məlumatın təsnifatından asılıdır: yanlış etiket və tanınmayan format səhv qərar yarada bilər.

USB nəzarətində yalnız yaddaş daşıyıcısını düşünmək kifayət deyil: qurğu klaviatura və ya şəbəkə adapteri kimi tanına bilər. Naməlum USB-nin qoşulmasını qadağan etmək, təsdiqlənmiş daşıyıcıya yalnız oxuma icazəsi vermək və konkret cihaz sinfini məhdudlaşdırmaq ayrı siyasətlərdir. AutoRun-u söndürmək faydalıdır, amma istifadəçinin faylı özü açmasını və saxta klaviatura davranışını dayandırmır.

Təcrübə məlumatları üçün idarə olunan fayl ötürmə kanalı yaradılır. USB ölçü cihazı lazımdırsa, istisna həmin funksiyaya verilir, bütün daşıyıcılara açıq icazəyə çevrilmir. Seriya nömrəsi və cihaz identifikatoru faydalı uçot məlumatıdır, lakin güclü kriptoqrafik kimlik sübutu sayılmır.

## Windows üçün praktik baza

İlk addım cihazın dəstəklənən buraxılışını və iş rolunu müəyyən etməkdir. Sonra mərkəzi siyasətlə firewall, antivirus, disk şifrələməsi, audit, ekran kilidi və administrator qrupları sazlanır. İnternetdən gələn sənədlərin aktiv məzmunu məhdudlaşdırılır; lazım olmayan SMBv1 və uzaqdan giriş xidmətləri söndürülür. SMB-nin bütün versiyalarını düşünmədən bağlamaq isə qanuni fayl işini dayandıra bilər; hər dəyişiklik üçün asılılıq yoxlanır.

Aşağıdakı PowerShell əmrləri mövcud vəziyyəti **oxumaq** üçündür (bəziləri administrator səlahiyyəti və uyğun Windows komponenti tələb edir); siyasəti avtomatik düzəltmir, nəticələr təsdiqlənmiş baza ilə müqayisə edilir.

```powershell
Get-MpComputerStatus
Get-NetFirewallProfile
Get-BitLockerVolume
Confirm-SecureBootUEFI
Get-Tpm
Get-LocalGroupMember -SID 'S-1-5-32-544'
```

Son əmr daxili Administrators qrupunu dilə bağlı ad əvəzinə SID ilə seçir; siyahıda hər hesabın iş səbəbi olmalıdır. `Confirm-SecureBootUEFI` dəstəklənməyən platformada xəta verə bilər; xəta ilə `False` nəticəsi eyni deyil. `Get-BitLockerVolume` çıxışında yalnız şifrələmə faizi yox, qoruyucular və qorumanın aktivliyi də qiymətləndirilir. BitLocker qorumasının müvəqqəti dayandırılması şifrəli məlumatın silinməsi demək deyil, lakin açar mühafizəsini zəiflədə bilər.

Windows Credential Guard kimi mexanizmlər uyğun platformada bəzi giriş sirlərinin qorunmasını gücləndirir; aktivliyi bütün parol və sessiyaların oğurlana bilməyəcəyinə zəmanət deyil. Uzaqdan inzibati giriş yalnız idarəetmə şəbəkəsindən verilir, adi hesablar RDP hüququ almır. Təhlükəsizlik agentinin müdaxilədən qorunması açılır, xidmətin dayanması xəbərdarlıq yaradır.

## Linux sistemlərinin gücləndirilməsi

### Əvvəl müşahidə, sonra dəyişiklik

Linux-da vahid universal gücləndirmə skripti yoxdur: paket meneceri, xidmət adı və təhlükəsizlik modulu distributivə görə dəyişir. Əvvəl buraxılış, rol və işləyən xidmətlər müəyyən edilir. Kitabxananın veb kataloq serverində çap xidməti lazım olmaya bilər, çap serverində isə əsas işdir. Portun açıq görünməsi onun zəif olduğu demək deyil; lazım olub-olmaması və giriş sərhədi araşdırılır.

Aşağıdakı əmrlər vəziyyəti oxuyur (`ss` çıxışında proses adları üçün inzibati hüquq lazım ola bilər; İnternetə çıxmadan da yoxlamaq mümkündür).

```bash
cat /etc/os-release
uname -r
sudo ss -lntup
systemctl --type=service --state=running
systemctl list-unit-files --state=enabled
findmnt -o TARGET,SOURCE,FSTYPE,OPTIONS
sudo sshd -T
```

İşləyən xidmətlə avtomatik başlayan xidmət ayrı anlayışdır: xidmət indi işləyə, amma növbəti yüklənmədə başlamaya bilər, yaxud əksinə. Dinləyən ünvan diqqətlə oxunur: `127.0.0.1` yalnız lokal giriş, `0.0.0.0` bütün IPv4 interfeyslərində dinləmədir. IPv6 sazlaması ayrıca yoxlanır; yalnız IPv4 firewall qaydası ilə kifayətlənmək IPv6 üzərindən gözlənilməyən giriş saxlaya bilər.

Debian və Ubuntu ailəsində paket siyahısını yeniləmək ilə paketləri quraşdırmaq fərqlidir (paket yükləmək üçün təsdiqlənmiş repozitoriyaya əlaqə lazımdır); RHEL ailəsində paket əməliyyatları dnf ilə aparılır.

```bash
sudo apt update
apt list --upgradable
sudo apt upgrade
```

`apt update` yalnız indeksləri yeniləyir, yamağı quraşdırmır. Yenilənmədən sonra işləyən köhnə proses və köhnə nüvə yaddaşda qala bilər; sistem tələb etdikdə xidmət və ya cihaz yenidən başladılır, sonra çalışan nüvə və paket versiyaları yoxlanır.

### SSH və minimum xidmət

SSH üçün açar əsaslı giriş hazırlanır, ayrıca administrator hesabı və sudo seçilir. Aşağıdakı parça şərti kitabxana serverinin `/etc/ssh/sshd_config` siyasətinə nümunədir (hesab adı şərtidir). Açarla yeni giriş yoxlanmadan parol girişi bağlanmır, mövcud idarəetmə sessiyası açıq saxlanır və konsol çıxışı hazırlanır.

```text
PermitRootLogin no
PubkeyAuthentication yes
PasswordAuthentication no
KbdInteractiveAuthentication no
AllowUsers kitabxanaadmin
X11Forwarding no
```

Bu nümunə SSH üzərindən interaktiv ikinci amil istifadə etməyən server üçündür; PAM ilə interaktiv MFA tətbiq olunan mühitdə `KbdInteractiveAuthentication no` həmin mexanizmi də kəsə bilər. Include, Match blokları və sazlama üstünlükləri yoxlanır. Əvvəl `sudo sshd -t` ilə sintaksis, sonra `sudo sshd -T` ilə effektiv baza sazlaması oxunur; Match şərtləri varsa, uyğun bağlantı parametrləri ilə də qiymətləndirmə aparılır. Sintaksisin düzgünlüyü girişin işlədiyini sübut etmir.

Xidmətin yenidən yüklənməsi distributivdəki adına görə aparılır: Debian və Ubuntu-da ad çox vaxt `ssh`, RHEL ailəsində `sshd`. Dəyişiklikdən sonra ayrıca yeni bağlantı sınağı aparılır. İstifadə edilməyən çap xidməti həqiqətən lazımsızdırsa, məsələn, `sudo systemctl disable --now cups` ilə dayandırıla və avtomatik başlanması bağlana bilər; socket və başqa asılı vahidlərin onu yenidən başlada bilməsi ayrıca yoxlanır.

### Firewall, fayl hüquqları və məcburi nəzarət

Ubuntu-da UFW seçilibsə, aşağıdakı nümunə şərti serverdə IPv4 üzrə SSH-ni idarəetmə şəbəkəsi ilə məhdudlaşdırır. Mövcud qaydalar da yoxlanmalı, daha geniş SSH girişi verən icazələr konsol və ya alternativ inzibati giriş saxlanmaqla ləğv edilməlidir; standart daxilolma siyasətinin dəyişdirilməsi əvvəlki icazələri silmir. `192.0.2.0/24` sənədləşdirmə ünvanıdır (RFC 5737) və real idarəetmə prefiksi ilə əvəz edilməlidir; serverin həqiqi mənbə ünvanı, VPN və NAT yolu əvvəl yoxlanır. Nümunə yalnız IPv4 qaydasını göstərir; IPv6 və digər xidmətlər ayrıca qiymətləndirilir.

```bash
sudo ufw default deny incoming
sudo ufw default allow outgoing
sudo ufw allow from 192.0.2.0/24 to any port 22 proto tcp
sudo ufw enable
sudo ufw status verbose
```

İctimai veb xidməti varsa, onun HTTPS girişi də əvvəlcədən əlavə edilir. Çıxışa ümumi icazə nümunəni sadələşdirir; həssas serverdə DNS, vaxt, repozitoriya və tətbiq asılılıqlarına görə çıxış siyahısı daraldıla bilər. UFW və başqa qayda idarəetmə vasitələrini plansız qarışdırmaq gözlənilməyən nəticə yaradır; konteyner platformasının firewall qaydalarına təsiri də yoxlanır.

Fayl hüquqlarında xidmət hesabına yalnız lazım olan kataloq verilir. `chmod 777` ilə icazə problemini örtmək başqa istifadəçilərə yazma imkanı aça bilər. Şəxsi SSH kataloqu üçün `chmod 700 ~/.ssh`, təsdiqlənmiş açarlar faylı üçün `chmod 600 ~/.ssh/authorized_keys` tipik sazlamalardır; sahiblik də düzgün olmalıdır. sudo qaydası `visudo` ilə yoxlanır; istənilən əmri parolsuz işlədən geniş qayda minimum səlahiyyət prinsipini pozur.

SELinux və AppArmor məcburi giriş nəzarəti vasitələridir: adi fayl hüququndan sonra prosesin hansı resursa çata biləcəyini əlavə siyasətlə məhdudlaşdırırlar. LMS xidməti pozulsa belə, siyasət ona aid olmayan faylları oxumağı çətinləşdirə bilər. Tətbiq işləməyəndə mexanizmi tam söndürmək əvəzinə rədd qeydi araşdırılır və dar qayda hazırlanır. `noexec` montaj seçimi də hər cür kod icrasını dayandırmır: interpretator faylı oxuyub icra edə bilər.

## Mobil cihazlar, MDM və BYOD

Mobil cihazların idarə edilməsi (Mobile Device Management, MDM) qeydiyyata alınmış cihazlara ekran kilidi, şifrələmə, tətbiq və şəbəkə siyasəti və uzaqdan silmə tətbiq edir (nümunələr: Intune, Jamf). Vahid son qurğu idarəetməsi (Unified Endpoint Management, UEM) müxtəlif cihaz siniflərini bir idarəetmədə birləşdirir. Tətbiq idarəetməsi (Mobile Application Management, MAM) tətbiq və onun təşkilati məlumatına yönəlir. Bu anlayışlar eyni sərhədi idarə etmir.

Öz cihazını gətir (Bring Your Own Device, BYOD) siyasətində cihaz şəxsin mülkiyyətində qalır; universitet hansı məlumatı görəcəyini və hansı əməliyyatı edə biləcəyini əvvəlcədən açıqlayır. Android iş profili (Work Profile) və uyğun tətbiq konteynerləri şəxsi sahə ilə iş məlumatını ayırmağa kömək edir; iOS-da imkanlar qeydiyyat üsulundan və idarəetmə rejimindən asılıdır. İtən cihazda **seçici silmə** yalnız universitet məlumatlarını silir, şəxsi şəkillərə toxunmur.

| Model | İdarəetmə | Məlumat silinməsi | Universitet nümunəsi |
| --- | --- | --- | --- |
| Universitet cihazı | Razılaşdırılmış tam siyasət | Tam silmə mümkün ola bilər | İnzibati planşet |
| Şəxsi qeydiyyatlı cihaz | İş sahəsinə uyğun siyasət | Seçici silmə üstün tutulur | Əməkdaşın şəxsi telefonu |
| Qeydiyyatsız şəxsi cihaz | Məhdud veb və tətbiq girişi | Cihaza tam nəzarət yoxdur | Tələbənin LMS girişi |
| Ortaq cihaz | Sessiya və istifadəçi ayrılığı | Hər sessiyadan sonra təmizləmə | Kitabxana planşeti |

Şərti nümunə: əməkdaşın şəxsi telefonu itir. İş profili və MAM dəstəyi varsa, universitet məlumatının seçici silinməsi tələb edilir, hesab sessiyaları və sertifikatları ləğv olunur. Uzaqdan silmə cihaz şəbəkəyə çıxmayınca icra edilməyə bilər; əmrin konsolda yaradılması məlumatın artıq silindiyini göstərmir. Tam silmə şəxsi şəkilləri də itirə bildiyi üçün mülkiyyət və səlahiyyət sərhədi əvvəlcədən müəyyən edilir.

Mobil sistemin dəstək müddəti, təhlükəsizlik yenilənməsi və root və ya jailbreak əlamətləri giriş qərarına daxil edilə bilər, amma bu əlamətlərin aşkarlanması tam deyil. Etibarlı mağaza zərərli tətbiq riskini sıfırlamır; tətbiqin kontakt, mikrofon və fayl icazələri iş ehtiyacına görə məhdudlaşdırılır. Qayda təhsilə əsassız maneə yaratmamalıdır: uyğun şəxsi cihazı olmayan tələbə üçün universitet terminalı və ya məhdud veb giriş yolu saxlanılır.

Yataqxana Wi-Fi şəbəkəsinə qoşulma tələbə bazasına inzibati giriş vermir; şəxsi telefonlar və idarə olunan kompüterlər ayrı zonalarda yerləşdirilir. LMS-ə tələbə girişi ilə baza idarəetməsi fərqli siyasət tələb edir. Şəbəkəyə qoşulma hüququ, cihazın idarə olunması və tətbiqdə verilən səlahiyyət bir-birindən ayrılır.

## Loglar, monitorinq və mərkəzi idarəetmə

### Nəyi və niyə toplamaq lazımdır

Jurnal qeydi (log entry) sistemdə baş verən hadisənin saxlanılmış təsviridir; hadisə adi əməliyyat da ola bilər. **Xəbərdarlıq** aşkarlama qaydasının araşdırılmalı saydığı nəticədir. **İnsident** təhlükəsizliyi pozan və ya real təhdid edən vəziyyətdir. Administrator hesabının yaradılması planlı iş ola bilər; icazəsiz yaradılıb məlumat çıxarmaq üçün işlədilməsi insidentdir.

Toplama konkret suallardan başlanır: kim daxil oldu, hansı proses başladı, hansı səlahiyyət dəyişdi, qoruma niyə dayandı, məlumat hara getdi? Vaxt, cihaz identifikatoru, istifadəçi, əməl, nəticə və mənbə saxlanır. Bütün cihazların saatı sinxronlaşdırılır; hadisənin baş vermə vaxtı ilə mərkəzə çatma vaxtı ayrı ola bilər, gecikmə araşdırmada nəzərə alınır.

| Mənbə | Müşahidə | Yoxlama məqsədi |
| --- | --- | --- |
| Windows Security 4624, 4625 | Uğurlu və uğursuz giriş | Hesab və mənbə əlaqəsi |
| Windows Security 4688 | Proses yaradılması | Sənəddən başlayan icra |
| Windows Security 4732 | Lokal təhlükəsizlik qrupuna üzv əlavəsi | Administrator hüququnun verilməsi |
| Windows Security 1102 | Audit jurnalının təmizlənməsi | İzlərin itməsi |
| Windows System 7045 | Xidmət quraşdırılması | Qalıcı giriş və planlı dəyişiklik |
| Linux journald və auditd | Giriş, proses və siyasət hadisələri | Səlahiyyət və fayl dəyişiklikləri |
| EDR və MDM | Sensor, siyasət, təcrid vəziyyəti | Nəzarətin həqiqətən işləməsi |

Audit sazlanmasa, bəzi hadisələr yaranmır. Windows-da 4688 qeydində komanda sətrinin görünməsi ayrıca siyasət tələb edir. 7045 Security jurnalında deyil, System jurnalındadır. Linux-da `/var/log/auth.log` və `/var/log/secure` yolları distributivə və jurnal sazlamasına bağlıdır; `journalctl` yerli jurnalın oxunmasına kömək edir. auditd qaydaları konkret fayl və səlahiyyət dəyişikliklərinə görə hazırlanır; bütün diskə düşünülməmiş audit böyük yük yarada bilər.

```bash
journalctl -u ssh --since today
journalctl -p warning --since today
sudo ausearch -k identity_changes
```

SSH xidmət vahidinin adı uyğunlaşdırılır; vaxt aralığı və hesab identifikatorları araşdırılan vəziyyətə görə seçilir. `identity_changes` əvvəlcədən qaydaya verilmiş açardır; belə qayda yoxdursa, nəticənin boş olması hadisənin olmadığını sübut etmir. Məsələn, `/etc/passwd` dəyişmələrinin izlənməsi hesab yaradılmasını göstərməyə kömək edə bilər; real istifadəçi həyat dövründə `/etc/shadow` və qrup faylları da nəzərə alınır.

### Əlaqələndirmə və mənbənin sağlamlığı

Aşağıdakı qeydlər real məhsul formatı deyil, sahələri göstərən şərti normallaşdırılmış tədris nümunəsidir (vaxtlar, cihaz, hesab və ünvanlar şərtidir); qeydin özü hücum barədə son qərar vermir.

```text
time=2026-11-08T08:10:00Z host=lab-17 user=telebe17 event=process_start parent=winword.exe child=powershell.exe time_source=endpoint result=success

time=2026-11-08T08:10:08Z host=lab-17 user=telebe17 event=network_connect dst=198.51.100.24 dst_port=443 result=allowed

time=2026-11-08T08:11:00Z host=lab-17 event=protection_service_stop change_ticket=none
```

Sənəd tətbiqindən interpretator başlanması, ardınca xarici bağlantı və qoruma xidmətinin dayanması birlikdə daha ciddi siqnaldır.

MITRE ATT&CK v19 (28 aprel 2026) Enterprise Defense Evasion taktikasını Stealth və Defense Impairment üzrə ayırıb. Windows hadisə jurnalının təmizlənməsi T1685.005 kimi göstərilir; köhnə mənbələrdə T1070.001 nömrəsi qalır. Qayda sənədində istifadə olunan versiya yazılır. Təsnifat araşdırmanı təşkil edir, hadisəni özbaşına zərərli elan etmir.

Qeydlər mərkəzi SIEM-ə qorunan kanalla göndərilir, ötürmə dayananda buferlənir və qəbul tərəfdə silinməkdən qorunur. TLS üzərindən syslog üçün TCP 6514 istifadə olunur (RFC 5425). Parollar və tokenlər komanda sətrində görünə bildiyindən loglara giriş də məhdudlaşdırılır. Susan agent və uzun müddət görünməyən noutbuk ayrıca xəbərdarlıq tələb edir; sakit konsol mütləq təhlükəsiz mühit demək deyil.

## İnsidentə cavab və yoxlanmış bərpa

İnsidentə hazırlıq əvvəlcədən məsul şəxsləri, əlaqə kanalını, təcrid üsulunu və sübut saxlamasını müəyyən edir. NIST SP 800-61 Rev. 3 (aprel 2025) cavab işini NIST CSF 2.0 ilə əlaqələndirir. CSF 2.0-nin altı funksiyası: Govern, Identify, Protect, Detect, Respond, Recover.

Şərti laboratoriya hadisəsi: EDR çoxlu faylın dəyişməsini göstərir. Əvvəl riskli cihaz şəbəkədən təcrid edilir, ümumi fayl qovluğuna yazma imkanı dayandırılır. EDR təcridi bəzi məhsullarda idarəetmə əlaqəsini açıq saxlayır, lakin konkret davranış yoxlanmalıdır. Cihazın enerjisini dərhal kəsmək yaddaşdakı sübutu itirə bilər; aktiv zərərin davam etməsi isə başqa məlumatları poza bilər. Qərar fəaliyyətin sürətinə və sübut ehtiyacına görə cavab planı əsasında verilir.

1. **Təcrid və əhatə.** Eyni hesab, sənəd və idarəetmə ünvanı ilə bağlı başqa cihazlar axtarılır.
2. **Sübut.** Loglar, proses məlumatı və lazım olduqda yaddaş və disk surəti səlahiyyətli mütəxəssis tərəfindən götürülür; vaxt və əməliyyatlar yazılır.
3. **Hesablar.** Etibarlı cihazdan parol dəyişir, sessiyalar və riskli tokenlər ləğv edilir, sertifikatlar qiymətləndirilir.
4. **İlkin səbəb.** Zəif xidmət, təhlükəli sazlama və qalıcı giriş mexanizmi müəyyən edilir.
5. **Bərpa.** Sistem təmiz mənbədən qurulur və ya yoxlanılmış nüsxədən bərpa olunur; sonra nəzarətlər və xidmət yoxlanır.

Şübhəli faylı silmək hücumçunun yaratdığı hesabı, planlı tapşırığı və oğurladığı sessiyanı aradan qaldırmır. Etibarı ciddi pozulmuş sistemin təsdiqlənmiş quraşdırma obrazından yenidən qurulması daha aydın etibar başlanğıcı verir. Bərpa edilən sənədlər də yoxlanır: təhlükəli makronu yenidən istifadəçi profilinə qaytarmaq təkrar yoluxma yarada bilər. İstismar edilmiş zəiflik aradan qalxmadan cihaz əvvəlki zonaya qaytarılmır.

| Sahə | Tələb olunan nəticə | Sübut |
| --- | --- | --- |
| Sistem | Dəstəklənən və yamanmış quruluş | Versiya və skan nəticəsi |
| Hesab | Riskli giriş ləğv edilib | Sessiya və açar dəyişiklikləri |
| Müdafiə | Firewall, audit və sensor işləyir | Mərkəzi sınaq hadisəsi |
| Məlumat | Düzgün və zərərsiz nüsxə | Tamlıq və tətbiq yoxlaması |
| Xidmət | Qanuni iş bərpa olunub | LMS və ya laboratoriya sınağı |
| İzləmə | Təkrar əlamət axtarılır | Gücləndirilmiş monitorinq |

Ehtiyat nüsxə əsas sistemlə eyni hesabla silinə bilirsə, hücumçu hər ikisini məhv edə bilər. Ayrı səlahiyyət, oflayn və ya dəyişdirilməz saxlanma, şifrələmə və bərpa sınaqları birlikdə planlaşdırılır. **RPO** qəbul edilən məlumat itkisi intervalını, **RTO** xidmətin bərpası üçün hədəf vaxtı göstərir. Şərti LMS üçün RPO dörd saat, RTO altı saat seçilibsə, nüsxələmə tezliyi və real sınaq həmin hədəflə uyğun olmalıdır; rəqəmlər bu nümunəyə aiddir, universal norma deyil.

Bərpa sınağı ayrıca mühitdə istifadəçinin işini tamamlamalıdır: tələbə daxil olur, dərs materialını açır, tapşırıq göndərir. Yalnız faylın arxivdən çıxması LMS-in bərpasını sübut etmir.

## Aktiv şəbəkə avadanlığı və onun gücləndirilməsi

### Dəqiq təsnifat

Aktiv şəbəkə avadanlığı xarici enerjidən istifadə edərək rabitə siqnalını yaradan, qəbul edib emal edən, bərpa edən, çevirən və ya məlumat ötürülməsini idarə edən qurğudur. Kommutator, marşrutizator, giriş nöqtəsi, media çevirici və ötürücü modul bu qrupa daxildir. Təkrarlayıcı siqnalı bərpa edir, gücləndirici enerji hesabına gücləndirir; hər ikisi aktivdir. Yalnız paket başlığını oxuyan qurğuları aktiv saymaq düzgün deyil.

Passiv rabitə komponenti xarici enerji hesabına siqnal yaratmadan və bərpa etmədən onu fiziki yolla ötürür, birləşdirir və ya bölür: kabel, konnektor, passiv optik bölücü, patch panel. Rəf və kabel meneceri siqnal yolunun özü deyil, fiziki dəstək infrastrukturudur. Sadə PDU elektrik enerjisini paylayır; şəbəkə interfeysi olan idarə olunan PDU isə ayrıca qorunan aktiv idarəetmə sistemi sayılır.

| Cihaz | Funksiya | Əsas risk | Gücləndirmə |
| --- | --- | --- | --- |
| Kommutator | Kadrları portlara ötürür | İcazəsiz port, idarəetmə itkisi | 802.1X, port siyasəti, idarə zonası |
| Marşrutizator | IP şəbəkələri arasında yol seçir | Səhv marşrut, açıq inzibati giriş | ACL, təhlükəsiz idarəetmə |
| Giriş nöqtəsi | Simsiz cihazı şəbəkəyə bağlayır | Saxta giriş, ortaq sirr | WPA3 və ya uyğun WPA2-Enterprise |
| Media çevirici | Siqnal mühitini çevirir | Uyğunsuzluq, fiziki müdaxilə | Etibarlı model, kilidli yerləşdirmə |
| SFP və SFP+ | Elektrik və optik ötürmə interfeysi | Yanlış modul, kanal itkisi | Uyğunluq və optik büdcə |
| PoE injektor | Kabelə enerji verir | Güc uyğunsuzluğu, dayanma | Standart və güc büdcəsi |
| Çap serveri | Çap növbəsini idarə edir | Sənəd sızması, xidmət zəifliyi | İcazə, yamaq, ayrıca zona |

### Kommutator, marşrutizator və giriş nöqtəsi

Adi ikinci səviyyə kommutatoru mənbə MAC ünvanından port uyğunluğu öyrənir, təyinat MAC ünvanına görə kadrı ötürür. Məlum unicast uyğun porta gedir; naməlum unicast və broadcast VLAN daxilində uyğun digər portlara yayıla bilər, ona görə kommutatorun hər trafiki yalnız bir porta ötürdüyünü demək dəqiq deyil. Üçüncü səviyyə funksiyalı kommutator IP marşrutlaşdırması da edə bilər. VLAN ayırması özbaşına şifrələmə vermir.

Laboratoriyanın istifadəsiz portları söndürülür, tələbə portları tələb olunan VLAN-a bağlanır, avtomatik trunk yaranması məhdudlaşdırılır. IEEE 802.1X port əsaslı şəbəkə giriş nəzarətidir: cihaz və ya istifadəçi autentifikasiya olunur, amma bütün tətbiq səlahiyyətləri verilmir. Uyğun platformada DHCP snooping, Dynamic ARP Inspection və BPDU Guard ayrıca sınaqdan keçirilir; etibarlı portun səhv seçilməsi qanuni əlaqəni kəsə və ya müdafiədə boşluq aça bilər.

Marşrutizator IP prefikslərinə və marşrut siyasətinə görə paketləri şəbəkələr arasında ötürür. OSPF təşkilat daxilində, BGP avtonom sistemlər arasında və uyğun daxili arxitekturalarda yol məlumatı mübadiləsi üçün istifadə olunur; hər kampus bağlantısında hamısı lazım deyil. Statik marşrut, ACL, VPN və xidmət keyfiyyəti imkanları platformaya görə seçilir. NAT ünvan çevirməsidir, tam təhlükəsizlik siyasəti sayılmır.

İdarəetmə planı istifadəçi məlumatı planından ayrılır: SSH və HTTPS yalnız idarəetmə zonasından açılır, Telnet və qorunmayan HTTP söndürülür. Sadə şəbəkə idarəetməsi üçün SNMP işlənirsə, mümkün olduqda SNMPv3-də autentifikasiya və məxfilik rejimi seçilir; v3 adının özü şifrələmənin aktiv olduğunu göstərmir. Fərdi administrator hesabları və autentifikasiya, avtorizasiya, uçot (AAA) qeydləri ortaq paroldan daha aydın məsuliyyət verir.

Giriş nöqtəsi (access point, AP) simsiz cihazları paylama şəbəkəsinə bağlayır; məişət qurğusunda AP, marşrutizator və kommutator bir korpusda ola bilər. Əməkdaş şəbəkəsində cihaz uyğunluğu nəzərə alınaraq WPA3-Enterprise, lazım olduqda WPA2-Enterprise tətbiq edilir. EAP-TLS sertifikatlarla qarşılıqlı yoxlama üçün istifadə oluna bilər. Müştərinin autentifikasiya serverinin sertifikatını yoxlamaması saxta giriş nöqtəsinə etibar riskini artırır; SSID adının tanış olması təhlükəsizlik sübutu deyil.

Yataqxana qonaq şəbəkəsi inzibati sistemlərdən ayrılır, müştərilərarası əlaqə ehtiyaca görə məhdudlaşdırılır, WPS söndürülür. AP firmware-i və idarəetmə hesabları yenilənir. RADIUS mühiti də yamaq prosesinə daxildir: Blast-RADIUS (CVE-2024-3596) RADIUS protokolunun bəzi istifadələrində risk göstərib; uyğun istehsalçı düzəlişi və protokol sərtləşdirməsi tətbiq edilir. Wi-Fi şifrələməsi son qurğunun zərərli proqramını və tətbiq səlahiyyətini həll etmir.

### Çeviricilər, modullar, enerji və çap

Media çevirici mis Ethernet ilə optik mühit arasında siqnalı çevirir. Çevirici şəffaf kabel deyil: firmware və idarəetmə interfeysi varsa qorunmalıdır; idarə olunmayan modeldə fiziki giriş, enerji və kabel uyğunluğu əsas yoxlama nöqtələridir.

SFP dəyişdirilə bilən yığcam ötürücü modul ailəsidir. Tipik Gigabit Ethernet üçün SFP, 10 Gigabit Ethernet üçün SFP+ işlədilir. Eyni görünən yuva hər sürət və modulun uyğun olduğu demək deyil: modulun standartı, dalğa uzunluğu, lif növü, məsafəsi və cihaz dəstəyi tutuşdurulur. İşləyən cihazda dəyişmə imkanı əlaqənin kəsilməyəcəyinə zəmanət vermir; modul çıxarılan kanal dayanır.

PoE injektor məlumat kabelinə elektrik enerjisi əlavə edir. IEEE 802.3af, 802.3at və 802.3bt ailələri müxtəlif güc imkanları verir. Standarta uyğun mənbə cihazın uyğunluğunu müəyyən edir; bazarda passiv PoE deyilən sadə enerji tətbiqi bu mexanizmlə eyniləşdirilmir. İnjektor enerji verən aktiv infrastruktur elementidir, amma mütləq paketləri kommutasiya etmir. AP və kameraların ümumi enerji büdcəsi hesablanır, ehtiyat enerji ehtiyacı qiymətləndirilir.

Çap serveri ayrıca cihaz və ya serverdə proqram ola bilər: növbəni qəbul edir, istifadəçini və printer icazəsini yoxlayır, işi printerə göndərir. Tələbə bazasından çıxan sənəd növbədə və printer yaddaşında qala bilər. Yamaq, qorunan idarəetmə, çapı istifadəçi yanında buraxma və saxlama müddəti siyasəti bu riski azaldır. Çap lazım olmayan serverdə spooler xidmətinin işləməsinə ehtiyac ayrıca əsaslandırılır.

## Passiv komponentlər və fiziki mühafizə

### Mis və optik ötürmə mühiti

UTP ekranlaşdırılmamış bükülmüş cüt kabeldir; cütlərin bükülməsi elektromaqnit təsirin və cütlərarası çarpaz təsirin azaldılmasına kömək edir. STP ifadəsi ekranlı bükülmüş cütlər üçün ümumi işlənir, dəqiq ekran quruluşu ayrıca işarələnir. Ekranlaşdırmanın faydası düzgün quraşdırma və torpaqlamadan asılıdır; kabelin yalnız qalın və ya ekranlı olması onun daha təhlükəsiz olduğunu sübut etmir.

Cat5e üzrə düzgün qurulmuş **100 metrlik** kanal 1000BASE-T üçün istifadə edilə bilər. Bu məsafə adətən daimi xətt və patch kordlar daxil olan kanal üçündür; hər hissəyə ayrıca 100 metr vermək olmaz. Cat6 və Cat6a fərqli ötürmə tələblərini ödəyir; sürət tək kateqoriya adı ilə seçilmir, məsafə və standart birlikdə yoxlanır. Kanal testi cütlərin düzülüşünü, itki və çarpaz təsiri qiymətləndirir.

Optik lifin nüvəsi və onu əhatə edən optik qabığı işığı istiqamətləndirən dalğaötürücü quruluş yaradır; xarici örtük mexaniki mühafizə üçündür. Tək rejimli lif seçilmiş dalğa uzunluğunda bir əsas yayılma rejimi üçün, çox rejimli lif çoxsaylı rejimlər üçün nəzərdə tutulur; tək rejim işığın sadəcə bir istiqamətə getməsi demək deyil.

| Meyar | UTP | Ekranlı mis | Optik lif |
| --- | --- | --- | --- |
| Siqnal | Elektrik | Elektrik | İşıq |
| Elektromaqnit təsir | Həssasdır | Düzgün ekranla azalır | Optik siqnal təsirlənmir |
| Enerji ötürülməsi | PoE mümkündür | PoE mümkündür | Adi liflə PoE ötürülmür |
| Mexaniki risk | Əzilmə, cüt pozuntusu | Ekran və torpaqlama qüsuru | Əyilmə, qırılma, çirkli uc |
| Məxfilik | Şifrələmə tələb olunur | Şifrələmə tələb olunur | Dinləmə mümkündür, şifrələmə tələb olunur |
| Universitet istifadəsi | Otaq bağlantısı | Müdaxiləli texniki mühit | Binalararası və magistral xətt |

Optik kanal itkisiz deyil: lif, birləşmə, adapter və əyilmə zəifləmə yaradır; qəbul olunan güc ötürücünün və qəbuledicinin optik büdcəsinə uyğun olmalıdır. Şərti kampus xəttində ümumi büdcə 8 dB, hesablanan itki 5 dB-dirsə, ehtiyat 3 dB-dir (tədris nümunəsidir, konkret modul spesifikasiyası deyil).

Lifi bölücü və ya fiziki müdaxilə ilə dinləmək mümkündür; elektromaqnit müdaxiləyə davamlılıq məxfiliyə zəmanət deyil. Binalar arasında tələbə məlumatı ötürülürsə, uyğun şifrələmə tətbiq olunur. Birbaşa optik porta və ya lifin ucuna baxılmır, lazer mənbəyi görünməyə bilər; ölçmə və təmizləmə uyğun alətlə, enerji və təhlükəsizlik qaydalarına əməl etməklə aparılır.

### Birləşdiricilər və təşkilat elementləri

Patch kordun hər iki ucunda, pigtail-in isə adətən bir ucunda konnektor olur; pigtail-in digər ucu əsas liflə birləşdirilir. Optik patch kordla mis patch kord eyni kabel deyil. Mis Ethernet-də gündəlik RJ45 adlandırılan 8P8C modul konnektoru işlənir; RJ45 və 8P8C adları praktikada qarışdırılsa da, qeydiyyatlı jack adı ilə fiziki kontakt quruluşu eyni anlayış deyil. Bunlar LC və SC kimi optik konnektorlar deyil. Type G və BS 1363 isə elektrik fişi və rozetkası ilə bağlıdır.

| Element | Quruluş və funksiya | Tipik istifadə | Yoxlama |
| --- | --- | --- | --- |
| LC | Kiçik optik konnektor | Sıx portlu avadanlıq | Lif və cilalama uyğunluğu |
| SC | LC-dən iri, itələmə ilə qoşulur | Optik paylama | Təmizlik və oturma |
| FC | Yivli optik bağlantı | Ölçmə və sabit bağlantılar | Mexaniki sıxlıq |
| ST | Süngü tipli optik bağlantı | Köhnə kampus xətləri də daxil | Uyğun lif və adapter |
| MT-RJ | İki lifli yığcam konnektor | Uyğun optik sistem | Pin və polarite |
| 8P8C | Səkkiz mövqe və kontakt | Mis Ethernet | Cüt düzülüşü və kateqoriya |
| Adapter paneli | Adapterləri yerləşdirir | Optik xəttin sonlandırılması | Etiket və mexaniki bərkitmə |
| Patch panel | Xətləri təşkil edir | Mis və ya optik paylama | Port xəritəsi və test |

Konnektorun forması tək və ya çox rejimli lifə yeganə işarə deyil; LC və SC hər ikisində işlənə bilər. Adapter iki uyğun konnektoru dəqiq hizalayır. LC-LC və SC-SC eyni formalı, LC-SC kimi hibrid adapterlər fərqli formalı ucları birləşdirə bilər, amma dalğa uzunluğunu və lif rejimini çevirmir. UPC və APC cilalama növlərinin yanlış birləşdirilməsi itki və zədələnmə yarada bilər.

LIU qutusu liflərin sonlandırılmasını, birləşmələrin və pigtail ehtiyatının yerləşdirilməsini təşkil edir. Lif birləşmə korpusu (joint enclosure) birləşmələri mühitdən və mexaniki zədədən qoruyur; adi şəbəkə şkafı ilə eyniləşdirilmir. Adapter paneli konnektor yuvalarını saxlayır, çarpaz bağlantı paneli xətlər arasında fiziki əlaqənin dəyişdirilməsini asanlaşdırır.

Şəbəkə rəfi avadanlığı yerləşdirən konstruksiyadır. Geniş yayılmış **19 düymlük** standart montaj ölçüsüdür, şkafın xarici eninin 19 düym olması demək deyil. Hündürlük U ilə ölçülür; **1U = 44,45 mm**. 24U, 36U və 42U müxtəlif yerləşdirmə tutumlarını göstərir. Kilid, yan panellərin mühafizəsi, havalandırma, enerji və kabel yolu birlikdə planlaşdırılır; qapı kilidli olsa da, arxadakı açıq panel fiziki giriş verə bilər.

Şaquli və üfüqi kabel menecerləri kabelləri ayırır, əyilməni və dartını azaldır, portlara çıxışı təşkil edir. Üz qapağı (face plate) divar jack-larını saxlayır və sonlandırmanı qoruyur. Jack kabelin rozetka hissəsidir, patch panel isə çoxsaylı sonlandırmanı bir yerdə təşkil edir.

### Fiziki hücum və əlçatanlıq

Şərti nümunə: açıq auditoriyadakı port inzibati VLAN-a bağlanıb; heç bir kabel zəifliyi olmadan həmin portdan icazəsiz giriş yarana bilər. İstifadəsiz portun bağlanması, autentifikasiya və düzgün port xəritəsi riski azaldır. Başqa halda texnik səhv etiketə görə ehtiyat nüsxə serverinin kabelini çıxarır; dəqiq etiketləmə və dəyişiklik qeydiyyatı əlçatanlığı qoruyur.

PDU rəfdə elektrik enerjisini çıxışlar arasında paylayır; paket, trafik və marşrut paylamır. UPS elektrik kəsilməsində məhdud müddət enerji verir, PDU isə bu funksiyanı mütləq daşımır. İdarə olunan PDU-da uzaqdan çıxış söndürmək mümkün olduğundan hesabın ələ keçirilməsi serverləri dayandıra bilər; onun firmware-i, HTTPS və SSH girişi, logları və idarəetmə zonası digər aktiv idarəetmə qurğuları kimi qorunur.

Kabellərin keçdiyi sahələr, şkaf açarları və kənar podratçıların girişi nəzarətdə saxlanır. İki ehtiyat bağlantı eyni kabel kanalından keçirsə, bir fiziki zədə hər ikisini kəsə bilər; ayrı yol və enerji asılılıqları yoxlanır.

## IoT və laboratoriya avadanlığının mühafizəsi

Əşyaların İnterneti (Internet of Things, IoT) cihazları sensor, kamera, ağıllı lövhə və idarəedici kimi funksiyalar daşıyır; kamera görüntüsü, otaq doluluğu və təcrübə nəticələri bu cihazlardan gələ bilər. Adi EDR agenti dəstəklənməyəndə nəzarət şəbəkə sərhədinə, hesab idarəsinə və firmware uçotuna keçir. Agentin olmaması cihazın təhlükəsizlik məsuliyyətini ləğv etmir.

Satınalma zamanı dəstək müddəti, imzalanmış yenilənmə, standart parolun dəyişməsi, lokal idarəetmə və məlumatın hara göndərilməsi soruşulur. Bulud xidmətinə bağlı cihaz üçün internet kəsiləndə hansı funksiyanın dayanacağı müəyyən edilir. Naməlum xidmətə avtomatik əlaqə laboratoriya məlumatını kampusdan çıxara bilər; istifadə olunmayan uzaqdan dəstək və avtomatik port açma funksiyaları məhdudlaşdırılır.

| Problem | Tədbir | Qalan məhdudiyyət |
| --- | --- | --- |
| Standart hesab | Fərqli sirr, lazımsız hesabın bağlanması | Daxili gizli hesab riski araşdırılır |
| Yamaq yoxdur | Ayrıca zona, çıxışın daraldılması | Zəiflik cihazda qalır |
| Zəif protokol | Vasitəçi və qorunan tunel | Vasitəçiyə qədərki hissə həssas qala bilər |
| Log zəifdir | Kommutator və trafik müşahidəsi | Daxili proses görünmür |
| Dəstək bitib | Müddətli istisna, əvəzləmə | Tam texniki düzəliş olmaya bilər |
| Məlumat saxlanır | İxrac, təmizləmə və utilizasiya qaydası | Silinmənin təsdiqi tələb olunur |

Şərti kimya laboratoriyasının ölçü cihazı yalnız köhnə idarəetmə kompüteri ilə işləyir. Cihaz və kompüter ayrıca VLAN-a yerləşdirilir, tələbə bazasına yol verilmir. Nəticə yalnız təsdiqlənmiş vasitəçi ilə çıxarılır, vasitəçidə fayl yoxlaması aparılır. Məlumat mənbəyi və bütövlüyü də yoxlanır: zərərli fayl aşkarlanmasa belə, ölçmə nəticəsi dəyişdirilmiş ola bilər. Avtomatik sıfırlama cihazın kalibrləmə və təcrübə məlumatını silməməlidir.

Laboratoriya sisteminə aktiv zəiflik skanı göndərməzdən əvvəl istehsalçı və laboratoriya məsulu ilə uyğunluq müəyyən edilir: bəzi cihazlar gözlənilməyən sorğuya dayanıqsız cavab verə bilər. Passiv trafik müşahidəsi ilkin uçot üçün daha münasib ola bilər, amma bütün zəiflikləri aşkar etmir.

Cihaz istifadədən çıxanda yaddaş, konfiqurasiya, Wi-Fi sirri, sertifikat və bulud hesabı əlaqəsi təmizlənir. Zavod sazlamasına qayıtmağın bütün modellərdə etibarlı silmə verdiyi fərz edilmir; daşıyıcının xüsusiyyətinə uyğun silmə və ya məhvetmə üsulu seçilir. Uçotda çıxarılma ilə bağlı sübut saxlanır, sertifikat və idarəetmə qeydiyyatı ləğv edilir.

## Zero Trust və universitet laboratoriyasının layihəsi

### Giriş qərarında cihazın vəziyyəti

Zero Trust yanaşması şəbəkə daxilində olmağı avtomatik etibar üçün kifayət saymır. NIST SP 800-207 resurs girişində açıq yoxlama və ən az səlahiyyətli qərara əsaslanan arxitekturanı təsvir edir. İstifadəçinin kimliyi, cihazın vəziyyəti və tələb olunan resursun həssaslığı birlikdə qiymətləndirilir. Bu, konkret bir agentin və ya VPN-in adı deyil, qərarların qurulma qaydasıdır.

LMS-in açıq dərs elanını oxumaqla tələbə bazasını idarə etmək eyni giriş tələbi daşımır: birincisi uyğun veb girişlə mümkün ola bilər, ikincisi idarə olunan cihaz, güclü autentifikasiya, məhdud inzibati rol və əlavə audit tələb edə bilər. Cihaz yenilənməyibsə, ona bütün şəbəkəni açmaq əvəzinə yenilənmə xidməti və dəstək portalı üçün məhdud yol verilə bilər.

Cihazın uyğunluğu son alınan məlumat əsasında qiymətləndirilir: bir ay əvvəl sağlam görünən noutbuk bu gün eyni vəziyyətdə olmaya bilər. Sensorun son əlaqə vaxtı və ölçmə etibarlılığı qərara daxildir. Uyğunluq siqnalı mümkün olduqda cihaz sertifikatı və qorunan qeydiyyatla əlaqələndirilir. Ekrandakı təsdiq işarəsi istifadəçinin geniş tətbiq hüququ almasına səbəb olmamalıdır.

![figure](m11-4.png)

*Şəkil 4. Şərti universitetdə cihaz qrupları (əməkdaş noutbuku, laboratoriya, BYOD, IoT və printer) giriş siyasətinə (NAC, MDM) gedir; nəticə tam giriş, dərs resursları, məhdud veb və ya təcrid VLAN-dır. Monitorinq qeydləri ayrı axınla SIEM-ə gedir.*

### Laboratoriyanın mərhələli dəyişdirilməsi

Şərti laboratoriyada 40 kompüter var: tələbələr administrator kimi işləyir, proqramları sərbəst quraşdırır, USB nəzarətsizdir, inzibati sistemlərə şəbəkə yolu açıqdır. İlk iş proqram və cihaz uçotudur: dərs proqramlarının siyahısı hazırlanır, quraşdırma tələbi ilə gündəlik icra ehtiyacı ayrılır. Tələbələrin yalnız bir aləti işlətmək üçün administrator hüququ alması əvəzinə fayl və xidmət icazəsi düzəldilə bilər.

Əvvəl bir neçə təmsilçi kompüterdə baza sınanır: adi hesablar, təsdiqlənmiş paketlər, firewall, tətbiq nəzarəti, audit və EDR. Tələbə proqram yazırsa, həmin dərs üçün ayrılmış virtual mühit verilir. Müvəqqəti inzibati icazə konkret işə və müddətə bağlanır. Təmiz obrazdan bərpa dərs arası dəyişiklikləri azaldır, lakin tələbə işləri əvvəl təsdiqlənmiş saxlanma yerinə ötürülməlidir.

Laboratoriya VLAN-ından yalnız tələb olunan LMS, DNS, vaxt, yenilənmə və fayl xidmətlərinə giriş verilir; tələbə bazasının inzibati interfeysi açılmır. Eyni laboratoriyada qurğu firewall-u və lazım olduqda port izolyasiyası qonşulararası riski azaldır. VLAN adının mövcudluğu kifayət deyil: zonalararası qaydalar və faktiki əlaqə yolları, digər idarəetmə interfeysləri də yoxlanır.

USB tədris ehtiyacına görə siniflərə ayrılır, alternativ fayl ötürmə kanalı yaradılır. Yenilənmələr qruplarla yayılır, imtahan öncəsi sabit quruluş yoxlanır. Təhlükəsizlik sınaqları zərərsiz hadisələrlə aparılır: adi istifadəçi inzibati qovluğa yaza bilmirmi, təsdiqlənməmiş proqram bloklanırmı, agentin susması xəbərdarlıq yaradırmı? Bərpa sınağı tələbənin həqiqi dərs işinin tamamlanmasını da əhatə edir.

## Effektivliyin ölçülməsi və qəbul meyarları

Proqram quraşdırma sayı nəzarətin işləməsini göstərmir; göstəricinin məxrəci, ölçmə anı və istisnaları müəyyən edilir. Şərti nümunə: uçotda 200 cihaz, vaxtında yamaqlanan 180 cihaz varsa, pay 90 faizdir. Skan daha 20 idarə olunmayan cihaz tapıbsa və hamısı eyni əhatəyə daxildirsə, ümumi görünüş 180/220, yəni təxminən **81,8 faiz** olur. Uçotun tamlığı yamaq göstəricisinin mənasını dəyişir.

Konspektin effektivlik göstəriciləri: yamanmış cihazların faizi, uçotdan kənar cihazların sayı, artıq admin hüquqlarının sayı, xəbərdarlığa reaksiya vaxtı, bərpa testlərinin nəticəsi.

| Göstərici | Hesab və ya sübut | Təfsir məhdudiyyəti |
| --- | --- | --- |
| Vaxtında yamaqlanma | Müddətə uyğun cihazlar bölünsün əhatə | Tək uğurlu paket sayı kifayət deyil |
| İdarə olunmayan cihaz | Əhatədə olub tələb olunan idarəetməyə daxil edilməmiş cihazların sayı | Aşkarlama əhatəsi nəzərə alınır |
| Artıq administrator | Əsaslandırılmamış hüquqların sayı | İstisna müddəti ayrıca yoxlanır |
| Sensor sağlamlığı | Vaxtında əlaqəli sensorların payı | Quraşdırılma sayı ilə qarışdırılmır |
| Cavab müddəti | Xəbərdarlıqdan təsdiqlənmiş tədbirə vaxt | Başlanğıc və son hadisə eyni seçilir |
| Bərpa uğuru | Qəbul meyarını keçən sınaqların payı | Faylın açılması tam xidmət deyil |
| Baza uyğunluğu | Keçilən tətbiq olunan yoxlamalar | Tətbiq olunmayan tələb ayrılır |

Orta cavab müddəti bir uzun hadisəni gizlədə bilər: median, ən uzun müddət və işdənkənar saatlardakı nəticələr də araşdırılır. Laboratoriya ilə LMS serverinin sınağı fərqlidir: birində dərs proqramının işləməsi, digərində giriş, məlumat yazılması və bərpa əsasdır.

Uyğunluq skanı sazlamanı yoxlayır, zəiflik skanı məlum zəifliyi axtarır, nəzarət sınağı isə tədbirin gözlənilən davranışını təsdiqləyir; bunlar eyni nəticə deyil. Baza tam uyğun ola, amma proqramda yamaqlanmamış zəiflik qala bilər; EDR işləyə, lakin xəbərdarlığı qarşılayan şəxs olmaya bilər. Qəbul zamanı texniki vəziyyət, iş funksiyası və cavab prosesi birlikdə yoxlanır.

Sınaqlar səlahiyyətli mühitdə, əvvəlcədən razılaşdırılmış sərhəddə aparılır. İstehsalat bazasına zərərli fayl buraxmaq və ya təhlükəsizlik xidmətlərini xəbərsiz söndürmək ölçmə üsulu seçilmir; zərərsiz sınaq hadisəsi, məhdud pilot və ayrıca bərpa mühiti kifayət edən sübutu verə bilər. Hər tapıntının məsulu və bağlanma sübutu yazılır; növbəti yoxlama həmin düzəlişin qalıcı olub-olmadığını ölçür.

:::note Köhnə slaydlarla fərq
Konspekt qeyd edir: mövzunun əsas hissəsi düzgündür, səhvlər əsasən əlavə olunmuş "aktiv və passiv şəbəkə avadanlığı" hissəsindədir. Düzəlişlər: təkrarlayıcı və siqnal gücləndiricisi passiv yox, **aktiv** avadanlıqdır; RJ45 mis kabel konnektorudur, optik deyil; PDU trafiki yox, elektrik enerjisini paylayır; 10 Gbit/s üçün SFP yox, SFP+ işlədilir; optik kabel itkisiz deyil və dinlənə bilər, şifrələməni əvəz etmir; simsiz AP nümunəsində WPA2 ilə yanaşı WPA3 də göstərilməlidir.
:::
