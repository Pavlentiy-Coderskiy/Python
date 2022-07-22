from PyQt5 import QtWidgets 
from PyQt5.QtWidgets import QApplication, QMainWindow 
import sys 

def add_label():
	print("aboba")



def application():
	app = QApplication(sys.argv)
	window = QMainWindow()
	window.setGeometry(300, 250, 350, 200)
	window.setWindowTitle("adc")
	aboba = QtWidgets.QLabel(window)
	aboba.setText("ABOBA BLЯ")	
	aboba.move(100, 100,)
	aboba.adjustSize()
	btn = QtWidgets.QPushButton
	btn.move(70, 150)
	btn.setText("ASS")
	btn.setFixedWidth(200)
	btn.clicked.connect(add_label)


	window.show()
	sys.exit(app.exec_())
if __name__ == "__QT__":
   application()      






