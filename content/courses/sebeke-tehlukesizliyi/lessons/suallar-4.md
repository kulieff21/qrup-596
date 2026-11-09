+++
title = "Təhlükəsizlik tədbirləri və şəbəkə təhlükəsizliyi protokolları"
unit = "suallar"
order = 4
summary = "Mövzu 4 üzrə bütün nəzarət sualları, mühazirə və konspektdən situasiyalar, ehtimal olunan əlavə suallar və özünüyoxlama testi, hamısı hazır cavablarla."
updated = 2026-11-09

[[source]]
title = "Mühazirə 4: Təhlükəsizlik tədbirləri və şəbəkə təhlükəsizliyi protokolları"
note = "Elmar Cabbarov, 2026–2027"

[[source]]
title = "Midterm konspekti, Mövzu 4"
note = "Elmar Cabbarov"
+++

Əvvəl cavabı öz sözlərinlə de, sonra aç. Situasiya cavablarında ardıcıllıq: aktiv, pozulan xassə, səbəb, tədbir, yoxlama; hər tədbirin növünü və funksiyasını adlandır.

## Nəzarət sualları

### Təhlükəsizlik tədbirləri üzrə

:::reveal Risk niyə ehtimal ilə təsirin birləşməsi kimi hesablanır?
- Ehtimal aşağı, təsir çox böyük ola bilər: yanğının ehtimalı azdır, server otağı üçün təsiri ağırdır.
- Yalnız ehtimala baxmaq belə riski gözdən qaçırır, ona görə risk iki ölçü ilə qiymətləndirilir.
- Keyfiyyət üsulu: ehtimal və təsir 1–5 şkalası (3 × 5 = 15, "yüksək"). Kəmiyyət üsulu: pulla.
:::

:::reveal SLE, ARO və ALE nədir? Hesablama nümunəsi göstərin.
- **SLE** (Single Loss Expectancy): bir hadisənin ziyanı. **ARO** (Annualized Rate of Occurrence): ildə gözlənilən say. **ALE** (Annualized Loss Expectancy) = SLE × ARO.
- Nümunə: fidyə proqramı ziyanı 20 000 manat, iki ildə bir (ARO 0,5): ALE = 10 000 manat.
- EDR ildə 4000 manatdır, ARO-nu 0,1-ə endirir: yeni ALE 2000. Fayda = 10 000 − 2000 − 4000 = 4000 manat.
:::

:::reveal Riskə cavabın dörd variantını sadalayın.
- Azaltmaq (tədbir görmək), ötürmək (kiber sığorta, xidmət müqaviləsi), qaçmaq (riskli xidməti bağlamaq), qəbul etmək (rəhbərlik qərarı ilə).
- "Göz yummaq" yoxdur: qəbul etmək yazılı və məsuliyyətli qərardır.
:::

:::reveal Kameranı növ və funksiya oxları üzrə təsnif edin.
- Növ: fiziki.
- Funksiya: əsasən aşkarlayan; görünən yerdə asılıbsa çəkindirən də.
- İki ox bir-birindən asılı deyil; situasiya cavabında ikisini də adlandırmaq tam bal gətirir.
:::

:::reveal Kompensasiyaedici tədbirə nümunə göstərin.
- Əsas tədbir mümkün olmayanda yerini tutur.
- Nümunə: yamaq qoyula bilməyən köhnə cihazı ayrıca seqmentə (VLAN) çıxarıb firewall ilə məhdudlaşdırmaq.
- Qalıq risk qalır, ona görə müddətli istisna kimi sənədləşdirilir.
:::

:::reveal Fail-safe və fail-secure arasında fərq nədir?
- **Fail-safe:** yanğın zamanı elektron qapı insanları içəridə kilidləməməlidir (insan həyatı birinci prioritetdir).
- **Fail-secure:** server otağının qapısı adi elektrik kəsintisində açıq qalmamalıdır.
- Balans layihə mərhələsində qurulur, çıxış tərəfi həmişə əl ilə açılır.
:::

:::reveal FAR, FRR və CER nədir?
- **FAR** (False Acceptance Rate): yad şəxsin qəbul edilməsi. **FRR** (False Rejection Rate): icazəli şəxsin rədd edilməsi.
- Həssaslığı artırdıqca FAR azalır, FRR artır.
- **CER** (Crossover Error Rate): iki əyrinin kəsişdiyi nöqtə, sistemləri müqayisə etmək üçün.
:::

:::reveal RTO və RPO arasında fərq nədir?
- **RTO** (Recovery Time Objective): xidmətin nə müddətə bərpa olunmalı olduğu.
- **RPO** (Recovery Point Objective): nə qədər məlumat itkisinin qəbul edildiyi.
- Nümunə: RTO 4 saat, RPO 1 saat: nüsxə ən azı saatda bir, sistem 4 saata qalxmalıdır.
:::

