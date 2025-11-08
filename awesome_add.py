#!/usr/bin/env python3
"""
Awesome Marktkommunikation Deutschland - Interactive Content Adder
Interaktives Tool zum Hinzufügen neuer Inhalte mit Content-Prüfung und Git-Integration
"""

import json
import os
import re
import subprocess
import sys
from typing import List, Optional
from awesome_common import SearchResult, clean_description
from awesome_finder import AwesomeFinder


class ContentReviewer:
    """Prüft und bewertet Content für die Awesome Liste"""

    def __init__(self):
        pass

    def review_content(self, result: SearchResult) -> dict:
        """Bewertet einen Content-Vorschlag"""
        url_lower = result.url.lower()

        # Qualitätskriterien
        quality_checks = {
            'has_https': url_lower.startswith('https://'),
            'german_focus': any(marker in url_lower for marker in ['.de', 'deutschland', 'german']),
            'reliable_domain': self.is_reliable_domain(url_lower),
            'good_score': result.score > 1.0,
        }

        # Risiko-Checks
        risk_checks = {
            'social_media': any(sm in url_lower for sm in ['facebook', 'twitter', 'linkedin/posts']),
            'commercial_only': any(cm in url_lower for cm in ['shop', 'kaufen', 'bestellen']),
        }

        quality_score = sum(quality_checks.values())
        risk_score = sum(risk_checks.values())

        recommendation = "✓ Empfohlen" if quality_score >= 2 and risk_score == 0 else "⚠ Prüfen"

        return {
            'quality_score': quality_score,
            'risk_score': risk_score,
            'checks': quality_checks,
            'risks': risk_checks,
            'recommendation': recommendation
        }

    def is_reliable_domain(self, url: str) -> bool:
        """Prüft ob die Domain zuverlässig erscheint"""
        reliable_markers = [
            # Behörden
            'bund.de', 'bundesnetzagentur', 'bsi.bund.de',
            # Organisationen
            'bdew.de', 'vde.com', 'dvgw.de', 'vku.de',
            # Etablierte Unternehmen
            'github.com', 'gitlab',
            # Fachportale
            'energie', 'strom',
        ]
        return any(marker in url for marker in reliable_markers)


class GitIntegration:
    """Git-Integration für automatische Commits"""

    def __init__(self, repo_path: str = "."):
        self.repo_path = repo_path

    def run_git(self, *args) -> tuple[int, str, str]:
        """Führt Git-Befehl aus"""
        try:
            result = subprocess.run(
                ['git'] + list(args),
                cwd=self.repo_path,
                capture_output=True,
                text=True,
                timeout=30
            )
            return result.returncode, result.stdout, result.stderr
        except Exception as e:
            return 1, "", str(e)

    def check_status(self) -> bool:
        """Prüft Git-Status"""
        returncode, stdout, stderr = self.run_git('status', '--porcelain')
        return returncode == 0

    def add_file(self, filepath: str) -> bool:
        """Fügt Datei zu Git hinzu"""
        returncode, _, _ = self.run_git('add', filepath)
        return returncode == 0

    def commit(self, message: str) -> bool:
        """Erstellt einen Commit"""
        commit_message = f"""{message}

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>"""

        returncode, _, _ = self.run_git('commit', '-m', commit_message)
        return returncode == 0

    def push(self, remote: str = 'origin', branch: str = 'main') -> bool:
        """Pusht zum Remote Repository"""
        returncode, _, stderr = self.run_git('push', remote, branch)
        if returncode != 0:
            print(f"⚠ Push fehlgeschlagen: {stderr}")
        return returncode == 0


