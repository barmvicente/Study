import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox

class comCloseEvent(QWidget):


	def closeEvent(self, event):
		resposta = QMessageBox.question(self,
		 "Titulo", "Deseja sair?",
		 QMessageBox.Yes | QMessageBox.No)

		if resposta == QMessageBox.Yes:
			event.accept()
		else:
			event.ignore()



class objectExit(comCloseEvent):


	def __init__(self):
		super().__init__()
		self.initUi()


	def initUi(self):
		self.setGeometry(300, 300, 300, 220)
		self.setWindowTitle("Exit")
		self.show()



if __name__ == "__main__":
	app = QApplication(sys.argv)
	ex = objectExit()
	sys.exit(app.exec_())