:::reveal Siyasət, standart, prosedur və təlimatı fərqləndirin.
- Siyasət: nə və niyə? Rəhbərlik təsdiqləyir, məcburi.
- Standart: hansı minimum tələblərlə? Məcburi.
- Prosedur: addım-addım necə və kim edir?
- Təlimat: tövsiyə, məcburi deyil.
- Siyasətə məhsul adı və tez dəyişən parametr yazılmır.
:::

:::reveal Niyə iki parol çoxfaktorlu autentifikasiya sayılmır?
- MFA fərqli kateqoriyaları birləşdirir: bilik (parol), sahiblik (telefon, açar), biometrik xüsusiyyət.
- İki parol eyni kateqoriyadandır (bilik).
:::

### Şəbəkə protokolları üzrə

:::reveal TCP əl sıxması niyə təhlükəsizlik vasitəsi deyil?
- SYN, SYN-ACK, ACK etibarlı (reliable) bağlantı qurur.
- Nə şifrələmə, nə autentifikasiya var.
- Port nömrəsi də təhlükəsizlik sərhədi deyil: TCP 443-dən zərərli trafik də keçir.
:::

:::reveal Telnet, FTP və SNMPv2c-nin ortaq zəifliyi nədir?
- Hamısı məlumatı, o cümlədən parolu və community string-i açıq mətnlə ötürür, trafiki dinləyən oxuya bilir.
- Əvəz: SSH, SFTP (və ya FTPS), SNMPv3 authPriv.
:::

:::reveal SFTP və FTPS arasında fərq nədir?
- SFTP SSH üzərində işləyir (TCP 22).
- FTPS TLS üzərində: explicit (21-də AUTH TLS) və ya implicit (990).
- Fərqli protokollardır.
:::

:::reveal SSH-da TOFU nə deməkdir, riski nədir?
- Trust On First Use: ilk qoşulmada istifadəçi host açarının barmaq izini təsdiqləyir, o known_hosts faylına yazılır.
- Risk: ilk qoşulmada ortada hücumçu varsa onun açarı qəbul edilə bilər.
- Müdafiə: barmaq izini başqa kanalla yoxlamaq; böyük şəbəkədə SSH sertifikatları.
:::

:::reveal Host açarı dəyişəndə SSH niyə xəbərdarlıq verir?
- Açarın dəyişməsi ya server yenidən qurulması, ya MITM hücumu ola bilər.
- Xəbərdarlıq SSH-ın verdiyi əsas qorunmadır; yoxlanmadan known_hosts sətrini silmək onu ləğv edir.
:::

:::reveal SPF, DKIM və DMARC hərəsi nəyi yoxlayır?
- SPF: göndərən IP domenin icazə verdiyi serverlərdəndirmi (zərf domeni).
- DKIM: məktubun rəqəmsal imzası doğrudurmu.
- DMARC: SPF və ya DKIM nəticəsi "From" domeni ilə uyğundurmu (alignment) və uğursuzluqda nə edilsin.
- Üçü də DNS TXT qeyddir.
:::

:::reveal DMARC-da none, quarantine, reject siyasətləri nə deməkdir?
- none: yalnız hesabat. quarantine: spam qovluğu. reject: rədd.
- Yeni domendə none ilə başlanır, hesabatlar öyrənilir, sonra sərtləşdirilir.
:::

:::reveal SNMPv3-ün üç təhlükəsizlik səviyyəsini sadalayın.
- noAuthNoPriv, authNoPriv, authPriv.
- authPriv həm autentifikasiya, həm şifrələmə verir və seçilməlidir.
:::

:::reveal NTP-nin saxtalaşdırılması hansı sistemlərə təsir edir?
- Kerberos biletləri, sertifikatların yoxlanması, SIEM korrelyasiyası vaxtdan asılıdır.
- Qorunma: NTS (RFC 8915).
:::

:::reveal 802.1X-də üç rolu izah edin. O, trafiki şifrələyirmi?
- Supplicant: istifadəçi cihazı. Authenticator: kommutator və ya giriş nöqtəsi. Authentication server: RADIUS.
- Cihaz autentifikasiyadan keçənə qədər şəbəkəyə buraxılmır.
- Şifrələmir, yalnız girişi idarə edir.
:::

### TLS/SSL üzrə

:::reveal TLS hansı üç xidməti verir?
- Məxfilik (yolda oxunmur), tamlıq (dəyişdirmə aşkar edilir), autentifikasiya (server sertifikatla; mTLS-də müştəri də).
:::

