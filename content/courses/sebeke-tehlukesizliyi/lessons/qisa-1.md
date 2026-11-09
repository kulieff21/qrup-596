+++
title = "Şəbəkə təhlükəsizliyinin əsasları: CIA və DAD triadası"
unit = "qisa"
order = 1
summary = "Mühazirənin skeleti: hər anlayış bir-iki cümlə ilə, mühazirənin ardıcıllığı ilə. CIA, DAD, AAA, risk, prinsiplər, OSI və üç hadisə daxil olmaqla heç nə atılmır."
updated = 2026-11-09

[[source]]
title = "Mühazirə 1: Şəbəkə təhlükəsizliyinin əsasları: CIA və DAD triadası"
note = "Elmar Cabbarov, 2026–2027"
+++

Bu mövzu kursun lüğətidir: sonrakı mövzularda hər hücum və müdafiə vasitəsi "hansı xassəni pozur, hansını qoruyur" sualına bağlanır. Universitet nümunələri şərti tədris nümunəsidir.

## İnformasiya, verilənlər və bilik

| Anlayış | Nədir |
| --- | --- |
| İnformasiya | Hadisə, obyekt, proses haqqında məna daşıyan məlumat |
| Verilənlər (*data*) | Məlumatın saxlanma və emal üçün formal təsviri (`score=85`) |
| Bilik (*knowledge*) | İnformasiyanı əlaqələndirib qərar verməyə imkan verən qaydalar və təcrübə |
| Kodlaşdırma (UTF-8, Base64), sıxılma | Məxfilik vermir, hər kəs bərpa edə bilər; yalnız şifrələmə açarla qoruyur |
| Keyfiyyət xassələri | Düzgünlük, dolğunluq, aktuallıq, aydınlıq, faydalılıq; təhlükəsizlik tamlığını əvəz etmir |

Siyahıdakı adların ilkin olaraq çatışmaması keyfiyyət qüsurudur, hücumçu silibsə tamlıq pozuntusudur. Tarixən yazı, çap (Qutenberq), teleqraf, telefon, radio və ARPANET informasiyanı yaydı; rəqəmsal daşıyıcı köhnəldiyi üçün yoxlama, miqrasiya və ehtiyat nüsxə lazımdır.

## İnformasiya təhlükəsizliyinin əhatəsi

- **İnformasiya təhlükəsizliyi** (*information security*): məxfilik, tamlıq, əlçatanlığı qoruyan idarəetmə vəziyyəti (kağız sənəd də daxildir).
- **Şəbəkə təhlükəsizliyi** (*network security*): rabitə infrastrukturu və şəbəkə xidmətləri.
- **Kibertəhlükəsizlik** (*cybersecurity*): rəqəmsal sistemlər və onların əlaqələri.
- **Aktiv** (*asset*): təşkilat üçün dəyəri olan hər şey (məlumat, server, insan, etimad); dəyəri qiymətinə bərabər deyil.
- **Səviyyələr:** şəxs, təşkilat, cəmiyyət, dövlət. **Tədbirlər:** inzibati, texniki, fiziki.
- Məqsəd bağlamaq yox, icazəli istifadəyə uyğun qorumaqdır; tələb xidmətin layihəsindən başlayır.

## CIA triadası

| Xassə | Mənası | Pozulma | Qoruyan |
| --- | --- | --- | --- |
| Məxfilik (*confidentiality*) | Yalnız icazəli subyekt görür | Sızma, dinləmə, açıq paylaşım | Şifrələmə, girişə nəzarət, MFA, təsnifat |
| Tamlıq (*integrity*) | İcazəsiz və ya təsadüfi dəyişiklik yoxdur, mənbə doğrudur | Məbləğin dəyişməsi, defacement | Heş, imza, HMAC, versiya nəzarəti |
| Əlçatanlıq (*availability*) | Xidmət lazım olanda əldə edilir | DDoS, ransomware, elektrik kəsintisi | Ehtiyat nüsxə, RAID, klaster, UPS |

