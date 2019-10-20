from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog, QTableWidgetItem

from src.models.project_model import ProjectModel
from src.views.tabs.project_tab import ProjectTab


class ProjectTabController:
    def __init__(self):
        self.tab = ProjectTab()
        self.model = ProjectModel()
        self.__addEventHandlers()
        self.__populateProjectList()

    def __populateProjectList(self):
        for item in self.model.getProjectList():
            self.tab.projectList.addItem(item.name)

    def __addEventHandlers(self):
        self.tab.browsePath.clicked.connect(lambda: self.__fileBrowser())
        self.tab.searchBox.returnPressed.connect(lambda: self.__searchForItem())
        self.tab.searchButton.clicked.connect(lambda: self.__searchForItem())
        self.tab.addProjectButton.clicked.connect(lambda: self.__addProject())
        self.tab.projectList.itemSelectionChanged.connect(lambda: self.__updateUI())
        self.tab.saveButton.clicked.connect(lambda: self.__saveProject())
        self.tab.deleteButton.clicked.connect(lambda: self.__deleteProject())

    def __updateUI(self):
        selectedItem = self.model.getSelectedProject(self.__getCurrentIndex())
        self.tab.projectName.setText(selectedItem.name)
        self.tab.projectDescription.setText(selectedItem.description)
        self.tab.binPath.setText(selectedItem.binaryPath)
        if selectedItem.hasBinaryAttributes():
            self.tab.table.setItem(0, 1, QTableWidgetItem(selectedItem.binaryProperties['os']))
            self.tab.table.setItem(1, 1, QTableWidgetItem(selectedItem.binaryProperties['arch']))
            self.tab.table.setItem(2, 1, QTableWidgetItem(selectedItem.binaryProperties['machine']))
            self.tab.table.setItem(3, 1, QTableWidgetItem(selectedItem.binaryProperties['class']))
            self.tab.table.setItem(4, 1, QTableWidgetItem(selectedItem.binaryProperties['bits']))
            self.tab.table.setItem(5, 1, QTableWidgetItem(selectedItem.binaryProperties['lang']))
            self.tab.table.setItem(6, 1, QTableWidgetItem(selectedItem.binaryProperties['canary']))
            self.tab.table.setItem(7, 1, QTableWidgetItem(selectedItem.binaryProperties['crypto']))
            self.tab.table.setItem(8, 1, QTableWidgetItem(selectedItem.binaryProperties['nx']))
            self.tab.table.setItem(9, 1, QTableWidgetItem(selectedItem.binaryProperties['pic']))
            self.tab.table.setItem(10, 1, QTableWidgetItem(selectedItem.binaryProperties['relocs']))
            self.tab.table.setItem(11, 1, QTableWidgetItem(selectedItem.binaryProperties['relro']))
            self.tab.table.setItem(12, 1, QTableWidgetItem(selectedItem.binaryProperties['stripped']))

    def __populateTable(self):
        selectedItem = self.model.getSelectedProject(self.__getCurrentIndex())


    def __fileBrowser(self):
        callback = QFileDialog.getOpenFileName()
        if callback:
            self.tab.binPath.setText(str(callback[0]))

    def __searchForItem(self):
        print("Search triggered")

    def __getCurrentIndex(self):
        i = self.tab.projectList.indexFromItem(self.tab.projectList.currentItem()).row()
        return i

    def __saveProject(self):
        selectedItem = self.model.getSelectedProject(self.__getCurrentIndex())
        selectedItem.name = self.tab.projectName.text()
        selectedItem.description = self.tab.projectDescription.toPlainText()
        selectedItem.binaryPath = self.tab.binPath.text()
        self.__updateUI()
        index = self.__getCurrentIndex()
        self.tab.projectList.clear()
        self.__populateProjectList()
        self.tab.projectList.setCurrentRow(index)
        self.model.saveProject(index)

    def __deleteProject(self):
        self.model.deleteProject(self.__getCurrentIndex())
        self.tab.projectList.clear()
        self.__populateProjectList()

    def __addProject(self):
        callback = QFileDialog.getOpenFileName()
        try:
            if callback:
                self.model.addProject(str(callback[0]))
                self.tab.projectList.clear()
                self.__populateProjectList()
            self.tab.projectList.setCurrentRow(self.tab.projectList.count() - 1)
        except:
            errorDialog = QtWidgets.QMessageBox()
            errorDialog.setText('Unsupported File')
            errorDialog.setWindowTitle("Error")
            errorDialog.setInformativeText("The selected file is not ELF x86 or PE x86")
            errorDialog.setIcon(3)
            errorDialog.exec_()

    def getCurrentProject(self):
        return self.model.getSelectedProject(self.__getCurrentIndex())
