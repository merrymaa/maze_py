from random import random, choice
from datetime import datetime
from pathlib import Path

CHANCE_SIDE = 0.5
CHANCE_FLOOR = 0.5


class Maze:
    def __init__(self, width, height):
        if width < 1 or height < 1:
            raise ValueError("Размеры лабиринта должныт быть больше 0")
        self.width = width
        self.height = height
        self.wall_v = [[1 for _ in range(width)] for _ in range(height)]
        self.wall_h = [[1 for _ in range(width)] for _ in range(height)]
        self.generate()

    @staticmethod
    def _merge_sets(row, target_id, new_id) -> None:
        for k in range(len(row)):
            if row[k] == target_id:
                row[k] = new_id

    def generate(self) -> None:
        """"Генерация идеального лабиринта по алгоритму Эллера"""
        counter = 1
        current_row = [0 for _ in range(self.width)]
        for i in range(self.width):
            if current_row[i] == 0:
                current_row[i] = counter
                counter += 1
        for i in range(self.height - 1):
            rooms = dict()
            for j in range(self.width - 1):
                if random() < CHANCE_SIDE:
                    if current_row[j] != current_row[j + 1]:  # проходы в бок
                        id_to_replace = current_row[j + 1]
                        new_id = current_row[j]
                        self._merge_sets(current_row, id_to_replace, new_id)
                        self.wall_v[i][j] = 0

            for indx, id in enumerate(current_row):
                if not id in rooms:
                    rooms[id] = [indx]
                else:
                    rooms[id].append(indx)

            for key, indices in rooms.items():
                opened_door = False
                for idx in indices:
                    if random() < CHANCE_FLOOR:
                        self.wall_h[i][idx] = 0
                        opened_door = True

                if not opened_door:
                    self.wall_h[i][choice(indices)] = 0

            next_row = [0 for _ in range(self.width)]

            for j in range(self.width):
                if self.wall_h[i][j] == 0:
                    next_row[j] = current_row[j]

            for j in range(self.width):
                if next_row[j] == 0:
                    next_row[j] = counter
                    counter += 1
            current_row = next_row

        for i in range(self.width - 1):  # соединение последней строки
            if current_row[i] != current_row[i + 1]:
                self.wall_v[self.height - 1][i] = 0

    def draw_maze(self) -> None:
        """"Отрисовка в консоле"""
        # for i in range(self.height):
        #     for j in range(self.width):
        #         if j == 0:
        #             print("|", end='')
        #         if self.wall_h[i][j] == 1:
        #             print('_', end='')
        #         if self.wall_h[i][j] == 0:
        #             print(" ", end='')
        #         if self.wall_v[i][j] == 1:
        #             print('|', end='')
        #         if self.wall_v[i][j] == 0:
        #             print(" ", end='')
        #     print()
        print("+" + "---+" * self.width)
        for i in range(self.height):
            row_str = "|"
            for j in range(self.width):
                row_str += "   "
                if j < self.width - 1:
                    row_str += "|" if self.wall_v[i][j] == 1 else " "
            print(row_str + "|")

            if i < self.height - 1:
                h_wall_str = "+"
                for j in range(self.width):
                    h_wall_str += "---" if self.wall_h[i][j] == 1 else "   "
                    h_wall_str += "+"
                print(h_wall_str)
        print("+" + "---+" * self.width)

    def record_file(self) -> None:
        data_dir = Path("data")
        data_dir.mkdir(exist_ok=True)

        time_now = str(datetime.now().strftime("%Y_%m_%d_%H_%M_%S"))

        file_path = data_dir / f"maze_{time_now}.txt"

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(f"{self.height} {self.width}\n")
            for i in range(self.height):
                for j in range(self.width):
                    print(self.wall_v[i][j], end=' ', file=f)
                print(file=f)

            f.write('\n')
            for i in range(self.height):
                for j in range(self.width):
                    print(self.wall_h[i][j], end=' ', file=f)
                print(file=f)
