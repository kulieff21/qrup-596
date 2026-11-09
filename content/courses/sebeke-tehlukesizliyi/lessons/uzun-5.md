+++
title = "Kibermüdafiə modelləri"
unit = "uzun"
order = 5
summary = "Mühazirə tam həcmdə: Cyber Kill Chain, Unified Kill Chain, Diamond Model, ATT&CK, Pyramid of Pain, D3FEND, NIST CSF 2.0, çoxsəviyyəli müdafiə, sıfır etibar və fidyə proqramı insidentinin bütün modellərlə təhlili."
updated = 2026-11-09

[[source]]
title = "Mühazirə 5: Kibermüdafiə modelləri"
note = "Elmar Cabbarov, 2026–2027"
+++

Hücumu təsvir etmək üçün ortaq dil lazımdır. Cyber Kill Chain hücumun mərhələlərini, Unified Kill Chain içəri girdikdən sonra baş verənləri, Diamond Model iştirakçılar arasındakı əlaqələri, ATT&CK konkret davranışı adlandırır. Bu mühazirənin məqsədi model adlarını əzbərləmək deyil: hücumu mərhələlərə ayırmaq, müşahidəni fərziyyədən seçmək, ATT&CK texnikasını telemetriya ilə əlaqələndirmək və seçilən tədbiri yoxlama üsulu ilə birlikdə təqdim etməkdir. Hansı modelin hansı suala cavab verdiyini bilmək əsas bacarıqdır.

## Kibermüdafiə modelinə nə üçün ehtiyac var

### Bir hadisəyə müxtəlif baxışlar

Poçt şlüzü şübhəli əlavə tapır, VPN uğurlu giriş yazır, fayl serverində çoxlu sənəd dəyişir. Bu qeydlər əlaqəli ola bilər, ayrı vaxtlarda baş vermiş adi fəaliyyət də ola bilər. Komanda hər qeydi eyni ağırlıqda qəbul etsə, lazımsız araşdırmalar çoxalır; hamısını təsadüf saysa, əlaqəli hücum qaçır. Model müşahidələri müəyyən suallar ətrafında düzmək üçün sadələşdirilmiş təsvirdir.

Kibermüdafiə modeli hücumun, müdafiənin və ya riskin seçilmiş tərəflərini göstərən anlayışlar sistemidir. O, konkret antivirus və ya firewall deyil: hansı məlumatı axtarmağı, hadisələri necə əlaqələndirməyi və qərarı necə əsaslandırmağı istiqamətləndirir. Hər model bəzi detalları saxlayır, digərlərini kənarda qoyur; bu seçim həm faydasını, həm məhdudiyyətini yaradır.

| Model | Nəyi göstərir |
| --- | --- |
| Cyber Kill Chain | hadisənin hücum yolunda yerini |
| Diamond Model | iştirakçı və vasitələr arasındakı əlaqəni |
| ATT&CK | müşahidə olunan davranışa ümumi ad verir |
| NIST CSF 2.0 | universitetin bu riskə görə hansı qərarları verməli olduğunu təşkil edir |

Birini o birinin əvəzinə işlətmək səhv sual verməyə səbəb olur: ATT&CK cədvəlindən büdcə və məsul şəxs çıxmır, CSF funksiyasından konkret aşkarlama qaydası alınmır.

| Səviyyə | Verilən sual | Universitetdən nümunə |
| --- | --- | --- |
| Strateji | Hansı zərəri qəbul edə bilərik? | İmtahan həftəsində LMS-in dayanma həddi |
| Əməliyyat | Hansı fəaliyyət yolu izlənir? | Kafedra cihazından fayl serverinə keçid |
| Taktiki və texniki | Hansı üsul və hansı sübut var? | İcazəsiz planlaşdırılmış tapşırıq və proses qeydi |
| Arxitektura | Keçidi hansı sərhəd dayandırmalıdır? | Yataqxana Wi-Fi-sından idarəetmə şəbəkəsinə qadağa |

### Sübut, fərziyyə və kəşfiyyat

- **Hadisə (event)** sistemdə baş verən fəaliyyətdir; jurnal qeydi onun saxlanmış təsviridir.
- **Xəbərdarlıq (alert)** bir qaydanın araşdırılmalı saydığı nəticədir.
- **İnsident** təhlükəsizliyi pozan və ya real təhdid edən haldır.

Poçt şlüzünün xəbərdarlığı araşdırmaya başlamaq üçün əsas ola bilər, amma kompüterdə zərərli proqramın işlədiyini öz-özünə sübut etmir.

**Təhdid kəşfiyyatı (threat intelligence)** qərar verməyə yarayan, mənbəsi və məhdudiyyətləri qiymətləndirilmiş təhdid məlumatıdır. Sadəcə IP siyahısı son məhsul deyil: ünvanların hansı xidmətlə əlaqəli olduğu, nə vaxt müşahidə edildiyi və indi kimə məxsus ola biləcəyi də araşdırılır. Köhnəlmiş ünvanı bloklamaq kitabxananın qanuni xidmətini dayandıra bilər.

**Kəşfiyyata əsaslanan müdafiə (intelligence-driven defense)** əvvəl məlumat tələbini müəyyən edir, uyğun mənbələri toplayıb təhlil edir və nəticəni tədbirə çevirir. Kitabxana üçün tələb: oğurlanmış hesabla abunə bazalarından kütləvi endirməni erkən görmək; bunun üçün autentifikasiya qeydləri, sorğu həcmi, hesab rolu və normal iş rejimi lazımdır. Geri əlaqə də var: verilən məlumat qərarı dəyişmirsə, tələb və mənbə seçimi yenidən baxılır.

| Səviyyə | Şərti müşahidə | Yazıla bilən nəticə |
| --- | --- | --- |
| Müşahidə | Şlüz əlavəni karantinə alıb | Bu nüsxənin çatdırılması bloklanıb |
| Fərziyyə | Eyni hesab üzrə yad giriş cəhdi var | İki fəaliyyət əlaqəli ola bilər |
| Təsdiqlənmiş nəticə | Əlavənin açılması və yaratdığı proses qeydə alınıb | Həmin cihazda icra baş verib |
| Naməlum sahə | Cihaz jurnalı toplanmayıb | İcranın olub-olmadığı müəyyən edilməyib |

“Əlamət yoxdur” ifadəsi mənbənin görmə imkanına bağlıdır: proses auditi açılmayıbsa, proses qeydinin olmaması arxayınlıq vermir. Vaxtın düzgünlüyü də yoxlanır; şlüzün saatı irəlidədirsə, real ardıcıllıq yanlış görünə bilər. Analitik hadisə vaxtını, qeydin qəbul vaxtını, mənbəni və vaxt qurşağını saxlayır. Əsaslandırılmış nəticə üçün bütün təpələri və fazaları zorla doldurmaq lazım deyil.

:::exam
Müşahidəni, fərziyyəni və təsdiqlənmiş nəticəni ayır. Nümunə: şlüz əlavəni bloklayıbsa, təsdiqlənən yalnız çatdırılmanın bloklanmasıdır; “kompüter yoluxub” fərziyyədir, “heç nə olmayıb” isə EDR susduğu üçün də sübut deyil.
:::

## Cyber Kill Chain

### Mənşə və əsas fərziyyə

Lockheed Martin tədqiqatçıları Eric Hutchins, Michael Cloppert və Rohan Amin 2011-ci ildə kəşfiyyata əsaslanan müdafiəni Cyber Kill Chain ilə izah etdilər. Model hərbi hədəfləmə zənciri fikrini kompüter şəbəkəsinə müdaxiləyə tətbiq edir; ilkin diqqət qabaqcıl davamlı təhdidlərə (advanced persistent threat, APT) və məqsədli müdaxilələrə yönəlmişdi. Yeddi mərhələ hazırlıqdan hücumçunun məqsədinə qədər bir yolu təsvir edir.

Əsas müdafiə fikri: konkret hücum yolu üçün zəruri addım dayandırılsa, həmin yol məqsədə çatmır. Bu, bütün kampaniyanın bitməsi demək deyil; hücumçu başqa hesab, başqa məktub və başqa xidmət sınaya bilər. Ona görə “zənciri qırdıq” hökmündə hansı cəhdin və hansı sübut əsasında dayandırıldığı göstərilməlidir. Universitet bir zərərli əlavəni blokladıqdan sonra eyni məktubun başqa ünvanlara gedən nüsxələrini də axtarır.

:::figure
src = "m05-1.png"
alt = "Yuxarıda Cyber Kill Chain-in yeddi mərhələsi oxlarla bağlanıb: Kəşfiyyat, Silahlanma, Çatdırılma, İstismar, Quraşdırma, İdarəetmə (C2), Məqsədə çatma. Aşağıda Unified Kill Chain-in üç hissəsi: In, Through, Out."
caption = "Cyber Kill Chain mərhələləri və Unified Kill Chain-in üç hissəsi. Oxlar analitik yolu göstərir; real fəaliyyətdə təkrarlar mümkündür."
wide = true
:::

### Yeddi mərhələ və hər mərhələdə müdafiə

:::tip Mərhələlərin sırası
Kəşfiyyat → Silahlanma → Çatdırılma → İstismar → Quraşdırma → C2 → Məqsəd. İngiliscə: Recon, Weaponize, Deliver, Exploit, Install, C2, Act. Nə qədər erkən mərhələdə dayandırsan, ziyan bir o qədər az olur.
:::

**1. Kəşfiyyat (reconnaissance)** hədəf haqqında ilkin məlumatın toplanmasıdır: kafedra saytından əməkdaş ünvanları, açıq sənəddən proqram adı, xarici xidmətdən server ünvanı. Açıq mənbə məlumatlarının toplanması (OSINT) çox vaxt universitetin öz jurnalına düşmür. Aktiv skan görünə bilər, amma hər skan məqsədli hücumun sübutu deyil. Müdafiəçi açıq məlumatın tərkibini yoxlayır, lazımsız texniki detalların yayılmasını azaldır, açıq xidmətlərin inventarını aparır. İctimai məlumatı tam gizlətmək universitetin işi ilə uyğun gəlmir; seçici nəzarət lazımdır.

**2. Silahlanma (weaponization)** hücum vasitəsinin hazırlanmasıdır: zəiflikdən istifadə edən kodun zərərli yüklə birləşdirilməsi (məsələn, saxta seminar sənədi). Hazırlıq hücumçunun mühitində gedir və yerli sensor onu birbaşa görmür. Müdafiəçi təhlil edilmiş nümunələrdən, etibarlı kəşfiyyat hesabatlarından və özündə tapılmış fayldan hazırlığın xüsusiyyətlərini öyrənə bilər; lakin sonradan əldə edilmiş fayl onun nə vaxt hazırlandığını göstərmir.

**3. Çatdırılma (delivery)** vasitənin hədəfə ötürülməsidir: fişinq məktubu, yoluxdurulmuş daşıyıcı, istifadəçilərin baş çəkdiyi səhifə. Poçt şlüzü təhlükəli əlavə növlərini məhdudlaşdırır, keçidləri qiymətləndirir, karantinə alınan məktubları qeyd edir; veb proksi də nəzarət nöqtəsidir. SPF, DKIM və DMARC domen saxtalaşdırılmasının müəyyən formalarını azaldır, amma qanuni hesabdan göndərilmiş zərərli məktubu mütləq dayandırmır. İstifadəçiyə şübhəli məktubu rahat bildirmək imkanı verilməlidir.

