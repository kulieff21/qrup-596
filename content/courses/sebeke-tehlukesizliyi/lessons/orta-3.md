+++
title = "Girişə nəzarət prinsipləri və modelləri; identifikasiya və giriş idarəetməsi (IAM)"
unit = "orta"
order = 3
summary = "Hər anlayış izahla: giriş qərarı, AAA, faktorlar və FIDO2, parol saxlanması, DAC/MAC/RBAC/ABAC, BLP, Biba və digər modellər, IAM, SSO, SAML, Kerberos, OAuth/OIDC, PAM, sıfır etimad və kimlik hücumları."
updated = 2026-11-09

[[source]]
title = "Mühazirə 3: Girişə nəzarət prinsipləri və modelləri; identifikasiya və giriş idarəetməsi (IAM)"
note = "Elmar Cabbarov, 2026–2027"
+++

Mövzu dörd sualı cavablandırır: sistemə kim girir, kimliyini necə yoxlayırıq, içəridə nəyə icazəsi var, etdiklərini kim yazır. Universitetin adları və rəqəmləri şərti tədris nümunəsidir.

## Siyasətdən giriş qərarına

Girişə nəzarət (access control) subyektin obyekt üzərində əməliyyat aparmasına icazə verən və ya rədd edən qaydalar və mexanizmlərdir. **Subyekt** sorğunu başladan aktiv tərəfdir (proses, xidmət hesabı, avtomatlaşdırılmış agent), **obyekt** qorunan resursdur (tələbə bazası sətri, LMS kursu, fayl, API), **əməliyyat** oxuma, yazma, silmə, icra, təsdiq, paylaşmadır. "Giriş obyekti" əlçatanlıq (availability) deyil.

| Səviyyə | Mənası | Nümunə |
| --- | --- | --- |
| Siyasət | Universitetin tələbi | Tələbə öz qiymətini görür, dəyişmir |
| Model | Siyasətin dəqiq təsviri; abstrakt, sadə, adekvat olmalıdır | İstifadəçi–kurs–əməliyyat əlaqəsi |
| Mexanizm | Modelin icrası | LMS hər sorğuda yoxlayır |

Modelin sübutu yalnız fərziyyələri daxilində doğrudur: proqram zəifliyi və ya modelə daxil olmayan ehtiyat nüsxə kanalı kənarda qala bilər.

**İstinad monitoru (reference monitor)**, başqa adla giriş dispetçeri, hər sorğunu siyasətə görə yoxlayır. Üç tələb: hər müraciət ondan keçməli (yan keçmək mümkün olmamalı), subyekt onu dəyişdirə bilməməli, yoxlanacaq qədər kiçik olmalıdır. Menyudakı düyməni gizlətmək kifayət deyil; birbaşa API sorğusunda server yenə yoxlamalıdır.

**Giriş matrisi** sətirdə subyekt, sütunda obyekt, xanada hüquq (R, W, X) göstərir. Çox xana boş olduğu üçün iki formada saxlanır: **ACL** (access control list), hər obyektin icazəli subyektləri; **səlahiyyət siyahısı (capability list)**, hər subyektin girə biləcəyi obyektlər (həqiqi capability-də istinad saxtalaşdırılmaqdan qorunur). Atribut əsaslı arxitekturada sorğunu **PEP** (icra nöqtəsi) tutur, **PDP** (qərar nöqtəsi) siyasəti (**PAP**, siyasət idarəsi) və atributları (**PIP**, atribut mənbəyi) əsasında qərar verir. Bunlar məntiqi funksiyalardır.

### Prinsiplər

| Prinsip | Mənası və nümunə |
| --- | --- |
| Minimal səlahiyyət (least privilege) | İşə lazım ən az hüquq, lazım resurs və müddətdə; kitabxanaçı borc qeydini yeniləyir, maliyyə məlumatını ixrac etmir |
| Bilmək zərurəti (need-to-know) | Məlumatın məzmununa bağlıdır; dekan başqa fakültənin tibbi sənədini oxumur |
| Vəzifələrin bölgüsü (separation of duties, SoD) | Statik: iki ziddiyyətli rol eyni şəxsdə olmur. Dinamik: hər ikisi ola bilər, amma eyni əməliyyatda həm hazırlayıb həm təsdiqləyə bilməz |
| Susmaya görə rədd (default deny) | Açıq icazə yoxdursa rədd |
| Tam vasitəçilik (complete mediation) | Hər sorğu hər dəfə yoxlanır, keşdəki köhnə icazəyə güvənilmir |
| Nasazlıqda bağlı qalma (fail-secure) | Qərar mexanizmi işləmirsə giriş açılmır; ehtiyat siyasət xidməti və nəzarətli keş qurula bilər |

