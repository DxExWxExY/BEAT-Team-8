class PluginItem:
    def __init__(self, n):
        self.structurePath = f"Path {n}"
        self.dataSetPath = f"Path {n}"
        self.name = f"Plugin {n}"
        self.description = f"Description {n}"
        self.outputFields = ["Output Type X"]
        self.pois = [f"PoI {n}" for n in range(5)]