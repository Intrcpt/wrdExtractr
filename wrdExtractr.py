import requests

PAGE_URL = 'http://URL'

resp = requests.get(PAGE_URL)
html_str = resp.content.decode()
print(html_str)

