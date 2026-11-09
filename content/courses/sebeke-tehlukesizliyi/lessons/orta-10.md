+++
title = "Zərərli proqram təminatı və kompromitasiya indikatorları (IoC)"
unit = "orta"
order = 10
summary = "Bütün anlayışlar 1–3 cümləyə sığdırılıb: zərərli proqram növləri, yoluxma yolu, davamlılıq, C2 və ikiqat şantaj, artefakt-IoC-IoA, Ağrı piramidası, indikatorun həyat dövrü, təhlil üsulları, YARA və Sigma, vasitələr, insidentə cavab və üç real hadisə."
updated = 2026-11-09

[[source]]
title = "Mühazirə 10: Zərərli proqram təminatı və kompromitasiya indikatorları (IoC)"
note = "Elmar Cabbarov, 2026–2027"
+++

Zərərli proqram necə yayılır, sistemdə nə edir və arxasında hansı izləri qoyur? Bu izlər (IoC) həm yoluxmanı aşkarlamaq, həm də başqa təşkilatları xəbərdar etmək üçün işlədilir. Universitet nümunələri (LMS, tələbə bazası, kitabxana, dekanlıq) və adlar şərti tədris nümunəsidir.

## Zərərli proqram və təhlükəsizliyin pozulması

Zərərli proqram təminatı (malware) məlumatı oğurlamaq, icazəsiz dəyişiklik etmək, xidməti pozmaq və ya resurslardan icazəsiz istifadə üçün hazırlanmış kod, skript, makro və ya yaddaşa yerləşdirilmiş koddur. Uzantı və ölçü zərərli olub-olmamağı müəyyən etmir. Kompüterin yavaşlığı da yoluxma sübutu deyil; analitik prosesləri, faylları, şəbəkə əlaqələrini və hesab fəaliyyətini yoxlayır. Qanuni alətdən zərərli istifadə (uzaqdan yardım proqramı) ilə xüsusi zərərli proqram ayrılır: icazə, istifadəçi, vaxt və əməl araşdırılır.

Eyni yoluxma universitetin LMS (Learning Management System), tələbə bazası və kitabxana xidmətlərində fərqli xassəni pozur: parol oğurluğu məxfiliyi, qiymət cədvəlinin dəyişməsi bütövlüyü, fayl serverinin şifrələnməsi əlçatanlığı.

| Anlayış | Mənası |
| --- | --- |
| Aktiv | Qorunan məlumat, xidmət və ya resurs |
| Zəiflik | İstismara şərait yaradan çatışmazlıq (kod səhvi və ya zəif iş qaydası) |
| Təhdid | Zərər yaratmaq potensialı |
| Eksploit (exploit) | Zəiflikdən istifadə edən kod və ya üsul; istismar (exploitation) onun tətbiqidir |
| Zərərli yük (payload) | Hücumun məqsədini yerinə yetirən hissə |
| Kompromitasiya | Sistemin, hesabın və ya məlumatın təhlükəsizliyinin faktiki pozulması |

:::tip Düstur
Aktiv + Zəiflik + Təhdid → Eksploit → Zərərli yük → Komprometasiya. Eksploit qapını açır, yük içəridə ziyan vurur. Hər yoluxmada eksploit olmur (istifadəçi proqramı özü başlada bilər), komprometasiya da həmişə zərərli proqramla olmur: oğurlanmış parolla giriş də komprometasiyadır.
:::

Üç yaxın anlayış: **hadisə (event)** sistemdə baş verən fəaliyyətdir; **xəbərdarlıq (alert)** qaydanın araşdırılmalı saydığı nəticədir; **insident (incident)** cavab tələb edən real pozuntudur. Telemetriya (telemetry) toplanan texniki müşahidələrdir (proses, valideyn, heş, şəbəkə istiqaməti); toplanmayanı sonradan IoC ilə bərpa etmək olmur.

## Zərərli proqram növləri

Növlər eyni suala cavab vermir: virus və qurd çoxalmanı, troyan aldadıcı təqdimatı, ransomware məqsədi, rootkit gizlənməni bildirir. Ona görə bir nümunə eyni anda troyan, bot və ransomware ola bilər (Emotet: troyan + yayılma + yükləyici; WannaCry: qurd + şifrələyici). Çoxmərhələli hücumda ilk tapılan faylı silmək kifayət deyil: ikinci yük, davamlılıq və oğurlanmış hesablar qala bilər.

