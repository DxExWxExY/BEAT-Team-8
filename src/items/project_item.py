import os


class ProjectItem():
    def __init__(self, n):
        super().__init__()
        self.name = f"Project {n}"
        self.description = f"{n}"
        self.binaryPath = "dlakjslk"
        self.binaryProperties = dict()

    def hasBinaryAttributes(self):
        return self.binaryProperties

