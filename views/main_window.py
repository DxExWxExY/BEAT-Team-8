from PyQt5.QtWidgets import QWidget, QDesktopWidget, QTabWidget, QMainWindow

from common import constants
from views.project_tab import ProjectTab


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.tabBuilder()
        self.buildWindow()

    def tabBuilder(self):
        self.tabs = QTabWidget()
        self.tabs.addTab(ProjectTab(), "Project")
        self.tabs.addTab(QWidget(), "Analysis")
        self.tabs.addTab(QWidget(), "Plugin Management")
        self.tabs.addTab(QWidget(), "Points of Interest")
        self.tabs.addTab(QWidget(), "Documentation")

    def buildWindow(self):
        # Tabs
        self.setCentralWidget(self.tabs)

        # Setup
        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.setWidth(constants.WIDTH)
        qtRectangle.setHeight(constants.HEIGHT)
        qtRectangle.moveCenter(centerPoint)
        self.setWindowTitle(constants.SYSTEM_TITLE)
        self.setGeometry(qtRectangle)
        self.show()
