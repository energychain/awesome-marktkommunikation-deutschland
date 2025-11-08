# Awesome Finder Tools

Automatisierte Tools zum Finden und Hinzufügen neuer relevanter Inhalte für die Awesome Marktkommunikation Deutschland Liste.

## Übersicht

Das Projekt enthält zwei CLI-Tools:

1. **awesome_finder.py** - Findet neue relevante Inhalte über die Corrently Search API
2. **awesome_add.py** - Interaktives Tool zum Prüfen, Validieren und Hinzufügen von Inhalten

## Installation

```bash
# Keine externe Dependencies - nutzt Python Standard Library
python3 --version  # Python 3.7+ erforderlich

# Skripte ausführbar machen
chmod +x awesome_finder.py awesome_add.py
```

## Usage

### 1. Neue Inhalte finden (awesome_finder.py)

Sucht nach neuen relevanten Inhalten und zeigt diese an:

```bash
# Alle Kategorien durchsuchen
python3 awesome_finder.py

# Nur bestimmte Kategorie
python3 awesome_finder.py --category "Open Source Projekte"

# Mit Limit
python3 awesome_finder.py --limit 20

# Ergebnisse in JSON exportieren
python3 awesome_finder.py --export results.json
```

**Optionen:**
- `--category, -c` - Nur in einer bestimmten Kategorie suchen
- `--limit, -l` - Maximale Anzahl von Ergebnissen (default: 10)
- `--export, -e` - Exportiere Ergebnisse in JSON-Datei

**Verfügbare Kategorien:**
- Software & Tools
- APIs & Schnittstellen
- Open Source Projekte
- Fachportale & Blogs
- Bildung & Weiterbildung
- Dienstleister & IT-Services

### 2. Interaktiv Inhalte hinzufügen (awesome_add.py)

Prüft gefundene Inhalte und fügt sie interaktiv zur README hinzu:

```bash
# Neue Suche durchführen und interaktiv hinzufügen
python3 awesome_add.py

# Nur bestimmte Kategorie
python3 awesome_add.py --category "Open Source Projekte"

# Von vorher exportierter JSON-Datei
python3 awesome_add.py --from-file results.json

# Mit Limit
python3 awesome_add.py --limit 5
```

**Optionen:**
- `--category, -c` - Nur in einer bestimmten Kategorie suchen
- `--limit, -l` - Maximale Anzahl von Ergebnissen (default: 5)
- `--from-file, -f` - Lade Ergebnisse aus JSON-Datei

## Workflow

### Empfohlener Workflow:

1. **Suche durchführen:**
   ```bash
   python3 awesome_finder.py --export results.json
   ```

2. **Ergebnisse prüfen:**
   ```bash
   python3 awesome_add.py --from-file results.json
   ```

3. **Interaktive Prüfung:**
   - Für jeden Vorschlag wird angezeigt:
     - Titel und URL
     - Vorgeschlagene Kategorie
     - Content-Beschreibung
     - Qualitäts-Score
     - Risiko-Bewertung

4. **Optionen pro Eintrag:**
   - `[y]` - Hinzufügen mit automatischer Beschreibung
   - `[e]` - Hinzufügen mit eigener Beschreibung
   - `[c]` - Kategorie ändern und hinzufügen
   - `[n]` - Überspringen
   - `[q]` - Abbrechen

5. **Automatische Git-Integration:**
   - Bei Bestätigung wird automatisch:
     - README.md aktualisiert (alphabetisch sortiert)
     - Git commit erstellt
     - Optional: Push zu GitHub

## Features

### awesome-finder.py

- ✓ Intelligente Suchbegriffe für verschiedene Kategorien
- ✓ Duplikat-Filterung gegen bestehende README.md
- ✓ Relevanz-Bewertung mit Score
- ✓ Automatische Kategoriezuordnung
- ✓ JSON-Export für weitere Verarbeitung

### awesome-add.py

- ✓ Interaktive Content-Prüfung
- ✓ Qualitäts-Checks:
  - HTTPS-Verwendung
  - Deutsche Fokussierung
  - Zuverlässige Domains
  - Relevanz-Score
