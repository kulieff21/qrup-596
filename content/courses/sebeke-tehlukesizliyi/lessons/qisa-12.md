+++
title = "SIEM və istifadəçi davranışlarının təhlili (UEBA)"
unit = "qisa"
order = 12
summary = "Mövzunun skeleti: hər anlayış bir sətirdə. SIEM axını, log mənbələri, qeydlər, korrelyasiya, UEBA, SOAR/XDR/SOC, ölçülər, tutum, məxfilik və praktiki iş."
updated = 2026-11-09

[[source]]
title = "Mühazirə 12: SIEM və istifadəçi davranışlarının təhlili (UEBA)"
note = "Elmar Cabbarov, 2026–2027"
+++

Hər anlayış bir sətirdə; izahlı variant orta və uzun səviyyədədir. Universitet nümunələri şərti tədris nümunəsidir.

## SIEM nədir

- **SIEM** (*Security Information and Event Management*): müxtəlif sistemlərin qeydlərini toplayıb vahid forma gətirən, əlaqələndirən, xəbərdarlıq yaradan və saxlayan sistem; termini 2005-ci ildə **Gartner** işlədib.
- **SIM** (uzunmüddətli saxlama, axtarış, hesabat) + **SEM** (real vaxt monitorinq, korrelyasiya) = SIEM.
- Nümunələr: Splunk, Microsoft Sentinel, IBM QRadar, Elastic Security, Wazuh (açıq mənbə).
- SIEM bir hesab və bir vaxt xətti üzərində VPN, AD, baza, proksi hadisələrini birləşdirir; təhlükəsizliyi **SOC** (Təhlükəsizlik Əməliyyatları Mərkəzi) təmin edir, sazlanmamış SIEM bahalı log arxividir.
- **Target**, 2013: xəbərdarlıq yaranmışdı, komanda vaxtında hərəkət etmədi, 40 milyon kartın məlumatı oğurlandı; xəbərdarlıq ilə reaksiya ayrı məsələdir.

## Əsas anlayışlar

| Anlayış | Mənası |
| --- | --- |
| Hadisə (event) | Qeydə alınan fəaliyyət |
| Jurnal qeydi (log entry) | Hadisəni təsvir edən saxlanılmış sətir |
| Xəbərdarlıq (alert) | Aşkarlama məntiqinin araşdırılmalı saydığı nəticə |
| İnsident (incident) | Təhlükəsizliyi pozan və ya real təhdid edən hadisə |
| TP / FP | Hücum var və xəbərdarlıq var / hücum yoxdur, amma xəbərdarlıq var (analitikin vaxtını alır) |
| FN / TN | Hücum var, SIEM susub (ən təhlükəlisi) / hücum yoxdur, SIEM susub |

## SIEM arxitekturası

