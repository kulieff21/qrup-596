+++
title = "Bulud hesablamalarının əsasları və bulud təhlükəsizliyi"
unit = "orta"
order = 14
summary = "Hər anlayış 1–3 cümlə ilə izahlı: NIST modeli, ortaq məsuliyyət, IAM, şifrələmə, şəbəkə, konteyner və serverless, audit, bulud vasitələri, RPO/RTO, standartlar, iki insident və LMS köçürməsi."
updated = 2026-11-09

[[source]]
title = "Mühazirə 14: Bulud hesablamalarının əsasları və bulud təhlükəsizliyi"
note = "Elmar Cabbarov, 2026–2027"
+++

Bulud təhlükəsizliyinin əsas fikri: serverlər başqasının data mərkəzindədir, amma məlumatın, hesabların və konfiqurasiyanın məsuliyyəti əsasən müştəridə qalır. Misallar universitetin tədris idarəetmə sisteminə (Learning Management System, LMS) aiddir və şərti tədris nümunəsidir.

## Bulud hesablamaları nədir

Bulud hesablamaları (cloud computing) konfiqurasiya edilə bilən resursların (server, yaddaş, şəbəkə, tətbiq, xidmət) ortaq hovuzuna şəbəkə vasitəsilə, tələbə uyğun və minimal idarəetmə səyi ilə giriş modelidir. NIST SP 800-145 beş xüsusiyyəti, üç xidmət modelini və dörd yerləşdirmə modelini müəyyən edir. Tərifdə "şəbəkə üzərindən" deyilir: daxili şəbəkədən əlçatan özəl bulud da uyğundur. Sabit server icarəsi və ya statik sayt avtomatik bulud deyil.

| Xüsusiyyət | Mənası | Nümunə |
| --- | --- | --- |
| Tələb üzrə özünəxidmət | Müştəri resursu provayder əməkdaşı olmadan panel və ya API ilə ayırır | Laboratoriya rəhbəri sınaq mühiti yaradır |
| Geniş şəbəkə girişi | Standart mexanizmlərlə müxtəlif cihazlardan giriş | Tələbə LMS-ə telefondan daxil olur |
| Resursların hovuzlaşdırılması | Çox müştəri arasında bölünür | Kitabxananın virtual maşını ortaq hovuzdadır |
| Sürətli elastiklik | Tutum tələbə görə artır və azalır | İmtahan vaxtı nüsxələr artır |
| Ölçülən xidmət | İstifadə ölçülür və hesabatlandırılır | Kafedra saat və saxlanc həcmini görür |

Özünəxidmət təsdiq qaydasının olmaması demək deyil: universitet kvota və təsdiqlənmiş obrazlar təyin edə bilər, sifariş sərhəd daxilində avtomatik emal olunur. Hovuzlaşdırma çoxicarəçiliyi (multi-tenancy) mümkün edir; kimlik, yaddaş və şəbəkənin məntiqi izolyasiyasını hipervizor (hypervisor), xidmətin avtorizasiyası və şəbəkə tədbirləri qurur, ona görə ortaq avadanlıq hər kəsin başqasının faylını oxuması demək deyil.

Elastiklik (elasticity) tələblə genişlənmə və daralmadır, miqyaslanma (scalability) isə artan yükü qarşılamaq qabiliyyətidir. Daha böyük maşın şaquli, çoxlu nüsxə üfüqi miqyaslanmadır. Elastik resurslar sonsuz deyil: kvota, region tutumu və büdcə var.

İdarəetmə müstəvisi (control plane) resursları yaradan və dəyişən interfeysdir (panel, API), məlumat müstəvisi (data plane) tətbiqin gündəlik məlumat əməliyyatıdır. Hücumçu LMS-in giriş səhifəsinə toxunmadan oğurlanmış idarəetmə hesabı ilə bütün bazanı silə bilər. Panel və proqramlaşdırma interfeysi (Application Programming Interface, API) eyni səlahiyyətin iki yoludur; məhdudiyyət avtorizasiya siyasətindədir.

## Yerli infrastruktur, üstünlüklər və məhdudiyyətlər

Yerli infrastrukturda (on-premises) universitet server otağını, enerjini, avadanlığı və proqram qatlarını özü idarə edir. Bulud bu işlərin bir hissəsini xidmət kimi verir, lakin xidmətin seçilməsi, hesablar və tələbə məlumatının qorunması universitetdə qalır: buluda keçid İT komandasının ləğvi deyil, iş bölgüsünün dəyişməsidir. Keyfiyyət yoxlaması (Quality Assurance, QA) mühitində real tələbə bazası əvəzinə şəxsiyyətsizləşdirilmiş məlumat işlədilir.

