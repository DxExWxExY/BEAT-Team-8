from PyQt5.QtCore import Qt
from PyQt5.QtGui import QWheelEvent, QFont
from PyQt5.QtWidgets import QDesktopWidget, QTabWidget, QMainWindow

from src.common import constants
from src.controllers.analysis_tab_controller import AnalysisTabController
from src.controllers.project_tab_controller import ProjectTabController
from src.controllers.pulgin_management_tab_controller import PluginManagementTabController
from src.views.tabs.documentation_tab import DocumentationTab
from src.views.tabs.points_of_intersets_tab import PointsOfInterestTab


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.projectController = ProjectTabController()
        self.analysisController = AnalysisTabController()
        self.pluginManagementController = PluginManagementTabController()
        self.fontSize = 14
        self.tabBuilder()
        self.buildWindow()

    def tabBuilder(self):
        self.tabs = QTabWidget()
        self.tabs.addTab(self.projectController.tab, "Project")
        self.tabs.addTab(self.analysisController.tab, "Analysis")
        self.tabs.addTab(self.pluginManagementController.tab, "Plugin Management")
        self.tabs.addTab(PointsOfInterestTab(), "Points of Interest")
        self.tabs.addTab(DocumentationTab(), "Documentation")
        self.tabs.setStyleSheet("QTabBar::tab { height: 50%; width: 200%; }")
        self.tabs.setFont(QFont("arial", 11))
        self.tabs.currentChanged.connect(lambda: self.setProjectForUse())

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

    def setProjectForUse(self):
        project = self.projectController.getCurrentProject()
        self.analysisController.setProject(project)

    def wheelEvent(self, event: QWheelEvent):
        if event.modifiers() == Qt.ControlModifier:
            font = QFont()
            if event.angleDelta().y() > 0:
                self.fontSize += 2
                print(self.fontSize)
                font.setPointSize(self.fontSize)
                self.setFont(font)
            else:
                if self.fontSize > 2:
                    self.fontSize -= 2
                    print(self.fontSize)
                    font.setPointSize(self.fontSize)
                    self.setFont(font)
            self.update()