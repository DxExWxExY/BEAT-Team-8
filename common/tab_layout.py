from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QGridLayout, QFrame, QLabel, QVBoxLayout

from common import constants

class TabLayout(QWidget):
    def __init__(self):
        super().__init__()
        __mainGrid = QGridLayout()
        leftFrame = QFrame()
        rightFrame = QFrame()
        self.leftPanelLayout = QVBoxLayout()
        self.rightPanelLayout = QVBoxLayout()

        leftFrame.setLayout(self.leftPanelLayout)
        rightFrame.setLayout(self.rightPanelLayout)

        self.leftPanelLabel = QLabel()
        self.rightPanelLabel = QLabel()

        self.leftPanelLabel.setStyleSheet(constants.PANEL_TITLE_STYLE)
        self.rightPanelLabel.setStyleSheet(constants.PANEL_TITLE_STYLE)

        self.leftPanelLabel.setText("LEFT")
        self.rightPanelLabel.setText("RIGHT")

        self.leftPanelLabel.setAlignment(Qt.AlignCenter)
        self.rightPanelLabel.setAlignment(Qt.AlignCenter)

        self.leftPanelLayout.addWidget(self.leftPanelLabel)
        self.rightPanelLayout.addWidget(self.rightPanelLabel)

        self.leftPanelLayout.setAlignment(self.leftPanelLabel, Qt.AlignTop)
        self.rightPanelLayout.setAlignment(self.rightPanelLabel, Qt.AlignTop)

        __mainGrid.addWidget(leftFrame, 0, 0, 1, 2)
        __mainGrid.addWidget(rightFrame, 0, 4, 1, 7)

        self.setLayout(__mainGrid)