class AwesomeAdder:
    """Hauptklasse für interaktives Hinzufügen"""

    README_PATH = "README.md"

    def __init__(self):
        self.finder = AwesomeFinder()
        self.reviewer = ContentReviewer()
        self.git = GitIntegration()
        self.readme_lines: List[str] = []
        self.load_readme()

    def load_readme(self):
        """Lädt README.md"""
        try:
            with open(self.README_PATH, 'r', encoding='utf-8') as f:
                self.readme_lines = f.readlines()
        except FileNotFoundError:
            print("⚠ README.md nicht gefunden")
            sys.exit(1)

    def save_readme(self):
        """Speichert README.md"""
        with open(self.README_PATH, 'w', encoding='utf-8') as f:
            f.writelines(self.readme_lines)

    def find_category_section(self, category: str) -> Optional[int]:
        """Findet die Zeile einer Kategorie-Section"""
        # Suche nach "## Kategorie"
        pattern = f"## {re.escape(category)}"
        for i, line in enumerate(self.readme_lines):
            if re.match(pattern, line):
                return i
        return None

    def insert_entry(self, category: str, title: str, url: str, description: str = "") -> bool:
        """Fügt einen Eintrag in die README ein"""
        section_line = self.find_category_section(category)

        if section_line is None:
            print(f"⚠ Kategorie '{category}' nicht gefunden")
            return False

        # Finde Ende der Section (nächste ## oder EOF)
        insert_pos = section_line + 2  # Skip header und leere Zeile

        # Sammle alle Einträge in dieser Section
        entries = []
        i = insert_pos
        while i < len(self.readme_lines):
            line = self.readme_lines[i]
            # Ende bei nächster Section oder EOF
            if line.startswith('##') or line.startswith('---'):
                break
            if line.strip().startswith('-'):
                entries.append((i, line))
            i += 1

        # Bereite neuen Eintrag vor
        if description:
            new_entry = f"- [{title}]({url}) - {description}\n"
        else:
            new_entry = f"- [{title}]({url})\n"

        # Finde alphabetische Position
        entries_text = [entry[1] for entry in entries]
        entries_text.append(new_entry)
        entries_text.sort(key=lambda x: x.lower())

        insert_index = entries_text.index(new_entry)

        if insert_index < len(entries):
            # Füge vor bestehendem Eintrag ein
            actual_line = entries[insert_index][0]
            self.readme_lines.insert(actual_line, new_entry)
        else:
            # Füge am Ende ein
            if entries:
                actual_line = entries[-1][0] + 1
            else:
                actual_line = insert_pos
            self.readme_lines.insert(actual_line, new_entry)

        return True

    def interactive_add(self, results: List[SearchResult]):
        """Interaktiver Prozess zum Hinzufügen von Einträgen"""
        if not results:
            print("\nKeine Vorschläge vorhanden.")
            return

        added_count = 0

        print("\n" + "=" * 80)
        print("INTERAKTIVE CONTENT-PRÜFUNG")
        print("=" * 80)

        for i, result in enumerate(results, 1):
            print(f"\n\n[{i}/{len(results)}] {result.title}")
            print(f"URL: {result.url}")
            print(f"Kategorie: {result.category}")
            print(f"Score: {result.score:.2f}")
            print(f"\nBeschreibung:\n{result.content[:200]}...")

            # Content Review
            review = self.reviewer.review_content(result)
            print(f"\n{review['recommendation']} (Qualität: {review['quality_score']}/4, Risiko: {review['risk_score']})")

            # Details anzeigen
            print("\nQualitätschecks:")
            for check, passed in review['checks'].items():
                icon = "✓" if passed else "✗"
                print(f"  {icon} {check}")

            if review['risks']:
                print("\nRisiken:")
                for risk, triggered in review['risks'].items():
                    if triggered:
                        print(f"  ⚠ {risk}")

            # User-Entscheidung
            print("\nOptionen:")
            print("  [y] Hinzufügen")
            print("  [e] Hinzufügen mit eigener Beschreibung")
            print("  [c] Kategorie ändern")
            print("  [n] Überspringen")
            print("  [q] Abbrechen")

            choice = input("\nAuswahl: ").lower().strip()

            if choice == 'q':
                break
            elif choice == 'n':
                continue
            elif choice == 'y':
                # Extrahiere kurze Beschreibung aus Content
                desc = clean_description(result.content) if result.content else ""
                if self.add_entry_with_commit(result.category, result.title, result.url, desc):
                    added_count += 1
            elif choice == 'e':
                desc = input("Beschreibung eingeben: ").strip()
                # Stelle sicher dass Beschreibung mit Punktierung endet
                desc = clean_description(desc) if desc else ""
                if self.add_entry_with_commit(result.category, result.title, result.url, desc):
                    added_count += 1
            elif choice == 'c':
                new_category = input("Neue Kategorie: ").strip()
                result.category = new_category
                desc = clean_description(result.content) if result.content else ""
                if self.add_entry_with_commit(result.category, result.title, result.url, desc):
                    added_count += 1

        print(f"\n\n✓ {added_count} Einträge hinzugefügt")

    def add_entry_with_commit(self, category: str, title: str, url: str, description: str) -> bool:
        """Fügt Eintrag hinzu und erstellt Git-Commit"""
        print(f"\n→ Füge hinzu zu '{category}'...")

        # Insert into README
        if not self.insert_entry(category, title, url, description):
            return False

        # Save README
        self.save_readme()
        print("  ✓ README.md aktualisiert")

        # Git add
        if not self.git.add_file(self.README_PATH):
            print("  ⚠ Git add fehlgeschlagen")
            return False
        print("  ✓ Git add")

        # Git commit
        commit_msg = f"docs: add {title} to {category}"
        if not self.git.commit(commit_msg):
            print("  ⚠ Git commit fehlgeschlagen")
            return False
        print("  ✓ Git commit")

        # Frage nach Push
        push_now = input("  Push zu GitHub? [y/N]: ").lower().strip()
        if push_now == 'y':
            if self.git.push():
                print("  ✓ Git push")
            else:
                print("  ⚠ Git push fehlgeschlagen")

        # Reload README für nächste Einträge
        self.load_readme()

        return True


def main():
    import argparse

    parser = argparse.ArgumentParser(
        description='Interaktives Tool zum Hinzufügen neuer Inhalte'
    )
    parser.add_argument(
        '--category', '-c',
        help='Nur in einer bestimmten Kategorie suchen'
    )
    parser.add_argument(
        '--limit', '-l',
        type=int,
        default=5,
        help='Maximale Anzahl von Ergebnissen (default: 5)'
    )
    parser.add_argument(
        '--from-file', '-f',
        help='Lade Ergebnisse aus JSON-Datei'
    )

    args = parser.parse_args()

    adder = AwesomeAdder()

    if args.from_file:
        # Lade von Datei
        with open(args.from_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
            results = [
                SearchResult(
                    title=item['title'],
                    url=item['url'],
                    content=item['content'],
                    score=item['score'],
                    engine='',
                    category=item['category']
                )
                for item in data
            ]
    else:
        # Führe neue Suche durch
        results = adder.finder.run_search(category=args.category, limit=args.limit)

    adder.interactive_add(results)


if __name__ == '__main__':
    main()
