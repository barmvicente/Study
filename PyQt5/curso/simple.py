import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon

class Example(QWidget):


	def __init__(self):
		super().__init__()
		self.initUI()


	def initUI(self):
		self.setGeometry(300, 300, 300, 220)
		self.setWindowTitle("icone")
		self.setWindowIcon(QIcon("icon1.jpg"))
		self.show()


app = QApplication(sys.argv)
ex = Example()
sys.exit(app.exec_())