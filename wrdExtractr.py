import requests

PAGE_URL = 'http://URL'

resp = requests.get(PAGE_URL)

if resp.status_code != 200:
    print(f'HTTP status code of {resp.status_code} returned, but 200 was expected. Exiting...')
    exit(1)

html_str = resp.content.decode()
print(html_str)

