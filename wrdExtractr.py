import requests
import re
from bs4 import BeautifulSoup

PAGE_URL = 'http://URL'

# fetches the HTML into a function and does a simple fail check for broken links
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

# word_count as an empty dictionary - a data structure of key/value pairs allowing the lookup of some value given some key.
word_count = {}

# Goes through each word in all_words and checks if it exists already.
for word in all_words:
# Sets the key (word) to a value of 1 if it does not exist.
    if word not in word_count:
        word_count[word] = 1
        
# Otherwise (else), we get the current value set for (word) and set the new value of word to the previous value plus one.        
    else:
        current_count = word_count.get(word)
        word_count[word] = current_count + 1
