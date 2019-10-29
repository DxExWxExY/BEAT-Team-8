class PluginItem:
    def __init__(self):
        self.id = None
        self.name = "New Plugin"
        self.description = ""
        self.outputFields = []
        self.pois = []
        self.types = []

    def asDictionary(self):
        if self.id is None:
            return {"name": self.name, "description": self.description, "fields": self.outputFields, "pois": self.pois,
                    "types": self.types}
        else:
            return {"_id": self.id, "name": self.name, "description": self.description, "fields": self.outputFields,
                    "pois": self.pois, "types": self.types}
