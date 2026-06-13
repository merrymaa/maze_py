from random import random, choice

class Maze:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.wall_v = [[1 for _ in range(width)] for _ in range(height)]
        self.wall_h = [[1 for _ in range(width)] for _ in range(height)]
        self.generate_maze()

    @staticmethod
    def _merge_sets(row, target_id, new_id):
        for k in range(len(row)):
            if row[k] == target_id:
                row[k] = new_id

    def generate_maze(self):
        counter = 1
        current_row = [0 for _ in range(self.width)]

        for i in range(self.width):
            if current_row[i] == 0:
                current_row[i] = counter
                counter += 1
        for i in range(self.height - 1):
            rooms = dict()
            for j in range(self.width - 1):
                if current_row[j] != current_row[j + 1] and random() < 0.5:  # проходы в бок
                    id_to_replace = current_row[j + 1]
                    new_id = current_row[j]
                    self._merge_sets(current_row, id_to_replace, new_id)
                    self.wall_v[i][j] = 0
            for indx, id in enumerate(current_row):
                if not id in rooms:
                    rooms[id] = [indx]
                else:
                    rooms[id].append(indx)
            for key, value in rooms.items():  # проходы вниз
                ind = choice(value)
                self.wall_h[i][ind] = 0
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

    def draw_maze(self):
        for i in range(self.height):
            for j in range(self.width):
                if j == 0:
                    print("|", end='')
                if self.wall_h[i][j] == 1:
                    print('_', end='')
                if self.wall_h[i][j] == 0:
                    print(" ", end='')
                if self.wall_v[i][j] == 1:
                    print('|', end='')
                if self.wall_v[i][j] == 0:
                    print(" ", end='')
            print()


