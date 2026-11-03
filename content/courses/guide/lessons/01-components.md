+++
title = "Bir dərsin tikinti blokları"
unit = "authoring"
order = 1
summary = "Burada dərs düz mətnlə məhdudlaşmır: sxem, addım-addım proses, təkrar kartı, uyğunlaşdırma və izahlı sual eyni səhifədə yaşayır."
objectives = ["Bələdçi"]
updated = 2026-11-03

[[source]]
title = "content/README.md — dərs yazma qaydaları"
note = "Bu səhifədəki hər komponentin tam sintaksisi oradadır."
+++

Bu səhifə **komponent bələdçisidir**. Əsl dərs deyil; dərs yazan hər kəsin bir dərsin necə görünəcəyini bir baxışda görməsi üçündür. Hər bölmə bir komponenti göstərir, onu yaradan sintaksis isə `content/README.md` faylında izah olunur.

## Mətn və vurğu

Abzaslar oxunaqlı enlikdə qalır. Mətnin içində **qalın**, *kursiv*, ==vurğulanmış ifadə== və `inline code` istifadə oluna bilər. Klaviatura qısayolları düymə kimi görünür: ++Ctrl+Shift+Esc++ və ya ++Win+R++. Xarici keçidlər yeni tabda açılır: [Wikipedia](https://az.wikipedia.org).

### Siyahılar

- Sırasız siyahı bəndi
- İç-içə siyahı da olur:
  - ikinci səviyyə bəndi
  - bir dənə də
- Son bənd

1. Nömrəli siyahı
2. Sıra vacib olanda
3. İstifadə olunur

> Sitat bloku: mənbədən birbaşa köçürülən cümlə üçün.

## Xəbərdarlıq qutuları

:::note
Ümumi qeyd. Axını kəsmədən əlavə məlumat verir.
:::

:::tip Yadda saxlama texnikası
Bir anlayışı öz cümlənlə izah edə bilmirsənsə, hələ öyrənməmisən.
:::

:::warning
Tez-tez edilən səhv və ya qarışdırılan iki anlayış üçün.
:::

:::exam
İmtahanda necə soruşulduğu, hansı tələlərin olduğu. Aralıq imtahanına hazırlıqda ən çox istifadə olunacaq qutu budur.
:::

:::example
Konkret ssenari: bir problem qoyulur, addım-addım həll olunur.
:::

## Cədvəl

| Komponent | Nə üçündür | İnteraktiv |
| --- | --- | :---: |
| `steps` | Ardıcıl prosesi addım-addım göstərir | Bəli |
| `flashcards` | Aktiv xatırlama üçün kartlar | Bəli |
| `quiz` | İzahlı çoxseçimli suallar | Bəli |
| `match` | İki siyahını uyğunlaşdırmaq | Bəli |
| `terms` | Abreviatura və termin lüğəti | Xeyr |

## Sxem

:::figure
src = "lesson-anatomy.svg"
alt = "Dərs səhifəsinin anatomiyası: solda dərs siyahısı, ortada məzmun, sağda başlıq xəritəsi."
caption = "Dərs səhifəsinin üç sütunu. Şəklə klikləyəndə böyüyür."
wide = true
:::

## Kod bloku

```bash
# Saytı məzmundan yığ
python3 tools/build.py
```

## Addım-addım proses

:::steps Yeni dərs əlavə etmək
[[step]]
title = "Faylı yarat"
body = "`content/courses/<fənn>/lessons/` qovluğunda `03-movzu-adi.md` adlı fayl aç. Əvvəldəki nömrə yalnız faylların sıralanması üçündür."

[[step]]
title = "Frontmatter-i doldur"
body = "`+++` sətirlərinin arasına başlıq, bölmə, sıra, xülasə və ən azı bir mənbə yazılır. Sahə çatışmırsa, build dayanır və sətir nömrəsini deyir."

[[step]]
title = "Məzmunu yaz"
body = "Markdown və bu səhifədəki komponentlər. Xam HTML qəbul olunmur; beləliklə bütün dərslər eyni dizaynda qalır."

[[step]]
title = "Yığ və yoxla"
body = "`python3 tools/check.py` işə sal. Keçirsə, dərs sayta əlavə olunub."
:::

## Terminlər

:::terms Abreviaturalar
[[term]]
name = "TOML"
full = "Tom's Obvious Minimal Language"
def = "Frontmatter və komponent məlumatı üçün istifadə olunan, səhvi asan tutulan konfiqurasiya dili."

[[term]]
name = "Direktiv"
def = "`:::` ilə açılıb bağlanan, mətnin içinə komponent yerləşdirən blok."

[[term]]
name = "Active recall"
full = "Aktiv xatırlama"
def = "Məlumatı yenidən oxumaq əvəzinə yaddaşdan çağırmağa çalışmaq. Kartlar və suallar bunun üçündür."
:::

## Əvvəl düşün, sonra bax

:::reveal Niyə dərsdə xam HTML qadağandır?
Çünki dərsləri müxtəlif adamlar və agentlər yazacaq. Xam HTML-ə icazə verilsə, hər biri öz işarələməsini yaradar və dizayn dağılar. Yalnız Markdown və müəyyən komponentlər qəbul olunanda görünüş bir yerdən, yəni stil faylından idarə olunur.
:::

## Təkrar kartları

:::flashcards
[[card]]
front = "Bir dərsdə ən azı neçə mənbə olmalıdır?"
back = "**Bir.** Mənbəsiz dərs build-dən keçmir."

[[card]]
front = "Komponent məlumatı hansı dildə yazılır?"
back = "TOML. Səhv olsa, build sətir nömrəsi ilə dayanır."

[[card]]
front = "Dərsin tamamlanma vəziyyəti harada saxlanılır?"
back = "Brauzerin yerli yaddaşında (`localStorage`). Server yoxdur, hesab yoxdur; hər kəsin irəliləyişi öz brauzerində qalır."
:::

## Uyğunlaşdırma

:::match Komponenti məqsədi ilə uyğunlaşdır
[[pair]]
left = "`steps`"
right = "Ardıcıl proses"

[[pair]]
left = "`flashcards`"
right = "Aktiv xatırlama"

[[pair]]
left = "`terms`"
right = "Abreviatura lüğəti"

[[pair]]
left = "`reveal`"
right = "Əvvəl düşün, sonra cavaba bax"
:::

## Özünü yoxla

:::quiz
[[question]]
prompt = "Build tanımadığı direktivlə qarşılaşanda nə edir?"
choices = ["Onu görməzdən gəlir", "Düz mətn kimi çap edir", "Xəta verir və sətir nömrəsini deyir", "Standart bir qutu çəkir"]
answer = 3
explain = "Səssizcə keçmək xarab dərsin hiss olunmadan yayımlanması deməkdir. Ona görə tanınmayan hər şey **xətadır**."

[[question]]
prompt = "Aşağıdakılardan hansılar dərsin frontmatter-ində **məcburidir**?"
choices = ["title", "objectives", "source", "unit"]
answer = [1, 3, 4]
explain = "`title`, `unit`, `order`, `summary` və ən azı bir `source` məcburidir. `objectives` istəyə bağlıdır, amma imtahan fənlərində istifadəsi gözlənilir."

[[question]]
prompt = "Dərsə şəkil əlavə etmək üçün fayl hara qoyulur?"
choices = ["Dərsin yanına, lessons/ qovluğuna", "Fənnin media/ qovluğuna", "src/assets/img/ qovluğuna", "İstənilən yerə, tam yol yazılır"]
answer = 2
explain = "Şəkillər fənnin `media/` qovluğunda durur; `lessons/` içində `.md`-dən başqa fayl build-i dayandırır."
:::
