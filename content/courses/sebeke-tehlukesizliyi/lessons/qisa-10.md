+++
title = "Zərərli proqram təminatı və kompromitasiya indikatorları (IoC)"
unit = "qisa"
order = 10
summary = "Mühazirənin skeleti: hər anlayış bir sətirdə. Zərərli proqram növləri, yoluxma yolu, davamlılıq, C2, IoC-IoA, təhlil, YARA və Sigma, vasitələr, cavab və real hadisələr."
updated = 2026-11-09

[[source]]
title = "Mühazirə 10: Zərərli proqram təminatı və kompromitasiya indikatorları (IoC)"
note = "Elmar Cabbarov, 2026–2027"
+++

Zərərli proqram necə yayılır, sistemdə nə edir və hansı izləri (IoC) qoyur? Bu izlər yoluxmanı aşkarlamaq və başqalarını xəbərdar etmək üçün işlədilir. Universitet nümunələri şərtidir.

## Zərərli proqram və təhlükəsizliyin pozulması

Zərərli proqram təminatı (malware) məlumatı oğurlamaq, dəyişdirmək, xidməti pozmaq və ya resursdan icazəsiz istifadə üçün kod, skript, makro və ya yaddaşdakı koddur; uzantı və ölçü zərərliliyi göstərmir. Eyni yoluxma LMS (Learning Management System), tələbə bazası və kitabxanada fərqli xassəni pozur: parol oğurluğu məxfiliyi, qiymət dəyişikliyi bütövlüyü, şifrələmə əlçatanlığı.

| Anlayış | Mənası |
| --- | --- |
| Aktiv | Qorunan məlumat, xidmət, resurs |
| Zəiflik | İstismara şərait yaradan çatışmazlıq |
| Təhdid | Zərər potensialı |
| Eksploit (exploit) | Zəiflikdən istifadə edən kod; istismar (exploitation) onun tətbiqidir |
| Zərərli yük (payload) | Məqsədi yerinə yetirən hissə (şifrələmə, oğurluq) |
| Kompromitasiya | Təhlükəsizliyin faktiki pozulması; oğurlanmış parolla giriş də buna daxildir |

:::tip Düstur
Aktiv + Zəiflik + Təhdid → Eksploit → Zərərli yük → Komprometasiya. Eksploit qapını açır, yük içəridə ziyan vurur; hər yoluxmada eksploit olmur.
:::

- **Hadisə (event):** sistemdə baş verən fəaliyyət. **Xəbərdarlıq (alert):** qaydanın araşdırılmalı saydığı nəticə. **İnsident (incident):** cavab tələb edən real pozuntu.
- **Telemetriya (telemetry):** proses, heş, şəbəkə kimi toplanan müşahidələr; toplanmayanı sonradan bərpa etmək olmur.
- Kompüterin yavaşlığı yoluxma sübutu deyil; qanuni uzaqdan yardım alətinin zərərli istifadəsi icazə və əmələ görə ayrılır.

## Zərərli proqram növləri

Növlər fərqli suallara cavab verir (necə yayılır, necə maskalanır, nə edir, necə gizlənir), ona görə bir nümunə eyni anda troyan, bot və ransomware ola bilər: Emotet troyan + yükləyici, WannaCry qurd + şifrələyici.

| Növ | Bir sətirdə |
| --- | --- |
| Virus | Başqa obyektə (fayl, makro, yükləmə sahəsi) yapışıb çoxalır |
| Qurd (worm) | Şəbəkə ilə özü yayılır, fayla yapışmır |
| Troyan (Trojan) | Faydalı görünür (krek), özünü çoxaltmır |
| Ransomware | Şifrələyib fidyə istəyir |
| Spyware | Gizli izləyir; keylogger düymə basmalarını toplayır |
| Infostealer | Parol, kuki, sessiya tokeni, açar oğurlayır |
| Backdoor | Gizli giriş yolu |
| RAT (Remote Access Trojan) | Uzaqdan idarə troyanı: əmr, fayl, ekran |
| Bot / botnet | Uzaqdan tapşırıq alan düyün / onların şəbəkəsi (spam, DDoS) |
| Rootkit | Özünü OS-dən gizlədir; bootkit yükləmə mərhələsinə yerləşir |
| Wiper | Məlumatı birdəfəlik məhv edir (NotPetya) |
| Kriptocəker (cryptojacker) | Resursu icazəsiz kripto hasilatına işlədir |
| Məntiqi bomba (logic bomb) | Şərt ödənəndə işə düşür |
| Dropper / downloader / loader | Yükü içində daşıyır / şəbəkədən endirir / yaddaşa yükləyib icra edir |