**Üstünlüklər.** İlkin kapital xərci dəyişkən xərcə çevrilir, imtahan mövsümündə əlavə tutum götürülür, coğrafi əhatə gecikməni azaldır. Şərtlər: istifadə bitəndə resurs bağlanmalıdır (dayandırılmış maşının diski ödəniş yarada bilər), məlumatın regionu və surətləri əvvəlcədən razılaşdırılmalıdır, idarə olunan xidmətin yenilənməsindən sonra inteqrasiya yenidən sınanmalıdır.

**Məhdudiyyətlər:** əlaqə və xidmət fasiləsi (çoxzonalı quruluş, bərpa sınağı), məxfilik riski (təsnifat, minimal icazə), hücum səthi (panel, API, hesablar; MFA, audit), məhdud texniki nəzarət (SaaS bazasına giriş yoxdur; ixrac əvvəl yoxlanır), provayderə bağlılıq (portativ format), dəyişkən xərc (kvota, xərc xəbərdarlığı, bitmə tarixi).

Ümumi sahibolma xərci (Total Cost of Ownership, TCO) hesablama, saxlanc, trafik, lisenziya, dəstək, audit və əməyi, həm də məlumatın çıxarılmasını əhatə edir; universal "bulud həmişə ucuzdur" qaydası yoxdur. Şərti nümunə: saatı 0,20 manat resurs 100 saat işləsə 20 manat, unudulub 720 saat işləsə 144 manat edir. Xidmət səviyyəsi razılaşması (Service Level Agreement, SLA) ölçülən əlçatanlığı, istisnaları və pozuntuda şərtləri təyin edir; xidmət krediti itirilmiş imtahanı bərpa etmir. DNS, kimlik xidməti və tətbiq də əlçatanlıq zəncirindədir.

## Buludun yerləşdirmə modelləri

Yerləşdirmə modeli infrastrukturdan kimin istifadə etdiyini göstərir və xidmət modelindən ayrıdır.

| Model | Tərif | Nümunə |
| --- | --- | --- |
| İctimai (public) | Geniş ictimaiyyət üçün, müştəri resursları məntiqi ayrılır | Microsoft 365, AWS |
| Özəl (private) | Yalnız bir təşkilat üçün, üçüncü tərəf də idarə edə bilər | OpenStack/Proxmox əsasında öz bulud |
| İcma (community) | Ortaq tələbləri olan təşkilatlar üçün | Universitetlərin ortaq tədqiqat buludu |
| Hibrid (hybrid) | Müstəqil iki və ya daha çox bulud, daşınmanı mümkün edən texnologiya ilə əlaqələndirilir | Özəl bazası + ictimai buludda tətbiq nüsxələri |

- İctimai bulud məlumatın hamıya açıq olması deyil; təhlükəsizlik izolyasiyadan, icazələrdən, konfiqurasiyadan asılıdır. İctimai saxlanc ayrıca konfiqurasiya qərarıdır.
- Özəl bulud mütləq universitetin İT şöbəsində olmur; "özəl" ad təhlükəsizlik vermir, yamaq gecikirsə və nüsxə yoxlanmırsa.
- İcma buludunda silmə və üzv ayrılması qaydaları əvvəl yazılır.
- Hibrid üçün bütün növlər tələb olunmur. Rabitə VPN-dən, İnternetdən və ya xüsusi bağlantıdan keçə bilər və mütləq yavaş deyil.
- Çoxbuludlu istifadə (multi-cloud) bir neçə provayderdən istifadədir, NIST-in beşinci modeli deyil; asılılığı azalda bilər, amma kimlik, audit və bacarıq tələbini artırır.

:::exam
Qarışdırılan fikirlər: "ictimai bulud açıq olduğu üçün az təhlükəsizdir" (yanlış), "hibrid üç növün birləşməsidir" (yanlış), "IaaS istifadəçi başına ödənir" (yanlış, resurs istifadəsinə görədir), "tərifdə İnternet var" (yox, şəbəkə).
:::

## Xidmət modelləri və ortaq məsuliyyət

İnfrastruktur xidmət kimi (Infrastructure as a Service, IaaS) hesablama, saxlanc və şəbəkə verir; qonaq ƏS və tətbiq universitetdədir (Amazon EC2, Azure Virtual Machines). Platforma xidmət kimi (Platform as a Service, PaaS) idarə olunan icra mühiti verir; kod, asılılıq və məlumat universitetdədir (Azure App Service, Google App Engine, Heroku). Proqram təminatı xidmət kimi (Software as a Service, SaaS) hazır tətbiqdir (Microsoft 365, Google Workspace); universitet hesabların həyat dövrünü, paylaşmanı, rolları və məlumatı idarə edir.

