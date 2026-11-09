+++
title = "Situasiya sualına necə cavab vermək"
unit = "strategiya"
order = 1
summary = "Situasiya sualına altı addımlı cavab şablonu və bir neçə mövzunu birləşdirən 16 situasiya cavabları ilə. İmtahan formatına ən yaxın hissə budur."
updated = 2026-11-09

[[source]]
title = "Midterm konspekti: \"Situasiya sualına necə cavab vermək\" və \"Qarışıq situasiya sualları\""
note = "Elmar Cabbarov, 2026–2027"
+++

Situasiya sualında tək düzgün söz axtarılmır, düşüncə ardıcıllığı yoxlanılır. Aşağıdakı altı addım demək olar hər suala uyğun gəlir. Sonrakı 16 situasiya bir neçə mövzunu birləşdirir; hər birində əvvəl cavabı özün qur, sonra açıb müqayisə et.

## Altı addım

| # | Addım | Özünə ver sual |
| --- | --- | --- |
| 1 | **Aktivi tap** | Nə qorunur? Tələbə məlumatı, qiymət jurnalı, imtahan sistemi, hesab? |
| 2 | **Nə baş verdiyini adlandır** | CIA-nın hansı xassəsi pozulub, hadisə DAD-ın hansı ünsürünə uyğundur? Hücumun adı nədir (fişinq, password spraying, evil twin)? |
| 3 | **Mərhələni və ya modeli göstər** | Kill Chain-in hansı mərhələsi? Kim, hansı alətlə (Diamond)? Bu təsdiqlənmiş faktdır, yoxsa fərziyyə? |
| 4 | **Kök səbəbi tap** | Hansı zəiflik: MFA yoxdur, minimal səlahiyyət pozulub, köhnə protokol, səhv konfiqurasiya, seqmentasiya yoxdur? |
| 5 | **Tədbir təklif et və təsnif et** | Dərhal nə edilməlidir (məhdudlaşdırma), sonra nə (aradan qaldırma, bərpa)? Tədbir fiziki/inzibati/texniki, qarşısını alan/aşkarlayan/düzəldəndir? |
| 6 | **Balansı və qalıq riski qeyd et** | Tədbir əlçatanlığa necə təsir edir? Nə risk qalır, kim qəbul etməlidir? |

:::example Qısa nümunə
*"Müəllimin hesabından gecə 03:00-da 40 tələbənin balı dəyişdirilib."*

- **Aktiv:** qiymət jurnalı. **Pozulan:** tamlıq (Alteration).
- **Model:** etibarlı hesabdan sui-istifadə (T1078), zaman anomaliyası.
- **Kök səbəb:** ehtimal ki, parol oğurlanıb, MFA yoxdur.
- **Tədbir:** sessiyaları ləğv et, parolu dəyiş, dəyişiklikləri audit logundan geri qaytar (düzəldən); MFA tətbiq et (qarşısını alan); gecə kütləvi dəyişiklik üçün SIEM qaydası yaz (aşkarlayan).
- **Qalıq risk:** MFA yorğunluğu, ona görə fişinqə davamlı MFA tövsiyə olunur.
:::

:::exam
Müşahidə ilə nəticəni ayır. "Böyük həcmdə yükləmə olub" faktdır; "məlumat oğurlanıb" fərziyyədir. Cavabda hansının təsdiqləndiyini, hansının yoxlanmalı olduğunu açıq yaz (Situasiya 13-ə bax).
:::

## Qarışıq situasiyalar

Hər situasiyanın yanında hansı mövzulara aid olduğu göstərilib.

### Situasiya 1 · Mövzu 1, 2, 3, 12

Qış sessiyasının son günü universitetin tələbə portalına gecə 02:00–02:40 arasında bir IP-dən 3 000 tələbə hesabının hər birinə 2 dəfə "Qis2026!" parolu ilə giriş cəhdi olur. 37 hesaba giriş uğurlu olur. Bu hesablardan 5-i tələbə şurası üzvlərinə məxsusdur və onlarla portalda başqa tələbələrin şəxsi məlumatlarına baxmaq mümkündür. Hücumu adlandır, pozulan xassələri, kök səbəbləri və tədbirləri yaz.

