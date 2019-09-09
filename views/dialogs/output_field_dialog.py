from PyQt5 import QtCore, QtGui, QtWidgets

class OutputFieldDialog(object):
    def setupUi(self, OutputFieldView):
        OutputFieldView.setObjectName("OutputFieldView")
        OutputFieldView.resize(501, 423)
        self.generateButton = QtWidgets.QPushButton(OutputFieldView)
        self.generateButton.setGeometry(QtCore.QRect(360, 360, 121, 31))
        self.generateButton.setObjectName("generateButton")
        self.plainTextEditName = QtWidgets.QPlainTextEdit(OutputFieldView)
        self.plainTextEditName.setGeometry(QtCore.QRect(160, 30, 331, 51))
        self.plainTextEditName.setObjectName("plainTextEditName")
        self.plainTextEditDescription = QtWidgets.QPlainTextEdit(OutputFieldView)
        self.plainTextEditDescription.setGeometry(QtCore.QRect(160, 90, 331, 151))
        self.plainTextEditDescription.setObjectName("plainTextEditDescription")
        self.nameLabel = QtWidgets.QLabel(OutputFieldView)
        self.nameLabel.setGeometry(QtCore.QRect(70, 40, 71, 31))
        self.nameLabel.setObjectName("nameLabel")
        self.descriptionLabel = QtWidgets.QLabel(OutputFieldView)
        self.descriptionLabel.setGeometry(QtCore.QRect(20, 150, 131, 31))
        self.descriptionLabel.setObjectName("descriptionLabel")
        self.locationLabel = QtWidgets.QLabel(OutputFieldView)
        self.locationLabel.setGeometry(QtCore.QRect(50, 260, 101, 31))
        self.locationLabel.setObjectName("locationLabel")
        self.plainTextEditLocation = QtWidgets.QPlainTextEdit(OutputFieldView)
        self.plainTextEditLocation.setGeometry(QtCore.QRect(160, 250, 331, 51))
        self.plainTextEditLocation.setObjectName("plainTextEditLocation")
        self.browseButton = QtWidgets.QPushButton(OutputFieldView)
        self.browseButton.setGeometry(QtCore.QRect(360, 320, 121, 31))
        self.browseButton.setObjectName("browseButton")

        self.retranslateUi(OutputFieldView)
        QtCore.QMetaObject.connectSlotsByName(OutputFieldView)

    def retranslateUi(self, OutputFieldView):
        _translate = QtCore.QCoreApplication.translate
        OutputFieldView.setWindowTitle(_translate("OutputFieldView", "Output Field View"))
        self.generateButton.setText(_translate("OutputFieldView", "Generate"))
        self.nameLabel.setText(_translate("OutputFieldView", "Name"))
        self.descriptionLabel.setText(_translate("OutputFieldView", "Description"))
        self.locationLabel.setText(_translate("OutputFieldView", "Location"))
        self.browseButton.setText(_translate("OutputFieldView", "Browse"))