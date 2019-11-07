from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QWheelEvent
from PyQt5.QtWidgets import QWidget, QGridLayout, QFrame, QLabel, QVBoxLayout, QFileDialog

from src.common import constants


class TabLayout(QWidget):
    def __init__(self, leftPanelLabel, rightPanelLabel, hasTopPanel=False):
        super().__init__()
        self.fontSize = 11
        self.__mainGrid = QGridLayout()
        leftFrame = QFrame()
        rightFrame = QFrame()
        TopFrame = QFrame()

        self.setFont(QFont("arial", self.fontSize))

        self._leftPanelLayout = QVBoxLayout()
        self._rightPanelLayout = QVBoxLayout()
        self._TopPanelLayout = QVBoxLayout()

        leftFrame.setLayout(self._leftPanelLayout)
        rightFrame.setLayout(self._rightPanelLayout)
        TopFrame.setLayout(self._TopPanelLayout)

        self.__leftPanelLabel = QLabel()
        self.__rightPanelLabel = QLabel()
        self.__TopPanelLabel = QLabel()

        self.__leftPanelLabel.setStyleSheet(constants.PANEL_TITLE_STYLE)
        self.__rightPanelLabel.setStyleSheet(constants.PANEL_TITLE_STYLE)

        self.__leftPanelLabel.setText(leftPanelLabel)
        self.__rightPanelLabel.setText(rightPanelLabel)

        self.__leftPanelLabel.setAlignment(Qt.AlignCenter)
        self.__rightPanelLabel.setAlignment(Qt.AlignCenter)
        self.__TopPanelLabel.setAlignment(Qt.AlignCenter)

        self._leftPanelLayout.addWidget(self.__leftPanelLabel)
        self._rightPanelLayout.addWidget(self.__rightPanelLabel)
        self._TopPanelLayout.addWidget(self.__TopPanelLabel)

        self._leftPanelLayout.setAlignment(self.__leftPanelLabel, Qt.AlignTop)
        self._rightPanelLayout.setAlignment(self.__rightPanelLabel, Qt.AlignTop)
        self._TopPanelLayout.setAlignment(self.__TopPanelLabel, Qt.AlignTop)

        if hasTopPanel:
            self.__mainGrid.addWidget(TopFrame, 0, 0, 1, 9)
            self.__mainGrid.addWidget(leftFrame, 1, 0, 1, 2)
            self.__mainGrid.addWidget(rightFrame, 1, 2, 1, 7)
        else:
            self.__mainGrid.addWidget(leftFrame, 0, 0, 1, 2)
            self.__mainGrid.addWidget(rightFrame, 0, 3, 1, 7)

    def addContentToLeftPanel(self, layout):
        self._leftPanelLayout.addLayout(layout)
        self._leftPanelLayout.setAlignment(layout, Qt.AlignTop)

    def addContentToRightPanel(self, layout):
        self._rightPanelLayout.addLayout(layout)
        self._rightPanelLayout.setAlignment(layout, Qt.AlignTop)

    def addContentToTopPanel(self, layout):
        self._TopPanelLayout.addLayout(layout)
        self._TopPanelLayout.setAlignment(layout, Qt.AlignTop)

    def build(self):
        self.setLayout(self.__mainGrid)

    def wheelEvent(self, event: QWheelEvent):
        if event.modifiers() == Qt.ControlModifier:
            font = QFont()
            if event.angleDelta().y() > 0:
                self.fontSize += 2
                font.setPointSize(self.fontSize)
                self.setFont(font)
            else:
                if self.fontSize > 2:
                    self.fontSize -= 2
                    font.setPointSize(self.fontSize)
                    self.setFont(font)
            self.update()