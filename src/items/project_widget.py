from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel, QPushButton


class ProjectWidget(QWidget):
    def __init__(self, project):
        super().__init__()

        self.project = project

        layout = QGridLayout()

        self.name = QLabel()
        self.info = QPushButton("Details")

        # self.

        layout.addWidget(self.name, 0, 0)
        layout.addWidget(self.info, 0, 1)

        self.setLayout(layout)

