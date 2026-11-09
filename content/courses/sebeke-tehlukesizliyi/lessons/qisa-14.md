+++
title = "Bulud hesablamalarının əsasları və bulud təhlükəsizliyi"
unit = "qisa"
order = 14
summary = "Mühazirənin bütün anlayışları ən qısa formada: NIST modeli, ortaq məsuliyyət, IAM, şifrələmə, şəbəkə, konteyner, audit, vasitələr, bərpa, standartlar və iki insident."
updated = 2026-11-09

[[source]]
title = "Mühazirə 14: Bulud hesablamalarının əsasları və bulud təhlükəsizliyi"
note = "Elmar Cabbarov, 2026–2027"
+++

Bulud təhlükəsizliyinin əsas fikri: serverlər başqasının data mərkəzindədir, amma məlumatın, hesabların və konfiqurasiyanın məsuliyyəti əsasən müştəridə (universitetdə) qalır. Aşağıdakı misallar universitetin tədris idarəetmə sisteminə (Learning Management System, LMS) aiddir və şərti tədris nümunəsidir.

## Bulud hesablamaları nədir

Bulud hesablamaları (cloud computing) konfiqurasiya edilə bilən resursların ortaq hovuzuna şəbəkə vasitəsilə, tələbə uyğun və az idarəetmə səyi ilə giriş modelidir. NIST SP 800-145 beş xüsusiyyəti, üç xidmət modelini və dörd yerləşdirmə modelini müəyyən edir. "Şəbəkə üzərindən" deyilir, "İnternet üzərindən" yox: özəl bulud yalnız daxili şəbəkədən də əlçatan ola bilər. Başqasının server otağında sabit icarə bulud sayılmır.

| Xüsusiyyət | Mənası |
| --- | --- |
| Tələb üzrə özünəxidmət | Müştəri resursu provayder əməkdaşı olmadan panel və ya API ilə ayırır |
| Geniş şəbəkə girişi | Standart mexanizmlərlə müxtəlif cihazlardan giriş |
| Resursların hovuzlaşdırılması | Resurslar çox müştəri arasında bölünür: çoxicarəçilik (multi-tenancy), məntiqi izolyasiya hipervizor (hypervisor) və avtorizasiya ilə |
| Sürətli elastiklik | Tutum tələbə görə artır və azalır |
| Ölçülən xidmət | İstifadə ölçülür, ödəniş çox vaxt ona görədir |

- Elastiklik (elasticity) tələblə genişlənmə və daralma, miqyaslanma (scalability) artan yükü qarşılamaq qabiliyyətidir; şaquli miqyaslanma daha böyük maşın, üfüqi miqyaslanma çoxlu nüsxədir.
- İdarəetmə müstəvisi (control plane) resursları yaradan interfeysdir (panel, API), məlumat müstəvisi (data plane) tətbiqin gündəlik məlumat əməliyyatıdır; oğurlanmış idarəetmə hesabı ilə bütün baza silinə bilər.
- Elastik resurslar sonsuz deyil: kvota və büdcə var.

## Yerli infrastruktur, üstünlüklər və məhdudiyyətlər

Yerli infrastrukturda (on-premises) universitet server otağını və bütün qatları özü idarə edir; buluda keçid İT komandasının ləğvi deyil, iş bölgüsünün dəyişməsidir. Sınaq mühitində (keyfiyyət yoxlaması, Quality Assurance, QA) real tələbə məlumatı yox, şəxsiyyətsizləşdirilmiş məlumat işlədilir.

- **Üstünlüklər:** ilkin kapital xərci əvəzinə dəyişkən xərc, sürətli yerləşdirmə, qlobal əhatə; resurs bitəndə bağlanmalıdır, çünki dayandırılmış maşının diski ödəniş yarada bilər.
- **Məhdudiyyətlər:** əlaqə və xidmət fasiləsi, məxfilik riski, hücum səthi, məhdud texniki nəzarət, provayderə bağlılıq, dəyişkən xərc.
- Ümumi sahibolma xərci (Total Cost of Ownership, TCO) hesablama, saxlanc, trafik, lisenziya, dəstək, audit və əməyi əhatə edir; buludun həmişə ucuz və ya bahalı olması barədə universal qayda yoxdur.
- Xidmət səviyyəsi razılaşması (Service Level Agreement, SLA) ölçülən əlçatanlığı və öhdəlik pozulanda şərtləri təyin edir; kredit itirilmiş imtahanı bərpa etmir.

