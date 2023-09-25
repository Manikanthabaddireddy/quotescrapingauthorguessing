### Project
Web scraping and author guessing !

## description
* Need to scrap data of author like author name, quote, link and date of birth and location.
* And store that data into list.
* Then display random quote and ask the player to guess the name of author who written this quote. If the author name is correct then display message like you guessed it right! else give another three chances if he not done by first attempt for second attempt give hint links date of birth and location of author if then also didnt guess it right give one more hint like First letter of the author.After complete all the four attempts ask him do you want to continue if yes continue game else quit.

## dependencies
requests
bs4

## class QuoteScraper
* In this class created  class variable for base url and constructor for variables intialization.
* With thin the class created two three methods.
  ## scrape_quotes method
        * By using this method, you can extract quotes,author name,link for bio.
        * And that extracted data stored in a list of dictionaries.
        * Used author info method as recursive method for extracting date of birth and location.
        * Aften returned that list for future use.
  ## scrape_author_info method
        * With this method extrcted date of birth and location of the author.
        * used in scrape_quote method.
  ## guess_author method
        * This method is for guessing the author name.
        * Need to give four chances for every player after first attempt give hint like date of birth and location of the author. For second attempt give hint like first letter of the author and so forth.
        * Aften completion of all the attempts if the player not guessed correctly or correct ask him like you want to play again if he say yes continue else quit.