Fenerbahçe = list()
Galatasaray = list()
Kayserispor = list()
Tranzonspor = list()
Beşiktaş = list()
Lille = list()

dosya1 = open("C:/Users/OKAN/Desktop/Futbolcular.txt","r+")
geçenler = list()
kalanlar = list()
def ortalama(satır):
    satır = satır[:-1]
    satır = satır.split(", ")
    futbolcu_ismi = satır[0]
    takım_ismi = satır[1]
    if takım_ismi == "Fenerbahçe":
        Fenerbahçe.append(futbolcu_ismi)
    elif takım_ismi == "Galatasaray":
        Galatasaray.append(futbolcu_ismi)
    elif takım_ismi == "Beşiktaş":
        Beşiktaş.append(futbolcu_ismi)
    elif takım_ismi == "Trabzonspor":
        Tranzonspor.append(futbolcu_ismi)
    elif takım_ismi == "Kayserispor":
        Kayserispor.append(futbolcu_ismi)
    elif takım_ismi == "Lille":
        Lille.append(futbolcu_ismi)



with open("C:/Users/OKAN/Desktop/Futbolcular.txt","r+") as dosya:
    liste = dosya.readlines()

    for i in liste:
        ortalama(i)
print("**********************")
print("Fenerbahçeli oyuncular: ")
for i in Fenerbahçe:
    print(i)
print("**********************")
print("Gs'li oyuncular: ")
for i in Galatasaray:
    print(i)
print("**********************")
print("Bjk'li oyuncular: ")
for i in Beşiktaş:
    print(i)
print("**********************")
print("Ts'li oyuncular: ")
for i in Tranzonspor:
    print(i)
print("**********************")
print("Kayserisporlu oyuncular: ")
for i in Kayserispor:
    print(i)
print("**********************")
print("Lille'li oyuncular: ")
for i in Lille:
    print(i)