**Fail-safe** insan təhlükəsizliyini önə qoyur (yanğında təxliyə qapısı açılır) və rəqəmsal bazanın hamıya açılması demək deyil.

## İdentifikasiya, autentifikasiya, avtorizasiya, uçot

| Mərhələ | Sual | Nümunə |
| --- | --- | --- |
| İdentifikasiya (identification) | Hansı hesabı təqdim edirsən? | aysel@unec.example |
| Autentifikasiya (authentication) | Onu idarə etdiyini necə sübut edirsən? | FIDO2 açarı sorğunu imzalayır |
| Avtorizasiya (authorization) | Nə edə bilərsən? | Yalnız öz kursuna bal yazır |
| Fəaliyyətin uçotu (accounting) | Nə baş verdi? | Kim, hansı balı, nə vaxt dəyişdi |

Son üçü **AAA**dır. **Hesabatlılıq (accountability)** qeydlər və təşkilati məsuliyyətlə hərəkətin kimə aid olduğunu əsaslandırmaqdır; paylaşılan hesab bunu pozur.

:::exam Tələ
Autentifikasiya kimliyi, avtorizasiya icazəni yoxlayır. Düzgün parol və MFA ilə girib başqa fakültənin tələbə işini aça bilən əməkdaşda avtorizasiya pozulub. READ, WRITE, EXECUTE autentifikasiya növləri deyil, giriş əməliyyatlarıdır.
:::

- **İlkin şəxsiyyət yoxlaması (identity proofing)** autentifikatordan əvvəl gəlir; səhv şəxsə bağlanmış hesabı güclü MFA da qorumaz. **NIST SP 800-63** (800-63-4, iyul 2025) üç təminat səviyyəsi verir: **IAL** (şəxsiyyətin ilkin yoxlanması), **AAL** (autentifikasiya), **FAL** (federasiya). Yüksək AAL yüksək IAL demək deyil.
- AAA şəbəkədə: **RADIUS** (yataqxana Wi-Fi) mərkəzi autentifikasiya və uçot, **TACACS+** avadanlığın inzibati girişində üç funksiyanı ayırır. Adın yazılması təhlükəsiz kanal demək deyil. **Blast-RADIUS** (CVE-2024-3596) köhnə fərziyyələrə arxalanmağın riskini göstərir.
- Uçot rolun verilməsini, MFA dəyişməsini, bərpanı və rədd edilmiş ixracı da yazır. **Audit** meyarlara qarşı sistemli qiymətləndirmədir; loqların analizi onun bir hissəsidir.

## Faktorlar, biometrika, FIDO2

| Faktor | Nümunə | Zəiflik |
| --- | --- | --- |
| Bildiyin şey | Parol, PIN | Oğurlanır, fişinqlə alınır |
| Sahib olduğun şey | Telefon, smart kart, FIDO2 açarı | İtir; SMS kodu **SIM-swap** ilə ələ keçir |
| Özünə məxsus olan | Barmaq izi, üz | Dəyişdirilmir |

IP, yer və vaxt faktor deyil, risk kontekstidir. Cihazdakı kriptoqrafik açar sahiblik faktorudur. **MFA (multi-factor authentication)** fərqli kateqoriyalardan ən azı iki faktordur: smart kart və PIN MFA-dır, parol və gizli sual deyil (hər ikisi bilik).

Güc sırası: SMS < **TOTP** (vaxta bağlı birdəfəlik kod; saxta sayta yazıla bilir) < push (rəqəm uyğunlaşdırması ilə; bildiriş yorğunluğu riski) < FIDO2/passkey. Üsul pilləsinə yox, konkret hücumda nəyin qorunduğuna baxılır.

**Biometrika** oxşarlıq həddi ilə işləyir. **FAR** yadın qəbulu (II tip, daha təhlükəli), **FRR** öz adamın rəddi (I tip); hədd sərtləşəndə FAR azalır, FRR artır; bərabərləşmə nöqtəsi **CER (EER)** sistemləri müqayisə üçündür, aşağı olması dəqiqliyi göstərir. Biometrika NIST-də fiziki autentifikatorun aktivləşdirilməsi üçündür (telefonda barmaq izi passkey açarını açır, serverə göndərilmir). Alternativ yol qurulmalıdır, sensor işləməyəndə yardım masası şəxsiyyəti yoxlamadan hesab açmamalıdır.

