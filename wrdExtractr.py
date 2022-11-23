import requests

PAGE_URL = 'http://URL'

# fetches the HTML into a function
def get_html_of(url):
    resp = requests.get(url)

    if resp.status_code != 200:
        print(f'HTTP status code of {resp.status_code} returned, but 200 was expected. Exiting...')
        exit(1)

    return resp.content.decode()

# print the result of this function call  
print(get_html_of(PAGE_URL))
