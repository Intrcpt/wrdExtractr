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

def count_occurrences_in(word_list):

   # word_count as an empty dictionary - a data structure of key/value pairs allowing the lookup of some value given some key.
    word_count = {}
    
    # Goes through each word in all_words and checks if it exists already.
    for word in word_list:
        # Sets the key (word) to a value of 1 if it does not exist.
        if word not in word_count:
            word_count[word] = 1
        # Otherwise (else), we get the current value set for (word) and set the new value of word to the previous value plus one.        
        else:
            current_count = word_count.get(word)
            word_count[word] = current_count + 1
    return word_count  

def get_all_words_from(url):
    html = get_html_of(url)
    soup = BeautifulSoup(html, 'html.parser')
    raw_text = soup.get_text()
    #  r'\w+' is telling Python to interpret the \w part of the string as two individual characters and not an escaped w.
    return re.findall(r'\w+', raw_text)

# Sorts list of words into a list
def get_top_words_from(all_words):
    occurrences = count_occurrences_in(all_words)
    return sorted(occurrences.items(), key=lambda item: item[1], reverse=True)

all_words = get_all_words_from(PAGE_URL)
top_words = get_top_words_from(all_words)

# function takes a URL as a parameter and then immediately uses the URL to call another function that gets the list of words needed.
def get_top_words_from(url):
    all_words = get_all_words_from(url)
    occurrences = count_occurrences_in(all_words)
    return sorted(occurrences.items(), key=lambda item: item[1], reverse=True)

# Prints first element of the tuple for each tuple (top_words[i][0])
for i in range(10):
    print(top_words[i][0])