**FIDO2** veb autentifikasiyası üçün **WebAuthn** və xarici autentifikatorlarla əlaqə üçün **CTAP** texnologiyalarını birləşdirir; **passkey** parolsuz girişdə işlənən açıq açarlı kimlik məlumatıdır.

1. Qeydiyyatda açar cütü yaranır; server açıq açarı saxlayır, şəxsi açar autentifikatorda qalır.
2. Girişdə server təsadüfi sorğu dəyəri (challenge) göndərir.
3. Autentifikator istifadəçi iştirakını (PIN/biometrika) yoxlayıb domenlə bağlı məlumatı və sorğunu imzalayır.
4. Server imzanı açıq açarla, təzəliyi və mənşəni yoxlayır.

Saxta domen həqiqi xidmət üçün imza ala bilmir: fişinqə davamlılıq **domen bağlanmasından** gəlir. Sinxronlaşdırılan passkey çox cihazda, cihazla məhdud açar bir autentifikatorda işləyir. Fişinqə davamlı giriş oğurlanmış sessiyanı, yoluxmuş cihazı və zəif hesab bərpasını aradan qaldırmır.

## Parol siyasəti və saxlanması

| Məsələ | Köhnə | NIST SP 800-63B-4 (2025) |
| --- | --- | --- |
| Uzunluq | min. 8 | Yalnız parolla girişdə min. 15; MFA tərkibində min. 8; 64 simvola qədər qəbul |
| Tərkib | Böyük hərf, rəqəm, simvol | Tələb edilmir ("Parol1!" kimi proqnozlaşdırıla bilən olur) |
| Dəyişmə | Hər 30–90 gün | Yalnız sızma sübutu olanda |
| Əlavə | — | Sızmış parol qara siyahısı, cəhd limiti, parol meneceri, paste |

Hesabın sərt kilidlənməsi hücumçuya tələbələri bloklamaq imkanı verə bilər, yataqxananın ortaq IP-si yalnız IP-yə görə bloklamanı riskli edir; artan gecikmə və təhlükəsiz bərpa seçilir. CAPTCHA köməkçidir.

Server parolu geri açılan şifrələmə ilə yox, törətmə funksiyası ilə saxlayır: hər parola təsadüfi **duz (salt)** verilir, funksiya parol, duz və xərc parametrlərindən nəticə yaradır, girişdə eyni hesablama müqayisə edilir. Duz sirr deyil; eyni parolların nəticəsini fərqləndirir və hazır cədvəlləri çətinləşdirir, lakin bazanı oğurlayanın oflayn təxminini dayandırmır, zəif parolu gücləndirmir. Xərci **Argon2id** kimi yavaş, yaddaş tələb edən funksiya artırır; adi SHA-256 sürətli olduğu üçün yaramır; **bcrypt**-in geniş reallaşdırmalarında 72 bayt limiti var. **Pepper** bazadan ayrı saxlanan əlavə sirrdir; itirilməsi üçün plan lazımdır. Ehtiyat nüsxələrdəki köhnə heşlər də qorunmalıdır.

## DAC, MAC, RBAC, ABAC, qayda əsaslı

| Model | Qərarın əsası | Nümunə | Uğursuzluq |
| --- | --- | --- | --- |
| **DAC** (discretionary access control) | Sahib hüquq verir | Fayl icazələri (Linux r/w/x, ACL), Drive "paylaş" | Səhv paylaşma; oxuyan kopyalayıb ötürür |
| **MAC** (mandatory access control) | Mərkəzi məcburi siyasət, etiket | **SELinux**, **AppArmor**, hərbi sistemlər | Yanlış etiket, sərt istisna |
| **RBAC** (role-based access control) | İş funksiyasının rolu | AD qrupları, ERP | **Role explosion**, hüquq yığılması |
| **ABAC** (attribute-based access control) | İstifadəçi, resurs, mühit atributları | Bulud IAM, Zero Trust | Köhnə və ya saxta atribut |
| Qayda əsaslı (rule-based access control) | Əvvəlcədən yazılmış şərtlər | Firewall ACL, iş saatından kənar giriş qadağası | Geniş istisna, səhv sıra |

