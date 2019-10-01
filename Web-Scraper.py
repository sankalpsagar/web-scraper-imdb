#url = https://www.imdb.com/movies-in-theaters/
import requests
import urllib.request
from bs4 import BeautifulSoup

url = 'https://www.imdb.com/movies-in-theaters/'
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")
text = soup.body.contents[5].find_all('h4')

for stuff in text:
	print (stuff.string)