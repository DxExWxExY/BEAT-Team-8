from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QGridLayout, QFrame, QLabel, QVBoxLayout

from common import constants

class TabLayout(QWidget):
    def __init__(self, leftPanelLabel, rightPanelLabel):
        super().__init__()
        self.__mainGrid = QGridLayout()
        leftFrame = QFrame()
        rightFrame = QFrame()
        self._leftPanelLayout = QVBoxLayout()
        self._rightPanelLayout = QVBoxLayout()

        leftFrame.setLayout(self._leftPanelLayout)
        rightFrame.setLayout(self._rightPanelLayout)

        self.__leftPanelLabel = QLabel()
        self.__rightPanelLabel = QLabel()

        self.__leftPanelLabel.setStyleSheet(constants.PANEL_TITLE_STYLE)
        self.__rightPanelLabel.setStyleSheet(constants.PANEL_TITLE_STYLE)

        self.__leftPanelLabel.setText(leftPanelLabel)
        self.__rightPanelLabel.setText(rightPanelLabel)

        self.__leftPanelLabel.setAlignment(Qt.AlignCenter)
        self.__rightPanelLabel.setAlignment(Qt.AlignCenter)

        self._leftPanelLayout.addWidget(self.__leftPanelLabel)
        self._rightPanelLayout.addWidget(self.__rightPanelLabel)

        self._leftPanelLayout.setAlignment(self.__leftPanelLabel, Qt.AlignTop)
        self._rightPanelLayout.setAlignment(self.__rightPanelLabel, Qt.AlignTop)

        self.__mainGrid.addWidget(leftFrame, 0, 0, 1, 2)
        self.__mainGrid.addWidget(rightFrame, 0, 4, 1, 7)

    def addContetentToLeftPanel(self, layout):
        self._leftPanelLayout.addLayout(layout)
        self._leftPanelLayout.setAlignment(layout, Qt.AlignTop)

    def addContetentToRightPanel(self, layout):
        self._rightPanelLayout.addLayout(layout)
        self._rightPanelLayout.setAlignment(layout, Qt.AlignTop)

    def build(self):
        self.setLayout(self.__mainGrid)
