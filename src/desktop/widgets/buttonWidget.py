from PySide6.QtCore import QSize
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QPushButton


class ButtonWidget(QPushButton):

    def __init__(self):
        super().__init__("Загрузить файл")
        self.setFixedSize(QSize(200, 50))

        custom_font = QFont("Arial", 14, QFont.Weight.Bold)
        self.setFont(custom_font)

class ButtonGenerate(QPushButton):

    def __init__(self):
        super().__init__("Генерация лабиринта")
        self.setFixedSize(QSize(300, 50))

        custom_font = QFont("Arial", 14, QFont.Weight.Bold)
        self.setFont(custom_font)
