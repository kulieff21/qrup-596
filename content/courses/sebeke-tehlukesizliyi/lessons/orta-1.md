+++
title = "Şəbəkə təhlükəsizliyinin əsasları: CIA və DAD triadası"
unit = "orta"
order = 1
summary = "Hər anlayış 1–3 cümlə ilə: informasiya və verilənlər, CIA və DAD, autentiklik, AAA, təhdid–zəiflik–risk, riskə cavab, layihələndirmə prinsipləri, təsnifat, OSI/TCP/IP və üç tanınmış hadisə."
updated = 2026-11-09

[[source]]
title = "Mühazirə 1: Şəbəkə təhlükəsizliyinin əsasları: CIA və DAD triadası"
note = "Elmar Cabbarov, 2026–2027"
+++

Bu mövzu bütün kursun lüğətidir: sonrakı mövzularda hər hücumu və müdafiə vasitəsini bu üç hərfə bağlayacağıq, yəni hansı xassəni pozur, hansını qoruyur. Universitet topologiyası, adlar və rəqəmlər şərti tədris nümunəsidir.

## İnformasiya, verilənlər və bilik

**Verilənlər** (*data*) məlumatın saxlanma və emal üçün formal təsviridir (`score=85`). **İnformasiya** hadisə, obyekt və proses haqqında məna daşıyan məlumatdır: rəqəmlərin fənnin yekun nəticəsi olduğu bilinəndə yaranır. **Bilik** (*knowledge*) informasiyanı əlaqələndirib qərar verməyə imkan verən qaydalar və təcrübədir. Təhlükəsizlik həm rəqəmləri, həm kontekstini qorumalıdır: bal dəyişməsə də başqa tələbənin identifikatoruna bağlanarsa, nəticə yanlışdır.

**Kodlaşdırma, sıxılma və şifrələmə eyni deyil.** UTF-8 və Base64 kodlaşdırmadır, hər kəs ilkin məzmunu bərpa edə bilər; sıxılma da məxfilik vermir. Yalnız şifrələmə məzmunu açarla qoruyur.

İnformasiyanın keyfiyyət xassələri (düzgünlük, dolğunluq, aktuallıq, aydınlıq, faydalılıq) təhlükəsizlik xassələrini əvəz etmir. Bütün tələbələrin adı olmayan siyahı ilkin olaraq belə hazırlanıbsa, bu keyfiyyət qüsurudur; hücumçu adları silibsə, **tamlıq pozuntusudur**. Tarixən yazı, çap (Qutenberq), teleqraf, telefon, radio və ARPANET informasiyanın yayılmasını genişləndirib; rəqəmsal sənəd isə asanlıqla çoxalır, daşıyıcı köhnəlir, format və açarlar itir, ona görə uzunmüddətli saxlama yoxlama, miqrasiya və ehtiyat nüsxə tələb edir.

## İnformasiya təhlükəsizliyinin əhatəsi

**İnformasiya təhlükəsizliyi** (*information security*) məxfiliyi, tamlığı və əlçatanlığı qoruyan idarəetmə vəziyyəti və fəaliyyətlərdir; kağız tələbə işi və bağlı şkaf buraya aiddir. **Şəbəkə təhlükəsizliyi** (*network security*) rabitə infrastrukturunu və şəbəkə xidmətlərini, **kibertəhlükəsizlik** (*cybersecurity*) rəqəmsal sistemləri və onların əlaqələrini qoruyur.

**Aktiv** (*asset*) təşkilat üçün dəyəri olan hər şeydir: tələbə bazası, qiymət jurnalı, diplom reyestri, avadanlıq, əməkdaşların təcrübəsi, xidmətə etimad. Aktivin dəyəri qiymətinə bərabər deyil: ucuz diskdəki yeganə dissertasiya nüsxəsi bahalı ehtiyat serverdən vacib ola bilər. Məqsəd resursu bağlamaq yox, **icazəli istifadəyə uyğun qorumaqdır**.

Təhlükəsizlik dörd səviyyədə tətbiq olunur: şəxs, təşkilat, cəmiyyət, dövlət. Tədbirlər üç növdür: **inzibati** (qayda və qərar), **texniki** (giriş nəzarəti, şifrələmə, audit) və **fiziki** (daşıyıcı və avadanlıq). Təhlükəsizlik tələbi xidmətin layihəsindən başlayır; sonradan alınmış məhsul məsuliyyət bölgüsünü düzəltmir.