:::reveal Cavab
- **Hücum:** password spraying (hər hesaba az cəhd, hesab bloklanmasın deyə).
- **Pozulan:** 37 hesabda autentifikasiya; 5 imtiyazlı hesab vasitəsilə başqa tələbələrin məlumatına giriş mümkün olduğundan məxfilik (Disclosure riski).
- **Kök səbəblər (yoxlanmalı):** proqnozlaşdırıla bilən parollar (qara siyahı yoxlaması ya yoxdur, ya işləmir); MFA ya yoxdur, ya bu hesablarda tətbiq olunmayıb; tələbə şurası üzvlərinə artıq hüquq (minimal səlahiyyət və bilmək zərurəti pozulub); SIEM-də yalnız "bir hesabda N cəhd" qaydası var.
- **Dərhal:** IP-ni bloklamaq, 37 hesabın sessiyalarını ləğv edib parollarını sıfırlamaq, 5 imtiyazlı hesabın nəyə baxdığını audit logundan yoxlamaq.
- **Sonra:** MFA; NIST 800-63B-4 üzrə parol siyasəti (sızmış parolların qara siyahısı); "bir mənbədən çox fərqli hesaba uğursuz giriş" korrelyasiya qaydası; tələbə şurası üçün ayrıca məhdud rol (RBAC/ABAC).
:::

### Situasiya 2 · Mövzu 5, 10, 11, 12

Kafedra müdirinə "Attestasiya_nəticələri.xlsm" faylı gəlir. Fayl açılandan sonra EDR `excel.exe → powershell.exe → rundll32.exe` zəncirini göstərir, kompüter hər 60 saniyədən bir eyni xarici domenə qoşulur, iki gün sonra isə fayl serverinə qeyri-adi SMB bağlantıları başlayır. Hadisəni Kill Chain mərhələlərinə yerləşdir və hər mərhələdə hücumu harada dayandırmaq olardı?

:::reveal Cavab
| Mərhələ | Nə baş verdi | Harada dayandırmaq olardı |
| --- | --- | --- |
| Çatdırılma | Makrolu Excel faylı poçtla | E-poçt şlüzündə makrolu əlavələrin bloklanması, İnternetdən gələn fayllarda makroların qadağası |
| İstismar və quraşdırma | Excel PowerShell başladır, rundll32 ilə yük işə düşür | EDR qaydası (Office-dən skript icrasını bloklamaq, ASR qaydaları), tətbiqlərə nəzarət, adminsiz istifadəçi |
| C2 | 60 saniyəlik müntəzəm bağlantı (beacon) | DNS/proksi süzgəci, çıxan trafikin süzülməsi, SIEM-də beacon aşkarlaması |
| Yanal hərəkət (UKC-nin Through fazası) | Fayl serverinə SMB | Daxili seqmentasiya, iş stansiyalarından serverə SMB-ni məhdudlaşdırmaq |

**İndi:** kompüteri təcrid etmək, domeni bloklamaq, IoC-ləri bütün universitetdə axtarmaq, müdirin hesabını bərpa etmək, fayl serverində şifrələmə və ya oğurluq əlamətlərini yoxlamaq.
:::

### Situasiya 3 · Mövzu 6, 7, 8, 9

Universitetdə "UNI-Guest" (parolsuz, captive portal) və "UNI-Staff" (WPA2-PSK) şəbəkələri var. Pentest göstərir ki: qonaq şəbəkəsindən korpusdakı IP-kameraların idarəetmə panelinə çatmaq olur; qonaqlar bir-birinin cihazlarını görür; kafedra otağında divara qoşulmuş naməlum router "UNI-Staff" adını yayır. Problemləri tap və hər birinə tədbir yaz.

