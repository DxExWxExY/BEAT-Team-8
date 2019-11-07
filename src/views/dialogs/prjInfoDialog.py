from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QGridLayout, QDesktopWidget, QVBoxLayout, QListWidget, QPushButton, QLabel, \
    QLineEdit, QTextEdit, QTableWidget, QTableWidgetItem


class prjInfoDialog(QWidget):

    def __init__(self):
        super().__init__()
        self.__setWindowPosition()
        self.__initUI()

    def __initUI(self):
        self.setWindowTitle('Project Information')
        self.setFont(QFont("arial", 11))
        self.layout = QVBoxLayout()
        self.gridLayout = QGridLayout()
        self.nameLayout = QGridLayout()
        self.descLayout = QGridLayout()

        layout = QGridLayout()
        self.projectName = QLineEdit()
        self.projectDescription = QTextEdit()
        self.binPath = QLineEdit()
        self.browsePath = QPushButton('Browse')
        self.deleteButton = QPushButton('Cancel')
        self.saveButton = QPushButton('Create')

        layout.addWidget(QLabel("Project Name"), 0, 0)
        layout.addWidget(QLabel('Binary File Path'), 3, 0)
        layout.addWidget(QLabel('Binary File Properties'), 4, 0)

        layout.addWidget(self.projectName, 0, 1, 1, 9)
        layout.addWidget(self.binPath, 3, 1, 1, 8)
        layout.addWidget(self.__tableBuilder(), 5, 1, 1, 9)


        layout.addWidget(self.deleteButton, 6, 8)
        layout.addWidget(self.saveButton, 6, 9)
        layout.addWidget(self.browsePath, 3, 9)
        self.setLayout(layout)

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


    def __setWindowPosition(self):
        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.setWidth(600)
        qtRectangle.setHeight(600)
        qtRectangle.moveCenter(centerPoint)
        self.setGeometry(qtRectangle)