## CIA triadası

CIA üç xassənin baş hərfləridir. Hər birinin Azərbaycan dilində bir neçə adı var.

| Xassə | Mənası | Pozulma | Qoruyan vasitələr |
| --- | --- | --- | --- |
| Məxfilik (*confidentiality*, konfidensiallıq) | Məlumatı yalnız icazəli subyekt görür | Sızma, dinləmə, səhv ünvana məktub, açıq paylaşım | Şifrələmə, girişə nəzarət, MFA, təsnifat |
| Tamlıq (*integrity*, bütövlük) | Məlumat icazəsiz və ya təsadüfi dəyişdirilməyib, mənbəyi doğrudur | Bank köçürməsində məbləğin dəyişməsi, saytın üzünün dəyişdirilməsi (defacement) | Heş, rəqəmsal imza, HMAC, versiya nəzarəti, loglar |
| Əlçatanlıq (*availability*, əlyetənlik) | İcazəli istifadəçi xidməti münasib vaxtda alır | DDoS, ransomware, elektrik kəsintisi, disk qəzası | Ehtiyat nüsxə, RAID, klaster, UPS, DDoS qoruması |

:::tip Hansı vasitə hansı xassəni qoruyur
Şifrələmə → məxfilik. Heş və imza → tamlıq. Ehtiyat nüsxə və artıqlıq (*redundancy*) → əlçatanlıq. Heş məlumatı gizlətmir, yalnız dəyişib-dəyişmədiyini göstərir.
:::

**Məxfilik** "heç kimə verməmək" deyil: tələbənin nəticəsini ona göstərmək icazəlidir. Sızma daxili əməkdaşdan, oğurlanmış xidmət hesabı açarından və ya açıq ehtiyat nüsxədən də gələ bilər, buna görə məxfilik bütün nüsxələrə və ötürmə yollarına aiddir. Disk şifrələməsi oğurlanmış daşıyıcını qoruyur, işləyən serverdəki icazəli tətbiqi yox; açar eyni qovluqda saxlanırsa faydası itir. Məxfilik fərdi həyatın toxunulmazlığı ilə eyni deyil.

:::example HTTPS var, amma sızma var
LMS-də `GET /api/results/142` sorğusunda server yalnız girişi yoxlayıb identifikatorun kimə aid olduğunu yoxlamırsa, başqa tələbənin nəticəsi görünür. HTTPS kanalı qoruyur, bu xətanı yox. Çatışan tədbir **obyekt səviyyəsində avtorizasiyadır**.
:::

**Tamlıq** nəzarət edilən dəyişikliyi tələb edir, dəyişməzliyi yox. **Heş** (*hash*) məlumatdan sabit ölçülü xülasə çıxarır (SHA-256); xülasə dəyişibsə, fayl dəyişib. Etalon xülasə ayrıca qorunmalıdır, çünki hücumçu həm faylı, həm heşi dəyişə bilər. **HMAC** xülasəni gizli açarla bağlayır, amma açarı paylaşan hər tərəf kod yarada bildiyindən müəlliflik üçün üçüncü tərəfə sübut vermir. **Rəqəmsal imza** (*digital signature*) şəxsi açarla yaradılır, açıq açarla yoxlanır və müəlliflik sübutuna yarayır. İmza səhv daxil edilmiş qiyməti həqiqətə çevirmir; iş prosesi, rol nəzarəti və dəyişiklik tarixçəsi lazımdır.

**Əlçatanlıq** xidmətin istifadəçi üçün işləməsidir: ad həlli, şəbəkə yolu, identifikasiya və baza da işləməlidir. Paylanmış xidmətdən imtina (*distributed denial of service*, DDoS) kanalı və ya resursu tükədir; mənbə IP-yə görə sərt bloklama yataqxana kimi paylaşılan IP-dən çıxan tələbələri də imtahandan uzaqlaşdırır.

