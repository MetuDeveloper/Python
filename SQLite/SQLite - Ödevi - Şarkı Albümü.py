"""Modül"""
import sqlite3
import time

class Şarkı():
    def __init__(self,şarkı_adı,sanatçı,albüm,yapımcı,süresi):
        self.şarkı_adı = şarkı_adı
        self.sanatçı = sanatçı
        self.albüm = albüm
        self.yapımcı = yapımcı
        self.süresi = süresi
    def __str__(self):
        return "Şarkı adı: {}\nSanatçı: {}\nAlbüm: {}\nYapımcı: {}\nSüresi: {}".format(self.şarkı_adı,self.sanatçı,self.albüm,self.yapımcı,self.süresi)

class Tablo():
    def __init__(self):
        self.bağlantı_oluştur()
    def bağlantı_oluştur(self):
        self.bağlantı = sqlite3.connect("kütüphane.db")
        self.cursor = self.bağlantı.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS Müzikler (şarkı_adı TEXT,sanatçı TEXT,albüm TEXT,yapımcı TEXT,süresi INT)")
        self.bağlantı.commit()
    def şarkı_ekle(self,şarkı):
        sorgu = "Insert into Müzikler Values(?,?,?,?,?)"
        self.cursor.execute(sorgu,(şarkı.şarkı_adı,şarkı.sanatçı,şarkı.albüm,şarkı.yapımcı,şarkı.süresi))
        self.bağlantı.commit()
    def şarkı_sil(self,isim):
        sorgu = "Delete From Müzikler where şarkı_adı = ? "
        self.cursor.execute(sorgu,(isim,))
        self.bağlantı.commit()
    def şarkıları_göster(self):
        sorgu = "Select * From Müzikler "
        self.cursor.execute(sorgu)
        hepsi = self.cursor.fetchall()
        if len(hepsi) == 0:
            print("Henüz hiçbir şarkı kaydı bulunmamaktadır...")
        else:
            for i in hepsi:
                türkü = Şarkı(i[0], i[1], i[2], i[3], i[4])
                print(türkü)
                print("***************************")
    def toplam_süre(self):
        sorgu = "Select * From Müzikler "
        self.cursor.execute(sorgu)
        hepsi = self.cursor.fetchall()
        süre = 0
        for i in hepsi:
            şarkı = Şarkı(i[0],i[1],i[2],i[3],i[4])
            süre += float(şarkı.süresi)
        print(round(süre,2))
        time.sleep(2)
    def şarkı_bul(self,isim):
        sorgu = "Select *From Müzikler where şarkı_adı = ?"
        self.cursor.execute(sorgu,(isim,))
        şarkı = self.cursor.fetchall()
        if len(şarkı) ==0:
            print("Şarkı bulunamadı.")
        else:
            şarkılar = Şarkı(şarkı[0][0],şarkı[0][1],şarkı[0][2],şarkı[0][3],şarkı[0][4])
            print(şarkılar)
            
            
****************************************************************************************************************************


""" Uygulama Kısmı"""
from Veri_Tabanı import *
print("""Winamp Programına Hoşgeldiniz
*************************************
1.Şarkıları göster
2.Şarkı ekle
3.Şarkı sil
4.Şarkı bul
5.Şarkıların toplam süresini göster
Çıkış yapmak için "q" tuşuna basınız...
*************************************""")
tablo = Tablo()

while True:
    işlem = input("Yapmak istediğiniz işlemi tuşlayınız: ")
    if işlem == "q":
        print("Program sonlandırılıyor...")
        time.sleep(2)
        print("Yine bekleriz...")
        break
    elif işlem == "1":
        tablo.şarkıları_göster()
        time.sleep(2)
    elif işlem == "2":
        isim = input("Eklemek istediğiniz şarkının adı: ")
        sanatçı = input("Sanatçı: ")
        albüm = input("Albümü: ")
        yapımcı = input("Yapımcısı: ")
        süresi = float(input("Süresi: "))
        şarkı = Şarkı(isim,sanatçı,albüm,yapımcı,süresi)
        tablo.şarkı_ekle(şarkı)
        print("Şarkı ekleniyor...")
        time.sleep(2)
        print("Eklendi.")
    elif işlem == "3":
        isim = input("Silmek istediğiniz şarkının adı: ")
        tablo.şarkı_sil(isim)
        print("Şarkı siliniyor...")
        time.sleep(2)
        print("Silindi.")
    elif işlem == "4":
        isim = input("Bulmak istediğiniz şarkının adı: ")
        tablo.şarkı_bul(isim)
    elif işlem == "5":
        tablo.toplam_süre()
    else:
        print("Yanlış bir işlem yaptınız...")
        time.sleep(1.5)