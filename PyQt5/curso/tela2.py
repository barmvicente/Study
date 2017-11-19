from custom import ClickableLabel
import sys
from PyQt5.QtWidgets import QApplication, QWidget 


def Click(pos):
	print(pos)


app = QApplication(sys.argv)
w = QWidget()
w.resize(200, 200)
label = ClickableLabel(1, w)
label.setText("texto")
label.sig_send_pos.connect(Click)
w.show()
sys.exit(app.exec_())