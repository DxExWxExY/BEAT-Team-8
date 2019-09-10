from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLabel, QVBoxLayout, QPushButton, QLineEdit, QComboBox, QListWidget, \
    QTextEdit, QGridLayout

from common.tab_layout import TabLayout


class PluginManagementTab(TabLayout):
    list = ["plugin1"]  # something of function to find list of plugin
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
        search = QLineEdit()
        new_plugin = QPushButton("New")

        search.setPlaceholderText("Search Plugin...")
        layout.addWidget(search)
        # TODO: Refactor to events
        if search.returnPressed:
            if search.text == '':
                print("Please enter text")
            else:
                print(search.text)
                # self.__searchPlugin(search.text)

        pluginList.addItem("Plugin 1")

        layout.addWidget(pluginList)
        layout.addWidget(new_plugin)

        return layout

    def rightPanelBuilder(self):
        layout = QGridLayout()

        # Plugin Structure
        ps_title = QLabel("Plugin Structure")
        ps_title.setAlignment(Qt.AlignRight)
        self.ps_path = QLineEdit("C:/plugin_structure.xml")
        ps_edit = QPushButton("Browse")
        ps_edit.clicked.connect(lambda: self.fileBrowser(self.ps_path))
        layout.addWidget(ps_title, 0, 0)
        layout.addWidget(self.ps_path, 0, 1)
        layout.addWidget(ps_edit, 0, 2)

        # Predefined Data Set
        ds_title = QLabel("Predefined Data Set")
        ds_title.setAlignment(Qt.AlignRight)
        self.ds_path = QLineEdit("C:/plugin_data_set.xml")
        ds_edit = QPushButton("Browse")
        ds_edit.clicked.connect(lambda: self.fileBrowser(self.ds_path))
        layout.addWidget(ds_title, 1, 0)
        layout.addWidget(self.ds_path, 1, 1)
        layout.addWidget(ds_edit, 1, 2)

        # Plugin Name
        n_title = QLabel("Plugin Name")
        n_title.setAlignment(Qt.AlignRight)
        # TODO: add functionality later
        n_name = QLineEdit("Network")
        layout.addWidget(n_title, 2, 0)
        layout.addWidget(n_name, 2, 1)

        # Plugin Description
        d_title = QLabel("Plugin Description")
        d_title.setAlignment(Qt.AlignRight)
        d_name = QTextEdit("Plugin used to detect network behaviors in binaries")
        layout.addWidget(d_title, 3, 0)
        layout.addWidget(d_name, 3, 1)

        # Output Field
        o_title = QLabel("Output Field")
        o_title.setAlignment(Qt.AlignRight)
        o_menu = QComboBox()
        # TODO: add from some kind of list
        o_menu.addItems(["Python File", "Other"])
        layout.addWidget(o_title, 4, 0)
        layout.addWidget(o_menu, 4, 1)

        # POI's
        p_title = QLabel("Points of Interest")
        p_list = QListWidget()
        for item in self.pois:
            p_list.addItem(str(item))
        layout.addWidget(p_title, 5, 0)
        layout.addWidget(p_list, 5, 1)

        # Bottom buttons : delete and save
        b_delete = QPushButton("Delete")
        b_save = QPushButton("Save")
        layout.addWidget(b_delete, 6, 0)
        layout.addWidget(b_save, 6, 2)

        layout.setContentsMargins(100, 0, 100, 0)

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
