+++
title = "Təhlükəsizlik tədbirləri və şəbəkə təhlükəsizliyi protokolları"
unit = "qisa"
order = 4
summary = "Mövzunun skeleti: hər anlayış bir sətirdə. Tədbirlər, protokolların təhlükəsiz əvəzləri, SSH, e-poçt, TLS, sertifikatlar, DNS hücumları və DNSSEC."
updated = 2026-11-09

[[source]]
title = "Mühazirə 4: Təhlükəsizlik tədbirləri və şəbəkə təhlükəsizliyi protokolları"
note = "Elmar Cabbarov, 2026–2027"
+++

Hər anlayış bir sətirdə; izahlı variant orta və uzun səviyyədədir. Universitet nümunələri şərtidir.

## Təhlükəsizlik tədbirləri

### Risk

| Anlayış | Mənası |
| --- | --- |
| Aktiv, təhdid, zəiflik | Dəyərli şey; ona zərər verə biləcək subyekt; istifadə olunan çatışmazlıq |
| Risk | Ehtimal **və** təsir (təkcə ehtimal yox) |
| Tədbir (control) | Riski azaldan təşkilati, texniki, fiziki addım |
| Qalıq risk | Tədbirdən sonra qalan; rəhbərlik yazılı qəbul edir |
| SLE, ARO, ALE | Single Loss Expectancy (bir hadisənin ziyanı), Annualized Rate of Occurrence (ildə say), Annualized Loss Expectancy: **ALE = SLE × ARO** |

Keyfiyyət üsulu 1–5 şkalasıdır (3 × 5 = 15). Nümunə: 20 000 × 0,5 = 10 000; EDR 4000 və ARO 0,1 → ALE 2000, fayda 4000. Dörd cavab: azaltmaq, ötürmək, qaçmaq, qəbul etmək.

### Təsnifat

Növ (fiziki, inzibati, texniki) və funksiya iki müstəqil oxdur; cavabda ikisini də yaz.

| Funksiya | Fiziki | İnzibati | Texniki |
| --- | --- | --- | --- |
| Qarşısını alan | Kilid, turniket, mantrap | Siyasət, təlim | Firewall, MFA, şifrələmə |
| Aşkarlayan | CCTV, sensor | Audit, hüquq baxışı | IDS, SIEM, antivirus |
| Düzəldən | Yanğınsöndürmə | İnsidentə cavab planı | Yamaq, karantin |
| Çəkindirən | Kamera lövhəsi | İntizam qaydası | Xəbərdarlıq mətni |

Əlavə: bərpaedici (recovery; ehtiyat nüsxə), kompensasiyaedici (compensating; yamaqsız cihazı ayrı seqmentə), yönləndirici (directive; "USB qadağandır"). Çoxsəviyyəli müdafiə (*defense in depth*): qat-qat tədbir. Seçim riskə, xərc-fayda müqayisəsinə görədir; effektivlik ölçülür.

### Fiziki və ətraf mühit

- **Giriş:** mexaniki kilid, elektron kart, PIN, biometrika, turniket, mantrap (şlüz), videomüşahidə.
- **FAR** (False Acceptance Rate) yad qəbulu, **FRR** (False Rejection Rate) icazəlinin rəddi, **CER** (Crossover Error Rate) kəsişmə nöqtəsi.
- **Tailgating:** ardınca keçmə; maarifləndirmə də lazımdır. Ziyarətçi qeydiyyatı, müşayiət, itirilmiş kartın ləğvi.
- **Server otağı:** pəncərəsiz, kilidli, jurnal, minimum imtiyaz, vəzifələr ayrılığı; təmiz masa və ekran; təhlükəsiz silmə, kriptoqrafik silmə, fiziki məhv.
- **Mühit:** ASHRAE temperatur diapazonu, rütubət (statik elektrik, kondensasiya), qaz və pre-action yanğınsöndürmə, su sızma sensoru.
- **Enerji:** UPS (qısa kəsinti), generator (uzun), soyutma, torpaqlama. Artıqlıq (*redundancy*) N+1; ortaq asılılıq = real artıqlıq yox.
- **Fasiləsizlik:** RTO (Recovery Time Objective, bərpa müddəti), RPO (Recovery Point Objective, qəbul olunan itki), 3-2-1 qaydası, immutable nüsxə; bərpa sınanmalıdır.

:::exam
**Fail-safe:** yanğında qapı içəridə kilidləmir (insan həyatı birinci). **Fail-secure:** elektrik kəsiləndə server otağı açıq qalmır. Çıxış həmişə əl ilə açılır.
:::

