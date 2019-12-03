from src.views.dialogs.documentation_dialog import DocumentationDialog
from src.models.documentation_model import DocumentationModel


class DocumentationController:

    def __init__(self):
        self.model = DocumentationModel()
        self.dialog = DocumentationDialog()
        self.__addEventHandlers()
        self.__populateDocumentationList()

    def __populateDocumentationList(self):
        documentsList = self.model.getDocumentationList()
        for i in range(len(documentsList)):
            self.dialog.documentationList.addItem(documentsList[i])

    def __addEventHandlers(self):
        self.dialog.documentationList.itemSelectionChanged.connect(lambda: self.__readDoc())
        self.dialog.searchBox.returnPressed.connect(lambda: self.__searchForDocument())
        self.dialog.searchButton.clicked.connect(lambda: self.__searchForDocument())
        pass

    def __readDoc(self):
        name = "./res/Documentation/"
        name += self.dialog.documentationList.currentItem().text() + "/" + self.dialog.documentationList.currentItem().text()
        name += ".html"
        try:
            contents = open(name).read()
        except Exception as err:
            contents = "<html><h1 align=center >Problem Reading Html. Html May Not Exist</h1></html>"
        # print(name)
        self.dialog.content.setHtml(contents)
        self.dialog.content.setReadOnly(True)

    def __searchForDocument(self):
        searchText = self.dialog.searchBox.text().lower()
        if searchText is "":
            self.dialog.documentationList.clear()
            self.__populateDocumentationList()
        else:
            documents = self.model.getDocumentationList()
            for i in range(len(documents)):
                if searchText in documents[i].lower():
                    self.dialog.documentationList.clear()
                    self.dialog.documentationList.addItem(documents[i])
                    print(documents[i])