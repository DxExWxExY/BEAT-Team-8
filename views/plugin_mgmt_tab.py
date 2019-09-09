from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QCheckBox, QComboBox
from common.tab_layout import TabLayout

class PluginMGMTTab(TabLayout):

    list = {"plugin1", "plugin2", "plugin3", "plugin4", "plugin5"}  # something of function to find list of plugin
    pois = {"a", "b", "c"}

    def __init__(self):
        # your constructor must make the following calls
        super().__init__("Plugin View", "Detailed Plugin View")
        super().addContetentToLeftPanel(self.leftPanelBuilder())
        super().addContetentToRightPanel(self.rightPanelBuilder())
        super().build()

    def leftPanelBuilder(self):
        layout = QVBoxLayout()

        # search box
        search = QLineEdit()
        search.setPlaceholderText("Search Plugin...")
        layout.addWidget(search,0,Qt.AlignTop)
        if search.returnPressed:
            if search.text == "":
                print("Please enter text")
            else:
                self.__searchPlugin(search.text)
                print("At least you entered something \(''/)/")  # search db? list of plugins

        for plugin in self.list:
            enable = QPushButton(plugin)
            enable.click()
            layout.addWidget(enable)

        new_plugin = QPushButton("New")
        layout.addWidget(new_plugin)
        return layout

    def rightPanelBuilder(self):
        layout = QVBoxLayout()

        # Plugin Structure
        structure = QHBoxLayout()
        ps_title = QLabel("Plugin Structure")
        ps_path = QLabel("./FilePath")
        ps_edit = QPushButton("Edit")
        structure.addWidget(ps_title)
        structure.addWidget(ps_path)
        structure.addWidget(ps_edit)
        layout.addLayout(structure)

        # Predefined Data Set
        data_set = QHBoxLayout()
        ds_title = QLabel("Predefined Data Set")
        ds_path = QLabel("./FilePath")
        ds_edit = QPushButton("Edit")
        data_set.addWidget(ds_title)
        data_set.addWidget(ds_path)
        data_set.addWidget(ds_edit)
        layout.addLayout(data_set)

        # Plugin Name
        name = QHBoxLayout()
        n_title = QLabel("Plugin Name")
        n_name = QLabel("Current Plugin") # add functionality later
        name.addWidget(n_title)
        name.addWidget(n_name)
        layout.addLayout(name)

        # Plugin Description
        descrip = QHBoxLayout()
        d_title = QLabel("Plugin Description")
        d_name = QLabel("Current Plugin's description")
        descrip.addWidget(d_title)
        descrip.addWidget(d_name)
        layout.addLayout(descrip)

        # Output Field
        output = QHBoxLayout()
        o_title = QLabel("Output Field")
        o_menu = QComboBox()
        o_menu.addItem("Python File")
        o_menu.addItem("Other")
        output.addWidget(o_title)
        output.addWidget(o_menu)
        layout.addLayout(output)

        # POI's
        poi = QHBoxLayout()
        p_title = QLabel("Points of Interest")
        p_list = QVBoxLayout()
        for item in self.pois:
            p_item = QLabel(item)
            p_list.addWidget(p_item)
        poi.addWidget(p_title)
        poi.addLayout(p_list)
        layout.addLayout(poi)

        return layout

    def __searchPlugin(self, str):
        return str
