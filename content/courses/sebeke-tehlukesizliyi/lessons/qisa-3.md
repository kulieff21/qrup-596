+++
title = "Girişə nəzarət prinsipləri və modelləri; identifikasiya və giriş idarəetməsi (IAM)"
unit = "qisa"
order = 3
summary = "Mövzunun bütün anlayışları bir-iki cümlə ilə: AAA, faktorlar və FIDO2, parol siyasəti, DAC/MAC/RBAC/ABAC, BLP və Biba, IAM, SSO, Kerberos, OAuth/OIDC, PAM, sıfır etimad və hücumlar."
updated = 2026-11-09

[[source]]
title = "Mühazirə 3: Girişə nəzarət prinsipləri və modelləri; identifikasiya və giriş idarəetməsi (IAM)"
note = "Elmar Cabbarov, 2026–2027"
+++

Girişə nəzarət (access control) subyektin obyekt üzərində əməliyyatına icazə verən və ya onu rədd edən qaydalar və mexanizmlərdir. Universitet nümunələri şərti tədris nümunəsidir.

## Siyasətdən giriş qərarına

| Anlayış | Nədir |
| --- | --- |
| Subyekt / obyekt / əməliyyat | Subyekt sorğunu başladan aktiv tərəf (proses, xidmət hesabı), obyekt qorunan resurs (fayl, API, LMS kursu), əməliyyat oxuma, yazma, icra və s. Giriş obyekti əlçatanlıq (availability) deyil. |
| Siyasət, model, mexanizm | Siyasət universitetin tələbi, model onun dəqiq təsviri, mexanizm modelin sistemdə icrasıdır. |
| İstinad monitoru (reference monitor) | Hər sorğunu siyasətə görə yoxlayır: yan keçilməməli, dəyişdirilməməli, yoxlanacaq qədər kiçik olmalıdır. |
| Giriş matrisi, ACL, capability list | Matris: sətir subyekt, sütun obyekt. ACL sütun üzrə (obyektin icazəli subyektləri), səlahiyyət siyahısı sətir üzrə saxlayır. |
| PEP, PDP, PAP, PIP | İcra, qərar, siyasət idarəsi və atribut mənbəyi nöqtələri; məntiqi funksiyalardır. |

Prinsiplər: **minimal səlahiyyət (least privilege)** işə lazım olan ən az hüquqdur; **bilmək zərurəti (need-to-know)** hüququ məlumatın məzmununa bağlayır; **vəzifələrin bölgüsü (separation of duties, SoD)** ziddiyyətli səlahiyyətləri ayırır (statik: iki rol eyni şəxsdə olmur; dinamik: eyni əməliyyatda həm hazırlayıb həm təsdiqləyə bilmir); **default deny** açıq icazəsi olmayanı rədd edir; **tam vasitəçilik (complete mediation)** hər sorğunu hər dəfə yoxlayır; **nasazlıqda bağlı qalma (fail-secure)** mexanizm sıradan çıxanda girişi açmır, **fail-safe** isə insan təhlükəsizliyini önə qoyur (yanğında qapı açılır).

## İdentifikasiya, autentifikasiya, avtorizasiya, uçot

- **İdentifikasiya (identification)**: kimlik iddiası. **Autentifikasiya (authentication)**: iddianın yoxlanması. **Avtorizasiya (authorization)**: yoxlanmış subyektin hüququ. **Fəaliyyətin uçotu (accounting)**: qeydlər. Son üç addım **AAA**; **hesabatlılıq (accountability)** hərəkətin kimə aid olduğunu əsaslandırmaqdır.
- **İlkin şəxsiyyət yoxlaması (identity proofing)** hesab açılmazdan əvvəl gəlir. **NIST SP 800-63** (2025) üç təminat səviyyəsi verir: IAL (şəxsiyyət), AAL (autentifikasiya), FAL (federasiya).
- **RADIUS** şəbəkə girişində (Wi-Fi) mərkəzi AAA, **TACACS+** avadanlığın inzibati girişində AAA funksiyalarını ayırır; **Blast-RADIUS** (CVE-2024-3596) RADIUS zəifliyidir. Protokolun adı təhlükəsiz kanal demək deyil.
- **Audit** qeydlərin oxunmasından genişdir: meyarlara qarşı sistemli qiymətləndirmə.

:::exam
Autentifikasiya ≠ avtorizasiya. Düzgün parol və MFA ilə girib başqa fakültənin məlumatını görmək avtorizasiya problemidir. READ/WRITE/EXECUTE giriş əməliyyatlarıdır, autentifikasiya növü deyil.
:::

