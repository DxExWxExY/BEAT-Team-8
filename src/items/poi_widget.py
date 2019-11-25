from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QGridLayout, QCheckBox, QLabel, QSizePolicy


class PoIWidget(QWidget):
    def __init__(self, poi):
        super().__init__()

        self.poi = poi
        layout = QGridLayout()

        self.check = QCheckBox('BP')
        name = QLabel(self.poi['name'])

        name.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        name.setAlignment(Qt.AlignLeft)

        layout.addWidget(self.check, 0, 0)
        layout.addWidget(name , 0, 1)
        layout.setAlignment(name, Qt.AlignLeft)

        self.setLayout(layout)

    def __contains__(self, item):
        return self.poi['name'] == item['name']