| Vasitə | İşi | Sərhədi |
| --- | --- | --- |
| Ehtiyat nüsxə (*backup*) | İtirilmiş vəziyyəti bərpa edir | Ayrı saxlanmalı, bərpası yoxlanmalıdır |
| Artıqlıq | Komponent sıradan çıxanda xidmət davam edir | Eyni asılılıq hamısını dayandıra bilər |
| RAID | Bəzi disk nasazlıqlarına qarşı | Ehtiyat nüsxənin əvəzi deyil, silinmə massivdə də görünür |
| Replikasiya | Başqa serverdə nüsxə | Zərərli dəyişikliyi də ötürür |

**RTO** (*recovery time objective*) xidmətin nə qədər müddətdə bərpa olunmalı olduğunu, **RPO** (*recovery point objective*) qəbul edilən məlumat itkisini ifadə edir: RTO 2 saat, RPO 15 dəqiqədirsə, xidmət iki saatda qayıtmalı, itki son 15 dəqiqədən çox olmamalıdır. Rəqəmləri satıcı yox, prosesin sahibi əsaslandırır.

**Xassələr arasında balans.** Hər səhifədə MFA tələb etmək girişə mane olur; daha yaxşı seçim həssas əməliyyatda əlavə yoxlama və məhdud sessiyadır. Kritik xassə sistemdən asılıdır: şəxsi işlər → məxfilik, qiymət jurnalı və diplom reyestri → tamlıq, imtahan günü test sistemi → əlçatanlıq, açıq dərs cədvəli → tamlıq və əlçatanlıq.

## DAD triadası

DAD pozuntu tərəfindən baxır: **ifşa** (*disclosure*, məxfiliyi pozur), **dəyişdirmə** (*alteration*, tamlığı pozur), **məhv etmə** (*destruction*) və ya xidmətdən imtina (*denial*, əlçatanlığı pozur). CIA qorunan xassəni, DAD baş verən nəticəni adlandırır: "nə baş verdi?" → DAD, "nə pozuldu?" → CIA. Məhv etmə ilə imtina eyni deyil, çünki məlumatı silmədən də ona girişi dayandırmaq olar.

:::figure
src = "m01-1.png"
alt = "CIA xassələri, universitet nümunələri və DAD nəticələri üç sıra ilə bağlanır."
caption = "Qorunan CIA xassələrinin DAD nəticələri ilə uyğunluğu."
:::

Bir hücum bir neçə xassəni poza bilər. **Ransomware** faylları şifrələyəndə tamlıq və əlçatanlıq pozulur; əvvəl məlumat çıxarılıbsa, məxfilik də. Şifrələnmiş fayl görmək oğurluğu sübut etmir, ifşa çıxış trafiki və oxuma qeydləri ilə təsdiqlənir. Əvvəl oğurlayıb sonra şifrələmə **ikiqat qəsb** (*double extortion*) adlanır. Fayl serverində əmrlərin açılmaması ransomware, disk xətası, yanlış icazə və ya açar itkisi ola bilər: əlaməti səbəblə qarışdırmaq yanlış tədbirə aparır. Tədbir də xassəyə uyğun seçilir: ehtiyat nüsxə ifşanı geri almır, şəbəkə bloklaması bazada edilmiş dəyişikliyi düzəltmir.

## CIA-dan kənar xassələr

| Xassə | Cavab verdiyi sual | Vasitə | Sərhəd |
| --- | --- | --- | --- |
| Autentiklik (*authenticity*) | Mənbə iddia edilən mənbədirmi? | İmza, sertifikat | Dəyişiklik aşkarlanmaması mənbənin doğruluğu demək deyil |
| İnkaredilməzlik (*non-repudiation*) | Mənşə barədə sonradan hansı sübut var? | Rəqəmsal imza, vaxt möhürü, qeyd zənciri | Açarın kimdə olduğu araşdırılır |
| Hesabatlılıq (*accountability*) | Əməliyyatı hansı subyekt edib? | Fərdi hesab, qorunan audit | Paylaşılan və ya oğurlanmış hesab əlaqəni pozur |

**Autentifikasiya** (*authentication*) kimlik iddiasının yoxlanmasıdır; sənədin autentikliyi ayrıca yoxlanır: tələbə hesabla daxil olub saxta arayış yükləyibsə, giriş sənədi həqiqi etmir. İnkaredilməzlik "təxirə salınmamaq" deyil, mənşəyi sonradan inkar etməyə qarşı sübutdur; açar oğurlana bilər. Qiymət düzəlişinin təsdiqi üçün bazada `approved=true` zəif sübutdur; versiya, hesab, vaxt və əsas birlikdə saxlanmalı, güclü sübut üçün konkret versiya imzalanmalıdır.