## Faktorlar, biometrika, FIDO2

| Anlayış | Nədir |
| --- | --- |
| Bildiyin şey | Parol, PIN; oğurlanır, fişinqlə alınır. |
| Sahib olduğun şey | Telefon, smart kart, FIDO2 açarı; kriptoqrafik açar buna aiddir. SMS kodu **SIM-swap** ilə ələ keçir. |
| Özünə məxsus olan | Barmaq izi, üz; dəyişdirilmir. IP, yer, vaxt faktor deyil, risk konteksti. |
| MFA (multi-factor authentication) | Fərqli kateqoriyalardan ən azı iki faktor; parol və gizli sual MFA deyil. |
| Güc sırası | SMS < TOTP < push < FIDO2/passkey. |
| FAR / FRR / CER (EER) | FAR yadın qəbulu (daha təhlükəli), FRR öz adamın rəddi; CER onların bərabər olduğu nöqtə, aşağı olması dəqiqdir. |
| FIDO2: WebAuthn, CTAP, passkey | WebAuthn veb qatı, CTAP xarici autentifikatorla əlaqə, passkey açıq açarlı kimlik məlumatı. Challenge imzalanır, açar domenə bağlıdır, buna görə saxta sayt işləmir. |

Fişinqə davamlı giriş oğurlanmış sessiyanı və zəif hesab bərpasını aradan qaldırmır.

## Parol siyasəti

**NIST SP 800-63B-4** yalnız parolla girişdə minimum 15, MFA tərkibində minimum 8 simvol, 64 simvola qədər qəbul tələb edir; tərkib qaydaları və təqvimlə məcburi dəyişmə yoxdur, sızmış parolların qara siyahısı, uğursuz cəhdin məhdudlaşdırılması, parol meneceri və paste var. Parol **salt** (duz) və yavaş funksiya (**Argon2id**, **bcrypt**; scrypt, PBKDF2) ilə saxlanır; duz sirr deyil və oflayn təxmini tam dayandırmır. **Pepper** bazadan ayrı qorunan əlavə sirrdir.

## DAC, MAC, RBAC, ABAC, qayda əsaslı

| Model | Qərarı kim verir, zəif cəhət |
| --- | --- |
| **DAC** (discretionary) | Sahib verir (fayl icazələri); səhv paylaşma, kopyalama. |
| **MAC** (mandatory) | Mərkəzi siyasət, etiketlər; **SELinux**, **AppArmor**; sərt, idarəsi çətin. |
| **RBAC** (role-based) | İcazə rola, rol istifadəçiyə; **role explosion**. UA, PA çoxun çoxadır, RH rol iyerarxiyası, sessiyada rolların altçoxluğu aktivdir. |
| **ABAC** (attribute-based) | İstifadəçi, resurs, mühit atributları; atributun təzəliyi və mənbəyi vacibdir. |
| **Qayda əsaslı (rule-based access control)** | Hamıya eyni qaydalar (firewall ACL); fərdi istisna çətindir. |

## Formal modellər

| Model | Mahiyyət |
| --- | --- |
| **Bell–LaPadula (BLP)**, 1973 | Məxfilik: no read up (ss), no write down (\*), ds matrisi də yoxlayır. Təhlükəsizlik qəfəsi (security lattice) kateqoriya əlavə edir; gizli kanal (covert channel) qalır. |
| **Biba**, 1977 | Tamlıq, BLP-nin güzgüsü: no read down, no write up. Windows **Mandatory Integrity Control** əlaqəli ideyadır. |
| **Clark–Wilson** | Tamlıq: CDI yalnız TP ilə dəyişir, UDI yoxlanmamış giriş, IVP tamlığı yoxlayır, vəzifələr bölünür. |
| **Brewer–Nash** (Chinese Wall) | Əvvəlki girişdən asılı maraq toqquşması: bir rəqibi açandan sonra digərinə giriş bağlanır. |
| **Harrison–Ruzzo–Ullman (HRU)** | Matrisin dinamik dəyişməsi; safety problem: hüquq icazəsiz subyektə sıza bilərmi? Ümumi halda həllolunmazdır. |

## IAM və federasiya

