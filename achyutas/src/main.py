from scraping_project import *

if __name__ == "__main__":
    num_pages = 10  # Specify the number of pages you want to scrape
    quote_scraper = QuoteScraper(num_pages)
    quote_scraper.scrape_quotes()
    quote_scraper.guess_author()