**Parker heksadı** (*Parkerian hexad*) altı xassədir: CIA + **sahiblik və nəzarət** (*possession or control*), autentiklik və **faydalılıq** (*utility*). Şifrəli disk oğurlananda nəzarət itir, məxfilik açarın qorunmasından asılıdır; açarı itmiş arxiv endirilsə də yararsızdır, bu faydalılıq itkisidir. Konspektə görə heksadı tanımaq kifayətdir.

## AAA

AAA üç ayrı qərardır: **autentifikasiya** (kim olduğunu yoxlayır), **avtorizasiya** (*authorization*, bu əmələ icazəsi varmı) və fəaliyyətin uçotu (*accounting*, nə, nə vaxt, hansı nəticə ilə). Şəbəkə girişi ilə tətbiq icazəsi ayrıdır: Wi-Fi-a qoşulmaq tələbə bazasına yazmaq hüququ vermir. Tipik səhvlər: uğurlu girişi bütün hüquqlar saymaq, icazəni yalnız interfeysdə gizlətmək (yoxlama serverdə, hər sorğuda aparılır), uçotda parol yazmaq.

**Çoxamilli autentifikasiya** (*multi-factor authentication*, MFA) fərqli kateqoriyaları birləşdirir: bilinən sirr, sahib olunan vasitə, biometrik xüsusiyyət. İki parol MFA deyil. Hesabın bərpası zəifdirsə, MFA keçilə bilər. Oğurlanmış sessiya identifikatoru yoxlanmış kimliyi təqlid edir, ona görə sessiya müddəti, ləğv və həssas əməliyyatda təkrar yoxlama lazımdır.

**RBAC** (*role-based access control*) icazələri vəzifə rollarına, **ABAC** (*attribute-based access control*) isə fənn, semestr, cihaz vəziyyəti, vaxt kimi atributlara bağlayır. Audit qeydi (kim, nə, köhnə/yeni dəyər, nəticə) iz verir, qanunilik sübut etmir; parol və sessiya sirləri qeydə yazılmır, audit anbarı özü də qorunan aktivdir.

## Təhdid, zəiflik, risk, insident

| Termin | Mənası | Universitet nümunəsi |
| --- | --- | --- |
| Təhdid (*threat*) | Aktivə zərər vura biləcək potensial hadisə və ya şərait; mənbəyi hücumçu və ya daşqın ola bilər | Balını qaldırmaq istəyən tələbə |
| Zəiflik (*vulnerability*) | İstifadə oluna bilən çatışmazlıq | İxracda icazə yoxlanmır, "123456" parolu |
| Risk (*risk*) | Zərərin ehtimalı və təsiri | Balın dəyişməsi ehtimalı və nəticəsi |
| Hücum (*attack*) | Qəsdli cəhd | İcazəsiz ixrac sorğusu |
| Eksploit (*exploit*) | Zəiflikdən istifadə üsulu və ya kodu | CVE üçün yazılmış skript |
| Hadisə (*event*) | Müşahidə edilən fakt | Server sorğunu qeydə alır |
| İnsident (*security incident*) | Təhlükəsizliyi pozan və cavab tələb edən hadisə | Balın həqiqətən dəyişdirilməsi |
| Tədbir (*control*) | Riski azaldan texniki, inzibati və ya fiziki addım | MFA, parol siyasəti |

:::exam Tələ
Hər hadisə insident deyil: gündə milyonlarla log yazısı yaranır, yalnız bir qismi insidentdir. "Server yamanmayıb" zəiflikdir, "kimsə istifadə edə bilər" təhdiddir, "baş versə bazanın sızması və cərimə" riskdir. Açıq portun özü həmişə zəiflik deyil.
:::

**Təhdidlər** mənşəyə (təbii, texniki, insan), niyyətə (qəsdli, qəsdsiz), yerləşməyə (daxili, xarici), təsirə (passiv, aktiv), hədəf xassəyə və zərərin növünə görə təsnif edilir. Daxili/xarici bölgüdə podratçı xarici ola-ola imtiyazlı hesabla daxil ola bilər; fişinqlə hesab alan xarici hücumçu daxili aktor deyil; mənbəsiz faizlər işlədilmir. **Passiv hücum** yalnız dinləyir və izi çətin tapılır (qarşısı şifrələmə ilə alınır), **aktiv hücum** məlumatı dəyişir və ya resursu tükədir; aktiv hücuma qarşı da giriş yoxlaması, sürət məhdudiyyəti və seqmentləşdirmə (*segmentation*) var, aşkarlama və bərpa isə ikisi üçün lazımdır.

