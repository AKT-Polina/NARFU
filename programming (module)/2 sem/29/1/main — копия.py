import sys
import pandas as pd
from PySide6.QtWidgets import *
from PySide6.QtCore import QDate
from PySide6.QtCore import QAbstractTableModel, Qt
from PySide6.QtGui import QColor, QStandardItemModel


class PandasModel(QAbstractTableModel):
    def __init__(self, data):
        QAbstractTableModel.__init__(self)
        self._data = data

    def rowCount(self, parent=None):
        return len(self._data.values)

    def columnCount(self, parent=None):
        return self._data.columns.size

    def data(self, index, role=Qt.DisplayRole):
        if index.isValid():
            if role == Qt.DisplayRole or role == Qt.EditRole:
                return str(self._data.iloc[index.row(), index.column()])
            if role == Qt.BackgroundRole:
                value = float(self._data.iloc[index.row()]['amount'])
                if value > 0:
                    return QColor('#90ee90')  # Зелёный цвет для дохода
                else:
                    return QColor('#ff9999')  # Красный цвет для расхода
        return None

    def headerData(self, col, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self._data.columns[col]
        return None

    def setData(self, index, value, role):
        if role == Qt.EditRole:
            self._data.at[index.row(), index.column()] = value
            return True
        return False

    def flags(self, index):
        return Qt.ItemIsEditable | Qt.ItemIsEnabled | Qt.ItemIsSelectable


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
        self.load_data()
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

        # Подключение сигналов
        self.add_button.clicked.connect(self.add_transaction)
        self.delete_button.clicked.connect(self.delete_transaction)
        self.table_view.doubleClicked.connect(self.on_double_click)

    def create_sidebar(self):
        sidebar = QListWidget(self)
        sidebar.insertItem(0, "Работа с данными")
        sidebar.insertItem(1, "О программе")
        sidebar.currentRowChanged.connect(self.sidebar_clicked)
        sidebar.setMaximumWidth(150)

        # Оборачиваем QListWidget в QDockWidget
        dock_widget = QDockWidget("Боковое меню", self)
        dock_widget.setWidget(sidebar)
        self.addDockWidget(Qt.LeftDockWidgetArea, dock_widget)

    def sidebar_clicked(self, index):
        if index == 0:
            self.show_data_section()
        elif index == 1:
            self.show_about_section()

    def show_data_section(self):
        self.load_data()

    def show_about_section(self):
        about_text = QLabel(
            "<h1>О программе</h1>"
            "<p>Это простое приложение для отслеживания ваших "
            "финансов.</p>",
            alignment=Qt.AlignCenter,
        )
        self.main_layout.removeItem(self.data_layout)
        self.main_layout.addWidget(about_text)

    def load_data(self):
        try:
            df = pd.read_csv('database.csv')
            self.model = PandasModel(df)
            self.table_view.setModel(self.model)
        except FileNotFoundError:
            print("Файл базы данных не найден.")

    def add_transaction(self):
        dialog = AddTransactionDialog(self)
        if dialog.exec():
            new_row = {
                'id': len(self.model._data) + 1,
                'date': dialog.date_edit.text(),
                'type': dialog.type_combo.currentText(),
                'amount': float(dialog.amount_edit.text()),
                'balance': float(dialog.balance_edit.text()),
                'comment': dialog.comment_edit.text()
            }
            df = self.model._data.append(new_row, ignore_index=True)
            df.to_csv('database.csv', index=False)
            self.load_data()

    def delete_transaction(self):
        selected_index = self.table_view.selectionModel().selectedRows()[0].row()
        df = self.model._data
        df.drop(selected_index, inplace=True)
        df.reset_index(drop=True, inplace=True)
        self.model.layoutChanged.emit()
        df.to_csv('database.csv', index=False)

    def on_double_click(self, index):
        self.table_view.edit(index)


class AddTransactionDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Добавить транзакцию")
        layout = QFormLayout(self)

        self.date_edit = QDateEdit(self)
        self.date_edit.setCalendarPopup(True)
        self.date_edit.setDate(QDate.currentDate())
        layout.addRow("Дата:", self.date_edit)

        self.type_combo = QComboBox(self)
        self.type_combo.addItems(["Доход", "Расход"])
        layout.addRow("Тип:", self.type_combo)

        self.amount_edit = QLineEdit(self)
        layout.addRow("Сумма:", self.amount_edit)

        self.balance_edit = QLineEdit(self)
        layout.addRow("Баланс:", self.balance_edit)

        self.comment_edit = QLineEdit(self)
        layout.addRow("Комментарий:", self.comment_edit)

        button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, self)
        button_box.accepted.connect(self.accept)
        button_box.rejected.connect(self.reject)
        layout.addRow(button_box)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
