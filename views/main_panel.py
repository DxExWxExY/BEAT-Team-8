import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon

class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.title = "BEAT: Behavior Extraction and Analysis Tool"
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.show()