## Risk və riskə cavab

Əvvəl qiymətləndirmənin sərhədi seçilir, sonra aktiv, təhdid və zəiflik yazılır. Yaxşı risk cümləsi səbəbi nəticəyə bağlayır: "ixracda obyekt üzrə icazə yoxlanmadığı üçün başqalarının sənədləri çıxarıla və fərdi məlumat sızması baş verə bilər". **Risk balı = ehtimal × təsir** (hər biri 1–5): ixrac 4×5 = 20, qısa kataloq nasazlığı 4×2 = 8, ağır yanğın 1×5 = 5. Bu dəqiq ehtimal deyil, prioritet şkalasıdır; aşağı hasilli yanğın insan təhlükəsizliyi və hüquqi tələblərə görə yenə nəzərə alınır.

**Kəmiyyət yanaşması:** kəsinti zərəri 2 000 AZN, illik tezlik 3 → illik gözlənilən itki 6 000 AZN; 1 500 AZN-lik tədbir tezliyi 1-ə endirirsə, qalan itki 2 000 + tədbir 1 500 = 3 500 AZN. Nadir böyük və pulla ölçülməyən itkini tam əhatə etmir.

| Strategiya | Mənası | Nümunə |
| --- | --- | --- |
| Azaltmaq (*mitigate*) | Ehtimalı və ya təsiri endirmək | MFA, ixrac nəzarəti, bərpa nüsxəsi |
| Yayınmaq (*avoid*) | Riski yaradan fəaliyyəti dayandırmaq | Lazımsız açıq paylaşımı bağlamaq |
| Ötürmək (*transfer*) | Maliyyə nəticəsini müqavilə ilə bölüşmək | Kiber sığorta, autsorsinq; məsuliyyət tam itmir |
| Qəbul etmək (*accept*) | Qalan riski səlahiyyətli qərarla saxlamaq | Az təsirli kataloq kəsintisi, yazılı qərar |

Tədbirdən sonra qalan risk **qalıq risk**dir (*residual risk*); sıfır risk yoxdur, sahibi və təkrar baxış tarixi olmalıdır. **Risk reyestri** (*risk register*) aktiv, ssenari, əsas, sahib, son tarix və qalıq riski saxlayır; tədbirin işlədiyi sınaqla (uğurlu bərpa) göstərilməlidir.

## Layihələndirmə prinsipləri

- **Minimum səlahiyyət** (*least privilege*): lazım olan hüquq, lazım olan resursda, lazım olan müddətə; xidmət hesabına da aiddir, hüquqlar müvəqqəti verilir və vaxtında götürülür.
- **Vəzifələrin ayrılması** (*separation of duties*): müraciət, təsdiq və icra ayrı subyektlərdədir; eyni hesab hər ikisini basa bilirsə, ayrılma yoxdur.
- **Dərinlik üzrə müdafiə** (*defense in depth*): bir tədbirin uğursuzluğu hamısını dağıtmır; ortaq açar və ortaq administrator gizli asılılıqdır.
- **Təhlükəsiz imtina** (*fail-secure*): nasazlıqda giriş nəzarətsiz açılmır (icazə serveri yoxdursa yazma rədd edilir). **Fail-safe** isə insan təhlükəsizliyidir: yanğın çıxışı enerji kəsiləndə açıq qalır.
- **Tam vasitəçilik** (*complete mediation*): hər həssas əməliyyatda icazə yoxlanır, yalnız girişdə yox.
- **Hücum səthinin azaldılması** (*attack surface reduction*): işlənməyən xidmət və hesablar bağlanır.
- **Sıfır etibar** (*zero trust*): şəbəkədəki yerə görə etimad yoxdur (NIST SP 800-207); qərara kimlik, cihaz vəziyyəti, resurs həssaslığı və sessiya konteksti daxildir. Bu, VPN-in və ya bir məhsulun adı deyil; mərhələli keçid həssas xidmət və imtiyazlı girişdən başlayır.

