class ProjectItem():
    def __init__(self, path=""):
        self.id = None
        self.name = ""
        self.description = ""
        self.binaryPath = path
        self.binaryProperties = dict()
        self.results = dict()

    def asDictionary(self):
        if self.id is None:
            return {"name": self.name, "description": self.description, "path": self.binaryPath,
                    "properties": self.binaryProperties, "results": self.results}
        else:
            return {"_id": self.id, "name": self.name, "description": self.description, "path": self.binaryPath,
                    "properties": self.binaryProperties, "results": self.results}