Müasir hücumlar çoxmərhələlidir: ilk faylı silmək kifayət deyil, ikinci yük, davamlılıq və oğurlanmış hesablar qala bilər. Sessiya tokeni oğurlanıbsa, parolu dəyişmək kifayət etmir, sessiyalar ləğv edilməlidir.

## Yoluxma yolları və hücumun ardıcıllığı

İlkin giriş (initial access) hücumçunun ilk çıxışı, yoluxma vektoru (infection vector) kodun çatdırıldığı yoldur. Vektorlar: fişinq əlavəsi, saxta keçid və yenilənmə, zəif xidmət (yamaqlanmamış LMS), etibarsız paket (krek), USB, oğurlanmış hesab, təchizat zənciri (supply chain: etibarlı yenilənmə və ya asılılıq dəyişdirilir; düzgün imza kodu təhlükəsiz etmir).

- **Proses ağacı (process tree):** hansı proses hansını başlatdı. Word, Excel, PDF oxuyucusunun `cmd.exe`, `powershell.exe`, `wscript.exe` başlatması güclü siqnaldır, amma təkbaşına hökm deyil.
- **Tipik ardıcıllıq:** ilkin giriş → icra → davamlılıq (xidmət, Run açarı, planlaşdırılmış tapşırıq, T1053) → imtiyazların artırılması → daxili hərəkət → C2 → məlumatın çıxarılması və ya şifrələmə. Sıra məcburi deyil.
- **İmtiyazların artırılması (privilege escalation):** daha yüksək səlahiyyət almaq. **Daxili yan hərəkət (lateral movement):** bir sistemdən başqasına keçmək.
- **MITRE ATT&CK:** taktika məqsəd, texnika üsuldur; kimliyi müəyyən etmir. Versiya saxlanır: v19-da Stealth (TA0005) və Defense Impairment (TA0112) ayrılıb.
- Çatdırılma, açılma, proses yaranması və uğurlu icra ayrı faktlardır.

## Davamlılıq və gizlənmə

Davamlılıq (persistence) yenidən başlamadan sonra da giriş saxlamaqdır; yeni xidmət özü yoluxma demək deyil, yaranma vaxtı, yaradan hesab və təsdiqli sifariş yoxlanır.

| Sistem | Yoxlanan yerlər |
| --- | --- |
| Windows | Run və RunOnce açarları, planlaşdırılmış tapşırıq, xidmət, başlanğıc qovluğu, WMI abunəsi |
| Linux | systemd xidmət və taymerləri, cron, SSH `authorized_keys`, shell başlanğıcı, tətbiq əlavələri |

Gizlənmə: obfuskasiya (obfuscation) kodu çaşdırır, paketləmə (packing) sıxıb icrada açır (qanuni proqram da işlədir); polimorf hər nüsxədə şifrələnməni, metamorf kodun özünü dəyişir, heşə əsaslanan aşkarlamanı çətinləşdirir. Faylsız (fileless) hücum yaddaşda və PowerShell, WMI ilə işləyir, amma reyestr, skript jurnalı və tapşırıq izi qalır.

## Komanda-idarəetmə və ikiqat şantaj

Komanda-idarəetmə (Command and Control, C2) yoluxmuş sistemə tapşırıq verib nəticə almaq kanalıdır; bağlantı daxildən başladığı üçün yalnız gələn trafikə baxmaq kifayət etmir. Dövri müraciət beacon, aralığın təsadüfiləşdirilməsi jitter adlanır; qanuni yenilənmə agenti də dövri bağlanır, ona görə ünvan prosesə bağlanır.

