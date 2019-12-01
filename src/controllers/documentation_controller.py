from src.views.tabs.documentation_tab import DocumentationTab
from src.models.documentation_model import DocumentationModel
from glob import glob , os
class DocumentationTabController:

    def __init__(self):
        self.model = DocumentationModel()
        self.tab = DocumentationTab()
        self.__populateDocumentationList()


    def __populateDocumentationList(self):

        self.tab.documentationList.addItem("BEAT Documentation")
        self.tab.documentationList.addItem("BEAT Documentation2")

    #     get all folder names
        os.chdir("src/Documentation")
        documents = glob('*/')
        for i in range(len(documents)):
            documents[i] = documents[i].replace('/', '')
        print(documents)

    #     get all html names
        for file in documents:
            path = "src/Documentation/"
            path += file
            path += "/"

            print(path,"____________")
            os.chdir(path)

        # htmlFiles = glob.glob("*.html")
        # print(htmlFiles)




    def __addEventHandlers(self):
        pass

    def __updateUI(self):
        pass

    def __searchForDocument(self):
        pass