- **Toplama:** agent (Wazuh agent, Splunk Universal Forwarder), syslog, API, kolektor; ötürmə TLS ilə qorunur, şəbəkə kəsiləndə bufer var, susan mənbə ayrıca izlənir.
- **Ayrışdırma (parsing):** xam sətirdən IP, istifadəçi, əməl çıxarılır.
- **Normallaşdırma:** fərqli adlı sahələr (`src_ip`, `srcaddr`, `IpAddress`) vahid sxemə düşür; sxemlər **ECS** (Elastic Common Schema) və **OCSF** (Open Cybersecurity Schema Framework), ötürmə protokolu deyillər.
- **Vaxt:** NTP ilə sinxron, UTC-də; hadisə vaxtı (**event time**) ilə qəbul vaxtı ayrıca saxlanır, gecikən hadisəni sabit 5 dəqiqəlik pəncərə buraxa bilər.
- **Zənginləşdirmə:** rol, aktiv, IP ölkəsi, təhdid kəşfiyyatı əlavə olunur.
- **Korrelyasiya və xəbərdarlıq:** qaydalar və modellər, nəticə SOC-a düşür.
- **Saxlama:** isti (**hot**) qat tez axtarış, ilıq (**warm**) daha ucuz, soyuq (**cold**) uzunmüddətli arxiv. PCI DSS tətbiq olunan mühitdə audit jurnalları üçün ən azı 12 ay (son 3 ay dərhal əlçatan); bu, bütün sistemlərə avtomatik aid deyil.
- **WORM** (bir dəfə yaz, çox oxu) silməni və dəyişdirməni məhdudlaşdırır; **heş zənciri (hash chain)** H_i = SHA-256(H_(i−1) || qeyd_i) sonradan dəyişməni aşkarlayır, son heşlər imzalanmış manifestdə saxlanır.
- Yerləşdirmə: **on-premises** (İT idarə edir, birbaşa nəzarət), **cloud-native** (provayder bir hissəni idarə edir, xərc izlənir), hibrid (kampus kolektorları + bulud analitikası).
- Komponentlər: **kolektor (collector)** qəbul edib ötürür, **indeksləyici (indexer)** axtarış üçün təşkil edir, **axtarış qovşağı (search head)** sorğunu indekslərə göndərir. Bufer: 200 hadisə/s × 500 bayt × 7 200 s = 720 MB. Deduplikasiya təkil hadisə identifikatoruna əsaslanır.

## Log mənbələri və formatları

| Mənbə | Sual |
| --- | --- |
| Firewall, VPN | Kim hara qoşulub? |
| AD, IAM | Hesab ələ keçirilibmi? |
| Əməliyyat sistemi | Host-da nə işə düşüb? |
| EDR | Zərərli proses/fayl davranışı varmı? |
| DNS, proksi (domen, URL) | C2 və məlumat çıxarılması varmı? |
| Verilənlər bazası (DB) | Həssas məlumat oxunubmu? |
| Bulud (CloudTrail) | Bulud hesabından sui-istifadə varmı? |
| DLP | Məlumat çıxırmı? |
| Tələ sistemi (honeypot) | Daxili skan varmı? |

- Hər şeyi toplamaq səhvdir: mənbə konkret aşkarlama sualına cavab verməlidir.
- **Syslog (RFC 5424)**: PRI = 8 × facility + severity (37 = 8 × 4 + 5: facility 4 auth, severity 5 notice). **CEF** (ArcSight) və **LEEF** (QRadar) sahələri standartlaşdırır.
- Ayrışdırma: müntəzəm ifadə (**regular expression**), **Grok** (adlandırılmış hazır şablonlar, Logstash). Sahənin çıxarılması dəyərin düzgünlüyü demək deyil; sahə doluluq faizi izlənir.
- ECS-ə uyğunlaşdırma: `ts` → `@timestamp`, `src` → `source.ip`, `result=failed` → `event.outcome` failure. İstifadəçi adı dəyişməz identifikator deyil, IAM identifikatoru götürülür.
- **NAT** arxasında çox istifadəçi bir IP ilə görünür; şəxsi tapmaq üçün hadisə vaxtına uyğun **DHCP** icarəsi lazımdır.

## Ən vacib qeydlər

| Event ID | Məna |
| --- | --- |
| 4624 / 4625 | Uğurlu giriş (Type 3 şəbəkə, 10 RDP) / uğursuz giriş (kobud güc, parol püskürtməsi) |
| 4648 | Ayrıca kimlik məlumatı ilə giriş cəhdi; daxili hərəkət |
| 4672 | Xüsusi imtiyazlar (admin girişi) |
| 4688 | Yeni proses; komanda sətri əlavə siyasətlə açılır |
| 4720 | Hesab yaradıldı: dayaqlanma (persistence) |
| 4728, 4732 | Qrupa üzv əlavə edildi: imtiyaz artımı (Subject edən, MemberSid əlavə olunan) |
| 4768, 4769 | Kerberos bileti: Kerberoasting |
| 1102 | Audit jurnalı təmizləndi: izlərin silinməsi |
| 7045 | Yeni xidmət: PsExec, dayaqlanma |

