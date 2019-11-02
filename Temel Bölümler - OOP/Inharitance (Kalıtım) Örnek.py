class Çalışan():
    def __init__(self,isim,maaş):

        self.isim= isim
        self.maaş = maaş

    def departman_degistir(self,yeni_departman):
        self.departman = yeni_departman

    def maaş_zammı(self,zam):
        self.maaş += zam

    def bilgileri_göster(self):
        print("""Personal Bilgileri...\nİsim: {}\nMaaş: {}\n************************ """.format(self.isim,self.maaş))

class Yönetici(Çalışan):
    def __init__(self,isim,maaş,departman):
        super().__init__(isim,maaş)
        self.departman = departman
    def bilgileri_göster(self):
        print("""Personal Bilgileri...\nİsim: {}\nMaaş: {}\nPozisyon: {}\n************************ """.format(self.isim, self.maaş,self.departman))


müdür = Yönetici("Osman",7000,"proje müdürü")
müdür.bilgileri_göster()
işçi = Çalışan("okan",3000)
işçi.bilgileri_göster()