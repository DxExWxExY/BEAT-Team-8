from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QWheelEvent
from PyQt5.QtWidgets import QWidget, QGridLayout, QFrame, QLabel, QVBoxLayout, QFileDialog, QGroupBox

from src.common import constants


class TabLayout(QWidget):
    def __init__(self, leftPanelLabel, rightPanelLabel, hasTopPanel=False):
        super().__init__()
        self.__mainGrid = QGridLayout()
        leftFrame = QGroupBox(leftPanelLabel)
        rightFrame = QGroupBox(rightPanelLabel)
        TopFrame = QGroupBox()
        self.setFont(QFont("arial", 11))

        self._leftPanelLayout = QVBoxLayout()
        self._rightPanelLayout = QVBoxLayout()
        self._TopPanelLayout = QVBoxLayout()

        leftFrame.setLayout(self._leftPanelLayout)
        rightFrame.setLayout(self._rightPanelLayout)
        TopFrame.setLayout(self._TopPanelLayout)

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