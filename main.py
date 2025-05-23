from scrapers.monster_scraper import scrape_monster
from scrapers.jobijoba_scraper import scrape_jobijoba
from export_excel import export_jobs_to_excel

def main():
    all_jobs = []
    all_jobs += scrape_monster()
    all_jobs += scrape_jobijoba()
    export_jobs_to_excel(all_jobs)

if __name__ == "__main__":
    main()