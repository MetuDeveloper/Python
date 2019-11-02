import math
import time
print(""" *********************************************
Çok fonksiyonlu hesap makinesi programi:

1.Sin
2.Cos
3.Log10()
4.tan
5.toplama
6.çıkarma
7.çarpma
8.bölme
Not: Çıkış yapmak istiyorsanı q'ya basınız.
*********************************************
""")
a = input("Programı başlatmak için bir tuşa basınız: ")
try:
    while True:
        if a != "q":
            a = int(input("1-10 arasi sayi giriniz: "))
            if a == 1:
                print("Sin işlemini seçtiniz.")
                x = int(input("bir derece giriniz: "))
                print(math.sin(math.radians(x)))
                time.sleep(1)
            elif a == 2:
                print("Cos işlemini seçtiniz.")
                x = int(input("bir derece giriniz: "))
                print(math.cos(math.radians(x)))
                time.sleep(1)
            elif a == 3:
                print("log10() işlemini seçtiniz.")
                x = int(input("bir sayi giriniz: "))
                print(math.log10(x))
                time.sleep(1)
            elif a == 4:
                print("tan işlemini seçtiniz.")
                x = int(input("bir derece giriniz: "))
                print(math.tan(math.radians(x)))
                time.sleep(1)
            elif a == 5:
                print("toplama işlemini seçtiniz.")
                x = int(input("bir sayi giriniz: "))
                y = int(input("bir sayi daha giriniz: "))
                print(int(math.fsum([x, y])))
                time.sleep(1)
            elif a == 6:
                print("çıkarma işlemini seçtiniz.")
                x = int(input("bir sayi giriniz: "))
                y = int(input("bir sayi daha giriniz: "))
                print(x - y)
                time.sleep(1)
            elif a == 7:
                print("çarpma işlemini seçtiniz.")
                x = int(input("bir sayi giriniz: "))
                y = int(input("bir sayi daha giriniz: "))
                print(x * y)
                time.sleep(1)
            elif a == 8:
                print("bölme işlemini seçtiniz.")
                x = int(input("bolunen sayiyi giriniz: "))
                y = int(input("bolen sayiyi giriniz: "))
                print(int(x / y))
                time.sleep(1)
            else:
                print("yanlis bir islem yaptınız.")
                time.sleep(1)
        else:
            print("Program Kapatılıyor...")
            time.sleep(1)
            break
except:
    print("Yanlış bir tuşa bastınız...\nProgram Kapatılıyor...")
    time.sleep(1)