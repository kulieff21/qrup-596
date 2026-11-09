+++
title = "Girişə nəzarət prinsipləri və modelləri; identifikasiya və giriş idarəetməsi (IAM)"
unit = "suallar"
order = 3
summary = "Mühazirənin bütün nəzarət sualları və situasiya tapşırıqları cavablarla, konspektdəki üç situasiya və ehtimal olunan əlavə suallar."
updated = 2026-11-09

[[source]]
title = "Mühazirə 3: Girişə nəzarət prinsipləri və modelləri; identifikasiya və giriş idarəetməsi (IAM)"
note = "Elmar Cabbarov, 2026–2027"

[[source]]
title = "Midterm konspekti, Mövzu 3"
note = "Elmar Cabbarov"
+++

Əvvəl sualı öz sözlərinlə cavablandır, sonra cavaba bax. Situasiya suallarında ardıcıllıq: aktiv, pozulan xassə, səbəb, tədbir, yoxlama.

## Nəzarət sualları

:::reveal Təhlükəsizlik siyasəti, model və mexanizm arasında hansı fərq var?
- **Siyasət** universitetin məzmunlu tələbidir: tələbə öz qiymətini görə bilər, dəyişə bilməz.
- **Model** bu tələbin dəqiq, təhlilə yararlı təsviridir: istifadəçi, kurs və əməliyyat arasındakı əlaqə. Abstrakt, sadə və adekvat olmalıdır.
- **Mexanizm** modeli proqramda və sistemdə icra edir: LMS hər sorğuda həmin əlaqəni yoxlayır.
- Firewall-un bağlantını buraxması LMS daxilindəki qiymət sətrinə icazə demək deyil.
:::

:::reveal Giriş subyekti, obyekti və əməliyyatı LMS nümunəsində necə ayrılır?
- **Subyekt**: sorğunu başladan aktiv tərəf (tələbə və ya müəllim adından işləyən proses, xidmət hesabı, agent).
- **Obyekt**: qorunan resurs (qiymət jurnalı sətri, LMS kursu, fayl, API funksiyası, printer).
- **Əməliyyat**: oxuma, yazma, silmə, icra, təsdiq, paylaşma (məsələn, müəllim öz kursunun jurnalına bal yazır).
- Giriş obyekti əlçatanlıq (availability) ilə qarışdırılmamalıdır.
:::

:::reveal İstinad monitoruna qoyulan üç tələb hansı səhvlərin qarşısını alır?
- **Hər müraciət ondan keçməlidir**: yan keçmə (məsələn, menyu düyməsini gizlədib birbaşa API sorğusunu yoxlamamaq) bağlanır.
- **Subyekt onu dəyişdirə bilməməlidir**: saxtalaşdırma və zəiflədilmə qarşısı alınır.
- **Yoxlanacaq qədər sadə (kiçik) olmalıdır**: düzgünlüyü təhlil etmək mümkün olur.
- Düzgün oxunuş: dispetçeri yan keçmək qeyri-mümkün olmalıdır.
:::

:::reveal İdentifikasiya, autentifikasiya, avtorizasiya və uçotun nəticələri nədir?
- İdentifikasiya: subyekt hansı hesabı təqdim etdiyini bildirir.
- Autentifikasiya: həmin hesabı idarə etdiyi autentifikatorla sübut olunur.
- Avtorizasiya: yoxlanmış subyektin konkret əməliyyata hüququ müəyyən edilir.
- Uçot: kim, nəyi, nə vaxt etdi və nəticə nə oldu qeyd olunur; son üçü AAA, qeydlərin hərəkəti kimə aid etməsi isə hesabatlılıqdır.
- Paylaşılan hesab, oğurlanmış sessiya və açıq terminal hesab–insan əlaqəsini zəiflədir.
:::

:::reveal İki addımlı giriş hansı halda MFA sayılmır?
- MFA fərqli kateqoriyalardan ən azı iki faktor tələb edir (bildiyin, sahib olduğun, özünə məxsus).
- İki addım eyni kateqoriyadadırsa MFA deyil: parol və gizli sual hər ikisi "bildiyin şey"dir.
- Smart kart və PIN (sahiblik və bilik) MFA-dır.
- IP, yer, vaxt faktor deyil, risk kontekstidir; yalnız seriya nömrəsi oxudan kart kriptoqrafik smart kart sayılmır.
:::

