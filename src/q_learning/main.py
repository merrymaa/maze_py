# from ..core.maze import Maze
# from random import choice, random
# from src.q_learning.position import Position
# from .qtable import QTable
#
# ALPHA = 0.1 # коэффициент альфа - скорость обучения
# GAMMA = 0.9 # коэффициент гамма - коэффициент дисконтирования
# EPSILON = 0.9 # коэффициент случайности
#
# def get_limit_steps(height_maze: int, width_maze: int, k = 5) -> int:
#     """"
#     height_maze - высота лабиринта
#     width_maze - ширина лабиринта
#     k - коэффициент запаса
#     return -> лимит шагов на эпизод
#     """
#
#     long_path = height_maze * width_maze
#     return k * long_path
#
# def calculate_q(q_old, reward, max_q_new_pos) -> float:
#     q = q_old + ALPHA * (reward + GAMMA * max_q_new_pos - q_old)
#
#     return q
#
# def calculate_reward(new_pos: tuple, finish: tuple, maze: Maze, wall=False) -> int:
#     """"
#     удар о стену -10
#     за один шаг -1
#     достижение цели +100
#     """
#     if wall:
#         return -10
#     tmp_pos = Position(*new_pos)
#     # упирается в стену
#     if not tmp_pos.valid_position(maze):
#         return -10
#     if new_pos != finish:
#         return -1
#     else:
#         return 100
#
#
# h = 5
# w = 5
#
# maze_v = [
#     [0, 0, 1, 1, 1],
#     [1, 1, 0, 1, 1],
#     [0, 1, 0, 1, 1],
#     [1, 1, 0, 0, 1],
#     [1, 0, 0, 0, 1]
# ]
# maze_h = [
#     [1, 0, 0, 0, 0],
#     [0, 1, 1, 0, 0],
#     [0, 0, 0, 1, 0],
#     [0, 0, 1, 1, 0],
#     [1, 1, 1, 1, 1]
# ]
#
# my_maze = Maze(h, w)
# my_maze.wall_v = maze_v
# my_maze.wall_h = maze_h
# my_maze.draw_maze()
#
# start_point = Position(0, 0)
# dst_point = Position(h - 1, w - 1)
#
# current_pos = start_point
#
# limit_steps = get_limit_steps(my_maze.height, my_maze.width)
#
# q_table = QTable(h, w)
# for _ in range(5000):
#     EPSILON = EPSILON * 0.995
#     # EPSILON = max(0.01, EPSILON * 0.995)
#     current_pos = Position(start_point.y, start_point.x)
#     steps = 0
#     while current_pos.not_eq(dst_point):
#         random_num = random()
#         if random_num < EPSILON: # делаем случайный шаг
#             action = choice(("up", "down", "left", "right"))
#
#         else: # делаем шаг на основе q-таблицы
#             # делаем ход в направлении, где самое большое значение Q
#             current_cords = current_pos.get_cords() # текущие координаты
#             action = q_table.get_best_step(current_cords) # новый вектор направления, может уйти вне лабиринта
#
#         old_cords = current_pos.get_cords()
#         new_cords = current_pos.get_new_cords(action)
#
#         if current_pos.valid_step(action, my_maze): # проверка, можно ли сделать шаг
#             current_pos.make_step(action)
#             max_q_new_pos = q_table.get_max_q(new_cords)
#             reward = calculate_reward(current_pos.get_cords(), dst_point.get_cords(), my_maze, wall=False)
#             current_cords = current_pos.get_cords()  # текущие координаты
#
#         else: # выход за пределы лабиринта или нет прохода
#             # обновляю q-значение
#             reward = calculate_reward(old_cords, dst_point.get_cords(), my_maze, wall=True)
#             max_q_new_pos = 0
#             current_cords = old_cords
#
#         q_old = q_table.get_q(old_cords, action)
#         q_new = calculate_q(q_old, reward, max_q_new_pos)
#         q_table.set_q(old_cords, action, q_new)
#
#         steps += 1
#         if steps == limit_steps:
#             break
#         # один эпизод закончился
#
# q_table.print_all()


# print("\n" + "="*50)
# print("ОБУЧЕНИЕ ЗАВЕРШЕНО")
# print("="*50)
#
# result = [[0 for _ in range(w)] for _ in range(h)]
# print(*result, sep='\n')
# print()
#
# current_pos = Position(start_point.y, start_point.x)
# current_cords = current_pos.get_cords()
# step = 1 # текущие координаты
# while current_pos.not_eq(dst_point):
#     action = q_table.get_best_step(current_cords)
#     old_cords = current_pos.get_cords()
#     if current_pos.valid_step(action, my_maze):  # проверка, можно ли сделать шаг
#         current_pos.make_step(action)
#         current_cords = current_pos.get_cords()  # текущие координаты
#
#         result[current_cords[0]][current_cords[1]] = 1
#         # print(current_cords)
#     else:
#         current_cords = old_cords
#         # print("мимо")
#     step += 1
#     if step == 300:
#         break
#
# print(*result, sep='\n')

from .q_learning import QLearning
from ..core.maze import Maze

my_maze = Maze(6, 6)
my_maze.draw_maze()
learning = QLearning(my_maze)
learning.start_learning()
learning.q_table.print_all()
learning.show_decision(0,3)