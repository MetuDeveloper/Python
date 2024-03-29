import sys
from PyQt5 import QtWidgets
import sqlite3

class Pencere(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.bağlantı_oluştur()
        self.init_ui()
    def bağlantı_oluştur(self):
        self.bağlantı = sqlite3.connect("Kullanıcı_DataBase.db")
        self.cursor = self.bağlantı.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS Data_Base(Kullanıcı_adı TEXT,Parolası TEXT)")
        self.bağlantı.commit()
    def init_ui(self):

        self.kullanıcı_adı = QtWidgets.QLineEdit()
        self.parola = QtWidgets.QLineEdit()
        self.parola.setEchoMode(QtWidgets.QLineEdit.Password)
        self.buton = QtWidgets.QPushButton("Giriş")
        self.yazı_alanı = QtWidgets.QLabel("")

        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(self.kullanıcı_adı)
        v_box.addWidget(self.parola)
        v_box.addWidget(self.buton)
        v_box.addWidget(self.yazı_alanı)
        v_box.addStretch()

        h_box = QtWidgets.QHBoxLayout()
        h_box.addStretch()
        h_box.addLayout(v_box)
        h_box.addStretch()
        self.setLayout(h_box)
        self.setWindowTitle("Kullanıcı Giriş Arayüzü")
        self.buton.clicked.connect(self.login)
        self.show()
    def login(self):
        adi = self.kullanıcı_adı.text()
        parola = self.parola.text()
        self.cursor.execute("Select*From Data_Base where Kullanıcı_adı = ? and Parolası = ? ",(adi,parola))
        data = self.cursor.fetchall()
        if len(data) == 0:
            self.yazı_alanı.setText("Böyle bir kullanıcı yok\nTekrar deneyiniz...")
        else:
            self.yazı_alanı.setText("Hoşgeldiniz"+adi)


app = QtWidgets.QApplication(sys.argv)
pencere = Pencere()
sys.exit(app.exec())