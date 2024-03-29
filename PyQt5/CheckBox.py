import sys
from PyQt5.QtWidgets import QWidget,QLabel,QPushButton,QVBoxLayout,QApplication,QCheckBox

class Pencere(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
    def init_ui(self):

        self.checkbox = QCheckBox("Python'ı seviyor musun?")
        self.yazı_alanı = QLabel("")
        self.buton = QPushButton("Buton")

        v_box = QVBoxLayout()
        v_box.addWidget(self.checkbox)
        v_box.addWidget(self.yazı_alanı)
        v_box.addWidget(self.buton)
        v_box.addStretch()
        self.setLayout(v_box)
        self.setWindowTitle("Chechbox Deneme Arayüzü")
        self.buton.clicked.connect(lambda : self.click(self.checkbox.isChecked(),self.yazı_alanı))
        self.show()
    def click(self,checkbox,yazı_alanı):
        if checkbox:
            self.yazı_alanı.setText("Güzell")
        else:
            self.yazı_alanı.setText("niye ki?")

app = QApplication(sys.argv)
pencere = Pencere()
sys.exit(app.exec())