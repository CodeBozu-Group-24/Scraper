"""
Dependencies:
requests
bs4 (BeautifulSoup4)
Install with pip
"""

import requests 
from bs4 import BeautifulSoup 

link = "https://example.com"
page = requests.get(link)

print(page)

soup = BeautifulSoup(page.content)

print(soup)