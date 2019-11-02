import sys
from PyQt5 import QtWidgets,QtGui

def Pencere():
    app = QtWidgets.QApplication(sys.argv)
    pencere = QtWidgets.QWidget()
    pencere.setWindowTitle("Como Lokko")
    pencere.setGeometry(250,500,750,250)
    etiket1 = QtWidgets.QLabel(pencere)
    etiket1.setText("İşte burada etiket 1 yazısı var..")
    etiket1.move(50,20)
    etiket2 = QtWidgets.QLabel(pencere)
    etiket2.setPixmap(QtGui.QPixmap("224660.jpg"))
    etiket2.move(0,50)
    pencere.show()

    sys.exit(app.exec())
Pencere()