| Növ | Əsas xüsusiyyət |
| --- | --- |
| Virus | Başqa obyektə (fayl, makro, yükləmə sahəsi) yapışıb çoxalır; yoluxmuş kod icra olunmalıdır, istifadəçi klikləməsi məcburi deyil |
| Qurd (worm) | Başqa fayla yapışmadan, şəbəkə xidməti zəifliyi ilə özü yayılır |
| Troyan (Trojan) | Faydalı görünür (krek, saxta quraşdırıcı), özünü çoxaltmır; imza da təhlükəsizlik zəmanəti deyil |
| Ransomware | Girişi məhdudlaşdırır və ya şifrələyib fidyə istəyir |
| Spyware | Gizli izləyir; keylogger düymə basmalarını toplayır |
| Infostealer | Parol, brauzer kukisi, sessiya tokeni, açar oğurlayır |
| Backdoor | Giriş nəzarətindən yan keçən gizli yol (məs. gizli hesab) |
| RAT (Remote Access Trojan) | Uzaqdan əmr icrası, fayl ötürməsi, ekran müşahidəsi |
| Bot / botnet | Uzaqdan tapşırıq alan düyün / belə düyünlərin toplusu (spam, DDoS, parol sınağı) |
| Rootkit | Fayl, proses, bağlantı izlərini gizlədir; nüvədə də işləyə bilər |
| Bootkit | Yükləmə zəncirinə yerləşir, OS-dən əvvəl işə düşür; hər rootkit bootkit deyil |
| Wiper | Məlumatı və ya fayl sistemi strukturlarını dağıdır (NotPetya) |
| Kriptocəker (cryptojacker) | CPU, GPU, bulud resursunu icazəsiz hasilata sərf edir |
| Məntiqi bomba (logic bomb) | Şərt ödənəndə işə düşür; yayılma qabiliyyəti lazım deyil |
| Dropper | Yükü içində daşıyıb mühitə yerləşdirir |
| Downloader | Yükü şəbəkədən endirir |
| Loader | Yükü icraya hazırlayıb yaddaşa yerləşdirir və başladır |

Adlandırma kəsişir: bir komponent həm endirə, həm aça, həm icra edə bilər; analitik ad əvəzinə faylın haradan gəldiyini, hara yazıldığını və hansı prosesdə işlədiyini sənədləşdirir. Tokenin oğurlanması parol və MFA-nı təkrar keçmədən giriş verə bilər, ona görə infostealer-dən sonra parol dəyişmək kifayət etmir: sessiyalar ləğv edilməli, cihaz təmizlənməlidir. Fidyə qeydi faylların açarla qayıdacağını sübut etmir, çünki wiper şifrələyici kimi görünə bilər.

## Yoluxma yolları və hücumun ardıcıllığı

İlkin giriş (initial access) hücumçunun ilk çıxışıdır; yoluxma vektoru (infection vector) kodun çatdırıldığı yoldur. Oğurlanmış VPN hesabı ilkin giriş verə bilər, fişinq isə cihazda kod işlətmədən parol oğurlaya bilər.

| Vektor | Tədbir |
| --- | --- |
| Fişinq əlavəsi | Əlavə təhlili, aktiv məzmun məhdudiyyəti, bildiriş kanalı |
| Keçid, saxta yenilənmə | Veb nəzarəti, rəsmi proqram mənbəyi |
| Zəif xidmət (yamaqlanmamış LMS) | Aktiv inventarı, yamaq, xarici girişin daraldılması |
| Etibarsız paket (krek) | Təsdiqli repozitoriya, paket yoxlaması |
| Çıxarılan daşıyıcı (USB) | Daşıyıcı siyasəti, icra nəzarəti |
| Oğurlanmış hesab | MFA, cihaz nəzarəti, sessiya monitorinqi |
| Təchizat zənciri (supply chain) | Mənbə, imza, qurma prosesi, davranış yoxlaması; düzgün imza zərərli kodu təhlükəsiz etmir |

Proses ağacı (process tree) hansı prosesin hansını başlatdığını göstərir. Ən güclü siqnallardan biri gözlənilməyən valideyn–övlad əlaqəsidir: Word, Excel və ya PDF oxuyucusunun `cmd.exe`, `powershell.exe`, `wscript.exe` başlatması normal iş axınında demək olar olmur. Bu təkbaşına hökm deyil; sənədin mənbəyi, əmr sətri, yaranan fayl, hesab və bağlantı birlikdə yoxlanır. Çatdırılma, açılma, proses yaranması və uğurlu icra ayrı faktlardır; bunları ayırmaq insidentin əhatəsini şişirtməmək üçündür.