**4. İstismar (exploitation)** zəiflikdən istifadə etməklə nəzərdə tutulan icraya və ya girişə nail olmaqdır. İstifadəçinin təhlükəli faylı işə salması da ümumi hücum hekayəsində icraya keçiddir, amma hər halda proqram zəifliyinin istismar edildiyini yazmaq düzgün deyil. Yamaq, təhlükəli məzmunun icrasına məhdudiyyət, istismar əleyhinə yaddaş tədbirləri (DEP/ASLR) və son qurğuda aşkarlama və cavab sistemi (EDR) müxtəlif səbəblərə müdaxilə edir; konkret səbəb müəyyənləşdirilməlidir, çünki yamaq istifadəçinin könüllü işlətdiyi skripti dayandırmır.

**5. Quraşdırma (installation)** hücum vasitəsinin yerləşdirilməsi və çox vaxt davamlı girişin yaradılmasıdır: iş stansiyasında icazəsiz xidmət və ya planlaşdırılmış tapşırıq. Faydalı tədbirlər: minimum hüquq, proqramların icrasına icazə siyahısı, dəyişiklik monitorinqi. Faylın diskə yazılması, prosesin işləməsi və yenidən başladıqdan sonra qalması fərqli sübutlardır; hər zərərli proses davamlılıq yaratmır. Yalnız yaddaşda işləyən fəaliyyət ayrıca fayl quraşdırılmadan da baş verə bilər.

**6. Komanda və idarəetmə (command and control, C2)** hücumçunun mühiti ilə ələ keçirilmiş sistem arasındakı əlaqədir; məsələn, LMS administratorunun cihazından xarici veb xidmətinə periodik sorğular. DNS, proksi və şəbəkə əlaqə qeydləri proses telemetriyası ilə birləşdirilir. Şifrələmə məzmunu gizlədir, amma istiqamət, vaxt və proses yenə faydalıdır. Sadəcə HTTPS işlənməsi əlaqəni qanuni etmir. Çıxışın icazəli xidmətlərlə məhdudlaşdırılması və cihazın təcridi idarəetmə kanalını kəsə bilər.

**7. Məqsədə yönəlmiş hərəkətlər (actions on objectives)** hücumçunun son texniki nəticəyə yönələn fəaliyyətidir: tələbə bazasının oğurlanması, qiymətlərin dəyişdirilməsi, fidyə proqramı ilə şifrələmə. Məlumat sızmasının qarşısının alınması (DLP), seqmentasiya, yazma hüquqlarının məhdudlaşdırılması və qorunan ehtiyat nüsxələr zərərin müxtəlif hissələrinə təsir edir. Ehtiyat nüsxə məxfiliyi bərpa etmir: oğurlanmış məlumat artıq kənardadır; ona görə şifrələmə ilə məlumat çıxarılması ayrıca araşdırılır.

| Mərhələ | Universitetdə mümkün əlamət | Qabaqlayıcı tədbir | Aşkarlama və cavab |
| --- | --- | --- | --- |
| Kəşfiyyat | Açıq LMS xidmətinin skanı | Lazımsız xidməti bağlamaq | Skanı qeyd edib konteksti yoxlamaq |
| Silahlanma | Əldə edilmiş zərərli sənəd | Təhlükəli icra imkanını azaltmaq | Nümunəni təcrid olunmuş təhlilə vermək |
| Çatdırılma | Saxta təqaüd məktubu | Poçt süzgəci və əlavə siyasəti | Nüsxələri tapıb karantinə almaq |
| İstismar | Sənəd açıldıqdan sonra icazəsiz icra | Yamaq və icra məhdudiyyəti | Proses ağacını yoxlayıb cihazı təcrid etmək |
| Quraşdırma | İcazəsiz tapşırıq və ya xidmət | Minimum hüquq, icazə siyahısı | Davamlılıq dəyişikliklərini araşdırmaq |
| C2 | Yad ünvana təkrarlanan əlaqə | Nəzarətli çıxış və proksi | Əlaqəni proseslə bağlayıb dayandırmaq |
| Məqsəd | Kütləvi ixrac və fayl dəyişməsi | Ayrı seqment, məhdud hüquq, nüsxə | İxracı yoxlamaq, yayılmanı kəsmək, bərpa etmək |

### Fəaliyyət variantları matrisi

Fəaliyyət variantları matrisi (courses of action matrix) mərhələ ilə müdafiə təsirini kəsişdirir. Hər mərhələ üçün altı təsir növü mümkündür, amma hər hüceyrəni doldurmaq məcburi deyil. Məsələn, universitet hücumçunun kompüterində hazırlanan faylı öz sensoru ilə müşahidə etmirsə, silahlanma üçün yerli aşkarlama imkanını varmış kimi göstərə bilməz.

| Variant | Mənası | Universitet nümunəsi |
| --- | --- | --- |
| Aşkarla (detect) | Fəaliyyəti müşahidə edib tanımaq | LMS cihazından şübhəli C2 əlaqəsini tapmaq |
| Rədd et (deny) | Tələb olunan imkanı verməmək | Poçtda zərərli əlavəni buraxmamaq |
| Poz (disrupt) | Davam edən fəaliyyəti kəsmək | Yoluxmuş kafedra cihazını təcrid etmək |
| Zəiflət (degrade) | Fəaliyyətin səmərəsini azaltmaq | Riskli ixracın sürətini məhdudlaşdırmaq |
| Aldat (deceive) | Saxta resursla davranışı üzə çıxarmaq | İstifadə olunmayan tələ hesabına cəhdi görmək |
| Məhv et (destroy) | Zərərli imkanı aradan qaldırmaq | Öz sistemində zərərli yükü təhlükəsiz silmək |

“Məhv et” universitetdən kənar sistemlərə qarşı cavab hücumuna icazə demək deyil: nümunə universitetin idarə etdiyi cihazdakı zərərli vasitənin aradan qaldırılmasıdır. Sübut üçün faylın nüsxəsi və heşi (hash) əvvəl qorunur. Tələyə yönəltmə də real məlumatı təhlükəyə atmaq hesabına aparılmır; saxta resurs ayrıca izolyasiya olunur.

### Modelin tənqidi və düzgün istifadəsi

Gücü sadə ünsiyyətdir: rəhbərliyə poçt süzgəcinin nəyi dayandırdığını və niyə daxili nəzarətin yenə lazım olduğunu göstərmək asandır. Eyni sadəlik daxili fəaliyyəti çox ümumiləşdirir: imtiyaz artırma, parol əldə etmə və serverlər arasında keçid çox vaxt son mərhələnin içində qalır.

Xətti təsvir də ehtiyatla oxunmalıdır. Hücumçu başqa cihaza keçə, yenidən kəşf apara, əvvəlki mərhələni təkrarlaya bilər. Oğurlanmış VPN hesabı, bulud sessiyası və daxili əməkdaşın sui-istifadəsi klassik zərərli fayl yoluna sığmır. Sistemin qanuni alətlərindən sui-istifadə (living off the land) ayrıca zərərli proqram quraşdırılmadan da məqsədə çatdıra bilər.

:::warning
Bloklanmış məktub yalnız həmin çatdırılma yolunun nəticəsini göstərir. “Bütün hücum dayandırılıb” demək üçün başqa nüsxələr, hesab girişləri və cihaz fəaliyyəti də yoxlanmalıdır. EDR-in susması onun işləkliyi və görmə sahəsi yoxlanmadan təhlükəsizlik sübutu sayılmır.
:::

Erkən müdaxilə adətən sonrakı zərərin qarşısını alır, amma həmişə ən ucuz tədbir deyil: həddən artıq sərt poçt qaydası imtahan sənədlərini də saxlaya bilər. Seçimdə xidmətin fasiləsizliyi, yanlış bloklama və cavab imkanı nəzərə alınır.

:::exam Tələ: klassik fərziyyə qanun deyil
“Hücumçu bütün mərhələlərdən ardıcıl keçməlidir, istənilən həlqəni qırmaq hücumu dayandırır” klassik modelin fərziyyəsidir, qanun deyil. Hücumçu mərhələ buraxa, başqa yol seçə, yenidən cəhd edə bilər; bir cəhdin bloklanması kampaniyanın bitdiyi demək deyil. Model perimetrə və zərərli proqrama yönəlib; daxili təhdidi, oğurlanmış parolla girişi, living off the land və yanal hərəkəti zəif təsvir edir.
:::

## Unified Kill Chain

### Yaranma səbəbi və quruluş

Paul Pols 2017-ci ildə Unified Kill Chain (UKC) yanaşmasını təqdim etdi. Model Cyber Kill Chain-in hücum yolu təsvirini ATT&CK-dan gələn davranış detalları ilə birləşdirir və genişləndirir. Onu Cyber Kill Chain ilə Diamond Model-in sadə birləşməsi adlandırmaq dəqiq deyil; Diamond əlaqələri təsvir edən ayrıca modeldir və UKC təhlilinə qoşula bilər.

UKC-də 18 faza üç hissədə toplanır:

- **In** ilkin dayağın əldə edilməsinə (sızma),
- **Through** daxili mühitdə mövqenin genişlənməsinə (şəbəkədə yayılma),
- **Out** məqsədə yönəlmiş nəticələrə (hədəfə çatma) aiddir.

Bölgü fiziki paketlərin mütləq “girməsi və çıxması” demək deyil: Out hissəsindəki təsir universitetin daxilində qalan qiymət bazasının pozulması ola bilər. Məlumatın çıxarılması hər hücumda baş vermir. Fazaların siyahısı da məcburi sıra deyil: icra imtiyaz artımından əvvəl də ola bilər, kəşf yeni serverə keçdikcə təkrarlana bilər. Analitik modelin sıra nömrəsini hadisənin vaxtı ilə qarışdırmır; faktiki vaxt xətti ayrıca saxlanılır.

| № | Hissə | Faza | Universitetdə şərti nümunə |
| --- | --- | --- | --- |
| 1 | In | Kəşfiyyat (Reconnaissance) | Açıq kafedra səhifəsindən hesab adları toplanır |
| 2 | In | Resurs hazırlığı (Resource Development) | Saxta seminar səhifəsi və göndərmə hesabı hazırlanır |
| 3 | In | Çatdırılma (Delivery) | Əməkdaşa zərərli keçid göndərilir |
| 4 | In | Sosial mühəndislik (Social Engineering) | Təcili qeydiyyat bəhanəsi ilə istifadəçi aldadılır |
| 5 | In | İstismar (Exploitation) | Açıq xidmətdə zəiflikdən istifadə edilir |
| 6 | In | Davamlılıq (Persistence) | Cihazda icazəsiz planlaşdırılmış tapşırıq yaradılır |
| 7 | In | Müdafiədən yayınma (Defense Evasion) | Zərərli fayl qanuni adla gizlədilir |
| 8 | In | Komanda və idarəetmə (Command and Control) | Cihaz xarici idarəetmə ünvanına bağlanır |
| 9 | Through | Körpü yaratma (Pivoting) | Ələ keçirilmiş cihazdan daxili zonaya tunel qurulur |
| 10 | Through | Daxili kəşf (Discovery) | Fayl serverləri və domen qrupları axtarılır |
| 11 | Through | İmtiyazların artırılması (Privilege Escalation) | Adi hesab daha geniş yerli hüquq qazanır |
| 12 | Through | İcra (Execution) | Başqa serverdə hücumçu əmri işləyir |
| 13 | Through | Kimlik məlumatlarına giriş (Credential Access) | Xidməti hesabın sirri əldə edilir |
| 14 | Through | Yanal hərəkət (Lateral Movement) | Həmin hesabla fayl serverinə keçilir |
| 15 | Out | Toplama (Collection) | Tələbə sənədləri bir qovluqda toplanır |
| 16 | Out | Məlumatın çıxarılması (Exfiltration) | Toplanmış arxiv xarici ünvana ötürülür |
| 17 | Out | Təsir (Impact) | Paylaşılmış fayllar şifrələnir |
| 18 | Out | Məqsədlər (Objectives) | Universitetdən ödəniş tələb etməyə cəhd edilir |

