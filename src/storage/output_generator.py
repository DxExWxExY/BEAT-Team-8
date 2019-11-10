import jinja2

class OutputGeneration():
    global file

    def __init__(self):
        pass

    # function for user to enter their own lines of code.
    def createForm(self):
        pass

    def __createFile(self, name, fileType):
        fileName = name + fileType
        self.file = open(fileName, "w")

    # generate strings, structs, variables.
    def __generateVars(self):

    