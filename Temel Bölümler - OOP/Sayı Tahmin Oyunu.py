import random
sonuc = random.randint(1,100)

def tahmin():
    a = float(input("düş biraz: "))
    return a

def tahmin2():
    c = float(input("Çık: "))
    return c


a = float(input("1-100 arasında rastgele bir sayı giriniz:"))

if a >= 100:
    print("100'den büyük bir sayı girdiniz.")
elif a <= 0:
    print("1'den küçük bir sayı girdiniz.")
else:
    while True:
        if a == sonuc:
            print("Tam isabet")
            break
        elif a<sonuc:
            c = tahmin2()
            if c < a:
                print("çık !!!")
                break
            else:
                a = c
        else:
            b = tahmin()
            if b > a :
                print("düş !!!")
                break
            else:
                a = b