- **LMS nümunəsi:** tələbə `GET /api/results/142` sorğusunda identifikatoru dəyişib başqasının nəticəsini alırsa, bu ifşadır (məxfilik); autentifikasiya işləyir, çatışan obyekt üzrə avtorizasiyadır.
- Şifrələmə → məxfilik; heş və imza → tamlıq; ehtiyat nüsxə və artıqlıq (*redundancy*) → əlçatanlıq. Heş məlumatı gizlətmir, yalnız dəyişikliyi göstərir.
- **Məxfilik** icazəli açıqlamanı istisna etmir; HTTPS kanalı qoruyur, obyekt üzrə avtorizasiyanı əvəz etmir. Disk şifrələməsi işləyən serverdəki tətbiqi dayandırmır. Fərdi həyatın toxunulmazlığı ayrıdır.
- **Heş** (*hash*, SHA-256) sabit ölçülü xülasədir; etalon ayrıca qorunmalıdır. **HMAC** açarlı koddur, müəlliflik üçün sübut deyil. **Rəqəmsal imza** (*digital signature*) şəxsi açarla yaradılır, müəlliflik sübutu verir.
- **Əlçatanlıq:** ad həlli, şəbəkə yolu, identifikasiya, tətbiq və baza işləməlidir. **DDoS** (*distributed denial of service*) resursu tükədir; sərt IP bloklaması paylaşılan IP-li tələbələri də vurur.
- **Backup** ehtiyat nüsxədir (ayrı saxlanır, bərpası yoxlanır); **RAID** nüsxənin əvəzi deyil; **replikasiya** zərərli dəyişikliyi də ötürür.
- **RTO** (*recovery time objective*): bərpa müddəti. **RPO** (*recovery point objective*): qəbul edilən itkinin zaman həddi. Məsələn RTO 2 saat, RPO 15 dəqiqə: xidmət 2 saata qayıdır, itki son 15 dəqiqədən çox deyil.
- **Balans:** şəxsi işlər → məxfilik; qiymət jurnalı, diplom reyestri → tamlıq; imtahan günü test sistemi → əlçatanlıq.

## DAD triadası

| DAD ünsürü | Pozur | Nümunə |
| --- | --- | --- |
| İfşa (*disclosure*) | Məxfilik | Açıq qovluqda abituriyent sənədləri |
| Dəyişdirmə (*alteration*) | Tamlıq | Balın icazəsiz dəyişməsi |
| Məhv etmə (*destruction*) / imtina (*denial*) | Əlçatanlıq | Silinmə, DDoS |

CIA nəyi qoruduğunu, DAD nəyin baş verdiyini adlandırır: "nə baş verdi?" → DAD, "nə pozuldu?" → CIA. Məhv etmə ilə imtina fərqlidir (məlumatı silmədən də girişi dayandırmaq olar).

- **Ransomware** tamlıq və əlçatanlığı pozur, əvvəl məlumat çıxarılıbsa məxfiliyi də; bu **ikiqat qəsbdir** (*double extortion*). Şifrələnmiş fayl görmək oğurluğu sübut etmir.
- Əlaməti səbəblə qarışdırmaq olmaz (açılmayan fayl ransomware, disk xətası və ya açar itkisi ola bilər).
- Tədbir pozulan xassəyə uyğun seçilir. Parolun dəyişdirilməsi aktiv sessiyaları avtomatik ləğv etməyə bilər. Ehtiyat nüsxə ifşanı geri almır; şəbəkə bloklaması bazada dəyişikliyi düzəltmir.

## CIA-dan kənar xassələr

| Xassə | Mənası |
| --- | --- |
| Autentiklik (*authenticity*) | Mənbə iddia edilən mənbədir (imza, sertifikat); dəyişməmək doğruluq deyil |
| Autentifikasiya (*authentication*) | Kimlik iddiasının yoxlanması; sənədin autentikliyi ayrıdır |
| İnkaredilməzlik (*non-repudiation*) | Mənşəyi sonradan inkar etməyə qarşı sübut (imza, vaxt möhürü); "təxirə salınmamaq" deyil |
| Hesabatlılıq (*accountability*) | Əməliyyat konkret subyektə bağlanır (fərdi hesab, audit) |
| Parker heksadı (*Parkerian hexad*) | CIA + sahiblik və nəzarət (*possession or control*), autentiklik, faydalılıq (*utility*) |

Şifrəli disk oğurlananda nəzarət itir, məxfilik açarın qorunmasından asılıdır; açarı itmiş arxiv yararsızdır (faydalılıq).

## AAA

- **Autentifikasiya:** kimlik; **avtorizasiya** (*authorization*): bu əmələ icazə; **uçot** (*accounting*): nə, nə vaxt, hansı nəticə ilə.
- Şəbəkə girişi ilə tətbiq icazəsi ayrı qərardır; yoxlama serverdə, hər sorğuda aparılır.
- **MFA** (*multi-factor authentication*): bilinən sirr, sahib olunan vasitə, biometrik amil; iki parol MFA deyil.
- Sessiya oğurluğu kimliyi təqlid edir: müddət, ləğv, təkrar yoxlama.
- **RBAC** (*role-based access control*): rol üzrə; **ABAC** (*attribute-based access control*): fənn, cihaz, vaxt kimi atributlar üzrə icazə.
- Tipik səhvlər: uğurlu girişi bütün hüquqlar saymaq, icazəni yalnız interfeysdə gizlətmək, uçotda parol saxlamaq.
- Audit qeydi iz verir, qanunilik sübut etmir; parol qeydə yazılmır.

