from PyQt5.QtWidgets import QPushButton, QDesktopWidget, QGridLayout, QDialog, QLineEdit


class CommentDialog(QDialog):
    def __init__(self, widget):
        super().__init__()
        self.widget = widget
        self.__initUI()
        self.__setWindowPosition()

    def __initUI(self):
        layout = QGridLayout()
        self.commentBox = QLineEdit()
        self.saveComment = QPushButton('Save')
        self.clearComment = QPushButton('Clear')

        layout.addWidget(self.commentBox, 0, 0, 5, 5)
        layout.addWidget(self.saveComment, 6, 4, 1, 1)
        layout.addWidget(self.clearComment, 6, 3, 1, 1)

        self.clearComment.clicked.connect(lambda: self.__clearComment())
        self.saveComment.clicked.connect(lambda: self.__saveComment())
        self.commentBox.returnPressed.connect(lambda: self.__saveComment())

        if 'comment' in self.widget.poi.keys():
            self.commentBox.setText(self.widget.poi['comment'])

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

    def __saveComment(self):
        if not self.commentBox.text():
            del self.widget.poi['comment']
        else:
            self.widget.poi['comment'] = self.commentBox.text()
        self.widget.updateCommentState()
        self.close()
        self.commentBox.clear()

