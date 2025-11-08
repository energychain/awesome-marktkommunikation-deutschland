#!/usr/bin/env python3
"""
Awesome Marktkommunikation Deutschland - Content Finder CLI
Findet relevante neue Inhalte für die Awesome Liste
"""

import argparse
import json
import sys
import urllib.parse
import urllib.request
from typing import Dict, List, Set
from awesome_common import SearchResult, URLManager


class AwesomeFinder:
    """Hauptklasse für die CLI"""

    SEARCH_API = "https://search.corrently.cloud/search"
    README_PATH = "README.md"

    # Kategorisierte Suchbegriffe
    SEARCH_TERMS = {
        "Software & Tools": [
            "EDIFACT Parser Tool",
            "Marktkommunikation Software Open Source",
            "MSCONS Converter",
            "AHB Parser",
            "BO4E Library",
        ],
        "APIs & Schnittstellen": [
            "Marktstammdatenregister API",
            "EDI Energy API",
            "AS4 Marktkommunikation",
        ],
        "Open Source Projekte": [
            "EDIFACT Open Source Germany",
            "Energiewirtschaft GitHub",
            "Smart Meter Open Source",
        ],
        "Fachportale & Blogs": [
            "Marktkommunikation Blog",
            "Energiewirtschaft Portal Deutschland",
            "BDEW News",
        ],
        "Bildung & Weiterbildung": [
            "Marktkommunikation Schulung",
            "Energiewirtschaft Kurs Online",
            "EDIFACT Training",
        ],
        "Dienstleister & IT-Services": [
            "Marktkommunikation Dienstleister Deutschland",
            "EDI Energy Service Provider",
        ],
    }

    def __init__(self):
        self.url_manager = URLManager(self.README_PATH)
        count = self.url_manager.load_existing_urls()
        if count > 0:
            print(f"✓ {count} bestehende URLs geladen")
        else:
            print("⚠ README.md nicht gefunden")
            sys.exit(1)

    def search(self, query: str) -> List[SearchResult]:
        """Führt eine Suche über die API durch"""
        params = {
            'q': query,
            'language': 'auto',
            'time_range': '',
            'safesearch': '0',
            'categories': 'general',
            'format': 'json'
        }

        url = f"{self.SEARCH_API}?{urllib.parse.urlencode(params)}"

        try:
            with urllib.request.urlopen(url, timeout=10) as response:
                data = json.loads(response.read().decode('utf-8'))

            results = []
            for item in data.get('results', []):
                result = SearchResult(
                    title=item.get('title', ''),
                    url=item.get('url', ''),
                    content=item.get('content', ''),
                    score=item.get('score', 0.0),
                    engine=item.get('engine', '')
                )
                results.append(result)

            return results
        except Exception as e:
            print(f"⚠ Fehler bei Suche '{query}': {e}")
            return []

    def is_relevant(self, result: SearchResult) -> bool:
        """Prüft ob ein Ergebnis relevant ist"""
        url_lower = result.url.lower()

        # Filtere offensichtlich irrelevante Domains
        irrelevant_domains = [
            'facebook.com', 'twitter.com', 'instagram.com',
            'linkedin.com/posts', 'youtube.com/watch',
            'amazon.', 'ebay.', 'wikipedia.org'
        ]

        for domain in irrelevant_domains:
            if domain in url_lower:
                return False

        # Prüfe auf deutsche Domains oder .de
        has_german_tld = '.de' in url_lower or 'deutschland' in url_lower

        # Oder relevante Keywords
        relevant_keywords = [
            'energie', 'strom', 'gas', 'bdew', 'edi', 'edifact',
            'markt', 'netz', 'mscons', 'utilmd', 'smart meter',
            'bo4e', 'hochfrequenz', 'mako', 'bnetza', 'bundesnetzagentur'
        ]

        content_lower = (result.title + ' ' + result.content).lower()
        has_keywords = any(kw in content_lower for kw in relevant_keywords)

        return (has_german_tld or has_keywords) and result.score > 0.5

    def filter_duplicates(self, results: List[SearchResult]) -> List[SearchResult]:
        """Filtert bereits vorhandene URLs"""
        filtered = []
        for result in results:
            if not self.url_manager.is_duplicate(result.url):
                filtered.append(result)
        return filtered

    def find_category(self, result: SearchResult) -> str:
        """Versucht die passende Kategorie zu bestimmen"""
        content_lower = (result.title + ' ' + result.content + ' ' + result.url).lower()

        # Kategoriezuordnung basierend auf Keywords
        category_keywords = {
            "Open Source Projekte": ['github.com', 'gitlab', 'open source', 'opensource'],
            "Software & Tools": ['tool', 'software', 'converter', 'parser', 'library', 'sdk'],
            "APIs & Schnittstellen": ['api', 'rest', 'soap', 'webservice', 'schnittstelle'],
            "Fachportale & Blogs": ['blog', 'news', 'portal', 'magazin', 'artikel'],
            "Bildung & Weiterbildung": ['schulung', 'kurs', 'training', 'seminar', 'webinar', 'lernen'],
            "Dienstleister & IT-Services": ['dienstleister', 'service', 'beratung', 'consulting', 'gmbh', 'ag'],
            "BDEW Veröffentlichungen & Standards": ['bdew', 'standard', 'veröffentlichung'],
            "Bundesnetzagentur Ressourcen": ['bundesnetzagentur', 'bnetza'],
            "Messstellenbetrieb & Smart Meter": ['smart meter', 'messstelle', 'messstellenbetrieb', 'imsy'],
        }

        scores = {}
        for category, keywords in category_keywords.items():
            score = sum(1 for kw in keywords if kw in content_lower)
            if score > 0:
                scores[category] = score

        if scores:
            return max(scores, key=scores.get)

        return "Software & Tools"  # Default

    def run_search(self, category: str = None, limit: int = 10):
        """Führt Suchen durch und zeigt Ergebnisse"""
        all_results = []

        # Wähle Suchbegriffe basierend auf Kategorie
        if category:
            search_terms = {category: self.SEARCH_TERMS.get(category, [])}
        else:
            search_terms = self.SEARCH_TERMS

        print(f"\n🔍 Starte Suche in {len(search_terms)} Kategorien...\n")

        for cat, terms in search_terms.items():
            print(f"📂 {cat}:")
            for term in terms:
                print(f"  → {term}...", end=' ')
                results = self.search(term)
                relevant = [r for r in results if self.is_relevant(r)]
                filtered = self.filter_duplicates(relevant)

                # Setze Kategorie
                for result in filtered:
                    result.category = cat

                all_results.extend(filtered[:2])  # Max 2 pro Suchbegriff
                print(f"{len(filtered)} neue")

        # Dedupliziere und sortiere nach Score
        seen_urls = set()
        unique_results = []
        for result in sorted(all_results, key=lambda x: x.score, reverse=True):
            normalized = URLManager.normalize_url(result.url)
            if normalized not in seen_urls:
                seen_urls.add(normalized)
                unique_results.append(result)

        # Begrenze auf limit
        unique_results = unique_results[:limit]

        print(f"\n✓ {len(unique_results)} relevante neue Einträge gefunden\n")

        return unique_results

    def display_results(self, results: List[SearchResult]):
        """Zeigt Ergebnisse an"""
        if not results:
            print("Keine neuen relevanten Inhalte gefunden.")
            return

        print("=" * 80)
        for i, result in enumerate(results, 1):
            print(f"\n[{i}] {result.title}")
            print(f"    URL: {result.url}")
            print(f"    Kategorie: {result.category}")
            print(f"    Score: {result.score:.2f}")
            print(f"    Beschreibung: {result.content[:150]}...")
        print("\n" + "=" * 80)


def main():
    parser = argparse.ArgumentParser(
        description='Findet relevante neue Inhalte für die Awesome Marktkommunikation Liste'
    )
    parser.add_argument(
        '--category', '-c',
        choices=list(AwesomeFinder.SEARCH_TERMS.keys()),
        help='Nur in einer bestimmten Kategorie suchen'
    )
    parser.add_argument(
        '--limit', '-l',
        type=int,
        default=10,
        help='Maximale Anzahl von Ergebnissen (default: 10)'
    )
    parser.add_argument(
        '--export', '-e',
        help='Exportiere Ergebnisse in JSON-Datei'
    )

    args = parser.parse_args()

    finder = AwesomeFinder()
    results = finder.run_search(category=args.category, limit=args.limit)
    finder.display_results(results)

    if args.export and results:
        with open(args.export, 'w', encoding='utf-8') as f:
            data = [
                {
                    'title': r.title,
                    'url': r.url,
                    'category': r.category,
                    'content': r.content,
                    'score': r.score
                }
                for r in results
            ]
            json.dump(data, f, indent=2, ensure_ascii=False)
        print(f"\n✓ Ergebnisse exportiert nach {args.export}")


if __name__ == '__main__':
    main()
