import sys
from PyQt6 import QtWidgets


class WindowManager:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(WindowManager, cls).__new__(cls)
            cls._instance._initialized = False
        return cls._instance
    
    def __init__(self):
        if not self._initialized:
            self.app = QtWidgets.QApplication(sys.argv)
            self.current_window = None
            self.current_user_id = None
            self._initialized = True
            self.suppress_order_close_event = False  # Флаг для подавления события
    
    def set_current_userID(self,userID):
        self.current_user_id = userID
        
    def get_current_userID(self):
        return self.current_user_id
    
    def set_current_RoleID(self,roleID):
        self.current_role_id = roleID
        
    def get_current_RoleID(self):
        return self.current_role_id
    
    def show_registration(self):
        """Показать окно регистрации"""
        from reg import Ui_Reg
        if self.current_window:
            self.current_window.close()
            
        self.reg_window = QtWidgets.QMainWindow()
        self.reg_ui = Ui_Reg()
        self.reg_ui.setupUi(self.reg_window)
        # self.reg_ui.pushButton.clicked.connect(self.show_sklad)
        
        self.current_window = self.reg_window
        self.reg_window.show()
    
    def show_sklad(self):
        from sklad import Ui_Sklad
        """Показать окно склада"""
        if self.current_window:
            self.current_window.close()

        self.sklad_window = QtWidgets.QMainWindow()
        self.sklad_ui = Ui_Sklad()
        self.sklad_ui.setupUi(self.sklad_window)

        self.sklad_window.closeEvent = self.sklad_close_event
        
        self.current_window = self.sklad_window
        self.sklad_window.show()

    def show_tovar_append(self):
        from tovar import Ui_Tovar
        if self.current_window:
            self.current_window.close()

        self.tovar_window = QtWidgets.QMainWindow()
        self.tovar_ui = Ui_Tovar()
        self.tovar_ui.setupUi(self.tovar_window)
        
        self.tovar_window.closeEvent = self.tovar_close_event

        self.current_window = self.tovar_window
        self.tovar_window.show()

    def tovar_close_event(self, event):
        self.show_sklad()
        event.accept()
    
    def sklad_close_event(self,event):
        if self.get_current_RoleID() == 1:
            self.show_operateWindow()
                # Подтверждаем закрытие текущего окна
            event.accept()
    
    def order_close_event(self, event):
        # Если флаг установлен, не выполняем стандартную логику
        if not self.suppress_order_close_event:
            self.show_operateWindow()
        event.accept()
    
    def client_close_event(self, event):
        self.show_orderCreateWindow()
        event.accept()


    def show_operateWindow(self):
        from operate import Ui_Operate
        if self.current_window:
            self.current_window.close()
        self.operate_window = QtWidgets.QMainWindow()
        self.operate_ui = Ui_Operate()
        self.operate_ui.setupUi(self.operate_window)
        self.current_window = self.operate_window
        self.operate_window.show()

    def show_orderCreateWindow(self):
        from orderCreate import Ui_OrderCreate
        if self.current_window:
            self.current_window.close()
        self.orderCreate_window = QtWidgets.QMainWindow()
        self.orderCreate_ui = Ui_OrderCreate()
        self.orderCreate_ui.setupUi(self.orderCreate_window)
        self.orderCreate_window.closeEvent = self.order_close_event
        self.current_window = self.orderCreate_window
        self.orderCreate_window.show()
    
    def show_clientCreateWindow(self):
        from client import Ui_ClientCreate
        # Временно отключаем обработку закрытия окна заказа
        self.suppress_order_close_event = True
        
        if self.current_window:
            self.current_window.close()
            
        self.clientCreate_window = QtWidgets.QMainWindow()
        self.clientCreate_ui = Ui_ClientCreate()
        self.clientCreate_ui.setupUi(self.clientCreate_window)
        self.clientCreate_window.closeEvent = self.client_close_event
        self.current_window = self.clientCreate_window
        self.clientCreate_window.show()
        
        # Включаем обратно обработку закрытия
        self.suppress_order_close_event = False

    def run(self):
        """Запуск приложения"""
        self.show_registration()
        sys.exit(self.app.exec())
    
    