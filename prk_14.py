from collections import deque
from typing import List

def count_islands_dfs(grid: List[List[int]]) -> int:
    if not grid or not grid[0]:
        return 0

    rows, cols = len(grid), len(grid[0])
    count = 0

    def dfs(r, c):
        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 0:
            return
        grid[r][c] = 0
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                dfs(r, c)
                count += 1
    return count


def count_islands_bfs(grid: List[List[int]]) -> int:
    if not grid or not grid[0]:
        return 0

    rows, cols = len(grid), len(grid[0])
    count = 0
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                count += 1
                queue = deque([(r, c)])
                grid[r][c] = 0
                while queue:
                    x, y = queue.popleft()
                    for dx, dy in directions:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 1:
                            grid[nx][ny] = 0
                            queue.append((nx, ny))
    return count


def print_grid(grid, title="Сетка"):
    print(f"\n{title}:")
    for row in grid:
        print(' '.join(str(x) for x in row))


if __name__ == "__main__":
    original = [
        [1, 1, 0, 0, 0],
        [1, 1, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 0, 1, 1]
    ]

    grid_dfs = [row[:] for row in original]  # копия
    print_grid(grid_dfs, "Исходная сетка")
    islands_dfs = count_islands_dfs(grid_dfs)
    print(f"\nКоличество островов (DFS): {islands_dfs}")

    grid_bfs = [row[:] for row in original]
    islands_bfs = count_islands_bfs(grid_bfs)
    print(f"Количество островов (BFS): {islands_bfs}")


    big = [
        [1, 1, 1],
        [1, 0, 1],
        [1, 1, 1]
    ]
    print_grid(big, "Кольцевой остров")
    print(f"Количество островов: {count_islands_bfs([row[:] for row in big])}")