Burada 2-ci faza “Resurs hazırlığı” adlanır; köhnə təsvirlərdə “Silahlanma” adına rast gəlmək olar. Yeni ad yalnız zərərli fayl hazırlığını deyil, hesab, domen və digər hücum resurslarını da əhatə edir. Təsir fazası üçün köhnə “Target Manipulation” adı da mənbələrdə qala bilər. UKC-dəki “Defense Evasion” adı ATT&CK versiyasındakı ad dəyişiklikləri ilə avtomatik yenilənmir; iki təsnifatın versiyaları ayrı izlənir.

### In, Through və Out üzrə araşdırma

**In.** Əsas sual ilkin girişin həqiqətən baş verib-verməməsidir. Keçidin göndərilməsi, açılması və hesaba yad şəxsin daxil olması üç ayrı nəticədir: poçt qeydi birincini, proksi ikinciyə aid bağlantını, autentifikasiya qeydi üçüncünü dəstəkləyə bilər. Uğurlu girişdə də bunun istifadəçinin öz fəaliyyəti olub-olmadığı yoxlanır. Resurs hazırlığı universitetdən kənarda baş verdiyindən “müşahidə olunmayıb” düzgün cavabdır.

**Through.** Bir cihazdan bütün mühitə baxmağa məcbur edir. İş stansiyasında tapılmış xidmət hesabı fayl serverində də qəbul edilirsə, yerli yoluxma daha geniş girişə çevrilir. Analitik hesabın hansı sistemlərdə işləndiyini, hansı hüquqları qazandığını və hansı sərhədlərdən keçdiyini araşdırır. Tək cihazı təmizləyib hesabın başqa sessiyalarını açıq saxlamaq hücumçunun geri qayıtmasına yol verə bilər.

**Out.** Hər nəticə ayrıca sübut istəyir. Arxiv yaratmaq məlumatın çıxması deyil; böyük ötürmə şifrələnmiş arxiv də, icazəli ehtiyat nüsxə də ola bilər. Faylın açılmaması həmişə fidyə proqramı deyil: disk xətası və icazə dəyişikliyi də mümkündür. Fayl məzmunu, prosesin davranışı, şəbəkə istiqaməti və xidmət hesabının fəaliyyəti birlikdə qiymətləndirilir. “Objectives” texniki əməliyyatdan geniş məqsədi göstərir: fidyə tələbi ödəniş alınmasını sübut etmir; məqsəd barədə nəticənin hansı sənədə, mesaj və ya müşahidəyə söykəndiyi qeyd edilir. Model niyyəti avtomatik oxumur.

### Təkrarlar və iki fərqli pivot

UKC-də **körpü yaratma (pivoting)** ələ keçirilmiş sistemdən başqa şəbəkə və resurslara çıxış üçün istifadə etməkdir. Şərti nümunədə yataqxana cihazı daxili printer şəbəkəsinə çıxışı olan sistemə çevrilib; onun üzərindən keçən tunel birbaşa çata bilməyən hücumçu üçün körpüdür. Seqmentlərarası qaydalar, icazəsiz tunellərin izlənməsi və çıxış nəzarəti bu yolu məhdudlaşdırır.

Yanal hərəkət başqa sistemdə mövqe əldə etməkdir. Körpü şəbəkə yolunu açır, yanal hərəkət həmin yoldan istifadə edib başqa sistemə keçidi təsvir edə bilər. İkisi eyni hadisədə görünə bilər, amma eyni anlayış deyil: hər serverə girişdə tunel qurulduğunu yazmaq olmaz, iki açıq daxili server arasında hesabla giriş tunelsiz də baş verə bilər. Məsələn, ələ keçirilmiş admin parolu ilə RDP vasitəsilə başqa serverə keçid yanal hərəkətdir, körpü deyil.

:::exam Tələ: iki “pivot”
UKC-də pivoting ələ keçirilmiş sistemi körpü kimi işlədib əlçatmaz şəbəkələrə çatmaqdır (tunel qurmaq). Diamond modelində analitik pivot isə tamam başqa şeydir: məlum bir faktdan (məsələn, domen və ya IP) başlayıb əlaqəli faktlara keçən təhlil üsulu. Birində hücumçu sistemlər arasında yol açır, digərində analitik faktlar arasında hərəkət edir. Hesabatda “analitik keçid” və ya “şəbəkə körpüsü” deyə dəqiqləşdirilir.
:::

UKC geniş təsvir verir, lakin mürəkkəbliyi də artırır. Kitabxana portalında bloklanmış skan üçün ilkin triaj kifayətdir; çoxhostlu insidentdə isə fazaların ayrıca yoxlanması gözdən qaçmış hesabı və çıxış kanalını tapmağa kömək edir. Detallıq əhatəyə uyğun seçilir.

## Diamond Model

### Hadisənin dörd əsas xüsusiyyəti

Sergio Caltagirone, Andrew Pendergast və Christopher Betz 2013-cü ildə “The Diamond Model of Intrusion Analysis” işini dərc etdilər. Əsas vahid ayrıca müdaxilə hadisəsidir: rəqib müəyyən infrastrukturdan istifadə edərək imkanını qurbana qarşı tətbiq edir. Bu dörd xüsusiyyət rombun təpələridir. Bir romb bütün kampaniyanı əvəz etmir; çoxsaylı hadisələrin əlaqələndirilməsi daha böyük mənzərə yaradır.

- **Rəqib (adversary):** fəaliyyəti aparan şəxs və ya qrup; analitik onun adını bilməyə bilər.
- **İnfrastruktur (infrastructure):** fəaliyyətə vasitəçilik edən domen, IP, server, C2 serveri, poçt hesabı.
- **İmkan (capability):** tətbiq olunan alət, zərərli proqram, texnika və ya istismar vasitəsi.
- **Qurban (victim):** təsirlənən şəxs, hesab, cihaz və ya təşkilat. Bir neçə səviyyədə göstərmək faydalıdır: kafedra hesabı və həmin hesabın cihazı ayrıca müəyyən edilir.

| Xüsusiyyət | Şərti LMS hadisəsində məlumat | Açıq qalan sual |
| --- | --- | --- |
| Rəqib | Naməlum aktor, hadisə qrupu A | Başqa hadisələri də eyni tərəf idarə edirmi? |
| İnfrastruktur | portal-yardim.example, 198.51.100.24 | Ünvan həmin vaxt kimə xidmət edib? |
| İmkan | Saxta giriş səhifəsi ilə hesab məlumatının toplanması | Sessiya nişanı da ələ keçirilibmi? |
| Qurban | Kafedra əməkdaşının LMS hesabı | Hesabın başqa xidmətlərdə hüquqları varmı? |

Naməlum təpə modelin istifadəsinə mane olmur: “Rəqib məlum deyil” yazmaq əsassız qrup adı yazmaqdan daha düzgündür. Eyni alət fərqli qruplarda ola bilər; hücumçu başqasının serverini ələ keçirib işlədə bilər; infrastruktur sahibi ilə hücumçu eyni şəxs sayılmır; hədəf cihazın universitetə məxsus olması hər əməliyyatı universitet əməkdaşının etdiyini göstərmir.

:::figure
src = "m05-2.png"
alt = "Romb: yuxarıda Rəqib, solda İmkan, sağda İnfrastruktur, aşağıda Qurban; təpələr oxlarla bağlıdır. İnfrastrukturdan sağda “Pivot” qutusu: domen, oradan əlaqəli hadisələr."
caption = "Diamond Model-in dörd təpəsi və bir domendən əlaqəli hadisələrə analitik keçid. Nümunədə rəqibin kimliyi açıq qalır."
wide = true
:::

Rəqib–qurban oxu **sosial-siyasi** əlaqəni, imkan–infrastruktur oxu **texnoloji** əlaqəni düşünməyə kömək edir: universitet niyə seçilib, hədəf hansı funksiyanı daşıyır, vasitə hansı infrastruktur tələb edir? Şəkildə bütün əlaqələrin çəkilməsi onların hamısının sübut olunduğunu göstərməməlidir; naməlum və fərziyyə olan əlaqələr açıq işarələnir.

### Meta-xüsusiyyətlər

Meta-xüsusiyyətlər (meta-features) dörd təpəni kontekstlə tamamlayır. Bu sahələrdən biri məlum deyilsə, boşluğun səbəbi yazılır; ehtimal fakt yerinə daxil edilmir.

| Xüsusiyyət | Nəyi təsvir edir? | Universitetdə şərti qeyd |
| --- | --- | --- |
| Vaxt möhürü (timestamp) | Hadisənin vaxtı və ya intervalı | 2026-11-03, 09:20–09:24, UTC+04:00 |
| Mərhələ (phase) | Seçilmiş zəncir üzrə mövqe | Çatdırılma, UKC faza 3 |
| Nəticə (result) | Fəaliyyətin məlum nəticəsi | Məktub çatıb, icra təsdiqlənməyib |
| İstiqamət (direction) | Tərəflər arasında fəaliyyətin yönü | Xarici infrastrukturdan qurban hesabına |
| Metodologiya (methodology) | Fəaliyyətin ümumi üsulu | Hədəfli fişinq və istifadəçinin aldadılması |
| Resurslar (resources) | Fəaliyyət üçün tələb olunan imkanlar | Domen, poçt hesabı, hazırlanmış məzmun |

Resurslarla infrastruktur qismən üst-üstə düşür: infrastruktur konkret texniki vasitədir, resurslar fəaliyyəti mümkün edən bilik, vaxt, giriş və imkanları daha geniş təsvir edir. Kafedra əməkdaşının iş qrafikini bilmək server deyil, lakin fişinq hazırlığında resurs ola bilər; sübut yoxdursa, yalnız mümkün tələb kimi göstərilir.

Nəticə sahəsində “uğurlu” sözünün obyekti göstərilməlidir: məktubun çatması uğurlu çatdırılmadır, hesabın ələ keçirilməsi deyil. Nəticə sonrakı məlumata görə yenilənə bilər; əvvəlki qiymətləndirmənin vaxtı da saxlanılır ki, qərarın hansı məlumatla verildiyi görünsün.

### Analitik keçid, hadisə zənciri və qruplaşdırma

Analitik keçid (analitik pivot) bir məlum xüsusiyyətdən əlaqəli məlumatı axtarmaqdır. Tapılmış qeydiyyat-yardim.example domeni əvvəl poçt arxivində axtarılır; eyni domenə keçid olan məktubların başqa kafedralara da gəldiyi aşkarlana bilər; proksi qeydləri keçidi hansı cihazların açdığını göstərir. Beləliklə domendən yeni qurbanlara və əlaqəli hadisələrə keçilir. Domenin qeydiyyat məlumatından eyni şəxsin başqa domenləri çıxa bilər; biri başqa şirkətə hücumda işlənibsə, yeni qurban və yeni imkan görünür.

