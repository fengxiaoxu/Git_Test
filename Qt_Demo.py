# -*- coding: utf-8 -*-
"""
@author: xuyansong
@software: PyCharm
@file: Qt_Demo.py
@time: 2021/2/21 10:29
"""
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class QtDemo(QWidget):
    def __init__(self):
        super(QtDemo, self).__init__()
        self.initUI()

    def initUI(self):
        # set windowTitle Name
        self.setWindowTitle('Qt Demo')
        # set window Size
        self.resize(500,400)

        self.Label = QLabel("这是一个标签")
        self.vLayout = QVBoxLayout()
        self.vLayout.addWidget(self.Label)
        self.setLayout(self.vLayout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QtDemo()
    window.show()
    sys.exit(app.exec_())
