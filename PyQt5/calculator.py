#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication
from PyQt5.QtCore import QCoreApplication


class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):               
        
        qbtn1 = QPushButton('1', self)
        qbtn1.clicked.connect(lambda x: 1)
        qbtn1.resize(qbtn1.sizeHint())
        qbtn1.move(0, 50)     
        
        qbtn2 = QPushButton('2', self)
        qbtn2.clicked.connect(lambda x: 2)
        qbtn2.resize(qbtn2.sizeHint())
        qbtn2.move(100, 50)

        qbtn3 = QPushButton('3', self)
        qbtn3.clicked.connect(lambda x: 3)
        qbtn3.resize(qbtn3.sizeHint())
        qbtn3.move(200, 50)

        qbtn4 = QPushButton('4', self)
        qbtn4.clicked.connect(lambda x: 4)
        qbtn4.resize(qbtn4.sizeHint())
        qbtn4.move(0, 100)

        qbtn5 = QPushButton('5', self)
        qbtn5.clicked.connect(lambda x: 5)
        qbtn5.resize(qbtn5.sizeHint())
        qbtn5.move(100, 100)

        qbtn6 = QPushButton('6', self)
        qbtn6.clicked.connect(lambda x: 6)
        qbtn6.resize(qbtn6.sizeHint())
        qbtn6.move(200, 100)

        qbtn7 = QPushButton('7', self)
        qbtn7.clicked.connect(lambda x: 7)
        qbtn7.resize(qbtn7.sizeHint())
        qbtn7.move(0, 150)

        qbtn8 = QPushButton('8', self)
        qbtn8.clicked.connect(lambda x: 8)
        qbtn8.resize(qbtn8.sizeHint())
        qbtn8.move(100, 150)

        qbtn9 = QPushButton('9', self)
        qbtn9.clicked.connect(lambda x: 9)
        qbtn9.resize(qbtn9.sizeHint())
        qbtn9.move(200, 150)

        self.setGeometry(800, 600, 500, 300)
        self.setWindowTitle('Calculadora')    
        self.show()

        return qbtn1, qbtn2
        
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
