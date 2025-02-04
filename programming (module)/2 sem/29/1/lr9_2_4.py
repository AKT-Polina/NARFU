import sys
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QGridLayout,
    QPushButton,
    QLineEdit
)
#Добавлен вызов для изменения цвета кнопок
from PySide6.QtGui import QColor

class CalculatorGrid(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        main_layout = QVBoxLayout()  # Основной вертикальный бокс-лайаут
        self.setLayout(main_layout)

        # Поле ввода
        self.line_edit = QLineEdit()
        main_layout.addWidget(self.line_edit)

        # Сетка кнопок
        grid_layout = QGridLayout()
        main_layout.addLayout(grid_layout)

        self.buttons = []
        #Объявление массива надписей на кнопках.
        buttons_data = [
            ('7', '8', '9', '+'),
            ('4', '5', '6', '-'),
            ('1', '2', '3', '*'),
            ('C', '0', '=', '/')
        ]
        #Создание и размещение кнопок
        row = 0
        for data_row in buttons_data:
            col = 0
            for label in data_row:
                button = QPushButton(label)
                button.clicked.connect(lambda _, btn=button: self.on_button_click(btn))
                grid_layout.addWidget(button, row, col)
                self.buttons.append(button)
                # Устанавливаем цвет кнопки при создании
                if not label.isnumeric():  # Если кнопка не числовая
                    button.setStyleSheet(f'background-color: {QColor(255, 165, 0).name()}')  # оранжевый цвет
                else:
                    button.setStyleSheet(f'background-color: {QColor(200, 200, 200).name()}')  # Серый цвет

                col += 1
            row += 1

        self.show()

    def on_button_click(self, button):
        '''Обработчик нажатия кнопки.'''
        #Если нажата кнопка С - очищаем QLineEdit
        if button.text() == 'C':
            self.line_edit.clear()
        # Если нажата кнопка '=' - считываем строку и считаем значение
        elif button.text() == '=':
            text = self.line_edit.text()
            result = eval(text)
            self.line_edit.setText(text+'='+str(result))
        else:
            string = self.line_edit.text()
            #Добавлена проверка на наличие знака =. Если он есть, значит формула уже была посчитана и необходимо
            #очистить поле ввода
            find_eqval= string.find('=')
            if find_eqval != -1:
                string = ''
            string +=   button.text()
            self.line_edit.setText(string)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CalculatorGrid()
    sys.exit(app.exec())