:::figure
src = "m10-1.png"
alt = "Sxem: winword.exe (Qiymet_yekun.docm) adi halda splwow64.exe (çap) başladır; şübhəli budaqda powershell.exe skripti profilə fayl yazır, schtasks ilə yeni tapşırıq yaradır və update-campus.example domeninə qoşulur."
caption = "Şəkil 1. Eyni proqram, fərqli davranış: adi və şübhəli proses əlaqələri (şərti nümunə)."
:::

Tipik ardıcıllıq: ilkin giriş → icra → davamlılıq (xidmət, Run açarı, planlaşdırılmış tapşırıq, ATT&CK T1053) → imtiyazların artırılması → daxili hərəkət → idarəetmə (C2) → məlumatın çıxarılması və ya şifrələmə. Bu sıra məcburi deyil: hücumçu davamlılıq qurmadan məlumat çıxara, artıq imtiyazlı girdiyinə görə artırmanı keçə bilər.

- **İmtiyazların artırılması (privilege escalation)** mövcud girişdən yüksək səlahiyyət almaqdır.
- **Daxili yan hərəkət (lateral movement)** bir sistemdən başqasına keçməkdir; adi hesabla bir neçə xidmətə giriş varsa, yerli admin şərt deyil.
- **MITRE ATT&CK:** taktika hücumçunun məqsədi, texnika məqsədə çatma üsuludur; texnika uyğunluğu kimliyi və ya niyyəti müəyyən etmir. Versiya saxlanılmalıdır: 28 aprel 2026-cı il tarixli v19-da Stealth (TA0005) və Defense Impairment (TA0112) ayrılıb, jurnal təmizlənməsi T1685.005 altındadır (köhnə mənbələrdə T1070.001).

## Davamlılıq və gizlənmə

Davamlılıq (persistence) proqram bağlandıqdan və ya sistem yenidən başladıqdan sonra giriş və icra imkanını saxlamaqdır. Yeni xidmət və ya tapşırıq özü yoluxma demək deyil (ehtiyat nüsxə agenti də belə işləyir); yaranma vaxtı, yaradan hesab, başladılan fayl və dəyişiklik sifarişi tutuşdurulur. Tapşırığın adı hökm üçün yetmir: hədəf faylın mövcudluğu, heşi, imzası və proses əlaqəsi yoxlanır.

| Sistem | Yoxlanılan yerlər |
| --- | --- |
| Windows | Run və RunOnce açarları, planlaşdırılmış tapşırıq, xidmət, başlanğıc qovluğu, WMI hadisə abunəsi |
| Linux | systemd xidmət və taymerləri, cron tapşırıqları, SSH `authorized_keys`, shell başlanğıc faylları (`.profile`), tətbiq əlavələri (plagin, modul) |

Oxuma əmrləri davamlılıq yaratmır: `reg query HKCU\...\Run`, `schtasks /query /fo LIST /v`, `Get-CimInstance Win32_Service`, Linux-da `systemctl list-unit-files`, `systemctl list-timers`, `crontab -l`, `journalctl -u`. Birincisi və `crontab -l` yalnız cari hesabı göstərir, digər profillər ayrıca yoxlanır. Qanuni görünən proqramın arqumenti dəyişdirilmiş ola bilər (məs. arxiv aləti yad qovluğu çıxarır), ona görə yalnız ada görə icazəli siyahı yetmir.

**Gizlənmə.** Obfuskasiya (obfuscation) kodun mənasını çətinləşdirir, paketləmə (packing) icraolunan məzmunu sıxılmış saxlayıb icrada açır; hər ikisini qanuni proqram da işlədə bilər, yüksək entropiya tək başına zərərli hökmü vermir. Polimorf zərərli proqramda hər nüsxədə şifrələnmə dəyişir, metamorfda kodun özü yenidən yazılır; ikisi də heşə və bayta əsaslanan aşkarlamanı çətinləşdirir, davranış isə eyni qala bilər. Faylsız (fileless) hücum yaddaşda və PowerShell, WMI kimi qanuni alətlərlə işləyir, amma iz qoymur demək deyil: reyestr, skript jurnalı, planlaşdırılmış tapşırıq və yaddaş səhifəsi iz saxlaya bilər.

## Komanda-idarəetmə və ikiqat şantaj