Ortaq məsuliyyət (shared responsibility): buludun təhlükəsizliyi (security of the cloud: bina, enerji, avadanlıq, hipervizor) provayderdədir, buluddakı təhlükəsizlik (security in the cloud: məlumat, hesablar, icazələr, konfiqurasiya) seçilən modeldən asılı olaraq universitetdədir.

| İş | IaaS | PaaS | SaaS |
| --- | --- | --- | --- |
| Bina, avadanlıq, hipervizor | Provayder | Provayder | Provayder |
| Qonaq ƏS yamaqları | Universitet | Provayder | Provayder |
| İcra mühiti, platforma yamaqları | Universitet | Provayder | Provayder |
| Tətbiq kodu, əlavələr | Universitet | Universitet | Əsas tətbiq provayder, inteqrasiyalar universitet |
| Hesablar, rollar, MFA siyasəti | Universitet | Universitet | Universitet |
| Məlumatın təsnifatı | Universitet | Universitet | Universitet |

Provayder öz izolyasiyasını və müqavilə tədbirlərini işlədir. Eyni LMS: virtual maşında universitet ƏS və tətbiq yamaqlarını saxlayır; idarə olunan platformada ƏS yamaqları provayderə keçir, amma təhlükəli fayl yükləməsi universitetindir; SaaS LMS-də yanlış kurs rolu ilə qiymətlərin görünməsi universitetin konfiqurasiya xətasıdır. Modellər qarışa bilər, ona görə aktiv reyestrində hər komponentin sahibi yazılır.

:::exam
Bulud insidentlərinin çoxu provayderin sındırılmasından yox, müştərinin səhv konfiqurasiyasından və oğurlanmış hesablardan baş verir. SaaS-da belə hesablar, MFA və paylaşma müştəridədir.
:::

## Buludda təhdid modeli

Təhdid modeli (threat model) aktivləri, etibar sərhədlərini, hücumçunun imkanlarını və zərəri əlaqələndirir. Aktiv yalnız maşın deyil: tələbə bazası, imtahan sualları, idarəetmə tokeni, ehtiyat nüsxə və büdcə də aktivdir. Tələbənin icazəsi ilə tətbiq rolunun səlahiyyəti ayrı kimliklərdir: zəiflik rolun bütün səlahiyyətini verə bilər, ona görə rol dar saxlanır.

| Risk | Nümunə | Tədbir |
| --- | --- | --- |
| Səhv konfiqurasiya | Açıq bucket, hər yerdən SSH-ə icazə verən security group | İctimai girişin qadağası, avtomatik yoxlama |
| Hesabın ələ keçirilməsi | Admin hesabında MFA yox, root hesabı gündəlik işlənir | Fişinqə davamlı MFA |
| Sızmış açarlar | AWS açarı GitHub-a yüklənir, botlar dəqiqələr ərzində tapır | Qısaömürlü kimlik, sirr skanı |
| Artıq icazələr | Xidmət hesabına AdministratorAccess | Dar siyasət |
| Təhlükəsiz olmayan API | Autentifikasiyasız, sürət məhdudiyyətsiz | Avtorizasiya, limit |

Konfiqurasiya xətası hücumla başlamır: qəbul şöbəsi asanlıq üçün anonim keçid aça bilər. Təhlükəsiz başlanğıc parametrləri, avtomatik yoxlama və alternativ kanal xətanı azaldır. Gizli İT (shadow IT) təsdiqlənmiş reyestrə düşməyən xidmət istifadəsidir (kafedranın öz kartı ilə SaaS alması); hesablaşma uçotu, kimlik icazələri və şəbəkə müşahidəsi ilə aşkarlanır, məsul şəxs və məlumatın yeri müəyyən edilir.

## Kimlik və girişin idarəsi

Kimlik və girişin idarəsi (Identity and Access Management, IAM) kimin hansı şərtlərlə nəyi edə biləcəyini müəyyən edir: autentifikasiya kimliyi yoxlayır, avtorizasiya icazəni qiymətləndirir. Kimlik insan, virtual maşın rolu, konteyner xidmət hesabı və ya yerləşdirmə tokeni ola bilər.

