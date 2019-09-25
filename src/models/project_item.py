from PyQt5.QtWidgets import QListWidgetItem


class ProjectItem(QListWidgetItem):
    def __init__(self, n):
        super().__init__()
        self.name = f"Project {n}"
        self.description = f"{n}"
        self.binaryPath = f"{n}"
        self.binaryProperties = [f"{n}"]
#         TODO: Add Missing fields

