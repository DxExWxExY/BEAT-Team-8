import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication
from src.views.main_window import MainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setAttribute(Qt.AA_EnableHighDpiScaling, True)
    mainWindow = MainWindow()
    sys.exit(app.exec_())
