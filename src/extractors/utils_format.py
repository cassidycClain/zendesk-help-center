thonpython
import re

def clean_text(text: str) -> str:
    if not text:
        return ""
    return " ".join(text.split()).strip()

def extract_article_id(url: str) -> str:
    match = re.search(r"/articles/(\d+)", url)
    return match.group(1) if match else ""