- **SSO və federasiya.** Vahid giriş (Single Sign-On, SSO) ilə əməkdaş kimlik provayderi (Identity Provider, IdP) vasitəsilə daxil olur; SAML və OpenID Connect federasiya mexanizmləridir. SSO doğru rol bölgüsü yaratmır.
- **RBAC və ABAC.** Rol əsaslı giriş nəzarəti (Role-Based Access Control, RBAC) icazəni vəzifəyə bağlayır; atribut əsaslı (Attribute-Based Access Control, ABAC) şöbə, etiket, mühit və sessiyaya görə qərar verir. Etiketi dəyişmək hüququ da qorunmalıdır, yoxsa məhdudiyyətdən yan keçmək olar.
- **Minimal səlahiyyət (least privilege).** Vəzifənin tələb etdiyi ən dar icazə, əməliyyat, resurs, mühit və vaxt üzrə. İcazə siyasəti rolun nə edə biləcəyini, etibar siyasəti rolu kimin qəbul edə biləcəyini bildirir; ikisi də dar olmalıdır.
- **IAM fraqmenti.** `s3:GetObject` ilə yalnız `unec-lms-example/assignments/*` oxunur; siyahılama və yazma yoxdur. Effektiv icazə digər siyasətlərə, təşkilat məhdudiyyətlərinə və açar siyasətinə də bağlıdır; AWS-də açıq rədd (explicit deny) icazəni üstələyə bilər.
- **MFA.** Çoxfaktorlu autentifikasiya (Multi-Factor Authentication, MFA) fərqli amilləri birləşdirir; adminlər üçün FIDO2 açarı və ya passkey kimi fişinqə davamlı üsullar, SMS və kor-koranə təsdiq isə zəif sayılır. Oğurlanmış sessiya tokeni MFA-dan sonra da risklidir, ona görə cihaz vəziyyəti və sessiya müddəti də baxılır.
- **Əsas hesab (root account) və PAM.** Root və qlobal admin gündəlik işlədilmir; imtiyazlı girişin idarəsi (Privileged Access Management, PAM) ilə səlahiyyət müvəqqəti (just-in-time) verilir. Fövqəladə giriş hesabı ayrıca qorunur. Ayrılan əməkdaşın rolları, sessiyaları və API açarları ləğv edilir.
- **Xidmət kimlikləri və sirlər.** Statik açar əvəzinə iş yükü kimliyi (workload identity) və qısaömürlü token. Sirlər AWS Secrets Manager və ya Azure Key Vault-da saxlanır, konteyner obrazına, Git-ə və loga yazılmır. Açar sızıbsa, silmək yetməz: ləğv edilir, istifadəsi araşdırılır, yaradılmış resurslar yoxlanır.

## Məlumatların və açarların qorunması

Təsnifat: açıq (elan), daxili (kafedra sənədləri), məxfi (qiymət, şəxsi iş), ciddi məhdud (imtahan sualları, sistem sirləri); hər sinfin giriş qaydası və saxlama tədbiri fərqlidir.

**Açıq saxlanc.** Obyekt saxlancı (object storage) faylı obyekt kimi saxlayır, konteyner bucket adlanır. Adın çətin təxmin edilməsi giriş nəzarəti deyil; ictimai siyasət, girişə nəzarət siyahısı (Access Control List, ACL), SaaS paylaşma keçidi və müvəqqəti imzalı URL ayrıca yoxlanır. Qəbul sənədləri defolt özəl saxlanır, hesab səviyyəsində ictimai giriş bloklanır. `get-public-access-block`, `get-bucket-policy-status` və `get-bucket-encryption` əmrləri bloku, siyasət qiymətləndirməsini və şifrələməni göstərir, amma heç biri tək effektiv girişin sübutu deyil; anonim oxunuşun rədd sınağı lazımdır.

**Şifrələmə.** Ötürülən məlumat TLS ilə qorunur (TLS 1.2 və 1.3), saxlanan məlumat disk, baza və ya obyekt şifrələməsi ilə. Saxlanarkən şifrələmə surətin icazəsiz əldə edilməsindən qoruyur, amma səlahiyyətli xidmət məlumatı açıb veririsə, yanlış avtorizasiyanı dayandırmır; açıq saxlancın şifrəli olması məxfilik demək deyil.

:::exam
Şifrələmə giriş nəzarətini əvəz etmir. Saxlancda şifrələmə aktivdir, amma anonim sorğu sənədi qaytarırsa, risk qalır.
:::

**KMS və açarlar.** Açar idarəetmə xidməti (Key Management Service, KMS) açarın yaranması, icazələri, auditi və həyat dövrünü verir. Zərf üsulu (envelope encryption) ilə məlumat məlumat açarı (Data Encryption Key, DEK) ilə şifrələnir, DEK isə açar şifrələmə açarı (Key Encryption Key, KEK) ilə qorunur; şifrəli DEK şifrəli obyektlə yanaşı saxlanır, KEK-in qorunması çoxlu obyektin açılmasına təsir edir.

