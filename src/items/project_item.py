class ProjectItem():
    def __init__(self, n):
        super().__init__()
        self.name = f"Project {n}"
        self.description = f"{n}"
        self.binaryPath = f"{n}"
        self.binaryProperties = dict()

    def hasBinaryAttributes(self):
        return len(self.binaryProperties) > 0
#         TODO: Add Missing fields
