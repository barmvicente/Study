import sys
from PyQt5 import QtWidgets, QtCore

from ui_tela import Ui_MainWindow

class Tela(QtWidgets.QMainWindow):


	def __init__(self):
		super().__init__()
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		self.connectSignals()
		self.ui.spinBox.installEventFilter(self)


	def connectSignals(self):
		self.ui.pushButton.clicked.connect(self.funcao)


	def funcao(self):
		self.ui.lineEdit.setText("Olar!")


	def eventFilter(self, obj, ev):
		if ev.type() == QtCore.QEvent.Wheel:
			return True
		else:
			return False


app = QtWidgets.QApplication(sys.argv)
m = Tela()
m.show()
sys.exit(app.exec_())

if __name__ == "__main__":
	main()