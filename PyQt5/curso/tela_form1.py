import sys
from PyQt5 import QtWidgets, QtCore
from form1 import Ui_MainWindow

import tela_form2

class form1(QtWidgets.QMainWindow):
	def __init__(self, parent=None):
		super().__init__()
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		self.connectSignals()


	def connectSignals(self):
		self.ui.botao.clicked.connect(self.envia)


	def envia(self):
		self.form2 = tela_form2.form2(self.ui.nome.text(), self.ui.idade.text(), self.ui.cpf.text())
		self.form2.show()
		self.parent().hide()