import sys
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QSizePolicy, QLabel, QFontDialog, QApplication



class Tela(QWidget):
	def __init__(self):
		super().__init__()
		self.initUi()


	def initUi(self):
		vbox = QVBoxLayout()
		b = QPushButton("Fonte", self)
		b.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
		#b.move(20, 20)
		vbox.addWidget(b)
		b.clicked.connect(self.showDialog)
		self.label = QLabel("Olar, eu sou uma fonte legal :D", self)
		#self.label.move(130, 20)
		vbox.addWidget(self.label)
		self.setLayout(vbox)
		self.setGeometry(300, 300, 300, 220)
		self.show()


	def showDialog(self):
		font, ok = QFontDialog.getFont()
		if ok:
			self.label.setFont(font)


def main():
	app = QApplication(sys.argv)
	m = Tela()
	m.show()
	sys.exit(app.exec_())


if __name__ == "__main__":
	main()