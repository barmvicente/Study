import sys
from PyQt5 import QtWidgets, QtCore
from form2 import Ui_MainWindow


class form2(QtWidgets.QMainWindow):
	def __init__(self, nome, idade, cpf):
		super().__init__()
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)

		self.ui.nome.setText(nome)
		self.ui.idade.setText(idade)
		self.ui.cpf.setText(cpf)