## Məlumatların təsnifatı və həyat dövrü

**Məlumatların təsnifatı** (*data classification*) məzmunu həssaslığa görə qruplaşdırır; adlar siyasətdən asılıdır. Şərti model: açıq, daxili, məxfi (qiymətlər), ciddi məhdud (imtahan sualları, imza açarları). **Məlumat sahibi** (*data owner*) məqsəd və qoruma tələbini müəyyən edir, **saxlayıcı** (*custodian*) onu sistemdə tətbiq edir; İT-nin texniki imkanı oxumaq hüququ vermir. Etiket nüsxələrə daşınır, dəyişməsi səlahiyyətli qərar tələb edir.

Məlumat üç vəziyyətdə olur: **sükunətdə** (*data at rest*), **ötürülərkən** (*data in transit*) və **istifadədə** (*data in use*). Şifrəli saxlanıb TLS ilə göndərilən siyahı əməkdaşın ekranında açıqdır, yalnız ilk ikisinə baxmaq kifayət deyil. Həyat dövrü: toplama, saxlama, istifadə, ötürmə, arxivləşdirmə, silinmə. Faylı silmək etibarlı məhv etmə deyil; şifrəli daşıyıcıda açarın məhvi mümkündür, lakin bütün açar nüsxələri nəzarətdə olmalıdır.

## OSI və TCP/IP

**OSI** (*Open Systems Interconnection*) yeddi, **TCP/IP** dörd səviyyəlidir (kanal, internet, nəqliyyat, tətbiq). Tətbiq sorğusu TCP, IP və kanal başlıqları ilə daşınır; bu **kapsullaşdırmadır** (*encapsulation*). Başlıqdakı ünvan kimliyin sübutu deyil.

| OSI | Təhdid | Tədbir |
| --- | --- | --- |
| 7 Tətbiq | İcazəsiz sorğu, inyeksiya | Obyekt üzrə icazə |
| 6 Təqdimat | Kodlaşdırmanın səhv emalı | Format və tip yoxlaması |
| 5 Sessiya | Sessiya oğurluğu | Token qorunması, ləğv |
| 4 Nəqliyyat | Bağlantı tükənməsi | Vəziyyət izləmə, məhdudiyyət |
| 3 Şəbəkə | Saxta IP, yanlış marşrut | Giriş filtrləri, IPsec |
| 2 Kanal | ARP saxtalaşdırması | Port nəzarəti |
| 1 Fiziki | Kabel kəsilməsi | Fiziki giriş, enerji |

**TCP** ardıcıllıq və yenidən ötürmə verir, **UDP** də, heç biri məxfilik və mənbə autentikliyi vermir; **IP** marşrutlaşdırır, mənbə ünvanının həqiqiliyini təsdiqləmir. **TLS** məxfilik və tamlıq verir, sertifikat zənciri və ad uyğunluğu yoxlanmalıdır (TLS 1.3 üçün RFC 9846, əvvəl RFC 8446). **IPsec** şəbəkə səviyyəsində, Wi-Fi qoruması cihaz–giriş nöqtəsi arasında qoruyur, **VPN** yoluxmuş noutbuku təmizləmir.

| Vasitə | Edir | Etmir |
| --- | --- | --- |
| DNS / DNSSEC | Ad → ünvan / mənşə və tamlıq yoxlaması | Məxfilik; DNSSEC şifrələmir |
| Firewall | Trafiki siyasətlə buraxır/rədd edir | Qiymət dəyişikliyinin əsasını yoxlamır |
| VLAN | Kanalda məntiqi ayrılma | Zonalararası marşrutu avtomatik qadağan etmir |
| NAT | Ünvan çevirir | Giriş siyasətini əvəz etmir |

**Seqmentləşdirmə** şəbəkəni iş funksiyasına görə ayırır, zonalararası keçidi firewall qaydaları idarə edir. DNS UDP/TCP 53, HTTPS çox vaxt TCP 443 işlədir, HTTP/3 isə QUIC üzərindən UDP ilə işləyə bilər; port nömrəsi tətbiqin kimliyini sübut etmir.

## Tanınmış hadisələr