:::reveal Cavab
1. **Qonaq şəbəkəsi daxili seqmentlərdən ayrılmayıb.** Ayrı SSID kifayət deyil: qonaq VLAN-ından daxili şəbəkəyə firewall-da default deny, kameralar ayrıca IoT VLAN-ında olmalıdır.
2. **Müştəri izolyasiyası yoxdur və captive portal şifrələmə vermir.** Client isolation açılmalı, OWE (Enhanced Open) tətbiq edilməlidir.
3. **Naməlum router** həm rogue AP-dir (kabel şəbəkəsinə qoşulub), həm də universitetin SSID-sini təqlid etdiyi üçün evil twin ola bilər: WIPS ilə tapılıb çıxarılmalı, kabel portlarında 802.1X/NAC tətbiq edilməlidir.
4. **"UNI-Staff" WPA2-PSK ilə ortaq paroldadır.** WPA2/WPA3-Enterprise-a (802.1X, EAP-TLS və ya düzgün sertifikat yoxlamalı PEAP) keçmək, PMF-i aktivləşdirmək lazımdır.
:::

### Situasiya 4 · Mövzu 1, 4, 13, 14

Universitetin bütün sistemləri bir data mərkəzindəki iki hipervizorda işləyir. Ehtiyat nüsxə kimi gündəlik snapshot-lar eyni yaddaş massivində saxlanır. Ransomware vCenter admin hesabı vasitəsilə bütün VM-ləri və snapshot-ları şifrələyir. Rəhbərlik hədəf qoyur: imtahan sistemi 4 saatdan çox dayanmamalı, ən çox 1 saatlıq məlumat itə bilər. Nə səhv idi və yeni arxitektura necə olmalıdır?

:::reveal Cavab
- **Pozulan xassələr:** əlçatanlıq (Destruction/Denial) və tamlıq (Alteration).
- **Səhvlər:** snapshot ehtiyat nüsxə deyil və eyni massivdə idi; idarəetmə müstəvisi (vCenter) kifayət qədər qorunmamışdı (MFA, ayrıca VLAN); ehtiyat nüsxələr istehsalatla eyni icazə sahəsində idi.
- **Hədəflər:** RTO = 4 saat, RPO = 1 saat.
- **Yeni arxitektura:** saatlıq ehtiyat nüsxə və ya replikasiya (RPO üçün); ayrıca hesabda və ya buludda immutable nüsxə, 3-2-1 qaydası; imtahan sistemi üçün ikinci saytda və ya buludda ehtiyat mühit (RTO üçün); vCenter və hipervizor idarəsi ayrıca idarəetmə VLAN-ında, fişinqə davamlı MFA və PAM ilə; bərpa planı müntəzəm sınanmalı.
:::

### Situasiya 5 · Mövzu 2, 5, 10

Universitetin SOC-u AzScienceCERT-dən TLP:AMBER etiketli məlumat alır: təhsil sektoruna hücum edən qrupun 12 IP-si, 4 domeni, zərərli DLL-in heşi və "qrup ilkin giriş üçün saxta konfrans dəvətləri, sonra rundll32 ilə DLL yükləyir" təsviri. (a) Bu məlumatın hansı hissələri hansı kəşfiyyat növüdür? (b) Ağrı piramidasına görə hansını prioritet etmək lazımdır? (c) Məlumatı tələbə klubunun Telegram kanalında paylaşmaq olarmı?

:::reveal Cavab
- **(a)** IP, domen, heş texniki kəşfiyyatdır (IoC); ilkin giriş və icra üsulunun təsviri taktiki kəşfiyyatdır (TTP).
- **(b)** IoC-lər ucuz və tez tətbiq olunur, ona görə dərhal bloklanmalıdır, amma hücumçu onları asanlıqla dəyişir. Davamlı qoruma üçün piramidanın zirvəsi, yəni davranış prioritetdir: "rundll32-nin istifadəçi qovluğundan DLL yükləməsi" və "Office/poçt əlavəsindən sonra rundll32" üçün EDR və SIEM qaydaları.
- **(c)** Xeyr. TLP:AMBER yalnız öz təşkilatı və bilməli olan müştəriləri ilə paylaşmağa icazə verir. Açıq kanalda paylaşmaq üçün mənbə ilə razılaşıb TLP:CLEAR versiyası hazırlamaq lazımdır.
:::

