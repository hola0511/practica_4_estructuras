from collections import deque


def calculate_path(grid, start, end1, end2, blocked_dirs):
    n = len(grid)
    visited = set()
    queue = deque([[start]])

    while queue:
        path = queue.popleft()
        x, y = path[-1]
        if (x, y) == end1 or (x, y) == end2:
            return path
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]:
            if (dx, dy) in blocked_dirs:
                continue
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] != "X" and (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append(path + [(nx, ny)])
    return None
