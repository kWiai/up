import sys
from PyQt6 import QtWidgets
from reg import Ui_Reg
from sklad import Ui_Sklad  # Импортируем класс второго окна

class WindowManager:
    def __init__(self):
        self.app = QtWidgets.QApplication(sys.argv)
        self.current_window = None
        
    def show_registration(self):
        """Показать окно регистрации"""
        if self.current_window:
            self.current_window.close()
            
        self.reg_window = QtWidgets.QMainWindow()
        self.reg_ui = Ui_Reg()
        self.reg_ui.setupUi(self.reg_window)
        
        # Подключаем кнопку для перехода на склад
        self.reg_ui.pushButton.clicked.connect(self.show_sklad)
        
        self.current_window = self.reg_window
        self.reg_window.show()
    
    def show_sklad(self):
        """Показать окно склада"""
        if self.current_window:
            self.current_window.close()
            
        self.sklad_window = QtWidgets.QMainWindow()
        self.sklad_ui = Ui_Sklad()
        self.sklad_ui.setupUi(self.sklad_window)
        
        # Подключаем кнопку для возврата к регистрации (если есть)
        # self.sklad_ui.backButton.clicked.connect(self.show_registration)
        
        self.current_window = self.sklad_window
        self.sklad_window.show()
    
    def run(self):
        """Запуск приложения"""
        self.show_registration()
        sys.exit(self.app.exec())

manager = WindowManager()
    