import sys 
from PyQt5.QtWidgets import QWidget, QPushButton, QLineEdit, QFormLayout, QInputDialog, QApplication


class Entrada(QWidget):


	def __init__(self, parent=None):
		super().__init__(parent)
		layout = QFormLayout()
		
		self.button1 = QPushButton("Escolher")
		self.button1.clicked.connect(self.getItem)
		self.lineedit1 = QLineEdit()
		layout.addRow(self.button1, self.lineedit1)
		
		self.button2 = QPushButton("Inteiro")
		self.button2.clicked.connect(self.getInt)
		self.lineedit2 = QLineEdit()
		layout.addRow(self.button2, self.lineedit2)
		
		self.button3 = QPushButton("Texto")
		self.button3.clicked.connect(self.getText)
		self.lineedit3 = QLineEdit()
		layout.addRow(self.button3, self.lineedit3)

		self.setLayout(layout)


	def getItem(self):
		items = ("C", "C++", "Java", "Python")
		item, ok = QInputDialog.getItem(self, "combobox",
									    "linguagens", items,
									     0, False)
		if ok and item:
			self.lineedit1.setText(item)


	def getInt(self):
		inteiro, ok = QInputDialog.getInt(self, "Entrada de inteiro",
										  "Digite um número")
		if ok:
			self.lineedit2.setText(str(inteiro))


	def getText(self):
		texto, ok = QInputDialog.getText(self, "Entrada de texto",
										 "Digite algo")
		if ok:
			self.lineedit3.setText(str(texto))


def main():
	app = QApplication(sys.argv)
	e = Entrada()
	e.show()
	sys.exit(app.exec_())


if __name__ == "__main__":
	main()