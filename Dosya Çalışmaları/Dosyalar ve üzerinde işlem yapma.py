dosya1 = open("C:/Users/OKAN/Desktop/como_lok1.txt","w")
geçenler = list()
kalanlar = list()
def ortalama(satır):
    satır = satır[:-1]
    satır = satır.split(" ")
    isim1 = satır[0]
    not1 = satır[1]
    not2 = satır[2]
    not3 = satır[3]
    aritmatik_ortalama = int(int(not1)*0.3+int(not2)*0.3+int(not3)*0.4)
    print("{} >>>>>>>>>>>>>>>> {}".format(isim1,aritmatik_ortalama))
    dosya1.write("{} >>>>>>>>>>>>>>>> {}\n".format(isim1,aritmatik_ortalama))
    if aritmatik_ortalama>60:
        geçenler.append(isim1)
    else:
        kalanlar.append(isim1)


with open("C:/Users/OKAN/Desktop/como_lok.txt","r+") as dosya:
    liste = dosya.readlines()
    for i in liste:
        ortalama(i)

print("Geçenler= ",geçenler)
print("Kalanlar= ",kalanlar)