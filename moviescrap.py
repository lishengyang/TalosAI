import requests
from bs4 import BeautifulSoup

url = 'https://www.imdb.com/chart/top/?ref_=nv_mv_250'
response = requests.get(url)

soup = BeautifulSoup(response.content, 'lxml')

movie_titles = []
movie_cells = soup.find_all('td', class_='titleColumn')
for cell in movie_cells:
    title = cell.find('a').text
    movie_titles.append(title)

for title in movie_titles:
    print(title)

