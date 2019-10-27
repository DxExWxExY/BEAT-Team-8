from PyQt5.QtWidgets import QWidget, QGridLayout, QDesktopWidget


class EditPoiDialog(QWidget):
    def __init__(self):
        super().__init__()
        self.__initUI()
        self.__setWindowPosition()
        self.show()

    def __initUI(self):
        layout = QGridLayout()



        self.setWindowTitle('Edit Points of Interest')
        self.setLayout(layout)

    def __setWindowPosition(self):
        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.setWidth(480)
        qtRectangle.setHeight(250)
        qtRectangle.moveCenter(centerPoint)
        self.setGeometry(qtRectangle)