### Situasiya 6 · Mövzu 3, 4, 7

Universitetin şəbəkə admini evdən korpus kommutatorlarına qoşulmaq üçün VPN istifadə edir, kommutatorlara isə Telnet ilə girir. Admin hesabı hamı üçün ortaqdır: "netadmin". Bir gün kommutatorlardan birinin konfiqurasiyası dəyişdirilir və bir korpus İnternetsiz qalır, kim etdiyini heç kim bilmir. Hansı prinsiplər pozulub?

:::reveal Cavab
- **Hesabatlılıq (accountability):** ortaq hesab əməliyyatı konkret şəxsə bağlamağa imkan vermir, ona görə inkaredilməzlik də yoxdur.
- **Məxfilik:** VPN tuneli yalnız ev ilə VPN şlüzü arasını qoruyur; şlüzdən kommutatora qədər Telnet parolu açıq mətnlə gedir.
- **Dəyişikliklərin idarəsi** (inzibati tədbir) yoxdur.
- **Həll:** hər admin üçün fərdi hesab; mərkəzi AAA ilə fərdi autentifikasiya və hər əmrin auditini dəstəkləyən TACACS+; Telnet əvəzinə SSH; VPN-də MFA; idarəetmə yalnız jump host və ya idarəetmə VLAN-ından; dəyişikliklər üçün təsdiq proseduru və konfiqurasiyanın ehtiyat nüsxəsi.
:::

### Situasiya 7 · Mövzu 1, 3, 14

Müəllim imtahan suallarını Google Drive-da "linki olan hər kəs görə bilər" rejimində saxlayır və linki assistentə poçtla göndərir. İmtahandan bir gün əvvəl suallar tələbə qruplarında yayılır. Hansı xassə pozulub, kim cavabdehdir və necə qarşısını almaq olardı?

:::reveal Cavab
- **Pozulan:** məxfilik (Disclosure).
- **Cavabdeh:** ortaq məsuliyyət modelinə görə SaaS-da paylaşma parametrləri müştərinin, yəni universitetin və konkret istifadəçinin məsuliyyətidir; Google-un təhlükəsizlik problemi deyil.
- "Linki olan hər kəs" link sızan kimi hər kəsə giriş verir: bilmək zərurəti prinsipi pozulub.
- **Tədbirlər:** yalnız adla göstərilmiş şəxslərə paylaşma; universitet domenindən kənara paylaşmanın admin səviyyəsində bağlanması; həssas fayllar üçün DLP etiketləri; Drive audit loglarında girişləri araşdırmaq (anonim istifadəçilərin kimliyi loglardan bilinməyə bilər); müəllimlərə qısa təlim.
:::

### Situasiya 8 · Mövzu 6, 10, 12

Perimetrdəki NIDS heç bir xəbərdarlıq vermir, amma NetFlow analizi göstərir ki, kompüter laboratoriyasındakı bir kompüter gecə ərzində universitetin 200 daxili IP-sinə 445 və 3389 portları ilə qoşulmağa çalışıb. Niyə NIDS bunu görmədi və bu nə ola bilər?

:::reveal Cavab
- **Niyə görmədi:** perimetr NIDS yalnız şimal–cənub (xarici) trafiki görür, bu isə daxildə şərq–qərb trafikidir.
- **Nədir:** daxili kəşf (discovery, şəbəkə skanı) və yanal hərəkətə hazırlıq; ola bilsin qurd tipli zərərli proqram (SMB və RDP portları). Bu, anomaliya əsaslı aşkarlamadır (NBA).
- **Tədbirlər:** kompüteri təcrid etmək və analiz etmək; laboratoriya VLAN-ından digər seqmentlərə SMB/RDP-ni firewall ilə bağlamaq; daxili seqmentlər arasında da sensor (IDS və ya EDR) qoymaq; "bir hostdan qısa müddətdə çox daxili hosta bağlantı" SIEM qaydası yazmaq.
:::

