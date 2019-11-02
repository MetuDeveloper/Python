def text_oluştur():
    with open("C:/Users/OKAN/Desktop/Mailler.txt","w") as file:
        file.write("coskun.m.murat@gmail.com\n"
                   "example@xyz.com\n"
                    "mustafa.com\n"
                    "mustafa@gmail\n"
                    "kerim@yahoo.com")

def mail_kontrol():
    with open("C:/Users/OKAN/Desktop/Mailler.txt", "r+") as dosya:
        liste1 = dosya.readlines()
        liste2 = list()
        for i in liste1:
            i = i.strip("\n")
            liste2.append(i)
        print("Tüm mail adresleri: ",liste2)
        for i in liste2:
            if i.count(".") == 1:
                pass
            else:
                liste2.remove(i)
        for i in liste2:
            if i.endswith(".com"):
                pass
            else:
                liste2.remove(i)
        for i in liste2:
            if i.count("@") == 1:
                pass
            else:
                liste2.remove(i)
        print("***********************************************************************************************************************")
        print("Doğru formattaki mail adresleri: ",liste2)
text_oluştur()
mail_kontrol()