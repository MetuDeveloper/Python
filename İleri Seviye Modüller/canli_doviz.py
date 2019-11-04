import requests
from bs4 import BeautifulSoup
url = "https://kur.doviz.com/"
response = requests.get(url)
html_icerigi = response.content
soup = BeautifulSoup(html_icerigi,"html.parser")
liste = list()
for i in soup.find_all("span"):
    a = i.text.replace(",",".")
    try:
        b = float(a)
        liste.append(b)
    except: 
        pass

def gram_altın(miktar):
    print(round((liste[0]*miktar),2),"tl")

def dolar(miktar):
    print(round((liste[1]*miktar),2),"tl")

def euro(miktar):
    print(round((liste[2]*miktar),2),"tl")

def euro_dolar(miktar):
    print(round((liste[5]*miktar),2),"dolar")

print("""Döviz hesaplama programına hoşgeldiniz:
işlem numaraları:
1) Tl 'den Gram altın hesaplama
2)Tl >> dolar hesaplama
3)Tl >> euro hesaplama
4)Euro >> dolar hesaplama
""")
try:
    q = int(input("Yapmak istediğiniz işlemin numarasını giriniz: "))
    if q == 1:
        w = float(input("Miktarı giriniz: "))
        gram_altın(w)
    elif q == 2:
        w = float(input("Miktarı giriniz: "))
        dolar(w)
    elif q == 3:
        w = float(input("Miktarı giriniz: "))
        euro(w)
    elif q == 4:
        w = float(input("Miktarı giriniz: "))
        euro_dolar(w)
    else:
        print("Hatalı bir işlem yaptınız...")
       
except:
    print("Hatalı bir işlem yaptınız...")