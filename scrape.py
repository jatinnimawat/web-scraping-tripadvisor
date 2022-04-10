from bs4 import BeautifulSoup as soup

url = "https://bigseventravel.com/50-most-visited-cities-in-the-world/"
page = soup(url, "html.parser")
