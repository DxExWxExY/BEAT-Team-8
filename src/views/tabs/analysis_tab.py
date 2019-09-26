from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import *
from src.common.tab_layout import TabLayout
from src.views.dialogs.output_field_dialog import OutputField
from src.views.dialogs.analysis_result_dialog import AnalysisResultDialog
from src.views.dialogs.comment_dialog import CommentDialog


class AnalysisTab(TabLayout):

    def __init__(self):
        self.list = []
        self.POIContentArea = QPlainTextEdit()
        # your constructor must make the following calls
        super().__init__("Point of Interest View", "Detailed Point of Interest View", True)
        super().addContentToTopPanel(self.TopPanelBuilder())
        super().addContentToRightPanel(self.rightPanelBuilder())
        super().addContentToLeftPanel(self.leftPanelBuilder())
        super().build()

    def leftPanelBuilder(self):
        layout = QVBoxLayout()
        projectList = QListWidget()
        layout.addLayout(self.searchBuilder())
        projectList.setSelectionMode(QAbstractItemView.MultiSelection)

        for i in range(4):
            item = QtWidgets.QListWidgetItem("Item %i" % i)
            projectList.addItem(item)

        projectList.itemClicked.connect(lambda: self.displayPOI(projectList))
        layout.addWidget(projectList)

        return layout

    def rightPanelBuilder(self):
        rightLayout = QtWidgets.QHBoxLayout()
        gridLayout = QtWidgets.QGridLayout()
        btnGrid = QtWidgets.QVBoxLayout()
        CommentVertLayout = QtWidgets.QVBoxLayout()
        btnSpacer = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)

        TerminalContent = QPlainTextEdit()

        CommentBtn = QPushButton()
        AnalysisResultbtn = QPushButton()
        OutPutFieldViewbtn = QPushButton()

        CommentBtn.setText("C")
        AnalysisResultbtn.setText("A")
        OutPutFieldViewbtn.setText("O")

        CommentBtn.setToolTip("Comment")
        AnalysisResultbtn.setToolTip("Analysis Results")
        OutPutFieldViewbtn.setToolTip("Output Field View")

        CommentBtn.clicked.connect(self.commentWindow)
        AnalysisResultbtn.clicked.connect(self.analysisResultWindow)
        OutPutFieldViewbtn.clicked.connect(self.outputFieldWindow)

        CommentVertLayout.addWidget(CommentBtn)
        CommentVertLayout.addItem(btnSpacer)

        btnGrid.addWidget(AnalysisResultbtn)
        btnGrid.addWidget(OutPutFieldViewbtn)
        btnGrid.addItem(btnSpacer)

        gridLayout.addWidget(self.POIContentArea, 0, 0, 1, 1)
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

        searchBox = QLineEdit()
        searchBox.setPlaceholderText("Search Points of Interest")
        searchBox.returnPressed.connect(lambda: print("Enter Detected"))

        searchButton = QPushButton('Search')

        layout.addWidget(searchBox, 0, 0, 1, 4)
        layout.addWidget(searchButton, 0, 4, 1, 2)

        return layout

    def staticLayout(self):
        _translate = QtCore.QCoreApplication.translate

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

        pluginLabel = QtWidgets.QLabel()
        pluginLabel.setText(_translate("Dialog", "Plugin"))
        gridLayout.addWidget(pluginLabel, 0, 0, 2, 2)

        StaticAn = QtWidgets.QLabel()
        StaticAn.setText(_translate("Dialog", "Static analysis"))
        gridLayout.addWidget(StaticAn, 0, 8, 2, 2)

        label_3 = QtWidgets.QLabel()
        label_3.setText(_translate("Dialog", "Point of Interest type"))
        gridLayout.addWidget(label_3, 0, 4, 2, 2)

        staticRunbtn = QtWidgets.QPushButton()
        staticRunbtn.setText(_translate("Dialog", "Run"))
        gridLayout.addWidget(staticRunbtn, 0, 10, 2, 2)



        layout.addLayout(gridLayout)

        return layout

    def dynamicLayout(self):
        _translate = QtCore.QCoreApplication.translate

        layout = QtWidgets.QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)

        DynamicAn = QtWidgets.QLabel()
        DynamicAn.setText(_translate("Dialog", "Dynamic analysis"))

        dynamicRunbtn = QtWidgets.QPushButton()
        dynamicRunbtn.setText(_translate("Dialog", "Run"))

        dynamicStopbtn = QtWidgets.QPushButton()
        dynamicStopbtn.setText(_translate("Dialog", "Stop"))

        spacerItem = QtWidgets.QSpacerItem(1, 1, QSizePolicy.Expanding)
        layout.addItem(spacerItem)
        layout.addWidget(DynamicAn)
        layout.addWidget(dynamicRunbtn)
        layout.addWidget(dynamicStopbtn)
        layout.addItem(spacerItem)


        return layout

    def commentWindow(self):
        self.commentView = CommentDialog()
        self.commentView.show()

    def outputFieldWindow(self):
        self.outputfieldWindow = OutputField()
        self.outputfieldWindow.show()

    def analysisResultWindow(self):
        self.analysisResultWindow = AnalysisResultDialog()
        self.analysisResultWindow.show()

    def displayPOI(self, projectList):
        items = projectList.selectedItems()
        x = []
        for i in range(len(items)):
            x.append(str(projectList.selectedItems()[i].text()))
        print(x)
        self.updatePOI(x)

    def updatePOI(self, x):
        screen = ""
        for i in range(len(x)):
            screen += x[i] + "\n"
        self.POIContentArea.setPlainText(screen)
