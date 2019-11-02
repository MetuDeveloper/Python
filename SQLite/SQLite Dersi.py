import sqlite3
con = sqlite3.connect("kütüphane.db")
cursor = con.cursor()

def tablo_olustur():
    con.execute("CREATE TABLE IF NOT EXISTS kitaplık (isim TEXT,yazar TEXT,konusu TEXT,sayfa_sayısı INT)")
    con.commit()
def veri_ekle():
    con.execute("insert into kitaplık Values('Okan','Kandemir','Python Dersleri',145)")
    con.commit()
def veri_ekle2():
    isim = input("isim giriniz: ")
    yazar = input("yazar ismi: ")
    konusu = input("kitabın konusu: ")
    sayfa_sayısı = input("sayfa sayısı: ")
    cursor.execute("insert into kitaplık Values(?,?,?,?)",(isim,yazar,konusu,sayfa_sayısı))
    con.commit()
def veri_cekme1():
    cursor.execute("Select*From kitaplık")
    liste = cursor.fetchall()
    for i in liste:
        print(i)
def veri_cekme2():
    cursor.execute("Select isim,konusu From kitaplık")
    liste = cursor.fetchall()
    for i in liste:
        print(i)
def veri_cekme3(isim):
    cursor.execute("Select*From kitaplık where isim = ?",(isim,))
    liste = cursor.fetchall()
    print(liste)
def verileri_güncelle(eskiveri,yeniveri):
    cursor.execute("Update kitaplık set isim = ? where isim = ?",(yeniveri,eskiveri))
    con.commit()

def veri_silme(isim):
    cursor.execute("Delete from kitaplık where isim = ?",(isim,))
    con.commit()

veri_silme("Nuri")
veri_cekme1()

con.close()