:::reveal FIDO2-nin fişinqə davamlılığı hansı domen əlaqəsindən yaranır?
- Qeydiyyatda xidmət üçün açar cütü yaranır; şəxsi açar autentifikatorda qalır.
- Giriş zamanı xidmət challenge göndərir, autentifikator domenlə əlaqəli məlumatı və sorğunu imzalayır.
- Server imzanı açıq açarla, challenge-in təzəliyini və mənşəni yoxlayır.
- Saxta domen həqiqi xidmət üçün imza ala bilmir: davamlılıq **domen bağlanmasından** gəlir.
- Oğurlanmış sessiyanı və zəif hesab bərpasını aradan qaldırmır.
:::

:::reveal FAR, FRR və EER hansı fərqli halları ölçür?
- **FAR** (II tip): aid olmayan şəxsin səhvən qəbulu, təhlükəsizlik üçün daha təhlükəlidir.
- **FRR** (I tip): icazəli şəxsin səhvən rəddi, istifadəçini əsəbiləşdirir.
- Hədd sərtləşdikcə FAR azalır, FRR artır.
- **EER (CER)**: FAR = FRR nöqtəsi; sistemləri müqayisə üçündür, nə qədər aşağıdırsa, o qədər dəqiqdir. Real yerləşdirmədə istifadəçi qrupu və saxta nümunənin aşkarlanması da yoxlanır.
:::

:::reveal NIST SP 800-63B-4 parol uzunluğu və dəyişməsi barədə nə tələb edir?
- Yalnız parolla girişdə minimum 15 simvol; MFA tərkibində minimum 8; ən azı 64 simvolluq parolların qəbulu tövsiyə olunur.
- Tərkib qaydaları (böyük hərf, rəqəm, simvol) tələb edilmir.
- Təqvimə görə məcburi dəyişmə yoxdur, yalnız sızma sübutu olanda dəyişdirilir.
- Sızmış və tez işlənən parol siyahısı, uğursuz cəhdlərin məhdudlaşdırılması, parol meneceri və paste dəstəyi.
:::

:::reveal Salt oflayn parol təxminini niyə tam dayandırmır?
- Duz sirr deyil, bazada heşlə saxlanır.
- Hər parol üçün ayrıdır: eyni parolların nəticəsini fərqləndirir və hazır cədvəlləri çətinləşdirir.
- Bazanı oğurlayan hücumçu hər hesab üçün təxminləri yenə sınaya bilər; zəif parolu duz gücləndirmir.
- Xərci yavaş, yaddaş tələb edən funksiya (Argon2id) artırır; SHA-256 sürətli olduğu üçün yaramır.
:::

:::reveal DAC ilə MAC-ın birlikdə tətbiqində sahibin icazəsi niyə kifayət etmir?
- DAC-da sahib hüquq verir (ACL, fayl icazələri).
- MAC-da mərkəzi siyasət və etiket qaydası da ödənməlidir; resurs sahibi onu zəiflədə bilmir.
- Birinin icazəsi digərinin qadağasını aradan qaldırmır: sahib hamıya açsa da, MAC siyasəti aşağı səviyyəyə açmanı rədd edə bilər.
- MAC-ın zəif cəhəti etiketləmə və istisnalardır; yanlış etiket yanlış girişə səbəb olur.
:::

:::reveal RBAC-da UA, PA və RH nəyi bildirir, sessiyada hansı rollar aktiv ola bilər?
- **UA**: istifadəçi–rol təyinatı; **PA**: rol–icazə təyinatı; ikisi də çoxun çoxadır. **RH**: rol iyerarxiyası. U, R, P, SE istifadəçi, rol, icazə, sessiya çoxluqlarıdır.
- Sessiyada istifadəçi ona təyin edilmiş rolların yalnız uyğun altçoxluğunu aktivləşdirir.
- Bütün rolları avtomatik birləşdirmək minimal səlahiyyətə uyğun olmaya bilər (Nigar nümunəsi: tədqiqat sessiyasında katib hüququ aktiv deyil).
- İyerarxiyada miras məcburi deyil.
:::

