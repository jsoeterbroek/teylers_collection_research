# Analysis of Teylers PP 0121: *Portret van Adriaen Blyenburg*

**Source record:** <https://teylers.adlibhosting.com/ais6/Details/museum/39224>
**Date of analysis:** 2026-03-06
**Time of analysis:** 10:20
**AI model:** claude-opus-4.6

---

## Object Description

This is an etching by Samuel van Hoogstraten (1627–1678), depicting Adriaen van Blyenburg half-length, facing forward, holding a parchment roll. It exists in 2 states; Teylers holds state 2 (the final published version with text). The Rijksmuseum holds an impression of the same state (RP-P-OB-12.792). Plate dimensions match almost exactly: Teylers 201×149mm vs Rijksmuseum 200×147mm.

## Teylers Catalog Record

| Field | Value |
|-------|-------|
| Object number | PP 0121 |
| Title | Portret van Adriaen Blyenburg |
| Creator | Samuel van Hoogstraten (1627-1678), graveur |
| Description | Portret van Adriaen Blyenburg, ten halve lijve van voren gezien. In zijn handen een rol perkament. Staat 2 van 2. |
| Subject | medicus |
| Persons keyword | Blyenburg, Adriaen |
| Object name | grafiek |
| Collection | Panpoeticon Batavum |
| Material | papier |
| Technique | gravure |
| Dimensions | plaatrand: 201×149 mm, papier: 209×154 mm, opzet: 463×314 mm |
| Inscription | FOL 124 / "Dit's BLYENBURG, die... Vrijheijt heeft geplant." (6 lines) / S.V.Hoogstraten. / N. 1589 Ol. 1639 / Zie van der An |

## Hidden Metadata (from HTML source, not visible on page)

- **`<meta name="description">`** — Concatenation of title and full description text
- **`<meta name="author">`** — `Hoogstraten, Samuel van (1627-1678)`
- **`<meta name="keywords">`** — `grafiek;papier`
- **`<meta http-equiv="content-language">`** — Reveals a template bug: `aa<%= AISHelpers.CurrentUICultureShort %>` (unresolved ASP.NET expression leaked into HTML)
- **Hidden input: `ais-detail-priref`** — value `39224` (internal Adlib priref/record ID)
- **Hidden input: `ais-database-name`** — `museum`
- **Hidden input: `ais-datasource-value`** — `museum`
- **Hidden input: `ais-request-database-name`** — `itemrequests` (separate database for loan/reservation requests)
- **Full-resolution image URL** (in `data-original` attribute):
  `https://teylers.adlibhosting.com/ais6/Content/GetContent?command=getcontent&server=images&value=PP 0121.jpg&folderId=39224&imageformat=jpg`
- **Image alt text** contains structured info: `PP 0121 <br/> Portret van Adriaen Blyenburg <br/> <em>Hoogstraten, Samuel van (1627-1678)</em>`
- **XML namespace** — `xmlns:str="http://xsltsl.org/string"` confirms page rendered via XSLT transformation from Adlib XML source

### Notable absences in metadata

- No Open Graph tags (`og:title`, `og:image`, etc.)
- No JSON-LD or schema.org structured data
- No Dublin Core metadata
- No RDF or linked data
- No rights/license information
- No date of creation for the artwork itself
- No acquisition/provenance information exposed
- The WWWOPAC API endpoint (`wwwopac.ashx`) is disabled/redirects to error

## Image File EXIF/XMP Metadata

| Field | Value |
|-------|-------|
| Format | JPEG, 555×750 (served), original 8000×7762 TIFF |
| Resolution | 300 DPI |
| Camera | Better Light Model Super8k (scanning camera) |
| Photographer | JanB |
| Exposure | 1/120 s, ISO 200 |
| Date digitized | 2011-10-10 13:50:00 |
| Software | Adobe Photoshop CS5 Macintosh |
| Last modified (XMP) | 2012-01-24 18:10:29 CET |
| IPTC Keywords | Collectie Kunst, PP 0121.tif |
| Copyright | Teylers Museum Haarlem the Netherlands |
| EXIF ImageDescription | **PP 0119** (mismatch — see findings below) |
| Original filename | Collectie Kunst PP 0121.tif |
| XMP DocumentID | xmp.did:123DA75E20206811871F98CA3A25FBE2 |

## Key Findings Not in Teylers' Record

### 1. WRONG SUBJECT CLASSIFICATION: "medicus" is incorrect

This is the most significant error. Teylers catalogs the subject as **"medicus" (physician)**. He was not a physician at all. Based on extensive biographical sources:

**The subject is Mr. Adriaen V Jacobsz van Blyenburg** (born Dordrecht, 8 October 1589 — died Dordrecht, 10 November **1630**), who was:

- **Lord of Naaldwijk**
- **Jurist** — studied law at Leiden (1605), licensed at Poitiers (1609)
- **Warden of the Mint of Holland** (from 1609), Master Minter (from 1616)
- **Councillor** of Dordrecht (1616-17)
- **Alderman** (schepen, 1623-24)
- **Schout** (chief magistrate) of Dordrecht (1626)
- **Knight of the Order of Saint Michael** (French royal order)

The Rijksmuseum correctly identifies him as **"schout van Dordrecht"** — not a physician. The "medicus" label at Teylers is a cataloging error.

