import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys
mesaj = MIMEMultipart()
mesaj["from"] = "asasinokan@gmail.com"
mesaj["to"] = "asasinokan@gmail.com"
mesaj["subject"] = "Smtp ile mail gönderme.."
yazi = """
Smtp ile mail göndermeyi
deniyorum....
okan kandemir

"""

mesaj_govdesi = MIMEText(yazi,"plain")
mesaj.attach(mesaj_govdesi)

try:
    mail = smtplib.SMTP("smtp.gmail.com",587)
    mail.ehlo()
    mail.starttls()
    mail.login("asasinokan@gmail.com","buket1993")
    mail.sendmail(mesaj["from"],mesaj["to"],mesaj.as_string())
    print("mail başarıyla gönderildi...")
    mail.close()
except:
    sys.stderr.write("mail gönderilemedi...")
    sys.stderr.flush()