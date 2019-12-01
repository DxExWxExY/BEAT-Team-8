from src.views.tabs.documentation_tab import DocumentationTab
from src.models.documentation_model import DocumentationModel
from glob import os
class DocumentationTabController:

    def __init__(self):
        self.model = DocumentationModel()
        self.tab = DocumentationTab()
        self.documents = []
        self.__addEventHandlers()
        self.__populateDocumentationList()

    def __populateDocumentationList(self):

        for path, subdirs, files in os.walk("src/Documentation"):
            for doc in files:
                doc = doc.replace(".html", '')
                self.tab.documentationList.addItem(doc)
                self.documents.append(doc)
                # print("files:", doc, "\n")


    def __addEventHandlers(self):
        self.tab.searchBox.returnPressed.connect(lambda: self.__searchForDocument())
        self.tab.searchButton.clicked.connect(lambda: self.__searchForDocument())
        pass

    def __updateUI(self):
        pass

    def __searchForDocument(self):
        searchText = self.tab.searchBox.text().lower()
        if searchText is "":
            self.tab.documentationList.clear()
            self.__populateDocumentationList()
        else:
            for i in range(len(self.documents)):
                if searchText in self.documents[i]:
                    self.tab.documentationList.clear()
                    self.tab.documentationList.addItem(self.documents[i])
                    print(self.documents[i])