:::reveal ABAC atributunun mənbəyi və təzəliyi qərarın doğruluğuna necə təsir edir?
- Qərar subyekt, obyekt, əməliyyat və mühit atributlarından hesablanır; atribut yanlışdırsa, qərar yanlışdır.
- Mənbə etibarlı olmalıdır: cihaz vəziyyəti istifadəçinin göndərdiyi sərbəst sahədən götürülsə, hücumçu managed=true yazar.
- Təzəlik: işdən çıxan əməkdaş gecə yenilənən kataloqda gün ərzində aktiv görünə bilər; hüquq dəyişməsi siqnalı, keş müddəti və ziddiyyətin həlli əvvəlcədən müəyyən edilir.
- Çatışmayan atribut icazə vermir.
:::

:::reveal Bell–LaPadula ilə sərt Biba-nın oxuma və yazma qaydaları necə fərqlənir?
- **BLP** (məxfilik): no read up, no write down (+ ds matris).
- **Sərt Biba** (tamlıq): no read down, no write up.
- Orta səviyyəli subyekt üçün: yuxarını oxumaq BLP-də qadağan, Biba-da mümkün; aşağını oxumaq BLP-də mümkün, Biba-da qadağan; yuxarıya yazmaq BLP-də mümkün, Biba-da qadağan; aşağıya yazmaq BLP-də qadağan, Biba-da mümkün.
- Biba BLP-nin güzgü əksidir; eyni səviyyədə digər icazələr varsa hər ikisi icazə verir.
:::

:::reveal Clark–Wilson modeli rəsmi məlumatın birbaşa dəyişdirilməsini niyə məhdudlaşdırır?
- Tamlığı düzgün əməliyyatlarla qoruyur: **CDI** yalnız təsdiqlənmiş **TP** ilə dəyişir; **UDI** yoxlanmamış girişdir; **IVP** uyğunluğu yoxlayır.
- Birbaşa dəyişmə TP-nin yoxlamalarını (interval, kurs, əsas, təsdiq) keçər; bazaya birbaşa UPDATE hüququ qoruyucunu pozur.
- Vəzifələr bölünür, hər əməliyyat audit olunur; yarımçıq tranzaksiya biznes tamlığı pozuntusudur.
:::

:::reveal Brewer–Nash modelində əvvəlki giriş sonrakı hüquqa necə təsir edir?
- Məlumat şirkətlərə, rəqiblər maraq toqquşması siniflərinə bölünür.
- Şəxs bir şirkətin məxfi məlumatını açandan sonra eyni sinifdəki rəqibin məlumatına giriş bağlanır; fərqli sinif açıq qala bilər.
- İcazə keçmiş hərəkətlərdən asılıdır (dinamik); yazma qaydaları dolayı ötürməni də bağlayır.
- Tarixçənin silinməsi və ikinci hesab modeli pozur.
:::

:::reveal HRU modelinin safety problemi nədir?
- HRU giriş matrisinin dinamik dəyişməsini (subyekt/obyekt yaratma, hüquq əlavə etmə və silmə əmrləri) təsvir edir.
- Safety sualı: başlanğıc vəziyyətdən əmrlər ardıcıllığı ilə hüquq əvvəl olmadığı xanaya, yəni icazəsiz subyektə sıza bilərmi?
- Ümumi HRU sistemləri üçün həllolunmazdır; məhdud qaydalar və konkret vəziyyət təhlili ilə yoxlanılan sərhəd qurulur.
:::

:::reveal Mover və leaver mərhələlərində hansı qalıq hüquqlar yoxlanmalıdır?
- **Mover**: köhnə vəzifənin hüquqları (məsələn, laborantın inventar admin hüququ); birbaşa və miras hüquqların fərqi; unudulsa privilege creep.
- **Leaver**: hesab, VPN, fiziki kart, aktiv sessiyalar, refresh token-lər, API açarları, üçüncü tərəf xidmətləri; lokal tətbiq kataloqla gec sinxronlaşa bilər.
- Yoxlama: hədəf sistemdə giriş sınağının rədd edilməsi.
:::

