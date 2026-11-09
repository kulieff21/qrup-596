+++
title = "Təhlükəsizlik tədbirləri və şəbəkə təhlükəsizliyi protokolları"
unit = "orta"
order = 4
summary = "Hər anlayış 1–3 cümlə ilə: tədbirlərin təsnifatı, fiziki və inzibati tədbirlər, protokolların təhlükəsiz əvəzləri, SSH, e-poçt, TLS və sertifikatlar, DNS hücumları və DNSSEC."
updated = 2026-11-09

[[source]]
title = "Mühazirə 4: Təhlükəsizlik tədbirləri və şəbəkə təhlükəsizliyi protokolları"
note = "Elmar Cabbarov, 2026–2027"
+++

Mövzu iki hissədən ibarətdir: riski azaldan tədbirləri düzgün təsnif etmək və şəbəkədə məlumatı qoruyan protokolların (SSH, TLS, IPsec, DNSSEC) nəyi qoruyub nəyi qorumadığını bilmək. Nümunələr şərti universitet ssenarisidir.

## Təhlükəsizlik tədbirləri

### Risk və əsas anlayışlar

Tədbir (nəzarət, *control*) riski aradan qaldırmaq, azaltmaq, aşkar etmək və ya hadisədən sonra bərpa etmək üçün görülən təşkilati, texniki və ya fiziki addımdır.

| Anlayış | Mənası |
| --- | --- |
| Aktiv | Dəyəri olan informasiya, sistem, xidmət, avadanlıq |
| Təhdid | Aktivə zərər vura biləcək hadisə və ya subyekt |
| Zəiflik | Təhdidin istifadə edə biləcəyi çatışmazlıq |
| Risk | **Ehtimal və təsirin** birləşməsi (təkcə ehtimal yox) |
| Qalıq risk | Tədbirlərdən sonra qalan, rəhbərliyin yazılı qəbul etdiyi risk |

Keyfiyyət üsulunda ehtimal və təsir 1–5 şkalası ilə qiymətləndirilir (3 × 5 = 15, "yüksək"). Kəmiyyət üsulunda: SLE (Single Loss Expectancy) bir hadisənin ziyanı, ARO (Annualized Rate of Occurrence) ildə gözlənilən say, ALE (Annualized Loss Expectancy) illik itki: **ALE = SLE × ARO**. Nümunə: ziyan 20 000, ARO 0,5, ALE 10 000 manat. EDR ildə 4000 başa gəlib ARO-nu 0,1-ə endirirsə, yeni ALE 2000 və illik fayda 10 000 − 2000 − 4000 = 4000 manatdır.

Riskə dörd cavab: azaltmaq, ötürmək (sığorta), qaçmaq (xidməti bağlamaq), qəbul etmək (yazılı rəhbərlik qərarı). Göz yummaq seçim deyil.

### Növ və funksiya

Tədbirə iki sual verilir: növü (fiziki, inzibati, texniki) və funksiyası. Situasiya cavabında hər iki ox adlandırılır.

| Növ | Qarşısını alan | Aşkarlayan | Düzəldən | Çəkindirən |
| --- | --- | --- | --- | --- |
| Fiziki | Kilid, turniket, mantrap | CCTV, sensorlar | Yanğınsöndürmə | Kamera lövhəsi, mühafizəçi |
| İnzibati | Siyasət, yoxlama, təlim | Hüquq baxışı, audit | İnsidentə cavab planı | İntizam qaydası |
| Texniki | Firewall, MFA, şifrələmə | IDS, SIEM, antivirus skanı | Yamaq, karantin | Giriş xəbərdarlıq mətni |

Əlavə funksiyalar: **bərpaedici** (recovery; ehtiyat nüsxə, ehtiyat data mərkəzi), **kompensasiyaedici** (compensating; yamaq mümkün olmayanda köhnə cihazı ayrıca seqmentə çıxarmaq), **yönləndirici** (directive; "USB qadağandır" qaydası).

