from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *

from src.common.tab_layout import TabLayout


class AnalysisTab(TabLayout):

    def __init__(self):
        self.list = []
        self.poiContentArea = QPlainTextEdit()
        super().__init__("Point of Interest View", "Detailed Point of Interest View", True)
        super().addContentToTopPanel(self.TopPanelBuilder())
        super().addContentToRightPanel(self.rightPanelBuilder())
        super().addContentToLeftPanel(self.leftPanelBuilder())
        super().build()

    def leftPanelBuilder(self):
        layout = QVBoxLayout()
        self.projectList = QListWidget()
        layout.addLayout(self.searchBuilder())
        self.projectList.setSelectionMode(QAbstractItemView.MultiSelection)

        layout.addWidget(self.projectList)

        return layout

    def rightPanelBuilder(self):
        rightLayout = QtWidgets.QHBoxLayout()
        gridLayout = QtWidgets.QGridLayout()
        btnGrid = QtWidgets.QVBoxLayout()
        CommentVertLayout = QtWidgets.QVBoxLayout()
        btnSpacer = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)

        TerminalContent = QPlainTextEdit()

        self.commentBtn = QPushButton("C")
        self.analysisResultBtn = QPushButton("A")
        self.outputFieldViewBtn = QPushButton("O")

        self.commentBtn.setToolTip("Comment")
        self.analysisResultBtn.setToolTip("Analysis Results")
        self.outputFieldViewBtn.setToolTip("Output Field View")

        CommentVertLayout.addWidget(self.commentBtn)
        CommentVertLayout.addItem(btnSpacer)

        btnGrid.addWidget(self.analysisResultBtn)
        btnGrid.addWidget(self.outputFieldViewBtn)
        btnGrid.addItem(btnSpacer)

        gridLayout.addWidget(self.poiContentArea, 0, 0, 1, 1)
        gridLayout.addWidget(TerminalContent, 1, 0, 1, 1)
        gridLayout.addItem(CommentVertLayout, 0, 1, 1, 1)
        gridLayout.addItem(btnGrid, 0, 2, 1, 1)

        rightLayout.addLayout(gridLayout)

        return rightLayout

    def TopPanelBuilder(self):
        topLayout = QGridLayout()
        topLayout.addLayout(self.staticLayout(), 0, 0)
        topLayout.addLayout(self.dynamicLayout(), 0, 1)

        return topLayout

    def searchBuilder(self):
        layout = QtWidgets.QGridLayout()

        self.searchBox = QLineEdit()
        self.searchBox.setPlaceholderText("Search Points of Interest")

        self.searchButton = QPushButton('Search')

        layout.addWidget(self.searchBox, 0, 0, 1, 4)
        layout.addWidget(self.searchButton, 0, 4, 1, 2)

        return layout

    def staticLayout(self):
        layout = QtWidgets.QHBoxLayout()

        gridLayout = QtWidgets.QGridLayout()

        dropDownMenuPlugin = QtWidgets.QComboBox()
        dropDownMenuPlugin.addItem("Network Plugin")
        dropDownMenuPlugin.addItem("Cryptography Plugin")
        gridLayout.addWidget(dropDownMenuPlugin, 0, 2, 2, 2)

        dropDownMenuPoi = QtWidgets.QComboBox()
        dropDownMenuPoi.addItem("Function")
        dropDownMenuPoi.addItem("Variable")
        dropDownMenuPoi.addItem("String")
        dropDownMenuPoi.addItem("DLL")
        dropDownMenuPoi.addItem("Struct")
        dropDownMenuPoi.addItem("Packet Protocol")
        gridLayout.addWidget(dropDownMenuPoi, 0, 6, 1, 2)

        pluginLabel = QtWidgets.QLabel("Plugin")
        gridLayout.addWidget(pluginLabel, 0, 0, 2, 2)

        StaticAn = QtWidgets.QLabel("Static analysis")
        gridLayout.addWidget(StaticAn, 0, 8, 2, 2)

        label_3 = QtWidgets.QLabel("Point of Interest type")
        gridLayout.addWidget(label_3, 0, 4, 2, 2)

        staticRunbtn = QtWidgets.QPushButton("Run")
        gridLayout.addWidget(staticRunbtn, 0, 10, 2, 2)

        layout.addLayout(gridLayout)

        return layout

    def dynamicLayout(self):
        layout = QtWidgets.QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)

        DynamicAn = QtWidgets.QLabel("Dynamic analysis")
        dynamicRunbtn = QtWidgets.QPushButton("Run")
        dynamicStopbtn = QtWidgets.QPushButton("Stop")

        spacerItem = QtWidgets.QSpacerItem(1, 1, QSizePolicy.Expanding)
        layout.addItem(spacerItem)
        layout.addWidget(DynamicAn)
        layout.addWidget(dynamicRunbtn)
        layout.addWidget(dynamicStopbtn)
        layout.addItem(spacerItem)

        return layout
