from bson import ObjectId


class ProjectItem():
    def __init__(self, path="", name="New Project"):
        self.id = None
        self.name = name
        self.description = ""
        self.binaryPath = path
        self.binaryProperties = dict()

    def asDictionary(self):
        return {"_id": self.id, "name": self.name, "description": self.description, "path": self.binaryPath, "properties": self.binaryProperties}