### İnzibati tədbirlər

| Sənəd | Sual |
| --- | --- |
| Siyasət | Nə və niyə; rəhbərlik təsdiqləyir; məcburi; məhsul adı yazılmır |
| Standart | Hansı minimum tələblərlə; məcburi |
| Prosedur | Addım-addım necə və kim |
| Təlimat (guideline) | Tövsiyə, məcburi deyil |

Siyasət: məqsəd, əhatə, rollar, ölçülə bilən tələb, pozuntu və eskalasiya, təsdiq, yenilənmə; sahib, versiya, baxış tarixi, müddətli istisna. Siyasətlər: məqbul istifadə (AUP), girişə nəzarət, təsnifat, uzaqdan iş, insident, ehtiyat nüsxə, tədarükçü, dəyişiklik. Personal: yoxlama, NDA, təlim, joiner, mover, leaver, vəzifələr ayrılığı, məcburi məzuniyyət.

Standartlar: ISO/IEC 27001:2022 (İTİS tələbləri), 27002:2022 (93 nəzarət, 4 mövzu: 37+8+14+34), 27005:2022 (risk idarəsi), NIST CSF 2.0 (Govern, Identify, Protect, Detect, Respond, Recover), NIST SP 800-53 Rev. 5, CIS Controls v8.1, NIST SP 800-61 Rev. 3.

### Texniki tədbirlər

- **Kimlik:** IAM, MFA, RBAC, PAM. **Məlumat:** şifrələmə, DLP, açar idarəsi. **Şəbəkə:** firewall, seqmentləşdirmə, IDS/IPS, NAC, WAF. **Son nöqtə:** EDR, antivirus, sərtləşdirmə. **Zəiflik:** skan, yamaq. **Monitorinq:** SIEM, zaman sinxronizasiyası. **Fasiləsizlik:** nüsxə, replikasiya.
- **Default deny.** Autentifikasiya kimliyi, avtorizasiya səlahiyyəti təsdiqləyir.
- **MFA** fərqli kateqoriyalar (bilik, sahiblik, biometrik); iki parol MFA deyil. Fişinq proksisi tokeni oğurlayır; FIDO2 fişinqə davamlıdır.

## Şəbəkə təhlükəsizliyi protokolları

### Təhdidlər

| OSI | Hücum | Qorunma |
| --- | --- | --- |
| 2 | MAC seli, ARP saxtalaşdırması, VLAN hopping | Port security, DAI, 802.1X, MACsec |
| 3 | IP saxtalaşdırması, marşrut oğurluğu | BCP 38, IPsec, RPKI |
| 4 | SYN seli, port skanı | SYN cookies, firewall |
| 5–6 | Versiya endirmə, MITM | TLS |
| 7 | İnyeksiya, parol oğurluğu | HTTPS, DNSSEC, SPF/DKIM/DMARC, SSH |

TCP-nin SYN, SYN-ACK, ACK əl sıxması etibarlıdır, təhlükəsiz deyil; port sərhəd deyil; MAC 48 bit; ARP autentifikasiyasızdır.

### Açıq mətndən təhlükəsizə

| Köhnə | Əvəzi |
| --- | --- |
| Telnet (TCP 23) | SSH (TCP 22) |
| HTTP (TCP 80) | HTTPS (TCP 443), HSTS |
| FTP (TCP 20/21) | SFTP (SSH üzərində) və ya FTPS (explicit 21, implicit 990): fərqli protokollar |
| SNMP v1/v2c (UDP 161) | SNMPv3 |
| DNS (53) | DNSSEC; DoT (DNS over TLS, 853), DoH (443) |
| LDAP (TCP 389) | LDAPS (TCP 636), StartTLS |
| POP3, IMAP | POP3S, IMAPS |
| SMTP | TCP 25 + STARTTLS; göndərmə TCP 587 + STARTTLS və ya TCP 465 + Implicit TLS |
| NTP (UDP 123) | NTS (Network Time Security, RFC 8915) |

### SSH

- Üç qat: nəqliyyat, autentifikasiya, bağlantı. Açar cütü (gizli açar istifadəçidə, açıq authorized_keys-də).
- **TOFU** (Trust On First Use): ilk host açarı başqa kanalla yoxlanır; dəyişəndə xəbərdarlığı yoxlamadan keçmə. Alternativ: SSH sertifikatları.
- Sərtləşdirmə: PermitRootLogin no, PasswordAuthentication no, AllowTcpForwarding no. Tunel: `ssh -L`, `ssh -D`; agent: `ssh -A` (risklidir).
- Zəifliklər: regreSSHion (CVE-2024-6387), XZ Utils arxa qapısı (CVE-2024-3094).

