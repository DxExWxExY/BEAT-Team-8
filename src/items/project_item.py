from bson import ObjectId


class ProjectItem():
    def __init__(self, path="", name="New Project"):
        self.id = ObjectId()
        self.name = name
        self.description = ""
        self.binaryPath = path
        self.binaryProperties = dict()

    def asDictionary(self):
        return {"name": self.name, "description": self.description, "path": self.binaryPath, "properties": self.binaryProperties}