- **C2 üsulları:** HTTP/HTTPS (məzmun şifrəli), DNS (uzun subdomenlər), qanuni bulud xidməti, birbaşa IP, həmyaşıd şəbəkə (P2P), domen yaratma alqoritmi (DGA).
- **DNS qeydi** adın ünvanla əlaqəsini göstərir; hansı cihazın sorğu göndərdiyini **DNS sorğu jurnalı** göstərir.
- **Məlumatın çıxarılması (exfiltration)** C2 kanalından keçə bilər, amma məcburi deyil; kiçik sızma da ağır ola bilər.
- **İkiqat şantaj (double extortion):** həm şifrələmə (əlçatanlıq), həm oğurlanmış məlumatın yayılması (məxfilik) ilə təzyiq. Bərpa sızmanı bağlamır, fidyə silinməyə zəmanət vermir.

## Artefakt, IoC və IoA

| Anlayış | Sual | Nümunə |
| --- | --- | --- |
| Artefakt (artifact) | Nə müşahidə olunub? Xam iz, zərərli olduğu sübut olunmayıb | Profil qovluğunda fayl |
| Kompromitasiya indikatoru (Indicator of Compromise, IoC) | Hansı məlum zərərli iz görünür? Etibarlılıq dərəcəsi ilə | Məlum zərərli SHA-256, domen |
| Hücum indikatoru (Indicator of Attack, IoA) | Hansı şübhəli davranış baş verir? Yeni variantda da işləyir | Sənəd skript başladır, sonra naməlum domenə qoşulur |

- **Qruplar:** fayl, şəbəkə, sistem, proses, hesab, poçt. **Təqdimata görə:** atomar (atomic: domen, IP), hesablanmış (computed: heş), davranış (behavioral: hadisələr arasındakı münasibət).
- **Kriptoqrafik heş (cryptographic hash):** SHA-256 sabit 256 bitdir; adı dəyişmək heşi dəyişmir, bir bayt dəyişir. Heş zərərliliyi, icranı və ailəni göstərmir. MD5 və SHA-1 üçün toqquşma hücumları var, SHA-256 üstündür.
- **Ağrı piramidası (Pyramid of Pain):** aşağıdan yuxarı heş, IP, domen, şəbəkə və host artefaktları, alətlər, TTP (Tactics, Techniques and Procedures); yuxarı getdikcə hücumçunun dəyişməsi çətindir. Etibarlılıq balı deyil.

## İndikatorların keyfiyyəti və həyat dövrü

- **Etibarlılıq dərəcəsi (confidence)** sübutun gücüdür, təsir aktivə mümkün zərərdir; paylaşılan IP-ni bütöv bloklamaq əvəzinə dar domen, URL və ya proses tədbiri seçilir.
- **Kart:** növ və dəyər, mənbə, ilk və son müşahidə, etibarlılıq, əlaqəli davranış, tədbir və sahibi, baxış tarixi, paylaşma məhdudiyyəti.
- **Həyat dövrü:** toplama (insident, xarici axın (feed), CERT) → normallaşdırma → zənginləşdirmə (enrichment) → tətbiq (SIEM, EDR, DNS) → qiymətləndirmə → köhnəlmə. Eyni hesabatın təkrarı çox təsdiq deyil.
- **Ömür (lifetime):** kontekstlə idarə olunur; IP başqasına keçə bilər, köhnə indikator aktiv blokdan çıxır, tarixi araşdırmada qalır.
- **Mübadilə:** STIX (Structured Threat Information Expression) məlumatın modeli, TAXII (Trusted Automated Exchange of Intelligence Information) onun protokoludur; **TLP (Traffic Light Protocol)** paylaşma sərhədini bildirir (CLEAR, GREEN, AMBER, AMBER+STRICT, RED).

## Təhlükəsiz qəbul və təhlil üsulları

Şübhəli fayl iş kompüterində açılmır: mənbə və SHA-256 qeyd edilir, orijinal qorunur, nüsxə ilə işlənir.

| Üsul | Nə edilir | Məhdudiyyət |
| --- | --- | --- |
| Statik | Fayl icra edilmədən öyrənilir: format, heş, imza, sətirlər (strings), disassembler (Ghidra, IDA) | Paketləmə və obfuskasiya |
| Dinamik | İzolyasiya olunmuş qum qutusunda (sandbox) icra və müşahidə | Zərərli proqram mühiti tanıyıb gözləyə bilər (yayınma, evasion); sakit test sübut deyil |
| Yaddaş | RAM görüntüsü (Volatility); faylsız hücum üçün vacibdir | Söndürmə yaddaşı itirir, görüntüdə parol ola bilər |

