from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QGridLayout, QDesktopWidget, QPushButton, QLineEdit, \
    QDialog, QGroupBox, QComboBox, QLabel


class AddPoiDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.__initUI()
        self.__setWindowPosition()

    def __initUI(self):
        self.setWindowTitle('Edit Points of Interest')
        self.setFont(QFont("arial", 11))
        layout = QGridLayout()

        layout.addWidget(self.newPoiForm())

        self.setLayout(layout)

    def newPoiForm(self):
        layout = QGridLayout()
        box = QGroupBox("New PoI")

        self.newPoiName = QLineEdit()
        self.newPoiType = QComboBox()
        self.newPoiMapping = QLineEdit()
        self.cancelButton = QPushButton("Cancel")
        self.saveNewPoi = QPushButton("Save")

        layout.addWidget(self.newPoiName, 1, 1, 1, 2)
        layout.addWidget(QLabel("Seek Name:"), 1, 0)
        layout.addWidget(self.newPoiType, 2, 1, 1, 2)
        layout.addWidget(QLabel("PoI Type"), 2, 0)
        layout.addWidget(self.newPoiMapping, 3, 1, 1, 2)
        layout.addWidget(QLabel("Mapping"), 3, 0)
        layout.addWidget(self.cancelButton, 4, 0)
        layout.addWidget(self.saveNewPoi, 4, 2)

        box.setLayout(layout)

        return box

    def __setWindowPosition(self):
        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.setWidth(400)
        qtRectangle.setHeight(400)
        qtRectangle.moveCenter(centerPoint)
        self.setGeometry(qtRectangle)
