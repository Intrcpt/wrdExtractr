import click
import requests
import re
from bs4 import BeautifulSoup

# fetches the HTML into a function and does a simple fail check for broken links
def get_html_of(url):
    resp = requests.get(url)

    if resp.status_code != 200:
        print(f'HTTP status code of {resp.status_code} returned, but 200 was expected. Exiting...')
        exit(1)

    return resp.content.decode()

def count_occurrences_in(word_list, min_length):

   # word_count as an empty dictionary - a data structure of key/value pairs allowing the lookup of some value given some key.
    word_count = {}
    
    # Goes through each word in all_words and checks if it exists already.
    for word in word_list:
        if len(word) < min_length:
            continue
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
def get_top_words_from(all_words, min_length):
    occurrences = count_occurrences_in(all_words, min_length)
    return sorted(occurrences.items(), key=lambda item: item[1], reverse=True)

@click.command()
@click.option('--url', '-u', prompt='Web URL', help='URL of webpage to extract from.')
@click.option('--length', '-l', default=0, help='Minimum word length (default: 0, no limit).')
def main(url, length):
    the_words = get_all_words_from(url)
    top_words = get_top_words_from(the_words, length)

    for i in range(10):
        print(top_words[i][0])

if __name__ == '__main__':
    main()
    