## Buludun yerləşdirmə modelləri

| Model | Tərif | Nümunə |
| --- | --- | --- |
| İctimai (public) | Provayderin infrastrukturu geniş ictimaiyyətə, resurslar məntiqi ayrılır | Microsoft 365, AWS |
| Özəl (private) | Yalnız bir təşkilat üçün; üçüncü tərəf də idarə edə bilər | Universitetin OpenStack/Proxmox buludu |
| İcma (community) | Ortaq tələbləri olan təşkilatlar qrupu üçün | Bir neçə universitetin tədqiqat buludu |
| Hibrid (hybrid) | Müstəqil qalan iki və ya daha çox bulud, daşınmanı mümkün edən texnologiya ilə əlaqələndirilir | Özəl bulud bazası + ictimai buludda əlavə tutum |

Çoxbuludlu istifadə (multi-cloud) bir neçə provayderdən istifadədir, NIST-in beşinci modeli deyil.

:::exam
"İctimai" xidmətin hamıya təklif olunması deməkdir, məlumatın hamıya açıq olması yox. Hibrid üç növün birləşməsi deyil. Özəl bulud mütləq öz İT şöbəsində olmur. "İctimai bulud özəldən bahadır" kimi universal sıralama yoxdur. Buluda keçmək riskləri autsorsinq etmək deyil.
:::

## Xidmət modelləri və ortaq məsuliyyət

| Model | Nə verir | Universitetdə qalan |
| --- | --- | --- |
| İnfrastruktur xidmət kimi (Infrastructure as a Service, IaaS), məsələn, Amazon EC2 | Virtual maşın, disk, şəbəkə | Qonaq ƏS, tətbiq, hesablar, məlumat |
| Platforma xidmət kimi (Platform as a Service, PaaS), məsələn, Azure App Service, Heroku | İdarə olunan icra mühiti | Kod, konfiqurasiya, hesablar, məlumat |
| Proqram təminatı xidmət kimi (Software as a Service, SaaS), məsələn, Microsoft 365 | Hazır tətbiq | Hesablar, MFA, rollar, paylaşma, məlumat |

Ortaq məsuliyyət (shared responsibility): provayder buludun təhlükəsizliyinə (security of the cloud: data mərkəzi, avadanlıq, hipervizor), müştəri buluddakı təhlükəsizliyə (security in the cloud: məlumat, hesablar, icazələr, konfiqurasiya) cavabdehdir. Məlumatın təsnifatı və hesablar bütün modellərdə müştəridədir; IaaS-da qonaq ƏS yamaqları da müştəridədir.

:::exam
Bulud insidentlərinin çoxu provayderin sındırılmasından yox, müştərinin səhv konfiqurasiyasından və oğurlanmış hesablardan baş verir. Ehtiyat nüsxə xidmətinin olması bərpanı yoxlamaq işini aradan qaldırmır.
:::

## Buludda təhdid modeli

Təhdid modeli (threat model) aktivləri, etibar sərhədlərini, hücumçunun imkanlarını və zərəri əlaqələndirir. Aktiv yalnız maşın deyil: tələbə bazası, imtahan sualları, idarəetmə tokeni, ehtiyat nüsxə və büdcə də aktivdir.

