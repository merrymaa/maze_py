from ..core.maze import Maze


class Position:

    def __init__(self, y=None, x=None):
        if isinstance(x, type(self)):
            # "конструктор копирования"
            self.x = x.x
            self.y = x.y
        else:
            # Обычный конструктор
            self.x = x if x is not None else 0
            self.y = y if y is not None else 0

    def get_cords(self) -> tuple:
        return self.y, self.x

    def eq(self, other) -> bool:
        return self.x == other.x and self.y == other.y

    def not_eq(self, other) -> bool:
        return self.x != other.x or self.y != other.y

    def make_step(self, action: str) -> None:
        """"
        step[0] - направление по Y
        step[1] - направление по X
        """
        match action:
            case "right":  # вправо
                step = (0, 1)
            case "left":  # влево
                step = (0, -1)
            case "down":  # вниз
                step = (1, 0)
            case "up":  # вверх
                step = (-1, 0)

        self.y += step[0]
        self.x += step[1]

    def print_pos(self):
        print(f"y = {self.y} \nx = {self.x}\n")

    def valid_position(self, maze: Maze) -> bool:
        """"Проверка текущей позиции на валидность"""
        return (self.x < maze.get_width() and self.y
                < maze.get_height()) and (self.y >= 0 and self.x >= 0)

    def copy(self, other):
        self.y = other.y
        self.x = other.x

    def valid_step(self, action: str, maze: Maze) -> bool:
        """"
        Проверка можно ли переместиться на следующую позицию внутри лабиринта
        action - направление движения, строка
        maze - лабиринт
        """

        dirs = {
        "up": (-1, 0),
        "down": (1, 0),
        "left": (0, -1),
        "right": (0, 1)
        }

        new_y = self.y + dirs[action][0]
        new_x = self.x + dirs[action][1]

        # проверка на выход за границы лабиринта
        if (new_x < 0 or new_y < 0) or (new_x >= maze.width or new_y >= maze.height):
            return False
        # проверка на наличие прохода
        match action:
            case "right":  # вправо
                if maze.wall_v[self.y][self.x] != 0:
                    return False
            case "left":  # влево
                if maze.wall_v[self.y][self.x - 1] != 0:
                    return False
            case "down":  # вниз
                if maze.wall_h[self.y][self.x] != 0:
                    return False
            case "up":  # вверх
                if maze.wall_h[self.y - 1][self.x] != 0:
                    return False
        return True


    def get_new_cords(self, action: str) -> tuple:
        """"
        vector[0] - y
        vector[1] - x
        Возвращает координаты (y,x)
        """
        vector = (0,0)
        match action:
            case "right":  # вправо
                vector = (0, 1)
            case "left":  # влево
                vector = (0, -1)
            case "down":  # вниз
                vector = (1, 0)
            case "up":  # вверх
                vector = (-1, 0)

        return self.y + vector[0], self.x + vector[1]