### Situasiya 9 · Mövzu 3, 9, 11

Universitetin rəsmi tabletləri dekanlıqlarda istifadə olunur, MDM yoxdur, ekran kilidi istəyə bağlıdır. Bir tablet itir; içində tələbə siyahıları və "UNI-Staff" Wi-Fi parolu saxlanıb. Nə etmək lazımdır və gələcək üçün hansı nəzarətlər qurulmalıdır?

:::reveal Cavab
- MDM olmadığından universitetin mərkəzi uzaqdan kilidləmə və silmə imkanı yoxdur (cihazda Find My kimi xidmətin aktiv olub-olmadığı yoxlanmalıdır). Ekran kilidi yoxdursa, tələbə siyahıları açıqdır (məxfilik).
- **Dərhal:** tabletdəki hesabların parollarını dəyişmək və sessiyalarını ləğv etmək; ortaq Wi-Fi parolunu dəyişib bütün cihazlara yenidən yazmaq (PSK-nın zəif cəhəti budur); insidenti qeydə almaq və lazım olsa sızma barədə bildiriş vermək.
- **Gələcək üçün:** bütün korporativ mobil cihazlar MDM-də (məcburi PIN, şifrələmə, uzaqdan silmə); Wi-Fi üçün 802.1X və cihaz sertifikatları (itən cihazın sertifikatı ayrıca ləğv edilir); cihaz uçotu.
:::

### Situasiya 10 · Mövzu 4, 6, 7

Universitet yeni tələbə portalını istifadəyə verir. Arxitektor təklif edir: portal serveri və verilənlər bazası eyni serverdə, daxili şəbəkədə dursun, İnternetdən portala firewall-da 80 və 443 portları birbaşa açılsın. Bu dizaynı təhlükəsizlik baxımından təhlil et və daha yaxşısını təklif et.

:::reveal Cavab
- **Problemlər:** İnternetə açıq server daxili şəbəkədədir, sındırılsa hücumçu birbaşa daxildədir; baza ilə veb eyni serverdədir, veb zəifliyi bazanı da açır; 80-ci port şifrəsiz HTTP-dir.
- **Təklif:**
  - DMZ-də reverse proksi və ya WAF: yalnız 443, TLS 1.2/1.3, HSTS; 80 yalnız 443-ə yönləndirmə.
  - Tətbiq serveri ayrı seqmentdə.
  - Verilənlər bazası daxili DB zonasında, ona yalnız tətbiq serverindən TCP 5432 (və ya 1433/3306) ilə giriş.
  - İdarəetmə yalnız VPN və jump host vasitəsilə.
  - Firewall-da default deny və egress süzgəci.
- Bu, çoxsəviyyəli müdafiədir: bir qat aşılanda növbəti qat hücumu saxlayır.
:::

### Situasiya 11 · Mövzu 1, 3

Universitetin tələbə sistemində tələbə öz profilinə baxanda URL belədir: `/students/profile?id=22051`. Bir tələbə id-ni 22052-yə dəyişib başqa tələbənin ünvanını, telefonunu və qiymətlərini görür. Bu hansı növ problemdir? Autentifikasiyamı, avtorizasiyamı?

:::reveal Cavab
- Tələbə sistemə düzgün daxil olub, yəni **autentifikasiya işləyir**. Problem **avtorizasiyadadır**: server sorğu olunan obyektin həmin istifadəçiyə aid olub-olmadığını yoxlamır.
- Bu, IDOR (Insecure Direct Object Reference) zəifliyi, yəni üfüqi imtiyaz artırılmasıdır. Pozulan xassə məxfilikdir.
- Tam vasitəçilik (complete mediation) prinsipi pozulub: hər müraciətdə icazə yoxlanmalıdır.
- **Həll:** server tərəfində obyekt səviyyəli icazə yoxlaması (istifadəçi yalnız öz id-sinə baxa bilər); proqnozlaşdırılmayan identifikatorlar köməkçi tədbir kimi; belə müraciətlərin loglanması və SIEM-də "bir istifadəçinin çox fərqli profilə baxması" qaydası.
:::

