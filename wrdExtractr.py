import requests
import re
from bs4 import BeautifulSoup

PAGE_URL = 'http://URL'

# fetches the HTML into a function
def get_html_of(url):
    resp = requests.get(url)

    if resp.status_code != 200:
        print(f'HTTP status code of {resp.status_code} returned, but 200 was expected. Exiting...')
        exit(1)

    return resp.content.decode()


html = get_html_of(PAGE_URL)
soup = BeautifulSoup(html, 'html.parser')
raw_text = soup.get_text()
#  r'\w+' is telling Python to interpret the \w part of the string as two individual characters and not an escaped w.
all_words = re.findall(r'\w+', raw_text)