Sandbox istehsalatdan ayrı olmalı, real məlumatsız, şəbəkə çıxışı nəzarətdə, ortaq qovluq və bufer bağlı olmalıdır; virtual maşın tək başına tam izolyasiya deyil.

## YARA və Sigma qaydaları

- **YARA** fayl və yaddaş məzmununda mətn, bayt və məntiqlə axtarır: `meta` (izah), `strings` (axtarılan sətirlər), `condition` (məntiq, məs. `all of them`, `filesize`). Uyğunluq zərərliliyi yox, şərtin ödənməsini göstərir.
- **Sigma** jurnal sahələri üzərində paylaşılabilən qaydadır (`logsource`, `selection`, `condition`, `falsepositives`, `level`). Hər SIEM-də eyni işləmir: sahə xəritəsi uyğunlaşdırılır. Word-dən PowerShell qaydası araya `cmd.exe` girəndə qaçırar.

## Tətbiq: vasitələr və keyfiyyət

| Vasitə | Rolu |
| --- | --- |
| Antivirus | İmza, evristika, davranış; karantin |
| EDR (Endpoint Detection and Response) | Son nöqtə telemetriyası və cihaz təcridi |
| IDS / IPS | Intrusion Detection System görür və xəbərdarlıq verir, Intrusion Prevention System yolda dayandıra bilir |
| SIEM (Security Information and Event Management) | Mənbələri birləşdirir, korrelyasiya |
| SOAR (Security Orchestration, Automation and Response) | Təkrarlanan cavab işlərini avtomatlaşdırır |
| DNS, proksi, firewall | Domen, URL, əlaqə bloku |

- **Sysmon** (Windows): Event ID 1 proses yaradılması, 3 şəbəkə bağlantısı (konfiqurasiyada açılır), 11 fayl yaradılması, 13 reyestr dəyişməsi, 22 DNS sorğusu.
- **Ölçü:** həqiqi müsbət (true positive, TP), yanlış müsbət (false positive, FP), yanlış mənfi (false negative, FN). Dəqiqlik: 40 xəbərdarlığın 10-u zərərlidirsə, 10 / 40 = 25%. Tamlıq (recall) = TP / (TP + FN).

## İnsidentə cavab və bərpa

NIST SP 800-61 Rev. 3 (aprel 2025) cavabı NIST CSF 2.0 ilə əlaqələndirir; funksiyalar: Govern, Identify, Protect, Detect, Respond, Recover.

1. **Əhatə:** hansı cihaz və hesab təsirlənib; IoC-ləri bütün şəbəkədə axtar.
2. **Təcrid:** EDR ilə şəbəkədən ayır, söndürmə (yaddaşdakı sübut itməsin).
3. **Sübutu qoru:** yaddaş və disk görüntüsü, loglar, heşlər, sübut zənciri (chain of custody).
4. **Aradan qaldır:** zəiflik, davamlılıq, ikinci yüklər, icazəsiz hesablar; bütövlüyə əmin deyilsənsə, sıfırdan qur.
5. **Hesabları bərpa et:** parol təmiz cihazdan, sessiya tokenləri ləğv.
6. **Bərpa et və izlə:** yoxlanmış nüsxədən; eyni C2-yə cəhd çirkli nüsxə əlamətidir.

## Real hadisələr

- **WannaCry** (may 2017): SMB zəifliyi ilə yayılan qurd + şifrələyici; MS17-010 yamağı martda çıxmışdı. Dərs: yamaq və inventar.
- **NotPetya** (iyun 2017): Ukraynada M.E.Doc yenilənməsi ilə başladı, wiper kimi öyrənilir. Dərs: təchizatçıya nəzarətsiz imtiyaz verməmək.
- **Emotet:** bank troyanından başqa yükləri çatdıran modul infrastruktura çevrildi. Dərs: məktubu silmək yetmir, kim açdı, hansı yük endi araşdırılır.

:::exam
Sandbox-da sakit keçən test "təmizdir" demək deyil. DNS qeydi ilə DNS sorğu jurnalını qarışdırma. Parol dəyişmək tokeni ləğv etmir. IoC konkret dəyər, IoA davranışdır. Bərpa məxfilik araşdırmasını bitirmir.
:::