:::reveal LDAP, SAML və Kerberos hansı müxtəlif funksiyaları yerinə yetirir?
- **LDAP**: kataloq (istifadəçi, qrup) sorğusu və idarəsi; 389 (StartTLS), LDAPS 636.
- **SAML 2.0**: XML əsaslı federativ kimlik təsdiqi; IdP imzalı assertion verir, SP yoxlayır.
- **Kerberos**: bilet əsaslı autentifikasiya (TGT, xidmət bileti).
- Üçü də resursun yerli avtorizasiyasını əvəz etmir; LDAP özü SSO/federasiya protokolu deyil.
:::

:::reveal Kerberos-da TGT, xidmət bileti və autentifikatorun vəzifələri nədir?
- **TGT**: AS-REP ilə gəlir, TGS-dən xidmət bileti almaq üçündür; TGS açarı ilə qorunur.
- **Xidmət bileti**: TGS-REP ilə gəlir, xidmətin açarı ilə qorunur, xidmətə təqdim olunur.
- **Autentifikator**: sessiya açarı ilə hazırlanan təzə məlumat; təzəlik və təkrar təqdimetmə yoxlaması üçündür.
- Ardıcıllıq: AS-REQ, AS-REP, TGS-REQ, TGS-REP, AP-REQ, AP-REP. Hüquqları ayrıca ACL müəyyən edir.
:::

:::reveal OAuth access token-i ilə OIDC ID token-in auditoriyası necə fərqlənir?
- **Access token** resurs serveri (API) üçündür: scope çərçivəsində məhdud giriş.
- **ID token** müştəri tətbiqi üçündür: autentifikasiya iddiaları.
- Birini digərinin yerinə qəbul etmək etimad sərhədini pozur.
- JWT-nin yoxlanması: imza, issuer, audience, vaxt; sonra obyekt səviyyəsində icazə.
:::

:::reveal PKCE, state və nonce hansı ayrı əlaqələri yoxlayır?
- **PKCE** (code_verifier/code_challenge): avtorizasiya kodunu müştərinin başlanğıcdakı sirrinə bağlayır, kodun tutulmasına qarşıdır.
- **state**: cavabı sessiyaya bağlayır, sorğunun saxtalaşdırılmasını azaldır.
- **nonce**: autentifikasiya sorğusu ilə ID token arasındakı əlaqəni yoxlayır.
- Üçü ayrı funksiyadır; redirect_uri dəqiq uyğunlaşdırılmalıdır.
:::

:::reveal PAM və sıfır etimad minimal səlahiyyəti necə tətbiq edir?
- **PAM**: admin və adi hesab ayrılır; daimi üzvlük əvəzinə JIT, məhdud müddət və əhatə; sessiya yazılır, müddət bitəndə hüquq götürülür; break-glass hesabı ayrıca qorunur.
- **Sıfır etimad**: şəbəkə yerləşməsinə görə etimad yoxdur; qərar kimlik, cihaz, resurs həssaslığı və risklə verilir; davamlı qiymətləndirmə.
- VPN avtomatik daxili səlahiyyət yaratmır; seqmentasiya və xidmət səviyyəsində avtorizasiya qalır.
:::

:::reveal Credential stuffing, pass-the-hash və Kerberoasting hansı fərqli sirrlərdən istifadə edir?
- **Credential stuffing**: başqa xidmətdən sızmış istifadəçi–parol cütləri (parol təkrarı).
- **Pass-the-hash**: NTLM ssenarisində parolun NT heşi parol əvəzinə işlədilir.
- **Kerberoasting**: SPN üçün alınan xidmət biletinin xidmət açarı ilə qorunan hissəsi oflayn təxmin edilir (zəif xidmət parolu).
- Tədbirlər uyğun olaraq: MFA və sızmış parol yoxlaması; imtiyaz ayrılığı və NTLM-in azaldılması; uzun sirr, gMSA, az imtiyaz.
:::

