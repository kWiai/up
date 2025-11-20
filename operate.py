from connector import c,db
from PyQt6 import QtCore, QtGui, QtWidgets
from config import manager
from PyQt6.QtWidgets import QMessageBox
import datetime
from decimal import Decimal

class Ui_Operate(object):
    def __init__(self):
        self.currentBoxIndex = -1
        self.change = False
    def setupUi(self, OperateWindow):
        OperateWindow.setObjectName("OperateWindow")
        OperateWindow.resize(1045, 655)
        self.centralwidget = QtWidgets.QWidget(parent=OperateWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 10, 371, 29))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 50, 171, 29))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.open_orderCreate)
        self.pushButton_3 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(190, 50, 191, 29))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.deleteOrder)
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(150, 90, 71, 20))
        self.label.setObjectName("label")
        self.comboBox = QtWidgets.QComboBox(parent=self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(230, 90, 151, 26))
        self.comboBox.setObjectName("comboBox")
        self.lineEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(10, 130, 371, 26))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.textChanged.connect(self.initOrdersTable)
        self.tableWidget = QtWidgets.QTableWidget(parent=self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 170, 371, 451))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.setEditTriggers(QtWidgets.QTableWidget.EditTrigger.NoEditTriggers)
        self.tableWidget.setSelectionMode(QtWidgets.QTableWidget.SelectionMode.SingleSelection)
        self.tableWidget.setSelectionBehavior(QtWidgets.QTableWidget.SelectionBehavior.SelectRows)
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
        self.tableWidget.itemSelectionChanged.connect(self.initDescriptionTableAndLabels)
        self.tableWidget_2 = QtWidgets.QTableWidget(parent=self.centralwidget)
        self.tableWidget_2.setGeometry(QtCore.QRect(390, 170, 631, 311))
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(5)
        self.tableWidget_2.setRowCount(0)
        self.tableWidget_2.verticalHeader().setVisible(False)
        self.tableWidget_2.setEditTriggers(QtWidgets.QTableWidget.EditTrigger.NoEditTriggers)
        self.tableWidget_2.setSelectionMode(QtWidgets.QTableWidget.SelectionMode.SingleSelection)
        self.tableWidget_2.setSelectionBehavior(QtWidgets.QTableWidget.SelectionBehavior.SelectRows)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(4, item)
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(390, 140, 131, 20))
        self.label_2.setObjectName("label_2")
        self.label_client = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_client.setGeometry(QtCore.QRect(400, 500, 63, 20))
        self.label_client.setText("")
        self.label_client.setObjectName("label_3")
        self.label_order = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_order.setGeometry(QtCore.QRect(400, 530, 63, 20))
        self.label_order.setText("")
        self.label_order.setObjectName("label_4")
        self.label_employer = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_employer.setGeometry(QtCore.QRect(400, 560, 63, 20))
        self.label_employer.setText("")
        self.label_employer.setObjectName("label_5")
        self.label_totalCost = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_totalCost.setGeometry(QtCore.QRect(400, 590, 63, 20))
        self.label_totalCost.setText("")
        self.label_totalCost.setObjectName("label_6")
        self.label_date = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_date.setGeometry(QtCore.QRect(730, 530, 63, 20))
        self.label_date.setText("")
        self.label_date.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(730, 600, 101, 20))
        self.label_8.setObjectName("label_8")
        self.label_8.setVisible(False)
        self.comboBox_2 = QtWidgets.QComboBox(parent=self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(838, 600, 191, 26))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.currentIndexChanged.connect(self.changeStatus)
        OperateWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=OperateWindow)
        self.statusbar.setObjectName("statusbar")
        OperateWindow.setStatusBar(self.statusbar)

        self.retranslateUi(OperateWindow)
        QtCore.QMetaObject.connectSlotsByName(OperateWindow)

    def retranslateUi(self, OperateWindow):
        _translate = QtCore.QCoreApplication.translate
        OperateWindow.setWindowTitle(_translate("OperateWindow", "Модуль оператора"))
        self.pushButton.setText(_translate("OperateWindow", "Посмотреть список товартов на складе"))
        self.pushButton.clicked.connect(self.open_sklad)
        self.pushButton_2.setText(_translate("OperateWindow", "Создать новый заказ"))
        self.pushButton_3.setText(_translate("OperateWindow", "Удалить заказ из системы"))
        self.label.setText(_translate("OperateWindow", "Поиск по:"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("OperateWindow", "Клиент"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("OperateWindow", "Номер заказа"))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("OperateWindow", "Артикул"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("OperateWindow", "Наименование"))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("OperateWindow", "Цена руб."))
        item = self.tableWidget_2.horizontalHeaderItem(3)
        item.setText(_translate("OperateWindow", "Кол-во"))
        item = self.tableWidget_2.horizontalHeaderItem(4)
        item.setText(_translate("OperateWindow", "Стоимость руб."))
        self.label_2.setText(_translate("OperateWindow", "Сведения о заказе"))
        self.label_8.setText(_translate("OperateWindow", "Статус заказа"))
        self.comboBox.addItems(["...по клиенту","...по номеру заказа"])
        self.change = True
        c.execute("SELECT Value FROM orderstatus")
        sr = c.fetchall()
        for i in range(len(sr)):        
            self.comboBox_2.addItem(str(sr[i][0]))
            print(sr[i][0])
        self.change = False
        self.comboBox_2.setVisible(False)
        self.initOrdersTable()
    
    def open_sklad(self):
        manager.show_sklad()
    
    def open_orderCreate(self):
        manager.show_orderCreateWindow()

    def deleteOrder(self):
        print("бабожир")

    def initDescriptionTableAndLabels(self):
        self.change = True
        self.tableWidget_2.clearContents()
        selected_items = self.tableWidget.selectedItems()
        if selected_items:
            self.label_8.setVisible(True)
            self.comboBox_2.setVisible(True)
            self.tableWidget_2.setVisible(True)
            order_text = selected_items[1].text()
            orderID = int(order_text.split()[1])
            self.label_order.setText(f"Заказ: {orderID}")
            self.label_order.adjustSize()
            c.execute("SELECT * FROM ordershopcase WHERE OrderID = %s",(orderID,))
            ordersChar = c.fetchall()
            c.execute("SELECT DateCreate, ClientID, StatusID FROM orders WHERE ID = %s",(orderID,))
            res = c.fetchone()
            date = res[0]
            c.execute("SELECT Surname,Name,Patronymic FROM users WHERE ID = %s",(res[1],))
            cr = c.fetchone()
            client = f"{cr[0]} {cr[1]} {cr[2]}"
            status = res[2]
            c.execute("SELECT Surname,Name,Patronymic FROM users WHERE ID = %s",(manager.get_current_userID(),))
            er = c.fetchone()
            employer = f"{er[0]} {er[1]} {er[2]}"

            self.label_employer.setText(f"Сотрудник: {employer}")
            self.label_employer.adjustSize()
            self.label_client.setText(f"Клиент: {client}")
            self.label_client.adjustSize()
            self.label_date.setText(f"Дата проведения заказа: {date.strftime('%d.%m.%Y %H:%M:%S')}")
            self.label_date.adjustSize()
            self.tableWidget_2.setRowCount(len(ordersChar))
            
            self.comboBox_2.setCurrentIndex(int(status)-1)
            self.currentBoxIndex = int(status)-1
            sumTovar = 0
            for i in range(len(ordersChar)):
                item = QtWidgets.QTableWidgetItem(str(ordersChar[i][1]))
                self.tableWidget_2.setItem(i,0,item)

                c.execute("SELECT Name,ManufacturerID,TypeID,CostValue FROM tovar WHERE ID = %s",(ordersChar[i][1],))
                res = c.fetchone()
                name = res[0]
                c.execute("SELECT Value FROM manufacturer WHERE ID = %s",(res[1],))
                manufacturer = c.fetchone()[0]
                c.execute("SELECT Value FROM typetovar WHERE ID = %s",(res[2],))
                type = c.fetchone()[0]
                cost =  res[3]

                item = QtWidgets.QTableWidgetItem(f"{type} {manufacturer} {name}")
                self.tableWidget_2.setItem(i,1,item)

                item = QtWidgets.QTableWidgetItem(str(cost))
                self.tableWidget_2.setItem(i,2,item)

                item = QtWidgets.QTableWidgetItem(str(ordersChar[i][2]))
                self.tableWidget_2.setItem(i,3,item)

                sumTovar+=ordersChar[i][3]
                item = QtWidgets.QTableWidgetItem(str(ordersChar[i][3]))
                self.tableWidget_2.setItem(i,4,item)            
        
                self.tableWidget_2.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
                self.tableWidget_2.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeMode.Stretch)
                self.tableWidget_2.horizontalHeader().setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeMode.Stretch)
            
            self.label_totalCost.setText(f"Стоимость заказа к оплате: {float(sumTovar)}руб.")
            self.label_totalCost.adjustSize()
        self.change = False
                
    def changeStatus(self):
        if self.change:
            pass
        else:
            reply = QtWidgets.QMessageBox.question(
                None,
                "Подтверждение",
                "Вы уверены?",
                QtWidgets.QMessageBox.StandardButton.Yes | 
                QtWidgets.QMessageBox.StandardButton.No,
                QtWidgets.QMessageBox.StandardButton.No  # кнопка по умолчанию
            )

            if reply == QtWidgets.QMessageBox.StandardButton.Yes:
                self.currentBoxIndex = self.comboBox_2.currentIndex()
                selected_items = self.tableWidget.selectedItems()
                
                if selected_items and len(selected_items) > 1:
                    # Правильно извлекаем ID заказа
                    order_text = selected_items[1].text()  # Получаем текст вида "№ 123 от 13.11.2025"
                    
                    # Извлекаем число после "№ "
                    try:
                        # Разделяем текст по пробелам и берем вторую часть (число)
                        orderID = int(order_text.split()[1])
                        
                        # В базе данных индексы статусов начинаются с 1, а currentIndex с 0
                        status_id = self.currentBoxIndex + 1
                        
                        c.execute("UPDATE orders SET StatusID = %s WHERE ID = %s", (status_id, orderID))
                        db.commit()
                        print(f"Статус заказа {orderID} изменен на {status_id}")
                        
                    except (ValueError, IndexError) as e:
                        print(f"Ошибка при извлечении ID заказа: {e}")
                    except Exception as e:
                        print(f"Ошибка при обновлении статуса: {e}")
                else:
                    print("Не выбран заказ для изменения статуса")

            else:
                self.change = True
                self.comboBox_2.setCurrentIndex(self.currentBoxIndex)
                self.change = False

    def initOrdersTable(self):
        if self.lineEdit.text() == "":
            c.execute("SELECT * FROM orders")
        elif self.comboBox.currentIndex() == 1:
            c.execute("SELECT * FROM orders WHERE ID = %s", (self.lineEdit.text(),))
        elif self.comboBox.currentIndex() == 0:
            user = self.lineEdit.text()
            # Используем UNION для объединения результатов
            query = """
                SELECT o.* FROM orders o
                WHERE o.ClientID IN (
                    SELECT ID FROM users WHERE Name = %s
                    UNION
                    SELECT ID FROM users WHERE Surname = %s
                    UNION
                    SELECT ID FROM users WHERE Patronymic = %s
                )
            """
            c.execute(query, (user, user, user))
            
        res = c.fetchall()
        if len(res) == 0:
            self.label_client.setText("")
            self.label_date.setText("")
            self.label_employer.setText("")
            self.label_totalCost.setText("")
            self.label_order.setText("")
            self.label_8.setVisible(False)
            self.comboBox_2.setVisible(False)
            self.tableWidget_2.setRowCount(0)
        orders = []
        for r in res:
            orders.append([r[0],r[1],r[2],r[3],r[4],r[5]])
        self.tableWidget.setRowCount(len(orders))
        for i in range(len(orders)):
            c.execute("SELECT Name,Surname,Patronymic FROM users WHERE ID = %s",(orders[i][3],))
            client = c.fetchone()
            item = QtWidgets.QTableWidgetItem(f"{client[1]} {client[0]} {client[2]}")
            self.tableWidget.setItem(i,0,item)
            dt = orders[i][1]

            item = QtWidgets.QTableWidgetItem(f"№ {orders[i][0]} от {dt.strftime('%d.%m.%Y')}")
            self.tableWidget.setItem(i,1,item)
            self.tableWidget.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
            self.tableWidget.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeMode.Stretch)
        