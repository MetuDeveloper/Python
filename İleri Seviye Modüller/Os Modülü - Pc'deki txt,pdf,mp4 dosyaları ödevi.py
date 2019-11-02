import os
liste_txt = list()
liste_pdf = list()
liste_mp4 = list()
dosya_pdf = open("C:/Users/OKAN/Desktop/Pdf_dosyaları.txt","w")
dosya_txt = open("C:/Users/OKAN/Desktop/Txt_dosyaları.txt","w")
dosya_mp4 = open("C:/Users/OKAN/Desktop/Mp4_dosyaları.txt","w")

for klasor_yolu,klasor_adi,alt_klasorler in os.walk("D:"):

    for i in alt_klasorler:
        if i.endswith(".txt"):
            liste_txt.append(i)
        elif i.endswith(".pdf"):
            liste_pdf.append(i)
        elif i.endswith(".mp4"):
            liste_mp4.append(i)

for i in liste_mp4:
    dosya_mp4.write(i+"\n")
for i in liste_txt:
    dosya_txt.write(i+"\n")
for i in liste_pdf:
    dosya_pdf.write(i+"\n")

dosya_txt.close()
dosya_pdf.close()
dosya_mp4.close()