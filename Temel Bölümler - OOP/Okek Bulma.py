import time
try:
    a = int(input("Bir sayi giriniz: "))
    b = int(input("2. sayiyi giriniz: "))
    x = a
    y = b
    liste = list()
    toplam = 1
    i = 2
    if a >= b:
        while i < (x + 1):
            if a % i == 0 or b % i == 0:
                if a % i == 0 and b % i == 0:
                    liste.append(i)
                    a = a / i
                    b = b / i
                elif a % i == 0:
                    liste.append(i)
                    a = a / i
                else:
                    liste.append(i)
                    b = b / i
            else:
                i = i + 1

    else:
        while i < (y + 1):
            if a % i == 0 or b % i == 0:
                if a % i == 0 and b % i == 0:
                    liste.append(i)
                    a = a / i
                    b = b / i
                elif a % i == 0:
                    liste.append(i)
                    a = a / i
                else:
                    liste.append(i)
                    b = b / i
            else:
                i += 1
    print(liste)
    for i in liste:
        toplam = toplam * i
    print("Ekok: ", toplam)
    time.sleep(2)
except:
    print("Bir hata oluştu...")
    time.sleep(2)