Komanda-idarəetmə (Command and Control, C2) yoluxmuş sistemə tapşırıq göndərib nəticə almaq mexanizmidir. Bağlantı daxildən başlayır, çünki firewall veb çıxışına icazə verir; ona görə yalnız daxil olan trafikə baxmaq RAT və botu görməyə kifayət etmir. Tapşırıq üçün dövri müraciət **beacon**, aralıqların təsadüfiləşdirilməsi **jitter** adlanır; tam sabit dövr olmaması C2-ni istisna etmir, qanuni yenilənmə agenti də dövri bağlanır, ona görə ünvan prosesə bağlanmalıdır.

| C2 üsulu | Aşkarlama sərhədi |
| --- | --- |
| HTTP/HTTPS | Şifrələnmiş məzmun görünmür; istiqamət, vaxt, həcm görünür |
| DNS üzərindən | Uzun subdomenlər, tezlik; CDN də mürəkkəb adlardan istifadə edir |
| Qanuni bulud xidməti | Xidmət domeninin bloklanması zəif seçimdir |
| Birbaşa IP | Portun adi olması qanuni etmir |
| Həmyaşıd şəbəkə (P2P) | Mərkəzi domeni bloklamaq kifayət deyil |
| Domen yaratma alqoritmi (DGA) | Çoxlu uğursuz sorğu; hər təsadüfi domen DGA deyil |

DNS qeydləri (A, AAAA) adın ünvanla əlaqəsini göstərir, hansı cihazın sorğu göndərdiyini yox; bunun üçün müştəri ünvanı və vaxtı saxlayan **DNS sorğu jurnalı** lazımdır (alternativ resolver olsa, yerli jurnalda sorğu olmaya bilər). Sertifikat, port və domen tək-tək hücumun məqsədini sübut etmir; EDR bağlantını yeni imzasız prosesə, o isə şübhəli sənədə bağlayanda fərziyyə güclənir.

Məlumatın icazəsiz çıxarılması (exfiltration) C2 ilə eyni kanaldan keçə bilər, amma məcburi deyil, və C2 bloklandıqdan sonra da davam edə bilər. Kiçik sızma da ağır ola bilər: admin açarı və ya token böyük fayl deyil, ona görə az trafik məxfiliyin qorunduğunu göstərmir.

İkiqat şantajda (double extortion) hücumçu həm işin dayanması, həm oğurlanmış məlumatın yayılması ilə təzyiq edir. Tipik ssenari: giriş, kəşfiyyat, məlumatın çıxarılması, bərpa imkanlarının zəiflədilməsi, şifrələmə və tələb. Çox vaxt oğurluq olur, amma məcburi deyil; ikisini də fərz etmək səhvdir. Əlçatanlıq, məxfilik və bütövlük ayrı suallardır: bərpa edilmiş LMS məlumatın sızmasını bağlamır, fidyə ödəmək də açarın işləməsinə və silinməyə zəmanət vermir. Ehtiyat nüsxələrin idarəetmə hesabları istehsal domenindən asılı olmamalı, bərpa sınanmalıdır (bazanın ardıcıllığı, tətbiqin işə düşməsi).

## Artefakt, IoC və IoA

Artefakt (artifact) fəaliyyətin yaratdığı texniki izdir (fayl, reyestr dəyəri, DNS sorğusu, giriş qeydi). Kompromitasiya indikatoru (Indicator of Compromise, IoC) zərərli fəaliyyətlə əlaqələndirilmiş izdir və yanında sübut, vaxt və etibarlılıq dərəcəsi saxlanılır. Hücum indikatoru (Indicator of Attack, IoA) hücumun gedişini göstərən davranışa yönəlir. Sərhəd bütün mənbələrdə eyni deyil, praktik fərq qaydanın dəyər axtarması ilə hərəkət əlaqəsi axtarması arasındadır.

| Meyar | Artefakt | IoC | IoA |
| --- | --- | --- | --- |
| Sual | Nə müşahidə olunub? | Hansı iz zərərli fəaliyyətlə bağlıdır? | Hansı şübhəli davranış baş verir? |
| Nümunə | Profil qovluğunda fayl | SHA-256 məlum zərərli nümunə ilə eyni | Sənəd skript başladır və davamlılıq yaradır |
| Məhdudiyyət | Zərərli əlaqə sübut olunmayıb | Dəyər dəyişə, kontekst köhnələ bilər | Qanuni avtomatlaşdırma oxşar görünə bilər |

