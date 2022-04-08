# WEB SCRAPING PROJECT ON MOST IN-DEMAND JOB SKILLS

# Loading the web page and storing the html code in a variable
from urllib.request import urlopen

url = "http://olympus.realpython.org/profiles/dionysus"
page = urlopen(url)
page = page.read()
page = page.decode("utf-8")
print(page)

print("Page is loaded in the code.\n")

# Extracting data from the html webpage
# Print the title of the page.
import re

string1 = re.search("<title.*?>.*?</title.*?>", page, re.IGNORECASE)
string2 = string1.group()
string2 = re.sub("<.*?>", "", string2)
print(string2)