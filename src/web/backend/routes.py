from fastapi import APIRouter, Query
from fastapi.responses import HTMLResponse, Response

from core.maze import Maze

router = APIRouter()

MIN_MAZE_SIZE = 2
MAX_MAZE_SIZE = 51

@router.get("/", status_code=200)
def start_page():
    html_content = f"<h2> Hello friend </h2>"
    return HTMLResponse(content=html_content)


@router.get("/generate", status_code=200)
def generate_maze(
        width: int = Query(ge=MIN_MAZE_SIZE, lt=MAX_MAZE_SIZE),
        height: int = Query(ge=MIN_MAZE_SIZE, lt=MAX_MAZE_SIZE)):
    new_maze = Maze(width, height)

    return {
        "width": new_maze.width,
        "height": new_maze.height,
        "wall_v": new_maze.wall_v,
        "wall_h": new_maze.wall_h
    }

@router.post("/export", status_code=200)
def export(data: dict):
    width = data.get("width")
    height = data.get("height")
    wall_v = data.get("wall_v")
    wall_h = data.get("wall_h")

    # Валидация
    if not all([width, height, wall_v, wall_h]):
        return Response(
            content="Неполные данные лабиринта",
            status_code=400,
            media_type="text/plain"
        )

    # Формируем содержимое файла (та же логика, что в Python record_file)
    lines = []
    lines.append(f"{height} {width}")  # Формат Школы 21: height width

    # Блок wall_v
    for row in wall_v:
        lines.append(' '.join(map(str, row)))

    # Пустая строка
    lines.append('')

    # Блок wall_h
    for row in wall_h:
        lines.append(' '.join(map(str, row)))

    content = '\n'.join(lines)

    # Возвращаем как текстовый файл для скачивания
    return Response(
        content=content,
        media_type="text/plain",
        headers={
            "Content-Disposition": "attachment; filename=maze_export.txt"
        }
    )


