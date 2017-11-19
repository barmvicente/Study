import sys
from PyQt5 import QtWidgets, QtCore
from functools import partial

from problemafor import Ui_MainWindow



class Tela(QtWidgets.QMainWindow):
	def __init__(self):
		super().__init__()
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		self.b_list = [self.ui.b1, self.ui.b2, self.ui.b3, 
					   self.ui.b4, self.ui.b5]
		self.connectSignals()


	def connectSignals(self):
		for i, button in enumerate(self.b_list):
			#button.clicked.connect(lambda: self.print_num(button.text()))
			button.clicked.connect(partial(self.print_num, i+1))


	def print_num(self, i):
		print(str(i))


def main():
	app = QtWidgets.QApplication(sys.argv)
	m = Tela()
	m.show()
	sys.exit(app.exec_())


if __name__ == "__main__":
	main()