:::reveal Niyə əl sıxmasında asimmetrik, məlumat üçün simmetrik kriptoqrafiya işlədilir?
- Asimmetrik kriptoqrafiya sürətli deyil, ona görə yalnız tərəflərin tanınması və açarın razılaşdırılması üçündür.
- Məlumat sürətli simmetrik alqoritmlə (AES-GCM, ChaCha20-Poly1305) şifrələnir.
:::

:::reveal TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384 şifr dəstini oxuyun.
- ECDHE: açar mübadiləsi (irəli məxfilik verir).
- ECDSA: server imzası (sertifikat ECDSA açarlıdır).
- AES_256_GCM: simmetrik şifr və rejim.
- SHA384: heş (PRF/açar törətmə üçün).
:::

:::reveal İrəli məxfilik nədir, niyə statik RSA onu vermir?
- Server açarı sonradan oğurlansa belə, köhnə yazılmış trafik açılmır.
- ECDHE-də hər sessiyaya müvəqqəti açar yaradılıb silinir.
- Statik RSA-da premaster_secret serverin açıq açarı ilə şifrələnib ötürülür; gizli açarla bərpa olunur və bütün köhnə sessiyalar açılır.
:::

:::reveal TLS 1.3 TLS 1.2-dən hansı alqoritmləri çıxarıb?
- Statik RSA, RC4, 3DES, CBC, sıxılma və yenidən danışıq.
- Açar törətmə PRF yerinə HKDF.
:::

:::reveal 0-RTT rejiminin riski nədir?
- Təkrar göndərmə (replay): hücumçu paketi yenidən göndərib əməliyyatı ikinci dəfə icra etdirə bilər.
- Yalnız vəziyyəti dəyişməyən sorğular (GET) üçün; ödəniş və qiymət dəyişdirmədə söndürülür.
- 0-RTT məlumatı irəli məxfilik də vermir.
:::

:::reveal Brauzer sertifikatı yoxlayarkən nələrə baxır?
- Zəncir etibar anbarındakı kök sertifikatla bitirmi (server və aralıq sertifikatlar).
- İmzalar düzgündürmü, tarix keçibmi.
- Domen SAN-da varmı.
- Sertifikat ləğv olunubmu.
:::

:::reveal CRL, OCSP və OCSP stapling arasında fərq nədir?
- CRL: CA-nın dövri yayımladığı ləğv siyahısı.
- OCSP: real vaxt sorğusu, amma istifadəçinin hansı sayta girdiyini CA-ya açır.
- OCSP stapling: server CA təsdiqini öz cavabına əlavə edir.
:::

:::reveal HSTS hansı hücuma qarşıdır?
- SSL stripping: hücumçu ilk açıq HTTP sorğusunu tutub istifadəçini HTTP-də saxlayır.
- HSTS (RFC 6797) brauzerə "yalnız HTTPS ilə gəl" deyir; preload siyahısı ilk ziyarət problemini həll edir.
:::

:::reveal Heartbleed niyə açarların da dəyişdirilməsini tələb edirdi?
- OpenSSL Heartbeat uzunluğu yoxlamırdı (CVE-2014-0160), sorğu başına 64 KB-a qədər server yaddaşı sızırdı.
- Gizli açarlar, parollar, sessiya məlumatları artıq oğurlanmış ola bilərdi; yalnız yamaq kifayət deyil.
:::

:::reveal ECH nəyi şifrələyir?
- ClientHello-nun həssas hissəsini (TLS 1.3-də açıq qalan SNI daxil), serverin açıq açarı ilə.
- RFC 9849 (2026).
:::

### DNSSEC üzrə

:::reveal DNS cavablarını saxtalaşdırmaq niyə mümkündür?
- DNS şəbəkə iştirakçılarının bir-birini tanıdığı dövrdə layihələnib; cavablarda orijinallığı yoxlayan mexanizm yoxdur, sorğular UDP 53-də açıq gedir.
- Həlledici yalnız sorğuya uyğunluğa baxır: TXID, mənbə portu, ad.
:::

:::reveal Kaminski hücumu köhnə keş zəhərlənməsindən nə ilə fərqlənirdi?
- Əvvəl saxta cavab uğursuz olsa ad TTL bitənə qədər keşdə qalırdı, yeni cəhd üçün gözləmək lazım idi.
- Kaminski mövcud olmayan adları (a1, a2...) sorğulayıb hər dəfə yeni yarış başlatdı və saxta cavaba bütöv domen üçün NS qeydi əlavə etdi.
- Sabit mənbə portu ilə yalnız 65 536 TXID tapmaq kifayət idi.
- Təsadüfi port (≈2³²) yalnız ehtimalı azaldır; əsaslı həll imzadır.
:::

