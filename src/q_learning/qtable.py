from .qvalues import QValues


class QTable:
    """"
    s - текущее состояние, картеж с координатами (y;x)
    a - действие, вверх, вниз, влево, вправо
    s_ - следующее состояние
    q_old - текущее q-значение
    R - награда
    """

    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.table = {}
        for i in range(height):
            for j in range(width):
                self.table[(i, j)] = QValues(0, 0, 0, 0)

    def set_q(self, state, action, q_value) -> None:
        """"
        Устанавливает q-value в таблицу
        """
        match action:
            case "right":  # вправо
                # print(f"set_q: action = {action}, q = {q_value}")
                self.table[state].right = q_value
            case "left":  # влево
                # print(f"set_q: action = {action}, q = {q_value}")
                self.table[state].left = q_value
            case "down":  # вниз
                # print(f"set_q: action = {action}, q = {q_value}")
                self.table[state].down = q_value
            case "up":  # вверх
                # print(f"set_q: action = {action}, q = {q_value}")
                self.table[state].up = q_value
            case _:
                # print(f"set_q: что-то не сработало")
                raise KeyError("вне лабиринта")

    def get_q(self, state: tuple, action: str) -> float:
        """"Возвращает Q-значение из конкретного состояния и согласно действию"""

        match action:
            case "right":  # вправо
                return self.table[state].right
            case "left":  # влево
                return self.table[state].left

            case "down":  # вниз
                return self.table[state].down
            case "up":  # вверх

                return self.table[state].up
            case _:
                raise KeyError("неизвестное действие")

    def get_max_q(self, state) -> float:
        """"
        Возвращает максимальное Q
        """
        return self.table[state].get_max()

    def get_best_step(self, state: tuple) -> str:
        """"
        Возвращает шаг (up, down, right, left)
        """

        action = self.table[state].get_best_step()

        return action

    def print_all(self, rows=2):
        for i in range(rows):
            for j in range(self.width):
                print(f"{(i,j)} {self.table[(i, j)].get_values()}")
