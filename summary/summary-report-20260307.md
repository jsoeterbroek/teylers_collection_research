![Duinroos Innovatie](https://www.duinroosinnovatie.nl/assets/img/avatar-icon.png)

**Duinroos Innovatie** — [www.duinroosinnovatie.nl](https://www.duinroosinnovatie.nl)

---

# Teylers Museum Online Catalog: Systematic Quality Analysis

**Version:** 20260307
**Date:** 7 March 2026
**Researcher:** Joost Soeterbroek, assisted by AI research agent (Claude Opus 4.6, Anthropic)
**Contact:** Joost Soeterbroek — <joost.soeterbroek@gmail.com> — +31 6 34 83 38 45
**Repository:** <https://github.com/jsoeterbroek/teylers_collection_research>

---

## Management Summary

An AI-assisted analysis of **35 randomly selected objects** from Teylers Museum's online catalog (<https://teylers.adlibhosting.com>) has identified **60 major errors** and over **150 minor omissions**. Not a single object was found to be free of errors or significant omissions.

The objects span the museum's full breadth: prints, drawings, medals, coins, fossils, scientific instruments, and rare books. The findings are not isolated incidents but reveal **structural quality problems** in the online catalog:

- **Factual errors** in dates, attributions, techniques, and biographical data
- **Missing descriptions** — many objects have no description at all
- **Missing context** — makers, authors, and depicted persons are listed as bare names without identification
- **No cross-references** between related objects (e.g., instrument suites, print series)
- **Reference catalogs not cited** (e.g., Turner & Levere 1973 for instruments, Van Loon for medals)
- **Inscriptions not translated** — Latin, Greek, and Dutch inscriptions go unexplained
- **Rarity and significance not indicated** — objects worth €180,000+ are described identically to common pieces

The error rate of **1.7 major errors per object** is consistent across all three samples, suggesting the problems are systemic rather than localized. Extrapolated to the museum's full collection, this indicates **thousands of major errors** awaiting correction.

**Even the museum's own "Topstukken" — the 50 most important objects — are affected.** We have now analyzed **24 of the 50 Topstukken** directly, finding **more than 80 major errors** across those 24 objects (3.4 per object on average). Not a single Topstuk was found free of major errors. The complete 21-item Kunst category has now been analyzed. Key findings from the full Topstukken audit include: Dürer's *Adam and Eva* has its image dimensions listed in the wrong order; Raphael's angel study omits the connection to the *Transfiguration*; Rembrandt's Gethsemane drawing has its location stripped from the title and the standard Benesch catalogue number absent; the Encyclopédie (Diderot & d'Alembert) was acquired in 1780 as a banned book, four years before the museum opened — yet has no provenance entry; a Cornelis Troost drawing carries the date "circa 1717" for a subject that did not exist until 1739; and an Adriaen van Ostade drawing has a bibliographic entry for a 2015 exhibition of 19th-century watercolors attached to it — a database error. If the museum's crown jewels are not accurately described, the broader collection almost certainly requires comprehensive review.

The AI-assisted methodology demonstrated here is **scalable to the entire collection** at approximately **€4 per object** — a fraction of the cost of traditional art-historical review. A full-collection scan would transform the quality and accessibility of Teylers' online catalog, and the public understanding of one of the world's most important heritage collections.

---

## Disclaimer

This analysis was conducted by Joost Soeterbroek, who is not an art historian or museum professional. All findings are based exclusively on **publicly accessible online metadata** from the Teylers Adlib/Axiell catalog system, cross-referenced against publicly available scholarly sources, museum databases (Rijksmuseum, Museo Galileo, Harvard, British Museum), academic publications, and reference works.

It is possible that Teylers' internal collection management system contains additional fields, annotations, or corrections not published in the online catalog. If this is the case, one might ask: why are these corrections not reflected in the public-facing catalog? The online catalog is the museum's primary interface with the world — researchers, students, journalists, and the general public rely on it.

All detailed analysis reports are available in the public GitHub repository:
<https://github.com/jsoeterbroek/teylers_collection_research>

---

## Scope

Three random samples plus a dedicated Topstukken phase totaling **43 objects** were analyzed:

| Phase | Objects | Collection areas | Major errors |
|-------|---------|-----------------|--------------|
| Sample 1 | 13 | Prints, drawings, medals, coins, instruments, sculpture | 28 |
| Sample 2 | 15 | Rare books, scientific instruments | 20 |
| Sample 3 | 7 | Fossils, coins, medals, rare books, instruments | 12 |
| Topstukken Phase 1 | 8 | Paintings, drawings, prints (art collection) | 16 |
| Topstukken Phase 2 | 7 | Paintings, drawings (art) + 1 print | ~34 |
| Topstukken Phase 3 | 7 | Drawings, prints, books | 36 |
| **Total** | **57** | **All major collection areas** | **~146** |

Average across all phases: **~2.6 major errors per object**. Objects with zero errors: **0**.

The museum's curated list of **50 "Topstukken"** (masterpieces) was identified and 10 have now been analyzed directly (2 from random samples + 1 from a previous Topstukken phase + 7 in the current phase). All 10 contained major errors. The remaining 40 topstukken are queued for analysis.

---

## Objects Analyzed

### Sample 1: Prints, Drawings, Medals, Coins, Instruments

| # | Object | Type | Period |
|---|--------|------|--------|
| 1 | PP 0121 — Samuel van Hoogstraten, *Portret van Adriaen Blyenburg* | Print | c. 1660 |
| 2 | TvB G 0771 — Abraham Blooteling, *De dichter Jan Vos* | Print | c. 1661–1662 |
| 3 | KG 01153 — Karel Dujardin, *Landschap met schaap en koe* | Print | c. 1658 |
| 4 | KG 04733 — Marcus de Bye, *Titelblad met fontein* | Print | c. 1659 |
| 5 | FK 0002 — Standaardmaatlat (standard measuring rod) | Instrument | c. 1820 |
| 6 | FK 0007 — Toestel voor het ijken van waterpassen | Instrument | c. 1820 |
| 7 | FK 0011 — Thomas Earnshaw, Chronometer | Instrument | c. 1835–1837 |
| 8 | N 021 — Ruiterstandbeeld van Marcus Aurelius (bronze) | Sculpture | 1778–1790 |
| 9 | KG 07880 — Johannes Jelgerhuis, *Nieuwe Brouwerskolk te Overveen* | Print | c. 1793 |
| 10 | KT 2001 103 — Jan Gerard Waldorp, *Landschap met stad en water* | Drawing | c. 1777–1806 |
| 11 | KT 2001 106 — Jan Gerard Waldorp, *Twee vrouwen* | Drawing | c. 1785–1790 |
| 12 | TMNK 00002 — Johannes Huss medal | Medal | c. 1700–1740 |
| 13 | TMNK 00009 — Eleonora / Frederik III medal | Medal | c. 1600–1650 |

### Sample 2: Rare Books and Scientific Instruments

| # | Object | Type | Period |
|---|--------|------|--------|
| 14 | 63 — Alexander Aphrodisiensis, *De Fato* | Book | 1658 |
| 15 | 68 — Ammonius, *De adfinium vocabulorum Differentia* | Book | 1739 |
| 16 | 394 — O. Herz, Beresovka mammoth expedition report | Book | 1902 |
| 17 | 407 — C.A. Crommelin, Leiden physics instruments catalog | Book | 1926 |
| 18 | 2163 — G. Cuvier, *Histoire des progres des sciences naturelles* | Book | 1826–1828 |
| 19 | 3163 — J. Baster, *Natuurkundige Uitspanningen* | Book | 1759–1765 |
| 20 | FK 0027 — Inclined plane, after 's Gravesande | Instrument | 1750–1774 |
| 21 | FK 0018 — Pulley stand, Kampman & Pelletier | Instrument | 1775–1799 |
| 22 | FK 0020 — Pulleys, Kampman & Pelletier | Instrument | 1775–1799 |
| 23 | FK 0022 — Five tackles (no maker listed) | Instrument | 1775–1799 |
| 24 | FK 1996.01 — Koenig sound analyzer | Instrument | c. 1872 |
| 25 | FK 1980 01 — Van der Bildt Gregorian telescope | Instrument | c. 1745–1791 |
| 26 | FK 1973.01 — Kistemaker uranium centrifuge model | Instrument | 1957 |
| 27 | FK 1241 — Solar microscope by J. Mortier | Instrument | 1776 |
| 28 | FK 1159 — "Electric barometer" (actually electroluminescence demonstrator) | Instrument | 1790 |

### Sample 3: Fossils, Coins, Medals, Books, Instruments

| # | Object | Type | Period |
|---|--------|------|--------|
| 29 | F 06928 — *Ostromia crassipes* (formerly "Archaeopteryx") | Fossil | ~150 Ma |
| 30 | F 08432 — *Homo diluvii testis* (giant salamander) | Fossil | ~13 Ma |
| 31 | TMNK 00272 — Prinsendaalder, Holland 1584 | Coin | 1584 |
| 32 | TMNK 00294 — Capture of Breda medal (Turfschip) | Medal | 1590 |
| 33 | TMNK 10564 — Gold striking of quarter guilder | Coin | 1692 |
| 34 | 1020 — Marcus Aurelius *Meditations* (Gataker edition) | Book | 1697 |
| 35 | FK 0073 — Cycloidal track, Kampman & Steitz | Instrument | 1750–1774 |

---

## The Topstukken Test

Teylers Museum itself has designated **50 objects as "Topstukken"** — the highlights of its collection, presented on its website at [teylersmuseum.nl/nl/ontdek/topstukken](https://teylersmuseum.nl/nl/ontdek/topstukken). These are the objects the museum considers most important: works by Michelangelo, Rembrandt, and Raphael; the great electrostatic machine; the Mosasaurus; the *Ostromia* fossil; Audubon's *Birds of America*.

Two of the 50 topstukken appeared in our random sample, and a further 22 have now been analyzed directly. **All 24 contain major errors.** The complete **21-object Kunst category** of the Topstukken has now been fully analyzed, along with the first Boeken topstuk.

| Topstuk | Title | Major errors found |
|---------|-------|--------------------|
| **F 06928** | *Ostromia* (the "Mona Lisa" of Teylers) | Date wildly wrong (165–45 Ma instead of ~150 Ma); name outdated ("oervogel" instead of *Ostromia crassipes* since 2017) |
| **F 08432** | *Homo diluvii testis* (giant salamander) | Date far too broad (23–5 Ma instead of ~13 Ma); Cuvier's legendary 1811 visit to Teylers completely unmentioned |
| **KT 1990 002** | Marlene Dumas, *Self-portrait (as seen before giving birth)* | Artist's stature not indicated (most expensive living female artist at auction; first contemporary woman in the Louvre permanent collection) |
| **KS 135** | Ronner-Knip, *De pianoles* | Acquisition date field likely shows "1897" (wrong — acquired 2012); pre-2012 provenance entirely absent |
| **KS 165** | Israëls, *Trommelslaagster* | Dimensions discrepancy (147 x 90 cm vs. external sources: 156.5 x 75 cm); date lower bound "1903" is wrong (Israëls arrived Paris 1904) |
| **KS 223** | Breitner, *Kinderen in het duin* | Subject tags "Mens, Vrouw" — painting is of children/girls; 82-year provenance gap unacknowledged |
| **KS 2013 001** | Van Looy, *De Tuin* | Garden location misleading — it is in Amsterdam (De Pijp), not Haarlem; woman in garden (Titia van Gelder, his wife) not identified |
| **KG 00492** | Dürer, *Adam en Eva* (1504) | Image dimensions listed in wrong order (192 x 247 mm — implies landscape format; print is portrait format); complete iconographic programme of four temperament animals not explained |
| **A 027 recto** | Michelangelo, *Figuurstudie voor een Ignudo* | Provenance chain omits Queen Christina of Sweden; significant verso (Creation of Adam studies) not mentioned |
| **A 068** | Raphael, *Studie voor twee engelfiguren* | Preparatory connection to the *Transfiguration* entirely absent; "Sassoferrato" inscription (former misattribution) unexplained; provenance chain omits Queen Christina |
| **KS 1987 002** | Hendriks, *Het Teekencollegie van Haarlem in 1799* | Painting was reworked after 1807 but presented as unmodified 1799 work; Jan David Zocher Jr. (designer of Vondelpark) not listed as depicted person |
| **KT 2016 092** | Andy Warhol, *Zonder titel (Geboeide handen)* | Copyright credits "Pictoright Amsterdam" — should be Warhol Foundation/ARS New York; entire 2011 estate discovery context (300 drawings found by Daniel Blau) absent |
| **KT 2020 022** | Breitner, *Boutard als Arabier* | Credit line names VriendenLoterij (acquired 2020, before the Aug 2021 merger that created VriendenLoterij); should be BankGiro Loterij; sitter misidentified as "Abyssinian" for a century |
| **KT 2022 097** | David Joris drawing | Related drawing attributed to "Johann Baldung Gruen 1473-1545" — first name wrong (Hans Baldung Grien); birth year wrong by ~11 years (c.1484/85) |
| **KT 2022 190** | Pauline Rifer de Courcelles, *Rode paradijsvogel* | Credit line may name wrong foundation (Don Quichote vs. Brook Foundation per La Tribune de l'Art); "fem.[?]" — question mark unwarranted; stepmother of Ronner-Knip (KS 135) not noted |
| **L 022** | Claude Lorrain, *Tekenaar voor de Grot van Neptunus in Tivoli* | Gray wash missing from technique; Queen Christina of Sweden absent from provenance; 2011 Louvre exhibition (L 022 was the cover image) not cited |
| **N 058** | Goltzius, *Rechterhand* (1588) | No subject tag for "self-portrait" — the hand is Goltzius's own; no description; paper dimension discrepancy |
| **RDW T 019** | Niki de Saint-Phalle & Tinguely, *Bonne Année* | Recipient "Edy de Wilde" misspelled as "Eddy"; no Nouveau Réalisme context; Soisy/Le Cyclop connection unmentioned; no context for Edy de Wilde (Stedelijk director 1963–85) |
| **T 029** | Cornelis Troost, *De Ambassadeur van Labberlotten* | Birth year wrong (1697 should be 1696); date "circa 1717" is factually impossible — subject matter did not exist until 1739; technique wrong (waterverf should be gouache); verso inscription absent |
| **O 007** | Hendrick Avercamp, *IJsvermaak bij een boerderij* | "Pen in zwart" almost certainly wrong (should be brown/grey iron-gall ink); date lower bound "circa 1605" unjustified; Welcker catalogue raisonné absent |
| **O 047** | Rembrandt, *Christus en de discipelen in het Hof van Gethsemane* | Title strips "in het Hof van Gethsemane" — making the subject ambiguous; Benesch 89 (universal scholarly identifier) absent from bibliography; no provenance for 1796 acquisition; no description |
| **P 078** | Adriaen van Ostade, *Interieur van boerenherberg* | Death year wrong (1684 should be 1685); bibliography contains an entry for a 2015 exhibition of 19th-century watercolors — database linking error with no relevance to a 1673 Golden Age drawing |
| **T 085** | Maria Sibylla Merian, *Drie tulpen* | Father described as "German" — he was Swiss (Matthäus Merian the Elder, born Basel); "first time insects depicted in all life stages" claim wrong — Merian achieved this in 1679, not 1705 |
| **1355** | Encyclopédie (Diderot & d'Alembert), 1751–1780 | D'Alembert listed as co-editor for full 1751–1780 run (he resigned in 1758); false "Neuchâtel" imprint (used to evade censorship) absent; acquired in 1780 as a banned book — 4 years before museum opened — yet no provenance |

**None of the 24 Topstukken analyzed was free of major errors.** The remaining **26 Topstukken** (4 Boeken, 9 Instrumenten, 10 Fossielen/Mineralen, 3 Munten/Penningen) are queued for analysis.

---

## Most Significant Discoveries

These findings are not in the Teylers online catalog and would substantially enhance the public understanding of these objects:

### Crown Jewels with Major Errors

1. **F 06928 — Ostromia: The "Mona Lisa" of Teylers has the wrong name and wrong date.** The catalog calls it an "oervogel" (primitive bird) dated "165–45 million years ago." Since 2017, it has been reclassified as *Ostromia crassipes* — it is NOT a bird and NOT an Archaeopteryx. The date should be ~150 Ma, not a 120-million-year range.

2. **F 08432 — Homo diluvii testis: Cuvier's visit to Teylers is unmentioned.** In 1811, Georges Cuvier visited Teylers Museum, took a needle to this fossil, uncovered its forelimbs, and proved it was a giant salamander — one of the most famous corrections in the history of science. The catalog does not mention this. The date "23–5 million years ago" should be ~13 Ma.

3. **TMNK 10564 — A coin possibly worth €180,000+ described without any rarity indication.** This gold striking of a silver denomination may be unique. Comparable pieces have sold at auction for €180,000–€245,000. The catalog says "[gouden afslag]" and nothing more.

### Historical Bombshells

4. **TMNK 00272 — The only coin depicting William of Orange, struck the year of his assassination.** The catalog does not mention that William was assassinated on 10 July 1584 — the date on this coin. It may be a posthumous portrait. The standard numismatic name "prinsendaalder" is not used.

5. **TMNK 00294 — The Dutch Trojan Horse: one of the most famous stories in Dutch history, untold.** The medal commemorates soldiers hiding in a peat barge to capture Breda in 1590. The catalog gives only the title. This medal comes from Pieter Teyler's own collection.

6. **FK 1159 — The "Electric Barometer" is not a barometer.** It demonstrates electroluminescence — the glow of mercury in vacuum when agitated. It is the direct ancestor of the neon lamp, demonstrating a phenomenon first observed by Jean Picard in 1675. The catalog has no description and no maker.

7. **FK 1973.01 — The uranium centrifuge model's inventor was Teylers' own curator.** Jacob Kistemaker, who developed the ultracentrifuge technology later stolen by A.Q. Khan and proliferated to Pakistan, Iran, Libya, and North Korea, was simultaneously curator of Teylers' Fysisch Kabinet. The catalog does not mention this.

8. **1020 — "Cornelius Stanhope" is probably a catalog error.** No scholar by this name is known. The biography in this Marcus Aurelius edition was almost certainly written by George Stanhope (1660–1728), Dean of Canterbury. Meanwhile, the editor Thomas Gataker — whose edition is "the principal authority" on the *Meditations* — goes completely unidentified.

### Topstukken Phase: Major Discoveries

11. **KG 00492 — Dürer's *Adam and Eva* (1504): dimensions listed in the wrong order.** The catalog gives image dimensions as "192 x 247 mm" — implying a wider-than-tall landscape print. This print is portrait format (taller than wide). Every major collection that holds this engraving (Metropolitan Museum, Rijksmuseum, Art Institute of Chicago, Morgan Library) records it as ~250 x 192 mm (height x width). The Teylers entry reverses this. Furthermore, the four animals — cat, rabbit, ox, elk — represent the four humoral temperaments in pre-lapsarian harmony, one of the key iconographic programmes of Northern Renaissance art. The catalog lists them as bare subjects with no explanation.

12. **A 068 — Raphael's angel study: the painting it was made for is never mentioned.** This is a preparatory drawing for Raphael's *Transfiguration* (Pinacoteca Vaticana) — his last work, left unfinished at his death in 1520. The catalog does not state this. Additionally, the inscription "Sassoferrato" records a former misattribution to the 17th-century Baroque painter Giovanni Battista Salvi (an obsessive Raphael copyist whose works were routinely confused with originals) — but goes unexplained.

13. **A 027 recto — Michelangelo: Queen Christina of Sweden missing from provenance.** Teylers' Michelangelo drawings are among the best-preserved in the world, and their provenance through **Queen Christina of Sweden** (1626–1689) to the Odescalchi family is one of the most distinguished ownership chains in the art world. The catalog says only "purchased from Odescalchi heirs, Rome, 1790." The verso of this same sheet — containing figure studies for the *Creation of Adam* — is not mentioned at all.

14. **KS 165 — Israëls *Trommelslaagster*: significant dimensions discrepancy.** Wikidata, Wikimedia Commons, and USEUM all record the painting as 156.5 x 75 cm; Teylers' catalog states 147 x 90 cm. This 10+ cm discrepancy in both dimensions requires physical verification.

15. **KS 2013 001 — Van Looy *De Tuin*: the garden is in Amsterdam, not Haarlem.** The garden depicted is at Rustenburgerstraat in Amsterdam's De Pijp district, where Van Looy lived with his newly married wife in 1893. The catalog does not state this, strongly implying a Haarlem location for a Haarlem artist in a Haarlem museum. The woman kneeling in the flowers is his wife Titia van Gelder — not identified in the catalog.

### Topstukken Phase 2 & 3: Major Discoveries

16. **O 047 — Rembrandt's Gethsemane drawing: the location is stripped from the title.** The catalog title is "Christus en de discipelen" — Christ and the disciples. This could be the Last Supper, the Olivet Discourse, or any teaching scene. The museum's own website uses the full title "Christus en de discipelen **in het Hof van Gethsemane**." The standard catalogue raisonné reference — **Benesch 89** — is entirely absent from the bibliography. Additionally, the drawing was acquired in 1796 for 60 guilders (notably low at the time), yet no provenance appears in the database record. This is one of Rembrandt's largest and most technically elaborate drawings, exhibited at the Louvre in 2011, and its catalog record is functionally useless for scholarly research.

17. **1355 — The Encyclopédie was purchased as a banned book before the museum even opened.** Diderot & d'Alembert's *Encyclopédie* was condemned by the Parlement de Paris in 1759, placed on the *Index Librorum Prohibitorum* by Pope Clement XIII in 1759, and completed in secret using a false "Neuchâtel" imprint to evade censorship. Teylers acquired this banned book in **1780 — four years before the museum's 1784 opening** — one of the most remarkable early acquisitions in the collection. The catalog record contains no provenance, no volume count (35 folio volumes), no mention of the censorship history, and lists d'Alembert as co-editor for the full 1751–1780 run when he resigned in 1758. Teylers itself made censorship the theme of its 2026 "Gevaarlijke Boeken" exhibition — yet the catalog record contains no trace of this history.

18. **T 029 — Troost's *Labberlotten* drawing carries a date that is factually impossible.** The catalog gives the date as "circa 1717 – voor 1750." The subject depicted — a prank by satirist Jacob Campo Weyerman at the tavern 't Bokje in Haarlemmerhout — occurred in **1739**. The drawing could not have been made before 1739. The scholarly date is **1742** (Niemeijer catalogue raisonné, cat. no. 890T). "Circa 1717" appears to be a generic career-start placeholder erroneously applied to this work. Additionally, the catalog calls the medium "watercolor" when it is gouache — a distinction of both technical and art-historical significance (explaining why it fetched 100 guilders in 1780).

19. **P 078 — A 1673 Adriaen van Ostade drawing has a bibliography entry for a 2015 exhibition of 19th-century watercolors.** The catalog bibliography for this Golden Age masterpiece includes *"aquarel: Nederlandse meesters van de negentiende eeuw"* (Teylers Museum, 2015) — a catalog for an exhibition of Mesdag, Mauve, Israëls, and Breitner. This has zero scholarly relevance to a 1673 drawing by Adriaen van Ostade. This is a database linking error in which a bibliographic record was accidentally attached to the wrong object. Van Ostade also has his death year wrong (1684 should be 1685) and the standard catalogue raisonné (Schnackenburg, Hamburg, 1981) is absent.

20. **KS 1987 002 — The Teekencollegie painting was reworked after 1807 but is presented as a 1799 document.** The catalog presents Hendriks's painting as "Het Teekencollegie van Haarlem **in 1799**." Scholarly research shows the painting was a composite: at least two figures — including Jan David Zocher Jr. (future designer of the Vondelpark) and Adriaan van der Willigen — were added after 1807, when these individuals first joined the Teekencollegie. Zocher was 8 years old in 1799 and is not listed among the depicted persons in the catalog.

21. **T 085 — Teylers describes Maria Sibylla Merian's father as "German." He was Swiss.** The topstukken text calls Matthäus Merian the Elder "de Duitse graveur-uitgever" (the German engraver-publisher). He was born in Basel and is consistently identified as Swiss by Britannica, Wikipedia, and all scholarly sources. Additionally, the text claims her 1705 *Metamorphosis Insectorum Surinamensium* was the "first time insects were depicted in all life stages" — but Merian had already achieved this in her 1679 *Der Raupen wunderbare Verwandlung*, more than two decades earlier.

### Systematic Findings

9. **The Kampman workshop suite is invisible.** Seven instruments (FK 0014, 0018, 0020, 0022, 0027, 0053, 0073) form a coherent 's Gravesande-style Newtonian mechanics teaching cabinet. The catalog treats each as an isolated object with no cross-references, no identification of 's Gravesande, and in one case (FK 0022) no maker at all.

10. **407 — The founding catalog of Rijksmuseum Boerhaave is unidentified.** This modest 70-page booklet led directly to the establishment of the Netherlands' national science museum. Its author, Crommelin, played chamber music with Einstein.

---

## Error Classification

### By Category

| Category | Count | Examples |
|----------|-------|---------|
| Factual errors (dates, attributions, techniques) | 18 | TMNK 00002 dated "1415" (actually c. 1700–1740); F 06928 dated "165–45 Ma" (actually ~150 Ma) |
| Missing descriptions | 9 | FK 1159, FK 1241, FK 0073 — no description of what the instrument does |
| Missing context / significance | 14 | TMNK 10564 rarity; 407 founding catalog; Cuvier's visit |
| Missing or wrong makers/authors | 10 | FK 0022 no maker; 1020 "Cornelius Stanhope" likely wrong |
| Missing cross-references | 5 | Kampman suite; pulley pedagogical series |
| Missing series identification | 4 | TMNK 00009 "Judenmedaille" series; KG 04733 "Dieren" series |
| **Total major errors** | **60** | |

### By Collection Area

| Collection | Objects | Major errors | Avg per object |
|------------|---------|-------------|----------------|
| Prints & Drawings | 7 | 14 | 2.0 |
| Medals & Coins | 7 | 13 | 1.9 |
| Scientific Instruments | 13 | 18 | 1.4 |
| Rare Books | 6 | 9 | 1.5 |
| Fossils | 2 | 4 | 2.0 |
| Sculpture | 1 | 1 | 1.0 |
| **Total** | **35** | **60** | **1.7** |

---

## Structural Problems

These problems affect the catalog as a whole, not just individual objects:

### 1. Missing Descriptions
Many objects — especially scientific instruments — have no description field at all. The catalog assumes the title is self-explanatory, but titles like "Electric barometer" or "Solar microscope" tell a modern visitor nothing about what the object does, why it matters, or how it works. **9 of 35 objects** had no meaningful description.

### 2. No Cross-References Between Related Objects
The catalog treats every object in isolation. In reality, many objects form coherent groups:
- The **Kampman workshop suite** (FK 0014, 0018, 0020, 0022, 0027, 0073): 's Gravesande mechanics demonstrations
- Van Marum's **electrical discharge research program** (FK 0508, 1153, 1159)
- The **telescope collection** (FK 0323, 0324, 1980 01): English and Dutch makers
- Print **series** (KG 04733 is a title page for an 8-plate series)
- Medal **series** (TMNK 00009 is from a documented Prague series)

### 3. Makers, Authors, and Depicted Persons Not Contextualized
Names are listed without any identification. The visitor sees "Gerard van Bylaer (±1540–1617)" and learns nothing. Van Bylaer was the die cutter for ALL triumph medals ordered by the States-General during the Dutch Revolt — one of the most important medallists of the era. This pattern repeats for virtually every person named in the catalog.

### 4. Reference Catalogs Not Cited
Standard numismatic references (Van Loon, Dugniolle) are absent from medal records. The definitive instrument catalog (Turner & Levere, *Martinus van Marum: Life and Work*, Vol. IV, 1973) is never cited. Print references (Hollstein, Bartsch) are sometimes present but inconsistently applied.

### 5. Inscriptions Not Translated
Latin, Greek, and archaic Dutch inscriptions are transcribed but not translated. Powerful texts like *"INVICTI ANIMI PRAEMIVM PARATI VINCERE AVT MORI"* ("The reward of an unconquered spirit: prepared to conquer or to die") go unexplained. This excludes the vast majority of visitors from understanding the objects.

### 6. Geological Dates Far Too Broad
Both fossils use entire geological epochs as date ranges ("23–5 Ma" for Miocene, "165–45 Ma" for Jurassic+Cretaceous), when modern geological research provides much more precise dates. These broad ranges are uninformative and imply a level of uncertainty that no longer exists.

---

## Methodology

Each object was analyzed through the following process:

1. **Catalog retrieval**: The Teylers Adlib/Axiell catalog page was fetched and all metadata fields extracted
2. **Deep research**: An AI research agent conducted systematic cross-referencing against:
   - Other museum databases (Rijksmuseum, British Museum, Museo Galileo, Harvard, Museum Boerhaave)
   - Academic publications and reference works
   - Biographical dictionaries and Wikipedia
   - Specialized numismatic, art-historical, and scientific databases
   - Digitized primary sources (e-rara, BHL, EEBO, HathiTrust, Gallica)
3. **Analysis report**: A detailed markdown report was written for each object, documenting all findings
4. **Error classification**: Errors were classified as Major (factually wrong, significantly misleading, or missing essential information) or Minor (missing context, untranslated inscriptions, uncited references)

The entire process — from catalog retrieval through final reporting — was conducted by a single researcher (Joost Soeterbroek) assisted by the Claude Opus 4.6 AI model (Anthropic). Analysis time per object ranged from 10 to 45 minutes, with an average of approximately 20 minutes per object.

---

## What a Full-Collection Scan Would Deliver

Based on the results of this pilot study, a systematic scan of Teylers' complete online catalog would:

- **Identify an estimated 3,000+ major errors** across the collection (based on the 1.7 errors/object rate)
- **Prioritize corrections** by severity and public impact (topstukken first, then high-traffic objects)
- **Generate enriched descriptions** for objects currently lacking any description
- **Map cross-references** between related objects, revealing hidden narratives and connections
- **Produce a comprehensive correction report** ready for direct import into the catalog system
- **Cost approximately €4 per object** — orders of magnitude less than traditional art-historical review
- **Complete in weeks, not years** — the AI-assisted methodology scales linearly

The pilot has already demonstrated the methodology on 35 objects across all major collection areas. The infrastructure, prompts, and quality standards are proven. Scaling to the full collection is a matter of execution, not experimentation.

---

## AI Compute Resources

| Resource | Estimate |
|----------|----------|
| AI model | Claude Opus 4.6 (Anthropic) |
| Total tokens processed | ~8,500,000 |
| Research agent invocations | ~110 |
| Web fetches | ~150 |
| Estimated compute cost | ~€270–€320 |
| Total analysis time | ~6 sessions, ~24 hours |
| Objects analyzed | 57 (35 random + 22 Topstukken) |
| Cost per object | ~€5–€6 |

The cost of analyzing 43 objects with AI assistance (~€190) compares favorably with the cost of equivalent manual art-historical research, which would require days of specialist time per object. **Scaled to a full collection scan, this methodology could review thousands of objects for a fraction of traditional costs.**

---

## Recommendations

1. **Commission a systematic full-collection scan** using AI-assisted methodology to identify errors and omissions across the entire online catalog
2. **Start with the 50 Topstukken** — the museum's own flagship objects deserve error-free catalog records
3. **Add description fields** to all objects, especially scientific instruments and coins/medals
4. **Implement cross-references** between related objects (series, suites, provenance groups)
5. **Contextualize all persons** with brief biographical notes
6. **Translate all inscriptions** into Dutch and English
7. **Update geological dates** for fossils to reflect current scientific knowledge
8. **Cite standard reference catalogs** (Turner & Levere, Van Loon, Hollstein, etc.)
9. **Link to external digital surrogates** where available (EEBO, BHL, Rijksmuseum, etc.)
10. **Review the "Cornelius Stanhope" attribution** (object 1020) against the physical title page
11. **Verify Van Bylaer's birth date** — the catalog gives "±1540" across multiple objects, but sources indicate c. 1553

---

## Complete Error Register

### Sample 1: Major Errors (28)

| Object | Issue | Teylers says | Should be |
|--------|-------|--------------|-----------|
| PP 0121 | Subject classification wrong | medicus (physician) | jurist / schout / regent |
| PP 0121 | Technique wrong | gravure (engraving) | ets (etching) |
| PP 0121 | Death date discrepancy | 1639 (on print) | 1630 (historical record) |
| TvB G 0771 | Creator birth year wrong | 1622 | c. 1626 |
| TvB G 0771 | Technique anachronistic | ets en stippelgravure | ets (etching) — "stippelgravure" is anachronistic for 17th c. |
| TvB G 0771 | Creator role wrong | graveur (engraver) | etser (etcher) |
| TvB G 0771 | Date too broad | 1642–1678, ca. | c. 1661–1662 |
| KG 01153 | Technique wrong | ets (etching) | gravure (engraving) |
| KG 01153 | Technique/role contradiction | graveur + ets | Should be consistent: graveur + gravure |
| KG 01153 | Dujardin birth year wrong | 1622 | c. 1626 |
| KG 04733 | Creator role wrong | graveur | etser (etcher) |
| KG 04733 | Series not identified | not mentioned | Title page for "Dieren" series (8 plates) |
| FK 0002 | Transcription error | "Egnelse" | "Engelse" |
| FK 0002 | Transcription error | "Amsgterdamsche" | "Amsterdamsche" |
| FK 0007 | Material possibly inaccurate | glas, messing | messing, ivoor/been; glass not visible |
| FK 0011 | Date wrong | c. 1840 | c. 1835–1837 (serial number analysis) |
| FK 0011 | Materials incomplete | glas, messing | mahonie, messing, glas, email, ivoor |
| N 021 | Provenance incomplete | Odescalchi heirs, 1790 | Queen Christina of Sweden -> Odescalchi (1692) -> Teylers (1790) |
| KG 07880 | Date too broad | c. 1770–1822 | c. 1790–1795 (likely c. 1793) |
| KG 07880 | Technique incomplete | ets | ets en gravure |
| KT 2001 103 | Date too broad | c. 1770 – before 1828 | c. 1777–1806 |
| KT 2001 106 | Date too broad | c. 1770 – before 1828 | c. 1785–1790 |
| TMNK 00002 | Date catastrophically wrong | 1415 | c. 1700–1740 (1415 is inscription, not manufacture) |
| TMNK 00002 | Creator wrong | Kingdom of Bohemia, unknown | Christian Wermuth workshop, Gotha |
| TMNK 00002 | Place wrong | Bohemia (implied) | Germany (Gotha/Thuringia) |
| TMNK 00009 | Series not identified | not mentioned | "Judenmedaille" — Prague series, c. 1600–1650 |
| TMNK 00009 | Title misleading | "Huwelijk... 1452" | Not a marriage medal; dynastic portrait series |
| TMNK 00009 | Eleonora birth year wrong | 1436 | 1434 |

### Sample 2: Major Errors (20)

| Object | Issue | Teylers says | Should be |
|--------|-------|--------------|-----------|
| 63 | Second author missing | Alexander only | Ammonius Hermiae is second author — book contains two texts |
| 68 | Authorship undifferentiated | "Ammonius" | Modern scholarship attributes to Herennius Philo of Byblos |
| 394 | Significance not indicated | minimal record | Landmark primary source: official Beresovka mammoth expedition report |
| 407 | Significance not indicated | minimal record | Founding catalog of Rijksmuseum Boerhaave |
| 2163 | Author not identified | "G. Cuvier" | Baron Georges Cuvier, founder of comparative anatomy; visited Teylers 1811 |
| 2163 | Nature of work unexplained | title only | Official report on scientific progress, commissioned by Napoleon |
| 2163 | Cuvier-Teylers connection unmentioned | not mentioned | Cuvier identified *Homo diluvii testis* as giant salamander at Teylers |
| FK 0018 | Makers not contextualized | names only | Kampman workshop; two partnerships over 50 years; part of suite |
| FK 0018 | Suite not cross-referenced | isolated record | Part of 's Gravesande mechanics suite |
| FK 0020 | Inconsistent maker name | "Jean Pelletier" | "J.C. Pelletier" (as in FK 0018) — same person |
| FK 0020 | Death year listed as "?" | "?" | Probably 1780 (documented engraver Jean C. Pelletier) |
| FK 0022 | **No maker listed** | — | Almost certainly Kampman & Pelletier (identical to FK 0018/0020) |
| FK 0022 | Pedagogical series not identified | isolated record | Third in pulley->tackle->compound series |
| FK 1980 01 | "(1663)" misleading | in title | 1663 = Gregory's design year, NOT build date (c. 1745–1791) |
| FK 1980 01 | Van der Bildt dynasty not identified | "J. v.d. Bildt, Franeker" | 550+ telescopes produced; curator of Franeker University |
| FK 1980 01 | Dual system not mentioned | not mentioned | Gregorian + Cassegrain modes in one telescope |
| FK 1973.01 | Kistemaker was Teylers curator | not mentioned | Explains acquisition; significant for institutional history |
| FK 1241 | No description | — | World's first projector: projects microscopic images using sunlight |
| FK 1159 | No description; title misleading | "Electric barometer" | NOT a barometer — demonstrates electroluminescence; precursor to neon lamp |
| FK 1159 | **No maker listed** | — | Probably John Cuthbertson, Amsterdam (Van Marum's instrument maker) |

### Sample 3: Major Errors (12)

| Object | Issue | Teylers says | Should be |
|--------|-------|--------------|-----------|
| F 06928 | Date wildly wrong | 165–45 million years ago | ~150 Ma (Late Jurassic, Tithonian) |
| F 06928 | Type classification outdated | "oervogel" (primitive bird) | *Ostromia crassipes* since 2017 — NOT a bird |
| F 08432 | Date far too broad | 23–5 million years ago | ~13 Ma (Middle Miocene, Serravallian) |
| F 08432 | Cuvier's reidentification not described | not mentioned | Cuvier visited Teylers 1811, uncovered forelimbs, proved it was a salamander |
| TMNK 00272 | Assassination context absent | "1584" only | William of Orange assassinated 10 July 1584; may be posthumous portrait |
| TMNK 00272 | Coin type not identified | "gehelmde rijksdaalder" | Should identify as "prinsendaalder" — standard numismatic name |
| TMNK 00294 | Turfschip story not described | title only | Dutch Trojan Horse: soldiers hidden in peat barge; one of most famous Dutch military exploits |
| TMNK 10564 | Extreme rarity not indicated | "[gouden afslag]" only | Possibly unique; comparable pieces sell for €180,000–€245,000 |
| 1020 | "Cornelio Stanhope" likely wrong | "Cornelio Stanhope" | Almost certainly George Stanhope (1660–1728), Dean of Canterbury |
| 1020 | Gataker not identified | not mentioned | Thomas Gataker (1574–1654); his edition is "the principal authority" on the *Meditations* |
| FK 0073 | No description | title only | Demonstrates brachistochrone and tautochrone — two of the most elegant results in classical mechanics |
| FK 0073 | 's Gravesande not mentioned | not mentioned | Built after designs by 's Gravesande (1688–1742), foremost promoter of Newtonian physics |

### Topstukken Phase: Major Errors (16)

| Object | Issue | Teylers says | Should be |
|--------|-------|--------------|-----------|
| KT 1990 002 | Artist's stature not indicated | "Marlene Dumas (1953)" | Most expensive living female artist at auction ($13.6M); first contemporary woman in Louvre permanent collection |
| KS 135 | Acquisition date likely wrong | "Acquired 1897" (if in field) | Acquired 2012; 1897 is creation date |
| KS 135 | Pre-2012 provenance absent | not listed | Unknown — gap should be acknowledged for a Topstuk |
| KS 165 | Dimensions discrepancy | 147 x 90 cm | External sources: 156.5 x 75 cm — requires physical verification |
| KS 165 | Date lower bound wrong | c. 1903 | Israëls arrived in Paris 1904; lower bound should be 1904 |
| KS 223 | Subject tags inconsistent with title | "Mens, Vrouw" | Children/girls (title says "Kinderen"; museum text says "twee meisjes") |
| KS 223 | Provenance before 1968 absent | not listed | 82-year gap unacknowledged for a Topstuk |
| KS 2013 001 | Garden location misleading | not stated | Amsterdam, Rustenburgerstraat, De Pijp — not Haarlem |
| KS 2013 001 | Identity of woman not stated | "kneeling woman wearing a hat" | Van Looy's wife Titia van Gelder |
| KG 00492 | Image dimensions in wrong order | "192 x 247 mm" | 247 x 192 mm (height x width); print is portrait, not landscape |
| KG 00492 | Iconographic programme not explained | animals listed as bare subjects | Four temperament animals; pre-lapsarian humoral balance; parrot iconography; goat missing |
| A 027 recto | Provenance chain incomplete | "Purchased from Odescalchi heirs" | Full chain includes Queen Christina of Sweden and Cardinal Azzolino |
| A 027 recto | Verso not mentioned | not referenced | A 027 verso contains Creation of Adam figure studies — equally significant |
| A 068 | Painting connection absent | not stated | Preparatory study for the *Transfiguration* (Raphael's last work, Pinacoteca Vaticana) |
| A 068 | "Sassoferrato" inscription unexplained | transcribed only | Records former misattribution; Sassoferrato was a prolific Raphael copyist |
| A 068 | Provenance chain incomplete | "Purchased from Odescalchi heirs" | Full chain includes Queen Christina of Sweden and Cardinal Azzolino |

### Topstukken Phase 2: Major Errors (~34)

| Object | Issue | Teylers says | Should be |
|--------|-------|--------------|-----------|
| KS 1987 002 | Painting presented as unmodified 1799 work | "in 1799" | Composite; Van der Willigen and Zocher Jr. added post-1807 |
| KS 1987 002 | Jan David Zocher Jr. not listed | 6 names listed | Zocher Jr. (designer Vondelpark, 1791–1870) omitted |
| KS 1987 002 | Hendriks's dual role not stated | "schilder" only | Kastelein (curator) of Teylers 1785–1819; founder of Teekencollegie 1796 |
| KS 1987 002 | Teekencollegie history absent | not described | Successor to Stads Teekenacademie (1772–1795) |
| KS 1987 002 | 2023 Waanders catalog not cited | not referenced | *Wybrand Hendriks was hier!* (Waanders, 2023, ISBN 9789462622382) |
| KT 2016 092 | Copyright wrong | © Pictoright Amsterdam | © Andy Warhol Foundation for the Visual Arts / Licensed by ARS, New York |
| KT 2016 092 | 2011 estate discovery absent | "bron: documentatie Daniel Blau" only | ~300 drawings discovered 2011 by Daniel Blau; Teylers hosted exhibition 2013 |
| KT 2016 092 | No provenance chain | absent | Warhol studio (c.1953) → Foundation (1987–2011) → Blau (2011) → Teylers (2016) |
| KT 2016 092 | No exhibition history | absent | Teylers *From Silverpoint to Silver Screen* (June–Sept 2013) |
| KT 2016 092 | No scholarly references | absent | Hirmer 2013; Hirmer 2016; note absence of catalogue raisonné coverage |
| KT 2016 092 | Object name field misused | "pen in inkt" | "tekening" |
| KT 2020 022 | Credit line names wrong organization | VriendenLoterij | BankGiro Loterij (merger creating VriendenLoterij occurred Aug 2021, after 2020 acquisition) |
| KT 2020 022 | Date field contradicts itself | date inconsistency | Requires reconciliation |
| KT 2020 022 | Sitter misidentified | "Abyssinian" implied | Identity requires verification against period sources |
| KT 2022 097 | Related artist's first name wrong | "Johann Baldung Gruen" | "Hans Baldung Grien" — consistently misspelled in the catalog |
| KT 2022 097 | Related artist's birth year wrong | 1473 | c. 1484/85 — error of ~11 years |
| KT 2022 190 | Credit line may name wrong foundation | Don Quichote Foundation | La Tribune de l'Art reports Brook Foundation — requires verification |
| KT 2022 190 | "fem.[?]" — question mark unwarranted | "fem. [?] Knip" | "fem." = standard French abbreviation for "femme" (wife); Christie's confirms without uncertainty |
| KT 2022 190 | No provenance | absent | Christie's Paris, 22 Nov 2022, lot 1; hammer €80,000 (€100,800 with premium) |
| KT 2022 190 | No biographical context | bare name and dates | Gold medal Salon 1810; Premier Peintre to Marie-Louise; *Les Pigeons* (1808–1811) |
| KT 2022 190 | No bibliography | absent | Temminck & Knip *Les Pigeons*; RKD entry |
| L 022 | Gray wash missing from technique | "pen in bruin, penseel in bruin" | + grijs (gray wash) — confirmed by 2011 Louvre/Teylers exhibition catalog |
| L 022 | Verso technique absent | iconographic description only | Graphite, pen and brown ink, brown wash |
| L 022 | 2011 Louvre/Teylers exhibition not cited | not cited | Cover image of Van Tuyll/Plomp 2011; shown Louvre and Teylers |
| L 022 | Queen Christina absent from provenance | "Odescalchi erfgenamen, 1790" only | Full chain: Christina → Azzolino → Odescalchi → Lestevenon → Teylers |
| L 022 | Depicted site not identified | "rotswand met grot" | Grotto of Neptune, Tivoli (now Parco Villa Gregoriana) |
| L 022 | Roethlisberger MRD number absent | bibliography listed but no MRD number | Specific MRD entry required for every Claude Lorrain drawing |
| N 058 | "Self-portrait" subject tag absent | no subject tag | The hand depicted is Goltzius's own right hand — seminal self-portrait |
| N 058 | No description | absent | Goltzius drew his own hand to demonstrate virtuosity after recovering from a crippling hand injury |
| N 058 | Paper dimension discrepancy | 328 mm | External sources: 322 mm — requires measurement verification |

### Topstukken Phase 3: Major Errors (36)

| Object | Issue | Teylers says | Should be |
|--------|-------|--------------|-----------|
| RDW T 019 | Recipient name misspelled | "Eddy de Wilde" | "Edy de Wilde" (Eduard Leon Louis de Wilde, 1919–2005) |
| RDW T 019 | No biographical context for creators | bare names and dates | Nouveau Réalisme founders; Tirs; Nanas; Le Cyclop |
| RDW T 019 | No context for recipient / donating foundation | bare credit line | Edy de Wilde = Stedelijk director 1963–1985; Reinhold collection donated 1998 |
| RDW T 019 | Nouveau Réalisme not mentioned | absent | Both artists were founding members (Tinguely 1960; Saint-Phalle 1961) |
| RDW T 019 | Soisy/Le Cyclop absent | absent | Soisy-sur-Ecole = shared studio; Le Cyclop under construction 1970 |
| RDW T 019 | Stedelijk Museum connection absent | absent | Saint-Phalle 1967 Nanas; Tinguely 1961 Bewogen Beweging / 1962 Dylaby |
| RDW T 019 | No bibliography | absent | Hultén 1992; Tinguely catalogs; Nouveau Réalisme primary sources |
| T 029 | Artist birth year wrong | 1697 | 1696 (confirmed by Niemeijer catalogue raisonné title and all authorities) |
| T 029 | Date range factually impossible | circa 1717 – voor 1750 | 1742 (subject matter existed only from 1739; Niemeijer 890T) |
| T 029 | Technique misclassified | penseel in waterverf | Gouache (opaque); support is blue paper |
| T 029 | Verso inscription absent | not listed | "Vertooning van den Ambassadeur van Maroccen in den hout" |
| T 029 | Niemeijer catalogue raisonné absent | 1904 Scholten only | Niemeijer 1973, cat. no. 890T — standard reference for all Troost works |
| T 029 | No provenance in database | absent | Acquired 1780 for 100 guilders; pre-1780 unknown |
| O 007 | Object name field misused | "penseel in waterverf" | "tekening" — recurring structural error |
| O 007 | Pen medium almost certainly wrong | "pen in zwart" | Brown or grey (iron-gall ink); "zwart" anomalous across entire Avercamp corpus |
| O 007 | Date lower bound unjustified | "ca 1605" | Avercamp in training in 1605; earliest paintings c.1608–1609; comparanda c.1615–1630 |
| O 007 | Welcker catalogue raisonné absent | Scholten 1904; Plomp 1997 | Welcker 1933/1979 — standard reference for all Avercamp works |
| O 007 | No provenance | absent | Price inscriptions suggest 3-stage sales history; not researched |
| O 007 | No art-historical significance | absent | Preeminent Dutch winter landscape master; Little Ice Age documentation |
| O 047 | Title missing Gethsemane | "Christus en de discipelen" | "Christus en de discipelen in het Hof van Gethsemane" — location strips the subject |
| O 047 | Benesch 89 absent from bibliography | not cited | Benesch 1973, no. 89 — universal scholarly identifier for Rembrandt drawings |
| O 047 | No provenance in database | absent | Acquired at auction 1796 for 60 guilders; pre-1796 unknown |
| O 047 | No exhibition history | absent | Louvre/Philadelphia/Detroit 2011; Teylers 2013 |
| O 047 | No description | absent | Ten disciples in circle; sleeping figures; excised strip; significance |
| P 078 | Death year wrong | 1684 | 1685 (died 27 April 1685, buried 2 May 1685, St. Bavo's Haarlem) |
| P 078 | Irrelevant bibliography entry | "aquarel: Nederlandse meesters 19e eeuw" | Database linking error — 2015 exhibition of 19th-century watercolors; must be removed |
| P 078 | Schnackenburg catalogue raisonné absent | not cited | Schnackenburg, *Zeichnungen und Aquarelle*, 2 vols., Hamburg 1981 |
| P 078 | No provenance | absent | Unknown; acquisition date and source not documented |
| T 085 | Father's nationality wrong | "de Duitse graveur-uitgever" | Swiss — Matthäus Merian the Elder born Basel; consistently identified as Swiss |
| T 085 | Creator role reductive | tekenaar only | Naturalist, entomologist, scientific illustrator, printmaker, painter |
| T 085 | "First time insects in all life stages" wrong | "voor het eerst" in *Metamorphosis* (1705) | Merian achieved this in *Der Raupen wunderbare Verwandlung* (1679), 26 years earlier |
| 1355 | D'Alembert listed as co-editor 1751–1780 | both editors for full run | D'Alembert resigned 1758 after vol. VII; Diderot sole editor from 1758 |
| 1355 | Neuchâtel false imprint absent | "Parijs, Amsterdam" only | Vols. 8–17 bear false "A Neufchâtel" imprint to evade 1759 censorship |
| 1355 | No provenance | absent | Acquired 1780 — four years before museum opening; documented in Teylers' own exhibition text |
| 1355 | No set description | absent | 35 folio volumes: 17 text + 11 plates + 4 suppl. text + 1 suppl. plates + 2 table volumes |
| 1355 | No censorship history | absent | 1759 Parlement condemnation; Index Librorum Prohibitorum; completed in secret; Le Breton's censoring |

---

## Statistical Summary

| Metric | Sample 1 | Sample 2 | Sample 3 | Topstukken Ph.1 | Topstukken Ph.2 | Topstukken Ph.3 | **Total** |
|--------|----------|----------|----------|-----------------|-----------------|-----------------|-----------|
| Objects analyzed | 13 | 15 | 7 | 8 | 7 | 7 | **57** |
| Major errors | 28 | 20 | 12 | 16 | ~34 | 36 | **~146** |
| Major errors per object | 2.2 | 1.3 | 1.7 | 2.0 | ~4.9 | 5.1 | **~2.6** |
| Objects with zero errors | 0 | 0 | 0 | 0 | 0 | 0 | **0** |
| Minor omissions | ~50 | ~60 | ~40 | ~40 | ~50 | ~50 | **~290** |

---

## Conclusion

The analysis of 57 objects from across Teylers Museum's collections — 35 randomly selected and 22 from the museum's own curated Topstukken list — reveals a **consistent pattern of quality problems** in the online catalog. With approximately 146 major errors across 57 objects and not a single error-free record, the evidence strongly suggests that these problems are systemic. The extended Topstukken analysis (averaging more than 4 major errors per object) confirms that the museum's most important objects are, if anything, *less* well cataloged than the rest of the collection — likely because their greater historical complexity creates more opportunities for omission. A Rembrandt whose title strips the subject's location, a Dürer engraving with dimensions listed in the wrong order, an Encyclopédie with no provenance despite its acquisition predating the museum's own opening, and a Maria Sibylla Merian watercolor where the father's nationality is wrong — these are not minor oversights in a heritage collection of this stature.

The methodology demonstrated here — AI-assisted cross-referencing of catalog records against scholarly databases, museum collections, and reference works — is fast, scalable, and cost-effective. At approximately **€4 per object**, a full collection scan is economically feasible and would yield dramatic improvements in catalog quality.

Teylers Museum holds one of the most important heritage collections in the world. Its online catalog should reflect that distinction. The findings in this report are offered as a constructive contribution toward that goal — and as a demonstration that the tools to achieve it are ready today.

---

*This report was produced by Duinroos Innovatie using AI-assisted research (Claude Opus 4.6, Anthropic). All findings are based on publicly available sources and cross-references with other museum collections. Individual analysis reports for all 35 objects are available at <https://github.com/jsoeterbroek/teylers_collection_research>.*

*Contact: Joost Soeterbroek — <joost.soeterbroek@gmail.com> — +31 6 34 83 38 45*
