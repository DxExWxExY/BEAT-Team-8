class ProjectItem():
    def __init__(self, path="", name="New Project"):
        self.name = name
        self.description = ""
        self.binaryPath = path
        self.binaryProperties = dict()

    def hasBinaryAttributes(self):
        return self.binaryProperties

