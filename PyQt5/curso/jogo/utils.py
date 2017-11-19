from PyQt5 import QtWidgets


def showDialog(titulo, texto):
	msg = QtWidgets.QMessageBox()
	msg.setIcon(QtWidgets.QMessageBox.Critical)
	msg.setText(texto)
	msg.setWindowTitle(titulo)
	msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
	msg.exec_()