- ✓ Risiko-Bewertung (Social Media, Commercial-Only, etc.)
- ✓ Automatische alphabetische Sortierung
- ✓ Git-Integration:
  - Automatische Commits mit standardisiertem Format
  - Optional: Push zu GitHub
  - Co-Authored-By: Claude

## Suchbegriffe

Die Tools verwenden kategorisierte Suchbegriffe:

**Software & Tools:**
- EDIFACT Parser Tool
- Marktkommunikation Software Open Source
- MSCONS Converter
- AHB Parser
- BO4E Library

**APIs & Schnittstellen:**
- Marktstammdatenregister API
- EDI Energy API
- AS4 Marktkommunikation

**Open Source Projekte:**
- EDIFACT Open Source Germany
- Energiewirtschaft GitHub
- Smart Meter Open Source

**Fachportale & Blogs:**
- Marktkommunikation Blog
- Energiewirtschaft Portal Deutschland
- BDEW News

**Bildung & Weiterbildung:**
- Marktkommunikation Schulung
- Energiewirtschaft Kurs Online
- EDIFACT Training

**Dienstleister & IT-Services:**
- Marktkommunikation Dienstleister Deutschland
- EDI Energy Service Provider

## Content-Qualitätskriterien

### Qualitäts-Checks:
- ✓ HTTPS-Nutzung
- ✓ Deutsche Fokussierung (.de, deutschland, etc.)
- ✓ Zuverlässige Domains (Behörden, Organisationen, Fachportale)
- ✓ Guter Relevanz-Score (> 1.0)

### Risiko-Checks:
- ⚠ Social Media Posts (nicht generelle Profile)
- ⚠ Rein kommerzielle Shop-Links

### Irrelevante Domains (automatisch gefiltert):
- Social Media Posts (Facebook, Twitter, LinkedIn Posts)
- Video-Plattformen (YouTube Watch-Links)
- Shopping-Plattformen (Amazon, eBay)
- Wikipedia (bereits gut dokumentiert)

## Git-Commit-Format

Automatisch generierte Commits folgen diesem Format:

```
docs: add [Titel] to [Kategorie]

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
```

## Beispiele

### Beispiel 1: Schnelle Suche und Hinzufügen

```bash
# Suche in Open Source Kategorie
python3 awesome_add.py --category "Open Source Projekte" --limit 3

# Interaktive Prüfung:
# [1/3] MIG Validator Tool
# URL: https://github.com/example/mig-validator
# Kategorie: Open Source Projekte
# Score: 2.5
#
# ✓ Empfohlen (Qualität: 4/4, Risiko: 0)
#
# Optionen:
#   [y] Hinzufügen
#   ...
# Auswahl: y
#
# → Füge hinzu zu 'Open Source Projekte'...
#   ✓ README.md aktualisiert
#   ✓ Git add
#   ✓ Git commit
#   Push zu GitHub? [y/N]: y
#   ✓ Git push
```

### Beispiel 2: Export und spätere Verarbeitung

```bash
# Schritt 1: Suche exportieren
python3 awesome_finder.py --limit 20 --export search-results.json

# Schritt 2: Später verarbeiten
python3 awesome_add.py --from-file search-results.json
```

### Beispiel 3: Alle Kategorien durchsuchen

```bash
# Findet in allen 6 Kategorien nach neuen Inhalten
python3 awesome_finder.py --limit 15
```

## Erweitern

### Neue Suchbegriffe hinzufügen

Editiere `awesome_finder.py` und füge zu `SEARCH_TERMS` hinzu:

```python
SEARCH_TERMS = {
    "Meine Kategorie": [
        "Suchbegriff 1",
        "Suchbegriff 2",
    ],
    # ...
}
```

### Neue Kategorien hinzufügen

Die Kategorien müssen in der README.md als `## Kategorie` Header existieren.

## Troubleshooting

### "README.md nicht gefunden"
→ Führe die Skripte im Root-Verzeichnis des Repositories aus

### "Kategorie nicht gefunden"
→ Prüfe, ob die Kategorie exakt so in README.md als `## Kategorie` existiert

### "Git push fehlgeschlagen"
→ Prüfe Git-Konfiguration und GitHub-Zugriffsrechte

## Lizenz

Teil des Awesome Marktkommunikation Deutschland Projekts
