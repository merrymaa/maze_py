from random import choice

class QValues:

    def __init__(self, up, down, left, right):
        self.up = up
        self.down = down
        self.left = left
        self.right = right

    def get_values(self):
        return self.up, self.down, self.left, self.right

    def get_max(self) -> float:
        """"Возвращает максимальное Q"""

        return max(self.up, self.down, self.left, self.right)

    def get_best_step(self) -> str:
        """"Возвращает направление с самым большим q-значением"""

        dirs = {"up": self.up, "down": self.down, "left": self.left, "right": self.right}
        max_val = max(dirs.values())
        best_dirs = [d for d, v in dirs.items() if v == max_val]

        return choice(best_dirs)

