from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLabel, QVBoxLayout, QPushButton, QLineEdit, QComboBox, QListWidget, \
    QTextEdit, QGridLayout

from src.common.tab_layout import TabLayout


class PluginManagementTab(TabLayout):
    list = ["plugin1"]
    pois = ["PoI a", "PoI b", "PoI c"]
    current = None

    def __init__(self):
        super().__init__("Plugin View", "Detailed Plugin View")
        super().addContentToLeftPanel(self.leftPanelBuilder())
        super().addContentToRightPanel(self.rightPanelBuilder())
        super().build()

    def leftPanelBuilder(self):
        layout = QVBoxLayout()
        pluginList = QListWidget()
        addPlugin = QPushButton("Add New Plugin")

        layout.addLayout(self.searchBuilder())

        pluginList.addItem("Plugin 1")

        layout.addWidget(pluginList)
        layout.addWidget(addPlugin)

        return layout

    def rightPanelBuilder(self):
        layout = QGridLayout()

        # Plugin Structure
        pluginStructureLabel = QLabel("Plugin Structure")
        self.pluginStructurePath = QLineEdit("C:/plugin_structure.xml")
        browseStructurePath = QPushButton("Browse")
        browseStructurePath.clicked.connect(lambda: self.fileBrowser(self.pluginStructurePath))
        layout.addWidget(pluginStructureLabel, 0, 0)
        layout.addWidget(self.pluginStructurePath, 0, 1, 1, 8)
        layout.addWidget(browseStructurePath, 0, 9)

        # Predefined Data Set
        dataSetLabel = QLabel("Predefined Data Set")
        self.dataSetPath = QLineEdit("C:/plugin_data_set.xml")
        browseDataPath = QPushButton("Browse")
        browseDataPath.clicked.connect(lambda: self.fileBrowser(self.dataSetPath))
        layout.addWidget(dataSetLabel, 1, 0)
        layout.addWidget(self.dataSetPath, 1, 1, 1, 8)
        layout.addWidget(browseDataPath, 1, 9)

        # Plugin Name
        pluginNameLabel = QLabel("Plugin Name")
        pluginName = QLineEdit("Network")
        layout.addWidget(pluginNameLabel, 2, 0)
        layout.addWidget(pluginName, 2, 1, 1, 9)

        # Plugin Description
        plugingDescriptionLabel = QLabel("Plugin Description")
        pluginDescription = QTextEdit("Plugin used to detect network behaviors in binaries")
        layout.addWidget(plugingDescriptionLabel, 3, 0)
        layout.addWidget(pluginDescription, 3, 1, 1, 9)

        # Output Field
        outputFieldLabel = QLabel("Output Field")
        outputField = QComboBox()
        # TODO: add from some kind of list
        outputField.addItems(["Python File", "Other"])
        layout.addWidget(outputFieldLabel, 4, 0)
        layout.addWidget(outputField, 4, 1, 1, 9)

        # POI's
        poiLabel = QLabel("Points of Interest")
        poiList = QListWidget()
        for item in self.pois:
            poiList.addItem(str(item))
        layout.addWidget(poiLabel, 5, 0)
        layout.addWidget(poiList, 5, 1, 1, 9)

        # Bottom buttons : delete and save
        deletePlugin = QPushButton("Delete")
        savePlugin = QPushButton("Save")
        layout.addWidget(deletePlugin, 6, 8)
        layout.addWidget(savePlugin, 6, 9)

        return layout

    def searchBuilder(self):
        layout = QGridLayout()

        searchBox = QLineEdit()
        searchBox.setPlaceholderText("Search Plugins")
        searchBox.returnPressed.connect(lambda: print("Enter Detected"))

        searchButton = QPushButton('Search')

        layout.addWidget(searchBox, 0, 0, 1, 4)
        layout.addWidget(searchButton, 0, 4, 1, 2)

        return layout

    def __searchPlugin(self, str):
        print("At least you entered something \\(\'\'/)/")
        return str

    def __editName(self):
        print("edit name")

    def __findPlugin(self, str):
        for item in self.list:
            if item == str:
                self.current = item
                print(self.current)
