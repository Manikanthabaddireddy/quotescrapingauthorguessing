from scraping_project import *

if __name__ == "__main__":
    num_pages = 10
    scraper = QuoteScraper(num_pages)
    scraper.guess_author()