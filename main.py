from PyQt5 import QtCore, QtGui, QtWidgets
from views.OutputFieldBox import Ui_OutputFieldView

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    OutputFieldView = QtWidgets.QDialog()
    ui = Ui_OutputFieldView()
    ui.setupUi(OutputFieldView)
    OutputFieldView.show()
    sys.exit(app.exec_())