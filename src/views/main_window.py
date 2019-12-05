import sys

from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QDesktopWidget, QMainWindow, QAction

from src.common import constants
from src.controllers.analysis_tab_controller import AnalysisTabController
from src.controllers.documentation_controller import DocumentationController
from src.controllers.plugin_management_controller import PluginManagementController
from src.controllers.project_controller import ProjectController


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.projectController = ProjectController()
        self.analysisController = AnalysisTabController()
        self.pluginManagementController = PluginManagementController()
        self.DocumentationTabController = DocumentationController()
        self.__openProjectSelector()

    def __openProjectSelector(self, beatOpen=False):
        self.projectController.projectSelection.exec_()
        if self.projectController.getCurrentProject() is not None:
            self.__openBeat(beatOpen)
        else:
            self.close()
            sys.exit(0)

    def __openPluginManager(self):
        self.pluginManagementController.dialog.exec_()
        self.__updateData()

    def __openHelp(self):
        self.DocumentationTabController.dialog.show()

    def __openBeat(self, wasOpen=False):
        self.__updateData()
        if wasOpen:
            self.show()
        else:
            self.__buildWindow()

    def __buildWindow(self):
        self.menu = self.menuBar()
        fileMenu = self.menu.addMenu('&File')
        viewMenu = self.menu.addMenu('&View')

        openSelector = QAction('&Open Project', self)
        openSelector.setShortcut('Ctrl+O')
        openSelector.triggered.connect(lambda: self.__openProjectSelector(True))

        manageSelector = QAction('&Manage Plugins', self)
        manageSelector.setShortcut('Ctrl+P')
        manageSelector.triggered.connect(lambda: self.__openPluginManager())

        help = QAction('&Documentation', self)
        help.setShortcut('F1')
        help.triggered.connect(lambda: self.__openHelp())

        fileMenu.addAction(openSelector)
        fileMenu.addAction(manageSelector)
        viewMenu.addAction(help)
        self.statusBar()

        self.setCentralWidget(self.analysisController.tab)
        self.setFont(QFont("arial", 11))

        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.setWidth(constants.WIDTH)
        qtRectangle.setHeight(constants.HEIGHT)
        qtRectangle.moveCenter(centerPoint)

        self.setWindowTitle(constants.SYSTEM_TITLE)
        self.setGeometry(qtRectangle)
        self.show()

    def __updateData(self):
        project = self.projectController.getCurrentProject()
        self.analysisController.setProject(project)
        self.analysisController.update()
        self.pluginManagementController.update()
