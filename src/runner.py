thonpython
import json
import logging
from pathlib import Path
from extractors.zendesk_parser import ZendeskParser
from outputs.exporters import JsonExporter

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

def load_settings():
    settings_path = Path(__file__).parent / "config" / "settings.example.json"
    with open(settings_path, "r") as f:
        return json.load(f)

def main():
    settings = load_settings()
    base_url = settings.get("base_url")
    locales = settings.get("locales", [])
    max_pages = settings.get("max_pages", 1)
    output_file = settings.get("output_file", "output.json")

    if not base_url:
        logging.error("base_url missing in settings.")
        return

    parser = ZendeskParser(base_url=base_url, max_pages=max_pages)

    results = []
    for locale in locales:
        logging.info(f"Scraping locale: {locale}")
        articles = parser.scrape_locale(locale)
        results.extend(articles)

    JsonExporter.export(results, output_file)
    logging.info(f"Scraping completed. Exported {len(results)} articles to {output_file}")

if __name__ == "__main__":
    main()