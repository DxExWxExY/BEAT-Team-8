from PyQt5 import QtWidgets
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QGridLayout, QPlainTextEdit, QVBoxLayout, QListWidget, QAbstractItemView, QLineEdit, \
    QPushButton, QSizePolicy, QCheckBox

from src.common.tab_layout import TabLayout


class AnalysisTab(TabLayout):

    def __init__(self):
        super().__init__("PoI Results", "PoI Details", "Analysis")
        self.list = []
        self.poiContentArea = QPlainTextEdit()
        super().addContentToTopPanel(self.__topPanelBuilder())
        super().addContentToRightPanel(self.__rightPanelBuilder())
        super().addContentToLeftPanel(self.__leftPanelBuilder())
        super().build()

    def __leftPanelBuilder(self):
        layout = QVBoxLayout()
        self.poiList = QListWidget()
        layout.addLayout(self.__searchBuilder())
        self.poiList.setSelectionMode(QAbstractItemView.MultiSelection)
        layout.addWidget(self.poiList)

        return layout

    def __rightPanelBuilder(self):
        rightLayout = QtWidgets.QHBoxLayout()
        gridLayout = QtWidgets.QGridLayout()
        btnGrid = QtWidgets.QVBoxLayout()
        btnSpacer = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)

        self.terminalContent = QPlainTextEdit()
        self.cliInput = QLineEdit()

        self.terminalContent.setPlaceholderText("Terminal Output")
        self.cliInput.setPlaceholderText("Enter Terminal Commands Here...")

        self.terminalContent.setFont(QFont("Consolas", 11))
        self.cliInput.setFont(QFont("Consolas", 11))

        self.terminalContent.setReadOnly(True)

        self.commentBtn = QPushButton("Comment")
        self.outputFieldViewBtn = QPushButton("Output")

        self.commentBtn.setEnabled(False)

        btnGrid.addWidget(self.outputFieldViewBtn)
        btnGrid.addWidget(self.commentBtn)
        btnGrid.addItem(btnSpacer)

        gridLayout.addWidget(self.poiContentArea, 0, 0, 1, 1)
        gridLayout.addWidget(self.terminalContent, 1, 0, 1, 1)
        gridLayout.addItem(btnGrid, 0, 2, 1, 1)
        gridLayout.addWidget(self.cliInput, 2, 0, 1, 1)

        rightLayout.addLayout(gridLayout)

        return rightLayout

    def __topPanelBuilder(self):
        layout = QGridLayout()

        self.pluginDropdown = QtWidgets.QComboBox()
        self.poiTypeDropdown = QtWidgets.QComboBox()

        pluginLabel = QtWidgets.QLabel("Plugin")
        staticLabel = QtWidgets.QLabel("Static Analysis")
        poiTypeLabel = QtWidgets.QLabel("Point of Interest Type")
        self.staticRunBtn = QtWidgets.QPushButton("Run")
        DynamicAn = QtWidgets.QLabel("Dynamic Analysis")
        self.dynamicRunbtn = QtWidgets.QPushButton("Run")
        self.dynamicStopbtn = QtWidgets.QPushButton("Stop")
        self.argsCheck = QCheckBox("Use Arguments")
        self.argsBox = QLineEdit()
        self.argsBox.setPlaceholderText("Arguments for Binary")
        self.argsBox.setEnabled(False)
        spacerItem = QtWidgets.QSpacerItem(1, 1, QSizePolicy.Expanding)

        layout.addWidget(pluginLabel, 0, 0, 1, 1)
        layout.addWidget(self.pluginDropdown, 0, 1, 1, 2)
        layout.addWidget(poiTypeLabel, 0, 3, 1, 2)
        layout.addWidget(self.poiTypeDropdown, 0, 5, 1, 2)
        layout.addItem(spacerItem, 0, 6, 1, 10)

        layout.addWidget(staticLabel, 1, 0, 1, 1)
        layout.addWidget(self.staticRunBtn, 1, 1, 1, 1)
        layout.addWidget(DynamicAn, 1, 2, 1, 1)
        layout.addWidget(self.dynamicRunbtn, 1, 3, 1, 1)
        layout.addWidget(self.dynamicStopbtn, 1, 4, 1, 1)
        layout.addWidget(self.argsCheck, 1, 5, 1, 1)
        layout.addWidget(self.argsBox, 1, 6, 1, 2)
        layout.addItem(spacerItem, 1, 5, 1, 13)

        return layout

    def __searchBuilder(self):
        layout = QtWidgets.QGridLayout()

        self.searchBox = QLineEdit()
        self.searchBox.setPlaceholderText("Search Points of Interest")

        self.searchButton = QPushButton('Search')

        layout.addWidget(self.searchBox, 0, 0, 1, 4)
        layout.addWidget(self.searchButton, 0, 4, 1, 2)

        return layout