### 2. DEATH DATE DISCREPANCY: "Ol. 1639" vs actual 1630

The inscription on the print reads **"N. 1589 Ol. 1639"** — meaning "Natus (born) 1589, Obiit (died) 1639." But all historical sources agree Adriaen V died on **10 November 1630**, not 1639. This is either:

- An error by Van Hoogstraten (who was only 3 when Blyenburg died, so he worked from second-hand information)
- A confusion with another family member
- A misreading of the source (1630 → 1639)

This date error appears to be **on the original print itself**, making it a 17th-century factual error baked into the copperplate.

### 3. "Zie van der An" inscription identified

The inscription note "Zie van der An" is a later annotation (possibly by a collector) referring to **A.J. van der Aa**, *Biographisch Woordenboek der Nederlanden* (1852–1878), which contains entries on the Blyenburg family. This dates the annotation to post-1852, establishing provenance context.

### 4. Technique misidentified

Teylers catalogs this as **"gravure" (engraving)**. The Rijksmuseum correctly catalogs it as **"ets" (etching)**. These are different intaglio techniques — etching uses acid to bite the plate, while engraving uses a burin to cut directly. Van Hoogstraten was known primarily as an etcher, not an engraver.

### 5. EXIF mismatch: wrong object number in scan metadata

The image file's EXIF `ImageDescription` field reads **"PP 0119"** but the catalog object number is **PP 0121**. This suggests either a labeling error during the 2011 digitization session by photographer "JanB", or that the scan was originally cataloged under a different number.

### 6. Panpoeticon Batavum context

Teylers purchased what remained of the Panpoeticon Batavum collection at auction in **1808** for 200 guilders (via Wybrand Hendriks). The "PP" prefix in the object number confirms this print belongs to that collection. The Panpoeticon was originally assembled by Arnoud van Halen (c. 1700) as a cabinet of portraits of Dutch poets and writers — confirming the Blyenburgs were included for their **literary/poetic contributions**, not medical ones. Multiple family members were known Latin poets.

### 7. Hollstein catalog reference missing from Teylers

The print is documented in the standard reference catalog as **Hollstein Dutch 7-1(2)** and **FMH 483**. These references are absent from Teylers' record.

### 8. Full family identification

The subject comes from one of Dordrecht's most prominent regent families. His father was Jacob Adriaensz van Blyenburg (1562–1609); his grandfather was Mr. Adriaen III (1532–1582) who secretly facilitated the Watergeuzen's capture of Dordrecht in 1572, a pivotal moment in the Dutch Revolt. His son was Mr. Adriaen VI (1616–1682), burgemeester and tutor to the young Prince William III of Orange.

---

## Summary of Errors and Omissions in Teylers' Catalog

|           | Issue | Teylers says | Should be |
|-----------|-------|--------------|-----------|
| Serious   | Subject classification | medicus (physician) | jurist / schout / regent |
| Serious   | Technique | gravure (engraving) | ets (etching) |
| Serious   | Death date (on print) | 1639 (via "Ol. 1639") | 1630 (historical record) |
| Minor     | Hollstein reference | missing | Dutch 7-1(2), FMH 483 |
| Minor     | EXIF object number | PP 0119 | PP 0121 |
| Minor     | Full subject identity | not specified | Mr. Adriaen V Jacobsz van Blyenburg, Lord of Naaldwijk |

---

## Object Comparison

The Rijksmuseum holds an impression of the same print:

| Field | Teylers (PP 0121) | Rijksmuseum (RP-P-OB-12.792) |
|-------|-------------------|-------------------------------|
| Technique | gravure (engraving) | ets (etching) |
| Subject ID | medicus | schout van Dordrecht |
| Plate dimensions | 201×149 mm | 200×147 mm |
| Date range | not specified | 1648–1677 |
| Hollstein ref | not listed | Dutch 7-1(2), FMH 483 |
| Persistent URL | — | https://id.rijksmuseum.nl/200128041 |

---

## Sources

- [Teylers Museum: PP 0121 Detail Page](https://teylers.adlibhosting.com/ais6/Details/museum/39224)
- [Rijksmuseum: Portret van Adriaen van Blijenburgh (RP-P-OB-12.792)](https://www.rijksmuseum.nl/en/collection/object/Portret-van-Adriaen-van-Blijenburgh--6fb92d993299fbdcab35bcfe28d2b068)
- [Regionaal Archief Dordrecht: Familie Van Blijenburg](https://www.regionaalarchiefdordrecht.nl/dordts-biografisch-woordenboek/familie-van-blijenburg/)
- [DBNL: Van der Aa, Biographisch Woordenboek — Blyenburg](https://www.dbnl.org/tekst/aa__001biog02_01/aa__001biog02_01_0936.php)
- [Winkler Prins 1870: Blyenburg](https://www.ensie.nl/winkler-prins-1870/blyenburg)
- [Schrijverskabinet: Samuel van Hoogstraten & Panpoëticon](https://www.schrijverskabinet.nl/artikel/samuel-van-hoogstraten/)
- [Stichting Familie van Hoogstraten: Panpoëticon](https://www.vanhoogstraten.org/nieuws/panpoeticon-batavum/)