### Situasiya 12 · Mövzu 2, 4, 12

İmtahan qeydiyyatı açılan gün universitet portalı 2 saat əlçatmaz olur: 15 000 müxtəlif IP-dən saniyədə yüz minlərlə sorğu gəlir. Eyni vaxt bir haktivist qrup sosial şəbəkədə hücumu öz üzərinə götürür. Hücumu təsnif et və tədbirləri qısa və uzunmüddətli olaraq ayır.

:::reveal Cavab
- **Təsnif:** DDoS hücumu, pozulan xassə əlçatanlıqdır (Denial). Trafik botnetdən və ya əks etdirmə/gücləndirmə vasitəsilə gələ bilər. Haktivist qrupun iddiası (siyasi motiv) atribusiya üçün ayrıca yoxlanmalı fərziyyədir.
- Yerli firewall və ya IPS kanal tam dolanda kömək etmir: trafik universitetə çatmazdan əvvəl xətti doldurur.
- **Qısa müddətli:** provayderlə əlaqə, yuxarı səviyyədə süzgəc (upstream filtering), bulud DDoS qoruması və ya CDN arxasına keçid, sorğu limitləri.
- **Uzunmüddətli:** portalı CDN/WAF arxasında saxlamaq, kritik tarixlərdə tutum ehtiyatı, DDoS cavab planı, SIEM-də trafik həcmi üçün anomaliya xəbərdarlığı, təhdid kəşfiyyatı ilə haktivist kampaniyalarını izləmək.
:::

### Situasiya 13 · Mövzu 5, 12

SIEM 09:05-də xəbərdarlıq verir: "Mühasibatlıq əməkdaşı 2 saatda 15 GB məlumatı xarici bulud xidmətinə yüklədi." Analitik hesabatına yazır: "Məlumat oğurlanıb, daxili təhdiddir, əməkdaş işdən çıxarılmalıdır." Bu nəticəni qiymətləndir.

:::reveal Cavab
- Analitik **müşahidəni nəticə kimi** təqdim edib. Təsdiqlənən yalnız böyük həcmdə yükləmədir.
- "Oğurluq" və "daxili təhdid" fərziyyədir. Alternativ izahlar: təsdiqlənmiş ehtiyat nüsxə, maliyyə hesabatının auditora göndərilməsi, oğurlanmış hesabla xarici hücumçunun işi.
- **Yoxlanmalı:** hansı fayllar; hansı xidmət (universitetin təsdiqlənmiş buludu, yoxsa şəxsi hesab); giriş adi cihazdan və MFA ilə olubmu; əməkdaşın rəhbəri bu işdən xəbərdardırmı.
- Araşdırma qanuni və etik çərçivədə, HR və hüquq şöbəsi ilə aparılır. UEBA anomaliyanı göstərir, niyyəti sübut etmir.
:::

### Situasiya 14 · Mövzu 8, 9, 13

Kibertəhlükəsizlik klubu tələbələrə Wi-Fi hücumlarını öyrətmək üçün laboratoriya qurmaq istəyir: tələbələr WPA2 əl sıxmasını yazıb parolu sındırmağı və evil twin qurmağı öyrənəcək. Bunu universitet şəbəkəsində təhlükəsiz və qanuni etmək üçün hansı şərtlər lazımdır?

