from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QVBoxLayout, QListWidget, QPushButton, QGridLayout, QLabel, QComboBox, QLineEdit, \
    QSpacerItem, QSizePolicy, QTextEdit

from common.tab_layout import TabLayout


class PointsOfInterestTab(TabLayout):
    def __init__(self):
        super().__init__("Points of Interest View", "Detailed Points of Interest View")
        super().addContetentToLeftPanel(self.leftPanelBuilder())
        super().addContetentToRightPanel(self.rightPanelBuilder())
        super().build()

    def leftPanelBuilder(self):
        layout = QVBoxLayout()
        poiList = QListWidget()
        addPoiButton = QPushButton('New Point of Interest')

        poiList.addItem("Point of Interest 1")
        poiList.addItem("Point of Interest 2")
        poiList.addItem("Point of Interest 3")
        poiList.addItem("Point of Interest 4")

        layout.addLayout(self.searchBuilder())
        layout.addWidget(poiList)
        layout.addWidget(addPoiButton)

        return layout

    def rightPanelBuilder(self):
        layout = QGridLayout()

        existingPluginsDropdown = QComboBox()
        typeDropdown = QComboBox()
        content = QTextEdit()

        existingPluginsDropdown.addItems(["Plugin 1", "Plugin 2", "Plugin 3"])
        typeDropdown.addItems(["Type 1", "Type 2", "Type 3"])

        layout.addWidget(QLabel("Plugin"), 0, 0, Qt.AlignRight)
        layout.addWidget(QLabel("Point of Interest Type"), 1, 0, Qt.AlignRight)
        layout.addWidget(existingPluginsDropdown, 0, 1)
        layout.addWidget(typeDropdown, 1, 1)

        spacer = QSpacerItem(1, 1, QSizePolicy.Expanding)

        layout.addWidget(content, 2, 0, 1, 6)

        layout.setContentsMargins(100, 0, 100, 0)
        layout.addItem(spacer, 0, 1, 1, 5)
        layout.addItem(spacer, 1, 1, 1, 5)

        return layout

    def searchBuilder(self):
        layout = QGridLayout()

        searchBox = QLineEdit()
        searchBox.setPlaceholderText("Search Projects")
        searchBox.returnPressed.connect(lambda: print("Enter Detected"))

        searchButton = QPushButton('Search')

        layout.addWidget(searchBox, 0, 0, 1, 4)
        layout.addWidget(searchButton, 0, 4, 1, 2)

        return layout