Çoxsəviyyəli müdafiə (*defense in depth*): heç bir tədbir səhvsiz olmadığından qatlar ardıcıl qurulur, hücumçu bir qatı keçsə növbəti onu dayandırır, ləngidir və ya aşkarlayır (poçt süzgəci, işçi təlimi, EDR, seqmentasiya). Tədbir riskə görə seçilir (aktivin dəyəri, ziyan, qanun, xərc, istifadəçiyə təsir); xərc və fayda eyni müddət üzrə müqayisə edilir və effektivlik ölçülür (yamaq günləri, fişinq sınağı faizi, bərpa testləri).

### Fiziki tədbirlər

Fiziki müdafiə də qatlardan ibarətdir: perimetr, qəbul zonası, daxili zonalar, server otağı, rack, aktiv.

| Vasitə | Üstünlük / məhdudiyyət |
| --- | --- |
| Mexaniki kilid | Ucuz; surəti çıxarılır, jurnal yoxdur |
| Elektron kart, PIN | Jurnal, tez dəyişir; verilə, klonlana, müşahidə edilə bilər |
| Biometrika | Şəxslə bağlı; məxfilik, səhv, dəyişdirilə bilməmə |
| Turniket, mantrap | Bir kartla iki nəfərin keçməsini azaldır |
| Videomüşahidə | Sübut yaradır; monitorinq tələb edir |

Biometrikada **FAR** (False Acceptance Rate) yad şəxsin qəbulu, **FRR** (False Rejection Rate) icazəlinin rəddidir; həssaslıq artdıqca FAR azalır, FRR artır; kəsişmə nöqtəsi **CER** (Crossover Error Rate). Biometrika adətən ikinci faktordur. **Mantrap** iki qapı arasındakı otaqdır (ikinci qapı birinci bağlananda açılır); **tailgating** (ardınca icazəsiz keçmə) sosial davranışdır, maarifləndirmə də lazımdır. Ziyarətçi qeydiyyatdan keçir, müşayiət olunur; itirilmiş kart dərhal deaktiv edilir.

Server otağı pəncərəsiz, borulardan uzaq, ayrıca kilidlidir; minimum imtiyaz və vəzifələr ayrılığı işləyir; giriş jurnalı, kilidli daşıyıcı, ayrı yerdə ehtiyat nüsxə, konsolların avtomatik kilidi tələb olunur. Təmiz masa və ekran qaydası, disklər üçün təhlükəsiz silmə, kriptoqrafik silmə (açarı məhv etmək) və ya fiziki məhv.

**Ətraf mühit:** ASHRAE 18–27 °C tövsiyə edir; aşağı rütubət statik elektrik, yüksək rütubət kondensasiya və korroziya yaradır. Server otağında su yerinə qaz sistemləri (FK-5-1-12, inert qazlar) və ya pre-action; su sızma sensorları. UPS qısa kəsintidə enerji verib düzgün söndürməyə vaxt yaradır, generator uzun kəsintilər üçündür, soyutma N+1, torpaqlama elektrik təhlükəsini azaldır. Artıqlıq (*redundancy*) N+1-dir; iki kondisioner eyni xəttdədirsə real artıqlıq yoxdur.

:::exam Fail-safe və fail-secure
Birinci prioritet insan həyatıdır: yanğında elektron qapı içəridə kilidləməməlidir (**fail-safe**); adi elektrik kəsintisində server otağı açıq qalmamalıdır (**fail-secure**). Çıxış tərəfi həmişə əl ilə açılır.
:::

Fasiləsizlik: **RTO** (Recovery Time Objective) bərpa müddəti, **RPO** (Recovery Point Objective) qəbul olunan məlumat itkisi (RTO 4 saat, RPO 1 saat: nüsxə saatda bir). **3-2-1:** üç nüsxə, iki daşıyıcı, biri başqa yerdə; biri dəyişdirilə bilməyən (immutable) və ya şəbəkədən ayrı. Bərpası sınanmayan nüsxə plan deyil.

### İnzibati tədbirlər