:::reveal Testbed, giriş baxışı və audit bir-birini hansı sübutlarla tamamlayır?
- **Testbed**: təcrid olunmuş mühitdə müsbət və mənfi, sərhəd sınaqları (gözlənilən qərar əvvəl yazılır); test nəticələri.
- **Giriş baxışı (access review)**: faktiki hüquq siyahısı və ləğv təsdiqi.
- **Audit**: siyasət, proses və sübutlar meyarlara qarşı təkrarlana bilən yoxlama; qaydanın faktiki icrasını müqayisə edir.
- Üçü birlikdə jurnal və proses sənədinin uyğun gəldiyini göstərir.
:::

## Situasiya tapşırıqları

**Situasiya 1.** Universitetin məhdud tədqiqat arxivində Açıq, Məxfi və Çox məxfi səviyyələri var. Məxfi səviyyədə işləyən Kamran çox məxfi sənədi oxumaq və açıq portala mətn yazmaq istəyir. Digər hüquqların mövcud olduğunu fərz etməklə Bell–LaPadula və sərt Biba qərarlarını müqayisə edin.

:::reveal Cavab
- **BLP** (məxfilik): yuxarı səviyyəni oxumaq (no read up) və aşağı səviyyəyə yazmaq (no write down) qadağandır, hər iki müraciət rədd olunur.
- Eyni sıra tamlıq səviyyələrini göstərsəydi, **sərt Biba** yuxarıdan oxumağa və aşağıya yazmağa mane olmazdı (qadağan: aşağıdan oxumaq, yuxarıya yazmaq).
- Səbəb: Biba məxfiliyi deyil, aşağı etibarlı məlumatın yuxarı tamlığa təsirini məhdudlaşdırır.
- Hər iki halda əlavə ACL, kateqoriya və əməliyyat şərtləri ayrıca ödənməlidir.
:::

**Situasiya 2.** Universitet laborantı katib vəzifəsinə keçib. İnventar administratorluğu saxlanıb, üstəlik ona qiymət düzəlişi hazırlamaq və həmin düzəlişi təsdiqləmək hüquqları verilib. Hüquq siyahısı baxışa göndərilib, lakin faktiki dəyişiklik olmayıb. Hansı tədbirlər tələb olunur?

:::reveal Cavab
- **Pozuntu**: mover prosesində köhnə hüquq götürülməyib, hüquq yığılması (privilege creep) var.
- Hazırlama və təsdiq hüquqlarının eyni şəxsdə olması statik vəzifə bölgüsü seçilibsə pozuntudur. Dinamik bölgüdə hər ikisi verilə bilər, amma şəxs öz hazırladığını təsdiqləyə bilməməlidir; situasiyada bu məhdudiyyətin işləyib-işləmədiyi göstərilmir, ayrıca yoxlanmalıdır.
- **Tədbir**: cari işə uyğun hüquq çoxluğu hesablanır, inventar hüququ ləğv edilir, seçilmiş bölgü qaydası tətbiq olunur.
- **Yoxlama**: siyahının baxışa göndərilməsi ləğvin sübutu deyil; icra təsdiqi və giriş sınağı lazımdır.
:::

**Situasiya 3.** Universitet əməkdaşı saxta kitabxana girişinə parol və SMS kodu yazıb. Sonra həqiqi LMS-də onun sessiyası ilə tələbə siyahısı ixrac edilib. Əməkdaş artıq parolu dəyişib. Hadisəni hansı mexanizm izah edir və cavab niyə bitmiş sayılmır?

:::reveal Cavab
- **Mexanizm**: real vaxt fişinqi; parol və kod həqiqi xidmətə ötürülüb, sessiya əldə edilib. SMS kodu domenlə bağlı olmadığı üçün bu hücuma davamlı deyil.
- **Niyə bitməyib**: parolun dəyişməsi hazır sessiyanı bağlamır.
- **Tədbir**: aktiv sessiyalar və yeniləmə token-ləri ləğv edilir, ixrac və hesab dəyişiklikləri araşdırılır, cihaz yoxlanır.
- **Gələcək**: FIDO2 və təhlükəsiz bərpa; FIDO2 artıq oğurlanmış sessiyanı öz-özünə ləğv etmir.
:::

**Situasiya 4.** Universitet mobil tətbiqinin API-si istənilən düzgün imzalanmış JWT-ni qəbul edir. Hücumçu başqa kitabxana müştərisi üçün verilmiş ID token-i göndərir. İmza düzgündür və token-in müddəti bitməyib. API nəyi səhv edir?