- DAC-da qovluqda r siyahılama, x keçid, w qeyd dəyişməsidir; fayl silmək qovluq hüququndan asılıdır. MAC-da klassik halda subyektin buraxılış dərəcəsi obyektin etiketi ilə müqayisə olunur; SELinux tip, AppArmor tətbiq profili ilə işləyir. DAC və MAC birlikdə işləyir: birinin icazəsi digərinin qadağasını aradan qaldırmır.
- RBAC-da U, R, P, SE istifadəçi, rol, icazə və sessiya çoxluqlarıdır; **UA** (istifadəçi–rol) və **PA** (rol–icazə) çoxun çoxadır; **RH** rol iyerarxiyasıdır; sessiyada təyin olunmuş rolların altçoxluğu aktivləşir (minimal səlahiyyət). İyerarxiyada miras məcburi deyil.
- ABAC-da atributların mənbəyi etibarlı olmalıdır (cihaz "managed=true" istifadəçi sahəsindən götürülmür) və təzə olmalıdır; çatışmayan atribut icazə vermir.

:::example RBAC və ABAC
"Müəllim yalnız öz qruplarının qiymətini, yalnız imtahan sessiyasında və idarə olunan kompüterdən dəyişə bilər." RBAC yalnız "müəllim" rolunu verir; ABAC bütün şərtləri bir siyasətdə yazır: vəzifə ∧ qrup ∧ tarix ∧ cihaz.
:::

## Formal modellər

**Bell–LaPadula (BLP)** məxfiliyi qoruyur (ilk təqdimat 1973, yekun 1975). Səviyyələr Açıq < Məxfi < Çox məxfi. **Sadə təhlükəsizlik (ss)** qaydası: no read up. **Ulduz (\*)** qaydası: no write down (sirr aşağı fayla köçürülməsin). **Diskresion (ds)** qayda: giriş matrisi də icazə verməlidir. **Təhlükəsizlik qəfəsi (security lattice)** səviyyəyə kateqoriyalar əlavə edir (bilməyin zərurəti). Səviyyənin endirilməsi yalnız səlahiyyətli prosedurla olur. **Gizli kanal (covert channel)** (məsələn cavab vaxtı ilə bit ötürmə) və etibarlı komponentin kompromitasiyası modeldən kənardadır: BLP virusdan qorumur.

**Biba** (1977) tamlığı qoruyur: aşağı etibarlı mənbə yüksək etibarlı məlumatı pozmasın. Sərt variant: no read down, no write up. Biba məxfilik modeli deyil, BLP-nin güzgüsüdür. Windows **Mandatory Integrity Control** (brauzer aşağı tamlıqda işləyir, sistem fayllarına yaza bilmir) əlaqəli ideyadır, Biba-nın tam reallaşması deyil. Real sistemdə yoxlama və təsdiq edən etibarlı çevirmə aşağı məlumatı yuxarı daşıyır.

:::figure
src = "m03-2.png"
alt = "Solda Bell–LaPadula: məxfi subyekt aşağıdan oxuyur, yuxarıya yazır; sağda sərt Biba: orta tamlıqlı subyekt yuxarıdan oxuyur, aşağıya yazır."
caption = "BLP və sərt Biba orta səviyyəli subyekt üçün."
:::

| Orta səviyyəli subyektin əməliyyatı | BLP | Sərt Biba |
| --- | --- | --- |
| Yuxarını oxumaq | Qadağan | Mümkün |
| Aşağını oxumaq | Mümkün | Qadağan |
| Yuxarıya yazmaq | Mümkün | Qadağan |
| Aşağıya yazmaq | Qadağan | Mümkün |

- **Clark–Wilson** (kommersiya, tamlıq, bank məntiqi): **CDI** (constrained data items), rəsmi bal, yalnız təsdiqlənmiş **TP** (transformation procedures) ilə dəyişir; **UDI** yoxlanmamış giriş (tələbənin ərizəsi); **IVP** (integrity verification procedure) uyğunluğu yoxlayır; vəzifələr bölünür, hər əməliyyat audit olunur. Bazaya birbaşa UPDATE hüququ bu qoruyucuları keçər.
- **Brewer–Nash** (Çin səddi, Chinese Wall): məlumat şirkətlərə, rəqibləri isə maraq toqquşması siniflərinə bölünür; bir şirkətin sirrini açandan sonra eyni sinifdəki rəqibə giriş bağlanır (icazə keçmişdən asılıdır). Yazma qaydaları dolayı ötürməni də məhdudlaşdırır. Tender komissiyası kimi bütün təklifləri müqayisə etməli prosesə tətbiq edilmir.
- **Harrison–Ruzzo–Ullman (HRU)** (1976): matrisin dinamik dəyişməsi; **safety problem**: hüquq əvvəl olmadığı xanaya sıza bilərmi? Ümumi halda həllolunmazdır, lakin məhdud qaydalarla konkret yoxlama mümkündür.

