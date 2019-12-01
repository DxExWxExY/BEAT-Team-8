from src.views.tabs.documentation_tab import DocumentationTab
from src.models.documentation_model import DocumentationModel
from glob import glob , os
class DocumentationTabController:

    def __init__(self):
        self.model = DocumentationModel()
        self.tab = DocumentationTab()
        self.__populateDocumentationList()


    def __populateDocumentationList(self):

        DocumentList=[]
        for path, subdirs, files in os.walk("src/Documentation"):
            for doc in files:

                doc = doc.replace(".html",'')

                self.tab.documentationList.addItem(doc)
                print("files:", doc,"\n")


    def __addEventHandlers(self):
        pass

    def __updateUI(self):
        pass

    def __searchForDocument(self):
        pass