from src.views.tabs.documentation_tab import DocumentationTab
from src.models.documentation_model import DocumentationModel
from glob import os
class DocumentationTabController:

    def __init__(self):
        self.model = DocumentationModel()
        self.tab = DocumentationTab()
        self.__addEventHandlers()
        self.__populateDocumentationList()

    def __populateDocumentationList(self):
        documentsList = self.model.getDocumentationList()
        for i in range(len(documentsList)):
            self.tab.documentationList.addItem(documentsList[i])


    def __addEventHandlers(self):
        self.tab.searchBox.returnPressed.connect(lambda: self.__searchForDocument())
        self.tab.searchButton.clicked.connect(lambda: self.__searchForDocument())
        pass

    def __updateDoc(self):
        pass

    def __searchForDocument(self):
        searchText = self.tab.searchBox.text().lower()
        if searchText is "":
            self.tab.documentationList.clear()
            self.__populateDocumentationList()
        else:
            documents = self.model.getDocumentationList()
            for i in range(len(documents)):
                if searchText in documents[i]:
                    self.tab.documentationList.clear()
                    self.tab.documentationList.addItem(documents[i])
                    # print(documents[i])