## IAM həyat dövrü

**IAM (identity and access management)** hesabları, autentifikatorları və hüquqları təşkilati hadisələrlə əlaqələndirir; mənbə kadr və ya qeydiyyat sistemidir.

- **Joiner**: şəxs yoxlanır, sabit identifikator yaranır, rol təsdiqlənir, minimum hüquq verilir. Hüququn bütün sistemlərə çatdırılması (**provisioning**) ayrıca yoxlanır.
- **Mover**: köhnə hüquqlar götürülür; unudulsa **privilege creep** (hüquq yığılması) yaranır. Keçid istisnasının sahibi və bitmə vaxtı yazılır.
- **Leaver**: hesab, VPN, kart, aktiv sessiyalar, refresh token-lər və API açarları bağlanır; hesabın silinməsi ilk addım olmaya bilər (sənəd sahibliyi, audit).

**Access review** hüquqların dövri yoxlanmasıdır: resurs sahibi hüququ iş ehtiyacı ilə müqayisə edir; birbaşa təyinatlar, iç-içə qruplar və rol iyerarxiyası əhatə olunur. Şərti tezlik: imtiyazlı hüquqlar hər ay, digərləri hər semestr. Hesablama: 120 təyinatdan 18-i ləğv olunmalı, 12-si icra edilibsə, tamamlanma 12/18 ≈ 66,7 %. Təsdiq düyməsi faktiki silinmənin sübutu deyil. **Xidmət hesabları** sahibli, məhdud, mümkünsə qısaömürlü sirrlidir; sirr kod deposunda saxlanmır, sahib çıxanda sahiblik ötürülür.

## SSO, LDAP, SAML, Kerberos

**SSO (single sign-on)** bir autentifikasiyadan sonra bir neçə xidmətə keçməkdir; hesab oğurlansa hamısı açılır, ona görə MFA mütləqdir. Federasiyada **IdP (identity provider)** istifadəçini yoxlayır, **SP (service provider)** nəticəni qəbul edir; IdP kimliyi təsdiqləsə də yerli avtorizasiya SP-nin işidir. IdP-də çıxış tətbiq sessiyasını həmişə bağlamır.

**LDAP** kataloq (istifadəçi, qrup) protokoludur, SSO/federasiya deyil; TCP 389 (**StartTLS** ilə qorunur), **LDAPS** adətən 636-da başlanğıcdan TLS işlədir (sertifikat və server adı yoxlanmalıdır). **Active Directory** LDAP, Kerberos və başqa xidmətləri birləşdirən kataloq və domen infrastrukturudur. İstifadəçi girişini filtrə birbaşa qoşmaq **LDAP injection** yaradır.

**SAML 2.0** XML əsaslı federasiya standartıdır: LMS (SP) istifadəçini IdP-yə yönəldir, IdP imzalı təsdiq (assertion) yaradır, brauzer onu LMS-in qəbul ünvanına çatdırır, LMS imza, issuer, audience, destination, recipient, vaxt və təkrar istifadəni yoxlayıb sessiya açır. İmza bütövlüyü yoxlayır, məzmunu gizlətmir.

**Kerberos** parolu göndərmədən **bilet (ticket)** ilə autentifikasiya edir. **KDC (key distribution center)** iki hissədən ibarətdir: **AS** və **TGS**; realm idarəetmə sahəsi, principal istifadəçi və ya xidmət kimliyidir.

1. AS-REQ: müştəri ilkin yoxlama ilə bilet istəyir.
2. AS-REP: **TGT** gəlir (TGS açarı ilə qorunur, müştəri içini görmür).
3. TGS-REQ: TGT, xidmət adı və autentifikator göndərilir.
4. TGS-REP: xidmət bileti və sessiya açarı.
5. AP-REQ: bilet və təzə autentifikator xidmətə verilir.
6. AP-REP: qarşılıqlı autentifikasiya.

