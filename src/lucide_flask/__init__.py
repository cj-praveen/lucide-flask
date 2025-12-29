import httpx
from typing import Set
from minify_html import minify as minify_html
from markupsafe import Markup
from pathlib import Path

class IconNotFoundError(Exception):
    pass

class Lucide:
    def __init__(self):
        self.cache_dir = Path(".lucide")
        self.cache_dir.mkdir(exist_ok=True)
        self.tags: Set[str] = self.fetch_tags()

    def fetch_tags(self) -> Set[str]:
        url: str = "https://unpkg.com/lucide-static@latest/tags.json"
        try:
            response = httpx.get(url, follow_redirects=True)
            response.raise_for_status()
            tags = response.json()
            return set(tags.keys())
        except httpx.RequestError as err:
            raise RuntimeError("Network error while fetching Lucide data")

    def __contains__(self, key: str) -> bool:
        return key in self.tags

    def __getitem__(self, key: str) -> Markup:
        url: str = f"https://unpkg.com/lucide-static@latest/icons/{key}.svg"

        path = self.cache_dir / f"{key}.svg"

        if path.exists():
            content: str = path.read_text(encoding="utf-8")
            return Markup(content)
        
        if key not in self.tags:
            raise IconNotFoundError(f"Icon '{key}' not found.")

        try:
            response = httpx.get(url, follow_redirects=True)
            response.raise_for_status()
            content: str = minify_html(response.text)
            self.cache(key, content)
            return Markup(content)
        except httpx.RequestError as err:
            raise RuntimeError(f"Failed to fetch icon '{key}'") from err

    def cache(self, icon: str , content: str) -> None:
        self.cache_dir.joinpath(f"{icon}.svg").write_text(content, encoding="utf-8")
