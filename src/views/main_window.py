import sys

from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QDesktopWidget, QTabWidget, QMainWindow, QAction

from src.common import constants
from src.controllers.analysis_tab_controller import AnalysisTabController
from src.controllers.documentation_controller import DocumentationTabController
from src.controllers.plugin_management_controller import PluginManagementTabController
from src.controllers.project_controller import ProjectTabController
from src.views.tabs.documentation_tab import DocumentationTab


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.projectController = ProjectTabController()
        self.analysisController = AnalysisTabController()
        self.pluginManagementController = PluginManagementTabController()
        self.DocumentationTabController = DocumentationTabController()
        self.__openSelector()

    def __openSelector(self, beatOpen=False):
        self.projectController.projectSelection.exec_()
        if self.projectController.getCurrentProject() is not None:
            self.__openBeat(beatOpen)
        else:
            self.close()
            sys.exit(0)

    def __openBeat(self, wasOpen=False):
        self.updateData()
        if wasOpen:
            self.show()
        else:
            self.tabBuilder()
            self.buildWindow()

    def tabBuilder(self):
        self.tabs = QTabWidget()
        self.tabs.addTab(self.analysisController.tab, "Analysis")
        self.tabs.addTab(self.pluginManagementController.tab, "Plugin Management")
        self.tabs.addTab(self.DocumentationTabController.tab, "Documentation")
        self.tabs.setStyleSheet("QTabBar::tab { height: 40%; width: 200%; }")
        self.tabs.setFont(QFont("arial", 11))
        self.tabs.currentChanged.connect(lambda: self.updateData())

    def buildWindow(self):
        # Menu bar
        self.menu = self.menuBar()
        fileMenu = self.menu.addMenu('&File')
        viewMenu = self.menu.addMenu('&View')

        openSelector = QAction('&Open Project', self)
        openSelector.setShortcut('Ctrl+O')
        openSelector.triggered.connect(lambda: self.__openSelector(True))

        help = QAction('&Documentation', self)
        help.setShortcut('F1')

        fileMenu.addAction(openSelector)
        viewMenu.addAction(help)

        self.statusBar()
        # Tabs
        self.setCentralWidget(self.tabs)

        # Setup
        self.setFont(QFont("arial", 11))
        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.setWidth(constants.WIDTH)
        qtRectangle.setHeight(constants.HEIGHT)
        qtRectangle.moveCenter(centerPoint)
        self.setWindowTitle(constants.SYSTEM_TITLE)
        self.setGeometry(qtRectangle)
        self.show()

    def updateData(self):
        project = self.projectController.getCurrentProject()
        self.analysisController.setProject(project)
        self.analysisController.update()
        self.pluginManagementController.update()