:::figure
src = "m03-4.png"
alt = "Kerberos ardıcıllığı: AS-REQ, AS-REP (TGT), TGS-REQ, TGS-REP (xidmət bileti), AP-REQ, AP-REP."
caption = "Kerberos bilet ardıcıllığı."
:::

TGT hər xidmətə hüquq vermir, ACL ayrıca tətbiq olunur. Saatlar uyğun olmalıdır (təzəlik və replay üçün). kdestroy yalnız lokal biletləri silir. KDC kompromitasiyası realm üçün ağırdır; zəif xidmət sirri biletdə oflayn təxmin hədəfidir.

## OAuth 2.0, OIDC, token-lər

**OAuth 2.0** avtorizasiya çərçivəsidir: tətbiq parolu almadan məhdud giriş səlahiyyəti alır. **Access token** resurs serverinə verilir (JWT və ya qeyri-şəffaf), **scope** sərhədi bildirir, server obyektin həmin istifadəçiyə aid olduğunu yenə yoxlayır. **OpenID Connect (OIDC)** OAuth üzərində autentifikasiya qatıdır: **ID token** müştəriyə, access token resurs serverinə aiddir; birini digərinin yerinə qəbul etmək etimad sərhədini pozur. **JWT** üç hissəni açıb oxumaqla yoxlanmır: imza, issuer, audience, vaxt yoxlanır. SAML XML/korporativ, OIDC JSON/JWT və müasir veb-mobil üçündür.

Avtorizasiya kodu axınında (mobil tətbiq) **PKCE** başlanğıcdakı `code_verifier`/`code_challenge` ilə kodu müştəriyə bağlayır (tutulmaya qarşı); **state** cavabı sessiyaya bağlayıb saxtalaşdırmanı azaldır; **nonce** ID token-i autentifikasiya sorğusuna bağlayır. `redirect_uri` dəqiq uyğunlaşdırılır; geniş şablon kodu başqa ünvana aparar. Sonda server access token, OIDC-də ID token, imkan varsa refresh token verir; API token-i audience, issuer, müddət və scope üzrə yoxlayır.

**Bearer token** təqdim edəndə işləyir, surəti oğurlana bilər; TLS yoluxmuş cihazı dayandırmır. Refresh token məhdud saxlanır, rotasiya olunur. Cookie üçün Secure, HttpOnly, SameSite seçilir; HttpOnly XSS-in sorğu aparmasını dayandırmır, **CSRF** ayrıca qorunur. Token URL-yə və loqa yazılmır. Müddət bitməsi ləğv deyil: imzası düzgün JWT-ni lokal yoxlayan API bağlanmış hesabı bilməyə bilər. Qısa müddət, introspeksiya və ya ləğv yayılması seçilir. **RFC 9700** OAuth üçün yaxşı təcrübələri toplayır.

| Mexanizm | Məqsəd | Artefakt |
| --- | --- | --- |
| LDAP | Kataloq | Qeyd, bind |
| Kerberos | Bilet autentifikasiyası | TGT, xidmət bileti |
| SAML | Federativ kimlik | XML assertion |
| OAuth 2.0 | Girişin delegasiyası | Access token |
| OIDC | OAuth üstündə autentifikasiya | ID token |

## PAM və sıfır etimad

**PAM (privileged access management)** yüksək təsirli hüquqları idarə edir: admin və adi hesab ayrılır, daimi üzvlük əvəzinə ehtiyac anında məhdud müddətə (**JIT**, just-in-time) giriş verilir, sessiya yazılır, hüquq vaxtında götürülür (şərti nümunə: sifariş, təsdiq, 30 dəqiqəlik giriş). Sirr seyfi PAM-ın yalnız hissəsidir; PAM özü yüksək dəyərli hədəfdir. **Break-glass account** əsas federasiya çöküşündə fövqəladə hesabdır: ayrıca qorunur, istifadəsi dərhal xəbərdarlıq yaradır, sınanır.

**Sıfır etimad (zero trust)** şəbəkə yerləşməsinə görə etimad vermir; **NIST SP 800-207** arxitekturanı təsvir edir. Qərar kimlik, cihaz vəziyyəti, resurs həssaslığı və risklə verilir. VPN bütün daxili resurslara səlahiyyət yaratmır; seqmentasiya və xidmət səviyyəsində avtorizasiya birlikdə işləyir. Davamlı qiymətləndirmə seçilmiş hadisələrdə cihaz və sessiyanı yenidən yoxlayır.

