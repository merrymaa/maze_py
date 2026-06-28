from ..core.maze import Maze
from random import choice, random
from src.q_learning.position import Position
from .qtable import QTable


class QLearning:



    def __init__(self, maze: Maze, alpha=0.1, gamma=0.9, epsilon=0.9, episodes=5000):
        self.maze = maze
        self.start_point = Position(0, 0)
        self.dst_point = Position(self.maze.height - 1, self.maze.width - 1)
        self.limit_steps = self.get_limit_steps(self.maze.height, self.maze.width)
        self.q_table = QTable(self.maze.height, self.maze.width)
        self.alpha = alpha  # коэффициент альфа - скорость обучения
        self.gamma = gamma  # коэффициент гамма - коэффициент дисконтирования
        self.epsilon = epsilon  # коэффициент случайности
        self.episodes = episodes

    @staticmethod
    def get_limit_steps(height_maze: int, width_maze: int, k=5) -> int:
        """"
        height_maze - высота лабиринта
        width_maze - ширина лабиринта
        k - коэффициент запаса
        return -> лимит шагов на эпизод
        """

        long_path = height_maze * width_maze

        return k * long_path


    def calculate_q(self, q_old, reward, max_q_new_pos) -> float:
        q = q_old + self.alpha * (reward + self.gamma * max_q_new_pos - q_old)

        return q

    @staticmethod
    def calculate_reward(new_pos: tuple, finish: tuple, maze: Maze, wall=False) -> int:
        """"
        удар о стену -10
        за один шаг -1
        достижение цели +100
        """
        if wall:
            return -10
        tmp_pos = Position(*new_pos)
        # упирается в стену
        if not tmp_pos.valid_position(maze):
            return -10
        if new_pos != finish:
            return -1
        else:
            return 100

    def start_learning(self):
        for _ in range(self.episodes):
            # self.EPSILON = self.EPSILON * 0.995
            self.epsilon = max(0.01, self.epsilon * 0.995)
            current_pos = Position(self.start_point.y, self.start_point.x)
            steps = 0
            while current_pos.not_eq(self.dst_point):
                random_num = random()
                if random_num < self.epsilon:  # делаем случайный шаг
                    action = choice(("up", "down", "left", "right"))

                else:  # делаем шаг на основе q-таблицы
                    # делаем ход в направлении, где самое большое значение Q
                    current_coords = current_pos.get_cords()  # текущие координаты
                    action = self.q_table.get_best_step(current_coords)  # новый вектор направления, может уйти вне лабиринта

                old_cords = current_pos.get_cords()
                new_cords = current_pos.get_new_cords(action)

                if current_pos.valid_step(action, self.maze):  # проверка, можно ли сделать шаг
                    current_pos.make_step(action)
                    max_q_new_pos = self.q_table.get_max_q(new_cords)
                    reward = self.calculate_reward(current_pos.get_cords(), self.dst_point.get_cords(), self.maze, wall=False)
                    current_coords = current_pos.get_cords()  # текущие координаты

                else:  # выход за пределы лабиринта или нет прохода
                    # обновляю q-значение
                    reward = self.calculate_reward(old_cords, self.dst_point.get_cords(), self.maze, wall=True)
                    # max_q_new_pos = 0
                    max_q_new_pos = self.q_table.get_max_q(old_cords)
                    current_coords = old_cords

                q_old = self.q_table.get_q(old_cords, action)
                q_new = self.calculate_q(q_old, reward, max_q_new_pos)
                self.q_table.set_q(old_cords, action, q_new)

                steps += 1
                if steps == self.limit_steps:
                    break
                # один эпизод закончился

    def show_decision(self, start_point_y: int, start_point_x: int) -> list[list]:
        result = [[0 for _ in range(self.maze.width)] for _ in range(self.maze.height)]
        print(*result, sep='\n')
        print()

        current_pos = Position(start_point_y, start_point_x)
        current_cords =current_pos.get_cords()
        step = 1 # текущие координаты
        while current_pos.not_eq(self.dst_point):
            action = self.q_table.get_best_step(current_cords)
            old_cords = current_pos.get_cords()
            if current_pos.valid_step(action, self.maze):  # проверка, можно ли сделать шаг
                current_pos.make_step(action)
                current_cords = current_pos.get_cords()  # текущие координаты

                result[current_cords[0]][current_cords[1]] = 1
                # print(current_cords)
            else:
                current_cords = old_cords
                # print("мимо")
            step += 1
            if step == 300:
                break

        print(*result, sep='\n')
        return result