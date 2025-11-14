thonpython
import logging
import re
import requests
from bs4 import BeautifulSoup
from .utils_format import clean_text, extract_article_id

class ZendeskParser:
    def __init__(self, base_url: str, max_pages: int = 1):
        self.base_url = base_url.rstrip("/")
        self.max_pages = max_pages
        self.session = requests.Session()
        self.session.headers.update({
            "User-Agent": "Mozilla/5.0 (compatible; ZendeskScraper/1.0)"
        })

    def build_page_url(self, locale: str, page: int):
        return f"{self.base_url}/hc/{locale}?page={page}"

    def scrape_locale(self, locale: str):
        articles = []

        for page in range(1, self.max_pages + 1):
            url = self.build_page_url(locale, page)
            logging.info(f"Requesting: {url}")

            try:
                response = self.session.get(url, timeout=10)
                response.raise_for_status()
            except Exception as e:
                logging.error(f"Request failed: {e}")
                continue

            soup = BeautifulSoup(response.text, "html.parser")
            links = soup.select("a.article-list-link, a[href*='articles/']")

            if not links:
                logging.info("No more articles found.")
                break

            for link in links:
                href = link.get("href")
                title = clean_text(link.get_text())
                if not href:
                    continue

                if href.startswith("/"):
                    href = f"{self.base_url}{href}"

                article_id = extract_article_id(href)

                articles.append({
                    "url": href,
                    "title": title,
                    "locale": locale,
                    "article_id": article_id,
                })

        return articles