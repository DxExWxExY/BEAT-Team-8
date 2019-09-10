from PyQt5.QtWidgets import QWidget, QDesktopWidget, QTabWidget, QMainWindow

from common import constants
from views.tabs.documentation_tab import DocumentationTab
from views.tabs.plugin_management_tab import PluginManagementTab
from views.tabs.points_of_intersets_tab import PointsOfInterestTab
from views.tabs.project_tab import ProjectTab
from views.tabs.analysis_tab import AnalysisTab

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.tabBuilder()
        self.buildWindow()

    def tabBuilder(self):
        # TODO: Add tab implementations
        self.tabs = QTabWidget()
        self.tabs.addTab(ProjectTab(), "Project")
        self.tabs.addTab(AnalysisTab(), "Analysis")
        self.tabs.addTab(PluginManagementTab(), "Plugin Management")
        self.tabs.addTab(PointsOfInterestTab(), "Points of Interest")
        self.tabs.addTab(DocumentationTab(), "Documentation")

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
