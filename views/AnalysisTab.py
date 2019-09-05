from PyQt5.QtWidgets import QLabel, QVBoxLayout, QPushButton, QLineEdit
from PyQt5 import QtCore, QtGui, QtWidgets


from common.tab_layout import TabLayout


class AnalysisTab(TabLayout):

    def __init__(self):

        # your constructor must make the following calls
        super().__init__("Point of Interest View", "Detailed Point of Interest View")
        super().addContetentToCentralPanel(self.centralPanelBuilder())
        super().addContetentToRightPanel(self.rightPanelBuilder())
        super().addContetentToLeftPanel(self.leftPanelBuilder())
        super().build()

    def leftPanelBuilder(self):

        layout = QVBoxLayout()
        layout.addWidget(QLabel('left'))


        return layout

    def rightPanelBuilder(self):

        layout = QVBoxLayout()
        layout.addWidget(QLabel('right'))
        return layout

    def centralPanelBuilder(self):
        _translate = QtCore.QCoreApplication.translate



        horizontalLayoutWidget = QtWidgets.QWidget(self)
        horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 761, 161))
        horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        horizontalLayout = QtWidgets.QHBoxLayout(horizontalLayoutWidget)
        horizontalLayout.setContentsMargins(0, 0, 0, 0)
        horizontalLayout.setObjectName("horizontalLayout")


        gridLayout = QtWidgets.QGridLayout()
        gridLayout.setObjectName("gridLayout")


        dropDownMenuPlugin = QtWidgets.QComboBox(horizontalLayoutWidget)
        dropDownMenuPlugin.setObjectName("comboBox")
        dropDownMenuPlugin.addItem("Existing Plugin")
        gridLayout.addWidget(dropDownMenuPlugin, 0, 1, 1, 3)

        dropDownMenuPoi = QtWidgets.QComboBox(horizontalLayoutWidget)
        dropDownMenuPoi.setObjectName("dropDownMenuPoi")
        dropDownMenuPoi.addItem("Type")
        gridLayout.addWidget(dropDownMenuPoi, 2, 1, 1, 1)

        pluginlabel = QtWidgets.QLabel(horizontalLayoutWidget)
        pluginlabel.setObjectName("pluginlabel")
        pluginlabel.setText(_translate("Dialog", "Plugin"))
        gridLayout.addWidget(pluginlabel, 0, 0, 1, 1)

        StaticAn = QtWidgets.QLabel(horizontalLayoutWidget)
        StaticAn.setObjectName("StaticAn")
        StaticAn.setText(_translate("Dialog", "Static analysis"))
        gridLayout.addWidget(StaticAn, 1, 0, 1, 1)
        label_3 = QtWidgets.QLabel(horizontalLayoutWidget)
        label_3.setObjectName("label_3")
        label_3.setText(_translate("Dialog", "point of interest type"))
        gridLayout.addWidget(label_3, 2, 0, 1, 1)
        staticRunbtn = QtWidgets.QPushButton(horizontalLayoutWidget)
        staticRunbtn.setObjectName("staticRunbtn")
        staticRunbtn.setText(_translate("Dialog", "Run"))
        gridLayout.addWidget(staticRunbtn, 1, 1, 1, 1)

        horizontalLayout.addLayout(gridLayout)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        horizontalLayout.addItem(spacerItem)


        DynamicAn = QtWidgets.QLabel(horizontalLayoutWidget)
        DynamicAn.setObjectName("DynamicAn")
        DynamicAn.setText(_translate("Dialog", "Dynamic analysis"))
        horizontalLayout.addWidget(DynamicAn)


        dynamicRunbtn = QtWidgets.QPushButton(horizontalLayoutWidget)
        dynamicRunbtn.setObjectName("dynamicRunbtn")
        dynamicRunbtn.setText(_translate("Dialog", "Run"))
        horizontalLayout.addWidget(dynamicRunbtn)


        dynamicStopbtn = QtWidgets.QPushButton(horizontalLayoutWidget)
        dynamicStopbtn.setObjectName("dynamicStopbtn")
        dynamicStopbtn.setText(_translate("Dialog", "Stop"))

        horizontalLayout.addWidget(dynamicStopbtn)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        horizontalLayout.addItem(spacerItem1)



        return horizontalLayout


    # def retranslateUi(self, Dialog):
    #     _translate = QtCore.QCoreApplication.translate
    #     Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
    #     self.pluginlabel.setText(_translate("Dialog", "Plugin"))
    #     self.StaticAn.setText(_translate("Dialog", "Static analysis"))
    #     self.label_3.setText(_translate("Dialog", "point of interest type"))
    #     self.staticRunbtn.setText(_translate("Dialog", "Run"))
    #     self.DynamicAn.setText(_translate("Dialog", "Dynamic analysis"))
    #     self.dynamicRunbtn.setText(_translate("Dialog", "Run"))
    #     self.dynamicStopbtn.setText(_translate("Dialog", "Stop"))
    #     return layout
    #
    # def setupUi(self, Dialog):
    #     Dialog.setObjectName("Dialog")
    #     Dialog.resize(801, 591)
    #     self.horizontalLayoutWidget = QtWidgets.QWidget(Dialog)
    #     self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 761, 161))
    #     self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
    #     self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
    #     self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
    #     self.horizontalLayout.setObjectName("horizontalLayout")
    #     self.gridLayout = QtWidgets.QGridLayout()
    #     self.gridLayout.setObjectName("gridLayout")
    #     self.comboBox_2 = QtWidgets.QComboBox(self.horizontalLayoutWidget)
    #     self.comboBox_2.setObjectName("comboBox_2")
    #     self.gridLayout.addWidget(self.comboBox_2, 2, 1, 1, 1)
    #     self.comboBox = QtWidgets.QComboBox(self.horizontalLayoutWidget)
    #     self.comboBox.setObjectName("comboBox")
    #     self.gridLayout.addWidget(self.comboBox, 0, 1, 1, 3)
    #     self.pluginlabel = QtWidgets.QLabel(self.horizontalLayoutWidget)
    #     self.pluginlabel.setObjectName("pluginlabel")
    #     self.gridLayout.addWidget(self.pluginlabel, 0, 0, 1, 1)
    #     self.StaticAn = QtWidgets.QLabel(self.horizontalLayoutWidget)
    #     self.StaticAn.setObjectName("StaticAn")
    #     self.gridLayout.addWidget(self.StaticAn, 1, 0, 1, 1)
    #     self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget)
    #     self.label_3.setObjectName("label_3")
    #     self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
    #     self.staticRunbtn = QtWidgets.QPushButton(self.horizontalLayoutWidget)
    #     self.staticRunbtn.setObjectName("staticRunbtn")
    #     self.gridLayout.addWidget(self.staticRunbtn, 1, 1, 1, 1)
    #     self.horizontalLayout.addLayout(self.gridLayout)
    #     spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
    #     self.horizontalLayout.addItem(spacerItem)
    #     self.DynamicAn = QtWidgets.QLabel(self.horizontalLayoutWidget)
    #     self.DynamicAn.setObjectName("DynamicAn")
    #     self.horizontalLayout.addWidget(self.DynamicAn)
    #     self.dynamicRunbtn = QtWidgets.QPushButton(self.horizontalLayoutWidget)
    #     self.dynamicRunbtn.setObjectName("dynamicRunbtn")
    #     self.horizontalLayout.addWidget(self.dynamicRunbtn)
    #     self.dynamicStopbtn = QtWidgets.QPushButton(self.horizontalLayoutWidget)
    #     self.dynamicStopbtn.setObjectName("dynamicStopbtn")

    #
    #     self.retranslateUi(Dialog)
    #     QtCore.QMetaObject.connectSlotsByName(Dialog)


