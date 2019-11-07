from PyQt5.QtWidgets import QWidget, QPushButton, QLineEdit, QDesktopWidget, QGridLayout, QTextEdit


class CommentDialog(QWidget):
    def __init__(self):
        # TODO: receive instance of the poi item whose comment will be added
        super().__init__()
        self.__initUI()
        self.__setWindowPosition()
        self.show()

    def __initUI(self):
        layout = QGridLayout()
        self.commentBox = QTextEdit()
        self.saveComment = QPushButton('Save')
        self.clearComment = QPushButton('Clear')

        layout.addWidget(self.commentBox, 0, 0, 5, 5)
        layout.addWidget(self.saveComment, 6, 4, 1, 1)
        layout.addWidget(self.clearComment, 6, 3 , 1, 1)

        self.clearComment.clicked.connect(lambda: self.__clearComment())

        self.setWindowTitle('Comment View')
        self.setLayout(layout)

    def __setWindowPosition(self):
        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.setWidth(480)
        qtRectangle.setHeight(250)
        qtRectangle.moveCenter(centerPoint)
        self.setGeometry(qtRectangle)

    def __clearComment(self):
        self.commentBox.clear()