Öz açarını gətirmə (Bring Your Own Key, BYOK) müştərinin açar materialını xidmətə gətirməsidir; provayderin məlumatı heç vaxt aça bilməməsi nəticəsi çıxmır. Aparat təhlükəsizlik modulu (Hardware Security Module, HSM) də tətbiq icazələrini əvəz etmir. Açar idarəçisi ilə məlumat oxuyan rol ayrılır; rotasiya köhnə nüsxənin açılmasına mane olmamalıdır. Məlumat sızmasının qarşısının alınması (Data Loss Prevention, DLP) həssas məzmunun icazəsiz ötürülməsini aşkarlayıb bloklayır; qayda əvvəl müşahidə rejimində sınanır.

## Bulud şəbəkəsinin təhlükəsizliyi

Virtual özəl bulud (Virtual Private Cloud, VPC) və Azure-da Virtual Network (VNet) məntiqi şəbəkə sərhədidir; alt şəbəkə, marşrut və təhlükəsizlik qaydası birlikdə trafik yolunu təyin edir. "Özəl" ad qorunma vermir: ictimai IP və İnternetə marşrut faktiki əlçatanlığı dəyişir. LMS üçün giriş, tətbiq və baza qatları ayrılır; istifadəçi yalnız giriş qatına HTTPS ilə gəlir, bazaya ictimai ünvan verilmir, idarəetmə qorunan giriş xidmətindən keçir.

Şəbəkə təhlükəsizlik qrupu (security group) trafik qaydaları dəstidir; AWS-də vəziyyəti izləyir (stateful) və yalnız icazə qaydaları var, Azure NSG-də prioritetli icazə və rədd qaydaları var. Şərti matris: İnternet → balanslaşdırıcı TCP 443; giriş qrupu → tətbiq TCP 8443; tətbiq → PostgreSQL TCP 5432; qorunan idarəetmə → tətbiq TCP 22; tətbiq → özəl saxlanc TCP 443; digər mənbələr → baza: heç nə. Açıq port tətbiq icazəsi deyil. 0.0.0.0/0 bütün IPv4, ::/0 bütün IPv6 mənbələrini əhatə edir; yalnız IPv4-ü sərtləşdirmək səhvdir.

- Özəl endpoint özəl yol verir, IAM-i əvəz etmir; NAT çıxış ünvanını dəyişir, sızmanı dayandırmır; tətbiqin çıxış trafiki məhdudlaşdırılır.
- Veb tətbiq firewall-u (Web Application Firewall, WAF) HTTP sorğularını süzür, sürət limiti və provayderin DDoS müdafiəsi giriş qatını qoruyur; başqa tələbənin tapşırığını oxuyan düzgün görünən sorğunu isə tətbiq obyekt səviyyəsində yoxlamalıdır.
- AWS Direct Connect və Azure ExpressRoute defolt başdan-başa şifrəli deyil; TLS, IPsec və ya ayrıca imkan lazımdır.

## Konteyner, serverless və təchizat zənciri

Eyni LMS əlavəsi virtual maşında, konteynerdə və funksiya kimi fərqli istismar qaydası tələb edir; iş yükünün (workload) forması yamaq, müşahidə və kimlik məsuliyyətini dəyişir.

- **Konteyner.** Asılılıqlarla paketlənir və hostun nüvəsini paylaşır. İmtiyazlı konteyner, yazma hüquqlu host qovluğu və idarəetmə soketi izolyasiyanı zəiflədir; tədbirlər: kök istifadəçi olmamaq, lazımsız imkanları azaltmaq, fayl sistemini yalnız oxunan etmək. Kubernetes-də idarəetmə API-si, xidmət hesabları, sirlər və şəbəkə siyasətləri ayrıca qorunur; ad məkanı (namespace) tək güclü sərhəd deyil. Obraz kriptoqrafik heşi (digest) ilə seçilir, skan olunur, icrada izlənir; skanın uğurlu olması gələcək zəiflik olmayacağına zəmanət deyil. NIST SP 800-190 konteyner, NIST SP 800-125 virtuallaşdırma üzrədir.
- **Serverless.** Serversiz hesablama (serverless computing) server istismarını müştəridən gizlədir; funksiya xidmət kimi (Function as a Service, FaaS) bunun formasıdır. Provayder icra infrastrukturunu, universitet kod, asılılıq, hadisə mənbəyi və rolu qoruyur. Təkrar gələn hadisəyə qarşı idempotency lazımdır: təkrar əməliyyat əlavə nəticə yaratmamalıdır. Bütün saxlancı oxuyan rol zəifliyin təsirini artırır; gec işə düşmə (cold start) imtahan vaxtı cavab müddətinə təsir edə bilər.
- **Təchizat zənciri.** Proqram təchizat zənciri (software supply chain) kod deposu, asılılıq, qurma, obraz reyestri və yerləşdirməni əhatə edir; zərərli asılılıq və ya ələ keçirilmiş qurma hesabı artefaktı dəyişə bilər, ona görə CI/CD (Continuous Integration and Continuous Delivery) səlahiyyəti istehsalat qədər qorunur. Tədbirlər: sirr skanı, kilid faylı, təcrid edilmiş qurma, obrazın heşə bağlanması, qəbul siyasəti. SBOM (Software Bill of Materials) asılılığın harada olduğunu tapmağa kömək edir; imza mənşəyi göstərir, kodun təhlükəsizliyini yox. OWASP Top 10:2025-də A03 Software Supply Chain Failures bu sahədir.

