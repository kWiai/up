
from PyQt6 import QtCore, QtGui, QtWidgets
from connector import c
from config import manager


class Ui_Sklad(object):
    def setupUi(self, SkladWindow):
        SkladWindow.setObjectName("SkladWindow")
        SkladWindow.resize(1017, 663)
        self.centralwidget = QtWidgets.QWidget(parent=SkladWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.SkladWindow = SkladWindow
        self.SkladWindow.closeEvent = self.close_event
        if manager.get_current_RoleID() == 2:
            self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
            self.pushButton.setGeometry(QtCore.QRect(10, 0, 201, 29))
            self.pushButton.setObjectName("pushButton")
            self.pushButton.clicked.connect(self.appendTovar)
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 40, 71, 20))
        self.label.setObjectName("label")
        self.comboBox = QtWidgets.QComboBox(parent=self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(100, 40, 151, 26))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItems(["...по артикулу","...по названию"])
        self.groupBox = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(680, 20, 321, 581))
        self.groupBox.setObjectName("groupBox")
        self.tableWidget_2 = QtWidgets.QTableWidget(parent=self.groupBox)
        self.tableWidget_2.setGeometry(QtCore.QRect(0, 20, 321, 561))
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(0)
        self.tableWidget_2.setRowCount(0)
        self.tableWidget_2.verticalHeader().setVisible(False)
        self.tableWidget_2.horizontalHeader().setVisible(False)
        self.tableWidget_2.setEditTriggers(QtWidgets.QTableWidget.EditTrigger.NoEditTriggers)
        self.tableWidget_2.setSelectionMode(QtWidgets.QTableWidget.SelectionMode.SingleSelection)
        self.tableWidget_2.setSelectionBehavior(QtWidgets.QTableWidget.SelectionBehavior.SelectRows)
        self.lineEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(250, 40, 421, 26))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.textChanged.connect(self.initProductTableData)
        self.groupBox_2 = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 80, 631, 521))
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.tableWidget = QtWidgets.QTableWidget(parent=self.groupBox_2)
        self.tableWidget.setGeometry(QtCore.QRect(0, 0, 631, 521))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setColumnWidth(1,110)
        self.tableWidget.setColumnWidth(3,150)
        self.tableWidget.setColumnWidth(4,169)
        self.tableWidget.setRowCount(0)
        self.tableWidget.horizontalHeader().setStyleSheet("""
            QHeaderView::section {
                background-color: #d3d3d3;
                color: #000000;
                font-weight: bold;
                padding: 8px;
                border: 1px solid #a9a9a9;
                font-size: 12px;
            }
        """)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.setEditTriggers(QtWidgets.QTableWidget.EditTrigger.NoEditTriggers)
        self.tableWidget.setSelectionMode(QtWidgets.QTableWidget.SelectionMode.SingleSelection)
        self.tableWidget.setSelectionBehavior(QtWidgets.QTableWidget.SelectionBehavior.SelectRows)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        self.tableWidget.itemSelectionChanged.connect(self.initCharacterTableData)
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 610, 63, 20))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(680, 610, 111, 20))
        self.label_3.setObjectName("label_3")
        SkladWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=SkladWindow)
        self.statusbar.setObjectName("statusbar")
        SkladWindow.setStatusBar(self.statusbar)

        self.retranslateUi(SkladWindow)
        QtCore.QMetaObject.connectSlotsByName(SkladWindow)

    def retranslateUi(self, SkladWindow):
        _translate = QtCore.QCoreApplication.translate
        SkladWindow.setWindowTitle(_translate("SkladWindow", "Форма складского учета"))
        if manager.get_current_RoleID() == 2:
            self.pushButton.setText(_translate("SkladWindow", "Добавить товар в систему"))
        self.label.setText(_translate("SkladWindow", "Поиск по:"))
        self.groupBox.setTitle(_translate("SkladWindow", "Характеристики товара"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("SkladWindow", "Артикул"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("SkladWindow", "Наименование"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("SkladWindow", "Цена"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("SkladWindow", "Кол-во на складе"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("SkladWindow", "Гарантия"))
        self.initProductTableData()
        c.execute("SELECT RoleID,Name,Surname,Patronymic FROM users WHERE ID = %s",(manager.get_current_userID(),))
        res = c.fetchone()
        c.execute("SELECT Value FROM roles WHERE ID = %s",(res[0],))
        
        self.label_2.setText(_translate("SkladWindow", "Версия"))
        self.label_3.setText(_translate("SkladWindow", f"Пользователь: {res[1]} {res[2]} {res[3]}    Роль: {c.fetchone()[0]}"))
        self.label_3.adjustSize()

    def initProductTableData(self):
        if self.lineEdit.text() == "":
            c.execute("SELECT * FROM Tovar")
            # (["...по артикулу",...по названию"])
        elif self.comboBox.currentIndex() == 0:
            c.execute("SELECT * FROM tovar WHERE ID = %s",(self.lineEdit.text(),))

        elif self.comboBox.currentIndex() == 1:
            c.execute("SELECT * FROM tovar INNER JOIN manufacturer ON tovar.ManufacturerID = manufacturer.ID INNER JOIN typetovar ON tovar.TypeID = typetovar.ID WHERE CONCAT(typetovar.Value,' ',manufacturer.Value,' ',tovar.Name) LIKE '%"+self.lineEdit.text()+"%'")

        result = c.fetchall()

        self.tableWidget.setRowCount(len(result))
        for i in range(len(result)):
            item = QtWidgets.QTableWidgetItem(str(result[i][0]))
            self.tableWidget.setItem(i,0,item)
            
            c.execute("SELECT Value FROM typetovar WHERE ID = %s",(result[i][3],))
            type_name = c.fetchone()[0]
            c.execute("SELECT Value FROM manufacturer WHERE ID = %s",(result[i][2],))
            manufacture_name = c.fetchone()[0]
            
            item = QtWidgets.QTableWidgetItem(f"{type_name} {manufacture_name} {result[i][1]}")
            self.tableWidget.setItem(i,1,item)
            
            item = QtWidgets.QTableWidgetItem(str(result[i][4]))
            self.tableWidget.setItem(i,2,item)
            item = QtWidgets.QTableWidgetItem(str(result[i][7]))
            self.tableWidget.setItem(i,3,item)
            
            c.execute("SELECT Value FROM garantytype WHERE ID = %s",(result[i][6],))
            garant_type = c.fetchone()[0]
            item = QtWidgets.QTableWidgetItem(f"{result[i][5]} {garant_type}")
            self.tableWidget.setItem(i,4,item)

    def initCharacterTableData(self):
        self.tableWidget_2.clearContents()
        selected_items = self.tableWidget.selectedItems()
        if selected_items:
            artikle = selected_items[0].text()
            c.execute("SELECT CharID FROM charvalues WHERE TovarID = %s", (artikle,))
            charlist = c.fetchall()  
            
            self.tableWidget_2.setRowCount(len(charlist))
            self.tableWidget_2.setColumnCount(2)
            
            for i in range(len(charlist)):
                charID = str(charlist[i][0])
                
                c.execute("SELECT Value FROM characters WHERE ID = %s", (charID,))
                char_name_result = c.fetchone()  
                if char_name_result:
                    char_name = char_name_result[0]
                    item = QtWidgets.QTableWidgetItem(char_name)
                    self.tableWidget_2.setItem(i, 0, item)
                
                c.execute("SELECT Value FROM charvalues WHERE TovarID = %s AND CharID = %s", (artikle, charID))
                char_value_result = c.fetchone()  
                if char_value_result:
                    char_value = char_value_result[0]
                    item = QtWidgets.QTableWidgetItem(char_value)
                    self.tableWidget_2.setItem(i, 1, item)
        
        self.tableWidget_2.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
        self.tableWidget_2.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeMode.Stretch)

    def appendTovar(self):
        manager.show_tovar_append()   
    
    def close_event(self, event):
        if manager.get_current_RoleID() == 1:
            manager.show_operateWindow()
                # Подтверждаем закрытие текущего окна
            event.accept()