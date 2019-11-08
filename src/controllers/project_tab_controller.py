from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QFileDialog, QTableWidgetItem, QMessageBox

from src.models.project_model import ProjectModel
from src.views.dialogs.prjInfoDialog import prjInfoDialog
from src.views.dialogs.project_selection_dialog import ProjectSelection


class ProjectTabController:
    def __init__(self):
        self.model = ProjectModel()
        self.projectSelection = ProjectSelection()
        self.newProjectDialog = prjInfoDialog()
        self.project = None
        self.__addEventHandlers()
        self.__populateProjectList()

    def __populateProjectList(self):
        for item in self.model.getProjectList().keys():
            self.projectSelection.projectsList.addItem(item)

    def __addEventHandlers(self):
        # self.tab.browsePath.clicked.connect(lambda: self.__fileBrowser())
        # self.tab.searchBox.returnPressed.connect(lambda: self.__searchForItem())
        # self.tab.searchButton.clicked.connect(lambda: self.__searchForItem())
        #     Dialog Handlers
        self.newProjectDialog.createButton.clicked.connect(lambda: self.__saveProject())
        self.newProjectDialog.createButton.clicked.connect(lambda: self.__saveProject())
        self.projectSelection.deleteProject.clicked.connect(lambda: self.__deleteProject())
        self.projectSelection.addProject.clicked.connect(lambda: self.__addProject())
        self.projectSelection.openProject.clicked.connect(lambda: self.__openProject())

    def __projectProperties(self):
        self.project = self.newProjectDialog.newItem
        self.newProjectDialog.binPath.setText(self.project.binaryPath)
        self.newProjectDialog.table.setItem(0, 1, QTableWidgetItem(self.project.binaryProperties['os']))
        self.newProjectDialog.table.setItem(1, 1, QTableWidgetItem(self.project.binaryProperties['arch']))
        self.newProjectDialog.table.setItem(2, 1, QTableWidgetItem(self.project.binaryProperties['machine']))
        self.newProjectDialog.table.setItem(3, 1, QTableWidgetItem(self.project.binaryProperties['class']))
        self.newProjectDialog.table.setItem(4, 1, QTableWidgetItem(self.project.binaryProperties['bits']))
        self.newProjectDialog.table.setItem(5, 1, QTableWidgetItem(self.project.binaryProperties['lang']))
        self.newProjectDialog.table.setItem(6, 1, QTableWidgetItem(self.project.binaryProperties['canary']))
        self.newProjectDialog.table.setItem(7, 1, QTableWidgetItem(self.project.binaryProperties['crypto']))
        self.newProjectDialog.table.setItem(8, 1, QTableWidgetItem(self.project.binaryProperties['nx']))
        self.newProjectDialog.table.setItem(9, 1, QTableWidgetItem(self.project.binaryProperties['pic']))
        self.newProjectDialog.table.setItem(10, 1, QTableWidgetItem(self.project.binaryProperties['relocs']))
        self.newProjectDialog.table.setItem(11, 1, QTableWidgetItem(self.project.binaryProperties['relro']))
        self.newProjectDialog.table.setItem(12, 1, QTableWidgetItem(self.project.binaryProperties['stripped']))

    def __fileBrowser(self):
        callback = QFileDialog.getOpenFileName()
        if callback:
            self.newProjectDialog.binPath.setText(str(callback[0]))

    def __searchForItem(self):
        searchText = self.tab.searchBox.text().lower()
        # When search is triggered with an empty string clear the list
        if searchText is "":
            self.tab.projectList.clear()
            self.__populateProjectList()
        else:
            # get all the items with substring of searched string
            searches = []
            for projectName in self.model.getProjectList().keys():
                if searchText in projectName.lower():
                    searches.append(projectName)
            # add those items with substring into the list
            self.tab.projectList.clear()
            for s in searches:
                self.tab.projectList.addItem(s)

    def __getCurrentIndex(self):
        return self.projectSelection.projectsList.currentItem().text()

    def __saveProject(self):
        self.newProjectDialog.newItem.name = self.newProjectDialog.projectName.text()
        self.model.saveProject(self.newProjectDialog.newItem)
        self.__populateProjectList()
        self.__clear()
        self.newProjectDialog.close()

    def __deleteProject(self):
        buttonReply = QMessageBox.question(self.projectSelection, 'Delete Project', "Are you sure you want to delete this project?",
                                           QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if buttonReply == QMessageBox.Yes:
            self.model.deleteProject(self.__getCurrentIndex())
            self.projectSelection.projectsList.clear()
            self.__populateProjectList()

    def __addProject(self):
        path, response = QFileDialog.getOpenFileName(self.projectSelection)
        try:
            if response:
                self.newProjectDialog.newItem = self.model.verifyBinary(path)
                self.__projectProperties()
                self.newProjectDialog.exec_()
                self.project = self.newProjectDialog.newItem
                self.__openProject()
        except KeyError:
            errorDialog = QtWidgets.QMessageBox()
            errorDialog.setText('Unsupported File')
            errorDialog.setWindowTitle("Error")
            errorDialog.setInformativeText("The selected file is not ELF x86 or PE x86")
            errorDialog.setIcon(3)
            errorDialog.exec_()

    def getCurrentProject(self):
        return self.project

    def __openProject(self):
        self.project = self.model.getSelectedProject(self.__getCurrentIndex())
        self.projectSelection.close()

    def __clear(self):
        self.newProjectDialog.projectName.clear()
        self.newProjectDialog.binPath.clear()
        for i in range(12):
            self.newProjectDialog.table.setItem(i, 1, QTableWidgetItem(''))
