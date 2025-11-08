"""
Gemeinsame Klassen und Utilities für Awesome Finder Tools
"""

import re
from dataclasses import dataclass
from typing import Set


@dataclass
class SearchResult:
    """Repräsentiert ein Suchergebnis"""
    title: str
    url: str
    content: str
    score: float
    engine: str
    category: str = ""


class URLManager:
    """Verwaltet URLs aus README.md"""

    def __init__(self, readme_path: str = "README.md"):
        self.readme_path = readme_path
        self.existing_urls: Set[str] = set()
        self.readme_content: str = ""

    def load_existing_urls(self) -> int:
        """Lädt bestehende URLs aus README.md"""
        try:
            with open(self.readme_path, 'r', encoding='utf-8') as f:
                self.readme_content = f.read()

            # Extrahiere alle URLs aus Markdown-Links
            url_pattern = r'\[([^\]]+)\]\(([^\)]+)\)'
            matches = re.findall(url_pattern, self.readme_content)

            for title, url in matches:
                # Normalisiere URLs (entferne trailing slashes, etc.)
                normalized_url = self.normalize_url(url)
                self.existing_urls.add(normalized_url)

            return len(self.existing_urls)
        except FileNotFoundError:
            return 0

    @staticmethod
    def normalize_url(url: str) -> str:
        """Normalisiert URLs für Vergleiche"""
        # Entferne trailing slash
        url = url.rstrip('/')
        # Entferne http/https Unterschiede
        url = url.replace('https://', '').replace('http://', '')
        # Entferne www
        url = url.replace('www.', '')
        return url.lower()

    def is_duplicate(self, url: str) -> bool:
        """Prüft ob URL bereits existiert"""
        normalized = self.normalize_url(url)
        return normalized in self.existing_urls