:::reveal Cavab
- API token-in növünü və nəzərdə tutulduğu auditoriyanı ayırmır.
- ID token müştərinin autentifikasiya nəticəsidir, API-yə giriş üçün access token əvəzi deyil.
- API özünə aid token-i etibarlı issuer, düzgün audience, müddət və tələb olunan səlahiyyət üzrə yoxlamalı, sonra obyekt səviyyəsində icazə verməlidir.
- Tək düzgün imza kifayət etmir.
:::

**Situasiya 5.** Universitetin kitabxana xidmət hesabı üçün bir istifadəçi qısa müddətdə çox sayda Kerberos xidmət bileti istəyib. Hesabın parolu zəifdir. Təhlükəsizlik qrupu yalnız həmin istifadəçini bağlamaq istəyir. Risk və daha tam tədbir nədir?

:::reveal Cavab
- **Risk**: davranış Kerberoasting ilə uyğun ola bilər, lakin kontekst yoxlanmadan hücum təsdiqlənmir.
- Artıq alınmış biletin qorunan hissəsi oflayn təxmin üçün saxlanıla bilər; istifadəçini bağlamaq bu hesablamanı dayandırmır.
- **Tədbir**: xidmətin sirri və açarları planlı dəyişdirilir, uyğun mühitdə idarə olunan xidmət hesabı (gMSA) seçilir, artıq imtiyazlar götürülür, hadisənin mənbə cihazı araşdırılır.
:::

**Situasiya 6.** Universitet məsləhətçisi bir-birinə rəqib iki şirkətin məxfi layihələrində çalışır. Birinci şirkətin sənədini oxuyub, sonra ikinci şirkətin layihəsinə keçmək istəyir. Ayrı brauzer və yeni sessiyanın kifayət etdiyini düşünür. Brewer–Nash modeli necə tətbiq olunmalıdır?

:::reveal Cavab
- Qərar brauzerin deyil, şəxsin əvvəlki girişinə əsaslanır.
- Şirkətlər eyni maraq toqquşması sinfindədirsə, birincinin məxfi məlumatını oxumaq ikincinin müvafiq məlumatına girişi məhdudlaşdırır.
- Tarixçə şəxs kimliyi ilə əlaqələndirilir, ikinci hesabla yayınma bağlanır.
- Yazma qaydaları birinci məlumatın ikinci layihəyə ötürülməsinin qarşısını almalıdır.
:::

**Situasiya 7.** Universitet əməkdaşının hesabı mərkəzi kataloqda bağlanıb, amma əvvəl açılmış LMS sessiyası ilə qiymət düzəlişi hələ mümkündür. IAM hesabatı işi tamamlanmış göstərir. Leaver prosesi necə düzəldilməlidir?

:::reveal Cavab
- **Səbəb**: mərkəzi bloklama ilə tətbiq sessiyasının ləğvi ayrılıb.
- **Tədbir**: LMS sessiyası dayandırılır, token müddəti və ləğv siqnalı yoxlanır, digər əlaqəli sistemlərdə qalıq giriş axtarılır.
- **Yoxlama**: tamamlanma kataloq cavabı ilə deyil, hədəf tətbiqlərdə girişin faktiki rəddi ilə ölçülür.
- Son qiymət dəyişiklikləri audit üçün araşdırılır.
:::

## Konspektdən situasiyalar

**Situasiya K1.** Universitetin hərbi kafedrasında BLP modeli tətbiq edilib, üç səviyyə var: Açıq < Məxfi < Çox məxfi. "Məxfi" buraxılışlı müəllim Kamran (a) çox məxfi hesabatı oxumaq, (b) açıq elan lövhəsinə (portala) qeyd yazmaq, (c) məxfi sənədi oxumaq istəyir. Hansılar mümkündür? Eyni səviyyələr Biba-da tamlıq səviyyələri olsaydı, nə dəyişərdi?