IoC yalnız insidentdən sonra yox, əvvəlcədən bloklamada da işləyir; IoA da həmişə hadisəni qabaqlamır. İndikator qrupları: fayl (heş, ad, yol, imza), şəbəkə (IP, domen, URL), sistem (xidmət, tapşırıq, reyestr), proses (valideyn, əmr sətri; PID təkrar işlənə bilər), hesab (yeni hesab, imtiyaz), poçt (başlıqlar, əlavə heşi; görünən göndərən adı mənbəni sübut etmir). Təqdimata görə: **atomar (atomic)** ayrıca dəyər (domen, IP), **hesablanmış (computed)** əməliyyatdan alınan (heş), **davranış (behavioral)** hadisələr arasındakı münasibətdir.

Kriptoqrafik heş (cryptographic hash) dəyişən ölçülü məlumatdan sabit uzunluqlu nəticə verir: SHA-256 256 bitdir, 64 onaltılıq simvolla yazılır. Adı dəyişmək heşi dəyişmir, bir bayt dəyişmək dəyişir. Heş eyni nümunəni tapmağa və sübutun dəyişmədiyini yoxlamağa kömək edir, amma faylın təhlükəsizliyini, icrasını və bütün ailəni göstərmir. MD5 və SHA-1 üçün toqquşma hücumları məlumdur, ona görə düşmən şəraitində SHA-256 seçilir; bu hər fayla dərhal əvəz yaratmaq demək deyil.

Ağrı piramidası (Pyramid of Pain) indikator bloklananda hücumçunun onu dəyişmək çətinliyini göstərir: aşağıdan yuxarı heşlər, IP, domen adları, şəbəkə və host artefaktları, alətlər və TTP (Tactics, Techniques and Procedures). Bu etibarlılıq balı deyil; heşlər sürətli məhdudlaşdırma üçün yenə lazımdır, yuxarıda aşkarlama isə zəngin telemetriya tələb edir.

:::figure
src = "m10-3.png"
alt = "Altı pilləli piramida; aşağıdan yuxarı: heş dəyərləri, IP ünvanları, domen adları, artefaktlar, alətlər, TTP. Yanda ox: hücumçu üçün dəyişdirmə çətinliyi artır."
caption = "Şəkil 2. Ağrı piramidası: yuxarı getdikcə hücumçunun dəyişmə çətinliyi artır."
:::

## İndikatorların keyfiyyəti və həyat dövrü

Keyfiyyət bloklama sürəti ilə yox, mənbənin etibarı, əlaqənin gücü, zaman uyğunluğu, seçicilik və tətbiqin nəticəsi ilə ölçülür. Paylaşılan IP-ni bütöv bloklamaq qanuni resursu bağlayır; dar URL, domen, hesab və ya proses səviyyəsi seçilir. Etibarlılıq dərəcəsi (confidence) sübutun gücüdür, təsir isə aktivə mümkün zərərdir; prioritet ikisindən və cari fəaliyyətdən asılıdır.

İndikator kartında olmalıdır: növ və dəyər, mənbə, ilk və son müşahidə, etibarlılıq və əsas, əlaqəli fəaliyyət, tədbir və sahibi, baxış və bitmə vaxtı, paylaşma məhdudiyyəti (TLP). Həyat dövrü: toplama (insident, analiz, tələ, jurnal, xarici axın (feed)) → normallaşdırma → zənginləşdirmə (enrichment) → tətbiq (SIEM, EDR, DNS) → qiymətləndirmə (FP, fayda) → köhnəlmə. Üç platformada təkrarlanan eyni hesabat üç təsdiq deyil. Normallaşdırmada heşin hərf registri fərq yaratmır, URL yolunda yarada bilər; xam dəyər ayrı saxlanılır. Zənginləşdirmədə cari DNS cavabı keçmiş ünvanı göstərməyə bilər. Nümunəni açıq xidmətə yükləmək sızma yarada bilər, heş sorğusu da məlumat ötürür.

İndikatorun ömrü (lifetime) kontekstlə idarə olunur: heş illərlə tanıyır, amma variantı tutmur; IP başqasına verilə, domen təmizlənə bilər. Aktiv bloklamadan çıxarılan indikator tarixi araşdırmadan silinməyə bilər: köhnə semestr insidentində yenə müqayisə olunur, amma bu gün avtomatik bloklanmır.

