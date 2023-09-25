import requests
import random
from bs4 import BeautifulSoup

class QuoteScraper:
    BASE_URL = "http://quotes.toscrape.com/page/"

    def __init__(self, num_pages):
        self.num_pages = num_pages

    def scrape_quotes(self):
        all_quotes = []
        for page_number in range(1, self.num_pages + 1):
            url = f"{self.BASE_URL}{page_number}/"
            response = requests.get(url)

            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                quote_elements = soup.find_all('div', class_='quote')

                for quote_element in quote_elements:
                    quote = quote_element.find('span', class_='text').get_text()
                    author = quote_element.find('small', class_='author').get_text()
                    author_link = quote_element.find('a', href=True)['href']

                    author_info = self.scrape_author_info(author_link)

                    quotes_data = {
                        'quote': quote,
                        'author': author,
                        'author_link': f"http://quotes.toscrape.com{author_link}",
                        'birth_date': author_info.get('birth_date'),
                        'birth_location': author_info.get('birth_location')
                    }

                    all_quotes.append(quotes_data)
            else:
                print(f"Failed to retrieve data for page {page_number}. Status code: {response.status_code}")
        return all_quotes

    def scrape_author_info(self, author_link):
        url = f"http://quotes.toscrape.com{author_link}"
        author_info = {}

        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')

            birth_date = soup.find('span', class_='author-born-date').get_text()
            birth_location = soup.find('span', class_='author-born-location').get_text()

            author_info = {
                'birth_date': birth_date,
                'birth_location': birth_location
            }
        else:
            print(f"Failed to retrieve author information. Status code: {response.status_code}")
        
        return author_info

    def guess_author(self):
        quotes = self.scrape_quotes()
        if not quotes:
            print("No quotes to guess from.")
            return

        for i in range(4):
            random_quote = random.choice(quotes)
            print("Randomly selected quote:")
            print(f"Quote Text: {random_quote['quote']}")
            print(f"Author: {random_quote['author']}")

            remaining_attempts = 4
            while remaining_attempts > 0:
                guessed_author = input("Enter guessed author (use only lowercase): ")
                if guessed_author == random_quote["author"].lower():
                    print("You guessed right!")
                    break
                else:
                    remaining_attempts -= 1
                    if remaining_attempts == 3:
                        print(f"HINT: Author's date of birth is {random_quote['birth_date']} and location is {random_quote['birth_location']}.")
                    elif remaining_attempts > 0:
                        print(f"HINT: Author's first letter is {random_quote['author'][0]}.")
                        print(f"You have {remaining_attempts} guess(es) left.")
            
            if remaining_attempts == 0:
                print(f"You ran out of guesses. The correct author was: {random_quote['author']}")

            continue_game = input("Do you want to continue? (yes/no): ")
            if continue_game.lower() != "yes":
                print("Thanks for playing!")
                break