### E-poçt, SNMP, NTP

| Mexanizm | Yoxlayır |
| --- | --- |
| SPF | Göndərən IP domenin siyahısındadır (TXT) |
| DKIM | İmza doğrudur (TXT, selector._domainkey) |
| DMARC | SPF/DKIM "From" ilə uyğundur (alignment); none, quarantine, reject (TXT, _dmarc) |

STARTTLS göndərənin kimliyini yoxlamır; MTA-STS endirməni dayandırır; ucdan uca: S/MIME, PGP. SNMPv3: noAuthNoPriv, authNoPriv, authPriv (seçilən); yalnız idarəetmə şəbəkəsi. NTP vaxtı (Kerberos, sertifikat, SIEM) sinxronlaşdırır; monlist (CVE-2013-5211).

### IPsec, 802.1X, uzaqdan idarəetmə

- **IPsec:** şəbəkə qatı, IKE açar razılaşdırır (SA), AH yalnız tamlıq, ESP şifrələmə; nəqliyyat və tunel rejimi (7-ci mövzu). TLS tətbiq bağlantısını, SSH sessiyanı qoruyur.
- **802.1X:** supplicant, authenticator, authentication server (RADIUS UDP 1812/1813). Şifrələmir. **NAC** uyğunsuzu karantin VLAN-ına göndərir.
- **TACACS+** (TCP 49): hər əmri avtorizə edir. **Blast-RADIUS** (CVE-2024-3596): MD5 cavab; Message-Authenticator və TLS.
- **Uzaqdan idarəetmə:** portlar açılmır, VPN, jump host, fərdi hesab + MFA, müvəqqəti hüquq, PAM, ayrıca VLAN və out-of-band kanal.

## TLS/SSL və sertifikatlar

### TLS

TLS (Transport Layer Security): məxfilik, tamlıq, autentifikasiya (**mTLS**-də müştəri də). Əl sıxma və record qatları. Portlar: HTTPS 443 (QUIC), 465, 587, IMAPS 993, POP3S 995, LDAPS 636, DoT 853, syslog 6514; UDP üçün DTLS (Datagram TLS).

| Versiya | Status |
| --- | --- |
| SSL 2.0 (RFC 6176), SSL 3.0 (RFC 7568) | Qadağan; POODLE |
| TLS 1.0, 1.1 | Köhnə (RFC 8996); BEAST |
| TLS 1.2 | Düzgün sazlananda |
| TLS 1.3 | Tövsiyə |

| Vəzifə | Müasir | Zəif |
| --- | --- | --- |
| Açar | (EC)DHE və DHE, X25519MLKEM768 | Statik RSA, statik DH |
| İmza | ECDSA, RSA-PSS, Ed25519 | RSA-PKCS#1 v1.5 + MD5/SHA-1 |
| Şifr | AES-GCM, ChaCha20-Poly1305 (AEAD) | RC4, 3DES, CBC |
| Heş | SHA-256, SHA-384, HKDF | MD5, SHA-1 |

Asimmetrik yalnız tanıma və açar razılaşması, məlumat simmetrik. **Diffie-Hellman** ortaq sirr yaradır, kimliyi sübut etmir (imza edir). Şifr dəsti: TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256 = ECDHE açar, RSA sertifikat imzası, AES-128 GCM, SHA-256. **İrəli məxfilik (forward secrecy):** ECDHE müvəqqəti açar, oğurlanmış server açarı köhnə trafiki açmır; statik RSA açır.

### Əl sıxması

ClientHello (versiya, şifrlər, SNI, TLS 1.3-də key_share) → ServerHello. TLS 1.2: sertifikat və ServerKeyExchange açıq, ChangeCipherSpec, Finished, 2-RTT. TLS 1.3: 1-RTT, sertifikat şifrəli, CertificateVerify (gizli açar sübutu), Finished (HMAC), uyğunsuzluqda HelloRetryRequest; statik RSA, RC4, 3DES, CBC, sıxılma çıxarılıb; HKDF. **0-RTT** replay hücumuna açıqdır, yalnız GET.

### Sertifikatlar

