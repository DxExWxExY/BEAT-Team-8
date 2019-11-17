from PyQt5.QtWidgets import QLabel, QVBoxLayout, QPushButton, QLineEdit, QComboBox, QListWidget, \
    QTextEdit, QGridLayout, QGroupBox

from src.common.tab_layout import TabLayout


class PluginManagementTab(TabLayout):
    def __init__(self):
        super().__init__("System Plugins", "Plugin Details")
        super().addContentToLeftPanel(self.leftPanelBuilder())
        super().addContentToRightPanel(self.rightPanelBuilder())
        super().build()

    def leftPanelBuilder(self):
        layout = QVBoxLayout()
        self.pluginList = QListWidget()
        self.addPlugin = QPushButton("Add New Plugin")

        layout.addLayout(self.searchBuilder())

        layout.addWidget(self.pluginList)
        layout.addWidget(self.addPlugin)

        return layout

    def poiViewer(self):
        layout = QGridLayout()
        box = QGroupBox("PoI Details")

        self.poiName = QLineEdit()
        self.poiType = QComboBox()
        self.poiMapping = QLineEdit()
        self.addPoi = QPushButton("Add PoI")
        self.deletePoi = QPushButton("Delete PoI")
        self.savePoi = QPushButton("Save PoI")

        layout.addWidget(self.poiName, 1, 1, 1, 2)
        layout.addWidget(QLabel("Seek Name:"), 1, 0)
        layout.addWidget(self.poiType, 2, 1, 1, 2)
        layout.addWidget(QLabel("PoI Type"), 2, 0)
        layout.addWidget(self.poiMapping, 3, 1, 1, 2)
        layout.addWidget(QLabel("Mapping"), 3, 0)
        layout.addWidget(self.addPoi, 4, 0)
        layout.addWidget(self.deletePoi, 4, 1)
        layout.addWidget(self.savePoi, 4, 2)

        box.setLayout(layout)

        return box

    def rightPanelBuilder(self):
        layout = QGridLayout()

        # Plugin Name
        pluginNameLabel = QLabel("Plugin Name")
        self.pluginName = QLineEdit()
        layout.addWidget(pluginNameLabel, 2, 0)
        layout.addWidget(self.pluginName, 2, 1, 1, 9)

        # Plugin Description
        plugingDescriptionLabel = QLabel("Plugin Description")
        self.pluginDescription = QTextEdit()
        layout.addWidget(plugingDescriptionLabel, 3, 0)
        layout.addWidget(self.pluginDescription, 3, 1, 1, 9)

        # Output Field
        outputFieldLabel = QLabel("Output Field")
        self.outputField = QComboBox()
        layout.addWidget(outputFieldLabel, 4, 0)
        layout.addWidget(self.outputField, 4, 1, 1, 9)

        # POI's
        poiLabel = QLabel("Points of Interest")
        self.poiList = QListWidget()

        layout.addWidget(poiLabel, 5, 0)
        layout.addWidget(self.poiList, 5, 1, 1, 3)
        layout.addWidget(self.poiViewer(), 5, 4, 1, 6)

        # Bottom buttons : delete and save
        self.deletePlugin = QPushButton("Delete")
        self.savePlugin = QPushButton("Save")
        layout.addWidget(self.deletePlugin, 6, 8)
        layout.addWidget(self.savePlugin, 6, 9)

        return layout

    def searchBuilder(self):
        layout = QGridLayout()

        self.searchBox = QLineEdit()
        self.searchButton = QPushButton('Search')

        self.searchBox.setPlaceholderText("Search Plugins")

        layout.addWidget(self.searchBox, 0, 0, 1, 4)
        layout.addWidget(self.searchButton, 0, 4, 1, 2)

        return layout