:::reveal DNSSEC hansı xassələri verir, hansını vermir?
- Verir: mənşənin autentifikasiyası, tamlıq, adın mövcud olmamasının sübutu, keş zəhərlənməsindən qorunma.
- Vermir: məxfilik, DDoS qorunması, registrator hesabının qorunması; yoxlamayan həlledicidə işləmir.
:::

:::reveal RRSIG, DNSKEY, DS qeydlərinin vəzifəsi nədir?
- RRSIG: qeydlər dəstinin (RRset) imzası.
- DNSKEY: zonanın açıq açarı (257 KSK, 256 ZSK).
- DS: valideyn zonada uşağın KSK heşi, zonalar arası etibar körpüsü.
:::

:::reveal KSK və ZSK niyə ayrılır?
- ZSK qeydləri imzalayır, tez-tez dəyişdirilir; KSK yalnız DNSKEY dəstini imzalayır, valideyndəki DS ona istinad edir.
- ZSK dəyişəndə valideyn zonaya müraciət lazım olmur.
- Məcburi deyil: tək açarla (CSK) də olur.
:::

:::reveal Etibar lövbəri nədir?
- Yoxlayan həllediciyə əvvəlcədən qoyulmuş kök zonanın KSK-sı.
- Zəncir kökdən aşağı DS və DNSKEY ilə ondan yoxlanır.
:::

:::reveal Secure, Insecure, Bogus və Indeterminate vəziyyətləri arasında fərq nədir?
- Secure: zəncir tam, AD bayrağı.
- Insecure: DS-in olmaması imzalı sübut olunub, cavab adi qaydada verilir.
- Bogus: imza səhv və ya vaxtı keçib, SERVFAIL.
- Indeterminate: etibar lövbəri olmadıqda.
:::

:::reveal NSEC-in yan təsiri nədir, NSEC3 onu necə azaldır?
- NSEC zəncirini izləyən bütün adları öyrənir (zone walking).
- NSEC3 adları heşləyir; lüğət hücumu qalır. Tam müdafiə: compact denial. RFC 9276: iterasiya 0, salt boş.
:::

:::reveal DNSSEC ilə DoH arasında fərqi izah edin.
- DNSSEC cavabın bütövlüyünü və mənşəyini sübut edir (məlumat səviyyəsi), sorğunu gizlətmir.
- DoH (TCP 443) müştəri ilə həlledici arasında kanalı şifrələyir (məxfilik), amma saxta cavabı şifrəli çatdıra bilər.
- Bir-birini əvəz etmirlər.
:::

:::reveal AD bayrağı nə deməkdir?
- Yoxlayan həlledici zənciri uğurla yoxlayıb (Secure).
- Son cihazla həlledici arasında qorunmur; yalnız etibarlı həlledici və qorunan kanalda (yerli həlledici, DoT, DoH) inanmaq olar.
:::

## Situasiya tapşırıqları

**Situasiya 1.** Kimya laboratoriyasındakı spektrometr Windows 7 ilə işləyir, istehsalçı yeniləmə vermir, cihazı dəyişmək iki il sonra büdcəyə düşəcək. Cihaz tələbə Wi-Fi-ı daxil bütün kampus şəbəkəsinə açıqdır. Hansı tədbirləri təklif edərdiniz və necə təsnif edərdiniz?

:::reveal Cavab
- Aktiv və problem: yamaqlanmayan cihaz; əsas tədbir mümkün deyil, ona görə kompensasiyaedici tədbirlər.
- Ayrıca VLAN, firewall ilə yalnız nəticə serverinə əlaqə: texniki, qarşısını alan.
- İnternet çıxışı, USB portları bağlanır, laboratoriya kilidlənir: fiziki və texniki.
- Trafikin IDS ilə izlənməsi: texniki, aşkarlayan.
- Riskin rəhbərlik tərəfindən yazılı qəbulu və dəyişdirmə tarixi: inzibati.
- Qalıq risk qalır: müddətli istisna kimi sənədləşdirilir.
:::

**Situasiya 2.** Server otağında biometrik giriş cihazı sıradan çıxıb, gecə kritik serverdə nasazlıq var. Növbətçi mühəndis otağa girməlidir. Düzgün yanaşma necədir?

:::reveal Cavab
- Əvvəlcədən hazırlanmış fövqəladə giriş proseduru: kilidli saxlancda möhürlənmiş açar və ya ikinci kart.
- İki nəfərin təsdiqi, girişin jurnala yazılması, kameranın işləməsinin yoxlanması.
- Bu kompensasiyaedici tədbirdir.
- Sonra: giriş nəzərdən keçirilir, açar yenidən möhürlənir, cihaz bərpa olunur.
:::