- X.509: subyekt, CA, tarix, açıq açar, SAN (domen buradan yoxlanır), keyUsage, EKU (serverAuth), basicConstraints (CA:TRUE).
- **DV** (domen; Let's Encrypt), **OV** (təşkilat), **EV** (hüquqi yoxlama). Kilid kanalı göstərir, dürüstlüyü yox.
- Zəncir: server, aralıq, kök (etibar anbarı); tarix, SAN, ləğv yoxlanır.
- Ləğv: **CRL** (Certificate Revocation List), **OCSP**, **OCSP stapling**. Müddətlər qısalır (SC-081v3), yeniləmə ACME (RFC 8555) ilə.
- Xətalar: NET::ERR_CERT_DATE_INVALID, ERR_CERT_COMMON_NAME_INVALID, ERR_CERT_AUTHORITY_INVALID, ERR_CERT_REVOKED, ERR_SSL_VERSION_OR_CIPHER_MISMATCH; kütləvi xəta MITM əlaməti.
- mTLS: EAP-TLS, xidmətlər arası. **DigiNotar** (2011) saxta *.google.com; cavab **Certificate Transparency**.

### Hücumlar və qorunma

| Hücum | Nə / qorunma |
| --- | --- |
| SSL stripping | HTTP-də saxlayır; HSTS (RFC 6797) |
| BEAST, CRIME | CBC IV; sıxılma |
| Heartbleed | OpenSSL yaddaş sızması (CVE-2014-0160); yenilə, açarları dəyiş |
| POODLE, FREAK, Logjam, DROWN, ROBOT | SSL 3.0 padding; export endirmə; SSLv2; RSA oracle |

TLS tətbiqi qorumur. SNI domeni, ALPN (h2) protokolu seçir; **ECH** (Encrypted Client Hello, RFC 9849) SNI-ni gizlədir. Bilet və PSK bərpası açar sızmasında riskli. ML-KEM (FIPS 203): kvant təhlükəsinə hibrid cavab. Yoxlama: `openssl s_client`, nmap, Wireshark, Qualys SSL Labs, NIST SP 800-52 Rev. 2; nginx: yalnız TLSv1.2/1.3 və HSTS.

## DNS təhlükəsizliyi və DNSSEC

### DNS hücumları

DNS: rekursiv həlledici, kök, TLD, avtoritativ server, TTL keşi; TXID (16 bit) və port yoxlanır. Qeydlər: A, AAAA, CNAME, MX, NS, TXT, PTR, SOA. UDP/TCP 53, AXFR, EDNS(0).

| Hücum | Qorunma |
| --- | --- |
| Keş zəhərlənməsi | Təsadüfi port/TXID, DNSSEC |
| DNS spoofing (LAN) | DHCP snooping, DAI, DoT/DoH |
| Domen ələ keçirilməsi | MFA, Registry Lock |
| Tunelləmə | Log analizi |
| Gücləndirmə (amplification) | RRL, BCP 38 |
| NXDOMAIN seli | Limit, anycast |

**Kaminski** (CVE-2008-1447): sabit port, mövcud olmayan adlar, NS qeydi; port təsadüfiləşdirməsi yalnız ehtimalı azaldır.

### DNSSEC

Verir: mənşə autentifikasiyası, tamlıq, yoxluq sübutu. **Şifrələmir**, DDoS və registrator hesabından qorumur.

| Qeyd | Vəzifə |
| --- | --- |
| RRSIG | RRset imzası |
| DNSKEY | Açıq açar (257 KSK, 256 ZSK) |
| DS | Valideyndə uşağın KSK heşi |
| NSEC, NSEC3 | Yoxluq sübutu (NSEC3 heşlənmiş) |
| CDS | Uşaqdan valideynə DS siqnalı |

- **ZSK** (Zone Signing Key) qeydləri, **KSK** (Key Signing Key) DNSKEY dəstini imzalayır; CSK tək açar. Alqoritm 13 (ECDSA P-256/SHA-256), 8 (RSA/SHA-256), 15.
- **Etibar zənciri:** validating resolver kök KSK-nı trust anchor kimi saxlayır; DS → DNSKEY → RRSIG kökdən aşağı. **Secure** (AD), **Insecure**, **Indeterminate**, **Bogus** (SERVFAIL). DO istəyir, CD söndürür; `dig +dnssec` yoxlamır, `delv` yoxlayır. Replay: imza müddəti qısa.
- **Yoxluq:** NSEC zone walking-ə yol verir, NSEC3 heşləyir, compact denial. NXDOMAIN (ad yox), NODATA (kod NOERROR, tip yox).
- **Açar idarəsi:** key rollover, pre-publish, kök KSK-2024 (RFC 5011); Slack (2021) nasazlığı.
- **DoT, DoH, DoQ** məxfilik verir; DNSSEC bütövlük; bir-birini əvəz etmir. DANE (TLSA) sertifikatı domenə bağlayır; DNSViz yoxlayır.
