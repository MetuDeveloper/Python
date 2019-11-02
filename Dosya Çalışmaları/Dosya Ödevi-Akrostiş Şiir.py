def text_oluştur():
    with open("C:/Users/OKAN/Desktop/Şiir.txt","w") as file:
        file.write("Memlekete sis çökmüş bir gece\n"
                   "Usulca yanağıma sen düşüyorsun\n"
                   "Sabah saat dokuzu beş geçe\n"
                    "Terk edip bizleri gidiyorsun\n"
                    "Ayrılık bu kadar yakmamıştı içimizi\n"
                    "Farkında mısın bilmiyorum\n"
                    "Aldın beraberinde cumhuriyetimizi\n"
                    "Korkunç bir veda, sararmıştı her yer\n"
                    "Ellerini uzat tutmak istiyoruz\n"
                    "Masmavi gözleri kaybetmiş çocuk\n"
                    "Aldı bir sabah ruhumuzu\n"
                    "Lakin nasıl bölmesin yokluğun uykumuzu\n")
def akrostiş_şiir():
    with open("C:/Users/OKAN/Desktop/Şiir.txt","r+") as dosya:
        liste1 = dosya.readlines()
        liste2 = list()
        for i in liste1:
            liste2.append(i[0])
        liste2.pop(0)
        liste2.insert(6," ")
        print(liste2)
        a = "M"
        for i in liste2:
            a += i
        print(a)
text_oluştur()
akrostiş_şiir()