**Situasiya 3.** Universitet ehtiyat nüsxələri eyni server otağında, eyni şəbəkədəki NAS-da saxlayır, bərpa heç vaxt sınanmayıb. Hansı risklər var?

:::reveal Cavab
- Pozulan xassə: əlçatanlıq (və bütövlük).
- Yanğın, su basması, oğurluq əsas sistemlə birlikdə nüsxələri də məhv edir.
- Fidyə proqramı eyni şəbəkədəki NAS-ı da şifrələyə bilir.
- Sınaqdan keçməyən nüsxənin işləyəcəyi bilinmir.
- Tədbir: 3-2-1 qaydası, biri başqa binada və dəyişdirilə bilməyən (immutable) formada; RTO və RPO müəyyən edilir; bərpa mütəmadi sınanır.
:::

**Situasiya 4.** İT şöbəsi "Təhlükəsizlik siyasəti" sənədinə Windows Server versiyalarını, firewall modelini və parol uzunluğunu yazıb, sənədi rəhbərliyə təqdim etmədən paylayıb. Səhvlər nədir?

:::reveal Cavab
- Siyasət rəhbərlik tərəfindən təsdiqlənməlidir; yoxsa məcburi qüvvəsi və resurs dəstəyi olmur.
- Məhsul adları və texniki parametrlər standart və prosedurlara aiddir; siyasətə yazılanda sənəd tez köhnəlir.
- Sənədin sahibi, versiyası, baxış tarixi, istisna və pozuntu qaydası göstərilməlidir.
:::

**Situasiya 5.** Administrator köhnə kommutatorları Telnet ilə idarə edir, monitorinq SNMPv2c ilə gedir, konfiqurasiya faylları FTP ilə serverə yığılır. Tələbə yataqxanası da eyni şəbəkədədir. Auditor bunu ciddi risk kimi qeyd edib. Niyə və nə etmək lazımdır?

:::reveal Cavab
- Pozulan xassə: məxfilik və tamlıq. Üç protokol parolu və community string-i açıq mətnlə ötürür; dinləyən tələbə ələ keçirə bilər.
- Əvəz: Telnet → SSH (host açarı yoxlaması ilə), SNMPv2c → SNMPv3 authPriv, FTP → SFTP.
- Keçid dövründə idarəetmə trafiki ayrıca idarəetmə VLAN-ına alınır, yalnız administrator kompüterlərindən icazə verilir.
:::

**Situasiya 6.** Administrator serverə qoşulanda SSH "REMOTE HOST IDENTIFICATION HAS CHANGED" xəbərdarlığı verir. Həmkarı deyir: "known_hosts-dan sətri sil, keç." Düzgün addım nədir?

:::reveal Cavab
- Xəbərdarlıq açarın dəyişdiyini göstərir: server yenidən qurulması və ya MITM.
- Əvvəl başqa kanalla (konsol, dəyişiklik qeydləri) yeni açarın barmaq izi yoxlanır.
- Yalnız təsdiqdən sonra köhnə sətir silinir.
- Yoxlamadan silmək SSH-ın verdiyi yeganə qorunmanı ləğv edir.
:::

**Situasiya 7.** Tələbələrə "rektor@universitet.example" ünvanından təqaüd barədə saxta məktub gəlib. Poçt serveri STARTTLS işlədir. Administrator: "Bizdə TLS var, belə hadisə olmamalı idi." Fikri qiymətləndirin.

:::reveal Cavab
- Səhv: STARTTLS yalnız serverlər arasındakı kanalı şifrələyir, göndərənin kimliyini yoxlamır.
- Lazım olan: SPF, DKIM, DMARC.
- DMARC əvvəl none ilə, hesabatlara baxılır, qanuni göndərənlər siyahıya alınır, sonra reject.
- Oxşar domenlərdən gələn məktublara qarşı istifadəçi təlimi və poçt süzgəci.
:::

**Situasiya 8.** LMS serverinin SSH portu İnternetə açıqdır, parolla giriş aktivdir, loglarda gündə minlərlə uğursuz giriş var. Hansı addımları təklif edərdiniz?

:::reveal Cavab
- SSH portu İnternetdən bağlanır, giriş VPN və jump host vasitəsilə.
- Parol və klaviatura-interaktiv giriş söndürülür, açarla autentifikasiya; PermitRootLogin no; icazə qrupla məhdudlaşdırılır.
- Uğursuz girişlər SIEM-ə göndərilir.
- Portu 22-dən başqa nömrəyə köçürmək yalnız səs-küyü azaldır, tədbir sayılmır.
:::