- Əsas risklər: səhv konfiqurasiya (açıq bucket, hər yerdən SSH), hesabın ələ keçirilməsi (MFA yox, root hesabı gündəlik işlədilir), sızmış açarlar, artıq icazələr, təhlükəsiz olmayan API-lər, məlumatın yeri, əlçatanlıq.
- Gizli İT (shadow IT) təsdiqlənməmiş SaaS istifadəsidir; hesablaşma uçotu, kimlik icazələri və şəbəkə müşahidəsi ilə aşkarlanır.
- İstifadəçinin kimliyi ilə tətbiq rolunun kimliyi qarışdırılmır; ikisi də dar saxlanır.

## Kimlik və girişin idarəsi

Kimlik və girişin idarəsi (Identity and Access Management, IAM) kimin nəyi edə biləcəyini müəyyən edir: autentifikasiya kimliyi yoxlayır, avtorizasiya icazəni qiymətləndirir.

| Anlayış | Qısa izah |
| --- | --- |
| Vahid giriş (Single Sign-On, SSO) | Kimlik provayderi (Identity Provider, IdP) ilə daxil olmaq; federasiya protokolları SAML və OpenID Connect |
| RBAC | Rol əsaslı giriş nəzarəti (Role-Based Access Control): icazə vəzifəyə bağlı |
| ABAC | Atribut əsaslı nəzarət (Attribute-Based Access Control): şöbə, etiket, mühit; etiketi dəyişmək hüququ da qorunur |
| Minimal səlahiyyət (least privilege) | Vəzifənin tələb etdiyi ən dar icazə; etibar siyasəti rolu kimin qəbul edə biləcəyini təyin edir |
| Açıq rədd (explicit deny) | AWS-də icazəni üstələyə bilər |
| MFA | Çoxfaktorlu autentifikasiya (Multi-Factor Authentication); adminlər üçün fişinqə davamlı FIDO2/passkey, oğurlanmış sessiya tokeni yenə risklidir |
| Əsas hesab (root account) | Gündəlik işlədilmir |
| PAM | İmtiyazlı girişin idarəsi (Privileged Access Management): müvəqqəti, just-in-time səlahiyyət |
| İş yükü kimliyi (workload identity) | Statik açar əvəzinə qısaömürlü token və rol |
| Sirlər seyfi | AWS Secrets Manager, Azure Key Vault; sızmış açar ləğv edilir, sadəcə silinmir |

## Məlumatların və açarların qorunması

Təsnifat: açıq, daxili, məxfi, ciddi məhdud; hər sinfin giriş qaydası və saxlama tədbiri var.

- Obyekt saxlancı (object storage) faylı obyekt kimi saxlayır, konteyner bucket adlanır; çətin təxmin edilən ad, ictimai siyasət, girişə nəzarət siyahısı (Access Control List, ACL) və imzalı keçid fərqli mexanizmlərdir. Hesab səviyyəsində ictimai giriş bloklanır.
- TLS ötürməni qoruyur (TLS 1.2 və 1.3); saxlanarkən şifrələmə diski qoruyur, amma yanlış avtorizasiyanı dayandırmır. Açıq saxlancın şifrəli olması məxfilik demək deyil.
- Açar idarəetmə xidməti (Key Management Service, KMS) açarın yaranması, icazələri və auditini verir. Zərf üsulu (envelope encryption): məlumat açarı (Data Encryption Key, DEK) məlumatı, açar şifrələmə açarı (Key Encryption Key, KEK) DEK-i qoruyur.
- Öz açarını gətirmə (Bring Your Own Key, BYOK) müştərinin açar materialını xidmətə gətirməsidir; aparat təhlükəsizlik modulu (Hardware Security Module, HSM) açarı aparatda qoruyur, ikisi də icazələri əvəz etmir.
- Məlumat sızmasının qarşısının alınması (Data Loss Prevention, DLP) həssas məzmunun icazəsiz ötürülməsini aşkarlayır və bloklayır.

## Bulud şəbəkəsinin təhlükəsizliyi

