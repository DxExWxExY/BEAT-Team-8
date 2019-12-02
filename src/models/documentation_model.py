import os


class DocumentationModel:
    def __init__(self):
        self.documents = []
        self.__loadDocuments()

    def __loadDocuments(self):
        for path, subdirs, files in os.walk("src/Documentation"):
            for doc in files:
                if "html" in doc:
                    doc = doc.replace(".html", '')
                    self.documents.append(doc)
                    # print("files:", doc, "\n")

    def getDocumentationList(self):
        return self.documents

    def getSelectedDocument(self, i):
        pass