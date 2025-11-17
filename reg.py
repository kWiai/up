from PyQt6 import QtCore, QtGui, QtWidgets
from connector import c
from PyQt6.QtWidgets import QMessageBox

class Ui_Reg(object):
    def setupUi(self, RegWindow):
        RegWindow.setObjectName("RegWindow")
        RegWindow.resize(605, 373)
        self.centralwidget = QtWidgets.QWidget(parent=RegWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 181, 20))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 40, 271, 20))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(70, 100, 63, 20))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(70, 140, 63, 20))
        self.label_4.setObjectName("label_4")
        self.lineLogin = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineLogin.setGeometry(QtCore.QRect(160, 100, 371, 26))
        self.lineLogin.setObjectName("lineLogin")
        self.linePassword = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.linePassword.setGeometry(QtCore.QRect(160, 140, 371, 26))
        self.linePassword.setObjectName("linePassword")
        self.linePassword.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.checkBox = QtWidgets.QCheckBox(parent=self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(380, 180, 151, 24))
        self.checkBox.setObjectName("checkBox")
        self.checkBox.toggled.connect(self.showPassword)
        self.authButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.authButton.setGeometry(QtCore.QRect(210, 270, 171, 51))
        self.authButton.setObjectName("authButton")
        self.authButton.clicked.connect(self.auth)
        RegWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=RegWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 605, 26))
        self.menubar.setObjectName("menubar")
        RegWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=RegWindow)
        self.statusbar.setObjectName("statusbar")
        RegWindow.setStatusBar(self.statusbar)

        self.retranslateUi(RegWindow)
        QtCore.QMetaObject.connectSlotsByName(RegWindow)

    def retranslateUi(self, RegWindow):
        _translate = QtCore.QCoreApplication.translate
        RegWindow.setWindowTitle(_translate("RegWindow", "Авторизация"))
        self.label.setText(_translate("RegWindow", "Панель авторизации"))
        self.label_2.setText(_translate("RegWindow", "Пожалуйста, авторизуйтесь в системе"))
        self.label_3.setText(_translate("RegWindow", "Логин:"))
        self.label_4.setText(_translate("RegWindow", "Пароль:"))
        self.checkBox.setText(_translate("RegWindow", "Показать пароль"))
        self.authButton.setText(_translate("RegWindow", "Авторизоваться"))

    def auth(self):
        login = self.lineLogin.text()
        password = self.linePassword.text()
        c.execute("SELECT password,UserID FROM autorization WHERE login = %s",(login,))
        result = c.fetchone()
        if result == None:
            QMessageBox.critical(None,"Ошибка","Такого пользователя не существует",QMessageBox.StandardButton.Ok)
        elif result[0] != password:
            QMessageBox.critical(None,"Ошибка","Неверный пароль",QMessageBox.StandardButton.Ok)
        else:
            from config import manager
            manager.set_current_userID(result[1])
            manager.show_sklad()
            
    def showPassword(self,checked):
        if checked:
            self.linePassword.setEchoMode(QtWidgets.QLineEdit.EchoMode.Normal)
        else:
            self.linePassword.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)