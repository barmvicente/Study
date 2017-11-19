import sys
from PyQt5.QtWidgets import QGridLayout, QApplication, QMainWindow, QMessageBox
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtCore import Qt

from velha import Ui_MainWindow
from custom import ClickableLabel
from utils import showDialog


class Jogo(QMainWindow):
	def __init__(self):
		super().__init__()
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		self.connectSignals()

		self.table = [-1] * 9
		self.turno = 0
		self.players = ["x", "o"]
		x = QPixmap()
		o = QPixmap()
		x.load(":/game/x.jpg")
		o.load(":/game/o.png")
		x = x.scaledToWidth(50)
		o = o.scaledToWidth(50)

		self.players_images = [x, o]
		self.label_list = []
		self.initTable()


	def initTable(self):
		parent = self.ui.jogo
		grid = QGridLayout(parent)
		
		for i, _ in enumerate(self.table):
			label = ClickableLabel(i)
			label.setText("_")
			newfont = QFont("Times", 40, QFont.Bold)
			label.setAlignment(Qt.AlignCenter)
			label.setFont(newfont)
			label.sig_send_pos.connect(self.gameAction)
			grid.addWidget(label, i%3, i//3)
			self.label_list.append(label)


	def connectSignals(self):
		self.ui.actionReset.triggered.connect(self.clear)


	def gameAction(self, pos):
		if self.table[pos] == -1:
			self.table[pos] = self. turno % 2
			self.turno += 1
			self.label_list[pos].setPixmap(self.players_images[self.turno % 2])

			if self.checkEnd():
				if self.turno % 2 == 0:
					self.ui.placar_x.setText(str(int(self.ui.placar_x.text()) + 1))
					showDialog("Resultado", "X venceu!")
				else:
					self.ui.placar_o.setText(str(int(self.ui.placar_o.text()) + 1))
					showDialog("Resultado", "O venceu!")
				self.restart()
			elif self.turno == 9:
				showDialog("Resultado", "Deu Empate :)")
				self.restart()


	def checkEnd(self):        
		if (((self.table[0] != -1 and self.table[1] != -1 and self.table[2] != -1) and
                (self.table[0] == self.table[1] == self.table[2])) or
                ((self.table[0] != -1 and self.table[3] != -1 and self.table[6] != -1) and
                    (self.table[0] == self.table[3] == self.table[6])) or
                ((self.table[0] != -1 and self.table[4] != -1 and self.table[8] != -1) and
                    (self.table[0] == self.table[4] == self.table[8])) or
                ((self.table[1] != -1 and self.table[4] != -1 and self.table[7] != -1) and
                    (self.table[1] == self.table[4] == self.table[7])) or
                ((self.table[2] != -1 and self.table[5] != -1 and self.table[8] != -1) and
                    (self.table[2] == self.table[5] == self.table[8])) or
                ((self.table[2] != -1 and self.table[4] != -1 and self.table[6] != -1) and
                    (self.table[2] == self.table[4] == self.table[6])) or
                ((self.table[3] != -1 and self.table[4] != -1 and self.table[5] != -1) and
                    (self.table[3] == self.table[4] == self.table[5])) or
                ((self.table[6] != -1 and self.table[7] != -1 and self.table[8] != -1) and
                    (self.table[6] == self.table[7] == self.table[8]))):
			return True
		else:
			return False


	def restart(self):
		self.turno = 0
		self.table = [-1]*9
		for label in self.label_list:
			label.setText("_")


	def clear(self):
		self.ui.placar_x.setText("0")
		self.ui.placar_o.setText("0")
		self.restart()


def main():
	app = QApplication(sys.argv)
	e = Jogo()
	e.show()
	sys.exit(app.exec_())


if __name__ == "__main__":
	main()