**Situasiya 9.** Ödəniş portalının yoxlamasında serverdə TLS 1.0, 1.1 aktivdir, RC4 şifrləri də açıqdır. İT işçisi: "Sertifikat etibarlıdır, kilid görünür, deməli, problem yoxdur." Qiymətləndirin.

:::reveal Cavab
- Kilid yalnız sertifikatın keçərli olduğunu göstərir, protokolun güclü olduğunu yox.
- TLS 1.0/1.1 RFC 8996 ilə köhnəlib, RC4 RFC 7465 ilə qadağandır; PCI DSS də erkən TLS-i qəbul etmir.
- Tədbir: TLS 1.2 və 1.3-ə keçid, köhnə versiyalar, RC4 və zəif şifrlər söndürülür.
- Yoxlama: nmap və ya Qualys.
:::

**Situasiya 10.** Qonaq Wi-Fi-ında tələbələr portal.universitet.example yazanda giriş səhifəsi http:// ilə açılır və parollar oğurlanır. Server HTTP-dən HTTPS-ə yönləndirmə qurub. Bu necə mümkündür?

:::reveal Cavab
- Hücum: SSL stripping. Hücumçu ilk açıq HTTP sorğusunu tutur, serverlə HTTPS, istifadəçi ilə HTTP danışır; yönləndirmə istifadəçiyə çatmır.
- Həll: HSTS başlığı, domeni preload siyahısına salmaq, istifadəçilərə əlfəcin vermək.
- OWE passiv radio dinləməsini çətinləşdirir, amma saxta AP və aktiv MITM-i dayandırmır.
- Əsas müdafiə HSTS preload və TLS server kimliyinin yoxlanmasıdır; müştəri izolyasiyası əlavədir.
:::

**Situasiya 11.** Serverin gizli açarı 2026-da oğurlanıb. Hücumçunun əlində 2024-dən yazılmış trafik var. Server 2024-də TLS_RSA_WITH_AES_128_CBC_SHA işlədirdi. Trafik açıla bilərmi? Server TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256 işlətsəydi nə dəyişərdi?

:::reveal Cavab
- Birinci halda açılır: statik RSA-da premaster_secret serverin açıq açarı ilə şifrələnib, gizli açarla bərpa olunur, trafik açarları ondan törədilir.
- ECDHE-də hər sessiyanın müvəqqəti açarı saxlanılmır; oğurlanmış RSA açarı yalnız imza açarıdır, köhnə sessiyaları açmır. Xassə: irəli məxfilik.
- Hadisədən sonra açar dəyişdirilir, sertifikat ləğv edilir (hücumçu serveri təqlid edə bilər).
:::

**Situasiya 12.** Portal sertifikatını CA ləğv edib, amma bəzi istifadəçilərin brauzeri xəbərdarlıq göstərmir. Niyə ola bilər?

:::reveal Cavab
- Brauzerlər ləğvi həmişə real vaxtda yoxlamır.
- OCSP cavabı alınmayanda çox müştəri bağlantını davam etdirir (soft-fail); CRL yenilənməsi gecikə bilər.
- Səbəb ləğv mexanizminin zəifliyidir; sənaye qısa ömürlü sertifikatlara keçir.
- Oğurlanmış açar hadisəsində sertifikat və açar dəyişdirilir.
:::

**Situasiya 13.** Rəhbərlik: "Tələbələrin hansı saytlara girdiyini provayder görməsin deyə DNSSEC quraq." Qiymətləndirin.

:::reveal Cavab
- DNSSEC məxfilik vermir, sorğular açıq qalır; məqsəd məxfilikdirsə DoT və ya DoH.
- DNSSEC cavabın saxtalaşdırılmasına qarşıdır.
- DoT/DoH yalnız DNS kanalını qoruyur: provayder hədəf IP-lərdən və ECH olmayan TLS-də SNI-dən sayt barədə məlumat ala bilər.
- Saxta saytlardan qorunmaq üçün universitet domenləri imzalanır və kampus həlledicisində yoxlama açılır.
:::

**Situasiya 14.** Domen sahibi DNSSEC-i işə salıb, DS-i registratora yükləyib. Sonra DNS provayderini dəyişib, amma köhnə DS-i silməyib. Bəzi istifadəçilərdə sayt açılır, bəzilərində yox. Səbəb?

:::reveal Cavab
- Yeni provayderin açarları valideyndəki köhnə DS-ə uyğun gəlmir, zəncir qırılır.
- Yoxlayan həlledicilər nəticəni Bogus sayıb SERVFAIL verir; yoxlamayanlar adi qaydada qəbul edir, ona görə problem hissə-hissə görünür.
- Həll: yeni açarla uyğun DS yerləşdirilir, köhnəsi silinir; provayder dəyişimi planlı açar dəyişimi kimi aparılır.
:::

