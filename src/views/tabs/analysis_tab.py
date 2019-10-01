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

        terminalContent = QPlainTextEdit()

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
        gridLayout.addWidget(terminalContent, 1, 0, 1, 1)
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
        layout = QtWidgets.QGridLayout()

        self.dropDownMenuPlugin = QtWidgets.QComboBox()
        self.dropDownMenuPoi = QtWidgets.QComboBox()

        pluginLabel = QtWidgets.QLabel("Plugin")
        staticLabel = QtWidgets.QLabel("Static Analysis")
        poiTypeLabel = QtWidgets.QLabel("Point of Interest Type")
        staticRunBtn = QtWidgets.QPushButton("Run")

        layout.addWidget(self.dropDownMenuPlugin, 0, 2, 2, 2)
        layout.addWidget(self.dropDownMenuPoi, 0, 6, 1, 2)
        layout.addWidget(pluginLabel, 0, 0, 2, 2)
        layout.addWidget(staticLabel, 0, 8, 2, 2)
        layout.addWidget(poiTypeLabel, 0, 4, 2, 2)
        layout.addWidget(staticRunBtn, 0, 10, 2, 2)

        return layout

    def dynamicLayout(self):
        layout = QtWidgets.QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)

        DynamicAn = QtWidgets.QLabel("Dynamic Analysis")
        dynamicRunbtn = QtWidgets.QPushButton("Run")
        dynamicStopbtn = QtWidgets.QPushButton("Stop")
        spacerItem = QtWidgets.QSpacerItem(1, 1, QSizePolicy.Expanding)

        layout.addItem(spacerItem)
        layout.addWidget(DynamicAn)
        layout.addWidget(dynamicRunbtn)
        layout.addWidget(dynamicStopbtn)
        layout.addItem(spacerItem)

        return layout