- Linux: `auth.log` (RHEL-də `secure`), **journald**, **auditd**. **Sysmon**: Event ID 1 proses, 3 şəbəkə, 11 fayl.
- 4688 Security, 7045 System, Sysmon ayrı kanaldadır; hamısı ayrıca toplanır. Qeydlər defolt yazılmır.
- Şərh: 4624 MFA keçdiyini sübut etmir; firewall `allow` təhlükəsiz demək deyil; proksi CONNECT 200 tunelin açıldığını göstərir, içini yox; DNS cavabı əlaqəni sübut etmir; CloudTrail-də `errorCode` yoxlanır.

## Korrelyasiya

| Növ | Mahiyyət və nümunə |
| --- | --- |
| Hədd (threshold) | Pəncərədə say həddi keçir: 10 dəqiqədə 20 uğursuz giriş |
| Ardıcıllıq (sequence) | A-dan sonra B: uğursuz girişlər, sonra uğurlu giriş |
| Çoxmənbəli | VPN girişi → imtiyazlı rol → baza ixracı → xaricə yükləmə |
| Kontekst əsaslı | Aktiv/rol ilə yoxlanır: tələbə hesabı maliyyə serverinə girir |
| Təhdid kəşfiyyatı | IoC siyahısı ilə tutuşdurma: bilinən C2 ünvanı |
| Yoxluq (absence) | Gözlənilən hadisə yoxdur: agent 30 dəqiqə susur |
| Statistik, davranış | Normadan kənarlaşma: ixrac 15 dəfə artıb |

- Konspekt zaman korrelyasiyasını da verir: müəllim hesabı gecə 03:00-da qiymətləri kütləvi dəyişir.
- Etibarlı hesabın sui-istifadəsi: ATT&CK T1078 (Valid Accounts); uğurlu giriş təhlükəsiz demək deyil.

:::exam Tələ
Hesab üzrə «10 uğursuz giriş» qaydası brute force-u (kobud güc) tutur, password spraying-i (parol püskürtməsi, MITRE ATT&CK T1110.003) tutmur: hər hesabda 1–2 cəhd olur. Qayda mənbə IP üzrə **fərqli hesabların sayını** götürməlidir (SPL və KQL-də nümunələr var, hədlər şərtidir).
:::

- **Sabit pəncərə (tumbling window)** vaxtı üst-üstə düşməyən hissələrə bölür, **sürüşən (sliding window)** hər anda əvvəlki intervalı götürür: 09:58-də 12 və 10:03-də 12 cəhd sabit pəncərələrdə həddi keçmir, sürüşəndə 24 cəhd görünür.
- **Sigma** məhsuldan asılı qayda formatıdır; çevrilmiş sorğu yoxlanmadan tətbiq edilmir.
- **Mümkünsüz səyahət** (*impossible travel*): iki uzaq ölkədən qısa fasilə ilə giriş; yanlış müsbət: korporativ VPN çıxışı.
- Hazır ssenarilər: kobud güc T1110.001, püskürtmə T1110.003, imtiyaz artımı T1098, izlərin silinməsi T1685.005 (köhnə T1070.001), yeni xidmət T1543.003, DNS tunelləmə T1071.004, C2 ilə çıxarma T1041. ATT&CK v19 (28 aprel 2026) Defense Evasion-ı Stealth (TA0005) və Defense Impairment (TA0112) taktikalarına ayırıb.
- **Aşkarlamanın kodla idarəsi (detection as code)**: qayda versiyalanır, sınaqdan keçir (sərhəd testi, **kölgə rejimi**, geri qaytarma). Qaydanı söndürmək FP-ni sıfırlayır, FN-ni artırır; istisna boşluq yaradır. Örtük: 20 ssenaridən 12-si tam yoxlanıbsa, 12 / 20 = 60%.
- Araşdırma ardıcıllığı: qeydlər, IP, MFA, cihaz, sonrakı fəaliyyət, istifadəçi ilə ayrı kanal, qərar (FP, dar istisna, insident), sübutun qeydi.