| Sənəd | Cavab verdiyi sual |
| --- | --- |
| Siyasət | Nə və niyə? Rəhbərlik təsdiqləyir, məcburi. Məhsul adı və texniki parametr yazılmır |
| Standart | Hansı minimum tələblərlə? Məcburi (məs. MFA üçün FIDO2) |
| Prosedur | Addım-addım necə və kim? |
| Təlimat (guideline) | Tövsiyə, məcburi deyil |

Siyasət hazırlanması: məqsəd və tələblər, əhatə, rollar, ölçülə bilən tələb, pozuntu və eskalasiya, razılaşdırma, təsdiq, tətbiq (standart, prosedur, təlim), ölçmə və dövri yeniləmə. Sahibi, versiyası, baxış tarixi olur; istisna müddətli və risk əsaslıdır. Əsas siyasətlər: məqbul istifadə (AUP), girişə nəzarət, məlumatın təsnifatı, uzaqdan iş, insidentlər, ehtiyat nüsxə, tədarükçü, dəyişikliklər. Personal: yoxlama, məxfilik müqaviləsi (NDA), təlim, joiner, mover, leaver prosesi, vəzifələr ayrılığı, məcburi məzuniyyət.

| Standart | Məzmun |
| --- | --- |
| ISO/IEC 27001:2022 | İTİS tələbləri, sertifikatlaşma |
| ISO/IEC 27002:2022 | 93 nəzarət, 4 mövzu: təşkilati 37, insan 8, fiziki 14, texnoloji 34 |
| ISO/IEC 27005:2022 | Risk idarəsi rəhbərliyi |
| NIST CSF 2.0 (2024) | Govern, Identify, Protect, Detect, Respond, Recover |
| NIST SP 800-53 Rev. 5 | Nəzarətlər kataloqu |
| CIS Controls v8.1 | Prioritetləşdirilmiş tədbirlər |
| NIST SP 800-61 Rev. 3 (2025) | İnsidentə cavab |

### Texniki tədbirlər

| İstiqamət | Tədbirlər |
| --- | --- |
| Kimlik və giriş | IAM, MFA, RBAC, PAM |
| Məlumat | Şifrələmə, DLP, açar idarəetməsi |
| Şəbəkə | Firewall, seqmentləşdirmə, IDS/IPS, NAC, WAF |
| Son nöqtə | EDR, antivirus, tətbiq nəzarəti, sərtləşdirmə |
| Zəiflik | Skan, yamaq, konfiqurasiya yoxlaması |
| Monitorinq | Jurnallar, SIEM, zaman sinxronizasiyası |
| Fasiləsizlik | Ehtiyat nüsxə, replikasiya, bərpa testi |

**Default deny:** icazə verilməyən bağlıdır. Autentifikasiya kimliyi, avtorizasiya səlahiyyəti müəyyən edir. MFA fərqli kateqoriyaları (bilik, sahiblik, biometrik) birləşdirir; **iki parol MFA deyil**. Fişinq proksiləri sessiya tokenini oğurlayır, bildiriş bombardmanı təsdiqə məcbur edir; FIDO2 domenə bağlı olduğu üçün fişinqə davamlıdır. Şifrələmə açar idarəsi olmadan dəyərsizdir. Zəiflik prioriteti aktivin kritikliyi və istismar ehtimalı ilə müəyyən olunur. Tələbə sistemi nümunəsində hər risk sahəsinə fiziki, inzibati (BCP/DR) və texniki tədbir qoşulur.

## Şəbəkə təhlükəsizliyi protokolları

### Təhdidlər və açıq mətn protokolları

Telnet, FTP, HTTP hər şeyi açıq göndərir. OSI üzrə: 2-ci səviyyədə MAC seli, ARP saxtalaşdırması, VLAN hopping (port security, DAI, 802.1X, MACsec); 3-də IP saxtalaşdırması, marşrut oğurluğu (BCP 38, IPsec, RPKI); 4-də SYN seli, port skanı (SYN cookies); 5–6-da versiya endirmə, MITM (TLS); 7-də inyeksiya, parol oğurluğu (HTTPS, DNSSEC, SPF/DKIM/DMARC, SSH). ARP autentifikasiyasızdır; MAC 48 bitdir. TCP-nin SYN, SYN-ACK, ACK əl sıxması etibarlıdır, təhlükəsiz deyil; port təhlükəsizlik sərhədi deyil.