**Situasiya 15.** Hücumçu registrator hesabına daxil olub NS qeydlərini və DS-i özününkü ilə dəyişib. DNSSEC qarşısını alacaqmı?

:::reveal Cavab
- Xeyr. Etibar valideyndəki DS-ə əsaslanır, DS isə registrator vasitəsilə dəyişdirilib; həlledici üçün zəncir düzgün görünür.
- Qorunma registrator hesabındadır: MFA, Registry Lock, dəyişikliklərin monitorinqi.
:::

**Situasiya 16.** Qonaq şəbəkəsində bir kompüter dəqiqədə minlərlə uzun, təsadüfi görünən subdomen sorğusu göndərir (DNS tunelləmə şübhəsi). DNSSEC kömək edərmi?

:::reveal Cavab
- Xeyr: tunelləmə düzgün imzalanmış domenlə də işləyir.
- DNS qeydlərinin analizi: ad uzunluğu, entropiya, bir domenə sorğu sayı; SIEM-də qayda.
- Müştərilərin yalnız daxili həllediciyə çıxışı; birbaşa TCP/UDP 53, icazəsiz xarici TCP 853 (DoT) və UDP 853 (DoQ) bağlanır.
- DoH üçün idarə olunan cihaz siyasəti və tətbiq səviyyəli nəzarət; yalnız məlum IP siyahısı tam nəzarət vermir.
:::

## Konspektdən situasiyalar

**Situasiya 1 (konspekt).** Kimya laboratoriyasındakı spektrometr Windows 7 ilə işləyir, yeniləmə yoxdur, dəyişdirmə iki ildən sonradır, cihaz tələbə Wi-Fi-ı daxil bütün kampusa açıqdır. Hansı tədbirləri təklif edərdin və necə təsnif edərdin?

:::reveal Cavab
- Yamaq mümkün deyil, kompensasiyaedici tədbirlər lazımdır.
- Ayrıca VLAN, firewall ilə yalnız nəticə serverinə icazə: texniki, qarşısını alan.
- İnternet çıxışı və USB bağlanır, laboratoriya kilidlənir: fiziki/texniki.
- IDS ilə izləmə: texniki, aşkarlayan.
- Riskin yazılı qəbulu, dəyişdirmə tarixi: inzibati; qalıq risk müddətli istisna kimi sənədləşir.
:::

**Situasiya 2 (konspekt).** Şəbəkə admini köhnə kommutatorları Telnet ilə idarə edir, monitorinq SNMPv2c, konfiqurasiya faylları FTP ilə yığılır; yataqxana eyni şəbəkədədir. Auditor ciddi risk qeyd edib. Niyə və nə etməli?

:::reveal Cavab
- Üç protokol admin parolunu və community string-i açıq mətnlə ötürür; tələbə Wireshark ilə ələ keçirə bilər: məxfilik və tamlığa birbaşa təhlükə.
- Əvəz: Telnet → SSH (host açarı yoxlaması), SNMPv2c → SNMPv3 authPriv, FTP → SFTP.
- Keçid dövründə idarəetmə trafiki ayrıca VLAN-a, yalnız admin kompüterlərindən.
:::

**Situasiya 3 (konspekt).** Tələbə portala girəndə brauzer "sertifikat bu domenə aid deyil" xəbərdarlığı verir. Tələbə "sayt HTTPS-dir, deməli təhlükəsizdir" deyib "Davam et" basır. Nə qədər təhlükəlidir?

:::reveal Cavab
- Çox təhlükəlidir: TLS serverin həqiqiliyini sertifikatdakı domen adı ilə yoxlayır; ad uyğun gəlmirsə tələbə saxta serverə (məs. ictimai Wi-Fi-da MITM) qoşula bilər.
- Şifrələmə olsa da məlumat hücumçunun serverinə şifrəli gedir.
- Xəbərdarlıqda davam etmək olmaz, İT xidmətinə bildirilir.
- Universitet tərəfdə: düzgün sertifikat və HSTS (HSTS olanda brauzer xəbərdarlığı keçməyə icazə vermir).
:::

## Ehtimal olunan əlavə suallar

:::reveal İstənilən tədbiri necə təsnif edirsən? Üç növ və dörd əsas funksiya üzrə cədvəl çək.
- Növ: fiziki, inzibati, texniki. Funksiya: qarşısını alan, aşkarlayan, düzəldən, çəkindirən; üstəgəl bərpaedici, kompensasiyaedici, yönləndirici.
- Fiziki: kilid / CCTV / yanğınsöndürmə / lövhə. İnzibati: siyasət, təlim / audit / insident planı / intizam qaydası. Texniki: firewall, MFA / IDS, SIEM / yamaq, karantin / xəbərdarlıq mətni.
:::