## Audit qeydləri, monitorinq və insidentə cavab

Virtual maşının sistem qeydləri idarəetmə API-sindəki dəyişiklikləri göstərmir və maşın dayananda agent də susur, ona görə idarəetmə auditi ayrıca mənbədir.

| Mənbə | Nəyi göstərir | Məhdudiyyət |
| --- | --- | --- |
| AWS CloudTrail | API və hesab fəaliyyəti | Obyekt səviyyəli data events ayrıca seçilir |
| Azure Activity Log | İdarəetmə müstəvisində fəaliyyət | Məlumat oxunuşlarını əhatə etmir |
| Entra giriş qeydləri | Kimlik girişləri | Sonrakı əməliyyatları göstərmir |
| Google Cloud Audit Logs | İdarəetmə və seçilən məlumat girişi | Data Access sazlanır |
| Şəbəkə axın qeydləri | Mənbə, hədəf, metadata | Paket məzmunu yoxdur |
| LMS, baza, saxlanc qeydləri | Tətbiq və sorğu əməliyyatı | Kodda audit yoxdursa, görünmür |

AWS CloudWatch metrik və log, AWS Config konfiqurasiya uyğunluğu, Amazon Inspector iş yükü zəifliyi üçündür. Sonradan logu açmaq yazılmamış qeydi yaratmır. Şərti CloudTrail qeydində `PutBucketPolicy` saxlanc siyasəti çağırışını göstərir, amma ictimai açıldığını sübut etmir: nəticə, dəyişən siyasət, əvvəlki vəziyyət və ictimai giriş blokları araşdırılır, rol sessiyasının arxasındakı insan tapılır, mənbə IP yoxlanır. Təhlükəsizlik məlumatı və hadisələrinin idarəsi sistemi (Security Information and Event Management, SIEM) bu qeydi giriş, MFA nəticəsi və sonrakı obyekt əməliyyatları ilə əlaqələndirir; planlı dəyişiklik ilə müqayisəsiz avtomatik insident hökmü verilmir.

Audit arxivi ayrı hesabda saxlanır, istehsalat administratoru onu silə bilmir, saxlama dəyişməzdir, toplamanın dayanması xəbərdarlıq yaradır. İnsidentdə yayılma dayandırılır və sübut qorunur: açar ləğv edilir, sessiyalar və etibar əlaqələri araşdırılır, zərərli rol təcrid olunur. Maşını dərhal silmək sübutu məhv edə bilər; surət və qeydlər qorunandan sonra təmiz mənbədən bərpa aparılır. NIST SP 800-61 Rev. 3 (aprel 2025) cavabı risk idarəetməsi ilə əlaqələndirir.

## CSPM, CWPP, CASB və CNAPP

| Sinif | Əsas sual | Nümunə |
| --- | --- | --- |
| CSPM | Konfiqurasiya tələbə uyğundurmu? | Açıq baza, söndürülmüş audit |
| CWPP | İş yükünün özündə risk varmı? | LMS maşınında zəif paket |
| CASB | SaaS-dan kim necə istifadə edir? | Şəxsi SaaS hesabına sənəd ötürülməsi |
| CNAPP | Koddan icraya qədər risklər necə əlaqələnir? | Açıq tətbiq + zəif obraz + artıq rol |

Bulud təhlükəsizlik vəziyyətinin idarəsi (Cloud Security Posture Management, CSPM) konfiqurasiyanı qaydalara görə qiymətləndirir (AWS Config, Defender for Cloud). İnfrastruktur kod kimi (Infrastructure as Code, IaC) şablonlarının yerləşdirmədən əvvəl yoxlanması səhvi erkən tutur, qurulmuş mühitin koddan yayınması (configuration drift) sonradan aşkarlanır. Bulud iş yüklərinin qorunması platforması (Cloud Workload Protection Platform, CWPP) maşın və konteynerin zəiflik və icra riskinə baxır. Bulud giriş təhlükəsizliyi vasitəçisi (Cloud Access Security Broker, CASB) SaaS istifadəsini, paylaşmanı və kölgə İT-ni müşahidə edir; görmə sahəsi API və trafik üzrə fərqlidir. Bulud əsaslı tətbiqlərin qorunması platforması (Cloud-Native Application Protection Platform, CNAPP) bunları əlaqələndirir: yalnız zəif paketə baxmaq əvəzinə konteynerin İnternetdən əlçatan və məxfi saxlanca artıq icazəli olması nəzərə alınır. Avtomatik düzəlişin təsiri qiymətləndirilir.

