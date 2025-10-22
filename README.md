# Awesome Marktkommunikation Deutschland ⚡️

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

Eine kuratierte Liste von Tools, Bibliotheken, Dokumentationen und Ressourcen für die Marktkommunikation in der deutschen Energiewirtschaft.

Die Marktkommunikation (MaKo) ist der standardisierte Datenaustausch zwischen Marktteilnehmern im liberalisierten deutschen Energiemarkt. Sie regelt die elektronische Kommunikation zwischen Netzbetreibern, Lieferanten, Messstellenbetreibern und weiteren Akteuren.

## Inhalt

- [Standards und Spezifikationen](#standards-und-spezifikationen)
- [Organisationen und Regulierer](#organisationen-und-regulierer)
- [Nachrichtenformate](#nachrichtenformate)
- [Tools und Software](#tools-und-software)
- [Bibliotheken und APIs](#bibliotheken-und-apis)
- [Dokumentation und Handbücher](#dokumentation-und-handbücher)
- [Testumgebungen](#testumgebungen)
- [Schulungen und Weiterbildung](#schulungen-und-weiterbildung)
- [Community und Austausch](#community-und-austausch)
- [Verwandte Themen](#verwandte-themen)

## Standards und Spezifikationen

### EDIFACT

- [UN/EDIFACT](https://unece.org/trade/uncefact/introducing-unedifact) - International standardisiertes elektronisches Datenaustauschformat für Geschäftskommunikation
- [EDIFACT Subset für die deutsche Energiewirtschaft](https://www.edi-energy.de/) - Anwendung von EDIFACT für den deutschen Energiemarkt

### Marktkommunikation

- [EDI@Energy](https://www.edi-energy.de/) - Zentrale Plattform für Formate und Prozesse der Marktkommunikation
- [MIG (Marktinformationsgeber)](https://www.edi-energy.de/) - Informationen zu Marktprozessen und -rollen
- [GPKE (Geschäftsprozesse zur Kundenbelieferung mit Elektrizität)](https://www.bdew.de/energie/marktprozesse/geschaeftsprozesse-und-datenformate/) - Geschäftsprozesse für Strom
- [GeLi Gas (Geschäftsprozesse Lieferantenwechsel Gas)](https://www.bdew.de/energie/marktprozesse/geschaeftsprozesse-und-datenformate/) - Geschäftsprozesse für Gas
- [WiM (Wechselprozesse im Messwesen)](https://www.edi-energy.de/) - Prozesse für Messstellenwechsel
- [MPES (Marktprozesse für intelligente Messsysteme)](https://www.edi-energy.de/) - Prozesse für Smart Meter

## Organisationen und Regulierer

### Behörden

- [Bundesnetzagentur (BNetzA)](https://www.bundesnetzagentur.de/) - Regulierungsbehörde für Elektrizität, Gas, Telekommunikation, Post und Eisenbahnen
- [Bundesministerium für Wirtschaft und Klimaschutz (BMWK)](https://www.bmwk.de/) - Übergeordnetes Ministerium für Energiepolitik

### Verbände

- [BDEW (Bundesverband der Energie- und Wasserwirtschaft)](https://www.bdew.de/) - Hauptverband der Energiewirtschaft
- [VKU (Verband kommunaler Unternehmen)](https://www.vku.de/) - Verband kommunaler Energieversorger
- [ZVEI (Zentralverband Elektrotechnik- und Elektronikindustrie)](https://www.zvei.org/) - Verband für Elektrotechnik und Elektronikindustrie

### Standardisierung

- [FNN (Forum Netztechnik/Netzbetrieb im VDE)](https://www.vde.com/de/fnn) - Technische Regeln und Standards für Netzbetrieb
- [DKE (Deutsche Kommission Elektrotechnik)](https://www.dke.de/) - Normungsorganisation

## Nachrichtenformate

### Stammdaten

- **UTILMD (Utilities Master Data)** - Austausch von Stammdaten (Marktlokationen, Zählpunkte, Kunden)
- **PRICAT (Price Catalogue)** - Preisblätter und Tarifstrukturen

### Messwerte und Abrechnungsdaten

- **MSCONS (Metered Services Consumption Report)** - Zählerstände und Verbrauchswerte
- **INVOIC (Invoice)** - Rechnungen
- **REMADV (Remittance Advice)** - Zahlungsavise

### Prozessnachrichten

- **APERAK (Application Error and Acknowledgement)** - Anwendungsbestätigungen und Fehlermeldungen
- **CONTRL (Control Message)** - Technische Empfangsbestätigungen
- **ORDCHG (Order Change)** - Bestellungsänderungen
- **ORDERS (Order)** - Bestellungen
- **QUOTES (Quote)** - Angebote

### Netzbezogene Nachrichten

- **IFTSTA (International Forwarding and Transport Status)** - Statusmeldungen
- **REQOTE (Request for Quote)** - Angebotsanfragen

## Tools und Software

### Konverter und Parser

- [Robotron EDIFACT Konverter](https://www.robotron.de/produkte/robotronedifactkonverter/) - Kommerzieller EDIFACT Konverter
- [EDI Inspector](https://www.ediinspector.com/) - Viewer und Validator für EDI-Nachrichten

### Entwicklertools

- [EDI Energy Validator](https://www.edi-energy.de/) - Validierungstools für EDI@Energy Nachrichten
- [EDIFACT Parser Bibliotheken](https://github.com/search?q=edifact+parser) - Open-Source Parser auf GitHub

### Middleware und Integration

- [SEEBURGER Business Integration Suite](https://www.seeburger.com/) - EDI-Middleware für B2B-Integration
- [Lobster_data](https://www.lobster.de/) - Datenaustausch- und Integrationsplattform
- [SAP PI/PO](https://www.sap.com/products/process-integration.html) - SAP Process Integration/Orchestration

### Test- und Entwicklungsumgebungen

- [EDIFACT Test Services](https://www.edi-energy.de/) - Testumgebungen von EDI@Energy
- [edi_energy_scraper](https://github.com/Hochfrequenz/edi_energy_scraper) - Tool zum Herunterladen von EDI@Energy Dokumenten

## Bibliotheken und APIs

### Python

- [maus](https://github.com/Hochfrequenz/maus) - Python-Bibliothek für Marktkommunikation
- [edifact](https://github.com/nerdocs/edifact) - EDIFACT Parser für Python
- [edi_energy_mirror](https://github.com/Hochfrequenz/edi_energy_mirror) - Mirror von EDI@Energy Dokumenten

### Java

- [EDI Solutions für Java](https://www.seeburger.com/de/ressourcen/technologie/java-edi/) - Java-basierte EDI-Lösungen
- [smooks](https://www.smooks.org/) - Framework für nachrichtenbasierte Transformationen

### JavaScript/TypeScript

- [edifact-parser-ts](https://github.com/search?q=edifact+typescript) - TypeScript EDIFACT Parser

### .NET

- [EDI.Net](https://github.com/indice-co/EDI.Net) - .NET EDIFACT/X12 Parser und Serializer

## Dokumentation und Handbücher

### Offizielle Dokumentation

- [EDI@Energy Dokumentenablage](https://www.edi-energy.de/) - Zentrale Dokumentenablage mit AHB, MIG, etc.
- [BDEW Marktprozesse](https://www.bdew.de/energie/marktprozesse/) - Übersicht über Marktprozesse
- [Bundesnetzagentur Festlegungen](https://www.bundesnetzagentur.de/DE/Beschlusskammern/beschlusskammern-node.html) - Regulatorische Vorgaben

### Anwendungshandbücher (AHB)

- **AHB UTILMD** - Anwendungshandbuch für Stammdatenaustausch
- **AHB MSCONS** - Anwendungshandbuch für Messwertaustausch
- **AHB INVOIC** - Anwendungshandbuch für Rechnungsaustausch

### Nachrichtenleitfäden

- [edi@energy-Nachrichtenleitfaden](https://www.edi-energy.de/) - Leitfäden für die Nachrichtenimplementierung

## Testumgebungen

- [EDI@Energy Testportal](https://www.edi-energy.de/) - Offizielle Testumgebung
- [Prüftools der Bundesnetzagentur](https://www.bundesnetzagentur.de/) - Validierungstools für regulatorische Anforderungen

## Schulungen und Weiterbildung

### Schulungsanbieter

- [BDEW Akademie](https://www.bdew-akademie.de/) - Schulungen zu Energiemarkt und Marktkommunikation
- [VKU Akademie](https://www.vku.de/themen/bildung/) - Weiterbildung für kommunale Unternehmen
- [Private Schulungsanbieter](https://www.energie-akademie.com/) - Spezialisierte Energiemarkt-Schulungen

### Online-Ressourcen

- [EDI@Energy Leitfaden](https://www.edi-energy.de/) - Online-Dokumentation und Tutorials
- [Bundesnetzagentur Informationsseiten](https://www.bundesnetzagentur.de/DE/Fachthemen/fachthemen-node.html) - Regulatorische Informationen

## Community und Austausch

### Foren und Diskussionsgruppen

- [BDEW Arbeitskreise](https://www.bdew.de/) - Arbeitskreise zu Marktkommunikation
- [EDI@Energy Konsultationen](https://www.edi-energy.de/) - Konsultationsverfahren für Formatänderungen

### Veranstaltungen

- **BDEW Kongress** - Jährlicher Branchenkongress
- **E-world energy & water** - Leitmesse der Energiewirtschaft
- **VKU Stadtwerke-Kongress** - Kongress für kommunale Unternehmen

## Verwandte Themen

### Smart Metering

- [BSI Smart Meter Gateway](https://www.bsi.bund.de/DE/Themen/Unternehmen-und-Organisationen/Standards-und-Zertifizierung/Smart-Metering/smart-metering.html) - Technische Richtlinien für Smart Meter
- [CLS (Controllable Local Systems)](https://www.edi-energy.de/) - Steuerbare Verbrauchseinrichtungen

### Energiedatenmanagement

- [EDIFACT für Energiedatenmanagement](https://www.edi-energy.de/) - EDI-Prozesse im Datenmanagement
- [Marktlokationen und Messlokationen](https://www.bdew.de/) - Identifikation im Energiemarkt

### Bilanzierung und Prognosen

- [Bilanzkreismanagement](https://www.bdew.de/energie/bilanzierung/) - Prozesse der Energiebilanzierung
- [GPKE und GeLi Gas](https://www.bdew.de/) - Mehr- und Mindermengenabrechnung

### Redispatch und Netzengpässe

- [Redispatch 2.0](https://www.bundesnetzagentur.de/redispatch) - Neue Prozesse zur Engpassbewirtschaftung
- [EEG-Einspeisemanagement](https://www.bundesnetzagentur.de/) - Management erneuerbarer Energien

## Beitragen

Beiträge sind willkommen! Bitte lesen Sie [CONTRIBUTING.md](CONTRIBUTING.md) für Details zum Verhaltenskodex und zum Prozess für Pull Requests.

## Lizenz

[![CC0](https://mirrors.creativecommons.org/presskit/buttons/88x31/svg/cc-zero.svg)](https://creativecommons.org/publicdomain/zero/1.0)

Soweit gesetzlich möglich, hat [STROMDAO](https://github.com/energychain) alle Urheberrechte und verwandten Rechte an diesem Werk aufgegeben.