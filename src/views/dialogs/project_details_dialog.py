from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QDesktopWidget, QTableWidgetItem, QTableWidget, QGridLayout, QDialog


class ProjectDetails(QDialog):
    def __init__(self, projectName):
        super().__init__()
        self.setFont(QFont("arial", 11))
        self.setWindowTitle(projectName)
        self.__initUI()
        self.__setWindowPosition()

    def __initUI(self):
        layout = QGridLayout()
        layout.addWidget(self.__tableBuilder())
        self.setLayout(layout)

    def __setWindowPosition(self):
        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.setWidth(500)
        qtRectangle.setHeight(600)
        qtRectangle.moveCenter(centerPoint)
        self.setGeometry(qtRectangle)

    def __tableBuilder(self):
        self.table = QTableWidget()
        self.table.setRowCount(13)
        self.table.setColumnCount(2)

        self.table.setItem(0, 0, QTableWidgetItem('OS'))
        self.table.setItem(1, 0, QTableWidgetItem('Binary Type'))
        self.table.setItem(2, 0, QTableWidgetItem('Machine'))
        self.table.setItem(3, 0, QTableWidgetItem('Class'))
        self.table.setItem(4, 0, QTableWidgetItem('Bits'))
        self.table.setItem(5, 0, QTableWidgetItem('Language'))
        self.table.setItem(6, 0, QTableWidgetItem('Canary'))
        self.table.setItem(7, 0, QTableWidgetItem('Crypto'))
        self.table.setItem(8, 0, QTableWidgetItem('Nx'))
        self.table.setItem(9, 0, QTableWidgetItem('Pic'))
        self.table.setItem(10, 0, QTableWidgetItem('Relocs'))
        self.table.setItem(11, 0, QTableWidgetItem('Relro'))
        self.table.setItem(12, 0, QTableWidgetItem('Stripped'))

        self.table.setHorizontalHeaderLabels(['Name', 'Value'])
        self.table.verticalHeader().setVisible(False)
        self.table.horizontalHeader().setStretchLastSection(True)

        return self.table