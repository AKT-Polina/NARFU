import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import Qt
from PySide6.QtGui import QColor


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # Настройка главного окна
        self.setWindowTitle("Отслеживание финансов")
        self.resize(800, 600)
        
        # Боковое меню
        self.create_sidebar()
        
        # Центральная область
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)
        
        # Раздел работы с данными
        self.data_layout = QVBoxLayout()
        self.table_view = QTableView()
        self.data_layout.addWidget(self.table_view)
        
        # Кнопки управления
        self.button_layout = QHBoxLayout()
        self.add_button = QPushButton("Добавить")
        self.delete_button = QPushButton("Удалить")
        self.edit_button = QPushButton("Изменить")
        self.button_layout.addWidget(self.add_button)
        self.button_layout.addWidget(self.delete_button)
        self.button_layout.addWidget(self.edit_button)
        
        # Добавляем кнопки в центральную часть
        self.data_layout.addLayout(self.button_layout)
        
        # Основной макет
        self.main_layout = QVBoxLayout(self.central_widget)
        self.main_layout.addLayout(self.data_layout)
    
    def create_sidebar(self):
        sidebar = QListWidget(self)
        sidebar.insertItem(0, "Работа с данными")
        sidebar.insertItem(1, "О программе")
        sidebar.currentRowChanged.connect(self.sidebar_clicked)
        sidebar.setMaximumWidth(150)
        self.addDockWidget(Qt.LeftDockWidgetArea, sidebar)
    
    def sidebar_clicked(self, index):
        if index == 0:
            self.show_data_section()
        elif index == 1:
            self.show_about_section()
    
    def show_data_section(self):
        pass
    
    def show_about_section(self):
        pass