- Virtual özəl bulud (Virtual Private Cloud, VPC) və Azure-da Virtual Network (VNet) məntiqi şəbəkə sərhədidir; "özəl" ad qorunma deyil, ictimai IP və marşrut faktiki əlçatanlığı təyin edir.
- Qatlar: giriş, tətbiq, baza; istifadəçi yalnız giriş qatına HTTPS ilə gəlir, bazaya ictimai ünvan verilmir.
- Şəbəkə təhlükəsizlik qrupu (security group) trafik qaydalarıdır; AWS-də vəziyyəti izləyir (stateful), yalnız icazə verir; Azure NSG-də icazə və rədd var. 0.0.0.0/0 IPv4, ::/0 IPv6-nı açır. Açıq TCP 443 tətbiq icazəsi deyil.
- Özəl endpoint IAM-i əvəz etmir; NAT sızmanı dayandırmır; veb tətbiq firewall-u (Web Application Firewall, WAF) HTTP sorğularını süzür, DDoS müdafiəsi giriş qatını qoruyur, amma biznes avtorizasiyasını yox.
- AWS Direct Connect və Azure ExpressRoute defolt olaraq şifrələnmir; TLS və ya IPsec lazımdır. Hibrid rabitə VPN-dən də keçə bilər.

## Konteyner, serverless və təchizat zənciri

- Konteyner hostun nüvəsini paylaşır, kiçik olması təhlükəsiz etmir; kök istifadəçi, imtiyazlı rejim və yazma icazəli host qovluğu izolyasiyanı zəiflədir. Kubernetes-də ad məkanı (namespace) tək başına güclü sərhəd deyil. Obraz kriptoqrafik heşi (digest) ilə seçilir, skan olunur; NIST SP 800-190 konteyner, NIST SP 800-125 virtuallaşdırma mənbəyidir.
- Serversiz hesablama (serverless computing) server istismarını gizlədir; funksiya xidmət kimi (Function as a Service, FaaS) bunun formasıdır. Riskləri: artıq rol, təkrar hadisə (həll: idempotency, yəni təkrar əməliyyatın əlavə nəticə verməməsi), müvəqqəti diskdə qalıq məlumat; gec işə düşmə (cold start) cavab müddətinə təsir edir.
- Proqram təchizat zənciri (software supply chain) kod, asılılıq, qurma, reyestr və yerləşdirməni əhatə edir; CI/CD (Continuous Integration and Continuous Delivery) səlahiyyəti qorunur. SBOM (Software Bill of Materials) komponent siyahısıdır; imza mənşəyi göstərir, kodun təhlükəsizliyini yox. OWASP Top 10:2025-də A03 bu sahədir.

## Audit qeydləri, monitorinq və insidentə cavab

| Mənbə | Nəyi göstərir |
| --- | --- |
| AWS CloudTrail | API və hesab fəaliyyəti; obyekt oxunuşu üçün data events ayrıca seçilir |
| Azure Activity Log | İdarəetmə müstəvisində abunə fəaliyyəti |
| Entra, Google Cloud Audit Logs | Kimlik girişləri; idarəetmə və seçilən məlumat qeydləri |
| Şəbəkə axın qeydləri, LMS, baza qeydləri | Metadata; tətbiq və sorğu əməliyyatları |

AWS CloudWatch metrik və log, AWS Config konfiqurasiya uyğunluğu, Amazon Inspector zəiflik aşkarlayır. Təhlükəsizlik məlumatı və hadisələrinin idarəsi sistemi (Security Information and Event Management, SIEM) qeydləri əlaqələndirir. Qeyd yazılmayıbsa, sonradan yaranmır. Audit arxivi ayrı hesabda, silinmədən qorunmaqla saxlanır. İnsidentdə zərər dayandırılır və sübut qorunur, maşını dərhal silmək olmaz; NIST SP 800-61 Rev. 3 cavabı risk idarəetməsi ilə əlaqələndirir.

## CSPM, CWPP, CASB və CNAPP

