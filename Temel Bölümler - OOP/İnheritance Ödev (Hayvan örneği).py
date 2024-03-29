class Hayvan():
    def __init__(self,tür="bilgi yok",ayak_sayısı="bilgi yok",yeteneği="bilgi yok",sevdiği_yemek = "bilgi yok"):
        self.tür = tür
        self.ayak_sayısı = ayak_sayısı
        self.yeteneği = yeteneği

class At(Hayvan):
    def __init__(self,tür,ayak_sayısı,yeteneği,sevdiği_yemek):
        super(At, self).__init__(tür,ayak_sayısı)
        self.yeteneği = "Hızlı Koşması"
        self.sevdiği_yemek = "Küp şeker"

class Köpek(Hayvan):
    def __init__(self,tür,ayak_sayısı,yeteneği,sevdiği_yemek):
        super(Köpek, self).__init__(tür,ayak_sayısı)
        self.yeteneği = "Kemik Toplamak"
        self.sevdiği_yemek = "Kemik"

class Kuş(Hayvan):
    def __init__(self,tür,ayak_sayısı,yeteneği,sevdiği_yemek):
        super(Kuş, self).__init__(tür)
        self.yeteneği = "Uçmak"
        self.ayak_sayısı = ayak_sayısı
        self.sevdiği_yemek = "Solucan"

hayvan1 = input("bir hayvan ismi giriniz(at/köpek yada kuş): ")
if hayvan1 == "at":
    hayvan1 = At("At",4,"yeteneği",".")
    print("Türü: {}\nAyak sayısı: {}\nYeteneği: {}\nSevdiği Yemek:"
          " {}".format(hayvan1.tür,hayvan1.ayak_sayısı,hayvan1.yeteneği,hayvan1.sevdiği_yemek))

elif hayvan1 == "köpek":
    hayvan1 = Köpek("Köpek",4,".",".")
    print("Türü: {}\nAyak sayısı: {}\nYeteneği: {}\nSevdiği Yemek: "
          "{}".format(hayvan1.tür, hayvan1.ayak_sayısı,hayvan1.yeteneği, hayvan1.sevdiği_yemek))


elif hayvan1 == "kuş":
    hayvan1 = Kuş("Kuş",3,".",5)
    print("Türü: {}\nAyak sayısı: {}\nYeteneği: {}\n"
          "Sevdiği Yemek: {}".format(hayvan1.tür, hayvan1.ayak_sayısı,hayvan1.yeteneği, hayvan1.sevdiği_yemek))

else:
    print("Aradığınız hayvan türü kayıtları kütüphanemizde bulunmamaktadır.")