:::reveal Cavab
- **BLP**: (a) qadağandır (no read up); (b) qadağandır (no write down, sirrin aşağı sızması riski); (c) icazəlidir (eyni səviyyə).
- **Biba**: qadağan olan aşağıdan oxumaq və yuxarıya yazmaqdır; ona görə (a) yuxarıdan oxumaq, (b) aşağıya yazmaq və (c) eyni səviyyə icazəlidir.
- **Səbəb**: Biba-nın məqsədi sirri qorumaq deyil, etibarlı məlumatı etibarsız mənbədən qorumaqdır.
:::

**Situasiya K2.** Universitetdə laborant üç il əvvəl müəllim olub, amma hələ də laborant dövründəki inventar sisteminə və maaş cədvəlinə admin girişi var. İndi o, həm də qiymət sistemində admin hüququ alıb. Hansı prinsiplər pozulub, nə etmək lazımdır?

:::reveal Cavab
- **Pozuntu**: vəzifə dəyişəndə köhnə hüquqlar götürülməyib, bu hüquq yığılmasıdır (privilege creep) və minimal səlahiyyətin pozulmasıdır.
- Vəzifələrin bölgüsü üçün hansı ziddiyyətli funksiyaların birləşdiyinə baxılır: məsələn, həm balı dəyişib, həm də bu dəyişikliyi özü təsdiqləyə bilirsə, prinsip pozulub.
- **Həll**: joiner–mover–leaver prosesində "mover" addımında köhnə hüquqların avtomatik götürülməsi, RBAC rolları, dövri hüquq yoxlaması (access review), admin hüquqlarının PAM ilə müvəqqəti verilməsi.
:::

**Situasiya K3.** Universitetdə müəllimlərin Microsoft 365 hesablarında SMS kodu ilə MFA var. Müəllimə "Kafedra iclasının protokolu" adlı məktub gəlir, linkdə saxta giriş səhifəsi açılır. Müəllim orada həm parolu, həm SMS kodunu daxil edir və hücumçu həmin an onun poçtuna və qiymət sisteminə girir. MFA niyə kömək etmədi və nə tövsiyə edərdin?

:::reveal Cavab
- **Mexanizm**: real vaxt fişinqi (adversary-in-the-middle): saxta sayt parolu və birdəfəlik kodu dərhal həqiqi sayta ötürür, sessiya tokenini oğurlayır. SMS və OTP kodları fişinqə davamlı deyil.
- **Tövsiyə**: müəllim və admin hesabları üçün FIDO2 açarları və ya passkey-lər (açar yalnız həqiqi domen üçün işləyir); şərti giriş siyasəti (qiymət sisteminə yalnız idarə olunan cihazlardan); qeyri-adi girişlərin izlənməsi.
- **İnsident**: sessiya tokenlərinin dərhal ləğvi, müəllimlərə fişinq təlimi.
:::

## Ehtimal olunan əlavə suallar

:::reveal Autentifikasiya ilə avtorizasiyanın fərqi nədir? Nümunə ilə izah edin.
- Autentifikasiya kimliyi, avtorizasiya icazəni yoxlayır.
- Dekanlıq əməkdaşı düzgün parol və MFA ilə daxil olub (autentifikasiya uğurludur), amma başqa fakültənin tələbəsinin şəxsi işini aça bilirsə, bu avtorizasiya problemidir.
- READ, WRITE, EXECUTE giriş əməliyyatlarıdır, yəni avtorizasiyaya aiddir.
- OAuth 2.0 avtorizasiya, OIDC autentifikasiya qatıdır.
:::

:::reveal DAC, MAC, RBAC, ABAC və qayda əsaslı modelləri müqayisə edin.
- **DAC**: sahib verir; fayl icazələri; zəif cəhət səhv paylaşma.
- **MAC**: mərkəzi siyasət, etiketlər; SELinux, AppArmor; sərt, idarəsi çətin.
- **RBAC**: rol əsaslı; AD qrupları, ERP; role explosion.
- **ABAC**: atributlar (istifadəçi, resurs, mühit); bulud IAM, Zero Trust; mürəkkəb siyasət, köhnə atribut.
- **Qayda əsaslı**: hamıya eyni qaydalar; firewall ACL; fərdi istisna çətindir.
:::

