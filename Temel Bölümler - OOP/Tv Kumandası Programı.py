import random
import time
"""
********************************************
Tv Kumandası Programı:

1. Aç
2. Kapat
3. Ses artır
4. Ses azalt
5. Kanal ekle
6. Toplam kanal sayısı
7. Rastgele kanal seç
8. Info
********************************************
"""

class Kumanda():
    def __init__(self,durum = "Kapalı",ses = 0,kanal_listesi = ["Trt"],secili_kanal = "Trt"):
        self.durum = durum
        self.ses = ses
        self.kanal_listesi = kanal_listesi
        self.secili_kanal = secili_kanal

    def tv_ac(self):
        if self.durum == "Açık":
            print("Tv zaten açık...")
        else:
            self.durum = "Açık"
            print("Tv açılıyor...")
            time.sleep(1.5)
            print("Açıldı.")

    def tv_kapat(self):
        if self.durum == "Kapalı":
            print("Tv zaten kapalı...")
        else:
            self.durum = "Kapalı"
            print("Tv kapanıyor...")
            time.sleep(1.5)
            print("Kapandı.")

    def ses_artır(self):
        if self.ses <32:
            self.ses += 1
            print("Ses Seviyesi = ",self.ses)
        else:
            print("Ses = 32 (maks.)")


    def ses_azalt(self):
        if self.ses > 0:
            self.ses -= 1
            print("Ses seviyesi = ",self.ses)
        else:
            print("Ses seviyesi = 0")

    def kanal_ekle(self,yeni_kanal):
        self.kanal_listesi.append(yeni_kanal)
        print(self.kanal_listesi)

    def __len__(self):
        print("Toplam Kanal Sayısı = ",len(self.kanal_listesi))

    def rastgele_kanal_sec(self):
        self.secili_kanal = self.kanal_listesi[random.randint(0,len(self.kanal_listesi)-1)]
        print(self.secili_kanal)

    def televizyon_bilgileri(self):
        print("********************************************\nTV BİLGİLERİ:\nTv durumu: {}\nSes seviyesi: {}\nKanal Listesi: {}\nSecili Kanal: {}\n********************************************".format(self.durum,self.ses,self.kanal_listesi,self.secili_kanal))

print(""""********************************************
Tv Kumandası Programı:

1. Aç
2. Kapat
3. Ses artır
4. Ses azalt
5. Kanal ekle
6. Toplam kanal sayısı
7. Rastgele kanal seç
8. Info
********************************************""")
vestel_kumanda = Kumanda()
print("(Eğer çıkış yapmak istiyorsanız q tuşuna basınız.)")


try:
    def kod():
        while True:
            basilan_tus = input("1 den 8 e kadar bir komut giriniz: ")
            if basilan_tus == "q":
                print("Kumanda'dan çıkılıyor...")
                time.sleep(1.5)
                print("Kumanda kapatıldı.")
                break

            if int(basilan_tus) == 1:
                vestel_kumanda.tv_ac()
            elif int(basilan_tus) == 2:
                vestel_kumanda.tv_kapat()
            elif int(basilan_tus) == 3:
                vestel_kumanda.ses_artır()
            elif int(basilan_tus) == 4:
                vestel_kumanda.ses_azalt()
            elif int(basilan_tus) == 5:
                a = input("Bir kanal ismi giriniz: ")
                vestel_kumanda.kanal_ekle(a)
            elif int(basilan_tus) == 6:
                vestel_kumanda.__len__()
            elif int(basilan_tus) == 7:
                vestel_kumanda.rastgele_kanal_sec()
            elif int(basilan_tus) == 8:
                vestel_kumanda.televizyon_bilgileri()
            else:
                print("Yanlış bir tuşa bastınız.")
    kod()
except:
    print("Bir hata oluştu.")
finally:
    kod()