:::reveal Cavab
- Hücumlar yalnız klubun öz, ayrıca test AP-lərinə qarşı aparılır: universitetin real şəbəkələrinə və ya başqalarının cihazlarına qarşı icazəsiz hücum qanunsuzdur.
- Yazılı icazə və qaydalar (rules of engagement) olmalıdır.
- Test AP-ləri real SSID-ləri ("UNI-Staff", "eduroam") təqlid etməməli, aşağı güclə və mümkünsə ekranlanmış otaqda işləməlidir ki, kənar istifadəçilər qoşulmasın.
- Laboratoriya şəbəkəsi universitet şəbəkəsindən tam ayrı olmalı, VM-lər host-only rejimdə işləməlidir.
- Universitetin WIPS-i bu AP-ləri tanıyıb istisna kimi qeyd etməlidir ki, SOC yanlış həyəcan almasın.
- Dərsin sonunda tədbirlər də öyrədilir: WPA3-SAE, Enterprise rejim, PMF, server sertifikatının yoxlanması.
:::

### Situasiya 15 · Mövzu 1, 2, 5, 14

Tələbə layihəsi üçün yaradılmış universitet AWS hesabının giriş açarı GitHub-da açıq repozitoriyaya düşür. 20 dəqiqə sonra hesabda 40 güclü server açılır və aylıq hesab 18 000 dollara çatır. Hücumçu kimdir, pozulan nədir və bunun qarşısını necə almaq olardı?

:::reveal Cavab
- **Hücumçu:** çox güman ki, açıq repozitoriyalardakı açarları avtomatik axtaran botlar işlədən pul motivli cinayətkarlar. Belə hallarda serverlər adətən kriptovalyuta hasilatı üçün açılır, amma bunu CloudTrail və serverlərin prosesləri ilə təsdiqləmək lazımdır.
- **Pozulan:** açarın məxfiliyi, resursların icazəsiz istifadəsi (maliyyə ziyanı); açarın geniş hüquqları varsa, məlumatın məxfiliyi və tamlığı da riskdədir. Ortaq məsuliyyət modelinə görə bu, müştərinin məsuliyyətidir.
- **Dərhal:** açarı deaktiv etmək, açılan resursları silmək, CloudTrail-dən başqa nə edildiyini yoxlamaq, provayderə müraciət.
- **Qarşısını almaq:** uzunmüddətli açar əvəzinə rollar və qısa ömürlü tokenlər; minimal icazələr; sirləri kodda saxlamamaq (secret scanning, pre-commit yoxlaması); büdcə xəbərdarlıqları və xidmət kvotaları; tələbə hesablarının əsas hesabdan ayrılması.
:::

### Situasiya 16 · Mövzu 1, 3, 4, 11

Universitetin server otağı zirzəmidədir, qapısı adi açarla açılır, açar mühafizəçidə və üç İT işçisindədir. Otaqda su sızma sensoru yoxdur, UPS 10 dəqiqəlik enerji verir, generator yoxdur. Yağışlı gündə su otağa daxil olur və elektrik kəsilir. Fiziki və ətraf mühit tədbirlərini təhlil et.

:::reveal Cavab
- **Zəifliklər:** yer seçimi (zirzəmi, daşqın riski); girişə nəzarət zəifdir (adi açar, kimin nə vaxt daxil olduğu bilinmir, hesabatlılıq yoxdur); aşkarlayan tədbir yoxdur (su sensoru, temperatur sensoru); enerji davamlılığı çatışmır (10 dəqiqəlik UPS yalnız düzgün söndürməyə yetir, generator yoxdur).
- **Pozulan:** əlçatanlıq; avadanlıq zədələnsə məlumat itkisi ilə tamlıq da risk altındadır.
- **Tədbirlər:** kartla giriş və giriş jurnalı; kamera (fiziki, aşkarlayan və çəkindirən); su sızma və temperatur sensorları xəbərdarlıqla; avadanlığın döşəmədən yuxarı qaldırılması; UPS + generator; uzunmüddətli olaraq otağın daha yüksək mərtəbəyə köçürülməsi və ya kritik sistemlərin ehtiyat sayta (və ya buluda) replikasiyası.
:::