Hər keçid üçün əsas və alternativ izah saxlanılır: eyni TLS sertifikatı bir neçə xidmətə aid ola bilər, eyni göndərən ünvanı ələ keçirilmiş hesab ola bilər, gizlədilmiş qeydiyyatda eyni vasitəçi eyni sahib demək deyil. Əlaqə “eyni gün, eyni keçid, eyni əlavə məzmunu” kimi ölçülə bilən xüsusiyyətlərlə sənədləşdirilir; vizual oxşarlıq zəif əsasdır.

Zaman və səbəb əlaqələri ilə birləşdirilmiş hadisələr **fəaliyyət zənciri (activity thread)** yaradır: məktub → keçidin açılması → hesabdan giriş → bazadan ixrac. Oxşar xüsusiyyətli hadisələr və zəncirlər **fəaliyyət qrupu (activity group)** kimi toplana bilər. Belə qrup analitik klasterdir; onun konkret təşkilat və ya dövlətə aid edilməsi ayrıca atribusiya (attribution) iddiasıdır.

| Ortaq xüsusiyyət | Mümkün alternativ izah | Yoxlanacaq əlavə məlumat |
| --- | --- | --- |
| Eyni bulud IP-si | Ünvan paylaşılır və ya başqa müştəriyə verilib | Müşahidə vaxtı, domen və xidmət ayrıntıları |
| Eyni fayl heşi | Hazır nümunə müxtəlif aktorlarda yayılıb | Çatdırılma yolu, konfiqurasiya, hədəf seçimi |
| Eyni TTP | Üsul çox geniş yayılıb | Üsulların birləşməsi və fəaliyyət ardıcıllığı |
| Eyni hesab | Qanuni istifadə və hücum qarışıb | Cihaz, sessiya, vaxt və sahibin təsdiqi |

Analitik əvvəl öz sualına cavab verən keçidləri seçir. Bir kitabxana hesabından başlayan araşdırmada bütün internet domen əlaqələrini toplamaq məqsədsiz genişlənmədir. Əhatə, vaxt pəncərəsi və dayanma meyarı müəyyən edilir (məsələn, eyni məktubu almış bütün universitet hesabları və həmin keçidə aid cihazlar). Şəxsi məlumatlara giriş də araşdırmanın ehtiyacı ilə məhdudlaşdırılır.

:::exam Tələ: ümumi infrastruktur atribusiya deyil
İki hücumda eyni bulud IP-sinin görünməsi onları eyni qrupun etdiyini sübut etmir: bulud ünvanları minlərlə müştəri arasında paylaşılır. Bu yoxlanmalı fərziyyədir, nəticə deyil. İmtahanda müşahidəni, fərziyyəni və təsdiqlənmiş nəticəni ayır. Fərziyyəni gücləndirən pivotlar: eyni domen qeydiyyatçısı, eyni TLS sertifikatı, kodda eyni xüsusiyyətlər, eyni iş saatları, eyni TTP-lər. Tapılmasa, kampaniyalar ayrı qeydə alınır, iki universitet isə məlumatı TLP:GREEN ilə bir-biri ilə paylaşır.
:::

## MITRE ATT&CK

### Taktika, texnika və prosedur

MITRE ATT&CK real müşahidələrə əsaslanan hücumçu davranışları bilik bazasıdır; adı Adversarial Tactics, Techniques, and Common Knowledge ifadəsindən gəlir. ATT&CK zəiflik kataloqu deyil: CVE konkret zəifliyi, ATT&CK isə həmin və ya başqa imkanlarla aparılan davranışı təsvir edir. Bir CVE müxtəlif hücum yollarında işlənə bilər, bir texnika isə konkret CVE olmadan tətbiq oluna bilər.

- **Taktika (tactic)** fəaliyyətin həmin məqamda **niyə** edildiyini göstərir.
- **Texnika (technique)** məqsədə **necə** çatıldığını təsvir edir.
- **Alt-texnika (sub-technique)** üsulu daha dar səviyyəyə bölür.
- **Prosedur (procedure)** konkret aktorun və ya proqramın texnikanı necə tətbiq etdiyinə dair nümunədir.

Taktika ümumi motivasiya ilə eyni deyil: “Credential Access” kimlik məlumatı əldə etmək məqsədidir, universitetdən pul almaq isə daha geniş niyyətdir.

| Anlayış | Məna | Universitet nümunəsi |
| --- | --- | --- |
| Taktika | Davranışın yaxın məqsədi | İcra, Execution |
| Texnika | Məqsədə çatma üsulu | T1059, əmr və skript interpretatorları |
| Alt-texnika | Üsulun konkret növü | T1059.001, PowerShell |
| Prosedur | Müşahidə edilmiş konkret tətbiq | Kafedra cihazında PowerShell ilə icazəsiz skript işlədilməsi |
| Proqram və qrup qeydləri | Davranışla əlaqələndirilən məlum obyektlər | Hesabatda təsvir edilmiş vasitənin işlənməsi |
| Azaltma tədbiri | Riskə təsir edən ümumi nəzarət | Skript icrasına məhdudiyyət |

Bir texnika birdən çox taktika ilə əlaqəli ola bilər. Etibarlı hesabdan istifadə (T1078) ilkin girişə, davamlılığa və başqa məqsədlərə xidmət edə bilər; əlaqə texnikanın rəsmi təsviri və hadisənin konteksti ilə seçilir. Hər uğurlu girişə T1078 yazmaq düzgün deyil: etiket hücumçu tərəfindən etibarlı hesabdan sui-istifadə üçün əsaslandırılır, adi müəllim girişləri hücum sayılmır.

ATT&CK Enterprise, Mobile və sənaye idarəetmə sistemləri üçün ICS sahələrini ayırır. İnzibati iş stansiyaları və serverlər üçün Enterprise baxışı başlanğıcdır; sənaye avadanlığı və mobil tətbiq üçün uyğun sahə ayrıca nəzərdən keçirilir. Platforma da seçilməlidir: Windows-a aid prosesi Linux LMS serverində eyni mənbə ilə aşkar etmək olmaz.

:::exam Tələ: strateji / necə
UKC-ni “strateji”, ATT&CK-ı “necə” adlandırmaq sadələşdirmədir: ATT&CK-da taktika niyə, texnika necə sualına cavab verir.
:::

### Versiya və v19 dəyişikliyi

ATT&CK yaşayan bilik bazasıdır; hesabatda istifadə edilən versiya və tarix saxlanılmalıdır. 28 aprel 2026-cı il tarixli v19-da Enterprise sahəsində əvvəlki Defense Evasion taktikasının məzmunu **Stealth (TA0005)** və **Defense Impairment (TA0112)** üzrə ayrılıb. Köhnə mənbələrdə TA0005 üçün “Defense Evasion” adı qalır. Köhnə etiketlə hazırlanmış qaydanı cari xəritəyə köçürəndə yalnız başlığı dəyişmək kifayət deyil; davranışın hansı təsnifata uyğun gəldiyi yoxlanır.

Mənaca: gizlənmə müdafiəçinin fəaliyyəti görməsini çətinləşdirən davranışlardır; müdafiə imkanlarının zəiflədilməsi isə onun nəzarət və müşahidə imkanına müdaxilədir. Konkret texnikanın yeri yaddaşdan təxmin edilmir; rəsmi versiya məlumatı və texnika əlaqələri əsas götürülür. Universitet qayda reyestrində ATT&CK identifikatoru ilə yanaşı versiya sahəsi saxlayır.

Windows hadisə jurnallarının təmizlənməsi əvvəl T1070.001 kimi göstərilirdi; v19-da T1685.005 identifikatoru işlənir. Windows Security jurnalındakı 1102 hadisəsi həmin jurnalın təmizləndiyini göstərir, bütün Windows kanallarının silindiyini sübut etmir; qanuni inzibati iş ehtimalı, əməliyyatı edən hesab və jurnalın uzaq nüsxəsi yoxlanır.

Versiya dəyişikliyi tarixi məlumatın mənasını itirməməlidir: köhnə etiketi səssiz dəyişib orijinal hesabatı pozmaq əvəzinə ilkin etiket, uyğunlaşdırılmış etiket və çevirmə qeydi saxlanılır; o vaxt mövcud qayda ilə cari qaydanın nəticəsi də ayrılır. Bu, magistr tədqiqatında fərqli illərin örtük göstəricilərini müqayisə edərkən xüsusilə lazımdır.

### Davranışın sübutdan xəritələnməsi

Xəritələmə (mapping) müşahidə olunan davranışı uyğun taktika və texnika ilə əlaqələndirməkdir. İş texnika adından başlamır: əvvəl cihazın nə etdiyi yazılır (hansı proses, hansı valideyn proses, hansı hesab, hansı fayl, hansı istiqamət), sonra təsvirə uyğun texnika seçilir. Yalnız məhsulun xəbərdarlıq adı ilə xəritələmək səhv etiketləri çoxaldır.

| Müşahidə | Mümkün texnika | Təsdiq üçün lazım olan detal |
| --- | --- | --- |
| Zərərli əlavə ilə fişinq | T1566.001 | Məktubun zərərli məqsədi və əlavə hissəsi |
| İstifadəçi zərərli faylı açıb | T1204.002 | İstifadəçi hərəkəti və uyğun proses əlaqəsi |
| PowerShell ilə icazəsiz icra | T1059.001 | Proses, əmr sətri və davranış konteksti |
| Planlaşdırılmış tapşırıq yaradılıb | T1053.005 | Tapşırığın məzmunu, hesabı və təyinatı |
| SMB vasitəsilə başqa sistemə giriş | T1021.002 | Hücumçu fəaliyyəti, mənbə və hədəf sessiyası |
| Fayllar arxivə yığılıb | T1560.001 | Arxiv alətinin proses və fayl qeydləri |
| Məlumat şifrələnib | T1486 | Zərərli prosesin fayl dəyişiklikləri və nəticə |
| Bərpa imkanına zərər vurulub | T1490 | Bərpa resurslarını hədəfləyən əməl və nəticə |

“Mümkün” sözü vacibdir: PowerShell inzibati işdə də işlənir, arxiv kitabxananın planlı ixracı ola bilər. Əvvəl davranışın icazəli olub-olmadığı yoxlanır, sonra hücum yolundakı yeri qiymətləndirilir. Texnika identifikatoru təhlükəlilik balı deyil: T1486 təsdiqlənmiş şifrələmə davranışını adlandırır, hansı faylların itirildiyini isə ayrıca inventar və bərpa yoxlaması göstərir.

### Navigator və örtüyün ölçülməsi

ATT&CK Navigator matrisi qatlar (layers) üzərində rəngləməyə, qeydlər və ballar əlavə etməyə imkan verən vizual vasitədir. Universitet ayrıca qatlarla ehtimal olunan təhdidləri, mövcud telemetriyanı və yoxlanmış aşkarlamaları göstərə bilər. Qatın mənbəsi, ATT&CK versiyası, rəng şkalası və yenilənmə tarixi sənədləşdirilir; rəngin mənası göstərilməzsə, eyni yaşıl xana biri üçün “məlumat var”, digəri üçün “hücum bloklanır” mənasını verə bilər.

