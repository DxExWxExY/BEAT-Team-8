from PyQt5 import QtWidgets
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QGridLayout, QPlainTextEdit, QVBoxLayout, QListWidget, QAbstractItemView, QLineEdit, \
    QPushButton, QSizePolicy

from src.common.tab_layout import TabLayout


class AnalysisTab(TabLayout):

    def __init__(self):
        super().__init__("Point of Interest View", "Detailed Point of Interest View", True)
        self.list = []
        self.poiContentArea = QPlainTextEdit()
        super().addContentToTopPanel(self.TopPanelBuilder())
        super().addContentToRightPanel(self.rightPanelBuilder())
        super().addContentToLeftPanel(self.leftPanelBuilder())
        super().build()

    def leftPanelBuilder(self):
        layout = QVBoxLayout()
        self.poiList = QListWidget()
        layout.addLayout(self.searchBuilder())
        self.poiList.setSelectionMode(QAbstractItemView.MultiSelection)

        layout.addWidget(self.poiList)

        return layout

    def rightPanelBuilder(self):
        rightLayout = QtWidgets.QHBoxLayout()
        gridLayout = QtWidgets.QGridLayout()
        btnGrid = QtWidgets.QVBoxLayout()
        CommentVertLayout = QtWidgets.QVBoxLayout()
        btnSpacer = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)

        self.terminalContent = QPlainTextEdit()
        self.cliInput = QLineEdit()

        self.terminalContent.setPlaceholderText("Terminal Output")
        self.cliInput.setPlaceholderText("Enter Terminal Commands Here...")

        self.terminalContent.setFont(QFont("Consolas", 11))
        self.cliInput.setFont(QFont("Consolas", 11))

        self.terminalContent.setReadOnly(True)

        self.commentBtn = QPushButton("Comment")
        self.analysisResultBtn = QPushButton("Analysis Results")
        self.outputFieldViewBtn = QPushButton("Output")

        CommentVertLayout.addWidget(self.commentBtn)
        CommentVertLayout.addItem(btnSpacer)

        btnGrid.addWidget(self.analysisResultBtn)
        btnGrid.addWidget(self.outputFieldViewBtn)
        btnGrid.addItem(btnSpacer)

        gridLayout.addWidget(self.poiContentArea, 0, 0, 1, 1)
        gridLayout.addWidget(self.terminalContent, 1, 0, 1, 1)
        gridLayout.addItem(CommentVertLayout, 0, 1, 1, 1)
        gridLayout.addItem(btnGrid, 0, 2, 1, 1)
        gridLayout.addWidget(self.cliInput, 2, 0, 1, 1)

        rightLayout.addLayout(gridLayout)

        return rightLayout

    def TopPanelBuilder(self):
        layout = QGridLayout()

        self.dropDownMenuPlugin = QtWidgets.QComboBox()
        self.dropDownMenuPoi = QtWidgets.QComboBox()

        pluginLabel = QtWidgets.QLabel("Plugin")
        staticLabel = QtWidgets.QLabel("Static Analysis")
        poiTypeLabel = QtWidgets.QLabel("Point of Interest Type")
        self.staticRunBtn = QtWidgets.QPushButton("Run")
        DynamicAn = QtWidgets.QLabel("Dynamic Analysis")
        self.dynamicRunbtn = QtWidgets.QPushButton("Run")
        self.dynamicStopbtn = QtWidgets.QPushButton("Stop")
        spacerItem = QtWidgets.QSpacerItem(1, 1, QSizePolicy.Expanding)

        layout.addWidget(pluginLabel, 0, 0, 1,1)
        layout.addWidget(self.dropDownMenuPlugin, 0, 1, 1, 2)
        layout.addWidget(poiTypeLabel, 0, 3, 1, 2)
        layout.addWidget(self.dropDownMenuPoi, 0, 5, 1, 2)
        layout.addItem(spacerItem, 0, 6 , 1, 10)

        layout.addWidget(staticLabel, 1, 0, 1, 1)
        layout.addWidget(self.staticRunBtn, 1, 1, 1, 1)
        layout.addWidget(DynamicAn, 1, 2, 1 ,1)
        layout.addWidget(self.dynamicRunbtn, 1, 3, 1 ,1)
        layout.addWidget(self.dynamicStopbtn, 1, 4, 1 ,1)
        layout.addItem(spacerItem, 1, 5, 1 ,13)

        return layout

    def searchBuilder(self):
        layout = QtWidgets.QGridLayout()

        self.searchBox = QLineEdit()
        self.searchBox.setPlaceholderText("Search Points of Interest")

        self.searchButton = QPushButton('Search')

        layout.addWidget(self.searchBox, 0, 0, 1, 4)
        layout.addWidget(self.searchButton, 0, 4, 1, 2)

        return layout

