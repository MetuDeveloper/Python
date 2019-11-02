class futbolcu():
    def __init__(self,isim,mevki,yaşı,takımı):
        self.isim = isim
        self.mevki = mevki
        self.yaşı = yaşı
        self.takımı = takımı

    def bilgiler(self):
        print("""
Adı :{}
Mevki :{}
Yaşı : {}
Takımı : {}""".format(self.isim,self.mevki,self.yaşı,self.takımı))


deniz_türüç = futbolcu("Deniz Türüç","Sağ Açık",26,"Fenerbahçe")
deniz_türüç.bilgiler()
vedat_muriqi  = futbolcu("Vedat Muriqi","Santrafor",25,"Fenerbahçe")
arda_turan = futbolcu("Arda Turan","10 numara",30,"Başakşehir")
arda_turan.bilgiler()
vedat_muriqi.bilgiler()