## Əlçatanlıq, ehtiyat nüsxə və bərpa

Region coğrafi sahədir, əlçatanlıq zonası (Availability Zone, AZ) region daxilində nasazlığı ayırır; iki maşın avtomatik ayrı zonada deyil, faktiki yerləşmə yoxlanır. Bulud AZ, replikasiya və nüsxə verir, layihələndirmə müştərinindir.

Yüksək əlçatanlıq (high availability) komponent düşəndə xidməti davam etdirir, fəlakətdən bərpa (disaster recovery) böyük nasazlıqdan sonra qaytarır. Replikasiya səhv silinməni və zərərli dəyişikliyi də çatdırır; ehtiyat nüsxə sağlam keçmişə qayıtmaq üçündür. Regionun itməsi üçün başqa region lazım ola bilər, xərc və məlumat yerləşməsi ilə birlikdə.

Bərpa nöqtəsi hədəfi (Recovery Point Objective, RPO) itirilməsi qəbul edilən məlumat pəncərəsidir; bərpa vaxtı hədəfi (Recovery Time Objective, RTO) qəbul edilən dayanma müddətidir. RPO nə qədər məlumat itir, RTO nə qədər müddət işləmir sualına cavabdır. Onları iş sahibi qoyur, hesablanmış nəticələrlə qarışdırmaq olmaz.

:::figure
src = "m14-4.png"
alt = "Vaxt xətti: 09:45 son nüsxə, 10:00 insident, 11:30 bərpa; itki 15 dəqiqə, dayanma 90 dəqiqə."
caption = "Məlumat itkisi pəncərəsi 15 dəqiqə, xidmətin dayanması 90 dəqiqə"
:::

Şərti nümunə: son nüsxə 09:45, insident 10:00, bərpa 11:30; itki 15, dayanma 90 dəqiqədir. RPO 5 dəqiqə seçilibsə, 15 dəqiqəlik itki tələbi ödəmir. Şərti hədəflər: imtahan bazası 5 dəqiqə / 1 saat, dərs materialları 24 / 8 saat, sınaq mühiti 48 / 24 saat. Gündə bir nüsxə təxminən bir günlük itki deməkdir. Nüsxələr ayrı hesabda, ayrı icazələrlə saxlanır, dəyişməzlik (immutability) və saxlama kilidi seçilir; ehtiyat hesabın etibarı eyni oğurlanmış kimlikdən asılıdırsa, ayrı ad kifayət deyil. Bərpa sınağı fayl-baza uyğunluğunu, rolları, DNS və sertifikatı yoxlayır; KMS açarı və ya kimlik provayderi əlçatmazdırsa, sağlam nüsxə də xidməti qaytarmaya bilər.

## Standartlar, məlumatın yerləşməsi və çıxış strategiyası

Sertifikat universitetin öz saxlanc siyasətinin və bərpasının düzgünlüyünü sübut etmir; sertifikatın əhatə etdiyi xidmətlər və nəzarətin kimə aid olduğu ortaq məsuliyyət cədvəlinə bağlanır.

- CSA Bulud nəzarət matrisi (Cloud Controls Matrix, CCM) v4.1 (yanvar 2026): 17 sahədə 207 nəzarət; hər nəzarətə cavabdeh və yoxlama sübutu bağlanır.
- ISO/IEC 27001:2022 idarəetmə sistemi tələblərini, 27002:2022 nəzarət tövsiyələrini, 27017 bulud nəzarətlərini, 27018 ictimai buludda fərdi məlumatın qorunmasını verir.
- NIST CSF 2.0 (fevral 2024) altı funksiya: Govern (idarə et), Identify (müəyyən et), Protect (qoru), Detect (aşkar et), Respond (cavab ver), Recover (bərpa et). Govern satınalma, risk qəbulu və təchizatçı nəzarətini əhatə edir.
- Məlumatın yerləşməsi (data residency) məlumatın harada saxlandığı və emal edildiyidir (ehtiyat nüsxə, log, analitika, alt emalçılar da); məlumat suverenliyi (data sovereignty) hüquqi yurisdiksiya və nəzarətdir.
- Provayderə bağlılıq (vendor lock-in) format, API, xüsusi xidmət və bacarıq səbəbindən köçün çətinləşməsidir; idarə olunan xidmət onu artırıb istismar işini azalda bilər. Çıxış strategiyası (exit strategy) müqavilə bitməmiş hazırlanır: format, ixracı kim təsdiq edir, açarlar, alternativ mühitin hazırlıq vaxtı. İxracın endirilməsi onun alternativdə işləməsi demək deyil; nümunə kurs bərpa edilərək sınanır.