| Köhnə | Əvəzi | Qeyd |
| --- | --- | --- |
| Telnet (TCP 23) | SSH (TCP 22) | Açarla autentifikasiya |
| HTTP (TCP 80) | HTTPS (TCP 443) | HTTP + TLS, HSTS |
| FTP (TCP 20/21) | SFTP (SSH üzərində, 22), FTPS (explicit 21, implicit 990) | Fərqli protokollar |
| SNMP v1/v2c (UDP 161) | SNMPv3 | Community string açıq gedir |
| DNS (53) | DNSSEC, DoT (853), DoH (443) | DNSSEC şifrələmir |
| LDAP (TCP 389) | LDAPS (TCP 636), StartTLS | Sorğular şifrələnir |
| POP3, IMAP | POP3S, IMAPS | Poçt qəbulu |
| SMTP | TCP 25 + STARTTLS; göndərmə TCP 587 + STARTTLS və ya TCP 465 + Implicit TLS | Məktub ucdan uca şifrələnmir |
| NTP (UDP 123) | NTS (RFC 8915) | Vaxt saxtakarlığı |

### SSH

SSH TCP 22-də üç qatdan ibarətdir: nəqliyyat (server autentifikasiyası, açar, şifrələmə), autentifikasiya (istifadəçi), bağlantı (çoxlu kanal). Host açarı **TOFU** (Trust On First Use) ilə qəbul olunur: ilk qoşulmada barmaq izi başqa kanalla yoxlanmalıdır, əks halda ortadakı hücumçunun açarı qəbul edilə bilər; sonra açar dəyişsə SSH xəbərdarlıq verir və known_hosts sətri yoxlamadan silinmir. İstifadəçi üçün açar cütü işlədilir (gizli açar istifadəçidə, açıq açar authorized_keys-də); parol şəbəkəyə çıxmır. Sərtləşdirmə: PermitRootLogin no, PasswordAuthentication no, AllowTcpForwarding no. `ssh -L` yerli port yönləndirir, `ssh -D` SOCKS proksi yaradır, `ssh -A` agent yönləndirir; üçü də risklidir. SSH yenilənməlidir: regreSSHion (CVE-2024-6387, OpenSSH-də autentifikasiyasız kod icrası) və XZ Utils arxa qapısı (CVE-2024-3094).

### E-poçt, SNMP, NTP

SMTP göndərənin kimliyini yoxlamır, STARTTLS bunu həll etmir.

| Mexanizm | Yoxlayır | DNS |
| --- | --- | --- |
| SPF | Göndərən IP domenin siyahısındadırmı (zərf domeni) | TXT |
| DKIM | Rəqəmsal imza doğrudurmu | TXT, selector._domainkey |
| DMARC | SPF/DKIM nəticəsi "From" ilə uyğundurmu (alignment), uğursuzluqda nə edilsin | TXT, _dmarc |

DMARC siyasətləri: none (hesabat), quarantine (spam), reject (rədd); none ilə başlanıb sərtləşdirilir. MTA-STS STARTTLS endirilməsinin qarşısını alır; ucdan uca məxfilik üçün S/MIME və ya PGP.

SNMP v1/v2c-də community string açıqdır; SNMPv3 səviyyələri noAuthNoPriv, authNoPriv, authPriv (sonuncu seçilir); yalnız idarəetmə şəbəkəsindən əlçatan olmalıdır. NTP vaxtı sinxronlaşdırır; Kerberos, sertifikat yoxlaması və SIEM vaxtdan asılıdır; NTS (Network Time Security) autentifikasiya əlavə edir; monlist (CVE-2013-5211) gücləndirmə hücumlarında işlədilib.

