from PyQt5.QtWidgets import QListWidgetItem

from src.views.dialogs.analysis_result_dialog import AnalysisResultDialog
from src.views.dialogs.comment_dialog import CommentDialog
from src.views.dialogs.output_field_dialog import OutputField
from src.views.tabs.analysis_tab import AnalysisTab


class AnalysisTabController:
    def __init__(self):
        self.tab = AnalysisTab()
        self.project = None
        # self.model = AnalysisModel()
        self.__addEventHandlers()
        self.__populateList()
        self.__populateDropdowns()

    def __addEventHandlers(self):
        self.tab.projectList.itemClicked.connect(lambda: self.__displayPOI())
        self.tab.searchBox.returnPressed.connect(lambda: self.__searchForPoi())
        self.tab.searchButton.clicked.connect(lambda: self.__searchForPoi())
        self.tab.commentBtn.clicked.connect(lambda: self.__commentWindow())
        self.tab.analysisResultBtn.clicked.connect(lambda: self.__analysisResultWindow())
        self.tab.outputFieldViewBtn.clicked.connect(lambda: self.__outputFieldWindow())

    def __populateList(self):
        # TODO: Move this logic to model
        for i in range(4):
            self.tab.projectList.addItem(QListWidgetItem("Item %i" % i))

    def __populateDropdowns(self):
        # TODO: Move this logic to model
        self.tab.dropDownMenuPlugin.addItem("Network Plugin")
        self.tab.dropDownMenuPlugin.addItem("Cryptography Plugin")

        self.tab.dropDownMenuPoi.addItem("Function")
        self.tab.dropDownMenuPoi.addItem("Variable")
        self.tab.dropDownMenuPoi.addItem("String")
        self.tab.dropDownMenuPoi.addItem("DLL")
        self.tab.dropDownMenuPoi.addItem("Struct")
        self.tab.dropDownMenuPoi.addItem("Packet Protocol")

    def __searchForPoi(self):
        print("Search triggered")
        pass

    def __commentWindow(self):
        self.tab.commentView = CommentDialog()
        self.tab.commentView.show()

    def __outputFieldWindow(self):
        self.tab.outputFieldWindow = OutputField()
        self.tab.outputFieldWindow.show()

    def __analysisResultWindow(self):
        self.tab.analysisResultWindow = AnalysisResultDialog()
        self.tab.analysisResultWindow.show()

    def __displayPOI(self):
        items = self.tab.projectList.selectedItems()
        x = []
        for i in range(len(items)):
            x.append(str(self.tab.projectList.selectedItems()[i].text()))
        self.__updatePOI(x)

    def __runStatic(self):
        plugin = self.tab.dropDownMenuPlugin.getCurrent()
        self.tab.poiList.addItems(self.model.getPois(plugin.name))

    def __updatePOI(self, x):
        screen = ""
        for i in range(len(x)):
            screen += x[i] + "\n"
        self.tab.poiContentArea.setPlainText(screen)

    def setProject(self, project):
        self.project = project