- **IAM (identity and access management)**: **joiner** (minimum hüquqla hesab), **mover** (köhnə hüquqlar götürülür, yoxsa **privilege creep**), **leaver** (hesab, VPN, kart, sessiya, token bağlanır); **provisioning** hüququn sistemlərə çatdırılmasıdır. **Access review** hüquqları dövri yoxlayır. **Xidmət hesabları** sahibli, məhdud, qısaömürlü sirrlidir.
- **SSO (single sign-on)**: bir giriş, çox xidmət; MFA şərtdir. **IdP (identity provider)** yoxlayır, **SP (service provider)** qəbul edir.
- **LDAP** kataloq protokoludur (TCP 389; **StartTLS** kanalı TLS ilə qoruyur; **LDAPS** 636-da başlanğıcdan TLS işlədir, sertifikat yoxlanmalıdır), **Active Directory** kataloq və domen infrastrukturudur; **LDAP injection** filtr səhvidir.
- **SAML**: XML əsaslı federasiya standartı; IdP imzalı assertion verir, SP onu imza, issuer, audience, vaxt və təkrar istifadə üzrə yoxlayır. İmza məzmunu gizlətmir.
- **Kerberos**: parolu göndərmədən bilet (ticket) ilə autentifikasiya; **KDC** = AS + TGS; AS **TGT** verir, TGS xidmət bileti, sonra xidmətə təqdimat; vaxt sinxronizasiyası vacibdir.
- **OAuth 2.0** avtorizasiyadır (access token, scope, refresh token); **OpenID Connect (OIDC)** autentifikasiyadır (ID token); **PKCE** kodu müştəriyə bağlayır, **state** sorğunu sessiyaya, **nonce** ID token-i sorğuya bağlayır; **JWT** token formatıdır. **Bearer token** oğurlana bilər; müddət bitməsi ləğv deyil.

## PAM, sıfır etimad, hücumlar

- **PAM (privileged access management)**: admin hüququ seyfdə, müvəqqəti (**JIT**), sessiya yazılır; **break-glass account** fövqəladə hesabdır.
- **Sıfır etimad (zero trust)**, NIST SP 800-207: yerləşməyə görə etimad yoxdur; kimlik, cihaz və risk davamlı qiymətləndirilir.
- Hücumlar: **credential stuffing** sızmış cütləri sınayır; **password spraying** az parolu çox hesaba; **pass-the-hash** NT heşini parol əvəzi işlədir (NTLM); **Kerberoasting** SPN biletini oflayn sındırır (**gMSA** müdafiədir); token oğurlanması sessiya ləğvi tələb edir. Cookie-də Secure, HttpOnly, SameSite; XSS və CSRF ayrıca qorunur. Windows hadisələri 4624/4625 giriş, 4768 TGT, 4769 xidmət bileti.

## PDCA, sınaq, audit, koordinasiya, hüquq

- **PDCA** (Plan, Do, Check, Act) giriş siyasətinin idarə dövrüdür; **ISO/IEC 27001** və 27002 çərçivədir.
- **Testbed** təcrid olunmuş sınaq mühiti: müsbət və mənfi sınaq, server səviyyəsində yoxlama.
- Koordinasiya: formal və qeyri-formal; ümumdövlət, korporativ, lokal, obyekt səviyyəsi; **SOC** xəbərdarlığı alır, IAM məhdudlaşdırır.
- Hüquq: 95/46/EC direktivi **GDPR** ilə əvəz olunub; 2002/58/EC elektron rabitə; Avropa Şurasının **ETS** 108, 181 (məlumat), 185 (Budapeşt, kibercinayət), 189 (irqçilik) sənədləri.

## Əsas fərqlər

- Autentifikasiya kimliyi, avtorizasiya icazəni yoxlayır; OAuth 2.0 avtorizasiyadır, OIDC onun üzərində autentifikasiyadır.
- BLP sirrin aşağı axmasını, Biba etibarsız məlumatın yuxarı çirkləndirməsini önləyir; ikisi də giriş matrisindən əlavə qaydadır.
- DAC-da qərarı sahib, MAC-da mərkəzi siyasət, RBAC-da rol, ABAC-da atributlar, qayda əsaslı modeldə sabit qaydalar verir.
- LDAP kataloqdur, SAML federasiya, Kerberos bilet əsaslı autentifikasiyadır; üçü də resursun daxili avtorizasiyasını əvəz etmir.
- İdentifikasiya iddia, autentifikasiya sübut, avtorizasiya hüquq, uçot isə qeyddir; hesabatlılıq bu qeydlərin kimə aid olduğunu göstərməsidir.
- Salt hazır cədvəlləri çətinləşdirir, yavaş funksiya (Argon2id) oflayn təxmini bahalaşdırır.
- Müddət bitməsi ləğv deyil: bağlanmış hesabın token-ləri və sessiyaları ayrıca ləğv edilir.
