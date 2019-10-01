from PyQt5.QtWidgets import QListWidgetItem

from src.views.dialogs.analysis_result_dialog import AnalysisResultDialog
from src.views.dialogs.comment_dialog import CommentDialog
from src.views.dialogs.output_field_dialog import OutputField
from src.views.tabs.analysis_tab import AnalysisTab


class AnalysisTabController:
    def __init__(self):
        self.tab = AnalysisTab()
        # self.model = AnalysisModel()
        self.__addEventHandlers()
        self.__populateList()

    def __addEventHandlers(self):
        self.tab.projectList.itemClicked.connect(lambda: self.__displayPOI())
        self.tab.searchBox.returnPressed.connect(lambda: self.__searchForItem())
        self.tab.searchButton.clicked.connect(lambda: self.__searchForItem())
        self.tab.commentBtn.clicked.connect(lambda: self.__commentWindow())
        self.tab.analysisResultBtn.clicked.connect(lambda: self.__analysisResultWindow())
        self.tab.outputFieldViewBtn.clicked.connect(lambda: self.__outputFieldWindow())

    def __populateList(self):
        # TODO: Move this logic to model
        for i in range(4):
            self.tab.projectList.addItem(QListWidgetItem("Item %i" % i))

    def __searchForItem(self):
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

    def __updatePOI(self, x):
        screen = ""
        for i in range(len(x)):
            screen += x[i] + "\n"
        self.tab.poiContentArea.setPlainText(screen)