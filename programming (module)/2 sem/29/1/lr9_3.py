import sys
from datetime import date
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QListWidget,
    QListWidgetItem,
    QLineEdit,
    QPushButton,
    QHBoxLayout,
    QToolBar,
)
from PySide6.QtGui import QAction, QIcon
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMessageBox


class TodoApp(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # Настройка главного окна
        self.setWindowTitle("ToDo List")
        self.resize(400, 300)

        # Создание вертикального макета
        vbox = QVBoxLayout()

        # Панель инструментов
        toolbar = QToolBar("Панель инструментов")
        vbox.addWidget(toolbar)

        # Действие для добавления задачи
        add_action = QAction(QIcon.fromTheme("list-add"), "Добавить задачу", self)
        add_action.triggered.connect(self.add_task)
        toolbar.addAction(add_action)

        # Действие для удаления задачи
        delete_action = QAction(QIcon.fromTheme("edit-delete"), "Удалить задачу", self)
        delete_action.triggered.connect(self.delete_task)
        toolbar.addAction(delete_action)

        # Разделитель
        toolbar.addSeparator()

        # Действие для вывода информации о программе
        about_action = QAction(QIcon.fromTheme("help-about"), "О программе", self)
        about_action.triggered.connect(self.about_dialog)
        toolbar.addAction(about_action)

        # Поле для ввода новой задачи
        self.task_input = QLineEdit()
        vbox.addWidget(self.task_input)

        # Кнопки для добавления и удаления задач
        hbox_buttons = QHBoxLayout()
        add_button = QPushButton("Добавить задачу")
        delete_button = QPushButton("Удалить задачу")
        hbox_buttons.addWidget(add_button)
        hbox_buttons.addWidget(delete_button)
        vbox.addLayout(hbox_buttons)

        # Список задач
        self.tasks_list = QListWidget()
        vbox.addWidget(self.tasks_list)

        # Подключение сигналов кнопок
        add_button.clicked.connect(self.add_task)
        delete_button.clicked.connect(self.delete_task)

        # Установка основного макета
        self.setLayout(vbox)

        # Показать окно
        self.show()

    def add_task(self):
        task_text = self.task_input.text().strip()
        if task_text:
            item = QListWidgetItem(task_text)
            item.setCheckState(Qt.Unchecked)  # По умолчанию задача не выполнена
            self.tasks_list.addItem(item)
            self.task_input.clear()

    def delete_task(self):
        selected_items = self.tasks_list.selectedItems()
        for item in selected_items:
            index = self.tasks_list.row(item)
            self.tasks_list.takeItem(index)

    def about_dialog(self):
        today = date.today().strftime("%d.%m.%Y")
        message_box = QMessageBox()
        message_box.setWindowTitle("О программе")
        message_box.setText(
            f"Текстовый редактор\nАвтор: Абрамова П.А.\nВерсия: 1.0\nДата создания: {today}"
        )
        message_box.exec()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    todo_app = TodoApp()
    sys.exit(app.exec())