STIX (Structured Threat Information Expression) təhdid məlumatını obyektlər və münasibətlərlə təsvir edən model, TAXII (Trusted Automated Exchange of Intelligence Information) isə onun mübadilə protokoludur; heç biri indikatorun etibarlılığını sübut etmir. Trafik işığı protokolu (Traffic Light Protocol, TLP) paylaşma sərhədini bildirir: FIRST TLP 2.0-da CLEAR, GREEN, AMBER, AMBER+STRICT, RED (zərərlilik balı deyil). Domenlə birlikdə tələbənin adı və sənədi paylaşılmır.

## Təhlükəsiz qəbul və təhlil üsulları

Şübhəli fayl iş kompüterində açılmır. Mənbə, vaxt, ölçü və SHA-256 qeyd edilir, orijinal toxunulmaz qalır, iş nüsxə ilə aparılır, anbara yalnız səlahiyyətli giriş olur. Parollu arxiv təsadüfi açılmanı azaldır, izolyasiya deyil. Laboratoriya məlumatı sintetik olmalıdır.

| Üsul | Sual | Məhdudiyyət |
| --- | --- | --- |
| Statik | Faylda hansı struktur və funksiyalar var? | Paketləmə və obfuskasiya gizlədir |
| Dinamik | Bu şərtlərdə nə etdi? | Başqa şərtdə başqa davranış ola bilər |
| Yaddaş | İcra zamanı hansı kod və obyektlər var? | Görüntü bir ana aiddir, həssas məlumat daşıyır, söndürmə yaddaşı itirir |

**Statik təhlil** faylı icra etmədən aparılır: əvvəlcə uzantıya yox, həqiqi formata (PE, ELF, PDF, Office) baxılır (`hesabat.pdf.exe` aldadır), sonra heş, rəqəmsal imza, sətirlər (strings), idxal funksiyaları, resurslar. Etibarlı imza zəmanət deyil, imzasız skript də avtomatik zərərli deyil. Sətirdə domen tapılması yalnız namizəd indikatordur. Disassembler maşın kodunu təlimatlara ayırır, decompiler yüksək səviyyəli təsvir qurur (Ghidra, IDA); bu mənbə kodunun tam bərpası deyil.

**Dinamik təhlil** nümunəni qum qutusunda (sandbox) icra edib müqayisə edir: yaranan proses, fayl, reyestr, şəbəkə. Mühit istehsalatdan ayrı olmalı, real məlumat və parol olmamalı, şəbəkə çıxışı nəzarətdə olmalı, ortaq qovluq və bufer (clipboard) bağlı olmalıdır; virtual maşın təkbaşına tam izolyasiya deyil, snapshot kənara çıxmış zərəri geri qaytarmır. Yayınma (evasion) zamanı proqram mühiti tanıyıb gözləyir, siçan hərəkəti və ya uzun gecikmə tələb edir; qısa sakitlik təhlükəsizlik sübutu deyil, nəticə yalnız müşahidə olunanla məhdud yazılır.

**Yaddaş təhlili** prosesləri, modulları, əlaqələri və yeridilmiş kodu araşdırır (Volatility); faylsız hücumlar üçün vacibdir. RAM-da parol və token ola bilər, ona disk kimi ciddi nəzarət tətbiq edilir; söndürmə uçucu sübutu itirir, götürmə isə sistemi dəyişir.

## YARA və Sigma qaydaları

YARA fayl və ya yaddaş məzmununda mətn, bayt və məntiqə görə axtarır. Tədris qaydası:

```yara
rule UNEC_Tedris_Markerleri : tedris {
  meta:
    description = "Zerersiz laboratoriya markerleri"
  strings:
    $a = "UNEC_LAB_MARKER_A" ascii
    $b = "UNEC_LAB_MARKER_B" ascii
  condition:
    filesize < 1MB and all of them
}
```

`rule` adı və teqi nəticəni tanıdır; `meta` mənşə və məqsədi izah edir, şərtə daxil deyil; `strings` axtarılan məzmunu verir (`ascii`, `wide` bayt təqdimatını seçir); `condition` məntiqdir (`all of them` hər iki sətir, `filesize` ölçü hədd). Uyğunluq faylın zərərli olduğunu yox, şərtin ödəndiyini göstərir. Real qayda təsadüfi domen sətrindən qurulmur: sabit kod və konfiqurasiya xüsusiyyətləri seçilir, qanuni proqramlarda yanlış uyğunluq ölçülür, yoxlama nümunələri sınaq nümunələrindən fərqli olmalıdır, hesabatda qayda versiyası, heş və tapılan xüsusiyyət saxlanılır.