:::reveal Hesablama: ziyan 30 000, ehtimal ildə 0,2; tədbir ildə 3000 manatdır və ARO-nu 0,05-ə endirir. Tədbir xeyirlidirmi?
- ALE = 30 000 × 0,2 = 6000.
- Yeni ALE = 30 000 × 0,05 = 1500.
- Fayda = 6000 − 1500 − 3000 = 1500 manat, tədbir xeyirlidir.
- Metod: illik ALE ilə illik xərc müqayisə edilir, birdəfəlik alış qiyməti ilə yox.
:::

:::reveal SSH, TLS və IPsec nəyi qoruyur?
- IPsec: şəbəkə (3) səviyyəsində bütün IP trafikini (saytdan sayta VPN); kimlik: sertifikat, PSK, EAP.
- TLS: tətbiq bağlantısını (veb, API, poçt); X.509 sertifikat.
- SSH: uzaqdan sessiya və fayl ötürməsini; host və istifadəçi açarı.
:::

:::reveal TLS 1.2 ilə TLS 1.3 əl sıxmasını müqayisə edin.
- 2-RTT və 1-RTT (0-RTT seçimi). Sertifikat açıq və şifrəli.
- İrəli məxfilik: TLS 1.2-də yalnız ECDHE/DHE seçiləndə; TLS 1.3-də (EC)DHE ilə 1-RTT-də var, PSK-only və 0-RTT-də yoxdur.
- TLS 1.3-də statik RSA, RC4, 3DES, CBC, sıxılma, yenidən danışıq çıxarılıb; açar törətmə PRF yerinə HKDF; şifr dəstləri onlarla variant yerinə beş.
:::

:::reveal CertificateVerify ilə Finished arasında fərq nədir?
- CertificateVerify: server əl sıxması tarixçəsinin heşini imzalayıb sertifikat açarının gizli hissəsinə sahib olduğunu sübut edir.
- Finished: HMAC; iki tərəfin eyni açarları və eyni tarixçəni gördüyünü təsdiqləyir.
:::

:::reveal Sertifikat xətalarını izah edin: DATE_INVALID, COMMON_NAME_INVALID, AUTHORITY_INVALID.
- DATE_INVALID: müddət bitib və ya cihaz saatı səhv; tarixi yoxlamaq.
- COMMON_NAME_INVALID: domen SAN-da yoxdur; sertifikatı düzgün domenə buraxmaq.
- AUTHORITY_INVALID: zəncir kökə çatmır, aralıq sertifikat yoxdur, özünü imzalayıb və ya TLS yoxlaması gedir; tam zənciri qurmaq.
- Kütləvi AUTHORITY_INVALID MITM əlaməti ola bilər: keçmə, İT-yə bildir.
:::

:::reveal DNSSEC etibar zəncirinin yoxlanmasını addımlarla izah edin.
- Etibar lövbəri (kök KSK) ilə kökün DNSKEY dəsti və RRSIG yoxlanır, ZSK etibarlı olur.
- Kökün ZSK-sı ilə example. üçün DS imzası yoxlanır.
- example. DNSKEY dəsti DS ilə tutuşdurulur, imza həmin KSK ilə yoxlanır.
- Eyni universitet.example. üçün; sonda A qeydinin RRSIG imzası domen ZSK-sı ilə yoxlanır.
- Nəticə: Secure (AD) və ya Bogus (SERVFAIL).
:::

:::reveal DNSSEC-in etibar modeli TLS PKI-dən nə ilə fərqlənir?
- PKI: brauzerdə yüzlərlə kök CA, istənilən CA hər domen üçün imzalaya bilər, bir CA sızması bütün internet üçün risk, yoxlama müştəridə.
- DNSSEC: bir kök, yalnız valideyn uşağı təsdiqləyir, zəiflik həmin zonanın aşağısı ilə məhdud, yoxlama adətən həlledicidə.
:::

:::reveal Kök KSK dəyişimi haqqında nə bilirsiniz?
- Kök zona 2010-da imzalandı, ilk KSK dəyişimi 11 oktyabr 2018.
- KSK-2024 (nişan 38696) 2025-də əlavə edilib; 11 oktyabr 2026-dan imzalayır, KSK-2017 11 yanvar 2027-də ləğv olunur.
- Həlledicilər yeni açarı RFC 5011 ilə 30 günlük hold-down-dan sonra qəbul edir; lövbəri yeniləməyən həlledicidə ad həlli pozulur.
:::
