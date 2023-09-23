from bs4 import BeautifulSoup
import requests
import random

class QuoteScraper:
    BASE_URL = "http://quotes.toscrape.com/page/"

    def __init__(self, num_pages):
        self.num_pages = num_pages

    def scrape_quotes(self):
        global all_quotes
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

                    # Extract the author's information
                    author_info = self.scrape_author_info(author_link)

                    quotes_data = {
                        'quote': quote,
                        'author': author,
                        'author_link': 'http://quotes.toscrape.com' + author_link,
                        'birth_date': author_info['birth_date'],
                        'birth_location': author_info['birth_location']
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

            # Extract birth date and location
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
        if quotes:
            random_quote = random.choice(quotes)
            print("Randomly selected quote:")
            print(f"Quote Text: {random_quote['quote']}")
            print(f"author: {random_quote['author']}")
            N=0
            while True:
                while N<4:
                    author=input("Enter guessed author [note : use only lower case]: ")
                    if author ==random_quote["author"].lower():
                        print("you guessed right")
                        break
                    else:
                        if N==0:
                            print("HINT: author Date of birth is: ",random_quote["birth_date"] ,'and',"location is:", random_quote["birth_location"])
                            remaing=4-(N+1)
                            print(f"You have only {remaing} guesse left ")
                        else:
                            print("HINT: author first letter is: ",random_quote["author"][0])
                            remaing=4-(N+1)
                            print(f"You have only {remaing} guesse left ")
                            
                    N+=1
                player=input("if you want to continue say yes or no:")
                if player!="yes":
                    print("you lost the game")
                
            
                

            
        else:
            print("No quotes to guess from.")



