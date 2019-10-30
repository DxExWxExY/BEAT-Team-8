from PyQt5 import QtWidgets

from src.models.analysis_model import AnalysisModel
from src.views.dialogs.analysis_result_dialog import AnalysisResultDialog
from src.views.dialogs.comment_dialog import CommentDialog
from src.views.dialogs.output_field_dialog import OutputField
from src.views.tabs.analysis_tab import AnalysisTab


class AnalysisTabController:
    def __init__(self):
        self.tab = AnalysisTab()
        self.project = None
        self.model = AnalysisModel()
        self.__addEventHandlers()
        self.__populateList()
        self.__populateDropdowns()

    def __addEventHandlers(self):
        self.tab.poiList.itemClicked.connect(lambda: self.__displayPOI())
        self.tab.searchBox.returnPressed.connect(lambda: self.__searchForPoi())
        self.tab.searchButton.clicked.connect(lambda: self.__searchForPoi())
        self.tab.commentBtn.clicked.connect(lambda: self.__commentWindow())
        self.tab.analysisResultBtn.clicked.connect(lambda: self.__analysisResultWindow())
        self.tab.outputFieldViewBtn.clicked.connect(lambda: self.__outputFieldWindow())
        self.tab.staticRunBtn.clicked.connect(lambda : self.__runStatic())
        self.tab.dropDownMenuPoi.currentIndexChanged.connect(lambda : self.__populateList())
        self.tab.dropDownMenuPlugin.currentIndexChanged.connect(lambda: self.__selectPlugin())
        self.tab.dynamicRunbtn.clicked.connect(lambda: self.__runDynamic())

    def __populateList(self):
        filter = str(self.tab.dropDownMenuPoi.currentText())
        self.tab.poiList.clear()
        list = []
        if filter != "":
            list = self.model.setFilterList(filter)

        for item in list:
            self.tab.poiList.addItem(item)

    def __selectPlugin(self):
        selected = self.tab.dropDownMenuPlugin.currentText()
        if selected in "Select Plugin":
            self.tab.dropDownMenuPoi.setEnabled(False)
            self.tab.staticRunBtn.setEnabled(False)
            self.tab.dynamicRunbtn.setEnabled(False)
            self.tab.dynamicStopbtn.setEnabled(False)
            self.tab.dropDownMenuPoi.clear()
            self.tab.poiContentArea.clear()
        else:
            self.tab.dropDownMenuPoi.setEnabled(True)
            self.tab.staticRunBtn.setEnabled(True)
            self.tab.dynamicRunbtn.setEnabled(True)
            self.tab.dynamicStopbtn.setEnabled(True)
            self.tab.dropDownMenuPoi.clear()
            self.tab.dropDownMenuPoi.addItems(self.model.getPluginFilters(selected))

    def __populateDropdowns(self):
        self.tab.dropDownMenuPlugin.addItems(self.model.getPluginsList())

    def __searchForPoi(self):
        searchText = self.tab.searchBox.text().lower()
        if searchText is "":
            self.tab.poiList.clear()
            self.__populateList()
        else:
            searchList = []
            for poiType in self.model.getPoiList().keys():
                for poiName in self.model.getPoiList()[poiType]:
                    if searchText in poiName.lower():
                        searchList.append(poiName)
            self.tab.poiList.clear()
            for item in searchList:
                self.tab.poiList.addItem(item)

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
        items = self.tab.poiList.selectedItems()
        x = []
        for i in range(len(items)):
            x.append(str(self.tab.poiList.selectedItems()[i].text()))
        self.__updatePOI(x)

    def __runStatic(self):
        if self.project is not None:
            self.model.run_static(self.project.binaryPath)
            self.__updateTerminal()
            self.__populateList()
        else:
            errorDialog = QtWidgets.QMessageBox()
            errorDialog.setText('Project Not Selected')
            errorDialog.setWindowTitle("Error")
            errorDialog.setInformativeText("Select a project from the Project Tab.")
            errorDialog.setIcon(3)
            errorDialog.exec_()

    def __updatePOI(self, x):
        screen = ""
        for i in range(len(x)):
            screen += x[i] + "\n"
        self.tab.poiContentArea.setPlainText(screen)

    def __updateTerminal(self):
        self.tab.terminalContent.appendPlainText(self.model.getTerminalOutput())

    def setProject(self, project):
        self.project = project

    def __runDynamic(self):
        if self.project is not None:
            # TODO: Replace with dynamic stuff
            # self.model.run_static(self.project.binaryPath)
            # self.__updateTerminal()
            # self.__populateList()
            pass
        else:
            errorDialog = QtWidgets.QMessageBox()
            errorDialog.setText('Project Not Selected')
            errorDialog.setWindowTitle("Error")
            errorDialog.setInformativeText("Select a project from the Project Tab.")
            errorDialog.setIcon(3)
            errorDialog.exec_()