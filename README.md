# Qrup 596

596-cı magistr qrupunun imtahanlara birlikdə hazırlaşmaq üçün açıq öyrənmə saytı. Hər fənn ana
səhifədə bir kartdır; fənnin içində bölmələr və dərslər var. Dərslər oxunuşu sxemlər, addım-addım
proseslər, təkrar kartları, uyğunlaşdırma və izahlı testlərlə birləşdirir. İrəliləyişin yalnız öz
brauzerində (`localStorage`) saxlanılır: hesab yoxdur, server yoxdur.

**Sayt:** https://kulieff21.github.io/qrup-596/

## İstifadə

Sadəcə saytı aç. Klaviatura: `Ctrl+K` və ya `/` axtarış, `Space` kartı çevirir, ox düymələri
kartlar arasında keçir.

## Lokal işə salmaq

```bash
python3 tools/build.py      # content/ + src/ -> site/
python3 tools/serve.py      # http://localhost:4173
```

Python 3.12+, yalnız standart kitabxana.

## Məzmun əlavə etmək

Hər şey [`content/README.md`](content/README.md) faylındadır (qısaca: hər fənn üçün bir
`course.toml`, hər dərs üçün TOML frontmatter-li bir Markdown faylı, komponentlər `:::direktiv`
kimi yazılır). Xam HTML qəbul olunmur, ona görə bütün dərslər eyni görünür.

Commit-dən əvvəl:

```bash
python3 tools/check.py      # parser self-test + build + keçid yoxlaması
```

`main` budağına hər push saytı GitHub Actions ilə yenidən yığıb GitHub Pages-ə yayımlayır.

## Struktur

| Yol | Nədir |
| --- | --- |
| `content/` | Fənlər, dərslər, şəkillər |
| `src/templates/`, `src/assets/` | Səhifə şablonu, CSS, JS, şriftlər |
| `tools/md.py` | Markdown alt dəsti və direktiv renderer |
| `tools/build.py` | Sayt generatoru |
| `tools/selftest.py` | Parserin pozulmamalı qaydaları |
| `tools/check.py` | Commit-dən əvvəlki yoxlama |
| `tools/pdfpages.py` | Mühazirə PDF-indən səhifə aralığının mətnini çıxarır |
| `tools/shoot.mjs` | Vizual yoxlama üçün headless Chrome ekran görüntüləri |
| `site/` | Yığılmış nəticə, commit olunmur |