Örtük (coverage) bir sözlə deyilsə də, müxtəlif səviyyələri var: sensorun quraşdırılması məlumatın toplandığını göstərməyə bilər; toplanan məlumat qaydanın onu işlətdiyini, qayda isə real şəraitdə vaxtında xəbərdarlıq verdiyini sübut etmir. Universitet hər seçilmiş davranış üçün telemetriya, aşkarlama və cavabın vəziyyətini ayrı saxlayır. “Məhsul bu texnikanı dəstəkləyir” yoxlanmış örtük deyil.

:::figure
src = "m05-3.png"
alt = "Beş qutu oxlarla bağlı: Davranış (ATT&CK, məsul CTI), Telemetriya (qeyd gəlir?, İT), Aşkarlama (qayda var?, SOC), Sınaq (xəbər verdi?, red team), Cavab (təsdiqlənib, IR)."
caption = "Hücum davranışından yoxlanmış müdafiəyə keçid. Hər keçiddə ayrıca sübut və məsul şəxs tələb olunur."
wide = true
:::

| Davranış | Mənbə | Aşkarlama | Test nəticəsi | Cavab |
| --- | --- | --- | --- | --- |
| T1053.005 | Tapşırıq və proses auditi | İcazəsiz tapşırıq qaydası | Sınaqda xəbər verdi | Cihaz təcridi yoxlanıb |
| T1021.002 | Server giriş və şəbəkə qeydi | Qayda hazırlanır | Yoxlanmayıb | Məsul təyin edilib |
| T1486 | EDR və fayl telemetriyası | Kütləvi dəyişmə qaydası | Laboratoriyada yoxlanıb | Server üçün ayrıca sınaq lazımdır |
| T1685.005 | Uzağa ötürülən audit qeydi | 1102 üzrə xəbərdarlıq | Testdə gecikmə var | Toplama gecikməsi araşdırılır |

:::example Şərti hesablama
Universitet prioritet seçdiyi 12 davranışdan 8-i üçün işlək telemetriya, 5-i üçün yoxlanmış aşkarlama, 3-ü üçün yoxlanmış cavab saxlayır. Aşkarlama örtüyü bu məhdud çoxluqda 5/12-dir. Bu rəqəm bütün ATT&CK-ın və bütün hücumların həmin hissəsinin tutulduğu demək deyil. Risk çəkisi də fərqlənir: tələbə bazasına yol açan zəif örtük az riskli laboratoriya davranışından əvvəl işlənə bilər.
:::

Texnikanın yalnız bir proseduru sınanıbsa, nəticə həmin prosedur və mühit üçün yazılır: bir tapşırığın tutulması bütün tətbiqlərin görüldüyünü sübut etmir. Əməliyyat sistemi, audit sazlaması və hüquqlar dəyişəndə nəticə də dəyişir. Rəngli matris təkbaşına müdafiə zəmanəti vermir.

## Pyramid of Pain

### Altı səviyyənin mənası

David Bianco 2013-cü ildə Pyramid of Pain modelini təqdim etdi. Model indikator və davranış növlərini hücumçunun onları dəyişdirməsi zamanı çəkdiyi çətinlik baxımından sıralayır. “Ağrı” müdafiəçinin xərci deyil, hücumçunun uyğunlaşma yüküdür: heşi bloklayanda hücumçu faylı dəyişib başqa heş yarada bilər, davranış zəncirini dayandıran tədbirdən yayınmaq isə daha geniş iş üsulunu dəyişməyi tələb edə bilər.

Kompromitasiya indikatoru (indicator of compromise, IoC) baş vermiş və ya ehtimal olunan təhlükəli fəaliyyətlə əlaqəli müşahidə edilə bilən göstəricidir (fayl heşi, domen, IP). Taktika, texnika və prosedurlar (TTP) daha geniş davranışı təsvir edir. Heş konkret obyektə çox dəqiq işarə edir, TTP isə müxtəlif alət və ünvanlarla təkrarlana bilər; dəqiqliklə dayanıqlılıq eyni meyar deyil.

| Səviyyə (aşağıdan yuxarı) | Hücumçunun dəyişə biləcəyi şey | Universitetin müdafiə qərarı |
| --- | --- | --- |
| Heşlər (hash values) | Faylın baytlarını dəyişib başqa heş almaq | Məlum nümunəni tez bloklamaq |
| IP ünvanları | Başqa server və ya ünvan işlətmək | Vaxtı yoxlanmış ünvanı bloklamaq |
| Domen adları | Başqa domen və yönləndirmə qurmaq | DNS və poçt axtarışını birlikdə aparmaq |
| Şəbəkə və host artefaktları | Sorğu nümunəsi, fayl yolu, xidmət adı | Bir neçə əlaqəli əlamətlə qayda qurmaq |
| Alətlər (tools) | Vasitəni dəyişmək və ya yenidən hazırlamaq | Alətin davranışını müxtəlif nümunələrlə yoxlamaq |
| TTP | Əməliyyat üsulunu dəyişmək | Hesab, icra və yanal hərəkəti əlaqələndirmək |

Sıra mütləq xərc qanunu deyil: bir aktor üçün xüsusi domeni dəyişmək çətin, başqası üçün hazır aləti əvəz etmək asan ola bilər. Model qərara istiqamət verir, maliyyə hesabı aparmır. Paylaşılan IP-nin bloklanması hücumçuya az təsir edib qanuni xidməti ciddi poza bilər; tədbirin yerli təsiri ayrıca ölçülür.

### Universitetdə pilləli tətbiq

Kafedra cihazında zərərli fayl tapılır. Birinci iş etibarlı heşi hesablayıb eyni nüsxəni başqa cihazlarda axtarmaqdır. Aşağıdakı əmr yalnız mövcud faylın heşini hesablayır, icra etmir; yol şərtidir, zərərli nümunə adi istifadəçi qovluğunda saxlanmamalıdır.

```bash
sha256sum /srv/ir/quarantine/sample.bin
```

İkinci iş faylın əlaqə saxladığı domeni və ünvanı mövcud qeydlərdə axtarmaqdır. Üçüncü iş daha davamlı davranış qaydasıdır: istifadəçi sənədi açır, gözlənilməyən interpretator başlayır, proses xarici ünvana bağlanır, sonra tapşırıq yaradılır. Bu ardıcıllıq bir heşə bağlı deyil; lakin qayda normal inzibati skriptləri də tuta bilər, ona görə valideyn proses, imza, hesab və dəyişiklik tapşırığı ilə kontekst daraldılır.

Piramidanın yuxarısına çalışmaq aşağı pillələri tərk etmək demək deyil: təsdiqlənmiş zərərli heş dərhal fayda verir, davranış qaydası isə vaxt istəyir. Universitet həm sürətli bloklama, həm daha dayanıqlı aşkarlama saxlayır. Hər indikator üçün mənbə, ilk və son müşahidə vaxtı, etibarlılıq, tətbiq edilən tədbir və yenidən baxma tarixi yazılır; bu reyestr köhnə blokların daimi maneəyə çevrilməsini azaldır.

## MITRE D3FEND

### Hücum texnikasından rəqəmsal artefakta

MITRE D3FEND müdafiə üsullarını və onların rəqəmsal obyektlərlə münasibətini formal təsvir edən bilik bazası və ontologiyadır (ontology: anlayışların və aralarındakı əlaqələrin müəyyən edilmiş sistemi). ATT&CK hücumçunun davranışını adlandırır, D3FEND müdafiəçinin texniki təsirini təsvir etməyə kömək edir. D3FEND hazır məhsul siyahısı və ya bütün insidentlər üçün icra planı deyil.

Başlanğıc nöqtəsi **rəqəmsal artefaktdır (digital artifact)**: proses, fayl, şəbəkə trafiki, hesab və digər müşahidə və müdaxilə obyektləri. LMS cihazındakı şübhəli skript həm fayl, həm işləyən proses, həm şəbəkə bağlantısı yarada bilər. Fayl, proses və trafik təhlili müxtəlif artefaktları görür; şəbəkə trafikinin süzülməsi isə həmin bağlantıya təsir edir. Hamısını “antivirus var” cümləsinə yığmaq texniki boşluqları gizlədir.

| Hücum müşahidəsi | Artefakt | Müdafiə üsulu | Yoxlama sualı |
| --- | --- | --- | --- |
| Zərərli sənəd gəlir | Fayl və poçt əlavəsi | Fayl təhlili və məzmun məhdudiyyəti | Şübhəli nüsxə vaxtında saxlanırmı? |
| İcazəsiz skript işləyir | Proses və əmr sətri | Proses təhlili və icra nəzarəti | Valideyn proses də görünürmü? |
| C2 əlaqəsi qurulur | Şəbəkə trafiki | Trafik təhlili və süzülməsi | İcazəli proksi xaricində çıxış varmı? |
| Ələ keçirilmiş hesab işlənir | Kimlik və sessiya | Kimlik məlumatlarının sərtləşdirilməsi | Sessiya ləğvi də yoxlanıbmı? |
| Yanal keçid sınanır | Şəbəkə yolu və giriş | Təcrid və seqmentlərarası nəzarət | Qadağa hər iki istiqamətdə uyğundurmu? |

Cədvəldəki adlar müdafiə üsullarının məntiqini göstərir. Konkret D3FEND qeydi seçiləndə onun tərifi, əlaqəli artefaktı və istifadə olunan versiyası saxlanılır. ATT&CK texnikası ilə müdafiə üsulu arasında əlaqə tapılması universal bloklama sübutu deyil: nəzarət müəyyən platformada, düzgün sazlamada və uyğun əhatədə işləyir. Bulud LMS-ində universitetin proses telemetriyasına çıxışı yoxdursa, yerli EDR nümunəsi oraya olduğu kimi köçürülmür.

### Seçim, tətbiq və məhdudiyyət

Kitabxananın elektron arxivindən icazəsiz kütləvi endirmə üçün əvvəl qorunacaq obyekt və icazə modeli seçilir; sonra müşahidə üsulu (tətbiq sorğuları, hesabın sessiyası, ötürmə həcmi); sonra müdaxilə (sorğu sürətinə hədd, sessiyanın məhdudlaşdırılması, əlavə autentifikasiya). Hər addım başqa təsir verir: yalnız şəbəkə ünvanını bloklamaq ortaq kampus proksisi arxasındakı qanuni istifadəçiləri də dayandıra bilər.

Tədbirin sənədində giriş şərti, görülən əməl və gözlənilən nəticə yazılır: məsələn, idarə olunmayan cihazın tələbə bazasına yazma sorğusu rədd edilir, səbəb qeydə alınır, hesabın qanuni oxuma işi ayrıca siyasətlə qiymətləndirilir. Test həm icazəsiz sorğunun rəddini, həm icazəli sorğunun işləməsini yoxlamalıdır; əks halda bütün trafiki kəsən səhv qayda da “hücumu dayandırdı” kimi görünər.

D3FEND texniki dili dəqiqləşdirir, amma universitetin riskini, hüquqi qərarını və məsuliyyət bölgüsünü özü təyin etmir; məxfi tələbə məlumatını hansı sensorun görə biləcəyi siyasətdə həll olunur. İdarəetmə üçün CSF, texniki təsir üçün D3FEND, davranışın təsviri üçün ATT&CK birgə işlədilə bilər.

## NIST CSF 2.0

### Altı funksiya və nəticə yönümlü yanaşma

NIST Cybersecurity Framework 2.0 2024-cü ilin fevralında dərc olunub. Çərçivə kiberriskin idarəsi üçün nəticələri altı funksiya altında təşkil edir. “Nəticə” təşkilatın əldə etmək istədiyi təhlükəsizlik vəziyyətidir; CSF hər nəticə üçün məcburi məhsul seçmir, universitet ölçüsünə, asılılıqlarına və riskinə uyğun tədbirlərlə ona çata bilər.

