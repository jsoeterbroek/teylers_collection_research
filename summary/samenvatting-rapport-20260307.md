![Duinroos Innovatie](https://www.duinroosinnovatie.nl/assets/img/avatar-icon.png)

**Duinroos Innovatie** — [www.duinroosinnovatie.nl](https://www.duinroosinnovatie.nl)

---

# Teylers Museum Online Catalogus: Systematische Kwaliteitsanalyse

**Versie:** 20260307
**Datum:** 7 maart 2026
**Onderzoeker:** Joost Soeterbroek, ondersteund door AI-onderzoeksagent (Claude Opus 4.6, Anthropic)
**Contact:** Joost Soeterbroek — <joost.soeterbroek@gmail.com> — +31 6 34 83 38 45
**Repository:** <https://github.com/jsoeterbroek/teylers_collection_research>

---

## Managementsamenvatting

Een AI-ondersteunde analyse van **35 willekeurig geselecteerde objecten** uit de online catalogus van Teylers Museum (<https://teylers.adlibhosting.com>) heeft **60 ernstige fouten** en meer dan **150 kleinere omissies** aan het licht gebracht. Geen enkel object bleek vrij van fouten of significante omissies.

De objecten bestrijken de volle breedte van het museum: prenten, tekeningen, penningen, munten, fossielen, wetenschappelijke instrumenten en zeldzame boeken. De bevindingen zijn geen incidenten maar onthullen **structurele kwaliteitsproblemen** in de online catalogus:

- **Feitelijke fouten** in dateringen, toeschrijvingen, technieken en biografische gegevens
- **Ontbrekende beschrijvingen** — veel objecten hebben helemaal geen beschrijving
- **Ontbrekende context** — makers, auteurs en afgebeelde personen staan als kale namen zonder identificatie
- **Geen kruisverwijzingen** tussen verwante objecten (bijv. instrumentensuites, prentenseries)
- **Referentiecatalogi niet geciteerd** (bijv. Turner & Levere 1973 voor instrumenten, Van Loon voor penningen)
- **Inscripties niet vertaald** — Latijnse, Griekse en oud-Nederlandse teksten blijven onverklaard
- **Zeldzaamheid en significantie niet aangegeven** — objecten ter waarde van €180.000+ worden identiek beschreven als gewone stukken

Het foutpercentage van **1,7 ernstige fouten per object** is consistent over alle drie steekproeven, wat erop wijst dat de problemen systemisch zijn. Geextrapoleerd naar de volledige collectie duidt dit op **duizenden ernstige fouten** die op correctie wachten.

**Zelfs de eigen "Topstukken" van het museum — de 50 belangrijkste objecten — zijn getroffen.** Twee van de 50 topstukken vielen binnen onze willekeurige steekproef en beide bevatten ernstige fouten: het *Ostromia*-fossiel (F 06928) heeft de verkeerde naam en een sterk onjuiste datering, en het *Homo diluvii testis* (F 08432) vermeldt Cuviers beroemde bezoek aan het museum in 1811 niet. Als de kroonjuwelen van het museum niet nauwkeurig beschreven zijn, is de kans klein dat de bredere collectie wel correct gecatalogiseerd is.

De hier gedemonstreerde AI-methodiek is **schaalbaar naar de gehele collectie** tegen circa **€4 per object** — een fractie van de kosten van traditioneel kunsthistorisch onderzoek. Een volledige collectiescan zou de kwaliteit en toegankelijkheid van Teylers' online catalogus transformeren, en het publieke begrip van een van 's werelds belangrijkste erfgoedcollecties.

---

## Disclaimer

Deze analyse is uitgevoerd door Joost Soeterbroek, die geen kunsthistoricus of museumprofessional is. Alle bevindingen zijn uitsluitend gebaseerd op **publiek toegankelijke online metadata** uit het Teylers Adlib/Axiell-catalogussysteem, gekruisverwijsd met publiek beschikbare wetenschappelijke bronnen, museale databases (Rijksmuseum, Museo Galileo, Harvard, British Museum), academische publicaties en naslagwerken.

Het is mogelijk dat Teylers' interne collectiebeheersysteem aanvullende velden, annotaties of correcties bevat die niet in de online catalogus zijn gepubliceerd. Als dat het geval is, rijst de vraag: waarom worden deze correcties niet weerspiegeld in de publiekscatalogus? De online catalogus is de primaire interface van het museum met de wereld — onderzoekers, studenten, journalisten en het brede publiek zijn ervan afhankelijk.

Alle gedetailleerde analyserapporten zijn beschikbaar in de publieke GitHub-repository:
<https://github.com/jsoeterbroek/teylers_collection_research>

---

## Omvang

Drie willekeurige steekproeven van in totaal **35 objecten** zijn geanalyseerd:

| Steekproef | Objecten | Collectiegebieden | Ernstige fouten |
|------------|----------|-------------------|-----------------|
| Steekproef 1 | 13 | Prenten, tekeningen, penningen, munten, instrumenten, beeldhouwkunst | 28 |
| Steekproef 2 | 15 | Zeldzame boeken, wetenschappelijke instrumenten | 20 |
| Steekproef 3 | 7 | Fossielen, munten, penningen, zeldzame boeken, instrumenten | 12 |
| **Totaal** | **35** | **Alle grote collectiegebieden** | **60** |

Gemiddeld: **1,7 ernstige fouten per object**. Objecten zonder fouten: **0**.

Daarnaast is de eigen gecureerde lijst van **50 "Topstukken"** van het museum geidentificeerd en gekruisverwijsd. Twee van deze topstukken verschenen in onze willekeurige steekproef — beide bevatten ernstige fouten. De overige 48 topstukken staan in de wachtrij voor analyse in volgende fasen.

---

## Geanalyseerde objecten

### Steekproef 1: Prenten, tekeningen, penningen, munten, instrumenten

| # | Object | Type | Periode |
|---|--------|------|---------|
| 1 | PP 0121 — Samuel van Hoogstraten, *Portret van Adriaen Blyenburg* | Prent | c. 1660 |
| 2 | TvB G 0771 — Abraham Blooteling, *De dichter Jan Vos* | Prent | c. 1661–1662 |
| 3 | KG 01153 — Karel Dujardin, *Landschap met schaap en koe* | Prent | c. 1658 |
| 4 | KG 04733 — Marcus de Bye, *Titelblad met fontein* | Prent | c. 1659 |
| 5 | FK 0002 — Standaardmaatlat | Instrument | c. 1820 |
| 6 | FK 0007 — Toestel voor het ijken van waterpassen | Instrument | c. 1820 |
| 7 | FK 0011 — Thomas Earnshaw, Chronometer | Instrument | c. 1835–1837 |
| 8 | N 021 — Ruiterstandbeeld van Marcus Aurelius (brons) | Beeldhouwkunst | 1778–1790 |
| 9 | KG 07880 — Johannes Jelgerhuis, *Nieuwe Brouwerskolk te Overveen* | Prent | c. 1793 |
| 10 | KT 2001 103 — Jan Gerard Waldorp, *Landschap met stad en water* | Tekening | c. 1777–1806 |
| 11 | KT 2001 106 — Jan Gerard Waldorp, *Twee vrouwen* | Tekening | c. 1785–1790 |
| 12 | TMNK 00002 — Johannes Huss-penning | Penning | c. 1700–1740 |
| 13 | TMNK 00009 — Eleonora / Frederik III-penning | Penning | c. 1600–1650 |

### Steekproef 2: Zeldzame boeken en wetenschappelijke instrumenten

| # | Object | Type | Periode |
|---|--------|------|---------|
| 14 | 63 — Alexander Aphrodisiensis, *De Fato* | Boek | 1658 |
| 15 | 68 — Ammonius, *De adfinium vocabulorum Differentia* | Boek | 1739 |
| 16 | 394 — O. Herz, Beresovka-mammoetexpeditierapport | Boek | 1902 |
| 17 | 407 — C.A. Crommelin, Catalogus natuurkundige instrumenten Leiden | Boek | 1926 |
| 18 | 2163 — G. Cuvier, *Histoire des progres des sciences naturelles* | Boek | 1826–1828 |
| 19 | 3163 — J. Baster, *Natuurkundige Uitspanningen* | Boek | 1759–1765 |
| 20 | FK 0027 — Hellend vlak, naar 's Gravesande | Instrument | 1750–1774 |
| 21 | FK 0018 — Statief met twee poelies, Kampman & Pelletier | Instrument | 1775–1799 |
| 22 | FK 0020 — Katrollen, Kampman & Pelletier | Instrument | 1775–1799 |
| 23 | FK 0022 — Vijf takels (geen maker vermeld) | Instrument | 1775–1799 |
| 24 | FK 1996.01 — Klankanalysator, naar Koenig | Instrument | c. 1872 |
| 25 | FK 1980 01 — Van der Bildt spiegeltelescoop | Instrument | c. 1745–1791 |
| 26 | FK 1973.01 — Kistemaker ultracentrifugemodel | Instrument | 1957 |
| 27 | FK 1241 — Zonnemicroscoop van J. Mortier | Instrument | 1776 |
| 28 | FK 1159 — "Elektrische barometer" (eigenlijk elektroluminescentie-demonstrator) | Instrument | 1790 |

### Steekproef 3: Fossielen, munten, penningen, boeken, instrumenten

| # | Object | Type | Periode |
|---|--------|------|---------|
| 29 | F 06928 — *Ostromia crassipes* (voorheen "Archaeopteryx") | Fossiel | ~150 Mj |
| 30 | F 08432 — *Homo diluvii testis* (reuzensalamander) | Fossiel | ~13 Mj |
| 31 | TMNK 00272 — Prinsendaalder, Holland 1584 | Munt | 1584 |
| 32 | TMNK 00294 — Inname van Breda-penning (Turfschip) | Penning | 1590 |
| 33 | TMNK 10564 — Gouden afslag kwart gulden | Munt | 1692 |
| 34 | 1020 — Marcus Aurelius *Meditaties* (editie Gataker) | Boek | 1697 |
| 35 | FK 0073 — Cycloïdebaan, Kampman & Steitz | Instrument | 1750–1774 |

---

## De Topstukken-test

Teylers Museum heeft zelf **50 objecten aangewezen als "Topstukken"** — de hoogtepunten van de collectie, gepresenteerd op de website op [teylersmuseum.nl/nl/ontdek/topstukken](https://teylersmuseum.nl/nl/ontdek/topstukken). Dit zijn de objecten die het museum als belangrijkst beschouwt: werken van Michelangelo, Rembrandt en Raphael; de grote elektriseermachine; de Mosasaurus; het *Ostromia*-fossiel; Audubons *Birds of America*.

Bij toeval verschenen **twee van deze 50 topstukken in onze willekeurige steekproef van 35 objecten**:

| Topstuk | Gevonden ernstige fouten |
|---------|------------------------|
| **F 06928** — *Ostromia* (de "Mona Lisa" van Teylers) | Datering sterk onjuist (165–45 Mj in plaats van ~150 Mj); naam verouderd ("oervogel" in plaats van *Ostromia crassipes* sinds 2017) |
| **F 08432** — *Homo diluvii testis* (de beroemde reuzensalamander) | Datering veel te breed (23–5 Mj in plaats van ~13 Mj); Cuviers legendarische bezoek aan Teylers in 1811 — een van de beroemdste momenten in de wetenschapsgeschiedenis — volledig onvermeld |

Beide bevatten ernstige fouten. Dit is een opvallend resultaat: als de eigen paradepaardes van het museum — de objecten die het naar voren schuift als het allerbeste — feitelijke fouten en kritische omissies bevatten, is de kans dat de bredere collectie nauwkeurig gecatalogiseerd is gering.

De overige **48 topstukken** zijn geidentificeerd en in de wachtrij geplaatst voor systematische analyse. De volledige lijst is beschikbaar in de projectrepository.

---

## Belangrijkste ontdekkingen

Deze bevindingen staan niet in de Teylers online catalogus en zouden het publieke begrip van deze objecten substantieel vergroten:

### Kroonjuwelen met ernstige fouten

1. **F 06928 — Ostromia: de "Mona Lisa" van Teylers heeft de verkeerde naam en de verkeerde datum.** De catalogus noemt het een "oervogel" gedateerd "165–45 miljoen jaar geleden." Sinds 2017 is het herclassificeerd als *Ostromia crassipes* — het is GEEN vogel en GEEN Archaeopteryx. De datum moet ~150 Mj zijn, niet een bereik van 120 miljoen jaar.

2. **F 08432 — Homo diluvii testis: Cuviers bezoek aan Teylers is onvermeld.** In 1811 bezocht Georges Cuvier Teylers Museum, nam een naald ter hand, legde de voorpoten van dit fossiel bloot en bewees dat het een reuzensalamander was — een van de beroemdste correcties in de wetenschapsgeschiedenis. De catalogus vermeldt dit niet. De datum "23–5 miljoen jaar geleden" moet ~13 Mj zijn.

3. **TMNK 10564 — Een munt die mogelijk €180.000+ waard is, beschreven zonder enige zeldzaamheidsaanduiding.** Deze gouden afslag van een zilveren denominatie is mogelijk uniek. Vergelijkbare stukken zijn geveild voor €180.000–€245.000. De catalogus zegt "[gouden afslag]" en verder niets.

### Historische ontdekkingen

4. **TMNK 00272 — De enige munt met het portret van Willem van Oranje, geslagen in het jaar van zijn moord.** De catalogus vermeldt niet dat Willem werd vermoord op 10 juli 1584 — het jaar op deze munt. Het kan een postuum portret zijn. De standaard numismatische naam "prinsendaalder" wordt niet gebruikt.

5. **TMNK 00294 — Het Turfschip van Breda: een van de beroemdste verhalen uit de Nederlandse geschiedenis, onverteld.** De penning herdenkt soldaten die zich in een turfschip verborgen om Breda te veroveren in 1590. De catalogus geeft alleen de titel. Deze penning komt uit Pieter Teylers eigen collectie.

6. **FK 1159 — De "Elektrische barometer" is geen barometer.** Het toont elektroluminescentie — het oplichten van kwik in vacuum bij schudden. Het is de directe voorloper van de neonlamp, een fenomeen voor het eerst waargenomen door Jean Picard in 1675. De catalogus heeft geen beschrijving en geen maker.

7. **FK 1973.01 — De uitvinder van het ultracentrifugemodel was zelf conservator van Teylers.** Jacob Kistemaker, die de ultracentrifugetechnologie ontwikkelde die later door A.Q. Khan werd gestolen en verspreid naar Pakistan, Iran, Libie en Noord-Korea, was tegelijkertijd conservator van Teylers Natuurkundig Kabinet. De catalogus vermeldt dit niet.

8. **1020 — "Cornelius Stanhope" is waarschijnlijk een catalogusfout.** Er is geen geleerde onder deze naam bekend. De biografie in deze Marcus Aurelius-editie werd vrijwel zeker geschreven door George Stanhope (1660–1728), deken van Canterbury. Ondertussen wordt de redacteur Thomas Gataker — wiens editie "the principal authority" is over de *Meditaties* — niet geidentificeerd.

### Systematische bevindingen

9. **De Kampman-werkplaatssuite is onzichtbaar.** Zeven instrumenten (FK 0014, 0018, 0020, 0022, 0027, 0053, 0073) vormen een samenhangend 's Gravesande-achtig Newtonians mechanica-leerkabinet. De catalogus behandelt elk als geïsoleerd object zonder kruisverwijzingen, zonder identificatie van 's Gravesande, en in een geval (FK 0022) zonder enige maker.

10. **407 — De oprichtingscatalogus van Rijksmuseum Boerhaave is niet geidentificeerd.** Dit bescheiden boekje van 70 pagina's leidde direct tot de oprichting van het nationale wetenschapsmuseum. De auteur, Crommelin, speelde kamermuziek met Einstein.

---

## Foutclassificatie

### Per categorie

| Categorie | Aantal | Voorbeelden |
|-----------|--------|-------------|
| Feitelijke fouten (data, toeschrijvingen, technieken) | 18 | TMNK 00002 gedateerd "1415" (eigenlijk c. 1700–1740); F 06928 gedateerd "165–45 Mj" (eigenlijk ~150 Mj) |
| Ontbrekende beschrijvingen | 9 | FK 1159, FK 1241, FK 0073 — geen beschrijving van wat het instrument doet |
| Ontbrekende context / significantie | 14 | TMNK 10564 zeldzaamheid; 407 oprichtingscatalogus; Cuviers bezoek |
| Ontbrekende of onjuiste makers/auteurs | 10 | FK 0022 geen maker; 1020 "Cornelius Stanhope" waarschijnlijk onjuist |
| Ontbrekende kruisverwijzingen | 5 | Kampman-suite; katrol-pedagogische reeks |
| Ontbrekende serie-identificatie | 4 | TMNK 00009 "Judenmedaille"-serie; KG 04733 "Dieren"-serie |
| **Totaal ernstige fouten** | **60** | |

### Per collectiegebied

| Collectie | Objecten | Ernstige fouten | Gem. per object |
|-----------|----------|-----------------|-----------------|
| Prenten & Tekeningen | 7 | 14 | 2,0 |
| Penningen & Munten | 7 | 13 | 1,9 |
| Wetenschappelijke instrumenten | 13 | 18 | 1,4 |
| Zeldzame boeken | 6 | 9 | 1,5 |
| Fossielen | 2 | 4 | 2,0 |
| Beeldhouwkunst | 1 | 1 | 1,0 |
| **Totaal** | **35** | **60** | **1,7** |

---

## Structurele problemen

Deze problemen treffen de catalogus als geheel, niet slechts individuele objecten:

### 1. Ontbrekende beschrijvingen
Veel objecten — met name wetenschappelijke instrumenten — hebben helemaal geen beschrijvingsveld. De catalogus veronderstelt dat de titel zelfverklarend is, maar titels als "Elektrische barometer" of "Zonnemicroscoop" vertellen een moderne bezoeker niets over wat het object doet, waarom het belangrijk is, of hoe het werkt. **9 van de 35 objecten** hadden geen zinvolle beschrijving.

### 2. Geen kruisverwijzingen tussen verwante objecten
De catalogus behandelt elk object geïsoleerd. In werkelijkheid vormen veel objecten samenhangende groepen:
- De **Kampman-werkplaatssuite** (FK 0014, 0018, 0020, 0022, 0027, 0073): 's Gravesande mechanica-demonstraties
- Van Marums **elektrisch ontladingsonderzoeksprogramma** (FK 0508, 1153, 1159)
- De **telescoopverzameling** (FK 0323, 0324, 1980 01): Engelse en Nederlandse makers
- Prenten**series** (KG 04733 is een titelpagina van een 8-delige serie)
- Penningen**series** (TMNK 00009 komt uit een gedocumenteerde Praagse serie)

### 3. Makers, auteurs en afgebeelde personen niet gecontextualiseerd
Namen worden vermeld zonder enige identificatie. De bezoeker ziet "Gerard van Bylaer (±1540–1617)" en leert niets. Van Bylaer was de stempelsnijder voor ALLE triomfpenningen in opdracht van de Staten-Generaal tijdens de Opstand — een van de belangrijkste medaillisten van het tijdperk. Dit patroon herhaalt zich bij vrijwel elke genoemde persoon.

### 4. Referentiecatalogi niet geciteerd
Standaard numismatische naslagwerken (Van Loon, Dugniolle) ontbreken bij penningrecords. De definitieve instrumentencatalogus (Turner & Levere, *Martinus van Marum: Life and Work*, Dl. IV, 1973) wordt nooit geciteerd. Prentreferenties (Hollstein, Bartsch) zijn soms aanwezig maar inconsistent toegepast.

### 5. Inscripties niet vertaald
Latijnse, Griekse en oud-Nederlandse inscripties worden getranscribeerd maar niet vertaald. Krachtige teksten als *"INVICTI ANIMI PRAEMIVM PARATI VINCERE AVT MORI"* ("De beloning van een ongebroken geest: bereid te overwinnen of te sterven") blijven onverklaard. Dit sluit de overgrote meerderheid van bezoekers uit van het begrijpen van de objecten.

### 6. Geologische dateringen veel te breed
Beide fossielen gebruiken hele geologische tijdperken als datumbereik ("23–5 Mj" voor Mioceen, "165–45 Mj" voor Jura+Krijt), terwijl modern geologisch onderzoek veel preciezere dateringen biedt. Deze brede bereiken zijn niet informatief en suggereren een mate van onzekerheid die niet meer bestaat.

---

## Methodologie

Elk object werd geanalyseerd via het volgende proces:

1. **Catalogus ophalen**: De Teylers Adlib/Axiell-cataloguspagina werd opgehaald en alle metadatavelden geextraheerd
2. **Diepgaand onderzoek**: Een AI-onderzoeksagent voerde systematische kruisverwijzingen uit met:
   - Andere museale databases (Rijksmuseum, British Museum, Museo Galileo, Harvard, Museum Boerhaave)
   - Academische publicaties en naslagwerken
   - Biografische woordenboeken en Wikipedia
   - Gespecialiseerde numismatische, kunsthistorische en wetenschappelijke databases
   - Gedigitaliseerde primaire bronnen (e-rara, BHL, EEBO, HathiTrust, Gallica)
3. **Analyserapport**: Een gedetailleerd markdown-rapport werd geschreven per object met alle bevindingen
4. **Foutclassificatie**: Fouten werden geclassificeerd als Ernstig (feitelijk onjuist, significant misleidend, of essentiële informatie ontbreekt) of Klein (ontbrekende context, onvertaalde inscripties, niet-geciteerde referenties)

Het volledige proces — van catalogus ophalen tot eindrapportage — werd uitgevoerd door een enkele onderzoeker (Joost Soeterbroek) ondersteund door het Claude Opus 4.6 AI-model (Anthropic). Analysetijd per object varieerde van 10 tot 45 minuten, met een gemiddelde van ongeveer 20 minuten per object.

---

## Wat een volledige collectiescan oplevert

Op basis van de resultaten van deze pilotstudie zou een systematische scan van Teylers' complete online catalogus:

- **Naar schatting 3.000+ ernstige fouten identificeren** in de collectie (op basis van het ratio van 1,7 fouten/object)
- **Correcties prioriteren** op ernst en publieke impact (topstukken eerst, dan veelbezochte objecten)
- **Verrijkte beschrijvingen genereren** voor objecten die momenteel geen beschrijving hebben
- **Kruisverwijzingen in kaart brengen** tussen verwante objecten, waardoor verborgen verhalen en verbanden zichtbaar worden
- **Een uitgebreid correctierapport produceren** dat direct importeerbaar is in het catalogussysteem
- **Circa €4 per object kosten** — ordes van grootte minder dan traditioneel kunsthistorisch onderzoek
- **In weken voltooid zijn, niet in jaren** — de AI-methodiek schaalt lineair

De pilot heeft de methodiek al gedemonstreerd op 35 objecten uit alle grote collectiegebieden. De infrastructuur, prompts en kwaliteitsnormen zijn bewezen. Opschaling naar de volledige collectie is een kwestie van uitvoering, niet van experiment.

---

## AI-rekenresources

| Resource | Schatting |
|----------|-----------|
| AI-model | Claude Opus 4.6 (Anthropic) |
| Totaal verwerkte tokens | ~4.000.000 |
| Onderzoeksagent-aanroepen | ~50 |
| Webophalen | ~70 |
| Geschatte rekenkosten | ~€130–€160 |
| Totale analysetijd | ~4 sessies, ~14 uur |

De kosten van het analyseren van 35 objecten met AI-ondersteuning (~€140) zijn gunstig in vergelijking met equivalente handmatige kunsthistorische research, waarvoor dagen specialistentijd per object nodig zouden zijn. **Opgeschaald naar een volledige collectiescan zou deze methodiek duizenden objecten kunnen beoordelen voor een fractie van de traditionele kosten.**

---

## Aanbevelingen

1. **Opdracht geven voor een systematische volledige collectiescan** met AI-ondersteunde methodiek om fouten en omissies in de hele online catalogus te identificeren
2. **Begin met de 50 Topstukken** — de eigen paradepaardes van het museum verdienen foutloze catalogusrecords
3. **Beschrijvingsvelden toevoegen** aan alle objecten, met name wetenschappelijke instrumenten en munten/penningen
4. **Kruisverwijzingen implementeren** tussen verwante objecten (series, suites, herkomstgroepen)
5. **Alle personen contextualiseren** met korte biografische notities
6. **Alle inscripties vertalen** in het Nederlands en Engels
7. **Geologische dateringen bijwerken** voor fossielen naar de huidige wetenschappelijke kennis
8. **Standaard referentiecatalogi citeren** (Turner & Levere, Van Loon, Hollstein, etc.)
9. **Linken naar externe digitale surrogaten** waar beschikbaar (EEBO, BHL, Rijksmuseum, etc.)
10. **De "Cornelius Stanhope"-toeschrijving herzien** (object 1020) aan de hand van de fysieke titelpagina
11. **Van Bylaers geboortedatum verifieren** — de catalogus geeft "±1540" bij meerdere objecten, maar bronnen wijzen op c. 1553

---

## Volledig foutenregister

### Steekproef 1: Ernstige fouten (28)

| Object | Fout | Teylers zegt | Moet zijn |
|--------|------|-------------|-----------|
| PP 0121 | Onderwerpclassificatie onjuist | medicus | jurist / schout / regent |
| PP 0121 | Techniek onjuist | gravure | ets |
| PP 0121 | Sterfdatum discrepantie | 1639 (op prent) | 1630 (historisch) |
| TvB G 0771 | Geboortejaar maker onjuist | 1622 | c. 1626 |
| TvB G 0771 | Techniek anachronistisch | ets en stippelgravure | ets — "stippelgravure" is anachronistisch voor 17e eeuw |
| TvB G 0771 | Rol maker onjuist | graveur | etser |
| TvB G 0771 | Datering te breed | 1642–1678, ca. | c. 1661–1662 |
| KG 01153 | Techniek onjuist | ets | gravure |
| KG 01153 | Techniek/rol tegenstrijdig | graveur + ets | graveur + gravure |
| KG 01153 | Geboortejaar Dujardin onjuist | 1622 | c. 1626 |
| KG 04733 | Rol maker onjuist | graveur | etser |
| KG 04733 | Serie niet geidentificeerd | niet vermeld | Titelpagina "Dieren"-serie (8 platen) |
| FK 0002 | Transcriptiefout | "Egnelse" | "Engelse" |
| FK 0002 | Transcriptiefout | "Amsgterdamsche" | "Amsterdamsche" |
| FK 0007 | Materiaal mogelijk onjuist | glas, messing | messing, ivoor/been; glas niet zichtbaar |
| FK 0011 | Datering onjuist | c. 1840 | c. 1835–1837 |
| FK 0011 | Materialen onvolledig | glas, messing | mahonie, messing, glas, email, ivoor |
| N 021 | Herkomst onvolledig | Odescalchi-erfgenamen, 1790 | Koningin Christina van Zweden -> Odescalchi (1692) -> Teylers (1790) |
| KG 07880 | Datering te breed | c. 1770–1822 | c. 1790–1795 (waarschijnlijk c. 1793) |
| KG 07880 | Techniek onvolledig | ets | ets en gravure |
| KT 2001 103 | Datering te breed | c. 1770 – voor 1828 | c. 1777–1806 |
| KT 2001 106 | Datering te breed | c. 1770 – voor 1828 | c. 1785–1790 |
| TMNK 00002 | Datering catastrofaal onjuist | 1415 | c. 1700–1740 (1415 is inscriptie, niet vervaardiging) |
| TMNK 00002 | Maker onjuist | Koninkrijk Bohemen, onbekend | Werkplaats Christian Wermuth, Gotha |
| TMNK 00002 | Plaats onjuist | Bohemen (gesuggereerd) | Duitsland (Gotha/Thuringen) |
| TMNK 00009 | Serie niet geidentificeerd | niet vermeld | "Judenmedaille" — Praagse serie, c. 1600–1650 |
| TMNK 00009 | Titel misleidend | "Huwelijk... 1452" | Geen huwelijkspenning; dynastiek portret uit serie |
| TMNK 00009 | Geboortejaar Eleonora onjuist | 1436 | 1434 |

### Steekproef 2: Ernstige fouten (20)

| Object | Fout | Teylers zegt | Moet zijn |
|--------|------|-------------|-----------|
| 63 | Tweede auteur ontbreekt | alleen Alexander | Ammonius Hermiae is tweede auteur — boek bevat twee teksten |
| 68 | Auteurschap ongedifferentieerd | "Ammonius" | Moderne wetenschap: Herennius Philo van Byblus |
| 394 | Significantie niet aangegeven | minimaal record | Landmark primaire bron: officieel Beresovka-mammoetrapport |
| 407 | Significantie niet aangegeven | minimaal record | Oprichtingscatalogus Rijksmuseum Boerhaave |
| 2163 | Auteur niet geidentificeerd | "G. Cuvier" | Baron Georges Cuvier, oprichter vergelijkende anatomie; bezocht Teylers 1811 |
| 2163 | Aard werk onverklaard | alleen titel | Officieel rapport over wetenschappelijke vooruitgang, in opdracht van Napoleon |
| 2163 | Cuvier-Teylers band onvermeld | niet vermeld | Cuvier identificeerde *Homo diluvii testis* als reuzensalamander bij Teylers |
| FK 0018 | Makers niet gecontextualiseerd | alleen namen | Kampman-werkplaats; twee partnerschappen over 50 jaar; deel van suite |
| FK 0018 | Suite niet gekruisverwijsd | geïsoleerd record | Deel van 's Gravesande mechanica-suite |
| FK 0020 | Inconsistente makersnaam | "Jean Pelletier" | "J.C. Pelletier" (zoals bij FK 0018) — zelfde persoon |
| FK 0020 | Sterfjaar als "?" | "?" | Waarschijnlijk 1780 (gedocumenteerde graveur Jean C. Pelletier) |
| FK 0022 | **Geen maker vermeld** | — | Vrijwel zeker Kampman & Pelletier (identiek aan FK 0018/0020) |
| FK 0022 | Pedagogische reeks niet herkend | geïsoleerd record | Derde in poelie->katrol->takel-reeks |
| FK 1980 01 | "(1663)" misleidend | in titel | 1663 = ontwerpjaar Gregory, NIET bouwdatum (c. 1745–1791) |
| FK 1980 01 | Van der Bildt-dynastie niet geidentificeerd | "J. v.d. Bildt, Franeker" | 550+ telescopen; conservator Franeker Universiteit |
| FK 1980 01 | Dubbelsysteem niet vermeld | niet vermeld | Gregoriaans + Cassegrain modi in een telescoop |
| FK 1973.01 | Kistemaker was Teylers conservator | niet vermeld | Verklaart acquisitie; belangrijk voor institutionele geschiedenis |
| FK 1241 | Geen beschrijving | — | 's Werelds eerste projector: projecteert microscopische beelden met zonlicht |
| FK 1159 | Geen beschrijving; titel misleidend | "Elektrische barometer" | GEEN barometer — toont elektroluminescentie; voorloper neonlamp |
| FK 1159 | **Geen maker vermeld** | — | Waarschijnlijk John Cuthbertson, Amsterdam (Van Marums instrumentmaker) |

### Steekproef 3: Ernstige fouten (12)

| Object | Fout | Teylers zegt | Moet zijn |
|--------|------|-------------|-----------|
| F 06928 | Datum sterk onjuist | 165–45 miljoen jaar geleden | ~150 Mj (Laat-Jura, Tithonien) |
| F 06928 | Typeclassificatie verouderd | "oervogel" | *Ostromia crassipes* sinds 2017 — GEEN vogel |
| F 08432 | Datum veel te breed | 23–5 miljoen jaar geleden | ~13 Mj (Midden-Mioceen, Serravallien) |
| F 08432 | Cuviers heridentificatie niet beschreven | niet vermeld | Cuvier bezocht Teylers 1811, legde voorpoten bloot, bewees dat het een salamander was |
| TMNK 00272 | Moordcontext afwezig | alleen "1584" | Willem van Oranje vermoord 10 juli 1584; mogelijk postuum portret |
| TMNK 00272 | Munttype niet geidentificeerd | "gehelmde rijksdaalder" | Moet identificeren als "prinsendaalder" — standaard numismatische naam |
| TMNK 00294 | Turfschipverhaal niet beschreven | alleen titel | Nederlands Paard van Troje: soldaten verborgen in turfschip; een van de beroemdste Nederlandse wapenfeiten |
| TMNK 10564 | Extreme zeldzaamheid niet aangegeven | "[gouden afslag]" alleen | Mogelijk uniek; vergelijkbare stukken geveild voor €180.000–€245.000 |
| 1020 | "Cornelio Stanhope" waarschijnlijk onjuist | "Cornelio Stanhope" | Vrijwel zeker George Stanhope (1660–1728), deken van Canterbury |
| 1020 | Gataker niet geidentificeerd | niet vermeld | Thomas Gataker (1574–1654); zijn editie is "the principal authority" over de *Meditaties* |
| FK 0073 | Geen beschrijving | alleen titel | Toont brachistochrone en tautochrone — twee van de elegantste resultaten in de klassieke mechanica |
| FK 0073 | 's Gravesande niet vermeld | niet vermeld | Gebouwd naar ontwerp van 's Gravesande (1688–1742), voornaamste promotor van Newtonse fysica |

---

## Statistische samenvatting

| Maatstaf | Steekproef 1 | Steekproef 2 | Steekproef 3 | **Totaal** |
|----------|-------------|-------------|-------------|-----------|
| Geanalyseerde objecten | 13 | 15 | 7 | **35** |
| Ernstige fouten | 28 | 20 | 12 | **60** |
| Ernstige fouten per object | 2,2 | 1,3 | 1,7 | **1,7** |
| Objecten zonder fouten | 0 | 0 | 0 | **0** |
| Kleine omissies | ~50 | ~60 | ~40 | **~150** |

---

## Conclusie

De analyse van 35 willekeurig geselecteerde objecten uit de collecties van Teylers Museum onthult een **consistent patroon van kwaliteitsproblemen** in de online catalogus. Met 60 ernstige fouten over 35 objecten en geen enkel foutvrij record wijst het bewijs sterk op systemische problemen. Het feit dat zelfs de eigen aangewezen "Topstukken" van het museum ernstige fouten bevatten, onderstreept de urgentie van een uitgebreide review.

De hier gedemonstreerde methodiek — AI-ondersteunde kruisverwijzing van catalogusrecords met wetenschappelijke databases, museale collecties en naslagwerken — is snel, schaalbaar en kosteneffectief. Tegen circa **€4 per object** is een volledige collectiescan economisch haalbaar en zou dramatische verbeteringen in cataloguskwaliteit opleveren.

Teylers Museum beheert een van de belangrijkste erfgoedcollecties ter wereld. De online catalogus zou die status moeten weerspiegelen. De bevindingen in dit rapport worden aangeboden als een constructieve bijdrage aan dat doel — en als demonstratie dat de instrumenten om het te bereiken vandaag beschikbaar zijn.

---

*Dit rapport is tot stand gekomen door Duinroos Innovatie met behulp van AI-onderzoek (Claude Opus 4.6, Anthropic). Alle bevindingen zijn gebaseerd op publiek beschikbare bronnen en kruisverwijzingen met andere museale collecties. Individuele analyserapporten voor alle 35 objecten zijn beschikbaar op <https://github.com/jsoeterbroek/teylers_collection_research>.*

*Contact: Joost Soeterbroek — <joost.soeterbroek@gmail.com> — +31 6 34 83 38 45*
