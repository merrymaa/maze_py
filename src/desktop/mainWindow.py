from PySide6.QtCore import QSize
from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QFileDialog, QLineEdit, QLabel, \
    QHBoxLayout, QMessageBox
from PySide6.QtGui import QIcon, Qt, QIntValidator

from desktop.widgets.buttonWidget import ButtonWidget, ButtonGenerate
from desktop.widgets.fieldWidget import FieldWidget


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Maze")
        self.setWindowIcon(QIcon("icons/icon-maze.png"))
        self.setFixedSize(QSize(900, 700))

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        main_layout = QHBoxLayout(central_widget)

        # Левая панель
        left_panel = QWidget()
        left_layout = QVBoxLayout(left_panel)
        left_layout.setAlignment(Qt.AlignTop)

        # Поля ввода размеров
        label_rows = QLabel("Строки:")
        self.rows_edit = QLineEdit()
        # self.rows_edit.setPlaceholderText("строки")
        self.rows_edit.setValidator(QIntValidator())
        self.rows_edit.setFixedWidth(100)

        label_cols = QLabel("Столбцы:")
        self.cols_edit = QLineEdit()
        # self.cols_edit.setPlaceholderText("столбцы")
        self.cols_edit.setValidator(QIntValidator())
        self.cols_edit.setFixedWidth(100)

        left_layout.addWidget(label_rows)
        left_layout.addWidget(self.rows_edit)
        left_layout.addSpacing(10)
        left_layout.addWidget(label_cols)
        left_layout.addWidget(self.cols_edit)
        left_layout.addSpacing(20)

        # Кнопки
        self.button = ButtonWidget()
        self.button_generate = ButtonGenerate()

        left_layout.addWidget(self.button)
        left_layout.addSpacing(10)
        left_layout.addWidget(self.button_generate)

        # Правая панель
        self.field = FieldWidget()

        main_layout.addWidget(left_panel, stretch=1)  # левая панель занимает 1 часть ширины
        main_layout.addWidget(self.field, stretch=3, alignment=Qt.AlignCenter)  # поле отрисовки занимает 3 части

        self.button.clicked.connect(self.load_maze)
        self.button_generate.clicked.connect(self.draw_maze)

    def load_maze(self):
        file_path, _ = QFileDialog.getOpenFileName(self,
                                                   "Выберите файл лабиринта")
        if file_path:
            self.field.parse_file(file_path)
            self.field.draw_maze()

    def draw_maze(self):
        if not self.rows_edit.text() or not self.cols_edit.text():
            QMessageBox.warning(self, "Упс", "Укажите размеры лабиринта")
            return

        rows = int(self.rows_edit.text().strip())
        cols = int(self.cols_edit.text().strip())
        self.field.generate_maze(rows, cols)
