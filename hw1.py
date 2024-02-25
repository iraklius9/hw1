from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(811, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.passwordoutput = QtWidgets.QLabel(self.centralwidget)
        self.passwordoutput.setGeometry(QtCore.QRect(530, 270, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.passwordoutput.setFont(font)
        self.passwordoutput.setText("")
        self.passwordoutput.setObjectName("passwordoutput")

        self.useroutput = QtWidgets.QLabel(self.centralwidget)
        self.useroutput.setGeometry(QtCore.QRect(530, 162, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.useroutput.setFont(font)
        self.useroutput.setText("")
        self.useroutput.setObjectName("useroutput")

        self.header = QtWidgets.QLabel(self.centralwidget)
        self.header.setGeometry(QtCore.QRect(210, 20, 371, 91))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.header.setFont(font)
        self.header.setAlignment(QtCore.Qt.AlignCenter)
        self.header.setObjectName("header")

        self.userline = QtWidgets.QLineEdit(self.centralwidget)
        self.userline.setGeometry(QtCore.QRect(320, 180, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.userline.setFont(font)
        self.userline.setObjectName("userline")

        self.passwordline = QtWidgets.QLineEdit(self.centralwidget)
        self.passwordline.setGeometry(QtCore.QRect(320, 270, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.passwordline.setFont(font)
        self.passwordline.setObjectName("passwordline")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(300, 380, 201, 81))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")

        self.pushButton.clicked.connect(self.buttonpushed)

        self.stackedWidget_2 = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget_2.setGeometry(QtCore.QRect(630, 460, 191, 80))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.stackedWidget_2.setFont(font)
        self.stackedWidget_2.setObjectName("stackedWidget_2")

        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")

        self.label = QtWidgets.QLabel(self.page_3)
        self.label.setGeometry(QtCore.QRect(16, 20, 151, 41))
        self.label.setText("")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        self.stackedWidget_2.addWidget(self.page_3)

        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.stackedWidget_2.addWidget(self.page_4)
        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 811, 21))
        self.menubar.setObjectName("menubar")

        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")

        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.passwordline.setEchoMode(QtWidgets.QLineEdit.Password)

    def buttonpushed(self):

        if self.userline.text() == "user" and self.passwordline.text() == "paroli":
            self.stackedWidget_2.setGeometry(0, 0, 850, 586)
            self.stackedWidget_2.setStyleSheet("background-color: grey;")
            self.label.setText("You Are Logged In !")
            self.label.setGeometry(300, 200, 180, 91)
            self.label.adjustSize()

            self.passwordline.setEchoMode(QtWidgets.QLineEdit.Password)
        else:
            self.useroutput.setText("Mail Is Incorrect")
            self.useroutput.adjustSize()
            self.passwordoutput.setText("Password Is Incorrect")
            self.passwordoutput.adjustSize()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.header.setText(_translate("MainWindow", "LOG IN!"))
        self.userline.setPlaceholderText(_translate("MainWindow", "Enter Your Email"))
        self.passwordline.setPlaceholderText(_translate("MainWindow", "Enter Your Password"))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