- **İdarəetmə (Govern):** digər işlərin niyə, kim tərəfindən və hansı risk həddi ilə aparıldığını müəyyən edir (2.0-da əlavə olunub).
- **Müəyyənləşdirmə (Identify):** aktivləri, asılılıqları və riskləri tanıyır.
- **Qoruma (Protect):** riski məhdudlaşdıran tədbirləri qurur.
- **Aşkarlama (Detect):** mümkün hücumu tapır və təhlil edir.
- **Cavab (Respond):** təsdiqlənmiş insidenti idarə edir.
- **Bərpa (Recover):** xidmətləri və imkanları qaytarır.

Bunlar bir dəfə sırayla keçilən altı layihə mərhələsi deyil; davamlı və əlaqəli işlərdir.

| Funksiya | Universitetin işi | Yoxlana bilən nəticə |
| --- | --- | --- |
| Govern | Risk həddi, məsuliyyət və təchizatçı tələblərini təsdiqləmək | LMS riski üçün qərar sahibi və qəbul qaydası var |
| Identify | Tələbə bazası, hesab və asılılıqları inventarlaşdırmaq | Bərpa üçün tələb olunan xidmətlər məlumdur |
| Protect | MFA, minimum hüquq, yamaq və nüsxə qurmaq | İcazəsiz giriş məhduddur, nüsxə ayrıdır |
| Detect | Hesab, cihaz və çıxışları izləmək | Şübhəli davranış üzrə yoxlanmış xəbərdarlıq var |
| Respond | Təcrid, əhatə təhlili və əlaqələndirmə aparmaq | Qərar və əməl vaxtları sənədləşib |
| Recover | Təmiz mühitdə xidməti bərpa etmək | Məlumat və xidmət sahibləri nəticəni yoxlayıb |

İdarəetmə funksiyası texniki işin qarşısında sənəd maneəsi deyil. Tələbə bazasını dayandırmaq qərarını kimin verəcəyi əvvəl məlum olmasa, SOC hücum zamanı gözləyə bilər; səlahiyyət və hədlər əvvəl razılaşdırılanda təcrid gecikmir. Təchizatçıdan alınan bulud LMS-i üçün jurnal əlçatanlığı, insident bildirişi və bərpa məsuliyyəti müqavilə və xidmət idarəsində nəzərə alınır.

### Core, profillər və səviyyələr

CSF-in nüvəsi (Core) nəticələri funksiyalar, kateqoriyalar və altkateqoriyalar şəklində təşkil edir. Təşkilati profil (Organizational Profile) seçilmiş nəticələrin universitet üçün hansı vəziyyətdə olduğunu göstərir: cari profil mövcud, hədəf profil çatmaq istənilən vəziyyətdir; aradakı fərq fəaliyyət planına çevrilir. Hədəf profil hər mümkün nəzarəti toplamaq deyil; tədris və tədqiqatın ehtiyacına uyğun nəticələr seçilir.

Nümunə: LMS-in nüsxəsi var, amma bərpa yoxlanmayıb və idarə hesabı istehsalatla eynidir; hədəf nüsxənin ayrı idarəsi və təcrid olunmuş mühitdə bərpa yoxlamasıdır. Məsul şəxs, vaxt, sübut və qalıq risk də müəyyən edilir.

| Sahə | Cari vəziyyət | Hədəf nəticə | Sübut |
| --- | --- | --- | --- |
| Aktivlər | Kafedra serverlərinin siyahısı natamamdır | Xidmət sahibi və asılılıq məlumdur | Təsdiqlənmiş inventar |
| Giriş | İmtiyazlı hesablarda fərqli qaydalar var | Ayrı admin hesabı və uyğun MFA var | Giriş testi |
| Aşkarlama | Qayda var, məlumat gəlmir | Mənbə sağlamlığı izlənir | Sınaq xəbərdarlığı |
| Bərpa | Nüsxə alınıb, açılmayıb | Tələbə bazası təmiz mühitdə bərpa olunur | Bərpa protokolu |

CSF səviyyələri (Tiers) Partial, Risk Informed, Repeatable və Adaptive adları ilə risk idarəsinin nə dərəcədə təşkil edildiyini təsvir edir. Bunlar avtomatik sertifikat balı deyil və ən yüksək səviyyə hər universitet üçün məcburi məqsəd sayılmır; seçim fəaliyyətə və riskə uyğun əsaslandırılır. Bir laboratoriyanın yetkin qaydası bütün bölmələrin eyni vəziyyətdə olduğunu göstərmir.

NIST SP 800-61 Rev. 3 2025-ci ilin aprelində dərc olunub və insidentə cavabı CSF 2.0 üzrə kiberrisk idarəsinə bağlayır. Hazırlıq, cavab və bərpa yalnız insident günü görülən işlər deyil: hesabların ayrılması, əlaqə siyahısı və bərpa məşqi əvvəl hazırlanır; hadisədən öyrənilənlər profilin növbəti dəyişməsinə daxil edilir.

:::exam NIST CSF 2.0 (2024)
Altı funksiya: İdarəetmə (Govern, 2.0-da əlavə olunub), Müəyyənləşdirmə (Identify), Qoruma (Protect), Aşkarlama (Detect), Cavab (Respond), Bərpa (Recover).
:::

## Çoxsəviyyəli müdafiə və sıfır etibar

### Qatların sayı və müstəqilliyi

Çoxsəviyyəli müdafiə (defense in depth) bir tədbirin uğursuzluğu zamanı digər tədbirlərin hücumu məhdudlaşdırması prinsipidir (4-cü mövzu). Qatlar insan, proses, fiziki mühit, kimlik, cihaz, şəbəkə, tətbiq və məlumat səviyyəsində ola bilər. Universitet poçtda məktubu süzür, cihazda icranı məhdudlaşdırır, şəbəkədə serverə yolu daraldır, bazada hüquqları ayırır və ayrıca nüsxədən bərpa imkanını saxlayır; bunlar eyni hücum yoluna müxtəlif nöqtələrdə təsir edir.

İki vasitənin olması onların müstəqil qat olması demək deyil. Eyni administrator hesabı həm fayl serverini, həm ehtiyat nüsxəni, həm jurnal arxivini silə bilirsə, bir hesabın ələ keçirilməsi bütün qatlara təsir edir. Eyni telemetriyadan asılı iki aşkarlama qaydası mənbə susanda birlikdə korlaşır. Qatlar seçilərkən **ortaq uğursuzluq səbəbləri** ayrıca araşdırılır.

| Qat | Tədbir | Universitetdə nəyi məhdudlaşdırır? |
| --- | --- | --- |
| İnsan və proses | Şübhəli məktubu bildirmə qaydası | Kafedradakı ilk xəbərdarlığın gecikməsini |
| Kimlik | Ayrı admin hesabı (imtiyazlı giriş idarəsi, PAM) və MFA | Adi hesabdan geniş hüquqa keçidi |
| Cihaz | İcra nəzarəti və EDR | İcazəsiz skript və davamlılıq mexanizmini |
| Şəbəkə | Seqmentlərarası icazə siyasəti | Yataqxanadan tələbə bazasına birbaşa yolu |
| Tətbiq və məlumat | Rol əsaslı giriş və ixrac auditi | LMS hesabının bütün bazanı götürməsini |
| Bərpa | Ayrı idarə olunan qorunan nüsxə | İstehsalatın şifrələnməsindən sonra itkinin artmasını |

Hər qatın uğursuzluq ssenarisi yazılır: MFA sessiya nişanının oğurlanmasının bütün formalarını həll etmir; seqmentasiya icazə verilmiş tətbiq yolundakı sui-istifadəni tanımır; EDR idarə olunmayan şəxsi cihazı görməyə bilər; nüsxə sonradan məxfiliyi qaytarmır. Magistrant tədbiri təqdim edəndə onun nəyi məhdudlaşdırdığını və hansı keçidin açıq qaldığını göstərməlidir.

### Sıfır etibarın qərar məntiqi

Sıfır etibar (zero trust) şəbəkədəki yerə və ya əvvəlki girişə görə avtomatik etibar verməyən yanaşmadır; əsas mənbə NIST SP 800-207-dir. Giriş kimlik, cihaz vəziyyəti, tələb olunan əməl və digər kontekst əsasında minimum hüquqla verilir. VPN-dən keçmək və ya kampus IP-si almaq bütün daxili xidmətlərə icazə yaratmamalıdır. Şüar: “heç vaxt etibar etmə, həmişə yoxla”.

“Həmişə yoxla” hər paketdə parol soruşmaq demək deyil. Autentifikasiya kimliyin yoxlanması, avtorizasiya həmin kimliyə konkret əməlin verilməsidir. Giriş və sessiya siyasət əsasında qiymətləndirilir, risk və vəziyyət dəyişəndə qərar yenilənə bilər. İdarə olunan cihazda kataloqu oxumaqla tələbə bazasını ixrac etmək eyni tələb deyil.

Üç məntiqi rol: **siyasət mühərriki (policy engine)** qərar verir; **siyasət administratoru (policy administrator)** qərara uyğun əlaqənin qurulmasını və ya bağlanmasını idarə edir; **siyasətin icra nöqtəsi (policy enforcement point, PEP)** giriş yolunda qərarı tətbiq edir. Rollar konkret məhsulda birləşə və ya ayrı ola bilər. Qərara kimlik xidməti, cihazın vəziyyəti və təhlükə siqnalları məlumat verir. İcra nöqtəsindən yan keçən yol qalarsa, siyasət kağız üzərində qalır.

:::figure
src = "m05-4.png"
alt = "İstifadəçi və cihaz sorğunu icra nöqtəsinə (PEP) göndərir, PEP yuxarıdakı qərar nöqtəsi (kimlik, cihaz, risk) ilə əlaqə saxlayır və yalnız icazəli sorğunu resursa (LMS, baza) buraxır. Aşağıda müstəqil qatlar: seqmentasiya, EDR, yamaq, monitorinq, ehtiyat nüsxə."
caption = "Universitetdə resursa görə giriş qərarı və müstəqil müdafiə qatları. Şəbəkədə olmaq təkbaşına tələbə bazasına icazə vermir."
wide = true
:::

| Sorğu | Kontekst | Qərar | Səbəb |
| --- | --- | --- | --- |
| Tələbə LMS materialını oxuyur | Təsdiqlənmiş hesab, normal sessiya | Müvafiq kursla məhdud icazə | Tədris hüququ uyğundur |
| Kafedra hesabı bazanı ixrac edir | İdarə olunmayan cihaz | Rədd və araşdırma | Bu rolun ixrac hüququ yoxdur |
| Admin serveri idarə edir | Ayrı admin hesabı, yoxlanmış cihaz | Məhdud müddətli icazə | Əməl və resurs uyğun təsdiqlənib |
| Kitabxana hesabı serverə keçir | Kataloq işi üçün açılmış sessiya | Rədd | Əvvəlki giriş başqa resursa aiddir |

Sıfır etibar şəbəkə seqmentasiyasını və ehtiyat nüsxəni əvəz etmir: kimlik siyasəti səhv qurula bilər, xidmət özü zəiflik daşıya bilər, daxili proses artıq icazəli hüquqla zərər verə bilər. Çoxsəviyyəli müdafiə belə uğursuzluqlardan sonra təsiri azaldır; sıfır etibar etibar qərarının harada və hansı əsasla verildiyini dəqiqləşdirir. Bu iki yanaşma bir arxitekturada işləyir.

