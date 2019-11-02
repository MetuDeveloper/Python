import requests
from bs4 import BeautifulSoup

url = "https://www.imdb.com/chart/top"
response = requests.get(url)
html_icerigi = response.content
soup = BeautifulSoup(html_icerigi,"html.parser")
a = float(input("Rating'i giriniz: "))

basliklar = soup.find_all("td",{"class":"titleColumn"})
ratingler = soup.find_all("td",{"class":"ratingColumn imdbRating"})
for baslik,rating in zip(basliklar,ratingler):
    baslik = baslik.text
    rating = rating.text
    baslik = baslik.strip()
    rating = rating.strip()
    baslik = baslik.replace("\n","")
    rating = rating.replace("\n","")
    if float(rating) > a:
        print("Filmin ismi: {} Filmin Ratingi: {}".format(baslik,rating))