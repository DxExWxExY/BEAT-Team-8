class ProjectItem():
    def __init__(self):
        self.name = ""
        self.description = ""
        self.binaryPath = ""
        self.binaryProperties = dict()

    def hasBinaryAttributes(self):
        return self.binaryProperties

