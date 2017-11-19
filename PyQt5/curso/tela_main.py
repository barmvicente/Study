import sys
from PyQt5 import QtWidgets, QtCore
from main import Ui_MainWindow
import tela_form1


class MainWindow(QtWidgets.QMainWindow):
	def __init__(self):
		super().__init__()
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		self.connectSignals()
		self.dock_widget = None


	def connectSignals(self):
		self.ui.botao.clicked.connect(lambda: self.add_widget("cadastro"))


	def add_widget(self, text):
		if not self.dock_widget:
			self.dock_widget = QtWidgets.QDockWidget(self)
			self.dock_widget.setMinimumWidth(400)
			self.dock_widget.setFeatures(QtWidgets.QDockWidget.DockWidgetClosable)
			self.addDockWidget(QtCore.Qt.LeftDockWidgetArea, self.dock_widget)
			self.dock_widget.show()
		else:
			self.dock_widget.show()

		if text == "cadastro":
			self.widget = tela_form1.form1(self.dock_widget.widget())
		self.dock_widget.setWidget(self.widget)


def main():
	app = QtWidgets.QApplication(sys.argv)
	mw = MainWindow()
	mw.show()
	sys.exit(app.exec_())


if __name__ == "__main__":
	main()