## İki insidentdən dərslər

**Capital One, 2019.** Açıq təsvirlər server tərəfli sorğu saxtalaşdırmasını (Server-Side Request Forgery, SSRF), müvəqqəti rol məlumatlarına çıxışı və saxlanc məlumatlarının götürülməsini əlaqələndirir; hadisəni sadəcə anonim açıq saxlanc kimi təsvir etmək dəqiq deyil. SSRF-də hücumçu serverə nəzərdə tutulmayan hədəfə sorğu göndərtdirir (məsələn, LMS-in şəkil gətirmə funksiyası ilə daxili xidmətlərə). Metadata xidməti ayrıca qorunur; IMDSv2 kömək edir, amma universal həll deyil. Dərs: sorğu imkanını daralt, rolu yalnız lazım olan obyektlərə məhdudlaşdır, qeyri-adi istifadəni izlə.

**Snowflake, 2024.** Mandiant-ın UNC5537 araşdırması oğurlanmış kimlik məlumatlarından və MFA ilə qorunmayan müştəri hesablarından istifadə edilən məlumat oğurluğu və şantaj kampaniyasını təsvir edir; platformanın özünün sındırıldığı demək deyil. Dərs: güclü MFA, iş yükü kimliyi, köhnə kimliyin ləğvi, qeyri-adi ixracın aşkarlanması; saxlanarkən şifrələmə etibarlı hesabla ixracı dayandırmır. Konspekt: Code Spaces (2014) admin hesabı və bütün nüsxələr eyni hesabda silindiyi üçün bağlandı.

## Universitet LMS-inin buluda köçürülməsi

Şərti vəziyyət: lms.unec.example yerli virtual maşında, tələbə reyestri özəl buludda; hədəf ictimai buludda idarə olunan tətbiq platforması, idarə olunan PostgreSQL və özəl obyekt saxlancıdır. Əvvəl asılılıqlar siyahıya alınır (kimlik provayderi, əlavələr, planlı tapşırıqlar, poçt, fayl yolları); lokal diskdə saxlanan sessiya nüsxələrin çoxalmasına mane olur. İstehsalat, sınaq, audit və bərpa ayrı sərhədlərdədir. Məsuliyyət matrisində hər iş üçün universitetdə icraçı, qərar sahibi və provayderin işi ayrılır; SOC auditin SIEM-ə ötürülməsində və insidentdə icraçıdır.

:::steps Köçürmənin dörd mərhələsi
[[step]]
title = "Təhlükəsiz baza mühiti"
body = "Hesablar, federasiya, audit arxivi, şəbəkə və xərc nəzarəti; resurslar IaC şablonlarından. Paneldən fövqəladə dəyişiklik sonradan kodla uyğunlaşdırılır, yoxsa növbəti yerləşdirmə onu geri çevirər."

[[step]]
title = "Sınaq"
body = "Şəxsiyyətsizləşdirilmiş məlumatla funksional və yük sınağı (şərti 2 000 paralel sessiya, real sorğu qarışığı). Mənfi sınaq: başqa kurs sənədi oxunmur, sınaq rolu istehsalat saxlancına çatmır, audit hadisəsi görünür."

[[step]]
title = "Sinxronlaşma və keçid"
body = "Yazıların dayandırılma anı və son fərq müəyyən edilir; paralel nəzarətsiz yazı ziddiyyət yaradır. Geri dönüş şərti əvvəl yazılır; DNS dəyişməsi məlumat sinxronlaşmasını həll etmir."

[[step]]
title = "Açılış və müşahidə"
body = "Səhv, gecikmə, rol dəyişiklikləri və xərc izlənir; nümunə kurs əməliyyatı, qorunan arxivdə sınaq hadisəsi və ayrıca mühitdə bərpa yoxlanır. Köhnə mühit yalnız qəbul və geri dönüş müddətindən sonra çıxarılır."
:::

Qəbul meyarları: icazə sərhədləri (icazəli və rədd olunan əməliyyatlar), şəxsi saxlancın anonim açılmaması, admin MFA və müvəqqəti rol, tam rol sessiyası ilə audit qeydi, ölçülmüş bərpa vaxtı və itki, kursun ixracı və alternativdə bərpası. Bunlar istismarın başlanğıcıdır, dövri yoxlanır.