## Təhdid, zəiflik, risk, insident

| Termin | Mənası |
| --- | --- |
| Təhdid (*threat*) | Aktivə zərər vura biləcək potensial hadisə (hücumçu, daşqın) |
| Zəiflik (*vulnerability*) | İstifadə oluna bilən çatışmazlıq |
| Risk (*risk*) | Zərərin ehtimalı və təsiri |
| Hücum (*attack*) | Qəsdli cəhd |
| Eksploit (*exploit*) | Zəiflikdən istifadə üsulu və ya kodu |
| Hadisə (*event*) | Müşahidə edilən fakt |
| İnsident (*security incident*) | Təhlükəsizliyi pozan, cavab tələb edən hadisə |
| Tədbir (*control*) | Riski azaldan addım |

Hər hadisə insident deyil: gündə milyonlarla log yazısı yaranır, yalnız bir qismi insidentə çevrilir. Açıq portun özü həmişə zəiflik deyil, uğursuz cəhd də hücum sayıla bilər. "Server yamanmayıb" zəiflikdir, "kimsə istifadə edə bilər" təhdiddir, "baş versə sızma və cərimə" riskdir.

**Təhdid təsnifatı:** mənşə (təbii, texniki, insan), niyyət (qəsdli, qəsdsiz), yerləşmə (daxili, xarici), təsir (passiv, aktiv), hədəf xassə, zərər növü. **Passiv** hücum dinləyir (qarşısı şifrələmə ilə), **aktiv** dəyişir və ya tükədir; aktivə qarşı da qabaqlayıcı tədbirlər (giriş yoxlaması, sürət məhdudiyyəti, seqmentləşdirmə, *segmentation*) var, aşkarlama və bərpa hər ikisi üçündür. Mənbəsiz faizlər işlədilmir.

## Risk və riskə cavab

- **Risk balı = ehtimal × təsir** (hər biri 1–5): ixrac 4×5 = 20, kataloq nasazlığı 4×2 = 8, yanğın 1×5 = 5. Prioritet şkalasıdır, dəqiq ehtimal deyil.
- Kəmiyyət: 2 000 AZN × 3 kəsinti = 6 000 AZN illik gözlənilən itki.
- **Dörd cavab:** azaltmaq (*mitigate*), yayınmaq (*avoid*), ötürmək (*transfer*, sığorta; məsuliyyət tam itmir), qəbul etmək (*accept*, yazılı qərar, baxış tarixi).
- Tədbirdən sonra qalan **qalıq risk** (*residual risk*): sıfır risk yoxdur; sahibi olmalıdır.
- **Risk reyestri** (*risk register*) qərarların yaddaşıdır; tədbirin işlədiyi sınaqla göstərilir.

## Layihələndirmə prinsipləri

| Prinsip | Mənası |
| --- | --- |
| Minimum səlahiyyət (*least privilege*) | Lazım olan hüquq, resurs və müddət |
| Vəzifələrin ayrılması (*separation of duties*) | Müraciət, təsdiq, icra ayrı subyektlərdə |
| Dərinlik üzrə müdafiə (*defense in depth*) | Bir tədbir pozulsa hamısı dağılmır; ortaq açar gizli asılılıqdır |
| Təhlükəsiz imtina (*fail-secure*) | Nasazlıqda giriş nəzarətsiz açılmır; **fail-safe** insan təhlükəsizliyidir (yanğın çıxışı) |
| Tam vasitəçilik (*complete mediation*) | Hər həssas əməliyyatda icazə yoxlanır |
| Hücum səthinin azaldılması (*attack surface reduction*) | İşlənməyən xidmət və hesablar bağlanır |
| Sıfır etibar (*zero trust*) | Şəbəkədəki yerə görə etimad yoxdur (NIST SP 800-207); kimlik, cihaz, resurs, sessiya konteksti |

Sıfır etibar məhsul və ya VPN deyil. Minimum səlahiyyət xidmət hesabına da aiddir (LMS-in baza hesabı bütün bazaları idarə etməməlidir); hüquqlar müvəqqəti verilir, vaxtında götürülür. Vəzifələrin ayrılmasında eyni hesab həm müraciət, həm təsdiq edə bilirsə, ayrılma yoxdur. Təhlükəsiz imtinada icazə serveri çatmırsa, yazma sorğusu rədd edilir.

## Məlumatların təsnifatı və həyat dövrü

- **Təsnifat** (*data classification*): şərti açıq, daxili, məxfi, ciddi məhdud.
- **Məlumat sahibi** (*data owner*) tələbi müəyyən edir; **saxlayıcı** (*custodian*) tətbiq edir.
- **Vəziyyətlər:** *data at rest* (saxlanma), *data in transit* (ötürmə), *data in use* (istifadə); yalnız ilk ikisini qorumaq kifayət deyil.
- **Dövr:** toplama, saxlama, istifadə, ötürmə, arxivləşdirmə, silinmə; faylı silmək etibarlı məhv deyil.

