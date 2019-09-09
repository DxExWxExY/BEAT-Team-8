from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QFrame, QComboBox
from common.tab_layout import TabLayout

class PluginManagementTab(TabLayout):

    list = {"plugin1", "plugin2", "plugin3", "plugin4", "plugin5"}  # something of function to find list of plugin
    pois = {"a", "b", "c"}
    current = None

    def __init__(self):
        # your constructor must make the following calls
        super().__init__("Plugin View", "Detailed Plugin View")
        super().addContetentToLeftPanel(self.leftPanelBuilder())
        super().addContetentToRightPanel(self.rightPanelBuilder())
        super().build()

    def leftPanelBuilder(self):
        layout = QVBoxLayout()

        search = QLineEdit()
        search.setPlaceholderText("Search Plugin...")
        layout.addWidget(search)
        if search.returnPressed:
            if search.text == '':
                print("Please enter text")
            else:
                print(search.text)
                #self.__searchPlugin(search.text)

        for plugin in self.list:
            enable = QPushButton(plugin)
            layout.addWidget(enable)
        enable.clicked.connect(self.__findPlugin)

        new_plugin = QPushButton("New")
        layout.addWidget(new_plugin)

        return layout

    def rightPanelBuilder(self):
        layout = QVBoxLayout()

        # Plugin Structure
        structure = QHBoxLayout()
        ps_title = QLabel("Plugin Structure")
        ps_title.setAlignment(Qt.AlignCenter)
        ps_path = QLabel("./FilePath")
        ps_path.setFrameShape(QFrame.Panel)
        ps_path.setAlignment(Qt.AlignCenter)
        ps_edit = QPushButton("Browse")
        structure.addWidget(ps_title)
        structure.addWidget(ps_path)
        structure.addWidget(ps_edit)
        ps_edit.clicked.connect(self.__editName)
        layout.addLayout(structure)

        # Predefined Data Set
        data_set = QHBoxLayout()
        ds_title = QLabel("Predefined Data Set")
        ds_title.setAlignment(Qt.AlignCenter)
        ds_path = QLabel("./FilePath")
        ds_path.setFrameShape(QFrame.Panel)
        ds_path.setAlignment(Qt.AlignCenter)
        ds_edit = QPushButton("Browse")
        data_set.addWidget(ds_title)
        data_set.addWidget(ds_path)
        data_set.addWidget(ds_edit)
        layout.addLayout(data_set)

        # Plugin Name
        name = QHBoxLayout()
        n_title = QLabel("Plugin Name")
        n_title.setAlignment(Qt.AlignCenter)
        n_name = QLabel(self.current) # add functionality later
        n_name.setAlignment(Qt.AlignCenter)
        name.addWidget(n_title)
        name.addWidget(n_name)
        layout.addLayout(name)

        # Plugin Description
        descrip = QHBoxLayout()
        d_title = QLabel("Plugin Description")
        d_title.setAlignment(Qt.AlignCenter)
        d_name = QLabel("Current Plugin's description")
        d_name.setAlignment(Qt.AlignCenter)
        descrip.addWidget(d_title)
        descrip.addWidget(d_name)
        layout.addLayout(descrip)

        # Output Field
        output = QHBoxLayout()
        o_title = QLabel("Output Field")
        o_title.setAlignment(Qt.AlignCenter)
        o_menu = QComboBox()
        o_menu.addItem("Python File") # add from some kind of list
        o_menu.addItem("Other")
        output.addWidget(o_title)
        output.addWidget(o_menu)
        layout.addLayout(output)

        # POI's
        poi = QHBoxLayout()
        p_title = QLabel("Points of Interest")
        p_title.setAlignment(Qt.AlignHCenter)
        p_list = QVBoxLayout()
        p_list.setAlignment(Qt.AlignTop)
        for item in self.pois:
            p_item = QLabel(item)
            p_item.setAlignment(Qt.AlignCenter)
            p_list.addWidget(p_item)

        poi.addWidget(p_title)
        poi.addLayout(p_list)
        layout.addLayout(poi)

        # Bottom buttons : delete and save
        bot_but = QHBoxLayout()
        b_delete = QPushButton("Delete")
        b_save = QPushButton("Save")
        bot_but.addWidget(b_delete)
        bot_but.addWidget(b_save)
        layout.addLayout(bot_but)

        return layout

    def __searchPlugin(self, str):
        print("At least you entered something \(''/)/")
        return str

    def __editName(self):
        print("edit name")

    def __findPlugin(self, str):
        for item in self.list:
            if item == str:
                self.current = item
                print(self.current)


