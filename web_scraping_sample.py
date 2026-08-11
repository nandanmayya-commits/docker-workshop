import requests
from bs4 import BeautifulSoup

url = "https://example.com"

response = requests.get(url)

print("Status Code:", response.status_code)

soup = BeautifulSoup(response.text, "html5lib")

print("Page Title:", soup.title.text)