:::reveal Faktorların təsnifatı və MFA-nın gücü. SMS, TOTP, push və FIDO2-ni sıralayın.
- Faktorlar: bildiyin (parol, PIN), sahib olduğun (telefon, smart kart, FIDO2 açarı), özünə məxsus (barmaq izi, üz); IP, yer, vaxt kontekstdir.
- Güc sırası: SMS < TOTP < push (rəqəm uyğunlaşdırması ilə) < FIDO2/passkey.
- Zəifliklər: SMS SIM-swap və real vaxt ötürmə; TOTP saxta sayta yazıla bilir; push bildiriş yorğunluğu; FIDO2 üçün bərpa və son qurğu qorunmalıdır.
:::

:::reveal Köhnə və NIST SP 800-63B-4 parol yanaşmasını müqayisə edin.
- Köhnə: min. 8 simvol; böyük hərf, rəqəm, simvol məcburiyyəti; hər 30–90 gündən bir dəyişmə.
- Yeni: yalnız parolla girişdə min. 15, MFA tərkibində min. 8, 64 simvola qədər qəbul; tərkib qaydaları və məcburi dəyişmə yox, yalnız sızma olanda.
- Əlavə: sızmış parol siyahısı, cəhd limiti, parol meneceri və paste.
- Saxlama: duzlanmış, yavaş funksiya (Argon2id, bcrypt, scrypt, PBKDF2).
:::

:::reveal Joiner–mover–leaver nədir və nəyi yoxlamaq lazımdır?
- Joiner: şəxs yoxlanır, sabit identifikator yaranır, rola uyğun minimum hüquq verilir, provisioning yoxlanır.
- Mover: köhnə hüquqlar götürülür, yenilər verilir; unudulsa privilege creep.
- Leaver: hesab, VPN, kart, sessiyalar, token-lər, API açarları dərhal bağlanır.
- Dövri yoxlama (access review): hüquqlar iş ehtiyacı ilə müqayisə olunur. Hesablama nümunəsi: 120 təyinatdan 18-i ləğv olunmalıdır, 12-si icra olunubsa, tamamlanma 12 / 18 ≈ 66,7 %.
:::

:::reveal SAML, OAuth 2.0 və OIDC-ni müqayisə edin.
- **SAML 2.0**: XML əsaslı, korporativ veb; imzalı assertion (IdP → SP).
- **OAuth 2.0**: avtorizasiya, access token, scope; parol verilmir.
- **OIDC**: OAuth üzərində autentifikasiya, ID token, JSON/JWT; müasir veb və mobil.
- Hər birində imza, issuer, audience, vaxt yoxlanır; yerli avtorizasiya ayrıca qalır.
:::

:::reveal Kerberos-da ardıcıllığı yazın və iki risk göstərin.
- AS-REQ, AS-REP (TGT), TGS-REQ (TGT, xidmət adı, autentifikator), TGS-REP (xidmət bileti), AP-REQ, AP-REP (qarşılıqlı autentifikasiya).
- Risklər: vaxt fərqi qanuni girişi pozur; zəif xidmət parolu Kerberoasting-ə imkan verir; KDC kompromitasiyası realmı təhlükəyə salır.
- kdestroy yalnız lokal biletləri silir.
:::

:::reveal Fail-secure ilə fail-safe fərqi nədir?
- Fail-secure: girişə nəzarət mexanizmi sıradan çıxanda icazəsiz giriş açılmır (siyasət xidməti dayananda ixrac rədd edilir).
- Fail-safe: insan təhlükəsizliyini önə qoyur (yanğında təxliyə qapısı açılır, 4-cü mövzu).
- Fail-secure yüksək əlçatanlığı ləğv etmir: ehtiyat siyasət xidməti və nəzarətli keş qurula bilər.
:::

:::reveal Token və sessiya oğurlanmasına qarşı hansı tədbirlər var?
- Bearer token təqdim edəndə işləyir; TLS yoluxmuş cihazı dayandırmır.
- Refresh token məhdud saxlanır, rotasiya olunur; token URL-yə və loqa yazılmır.
- Cookie: Secure, HttpOnly, SameSite; XSS və CSRF ayrıca qorunur.
- Müddət bitməsi ləğv deyil; qısa müddət, introspeksiya, ləğv yayılması. İnsidentdə sessiya və refresh token-lər ləğv edilir.
:::
