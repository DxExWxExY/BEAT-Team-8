from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QGridLayout, QVBoxLayout, QGroupBox


class TabLayout(QWidget):

    def __init__(self, leftPanelLabel, rightPanelLabel, topPanelLabel):
        super().__init__()
        self.__mainGrid = QGridLayout()
        leftFrame = QGroupBox(leftPanelLabel)
        rightFrame = QGroupBox(rightPanelLabel)
        topFrame = QGroupBox(topPanelLabel)
        self.setFont(QFont("arial", 11))

        self._leftPanelLayout = QVBoxLayout()
        self._rightPanelLayout = QVBoxLayout()
        self._topPanelLayout = QVBoxLayout()

        leftFrame.setLayout(self._leftPanelLayout)
        rightFrame.setLayout(self._rightPanelLayout)
        topFrame.setLayout(self._topPanelLayout)

        self.__mainGrid.addWidget(topFrame, 0, 0, 1, 9)
        self.__mainGrid.addWidget(leftFrame, 1, 0, 1, 2)
        self.__mainGrid.addWidget(rightFrame, 1, 2, 1, 7)

    def addContentToLeftPanel(self, layout):
        self._leftPanelLayout.addLayout(layout)
        self._leftPanelLayout.setAlignment(layout, Qt.AlignTop)

    def addContentToRightPanel(self, layout):
        self._rightPanelLayout.addLayout(layout)
        self._rightPanelLayout.setAlignment(layout, Qt.AlignTop)

    def addContentToTopPanel(self, layout):
        self._topPanelLayout.addLayout(layout)
        self._topPanelLayout.setAlignment(layout, Qt.AlignTop)

    def build(self):
        self.setLayout(self.__mainGrid)