## Kimliyə qarşı hücumlar

| Hücum | Mahiyyət | Tədbir |
| --- | --- | --- |
| **Credential stuffing** | Sızmış cütlərin kütləvi sınanması (parol təkrarı) | MFA, limit, sızmış parol yoxlaması |
| **Password spraying** | Az parol, çox hesab | Hesablararası korrelyasiya |
| **Pass-the-hash** | NTLM-də parol əvəzinə NT heşi | İmtiyazları ayırmaq, NTLM-i azaltmaq, sirrin mənbəyini təmizləmək |
| **Kerberoasting** | SPN üçün xidmət bileti alıb oflayn təxmin | Uzun sirr, **gMSA**, az imtiyaz |
| Token oğurlanması | Parolsuz hazır sessiya | Token və sessiya ləğvi, cihaz araşdırması |

Bir IP-dən çox hesaba cəhd hücum ola bilər, yataqxananın ortaq NAT-ı da belə görünür; kontekst birlikdə baxılır. Windows hadisələri: 4624/4625 giriş, 4768 TGT, 4769 xidmət bileti (tək 4769 sübut deyil). Loqda autentifikasiya uğuru ilə avtorizasiya rəddi ayrı sahələrdir, uzaq qorunan mənbəyə göndərilir, saatlar sinxronlaşdırılır.

## PDCA, sınaq, audit, koordinasiya, hüquq

- **PDCA**: Plan (risk və siyasət), Do (MFA, rol, API yoxlaması), Check (icazəli və qadağan sorğuların sınağı), Act (artıq hüququn düzəldilməsi). **ISO/IEC 27001** tələbləri, **ISO/IEC 27002** (93 tədbir) tədbirləri verir. Şərti hədəf: ayrılan əməkdaşın girişi 15 dəqiqəyə bağlanır; ölçmə kadr hadisəsindən başlayır, orta göstərici ən uzun gecikməni gizlədir.
- **Testbed** təcrid olunmuş sınaq mühitidir (formal model deyil): saxta məlumat, test hesabı. Müsbət sınaq icazənin işlədiyini, mənfi sınaq qadağanın işlədiyini göstərir; sərhəd sınağı rol ləğvindən sonrakı sessiyanı yoxlayır; gözlənilən nəticə əvvəl yazılır. **Audit** təkrarlana bilən sübutdur.
- Koordinasiyada agent təhlükəsizlik domeninin xidmətidir. Formal koordinasiya qayda və hadisə formatı, qeyri-formal şəxsi əlaqələrlədir. Dörd səviyyə: ümumdövlət, korporativ, lokal, obyekt. **SOC** xəbərdarlığı alır, IAM sessiyaları məhdudlaşdırır, LMS sahibi qiymət dəyişikliyini yoxlayır.
- Hüquqi çərçivə: 95/46/EC direktivi 25 may 2018-dən **GDPR** ((EU) 2016/679) ilə əvəz olunub; 2002/58/EC elektron rabitədir; Avropa Şurasının **ETS** 108 və 181 fərdi məlumatlar, 185 (Budapeşt) kibercinayətkarlıq, 189 irqçi və ksenofob əməllər üçündür.

:::reveal Hesab mərkəzi kataloqda bağlanıb, amma LMS sessiyası açıqdır. Nə səhvdir?
Mərkəzi bloklama ilə tətbiq sessiyasının ləğvi ayrılıb. LMS sessiyası dayandırılır, token müddəti və ləğv siqnalı yoxlanır, digər sistemlərdə qalıq giriş axtarılır. Leaver tamamlanması kataloq cavabı ilə yox, hədəf tətbiqdə girişin faktiki rəddi ilə ölçülür.
:::

:::reveal Məxfi səviyyəli müəllim çox məxfi sənədi oxumaq və açıq portala yazmaq istəyir. BLP və Biba?
BLP hər ikisini rədd edir (no read up, no write down). Eyni səviyyələr tamlıq olsaydı, sərt Biba yuxarıdan oxumağa və aşağıya yazmağa mane olmazdı; Biba sirri yox, etibarlı məlumatı qoruyur. Əlavə ACL və kateqoriya şərtləri ayrıca ödənməlidir.
:::
