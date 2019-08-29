from PyQt5.QtWidgets import QApplication

from views.main_panel import MainWindow

if __name__ == "__main__":
    #Add your classes executions here
    app = QApplication([])
    mainWindow = MainWindow()
    app.exec_()