## UEBA

| | UBA (User Behavior Analytics) | UEBA (User and Entity Behavior Analytics) |
| --- | --- | --- |
| İzləyir | İstifadəçiləri | İstifadəçilər + cihaz, server, tətbiq, xidmət hesabı |
| Əlavə tutur | Oğurlanmış hesab, daxili təhdid | Yoluxmuş server, sui-istifadə olunan xidmət hesabı |

- Fərq alqoritmdə yox, obyekt dairəsindədir; maşın öyrənməsini UBA da işlədir.
- **Baza profili (baseline)**: iş saatı, cihaz, IP, tətbiq, həcm (30–90 gün tez-tez seçilir). Müqayisə: şəxsin öz tarixçəsi, **oxşar qrup (peer group)**, təşkilat.
- **Z-balı:** z = (x − μ) / σ. μ = 200 MB, σ = 50 MB, x = 500 MB → z = 6. Şəkildəki ayrı nümunə: μ ≈ 202, σ ≈ 29, x = 650 → z ≈ 15. Normal paylanma fərziyyəsi olmadan ehtimal çıxarılmır. **Persentil** (95-ci persentil həddi) və **MAD** (median əsaslı) böyük sıçrayışa davamlıdır. **Mövsümilik (seasonality)**: imtahan həftəsi adi həftə ilə müqayisə edilmir.
- **Anomaliya insident deyil**, araşdırma səbəbidir. **Risk balı:** R = 0,4A + 0,35K + 0,25S (A anomaliya, K təhlükə konteksti, S həssaslıq); A = 80, K = 60, S = 90 → 75,5. Bal ehtimal deyil, prioritetdir; eyni giriş üçün üç siqnal iki dəfə sayılmır; bal zamanla azalır.
- Anomaliya növləri: nöqtə, kontekst, kollektiv; konspektdə zaman, cihaz, həcm, resurs, ardıcıllıq, coğrafi.
- Maşın öyrənməsi: nəzarətsiz (*unsupervised*): **k-means**, **DBSCAN**, **Isolation Forest** (kənar nöqtə hücum etiketi deyil); nəzarətli üsul etiket tələb edir; qraf təhlili hesab-cihaz-resurs əlaqələrini göstərir; izah olunmayan model etibar qazanmır.
- **Konseptin sürüşməsi (concept drift)**: normal dəyişir; model yavaş uyğunlaşsa yanlış həyəcan artır, çox tez uyğunlaşsa hücumçunun davranışı norma olur (**low and slow**).
- **DLP** (*Data Loss Prevention*): həssas məlumatın çıxmasını aşkarlayır, dayandırır; şəbəkə (hərəkətdə), son qurğu (istifadədə), saxlama/bulud (sükunətdə); regex, barmaq izi, etiket, maşın öyrənməsi; TLS yoxlaması olmadan məhduddur, əvvəl izləmə rejimində.

## SOAR, XDR və SOC

| Sistem | Vəzifə |
| --- | --- |
| EDR | Son qurğuda davranışı izləyib cavab verir; yalnız qurğu, amma daha dərin |
| XDR | Bir neçə qatın telemetriyasını və cavabını birləşdirir; çox vaxt ekosistemə bağlı |
| UEBA | Davranış anomaliyası; SIEM-in modulu |
| SOAR | Playbook ilə araşdırma və cavabı avtomatlaşdırır |
| SOC | İnsanlar və proseslər |