:::steps Üç hadisə, üç CIA xassəsi
[[step]]
title = "Equifax, 2017: məxfilik"
body = "Böyük həcmdə fərdi məlumat sızması; yol: **Apache Struts** zəifliyi və vaxtında tətbiq edilməyən yamaq. Sistem işləyə-işləyə məlumat çıxarıla bilər. Dərs: inventar, yamaq məsuliyyəti, çıxış fəaliyyətinin görünməsi."

[[step]]
title = "Stuxnet, 2010: tamlıq"
body = "Sənaye idarəetmə sistemlərini hədəfləyən zərərli proqram: idarəetmə məntiqini dəyişir, operatorun mənzərəsini aldadır. Ekrandakı normal göstərici prosesin doğruluğunu sübut etmir; müstəqil ölçmə lazımdır."

[[step]]
title = "WannaCry, 2017: əlçatanlıq"
body = "SMB zəifliyi ilə yayılan ransomware; MS17-010 yeniləməsi hadisədən əvvəl dərc edilmişdi. Dərs: yamaq, lazımsız SMB-nin bağlanması, seqmentləşdirmə, bərpa sınağı. Əvvəl yayılma yolu bağlanır, sonra təmiz nüsxədən bərpa."
:::

## Hüquqi çərçivə və idarəetmə

Açıqlıq və məxfilik birlikdə nəzərə alınır: məhdudiyyət hüquqi əsasa bağlıdır. Mənbələr: "İnformasiya əldə etmək haqqında", "Fərdi məlumatlar haqqında", "İnformasiya, informasiyalaşdırma və informasiyanın mühafizəsi haqqında", "Elektron imza və elektron sənəd haqqında" qanunları. Adı silmək həmişə anonimləşdirmə deyil: kiçik qrupda nadir güzəşt şəxsi tanıdır. Milli səviyyədə 2 iyun 2026-cı ildən Milli Kibertəhlükəsizlik Agentliyi nəzərə alınır; dövlət orqanlarının rabitəsi üzrə Xüsusi Rabitə və İnformasiya Təhlükəsizliyi Dövlət Xidməti ayrı qurumdur.

Standartlar: **ISO/IEC** 27001:2022 (idarəetmə sistemi), 27002:2022 (93 tədbir), 27005:2022 (risk). **NIST** CSF 2.0 altı funksiyadır: **Govern**, **Identify**, **Protect**, **Detect**, **Respond**, **Recover**; ardıcıl mərhələlər deyil, paralel işləyir. NIST SP 800-61 Rev. 3 insidentə cavabı bu çərçivəyə bağlayır. Təhlükəsizlik məhsul sayı ilə deyil, yamaqlanmış kritik xidmət payı, icazə baxışı və bərpa sınağı ilə ölçülür.

## Tələblərin hazırlanması və yoxlanması

Tələb iş prosesindən çıxarılır və yoxlanıla bilən olmalıdır: məxfilik (tələbə başqasının cavabını ala bilməz), tamlıq (dəyişiklik versiya və səlahiyyətlə bağlıdır), əlçatanlıq (yük və gecikmə proses sahibi ilə razılaşdırılır), hesabatlılıq, bərpa (RTO/RPO), hüququn götürülməsi. Yoxlama qeyri-dağıdıcıdır: sınaq tələbəsi başqasının obyektini istəyir, server rədd edir. `ss -lntup`, `ip route show`, `systemctl --failed` inventar yoxlamasına kömək edir; hər birinin nəyi görmədiyi də yazılır.

İnsidentdə əvvəl faktlar toplanır, davam edən zərər məhdudlaşdırılır, sübut qorunur, təmiz mənbədən bərpa seçilir, sonra risk reyestri yenilənir. Hesabı bağlamaqla kifayətlənmək olmaz, sessiya və açarlar yoxlanır; sübutsuz qiymət bazasını doğru saymaq tamlığı pozur.

:::reveal Ransomware-dən sonra təmiz nüsxədən bərpa hər şeyi həll edirmi?
Xeyr. Bərpa tamlığı və əlçatanlığı qaytara bilər, amma artıq oğurlanmış məlumatın **məxfiliyini** yox. Davam edən hücum məhdudlaşdırılır, giriş yolu bağlanır, nüsxənin təmizliyi yoxlanır, ifşanın əhatəsi müəyyən edilir və bildiriş qərarları hüquqi tələblərə görə verilir.
:::