Sigma jurnal məlumatları üçün paylaşılabilən aşkarlama qaydasıdır: YARA məzmunu, Sigma hadisə sahələrini yoxlayır. Başqa SIEM-ə çevirmədə sahə xəritəsi, məlumat mənbəyi və semantika uyğunlaşdırılmalıdır. Tədris qaydası Word-dən PowerShell başlanmasını axtarır: `logsource` (category `process_creation`, product `windows`) mənbəni, `selection` sahə şərtlərini (`ParentImage|endswith: '\WINWORD.EXE'`, `Image|endswith` ilə `powershell.exe` və `pwsh.exe` alternativləri), `condition` seçimin istifadəsini, `falsepositives` qanuni səbəbləri (avtomatik istisna deyil), `level` ilkin ciddiliyi göstərir. Qayda yalnız birbaşa valideyni Word olan prosesi tutur; araya `cmd.exe` girsə qaçırar, ona görə proses ağacı ilə tamamlanır, istisna dar qurulur.

## Tətbiq: vasitələr və keyfiyyətin ölçülməsi

| Vasitə | Rol | Kor nöqtə |
| --- | --- | --- |
| Antivirus | İmza, evristika, davranış; karantin | Ailənin başqa variantı, hesab oğurluğu |
| EDR (Endpoint Detection and Response) | Proses, fayl, hesab telemetriyası, cihaz təcridi | Agentsiz cihaz |
| DNS nəzarəti | Zərərli domen sorğusunu məhdudlaşdırır | Alternativ resolver, birbaşa IP |
| Proksi və firewall | URL, domen, əlaqə qaydası | Paylaşılan ünvanı bloklamaq qanuni xidməti poza bilər |
| IDS (Intrusion Detection System) / IPS (Intrusion Prevention System) | IDS xəbərdarlıq verir, IPS uyğun yerləşmədə trafiki dayandırır | Şifrələmə və sensorun yeri |
| SIEM (Security Information and Event Management) | Mənbələrarası axtarış və korrelyasiya | Yanlış sahə xəritəsi, saat fərqi |
| SOAR (Security Orchestration, Automation and Response) | Təkrarlanan cavab işlərini avtomatlaşdırır | Yanlış nəticə sürətlə yayılır; kritik giriş kəsilməsi üçün əvvəlcədən təsdiqlənmiş səlahiyyət lazımdır |

Heş üzrə qadağa oğurlanmış sessiyanı ləğv etmir, cavab cihaz və kimlik səviyyəsində planlaşdırılır.

Sysmon Windows-da əlavə telemetriya yaradır: Event ID 1 proses yaradılması (valideyn ilə), 3 şəbəkə bağlantısı (standart aktiv deyil, konfiqurasiyada açılır), 11 fayl yaradılması, 13 reyestr dəyərinin dəyişməsi, 22 DNS sorğusu. `ProcessGuid` eyni prosesin hadisələrini bağlayır, PID təkrar verilə bilər. Korrelyasiya sənəd, skript, DNS və bağlantı hadisələrini birləşdirir; hadisə vaxtı ilə SIEM-ə çatma vaxtı ayrı saxlanılır. DNS sorğusu uğurlu bağlantını, bağlantı isə oğurluğu təkbaşına sübut etmir.

Uyğunluq həqiqi zərərli fəaliyyətdirsə həqiqi müsbət (true positive, TP), qanuni fəaliyyətdirsə yanlış müsbət (false positive, FP), buraxılmış hücum yanlış mənfidir (false negative, FN). Qayda 40 xəbərdarlıq verib, 10-u zərərlidirsə, dəqiqlik 10 / 40 = 25%; bu, hücumların hansı hissəsinin tapıldığını göstərmir. Bunu tamlıq (recall) göstərir: TP / (TP + FN). Sensorun susması ayrıca xəbərdarlıq yaratmalıdır, çünki sıfır nəticə işləməyən toplama da ola bilər.

## İnsidentə cavab və bərpa

NIST SP 800-61 Rev. 3 (aprel 2025) insidentə cavabı NIST CSF 2.0 ilə əlaqələndirir; CSF 2.0-ın funksiyaları Govern, Identify, Protect, Detect, Respond, Recover. Hazırlıq məsul şəxsləri, aktiv inventarını, ehtiyat nüsxələri, jurnal toplamanı və qərar səlahiyyətlərini əvvəlcədən müəyyən edir.