| Sinif | Sual |
| --- | --- |
| Bulud təhlükəsizlik vəziyyətinin idarəsi (Cloud Security Posture Management, CSPM) | Konfiqurasiya tələbə uyğundurmu? İnfrastruktur kod kimi (Infrastructure as Code, IaC) şablonları yoxlayır, configuration drift-i tapır |
| Bulud iş yüklərinin qorunması platforması (Cloud Workload Protection Platform, CWPP) | İş yükünün özündə zəiflik və şübhəli proses varmı? |
| Bulud giriş təhlükəsizliyi vasitəçisi (Cloud Access Security Broker, CASB) | SaaS-dan kim necə istifadə edir? |
| Bulud əsaslı tətbiqlərin qorunması platforması (Cloud-Native Application Protection Platform, CNAPP) | Koddan icraya qədər risklər necə əlaqələnir? |

## Əlçatanlıq, ehtiyat nüsxə və bərpa

- Region coğrafi sahə, əlçatanlıq zonası (Availability Zone, AZ) region daxilində nasazlığı ayırır; iki maşın avtomatik ayrı zonada deyil.
- Yüksək əlçatanlıq (high availability) komponent düşəndə xidməti saxlayır, fəlakətdən bərpa (disaster recovery) böyük nasazlıqdan sonra qaytarır. Replikasiya səhv silinməni də çatdırır, ehtiyat nüsxə isə sağlam keçmişə qaytarır.
- Bərpa nöqtəsi hədəfi (Recovery Point Objective, RPO) qəbul edilən məlumat itkisi pəncərəsidir; bərpa vaxtı hədəfi (Recovery Time Objective, RTO) qəbul edilən dayanma müddətidir. Nümunə: son nüsxə 09:45, insident 10:00, bərpa 11:30 olarsa, itki 15 dəqiqə, dayanma 90 dəqiqədir; bunlar nəticədir, hədəf deyil.
- Ehtiyat nüsxələr ayrı hesabda, ayrı icazələrlə və dəyişməz (immutability) saxlanır; bərpa sınağı fayl-baza uyğunluğunu, DNS-i və açarı da yoxlayır.

## Standartlar, məlumatın yerləşməsi və çıxış strategiyası

- Sertifikat universitetin öz konfiqurasiyasının düzgünlüyünü sübut etmir.
- CSA Cloud Controls Matrix (CCM) v4.1: 17 sahədə 207 nəzarət. ISO/IEC 27001 idarəetmə sistemi tələbləri, 27002 nəzarət tövsiyələri, 27017 bulud nəzarətləri, 27018 ictimai buludda fərdi məlumat.
- NIST CSF 2.0 altı funksiya: Govern (idarə et), Identify (müəyyən et), Protect (qoru), Detect (aşkar et), Respond (cavab ver), Recover (bərpa et).
- Məlumatın yerləşməsi (data residency) məlumatın harada saxlandığıdır (ehtiyat nüsxə və loglar da); məlumat suverenliyi (data sovereignty) hüquqi yurisdiksiyadır.
- Provayderə bağlılıq (vendor lock-in) köçün çətinləşməsidir; çıxış strategiyası (exit strategy) müqavilə bitməmiş hazırlanır, ixrac alternativdə bərpa ilə sınanır.

## İki insident və LMS-in köçürülməsi

- **Capital One, 2019:** SSRF (Server-Side Request Forgery) müvəqqəti rol məlumatlarına çıxış verdi və saxlanc oxundu; dərs: sorğu imkanını daralt, rolu dar saxla, IMDSv2 kimi metadata qoruması işlət.
- **Snowflake, 2024 (Mandiant UNC5537):** oğurlanmış kimlik məlumatları və MFA-sız müştəri hesabları; platformanın sındırılması deyil.
- **Code Spaces (2014):** admin hesabı və ehtiyat nüsxələr eyni hesabda silindi, şirkət bağlandı.
- **LMS köçürülməsi:** asılılıqların siyahısı, dörd mərhələ (təhlükəsiz baza, sınaq, məlumat sinxronlaşması və keçid, açılış), qəbul sübutları (anonim sorğu rədd, MFA, audit, ölçülmüş bərpa, ixrac). Məsuliyyət matrisində SOC auditi SIEM-ə ötürür.