### IPsec, 802.1X, RADIUS, uzaqdan idarəetmə

| | IPsec | TLS | SSH |
| --- | --- | --- | --- |
| Səviyyə | Şəbəkə (3) | Nəqliyyatla tətbiq arası | Tətbiq |
| Qoruyur | Bütün IP trafiki | Tətbiq bağlantısı | Sessiya, fayl |
| Kimlik | Sertifikat, PSK, EAP | X.509 | Host və istifadəçi açarı |

IPsec: IKE açarları razılaşdırır (SA), AH yalnız tamlıq verir, ESP şifrələmə və tamlıq (praktikada həmişə ESP); detallar 7-ci mövzudadır. **802.1X** portda autentifikasiyaya qədər girişi bağlayır; rollar: supplicant (cihaz), authenticator (kommutator/AP), authentication server (RADIUS). Trafiki şifrələmir. **NAC** cihaz vəziyyətini yoxlayıb uyğunsuzu karantin VLAN-ına göndərir. RADIUS UDP 1812/1813, TACACS+ (TCP 49) inzibati giriş üçün hər əmri avtorizə edir. Blast-RADIUS (CVE-2024-3596) RADIUS-un MD5 cavab yoxlamasına hücumdur: Message-Authenticator məcburi, RADIUS TLS üzərində.

Uzaqdan idarəetmə: portlar İnternetə açılmır; VPN, sonra jump host; fərdi hesab və MFA; müvəqqəti hüquq; sessiya jurnalı, PAM; idarəetmə kompüteri poçt və veb üçün işlədilmir; ayrıca idarəetmə VLAN-ı və out-of-band kanal.

## TLS/SSL və sertifikatlar

### TLS və versiyalar

TLS (Transport Layer Security) üç xidmət verir: məxfilik, tamlıq, autentifikasiya (adətən yalnız server; **mTLS**-də müştəri də). İki qat: əl sıxma protokolu və record protokolu. İstifadə: HTTPS 443 (HTTP/3 QUIC üzərində), SMTPS 465, Submission 587, IMAPS 993, POP3S 995, LDAPS 636, FTPS, DoT 853, syslog 6514. UDP üçün DTLS (Datagram TLS).

| Versiya | Status |
| --- | --- |
| SSL 2.0 (RFC 6176), SSL 3.0 (RFC 7568) | Qadağan; POODLE |
| TLS 1.0, 1.1 | Köhnəlib (RFC 8996); BEAST |
| TLS 1.2 | Düzgün sazlananda qəbul edilir |
| TLS 1.3 (2018) | Tövsiyə; köhnə alqoritmlər çıxarılıb |

### Alqoritmlər və irəli məxfilik

Asimmetrik kriptoqrafiya yalnız tanıma və açar razılaşması üçün, məlumat simmetrik şifrələnir.

| Vəzifə | Müasir | Zəif |
| --- | --- | --- |
| Açar mübadiləsi | (EC)DHE və DHE (X25519), X25519MLKEM768 | Statik RSA, statik DH |
| İmza | ECDSA, RSA-PSS, Ed25519 | RSA-PKCS#1 v1.5 + MD5/SHA-1 |
| Şifr | AES-GCM, ChaCha20-Poly1305 (AEAD) | RC4, 3DES, CBC |
| Heş/açar törətmə | SHA-256, SHA-384, HKDF | MD5, SHA-1 |

Şifr dəsti oxunuşu: TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256 = açar mübadiləsi ECDHE, server imzası RSA sertifikat, şifr AES-128 GCM, heş SHA-256. TLS 1.3 adı qısadır (TLS_AES_128_GCM_SHA256 və s.). **Diffie-Hellman** açıq kanalda ortaq sirr yaradır (diskret loqarifm çətinliyi), amma kimliyi sübut etmir; MITM-i server imzası dayandırır.

