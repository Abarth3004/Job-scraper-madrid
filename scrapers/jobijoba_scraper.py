import requests
from bs4 import BeautifulSoup
from filters import is_valid_job

def scrape_jobijoba():
    jobs = []
    for page in range(1, 6):
        url = f"https://www.jobijoba.com/emplois/marketing+Madrid-{page}"
        headers = {"User-Agent": "Mozilla/5.0"}
        resp = requests.get(url, headers=headers)
        if resp.status_code != 200:
            break
        soup = BeautifulSoup(resp.text, "html.parser")
        cards = soup.select(".JobCardItem")
        if not cards:
            break
        for card in cards:
            title = card.select_one(".JobCardItem-title").get_text(strip=True)
            company = card.select_one(".JobCardItem-company").get_text(strip=True)
            summary = card.select_one(".JobCardItem-snippet").get_text(strip=True)
            url = card.find("a", href=True)["href"]
            combined = f"{title} {summary}"
            if is_valid_job(combined):
                jobs.append({
                    "source": "Jobijoba",
                    "title": title,
                    "company": company,
                    "location": "Madrid",
                    "summary": summary,
                    "url": url
                })
    return jobs