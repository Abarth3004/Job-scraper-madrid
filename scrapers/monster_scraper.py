import requests
from bs4 import BeautifulSoup
from filters import is_valid_job

def scrape_monster():
    jobs = []
    for page in range(1, 6):
        url = f"https://www.monster.es/empleos/buscar/?q=marketing&where=Madrid&page={page}"
        headers = {"User-Agent": "Mozilla/5.0"}
        resp = requests.get(url, headers=headers)
        if resp.status_code != 200:
            break
        soup = BeautifulSoup(resp.text, "html.parser")
        cards = soup.select("section.card-content")
        if not cards:
            break
        for card in cards:
            title = card.find("h2").get_text(strip=True)
            company = card.select_one(".company").get_text(strip=True) if card.select_one(".company") else ""
            summary = card.select_one(".summary").get_text(strip=True) if card.select_one(".summary") else ""
            url = card.find("a", href=True)["href"]
            combined = f"{title} {summary}"
            if is_valid_job(combined):
                jobs.append({
                    "source": "Monster",
                    "title": title,
                    "company": company,
                    "location": "Madrid",
                    "summary": summary,
                    "url": url
                })
    return jobs