**İrəli məxfilik (forward secrecy):** ECDHE-də hər sessiyanın müvəqqəti açarı silinir, serverin gizli açarı sonra oğurlansa da köhnə trafik açılmır. Statik RSA-da premaster_secret server açıq açarı ilə şifrələnir, ona görə açar oğurlananda yazılmış trafik açılır. TLS 1.3 statik RSA-nı çıxarıb; yalnız PSK-only (psk_ke) və 0-RTT irəli məxfilik vermir.

### Əl sıxması

**Ardıcıllıq.** ClientHello (versiya, şifr dəstləri, təsadüfi ədəd, SNI; TLS 1.3-də key_share də) → ServerHello. TLS 1.2-də sertifikat və imzalı ServerKeyExchange açıq gəlir, tərəflər ChangeCipherSpec və Finished ilə keçir (2-RTT). TLS 1.3-də ortaq sirr ServerHello ilə hazırdır, sonrası şifrəlidir; CertificateVerify serverin gizli açara sahibliyini (heşin imzası), Finished isə tarixçənin eyniliyini (HMAC) təsdiqləyir (1-RTT). key_share qrupu uyğun deyilsə HelloRetryRequest.

| | TLS 1.2 | TLS 1.3 |
| --- | --- | --- |
| Əl sıxması | 2-RTT | 1-RTT (0-RTT seçimi) |
| Sertifikat | Açıq | Şifrəli |
| Çıxarılanlar | | Statik RSA, RC4, 3DES, CBC, sıxılma, yenidən danışıq |
| Açar törətmə | PRF | HKDF |

**0-RTT** replay (təkrar göndərmə) hücumuna açıqdır, yalnız vəziyyəti dəyişməyən sorğular (GET) üçündür; ödənişdə söndürülür.

### Sertifikatlar

