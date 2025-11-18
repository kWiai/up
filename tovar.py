from PyQt6 import QtCore, QtGui, QtWidgets
from connector import c
from config import manager
from PyQt6.QtWidgets import QMessageBox

class Ui_Tovar(object):
    
    def __init__(self):
        self.changed = False
        
    def setupUi(self, TovarWindow):
        TovarWindow.setObjectName("TovarWindow")
        TovarWindow.resize(615, 662)
        self.centralwidget = QtWidgets.QWidget(parent=TovarWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.TovarWindow = TovarWindow
        self.TovarWindow.closeEvent = self.close_event
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 10, 221, 29))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.add_tovar)
        self.groupBox = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 70, 601, 181))
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(parent=self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 30, 121, 20))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 60, 121, 20))
        self.label_2.setObjectName("label_2")
        self.manufactureBox = QtWidgets.QComboBox(parent=self.groupBox)
        self.manufactureBox.setGeometry(QtCore.QRect(130, 30, 281, 26))
        self.manufactureBox.setObjectName("comboBox")
        self.label_3 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(440, 30, 51, 20))
        self.label_3.setObjectName("label_3")
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(parent=self.groupBox)
        self.doubleSpinBox.setGeometry(QtCore.QRect(490, 30, 101, 26))
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.lineEdit = QtWidgets.QLineEdit(parent=self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(130, 60, 461, 26))
        self.lineEdit.setObjectName("lineEdit")
        self.checkBox = QtWidgets.QCheckBox(parent=self.groupBox)
        self.checkBox.setGeometry(QtCore.QRect(0, 90, 161, 31))
        self.checkBox.setObjectName("checkBox")
        self.checkBox.toggled.connect(self.garant_toggled)
        self.label_4 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(170, 90, 81, 31))
        self.label_4.setObjectName("label_4")
        self.spinBox = QtWidgets.QSpinBox(parent=self.groupBox)
        self.spinBox.setGeometry(QtCore.QRect(250, 90, 51, 31))
        self.spinBox.setObjectName("spinBox")
        self.spinBox.setEnabled(False)
        self.garantBox = QtWidgets.QComboBox(parent=self.groupBox)
        self.garantBox.setGeometry(QtCore.QRect(310, 90, 131, 31))
        self.garantBox.setObjectName("comboBox_2")
        self.label_5 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(450, 90, 91, 31))
        self.label_5.setObjectName("label_5")
        self.spinBox_2 = QtWidgets.QSpinBox(parent=self.groupBox)
        self.spinBox_2.setGeometry(QtCore.QRect(540, 90, 51, 31))
        self.spinBox_2.setObjectName("spinBox_2")
        self.typeBox = QtWidgets.QComboBox(parent=self.groupBox)
        self.typeBox.setGeometry(QtCore.QRect(100, 140, 291, 26))
        self.typeBox.setObjectName("comboBox_3")
        self.typeBox.currentIndexChanged.connect(self.swaptype)
        self.label_6 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(10, 140, 121, 20))
        self.label_6.setObjectName("label_6")
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.groupBox)
        self.pushButton_2.setGeometry(QtCore.QRect(400, 138, 191, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.charappend)
        self.groupBox_2 = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 260, 601, 401))
        self.groupBox_2.setObjectName("groupBox_2")
        self.groupBox_2.setVisible(False)
        self.groupBox_3 = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 260, 601, 401))
        self.groupBox_3.setObjectName("groupBox_2")
        self.groupBox_3.setVisible(False)
        self.label_7 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_7.setGeometry(QtCore.QRect(10, 30, 111, 20))
        self.label_7.setObjectName("label_7")
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=self.groupBox_2)
        self.lineEdit_2.setGeometry(QtCore.QRect(130, 30, 461, 26))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.tableWidget = QtWidgets.QTableWidget(parent=self.groupBox_2)
        self.tableWidget.setGeometry(QtCore.QRect(10, 70, 321, 301))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.tableWidget_char = QtWidgets.QTableWidget(parent=self.groupBox_3)
        self.tableWidget_char.setGeometry(QtCore.QRect(0, 0, 601, 370))
        self.tableWidget_char.setObjectName("tableWidget")
        self.tableWidget_char.setColumnCount(2)
        self.tableWidget_char.setRowCount(0)
        self.tableWidget_char.verticalHeader().setVisible(False)
        self.tableWidget_char.horizontalHeader().setVisible(False)
        self.label_8 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_8.setGeometry(QtCore.QRect(350, 70, 171, 20))
        self.label_8.setObjectName("label_8")
        self.lineEdit_3 = QtWidgets.QLineEdit(parent=self.groupBox_2)
        self.lineEdit_3.setGeometry(QtCore.QRect(350, 100, 241, 26))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.pushButton_3 = QtWidgets.QPushButton(parent=self.groupBox_2)
        self.pushButton_3.setGeometry(QtCore.QRect(350, 140, 241, 29))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(parent=self.groupBox_2)
        self.pushButton_4.setGeometry(QtCore.QRect(350, 340, 241, 29))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(parent=self.groupBox_2)
        self.pushButton_5.setGeometry(QtCore.QRect(350, 300, 241, 29))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.clicked.connect(self.discard)
        TovarWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=TovarWindow)
        self.statusbar.setObjectName("statusbar")
        TovarWindow.setStatusBar(self.statusbar)

        self.retranslateUi(TovarWindow)
        QtCore.QMetaObject.connectSlotsByName(TovarWindow)

    def retranslateUi(self, TovarWindow):
        _translate = QtCore.QCoreApplication.translate
        TovarWindow.setWindowTitle(_translate("TovarWindow", "Создание нового товарного наименования"))
        self.pushButton.setText(_translate("TovarWindow", "Добавить товар в систему"))
        self.groupBox.setTitle(_translate("TovarWindow", "Основные сведения"))
        
        self.label.setText(_translate("TovarWindow", "Производитель:"))
        self.label_2.setText(_translate("TovarWindow", "Наименование:"))
        self.label_3.setText(_translate("TovarWindow", "Цена:"))
        self.checkBox.setText(_translate("TovarWindow", "Гарантия на товар"))
        self.label_4.setText(_translate("TovarWindow", "Гарантия:"))
        self.label_5.setText(_translate("TovarWindow", "Количество"))
        self.label_6.setText(_translate("TovarWindow", "Тип товара:"))
        self.pushButton_2.setText(_translate("TovarWindow", "Добавить новый тип"))
        self.groupBox_2.setTitle(_translate("TovarWindow", "Создание нового шаблона характеристик товара"))
        self.label_7.setText(_translate("TovarWindow", "Наименование:"))
        self.label_8.setText(_translate("TovarWindow", "Новая характеристика:"))
        self.pushButton_3.setText(_translate("TovarWindow", "Добавить"))
        self.pushButton_4.setText(_translate("TovarWindow", "Применить изменения"))
        self.pushButton_5.setText(_translate("TovarWindow", "Отменить действие"))
        self.manufactureBox.addItem("", userData=None)
        self.typeBox.addItem("", userData=None)
        self.garantBox.addItem("", userData=None)
        c.execute("SELECT Value,ID FROM typetovar")
        types = c.fetchall()
        c.execute("SELECT Value,ID FROM garantytype")
        garantytypes = c.fetchall()
        c.execute("SELECT Value,ID FROM manufacturer")
        manufacturer = c.fetchall()
        for manufact in manufacturer:
            self.manufactureBox.addItem(manufact[0],userData=manufact[1])
        for type in types:
            self.typeBox.addItem(type[0],userData=type[1])
        for garant in garantytypes:
            self.garantBox.addItem(garant[0],userData=garant[1])
        self.garantBox.setEnabled(False)
        self.garantBox.setCurrentIndex(1)
        
    def swaptype(self):
        if self.typeBox.currentText() == "":
            self.groupBox_3.setVisible(False)
            
        elif self.changed == True:
            self.groupBox_3.setVisible(False)
            
        else:
            self.charTableInit()
            self.groupBox_3.setVisible(True)
            
            
    def garant_toggled(self,checked):
        if checked:
            self.spinBox.setEnabled(True)
            self.garantBox.setEnabled(True)
            self.garantBox.setCurrentIndex(2)
        else:
            self.spinBox.setEnabled(False)
            self.spinBox.setValue(0)
            self.garantBox.setEnabled(False)
            self.garantBox.setCurrentIndex(1)
    def charappend(self):
        self.changed = True
        if self.groupBox_3.isVisible():
            self.groupBox_3.setVisible(False)
        self.groupBox_2.setVisible(True)

    def discard(self):
        self.changed = False
        self.groupBox_2.setVisible(False)
    
    def charTableInit(self):
        typeID = self.typeBox.currentData()
        c.execute("SELECT CharID FROM typecharlist WHERE TypeID = %s",(typeID,))
        chars = c.fetchall()
        self.tableWidget_char.setRowCount(len(chars))
        for i in range(len(chars)):
            c.execute("SELECT Value FROM characters WHERE ID = %s",(chars[i][0],))
            itemName = c.fetchone()[0]
            item = QtWidgets.QTableWidgetItem(str(itemName))
            item.setFlags(item.flags() & ~QtCore.Qt.ItemFlag.ItemIsEditable)
            self.tableWidget_char.setItem(i,0,item)
        self.tableWidget_char.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
        self.tableWidget_char.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeMode.Stretch)
    
    def add_tovar(self):
        if self.changed:
            pass
        manufactureID = self.manufactureBox.currentData()
        cost = self.doubleSpinBox.value()
        name = self.lineEdit.text()
        garantType = self.garantBox.currentData()
        garantValue = self.spinBox.value()
        count = self.spinBox_2.value()
        typeID = self.typeBox.currentData()
        if manufactureID == None or cost == 0 or name == "" or (self.checkBox.isChecked() and (garantValue == 0 or (garantType == None or garantType == 1))) or count == 0 or typeID == None:
            QMessageBox.critical(None,"Ошибка","Данные заполнены некорректно",QMessageBox.StandardButton.Ok)
        else:
            print("почти красавчик")
        
    
    def close_event(self, event):
        """Обработчик закрытия окна - открывает окно склада"""
        # Открываем окно склада
        manager.show_sklad()
        # Подтверждаем закрытие текущего окна
        event.accept()