- **SOAR** (*Security Orchestration, Automation and Response*): zənginləşdirmə, bilet, müvəqqəti bloklama; dağıdıcı addımlar üçün hədd, təsdiq, geri qaytarma lazımdır; əməliyyat idempotent olmalıdır (idempotentlik).
- **L1** ilkin baxış, **L2** dərin araşdırma, **L3** təhdid ovu (**threat hunting**) və yeni qaydalar. Misal LMS hesabı araşdırması: giriş → həssas qovluq → endirmə → xarici ötürmə; «MFA var» deyib bağlamaq olmaz.
- NIST SP 800-61 insident işini yönləndirir; Rev. 3 (aprel 2025) onu NIST CSF 2.0 funksiyalarına bağlayır (Govern, Identify, Protect, Detect, Respond, Recover). Konspektin dörd mərhələsi Rev. 2-yə aiddir. Jurnal üçün NIST SP 800-92.
- Köhnə slaydlarla fərq: z-balı nümunəsi ilə qrafik fərqli verilənlərdir; FPR = FP / (FP + TN), boş pay isə FP / (TP + FP); "Azure Sentinel" indi Microsoft Sentinel.

## Ölçülər və tutum

| Göstərici | Məna |
| --- | --- |
| MTTD | Hücumun başlanğıcından aşkarlanmaya orta vaxt |
| MTTR | Aşkarlanmadan aradan qaldırılmaya orta vaxt (tərif yazılmalıdır) |
| Dəqiqlik (precision) | TP / (TP + FP) |
| Tamlıq (recall) | TP / (TP + FN) |
| ATT&CK örtüyü, mənbə sağlamlığı | Aşkarlanan texnikaların payı; vaxtında gələn mənbələrin faizi |

- 100 xəbərdarlıq: 20 TP, 80 FP, 5 FN → dəqiqlik 20 / 100 = 20%, tamlıq 20 / 25 = 80%. **FPR** = FP / (FP + TN); TN yoxdursa hesablanmır (TN = 920 → 8%).
- **Xəbərdarlıq yorğunluğu:** çox FP analitiki real hücuma kor edir. Dəqiqliyi artırmaq tamlığı azalda bilər. Tamlığı idarə olunan testlər (**purple team**, **Atomic Red Team**) yoxlayır.
- MTTD: 8, 12, 25 dəq → 15 dəq; MTTR: 30, 50, 100 dəq → 60 dəq.
- Tutum **EPS** (*events per second*) ilə: 2000 EPS × 500 bayt = 1 MB/s = 86,4 GB/gün ≈ 7,8 TB 90 gündə (sıxılmadan, indeks və replikasız). İndeks, replika və 25% ehtiyatla ≈ 15,55 TB. Replika ehtiyat nüsxə deyil; pik yük ortadan yüksəkdir.

## Səhvlər, məxfilik, SIEM-in qorunması

- Tipik səhvlər: məqsədsiz toplama, saatların sinxron olmaması, yanlış ayrışdırma, hesabların qorunmaması, susan mənbələrə nəzarətsizlik, tənzimsiz hazır qaydalar, log silinməsinə qarşı müdafiəsizlik.
- UEBA balı intizam qərarı deyil; faktlar və səlahiyyətli insan qərar verir. Toplama məqsədi, sahələr, müddət siyasətdə yazılır; artıq məzmun çıxarılır.
- **Psevdonimləşdirmə** identifikatoru işarə ilə əvəz edir; sadə heş anonimlik vermir, **HMAC** lüğət hücumunu çətinləşdirir.
- SIEM hesabları MFA və ən az səlahiyyətlə qorunur, hüquqlar ayrılır, analitik baxışı audit olunur; log məzmunu etibarsızdır (sətirsonu, qaçışlama), SIEM çöksə bərpa planı var.

## Praktiki iş

Nigar hesabı: normal giriş, 7 uğursuz cəhd, yeni cihaz, kritik fayllar, kütləvi endirmə. Tələbə sxemə çevirir, hədd və ardıcıllıq qaydası yazır, UEBA ilə ən azı üç alternativ izah verir, faktı fərziyyədən ayırır. Bal: hazırlıq 20, korrelyasiya 25, profil 20, alternativlər 15, reaksiya və rəy 20.
