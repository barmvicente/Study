import sys
from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import pyqtSignal


class ClickableLabel(QLabel):
	sig_send_pos = pyqtSignal(int)


	def __init__(self, pos, parent=None):
		super(ClickableLabel, self).__init__(parent)
		self.pos = pos


	def mousePressEvent(self, e):
		QLabel.mousePressEvent(self, e)
		self.sig_send_pos.emit(self.pos)
