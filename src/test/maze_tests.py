import pytest
from core.maze import Maze


def test_maze_initialization():
    """Тест 1: массивы создаются правильного размера"""
    maze = Maze(5, 7)
    assert maze.width == 5
    assert maze.height == 7
    assert len(maze.wall_v) == 7  # 7 строк
    assert len(maze.wall_v[0]) == 5  # 5 столбцов
    assert len(maze.wall_h) == 7
    assert len(maze.wall_h[0]) == 5


def test_invalid_dimensions():
    """Тест 2: на некорректные размеры"""
    with pytest.raises(ValueError):
        Maze(0, 5)
    with pytest.raises(ValueError):
        Maze(5, -1)
    with pytest.raises(ValueError):
        Maze(0, 0)


def test_boundary_walls():
    """Тест 3: правая и нижняя границы должны быть сплошными стенами """
    maze = Maze(10, 10)

    for r in range(maze.height):
        assert maze.wall_v[r][maze.width - 1] == 1, "Правая граница не закрыта!"

    for c in range(maze.width):
        assert maze.wall_h[maze.height - 1][c] == 1, "Нижняя граница не закрыта!"


def test_perfect_maze_connectivity():
    """Тест 4: на "идеальный" лабиринт"""

    maze = Maze(15, 15)
    visited = set()
    queue = [(0, 0)]
    visited.add((0, 0))

    while queue:
        r, c = queue.pop(0)

        if c < maze.width - 1 and maze.wall_v[r][c] == 0:
            if (r, c + 1) not in visited:
                visited.add((r, c + 1))
                queue.append((r, c + 1))

        if c > 0 and maze.wall_v[r][c - 1] == 0:
            if (r, c - 1) not in visited:
                visited.add((r, c - 1))
                queue.append((r, c - 1))

        if r < maze.height - 1 and maze.wall_h[r][c] == 0:
            if (r + 1, c) not in visited:
                visited.add((r + 1, c))
                queue.append((r + 1, c))

        if r > 0 and maze.wall_h[r - 1][c] == 0:
            if (r - 1, c) not in visited:
                visited.add((r - 1, c))
                queue.append((r - 1, c))

    total_cells = maze.width * maze.height
    assert len(
        visited) == total_cells, f"Лабиринт неидеален! Посещено {len(visited)} из {total_cells} клеток. Есть изолированные зоны."


@pytest.mark.parametrize("width,height", [
    (3, 3),
    (1, 10),
    (10, 1),
    (50, 50),
])
def test_maze_sizes_parametrized(width, height):
    maze = Maze(width, height)
    assert len(maze.wall_v) == height
    assert len(maze.wall_h[0]) == width
