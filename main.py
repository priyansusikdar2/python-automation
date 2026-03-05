from database import create_db
import scraper

def main():

    print("Creating Database...")
    create_db()

    print("Starting Scraper...")
    scraper.run_scraper()

    print("Scraping Completed")

if __name__ == "__main__":
    main()