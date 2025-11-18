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
    
    def set_current_userID(self,userID):
        self.current_user_id = userID
        
    def get_current_userID(self):
        return self.current_user_id
    
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
        
    def run(self):
        """Запуск приложения"""
        self.show_registration()
        sys.exit(self.app.exec())
    
    