### Universitetə uyğun keçid

Keçid bütün kampusu bir gündə bağlamaqla başlamır. Əvvəl ən həssas resurs və ona qanuni giriş yolları müəyyən edilir; tələbə bazasının administrator yolu kafedra istifadəçi yolundan ayrılır; idarə olunan cihaz tələbi və sessiyanın ləğvi əvvəl sınaq qrupunda yoxlanır. Tədrisi dayandıran qanuni istisnalar varsa, onların sahibi, müddəti və əlavə nəzarəti müəyyən edilir.

İmtahan vaxtı kimlik xidməti dayananda davranış əvvəlcədən razılaşdırılmalıdır: avtomatik açıq giriş məxfi bazanı təhlükəyə atar, hər şeyi bağlamaq tədrisi dayandırar. Qorunan fövqəladə giriş, məhdud funksiyalı davam rejimi və xidmətə uyğun nasazlıq siyasəti ayrıca layihələndirilir; fövqəladə hesablar gündəlik işlədilmir, istifadəsi sonradan yoxlanır.

## Modelləri müqayisə etmək və seçmək

| Model | Əsas sual | Güclü tətbiq | Məhdudiyyət |
| --- | --- | --- | --- |
| Cyber Kill Chain | Hücum yolunda hansı mərhələ görünür? | Erkən müdaxilə və rəhbərliyə izah | Daxili fəaliyyət çox ümumiləşir |
| Unified Kill Chain | Girişdən məqsədə hansı fəaliyyətlər var? | Çoxhostlu insidentin əhatəsi | 18 fazanı idarə etmək əlavə iş istəyir |
| Diamond Model | Kim, hansı imkan və infrastrukturla, kimə qarşı? | Əlaqələr, analitik keçid və qruplaşdırma | Təqvim və tədbir planı ayrıca lazımdır |
| ATT&CK | Hansı məqsəd və davranış müşahidə edilib? | Texnika xəritəsi və aşkarlama mühəndisliyi | Ardıcıllıq və ümumi risk balı vermir |
| Pyramid of Pain | Hücumçu nəyi dəyişəndə çətinlik çəkər? | İndikatorla davranışa qoyulan səyin seçimi | Çətinlik keyfiyyətcə qiymətləndirilir |
| D3FEND | Hansı artefakta hansı müdafiə təsiri var? | Texniki tədbiri dəqiq təsvir etmək | Uyğunluq real mühitdə test istəyir |
| NIST CSF 2.0 | Risk və təhlükəsizlik nəticəsi necə idarə olunur? | Profil, məsuliyyət və prioritet | Konkret aşkarlama qaydası vermir |
| Çoxsəviyyəli müdafiə | Bir qat keçilsə, nə zərəri saxlayır? | Müstəqil tədbirlərlə təsiri azaltmaq | Ortaq asılılıqlar bütün qatları zəiflədə bilər |
| Sıfır etibar | Bu kimliyə bu resursda bu əməl verilməlidirmi? | Minimum hüquq və kontekstlə giriş | Yanlış siyasət və görünməyən cihaz riski qalır |

Seçim işin sualından başlayır. Rektorluğa LMS dayanmasının səbəbini qısa izah etmək üçün Cyber Kill Chain və CSF nəticələri kifayət edə bilər. SOC-un serverlər arasında keçidi araşdırması UKC, ATT&CK və cihaz qeydləri istəyir. Başqa kafedralarda eyni kampaniyanın olub-olmadığını axtarmaq üçün Diamond Model daha uyğun başlanğıcdır. Heç bir model digərinin bütün suallarına cavab vermir.

Modelləri birgə tətbiq etmək bütün terminləri hər sətirdə təkrarlamaq deyil: bir əsas hadisə reyestri saxlanılır, ona mərhələ, texnika, əlaqə və tədbir sahələri əlavə edilir. Eyni müşahidənin müxtəlif modellərdə görünməsi yeni müstəqil sübut yaratmır: EDR qeydinə həm UKC, həm ATT&CK etiketi verilməsi yenə bir mənbəyə əsaslanır, etibarlılıq qiymətləndirməsində bu asılılıq nəzərə alınmalıdır.

## Tam təhlil: universitetdə fidyə proqramı insidenti

### Mühit və müşahidələr

Bu bölmədəki hadisə, tarixlər, vaxtlar, hesablar, həcm və hədəflər tədris üçün şərtidir; ssenari heç bir real universitet insidentini təsvir etmir. Məqsəd eyni sübut dəstinin müxtəlif modellərlə necə işlənəcəyini göstərməkdir. Universitetdə lms.uni.example tədris platforması, files.uni.example fayl xidməti və ayrıca tələbə bazası var. Kafedra cihazı 10.20.5.24, fayl serveri 10.30.0.12, ehtiyat nüsxə idarəsi ayrı seqmentdədir.

Fayl serverində svc-arxiv xidməti hesabı istifadə olunur; onun bəzi kafedra qovluqlarında ehtiyacdan geniş yazma hüququ var. Köhnə inzibati skriptdə saxlanan sirri kafedra cihazındakı adi hesab oxuya bilir. Bu konfiqurasiya səhvi yanal keçid üçün imkan yaradır. Tələbə bazasının şəbəkə qaydaları daha dardır: kafedra cihazından birbaşa bağlantı buraxılmır; nüsxə idarəsi üçün də ayrı hesab tələb olunur.

| Vaxt (UTC+04:00) | Müşahidə | Sübut mənbəyi |
| --- | --- | --- |
| 09:10 | Kafedra əməkdaşına Cədvəl.zip əlavəli məktub çatır | Poçt şlüzü və məktub nüsxəsi |
| 09:12 | İstifadəçi arxivdəki Cədvəl.exe faylını açır, PowerShell başlayır | EDR proses ağacı və fayl qeydi |
| 09:14 | İcazəsiz tapşırıq yaranır, xarici HTTPS əlaqəsi başlayır | Tapşırıq auditi, EDR və proksi |
| 09:20 | Daxili paylaşmalar axtarılır, skriptdən svc-arxiv sirri oxunur | Proses, fayl girişi və sonrakı sessiya təhlili |
| 09:28 | Həmin hesabla files.uni.example üzərində SMB sessiyası açılır | Server girişləri və şəbəkə qeydləri |
| 09:32 | Kafedra sənədləri bir arxivdə toplanır | Server proses və fayl qeydləri |
| 09:39 | Xarici ünvana böyük ötürmə var, arxiv oxunması ilə üst-üstə düşür | Proksi və proses telemetriyası |
| 09:44 | Fayl serverində sənədlər kütləvi şifrələnir, fidyə qeydi yazılır | EDR, fayl nümunələri və fidyə mətni |
| 09:46 | SOC cihazı və serveri təcrid edir, hesab sessiyalarını kəsir | Cavab əməliyyatlarının auditi |
| 10:05 | Tələbə bazasına keçid cəhdinin rədd edildiyi müəyyənləşir | Seqmentlərarası firewall və baza qeydləri |

Son sətirdə 10:05 cəhdin baş vermə vaxtı deyil, araşdırmada onun müəyyən edildiyi vaxtdır; ilkin cəhdin vaxtı xam qeyddə ayrıca saxlanılır. Bu fərq hücumun təcriddən sonra davam etməsi barədə səhv nəticənin qarşısını alır. Nüsxə sisteminin də qeyd və bütövlük yoxlaması aparılır; ona girişin görünməməsi yalnız toplanan mənbələrin əhatəsində qiymətləndirilir.

Aşağıdakı sətirlər tədris üçün normallaşdırılmış şərti hadisələrdir, konkret məhsulun xam formatı deyil (xarici ünvan 198.51.100.24, domen yenileme-kurs.example ssenari üçündür):

```text
09:12 host=kafedra24 user=leyla action=process_start image=powershell.exe parent=Cedvel.exe
09:14 host=kafedra24 action=task_create name=KursUpdate creator=leyla target=powershell.exe
09:14 host=kafedra24 action=network_connect dst=198.51.100.24 port=443 domain=yenileme-kurs.example
09:28 host=files01 action=logon result=success type=3 user=svc-arxiv src=10.20.5.24
09:44 host=files01 action=mass_file_change result=encrypted process_id=4312 scope=kafedra_share
09:46 host=files01 action=isolate result=success operator=soc
```

İlk iki qeyd arasında proses və istifadəçi əlaqəsi var. Üçüncü qeyd C2 ehtimalını artırır, lakin təkcə port 443 C2-ni sübut etmir; fayl təhlili və prosesin bu əlaqədən idarə olunduğuna dair tapıntılar nəticəni gücləndirir. Uğurlu şəbəkə girişi serverdə kod icrasını ayrıca təsdiq etmir; serverin proses qeydləri bu boşluğu doldurur. Eyni proses identifikatoru vaxtla birlikdə işlənir, çünki identifikator sonradan təkrar verilə bilər.

### Cyber Kill Chain və UKC ilə xəritə

| Mərhələ | Ssenaridə nəticə | Müdafiə dərsi |
| --- | --- | --- |
| Kəşfiyyat | Kafedra ünvanının necə seçildiyi məlum deyil | Açıq məlumat və poçt hədəfləri araşdırılır |
| Silahlanma | Hazırlanmış fayl əldə edilib, hazırlanma prosesi görünmür | Nümunə təhlili ilə icra məhdudiyyəti yaxşılaşdırılır |
| Çatdırılma | Arxivli məktub çatıb | Əlavə siyasəti və karantin qaydası yenidən yoxlanır |
| İstismar | İstifadəçi icrası təsdiqlənib, proqram zəifliyi sübut olunmayıb | Təhlükəli icra yoluna nəzarət lazımdır |
| Quraşdırma | İcazəsiz tapşırıq yaradılıb | Tapşırıq auditi və icazə nəzarəti gücləndirilir |
| C2 | Proseslə bağlı xarici idarəetmə əlaqəsi təsdiqlənib | Nəzarətsiz çıxış bağlanır |
| Məqsədə yönəlmiş hərəkətlər | Şifrələmə var, məlumat çıxışı ayrıca araşdırılır | Yanal keçid, ixrac və nüsxə qorunması ayrılır |

Xəritə ilk müdaxilə fürsətinin poçt və icra nəzarəti olduğunu göstərir. Lakin daxili sirrin oxunması, xidmət hesabı və serverə keçid son sətrə yığılır; əhatəni müəyyən etmək üçün UKC ilə daha detallı siyahı hazırlanır.

