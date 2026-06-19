from PySide6.QtCore import QSize
from PySide6.QtGui import QColor, QPen
from PySide6.QtWidgets import QGraphicsView, QGraphicsScene, QMessageBox

from config import *
from core.maze import Maze


class FieldWidget(QGraphicsView):

    def __init__(self):
        super().__init__()

        self.scene = QGraphicsScene(self)
        self.setScene(self.scene)

        self.setFixedSize(QSize(SIZE_FIELD, SIZE_FIELD))

        self.maze_wide = 0
        self.maze_high = 0
        self.cell_wide = 0
        self.cell_high = 0
        self.data_right = []
        self.data_bottom = []

    def parse_file(self, file_path):
        self.data_right.clear()
        self.data_bottom.clear()
        self.maze_wide = 0
        self.maze_high = 0

        with (open(file_path, encoding='utf-8') as file):
            first_line = file.readline()
            if not first_line:
                QMessageBox.warning(self, "Ошибка", "Пустой файл")
                return

            self.maze_high, self.maze_wide = map(int, first_line.split())

            if (self.maze_wide > MAX_SIZE_MAZE
                    or self.maze_high > MAX_SIZE_MAZE or self.maze_wide <= 0
                    or self.maze_high <= 0):
                QMessageBox.warning(self, "Ошибка",
                                    "Некорректный размер лабиринта")
                return
            else:

                lines = file.readlines()
                for line in lines[:self.maze_high]:
                    self.data_right.append(line.replace(' ', '').strip())

                for line in lines[self.maze_high + 1:]:
                    self.data_bottom.append(line.replace(' ', '').strip())

    def draw_maze(self):
        if not self.maze_high or not self.maze_wide:
            return

        self.scene.clear()

        self.cell_high = (SIZE_FIELD - 2 * WIDE_WALL) / self.maze_high
        self.cell_wide = (SIZE_FIELD - 2 * WIDE_WALL) / self.maze_wide

        pen = QPen(QColor("#2c3e50"))
        pen.setWidth(WIDE_WALL)

        full_high = self.maze_high * self.cell_high
        full_wide = self.maze_wide * self.cell_wide

        self.scene.addLine(0, 0, full_high, 0, pen)
        self.scene.addLine(0, 0, 0, full_wide, pen)
        self.scene.addLine(full_high, 0, full_high, full_wide, pen)
        self.scene.addLine(0, full_wide, full_high, full_wide, pen)

        for row in range(self.maze_high):
            for col in range(self.maze_wide):
                if self.data_right[row][col] == '1':
                    x = (col + 1) * self.cell_wide
                    y1 = row * self.cell_high
                    y2 = (row + 1) * self.cell_high
                    self.scene.addLine(x, y1, x, y2, pen)

                if self.data_bottom[row][col] == '1':
                    y = (row + 1) * self.cell_high
                    x1 = col * self.cell_wide
                    x2 = (col + 1) * self.cell_wide
                    self.scene.addLine(x1, y, x2, y, pen)

    def generate_maze(self, height, width):
        """"Генерация, отрисовка и сохранение лабюиринта в файл"""
        new_maze = Maze(height, width)
        self.maze_high = height
        self.maze_wide = width

        new_maze.record_file()
        # new_maze.draw_maze()
        self.data_right = []
        for row in new_maze.wall_v:
            s = ''.join(str(cell) for cell in row)
            if len(s) < width:
                s += '0' * (width - len(s))
            self.data_right.append(s)

        self.data_bottom = []
        for row in new_maze.wall_h:
            s = ''.join(str(cell) for cell in row)
            if len(s) < width:
                s += '0' * (width - len(s))
            self.data_bottom.append(s)

        self.draw_maze()
