from Veri_Tabanı import *
print("""***************************************

1.Kitapları Göster

2.Kitap Sorgulama

3.Kitap Ekle

4.Kitap Sil

5.Baskı Yükselt

6.Baskı Sayısını Göster

Çıkmak için q'ya basınız.
***************************************""")
kütüphane = Kütüphane()
while True:
    işlem = input("Yapacağınız işlemi giriniz: ")
    if işlem == "q":
        print("Program Sonlandırılıyor...")
        break
    elif işlem == "1":
        kütüphane.kitapları_göster()
    elif işlem == "2":
        isim = input("Aradığınız kitabın ismini giriniz: ")
        print("Kitap aranıyor...")
        time.sleep(2)
        kütüphane.kitap_sorgula(isim)
    elif işlem == "3":
        isim = input("İsim: ")
        yazar = input("Yazar: ")
        yayınevi = input("Yayınevi: ")
        tür = input("Tür: ")
        baskı = int(input("Baskı Sayısı: "))
        yeni_kitap = Kitap(isim,yazar,yayınevi,tür,baskı)
        print("Kitap ekleniyor...")
        time.sleep(2)
        kütüphane.kitap_ekle(yeni_kitap)
        print("Eklendi.")
    elif işlem == "4":
        isim = input("Silmek istenilen kitabın adı: ")
        cevap = input("Emin misiniz E/H ?")
        if cevap == "E":
            silinecek_kitap = kütüphane.kitap_sil(isim)
            print("Kitap siliniyor...")
            time.sleep(2)
            print("Silindi.")
    elif işlem == "5":
        isim = input("Baskı yükselticek kitabın ismi: ")
        kütüphane.baskı_yükselt(isim)
        time.sleep(2)
        print("İşleminiz gerçekleştirildi.")
    elif işlem == "6":
        isim = input("Baskı sayısı sorulan kitap ismi: ")
        kütüphane.baskı_sayısını_göster(isim)
        time.sleep(2)
        print("İşlem tamamlandı.")
    else:
        print("Yanlış bir tuşlama yaptınız...")