## OSI və TCP/IP

**OSI** (*Open Systems Interconnection*) yeddi, **TCP/IP** dörd səviyyəlidir. Tətbiq sorğusu başlıqlarla daşınır: **kapsullaşdırma** (*encapsulation*).

| OSI səviyyəsi | Təhdid → tədbir |
| --- | --- |
| 7 Tətbiq | İcazəsiz sorğu, inyeksiya → obyekt icazəsi |
| 6 Təqdimat | Kodlaşdırma səhvi → format yoxlaması |
| 5 Sessiya | Sessiya oğurluğu → token qorunması |
| 4 Nəqliyyat | Bağlantı tükənməsi → vəziyyət izləmə |
| 3 Şəbəkə | Saxta IP → giriş filtrləri, **IPsec** |
| 2 Kanal | **ARP** saxtalaşdırması → port nəzarəti |
| 1 Fiziki | Kabel kəsilməsi → fiziki giriş |

- **TCP** ardıcıllıq, **UDP**, **IP** marşrut verir; heç biri məxfilik və mənbə autentikliyi vermir.
- **TLS** məxfilik və tamlıq verir; sertifikat yoxlanmalıdır (RFC 9846, əvvəl RFC 8446). **Wi-Fi** qoruması yalnız cihaz–giriş nöqtəsi arasındadır; **VPN** yoluxmuş cihazı təmizləmir. **HTTPS** çox vaxt TCP 443, DNS 53, HTTP/3 isə **QUIC** üzərindən UDP işlədir.
- **DNS** adı ünvana çevirir; **DNSSEC** mənşə və tamlığı yoxlayır, şifrələmir. **Firewall** trafiki siyasətlə buraxır, **VLAN** kanalda ayırır, **NAT** ünvan çevirir; heç biri bütün nəzarəti əvəz etmir.
- Port nömrəsi tətbiqin kimliyini sübut etmir.

## Tanınmış hadisələr

| Hadisə | CIA | Dərs |
| --- | --- | --- |
| **Equifax**, 2017 | Məxfilik | **Apache Struts** zəifliyi, vaxtında tətbiq edilməyən yamaq; inventar və çıxış nəzarəti |
| **Stuxnet**, 2010 | Tamlıq | Sənaye idarəetmə məntiqini dəyişdi; normal ekran doğruluq deyil, müstəqil ölçmə |
| **WannaCry**, 2017 | Əlçatanlıq (və tamlıq) | **SMB** zəifliyi, MS17-010 yeniləməsi əvvəl çıxmışdı; yamaq, seqmentləşdirmə, bərpa sınağı |

## Hüquqi çərçivə və idarəetmə

- Açıqlıq və məxfilik birlikdə nəzərə alınır. Qanunlar: "İnformasiya əldə etmək haqqında", "Fərdi məlumatlar haqqında", "İnformasiya, informasiyalaşdırma və informasiyanın mühafizəsi haqqında", "Elektron imza və elektron sənəd haqqında". Adı silmək həmişə anonimləşdirmə deyil.
- Milli qurum: 2 iyun 2026-cı ildən Milli Kibertəhlükəsizlik Agentliyi; dövlət orqanları üçün Xüsusi Rabitə və İnformasiya Təhlükəsizliyi Dövlət Xidməti.
- **ISO/IEC** 27001:2022 (idarəetmə sistemi), 27002:2022 (93 tədbir), 27005:2022 (risk).
- **NIST** CSF 2.0 altı funksiya: **Govern**, **Identify**, **Protect**, **Detect**, **Respond**, **Recover**; paralel işləyir. NIST SP 800-61 Rev. 3 insidentə cavabı bağlayır.
- Ölçmə məhsul sayı ilə yox, yamaqlanmış kritik xidmət payı, icazə baxışı, bərpa sınağı ilə.

## Tələblərin hazırlanması və yoxlanması

Tələb iş prosesindən çıxarılır və qeyri-dağıdıcı sınaqla yoxlanır: məxfilik (başqasının obyekti rədd), tamlıq (təsdiqsiz düzəliş rədd və auditə), hesabatlılıq, əlçatanlıq (razılaşdırılmış yük), bərpa (RTO/RPO), hüququn götürülməsi. İnsidentdə: faktlar, zərərin məhdudlaşdırılması, sübutun qorunması, təmiz bərpa, risk reyestrinin yenilənməsi.

:::exam
Ransomware sualında hamısını sadala: ifşa (məxfilik), şifrələmə (əlçatanlıq), icazəsiz dəyişdirmə (tamlıq). Bərpa məxfiliyi qaytarmır.
:::
