import os

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
        self.dialog.saveButton.clicked.connect(lambda: self.__saveDocument())
        self.dialog.editButton.clicked.connect(lambda: self.__editDocument())
        pass

    def __readDoc(self):
        flag = False
        name = "./res/Documentation/"
        name += self.dialog.documentationList.currentItem().text() + "/" + self.dialog.documentationList.currentItem().text()
        name += ".html"
        try:
            with open(name, "r") as f:
                contents = f.read()
                f.close()
            self.dialog.content.setHtml(contents)
            flag = True
        except Exception:
            pass
        try:
            name = "./res/Documentation/"
            name += self.dialog.documentationList.currentItem().text()
            name += ".html"
            with open(name, "r") as f:
                contents = f.read()
                f.close()
            self.dialog.content.setHtml(contents)
            flag = True
        except Exception:
            pass
        try:
            name = "./res/Documentation/"
            name += self.dialog.documentationList.currentItem().text() + "/" + self.dialog.documentationList.currentItem().text()
            name += ".txt"
            with open(name, "r") as f:
                contents = f.read()
                f.close()
            self.dialog.content.setText(contents)
            flag = True
        except Exception:
            pass
        try:
            name = "./res/Documentation/"
            name += self.dialog.documentationList.currentItem().text()
            name += ".txt"
            with open(name, "r") as f:
                contents = f.read()
                f.close()
            self.dialog.content.setText(contents)
            flag = True
        except Exception:
            pass
        # print(name)
        if not flag:
            contents = "<html><h1 align=center >Problem Reading Html. Html May Not Exist</h1></html>"
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

    def __saveDocument(self):
        name = "./res/Documentation/"
        name += self.dialog.documentationList.currentItem().text() + "/" + self.dialog.documentationList.currentItem().text()
        name += ".html"
        try:
            if os.path.exists(name):
                self.dialog.error_message.showMessage("Can only edit text files here.")
        except Exception:
            pass
        try:
            name = "./res/Documentation/"
            name += self.dialog.documentationList.currentItem().text()
            name += ".html"
            if os.path.exists(name):
                self.dialog.error_message.showMessage("Can only edit text files here.")
        except Exception:
            pass
        try:
            name = "./res/Documentation/"
            name += self.dialog.documentationList.currentItem().text() + "/" + self.dialog.documentationList.currentItem().text()
            name += ".txt"
            if os.path.exists(name):
                contents = self.dialog.content.toPlainText()
                with open(name, "w") as f:
                    f.write(contents)
                    f.close()
        except Exception:
            pass
        try:
            name = "./res/Documentation/"
            name += self.dialog.documentationList.currentItem().text()
            name += ".txt"
            if os.path.exists(name):
                contents = self.dialog.content.toPlainText()
                with open(name, "w") as f:
                    print(contents)
                    f.write(contents)
                    f.close()
        except Exception:
            pass
        # print(name)
        self.dialog.content.setReadOnly(True)
        self.dialog.saveButton.setEnabled(False)
        self.dialog.editButton.setEnabled(True)
        self.dialog.repaint()

    def __editDocument(self):
        self.dialog.content.setReadOnly(False)
        self.dialog.saveButton.setEnabled(True)
        self.dialog.editButton.setEnabled(False)
        self.dialog.repaint()
