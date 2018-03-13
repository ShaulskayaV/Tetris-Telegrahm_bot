import pygame
import PyQt5
import sys,random
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget


class Tetris(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.tboard = Board(self)
        self.setCentralWidget(self.tboard)

        self.statusbar =self.statusBar()
        self.tboard.msg2Statusba[str].connect(self.statusbar.showMessage)
        self.tboard.start()
        self.resize(180,380)
        self.center()
        self.setWindowTitle('Tetris')
        self.show()
    def center(self):
        screen= QDesktopWidget().screenGeometry()
        size= self.geometry()
        self.move ((screen.width()-size.width())/2, (screen.height()-size.height())/2)