| İş | Məzmun |
| --- | --- |
| Əhatə | Eyni faylı alan hesablar, domenlər, ikinci yüklər, tapşırıqlar, məlumat resursları; IoC ilə keçmiş, davranışla variantlar. Agentsiz cihazı yoxlamadan təmiz elan etmək olmaz |
| Təcrid | EDR ilə (idarəetmə kanalı qalır) və ya kommutator/firewall ilə; dərhal söndürmə uçucu sübutu itirir, amma aktiv dağıntıda təcili qərar ola bilər |
| Sübut | Disk və yaddaş görüntüsü, jurnal, poçt başlıqları; ötürülmə zənciri (chain of custody) kimin, nə vaxt, necə götürdüyünü qeyd edir, SHA-256 dəyişikliyi yoxlayır |
| Aradan qaldırma | Zəifliyi bağla, davamlılıq, ikinci yük və hesabları sil; rootkit və ya dərin müdaxilə şübhəsində yoxlanmış mənbədən yenidən qur, firmware şübhəsində adi qurulum yetməyə bilər |
| Hesablar | Parolu təmiz cihazdan dəyiş, sessiya və yeniləmə tokenlərini ləğv et, icazələri, poçt yönləndirmələrini, SSH açarlarını yoxla; infostealer ehtimalında həmin cihazdakı bütün hesablar əhatədədir |
| Bərpa | Yoluxmadan əvvəlki etibarlı nüsxə (tarix köhnəliyi kifayət deyil), ayrı mühitdə yoxlama, zəifliyin bağlanması, tətbiq səviyyəsində test, sonra müşahidə (eyni C2-yə cəhd çirkli nüsxə ola bilər) |

Araşdırılmamış məsələ hesabatda açıq qalır; bilinməyən faktı olmadı kimi yazmaq olmaz.

## Real hadisələrin dərsləri

- **WannaCry** (may 2017): Windows SMB zəifliyindən istifadə edən qurd komponenti olan şifrələyici; Microsoft MS17-010 yenilənmələri zəiflikləri həmin ilin martında bağlamışdı. Dərs: yamağın mövcudluğu ilə hər aktivə tətbiqi ayrıdır; inventar, SMB girişinin daraldılması, bərpa nüsxəsi lazımdır, heşi bloklamaq kifayət deyil.
- **NotPetya** (iyun 2017): Ukraynada M.E.Doc proqramının kompromitasiya edilmiş yenilənməsi ilə başladı, daxildə zəifliklər və oğurlanmış kimlik məlumatları işlədi. Fidyə görünüşünə baxmayaraq dağıdıcı (wiper) nümunəsi kimi öyrənilir. Dərs: təchizatçı yenilənməsinə nəzarətsiz imtiyaz verilməməlidir, yamaq oğurlanmış etibarlı hesabla hərəkəti qarşılamır.
- **Emotet:** əvvəl bank troyanı, sonra başqa yüklərin çatdırıldığı modul infrastruktura çevrildi; poçt kampaniyası və çoxmərhələli məntiq. Hər halda son şifrələyicinin adı kimi işlətmək düzgün deyil. Dərs: məktubu silmək yetmir, kimin açdığı, hansı proseslər və yüklər, hesab oğurluğu araşdırılır; tarixi indikator tətbiqdən əvvəl yenidən yoxlanır.

:::reveal Sənəd açıldıqdan sonra powershell başlayıb, tapşırıq yaranıb, domenə dövri HTTPS gedir. Bunları necə təsnif edərsən?
Word-dən kodlaşdırılmış PowerShell icra və şübhəli proses ağacıdır (IoA); planlaşdırılmış tapşırıq davamlılıqdır (T1053); dövri HTTPS digər əlamətlərlə C2 beacon ehtimalıdır. Heş, domen və tapşırıq adı IoC kimi qeydə alınır. İlk addım: EDR ilə söndürmədən təcrid, domenin bloklanması, SIEM-də eyni fayl və domenin axtarışı, parolun təmiz cihazdan dəyişdirilməsi, sübut toplanması.
:::

:::reveal Sandbox-da 3 dəqiqə heç nə olmayıb. "Fayl təmizdir" yazmaq olarmı?
Yox. Zərərli proqram mühiti tanıyıb gözləyə bilər. Nəticə yalnız müşahidə olunan mühit və müddətlə məhdud yazılır; statik təhlil, heşin təhdid kəşfiyyatında yoxlanması, fərqli sandbox və lazım gəlsə yaddaş təhlili ilə tamamlanır.
:::
