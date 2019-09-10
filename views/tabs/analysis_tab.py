from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import *
from common.tab_layout import TabLayout
from views.dialogs.output_field_dialog import OutputField
from views.dialogs.analysis_result_dialog import AnalysisResultDialog
from views.dialogs.comment_dialog import CommentDialog


class AnalysisTab(TabLayout):

    def __init__(self):
        self.list = []
        self.POIcontentArea = QPlainTextEdit()
        # your constructor must make the following calls
        super().__init__("Point of Interest View", "Detailed Point of Interest View")
        super().addContentToTopPanel(self.TopPanelBuilder())
        super().addContentToRightPanel(self.rightPanelBuilder())
        super().addContentToLeftPanel(self.leftPanelBuilder())
        super().build()

    def leftPanelBuilder(self):
        layout = QVBoxLayout()
        projectList = QListWidget()
        layout.addLayout(self.searchBuilder())

        projectList.addItem("POI 1")
        projectList.addItem("POI 2")
        projectList.addItem("POI 3")
        projectList.addItem("POI 4")
        projectList.itemClicked.connect(lambda : self.printItemText(projectList))
        layout.addWidget(projectList)

        return layout

    def rightPanelBuilder(self):
        rightLayout = QtWidgets.QHBoxLayout()
        gridLayout = QtWidgets.QGridLayout()
        gridLayout.setObjectName("gridLayout")
        btnGrid = QtWidgets.QVBoxLayout()
        CommentVertLayout = QtWidgets.QVBoxLayout()
        btnSpacer = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)

        TerminalContent = QPlainTextEdit()

        CommentBtn = QPushButton()
        CommentBtn.setText("C")
        CommentBtn.clicked.connect(self.commentWindow)

        AnalysisResultbtn = QPushButton()
        AnalysisResultbtn.setText("A")
        AnalysisResultbtn.clicked.connect(self.analysisResultWindow)

        OutPutFieldViewbtn = QPushButton()
        OutPutFieldViewbtn.setText("O")
        OutPutFieldViewbtn.clicked.connect(self.outputfieldWindow)

        CommentVertLayout.addWidget(CommentBtn)
        CommentVertLayout.addItem(btnSpacer)

        btnGrid.addWidget(AnalysisResultbtn)
        btnGrid.addWidget(OutPutFieldViewbtn)
        btnGrid.addItem(btnSpacer)

        gridLayout.addWidget(self.POIcontentArea, 0, 0, 1, 1)
        gridLayout.addWidget(TerminalContent, 1, 0, 1, 1)
        gridLayout.addItem(CommentVertLayout, 0, 1, 1, 1)
        gridLayout.addItem(btnGrid, 0, 2, 1, 1)

        rightLayout.addLayout(gridLayout)
        return rightLayout

    def TopPanelBuilder(self):
        topLayout = QtWidgets.QHBoxLayout()
        topLayout.addLayout(self.StaticLayout())
        topLayout.addLayout(self.DynamicLayout())

        return topLayout

    def searchBuilder(self):
        layout = QtWidgets.QGridLayout()

        searchBox = QLineEdit()
        searchBox.setPlaceholderText("Search Points of Interest")
        searchBox.returnPressed.connect(lambda: print("Enter Detected"))

        searchButton = QPushButton('Search')

        layout.addWidget(searchBox, 0, 0, 1, 4)
        layout.addWidget(searchButton, 0, 2, 1, 2)

        return layout

    def StaticLayout(self):
        _translate = QtCore.QCoreApplication.translate

        layout = QtWidgets.QHBoxLayout()
        layout.setObjectName("horizontalLayout")

        gridLayout = QtWidgets.QGridLayout()
        gridLayout.setObjectName("gridLayout")

        dropDownMenuPlugin = QtWidgets.QComboBox()
        dropDownMenuPlugin.setObjectName("comboBox")
        dropDownMenuPlugin.addItem("Network Plugin")
        dropDownMenuPlugin.addItem("cryptography Plugin")
        gridLayout.addWidget(dropDownMenuPlugin, 0, 1, 1, 3)

        dropDownMenuPoi = QtWidgets.QComboBox()
        dropDownMenuPoi.setObjectName("dropDownMenuPoi")
        dropDownMenuPoi.addItem("Functions")
        dropDownMenuPoi.addItem("Variables")
        dropDownMenuPoi.addItem("Strings")
        gridLayout.addWidget(dropDownMenuPoi, 2, 1, 1, 1)

        pluginlabel = QtWidgets.QLabel()
        pluginlabel.setObjectName("pluginlabel")
        pluginlabel.setText(_translate("Dialog", "Plugin"))
        gridLayout.addWidget(pluginlabel, 0, 0, 1, 1)

        StaticAn = QtWidgets.QLabel()
        StaticAn.setObjectName("StaticAn")
        StaticAn.setText(_translate("Dialog", "Static analysis"))
        gridLayout.addWidget(StaticAn, 1, 0, 1, 1)

        label_3 = QtWidgets.QLabel()
        label_3.setObjectName("label_3")
        label_3.setText(_translate("Dialog", "point of interest type"))
        gridLayout.addWidget(label_3, 2, 0, 1, 1)

        staticRunbtn = QtWidgets.QPushButton()
        staticRunbtn.setObjectName("staticRunbtn")
        staticRunbtn.setText(_translate("Dialog", "Run"))
        gridLayout.addWidget(staticRunbtn, 1, 1, 1, 1)

        layout.addLayout(gridLayout)

        return layout

    def DynamicLayout(self):
        _translate = QtCore.QCoreApplication.translate

        layout = QtWidgets.QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setObjectName("horizontalLayout")

        DynamicAn = QtWidgets.QLabel()
        DynamicAn.setObjectName("DynamicAn")
        DynamicAn.setText(_translate("Dialog", "Dynamic analysis"))

        dynamicRunbtn = QtWidgets.QPushButton()
        dynamicRunbtn.setObjectName("dynamicRunbtn")
        dynamicRunbtn.setText(_translate("Dialog", "Run"))

        dynamicStopbtn = QtWidgets.QPushButton()
        dynamicStopbtn.setObjectName("dynamicStopbtn")
        dynamicStopbtn.setText(_translate("Dialog", "Stop"))

        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        layout.addItem(spacerItem)
        layout.addWidget(DynamicAn)
        layout.addWidget(dynamicRunbtn)
        layout.addWidget(dynamicStopbtn)
        layout.addItem(spacerItem)

        return layout

    def commentWindow(self):
        self.commentView = CommentDialog()
        self.commentView.show()

    def outputfieldWindow(self):
        self.outputfieldWindow = OutputField()
        self.outputfieldWindow.show()

    def analysisResultWindow(self):
        self.analysisResultWindow = AnalysisResultDialog()
        self.analysisResultWindow.show()

    def printItemText(self, projectList):
        items = projectList.selectedItems()
        x = []
        for i in range(len(items)):
            x.append(str(projectList.selectedItems()[i].text()))
        print(x)
        self.updatePOI(x)

    def updatePOI(self,x):

        for i in range(len(x)):
            self.POIcontentArea.setPlainText(x[i])
