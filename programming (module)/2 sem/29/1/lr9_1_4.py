import sys
from PySide6.QtWidgets import (
    QApplication,
    QLabel,
    QLineEdit,
    QMainWindow,
    QVBoxLayout,
    QWidget, QPushButton,
)
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        self.label1 = QLabel('Введите значение в метрах')
        self.input = QLineEdit()
        self.label2 = QLabel()
        self.label3 = QLabel()
        self.label4 = QLabel()
        self.button1 = QPushButton("Перевести")

        self.button1.clicked.connect(self.the_button_was_clicked)


        layout = QVBoxLayout()
        layout.addWidget(self.label1)
        layout.addWidget(self.input)
        layout.addWidget(self.button1)
        layout.addWidget(self.label2)
        layout.addWidget(self.label3)
        layout.addWidget(self.label4)

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)
    def the_button_was_clicked(self):
        size = int(self.input.text())
        self.label2.setText(str(size*10) + ' дециметров')
        self.label3.setText(str(size * 100) + ' сантиметров')
        self.label4.setText(str(size * 1000) + ' миллиметров')

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