Sertifikat domeni açıq açarla bağlayır və CA imzalayır. Sahələr: subyekt, CA, tarixlər, açıq açar, SAN (domen buradan yoxlanır), keyUsage, EKU (serverAuth), basicConstraints (CA:TRUE yalnız CA-da). Növlər: **DV** (domen nəzarəti, Let's Encrypt), **OV** (təşkilat), **EV** (ətraflı hüquqi yoxlama). Kilid saytın dürüstlüyünü yox, kanalın qorunduğunu göstərir; fişinq də DV ala bilir.

Brauzer yoxlayır: zəncir etibar anbarındakı kökə çatırmı (server + aralıq sertifikat), imzalar, tarix, SAN, ləğv. Kök açarı oflayndır, aralıq CA gündəlik imzalayır.

- **CRL** (Certificate Revocation List): dövri ləğv siyahısı.
- **OCSP:** real vaxt sorğusu, istifadəçinin saytını CA-ya açır; **OCSP stapling** təsdiqi serverin cavabına qoşur.
- Müddətlər qısalır (SC-081v3: 200, 100, 47 gün), yeniləmə ACME (RFC 8555) ilə avtomatlaşdırılır; bitmiş portal sertifikatı hücum yox, inventar problemidir.
- Xətalar: NET::ERR_CERT_DATE_INVALID (müddət, saat), ERR_CERT_COMMON_NAME_INVALID (domen SAN-da yox), ERR_CERT_AUTHORITY_INVALID (zəncir, özünü imzalama, MITM), ERR_CERT_REVOKED, ERR_SSL_VERSION_OR_CIPHER_MISMATCH. Kütləvi AUTHORITY_INVALID MITM əlaməti ola bilər.
- **mTLS:** müştəri də sertifikatla imza atır (xidmətlərarası, SIEM agenti, EAP-TLS); daxili PKI tələb edir.
- **DigiNotar** (2011) sındırıldı, *.google.com üçün saxta sertifikat; cavab **Certificate Transparency** (RFC 6962): açıq, yalnız əlavə olunan jurnallar.

### Hücumlar, HSTS, ECH, konfiqurasiya

| Hücum | Mahiyyət / qorunma |
| --- | --- |
| SSL stripping | İstifadəçini HTTP-də saxlayır; HSTS |
| BEAST | TLS 1.0 CBC IV; TLS 1.2+, AEAD |
| CRIME | Sıxılma sirri açır; sıxılmanı söndür |
| Heartbleed | OpenSSL Heartbeat uzunluq yoxlamır (CVE-2014-0160), 64 KB yaddaş sızır; yenilə, açarları və sertifikatları dəyiş |
| POODLE | SSL 3.0 padding; SSL 3.0 söndür |
| FREAK, Logjam | Export zəif şifrlərə endirmə |
| DROWN | SSLv2 eyni açarda TLS-i zəiflədir |
| ROBOT | RSA padding oracle; statik RSA söndür |

TLS tətbiqi qorumur (SQL inyeksiyası, XSS). SNI domeni, ALPN protokolu (h2, http/1.1) seçir; QUIC TLS 1.3-ü işlədir, record qatını yox. Metaməlumat (IP, vaxt, həcm, SNI) qalır; **ECH** (Encrypted Client Hello, RFC 9849) həssas hissəni şifrələyir. **HSTS** (RFC 6797) brauzeri yalnız HTTPS-ə məcbur edir, preload ilk ziyarət problemini həll edir. Sessiya bərpası (bilet, PSK) açar sızmasında irəli məxfiliyi pozur, bilet açarları dəyişdirilir. "Harvest now, decrypt later" səbəbindən ML-KEM (FIPS 203) və hibrid X25519MLKEM768 işlənir.

Konfiqurasiya: TLSv1.2 və 1.3, HSTS, ACME, tam zəncir, zəif şifrlərin söndürülməsi, açar 0600, daxili trafik də TLS. Yoxlama: `openssl s_client`, `nmap --script ssl-enum-ciphers`, Wireshark (`tls.handshake.type == 1`), Qualys SSL Labs, NIST SP 800-52 Rev. 2.

## DNS təhlükəsizliyi və DNSSEC

### DNS və hücumlar

DNS adı IP-yə çevirir: rekursiv həlledici kök, TLD, avtoritativ server yolu ilə A qeydini alır, TTL qədər keşləyir. Cavabın orijinallığı yoxlanmır, həlledici yalnız TXID (16 bit), mənbə portu və adı uyğunlaşdırır. Qeydlər: A, AAAA, CNAME, MX, NS, TXT, PTR, SOA. UDP 53, böyük cavab və AXFR üçün TCP 53; EDNS(0) və DO bayrağı ilə DNSSEC cavabları böyükdür.

| Hücum | Qorunma |
| --- | --- |
| Keş zəhərlənməsi | Təsadüfi port və TXID, DNSSEC |
| DNS spoofing (LAN) | DHCP snooping, DAI, DNSSEC, DoT/DoH |
| Domen ələ keçirilməsi (registrator) | MFA, Registry Lock |
| DNS tunelləmə | Log analizi, çıxışı məhdudlaşdırma |
| Gücləndirmə (amplification) | Açıq həlledicini bağla, RRL, BCP 38 |
| NXDOMAIN seli | Sürət limiti, anycast |

**Kaminski** (CVE-2008-1447, 2008): sabit mənbə portu ilə yalnız 65 536 TXID tapmaq kifayət idi; mövcud olmayan a1, a2... adları ilə hər dəfə yeni yarış başladılır və saxta cavaba bütöv domen üçün NS qeydi qoşulurdu. Port təsadüfiləşdirilməsi (≈2³²) yalnız ehtimalı azaldır; yolda olan hücumçuya qarşı həll imzadır.

### DNSSEC

DNSSEC (RFC 4033–4035, RFC 9364) imza əlavə edir: mənşə autentifikasiyası, tamlıq, adın olmamasının sübutu. **Şifrələmir** (məxfilik üçün DoT/DoH), DDoS-dan və registrator hesabının ələ keçirilməsindən qorumur, yoxlamayan həlledicidə işləmir.

| Qeyd | Vəzifə |
| --- | --- |
| RRSIG | RRset imzası |
| DNSKEY | Açıq açar (257 KSK, 256 ZSK) |
| DS | Valideyndə uşağın KSK heşi, etibar körpüsü |
| NSEC, NSEC3 | Adın yoxluq sübutu; NSEC3 heşlənmiş (RFC 5155) |
| CDS, CDNSKEY | Uşağın valideynə yeni DS siqnalı |

**ZSK** (Zone Signing Key) qeydləri imzalayır, tez dəyişir; **KSK** (Key Signing Key) DNSKEY dəstini imzalayır, DS ona istinad edir; tək açarla CSK. Alqoritmlər: 13 (ECDSA P-256/SHA-256), 8 (RSA/SHA-256), 15 (Ed25519); 5 və 7 köhnəlib.

**Etibar zənciri:** yoxlayan həlledici (validating resolver) kök KSK-nı etibar lövbəri (trust anchor) kimi saxlayır; kök DNSKEY, sonra example. üçün DS, example. DNSKEY, universitet.example. DS və DNSKEY, sonda A qeydinin RRSIG imzası ardıcıl yoxlanır. Nəticələr: **Secure** (AD bayrağı), **Insecure** (DS yoxluğu imzalı sübutdur), **Indeterminate** (lövbər yox), **Bogus** (imza səhv/bitmiş: SERVFAIL). DO bayrağı DNSSEC qeydlərini istəyir, CD yoxlamanı söndürür; `dig +dnssec` yoxlamır, `delv` yoxlayır. AD bayrağına yalnız etibarlı həlledici və qorunan kanalda inanılır. Saxta cavab zəncirin heç yerində imzalana bilmir; replay isə imza müddəti bitənə qədər keçir, ona görə müddətlər qısadır.

| | TLS PKI | DNSSEC |
| --- | --- | --- |
| Başlanğıc | Yüzlərlə kök CA | Bir kök zona |
| Sızma | Bir CA hər domen üçün saxta sertifikat verə bilər | Zonanın aşağısı ilə məhdud |

**Yoxluğun sübutu:** NSEC növbəti mövcud adı göstərir, yan təsiri zona siyahılanması (zone walking). NSEC3 heşləyir, lüğət hücumu qalır, "ağ yalanlar" (compact denial) cavabı anında imzalayır; RFC 9276 iterasiya 0 tövsiyə edir. NXDOMAIN ad yoxdur, NODATA (kod NOERROR) ad var, tip yoxdur.

**Açar idarəsi:** key rollover; ZSK üçün pre-publish. Kök KSK 2018-də dəyişdi, KSK-2024 (38696) 2025-də əlavə edildi, 11 oktyabr 2026-dan imzalayır, KSK-2017 11 yanvar 2027-də ləğv olunur; yeni açar RFC 5011 ilə 30 günlük hold-down-dan sonra qəbul edilir. Slack (2021) DNSSEC işə salanda xidmət əlçatmaz oldu: DS silmək keş TTL səbəbilə kifayət etmədi.

| | Port | Qoruyur |
| --- | --- | --- |
| DNSSEC | 53 | Bütövlük, mənşə |
| DoT (RFC 7858) | TCP 853 | Məxfilik, kanal |
| DoH (RFC 8484) | TCP 443 | Məxfilik; korporativ DNS-dən yan keçə bilir |
| DoQ (RFC 9250) | UDP 853 | Məxfilik, QUIC üzərində |

Bunlar bir-birini əvəz etmir. DANE (RFC 6698) TLSA qeydləri ilə sertifikatı domenə bağlayır. Qurulma: dəstək yoxlanır, açarlar və alqoritm 13, inline signing (Bind, PowerDNS), DS registratorda, yoxlama (dig, delv, DNSViz, Verisign Analyzer), həlledicidə `dnssec-validation auto` (BIND) və ya validator iterator (Unbound), monitorinq, geri qaytarma planı.

DNSSEC quraraq provayderin baxdığı saytları gizlətmək olmaz: sorğular açıq qalır, məxfilik DoT (DNS over TLS) və DoH ilə gəlir.