| № | Faza | Sübut və ya açıq məsələ |
| --- | --- | --- |
| 1 | Kəşfiyyat | Müşahidə edilməyib; ünvanın əldə edilmə yolu naməlumdur |
| 2 | Resurs hazırlığı | Domen və fayl var; hazırlıq vaxtı və üsulu məlum deyil |
| 3 | Çatdırılma | Məktub və əlavə universitetə çatıb |
| 4 | Sosial mühəndislik | Məktub tədris cədvəli bəhanəsi ilə açmağa sövq edib |
| 5 | İstismar | Ayrıca proqram zəifliyinin istismarı təsdiqlənməyib |
| 6 | Davamlılıq | İcazəsiz planlaşdırılmış tapşırıq tapılıb |
| 7 | Müdafiədən yayınma | Bu faza üçün ayrıca yetərli sübut yoxdur |
| 8 | C2 | Proses və əlaqə təhlili idarəetmə kanalını təsdiqləyib |
| 9 | Körpü yaratma | Tunel və vasitəçi yol aşkarlanmayıb; SMB keçidi bunu sübut etmir |
| 10 | Daxili kəşf | Paylaşmaların axtarışı proses qeydlərində görünür |
| 11 | İmtiyaz artırma | Yerli hüquq artımı sübut olunmayıb; başqa hesabın sirri tapılıb |
| 12 | İcra | Kafedra cihazında və fayl serverində icra təsdiqlənib |
| 13 | Kimlik məlumatlarına giriş | Skriptdəki xidmət sirrinin oxunması və istifadəsi əlaqələndirilib |
| 14 | Yanal hərəkət | Xidmət hesabı ilə fayl serverinə keçid təsdiqlənib |
| 15 | Toplama | Kafedra sənədlərindən arxiv yaradılıb |
| 16 | Məlumatın çıxarılması | Arxiv oxunması ilə böyük ötürmə əlaqəlidir; məzmun tam təsdiqlənməyib |
| 17 | Təsir | Faylların zərərli şifrələnməsi nümunələrlə təsdiqlənib |
| 18 | Məqsədlər | Fidyə tələbi var; ödəniş alınması və digər niyyətlər sübut olunmayıb |

Sirr yalnız yoluxmuş cihazdan silinmir, onun işlədiyi bütün xidmətlər müəyyən edilib dəyişdirilir; fayl serveri də araşdırılır. Tələbə bazasına rədd cavabı həmin cəhdin uğursuz olduğunu göstərir, amma başqa hesab və tətbiq yolu ehtimalını bağlamır. UKC boşluqları yeni axtarış suallarına çevirir.

### Diamond Model, ATT&CK və indikatorlar

**Diamond.** Birinci hadisə: qurban kafedra əməkdaşı və cihazı, imkan zərərli faylın istifadəçi tərəfindən işə salınması, infrastruktur göndərmə hesabı və domen, rəqib naməlum aktor. İkinci hadisə: qurban fayl serveri, imkan oğurlanmış sirrlə uzaq giriş, infrastruktur ələ keçirilmiş kafedra cihazı və şəbəkə yolu. Eyni cihaz bir hadisədə qurban, sonrakında hücum infrastrukturunun hissəsi ola bilər. Analitik poçtdakı əlavə heşindən bütün qəbul edənlərə, domendən proksi bağlantılarına, xidmət hesabından bütün server sessiyalarına keçir; bu keçidlər əlavə təsirlənmiş sistemləri axtarır. Eyni domendən iki kafedraya məktub gəlməsi əlaqəli çatdırılmanı dəstəkləyir, aktorun hüquqi kimliyini göstərmir. Meta-xüsusiyyətlərdə hər hadisənin vaxtı, nəticəsi və mərhələsi ayrıca saxlanılır.

**ATT&CK.** Zərərli əlavə T1566.001, faylın işə salınması T1204.002, PowerShell icrası T1059.001, tapşırıq T1053.005, SMB ilə yanal hərəkət T1021.002, arxiv aləti ilə toplama T1560.001, şifrələmə T1486. Xidmət hesabından sui-istifadə T1078 ilə əlaqələndirilə bilər. Məlumat çıxışına texnika seçmək üçün kanal və davranış dəqiqləşdirilir; naməlum ötürməyə sadəcə xarici trafik olduğu üçün T1041 yazılmır.

**Pyramid of Pain.** İlk tədbirlər məlum fayl heşini və domeni axtarmaqdır. Sonrakı iş adlara bağlı olmayan davranışı tutmaqdır: istifadəçi faylından interpretatorun başlaması, tapşırıq yaradılması, yeni xidmət hesabı sessiyası. Hücumçu domeni dəyişəndə bu əlaqələrin bəziləri qalır. Qanuni inzibati işlər nəzərə alınmaqla test edilməyən davranış qaydası dərhal sərt bloklama rejiminə qoyulmur.

### D3FEND, arxitektura və CSF üzrə tədbirlər

**D3FEND** zərərli faylı, proses ağacını, şəbəkə əlaqəsini və hesab sessiyasını ayrı müdafiə obyektləri kimi götürür: fayl və proses təhlili icranı izah edir, trafik süzülməsi C2 yoluna təsir edir, təcrid yayılmanı məhdudlaşdırır, kimlik məlumatlarının sərtləşdirilməsi xidmət sirrinin qorunmasını və istifadə şərtlərini dəyişir. Tədbirlərin hər biri öz testi ilə yoxlanır; adın D3FEND-də olması işi tamamlamır.

**Çoxsəviyyəli müdafiə.** Poçt və cihaz qatları bu yolu dayandıra bilməyib; sirrin zəif qorunması və geniş yazma hüququ daxili keçidi mümkün edib; tələbə bazasının ayrıca sərhədi müşahidə olunan bir cəhdi rədd edib; ayrı nüsxə idarəsi şifrələnmiş faylları bərpa etmək imkanı verib. Müdafiə ya tam uğurlu, ya tam uğursuz kimi qiymətləndirilmir; hər qatın nəticəsi ayrı göstərilir.

**Sıfır etibar.** Sual: kafedra cihazından xidmət hesabı ilə fayl serverinə bu əməliyyat niyə verilir? Xidmət hesabı yalnız müəyyən server və prosesdən işləməli idisə, adi iş stansiyasından girişi rədd edilməli idi; icazə verilən paylaşmalar və yazma əməliyyatları da daraldılır. Şəbəkə yerinə əsaslanan etibar konkret resurs və əməl siyasəti ilə əvəz olunur. Qanuni arxiv işinin davamı ayrıca yoxlanır.

**CSF.** Govern məsul şəxsi, xidmətin dayandırılması səlahiyyətini və bərpa prioritetini müəyyən edir. Identify eyni sirrin istifadə olunduğu yerləri və təsirlənmiş sənədləri tapır. Protect hesabları ayırır, sirri dəyişir, icra yolunu daraldır. Detect poçt, cihaz və server əlaqəsini qaydaya çevirir. Respond təcridi, sübutların qorunmasını və əhatə təhlilini aparır. Recover təmiz qurulmuş serverə yoxlanmış nüsxəni qaytarır və xidmət sahibi ilə nəticəni təsdiqləyir.

Bərpa yalnız şifrələnmiş faylların üzərinə köhnə faylları yazmaq deyil: davamlılıq mexanizmi aradan qaldırılır, hesablar və sirrlər yenilənir, bərpa mənbəyinin hücumdan əvvəlki etibarlı vəziyyəti yoxlanır. Şərti hədəf kimi fayl xidməti üçün RTO 6 saat, RPO 4 saat seçilibsə, faktiki dayanma və itən dəyişiklik intervalı bu hədəflərlə müqayisə edilir. **RTO** xidmətin bərpası üçün hədəf vaxt, **RPO** qəbul edilən məlumat itkisinə uyğun bərpa nöqtəsi hədəfidir. Nüsxənin mövcudluğu bu hədəflərə çatıldığını göstərmir. Məlumat çıxışı araşdırması bərpadan sonra da davam edə bilər: şifrələnmiş faylların açılması məxfilik problemini həll etmir; hesabatda təsdiqlənən məzmun, ehtimal olunan çıxış və müəyyən edilə bilməyən hissə ayrılır, qalıq riskin sahibi qərar verir.

## Aşkarlama qaydasını hazırlamaq və yoxlamaq

### Qaydanın texniki və əməliyyat hissəsi

Aşkarlama mühəndisliyi (detection engineering) hücum fərziyyəsini işlək, yoxlanmış və idarə olunan qaydaya çevirməkdir. İlkin fərziyyə: istifadəçi cihazında planlaşdırılmış tapşırıq vasitəsilə PowerShell-in başladılması araşdırılmalıdır. Bu mənbə seçiminə çevrilir: Windows-da uyğun audit siyasəti açıldıqda Security jurnalındakı 4698 planlaşdırılmış tapşırığın yaradılmasını göstərir; tapşırıq məzmununun kollektor tərəfindən saxlanması da yoxlanmalıdır.

Aşağıdakı Sigma nümunəsi tədris üçündür: yalnız tapşırıq məzmununda powershell.exe olan yaradılmaları seçir. Konkret SIEM-ə çevirmə, XML sahələrinin ayrışdırılması və yerli audit sazlaması ayrıca yoxlanmalıdır; nümunənin işlək sistemdə yoxlanıldığı iddia edilmir.

```yaml
title: PowerShell ile planlasdirilmis tapsiriq
status: experimental
description: Tedris ucun serti askarlama numunesi
logsource:
  product: windows
  service: security
detection:
  selection:
    EventID: 4698
    TaskContent|contains: 'powershell.exe'
  condition: selection
falsepositives:
  - Tesdiqlenmis inzibati avtomatlasdirma
level: medium
tags:
  - attack.t1053.005
```

Qayda hücum hökmü vermir: analitik tapşırığı yaradan hesabı, cihazın rolunu, skript yolunu, imzanı və dəyişiklik qeydini yoxlayır. Bütün administratorları istisnaya çıxarmaq təhlükəlidir; istisna konkret təsdiqlənmiş tapşırığa, cihaz qrupuna və müddətə daraldılır. Qayda sənədində sahibi, tələb olunan mənbələr, cavab addımları və məlum kor nöqtələr saxlanılır.

### Təhlükəsiz yoxlama və ölçmə

İdarə olunan yoxlama istehsalat tələbə bazasında real fidyə proqramı işlətmək deyil. Ayrı laboratoriyada həssas məlumat daşımayan fayllarla gözlənilən telemetriya və xəbərdarlıq sınanır. Zərərsiz test tapşırığı yaradılıb silinə bilər, lakin onun hansı proseduru təmsil etdiyi sənədləşdirilir. Eyni mühitdə qanuni inzibati tapşırıq da yoxlanır ki, qaydanın yanlış müsbət nəticələri görünsün.

Şərti testdə gözlənilən 10 sınaqdan 8-i xəbərdarlıq yaradır, 2-si məlumat gecikməsinə görə görünmürsə, nəticə “tam örtük” deyil. Gecikmənin mənbə, ötürmə və ya qayda pəncərəsində olduğu ayrılır; aşkarlamadan təcridə qədər vaxt da ölçülür. Mənbə susmasını izləmək ayrıca tələbdir: qaydanın məntiqi düzgün olsa da, hadisə gəlməyəndə işləyə bilməz.

Müdafiə yoxlamasında nəticə, sübut və məhdudiyyət birlikdə saxlanılır. ATT&CK texnikası davranışı, UKC onun hadisədəki yerini, Diamond əlaqələri, D3FEND müdaxiləni, CSF isə çatışmazlığa görə məsuliyyəti göstərir. Testdən sonra reyestr və uyğun vizual qat yenilənir.

## Köhnə slaydlarla fərq

:::note Köhnə slaydlarla fərq
Köhnə slaydlarda UKC “Kill Chain və Diamond-un inteqrasiyası” kimi təqdim olunurdu; düzgünü UKC-nin əsasən Kill Chain və ATT&CK-ı birləşdirməsidir. UKC-nin 2-ci mərhələsi “Silahlanma” deyil, “Resurs hazırlığı (Resource Development)” adlanır; köhnə “Target Manipulation” isə “Impact” olub.
:::
