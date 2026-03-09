
import requests
from bs4 import BeautifulSoup

from src.search_engine import google_search, google_company_description


def clean_company_name(title):

    if not title:
        return "Unknown"

    separators = ["|", "-", "–", ":"]

    for sep in separators:
        if sep in title:
            return title.split(sep)[0].strip()

    return title.strip()


def fetch_with_requests(domain):
    """
    Try scraping website directly
    """

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    urls = [
        f"https://{domain}",
        f"http://{domain}",
        f"https://www.{domain}",
        f"http://www.{domain}",
    ]

    for url in urls:
        try:
            r = requests.get(url, headers=headers, timeout=6)

            if r.status_code == 200:
                soup = BeautifulSoup(r.text, "html.parser")

                title = soup.title.string.strip() if soup.title else None

                title = clean_company_name(title)

                text = soup.get_text(" ", strip=True)

                return title, text

        except Exception:
            continue

    return None, None


def fetch_from_google(domain):
    """
    Use Google search to find company website
    """

    try:

        url = google_search(domain)

        if not url:
            return None, None

        r = requests.get(url, timeout=8)

        soup = BeautifulSoup(r.text, "html.parser")

        title = soup.title.string.strip() if soup.title else None

        title = clean_company_name(title)

        text = soup.get_text(" ", strip=True)

        return title, text

    except Exception:
        return None, None


def fetch_website_data(domain):
    """
    Main scraping pipeline
    """

    #  direct website scraping
    title, text = fetch_with_requests(domain)

    if title:
        return title, text

    print("Direct website blocked → trying Google search...")

    #  Google search result
    title, text = fetch_from_google(domain)

    if title:
        return title, text

    print("Google site fetch failed → using Google snippet description...")

    #  Google snippet fallback
    snippet = google_company_description(domain)

    if snippet:
        title = domain.split(".")[0].capitalize()
        return title, snippet

    return None, None