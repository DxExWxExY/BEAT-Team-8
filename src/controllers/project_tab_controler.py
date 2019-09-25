from PyQt5.QtWidgets import QFileDialog

from src.views.tabs.project_tab import ProjectTab


class PojoectTabController:
    def __init__(self):
        self.tab = ProjectTab()
        # self.model = ProjectModel()

    def __populateList(self):
        pass

    def __addEventHandlers(self):
        self.tab.browsePath.clicked.connect(lambda: self.fileBrowser(self.tab.binPath))
        pass

    def fileBrowser(self, textBox):
        callback = QFileDialog.getOpenFileName()
        if callback:
            textBox.setText(str(callback[0]))