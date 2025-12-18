from collections import deque
from typing import List, Dict, Optional

class AdjacencyMatrixGraph:
    def __init__(self, n: int):
        self.n = n
        self.matrix = [[0] * n for _ in range(n)]

    def add_edge(self, u: int, v: int) -> None:
        self.matrix[u][v] = 1
        self.matrix[v][u] = 1

    def bfs(self, start: int) -> List[int]:
        visited = [False] * self.n
        queue = deque([start])
        visited[start] = True
        order = []

        while queue:
            u = queue.popleft()
            order.append(u)
            for v in range(self.n):
                if self.matrix[u][v] and not visited[v]:
                    visited[v] = True
                    queue.append(v)
        return order

    def dfs(self, start: int) -> List[int]:
        visited = [False] * self.n
        order = []

        def _dfs(u):
            visited[u] = True
            order.append(u)
            for v in range(self.n):
                if self.matrix[u][v] and not visited[v]:
                    _dfs(v)

        _dfs(start)
        return order

    def shortest_path(self, start: int, end: int) -> Optional[List[int]]:
        if start == end:
            return [start]
        visited = [False] * self.n
        prev = [-1] * self.n
        queue = deque([start])
        visited[start] = True

        while queue:
            u = queue.popleft()
            for v in range(self.n):
                if self.matrix[u][v] and not visited[v]:
                    visited[v] = True
                    prev[v] = u
                    if v == end:
                        path = []
                        cur = v
                        while cur != -1:
                            path.append(cur)
                            cur = prev[cur]
                        return path[::-1]
                    queue.append(v)
        return None


class AdjacencyListGraph:
    def __init__(self, n: int):
        self.n = n
        self.adj = [[] for _ in range(n)]

    def add_edge(self, u: int, v: int) -> None:
        self.adj[u].append(v)
        self.adj[v].append(u)

    def bfs(self, start: int) -> List[int]:
        visited = [False] * self.n
        queue = deque([start])
        visited[start] = True
        order = []

        while queue:
            u = queue.popleft()
            order.append(u)
            for v in self.adj[u]:
                if not visited[v]:
                    visited[v] = True
                    queue.append(v)
        return order

    def dfs(self, start: int) -> List[int]:
        visited = [False] * self.n
        stack = [start]
        order = []
        visited[start] = True

        while stack:
            u = stack.pop()
            order.append(u)
            for v in self.adj[u]:
                if not visited[v]:
                    visited[v] = True
                    stack.append(v)
        return order

    def shortest_path(self, start: int, end: int) -> Optional[List[int]]:
        if start == end:
            return [start]
        visited = [False] * self.n
        prev = [-1] * self.n
        queue = deque([start])
        visited[start] = True

        while queue:
            u = queue.popleft()
            for v in self.adj[u]:
                if not visited[v]:
                    visited[v] = True
                    prev[v] = u
                    if v == end:
                        path = []
                        cur = v
                        while cur != -1:
                            path.append(cur)
                            cur = prev[cur]
                        return path[::-1]
                    queue.append(v)
        return None


if __name__ == "__main__":

    print("Тест на графе из 4 узлов: 0-1-2 и 0-3-2")

    g_mat = AdjacencyMatrixGraph(4)
    g_mat.add_edge(0, 1)
    g_mat.add_edge(1, 2)
    g_mat.add_edge(0, 3)
    g_mat.add_edge(3, 2)

    print("\n[Матрица] BFS из 0:", g_mat.bfs(0))
    print("[Матрица] DFS из 0:", g_mat.dfs(0))
    print("[Матрица] Кратчайший путь 0→2:", g_mat.shortest_path(0, 2))

    g_list = AdjacencyListGraph(4)
    g_list.add_edge(0, 1)
    g_list.add_edge(1, 2)
    g_list.add_edge(0, 3)
    g_list.add_edge(3, 2)

    print("\n[Список] BFS из 0:", g_list.bfs(0))
    print("[Список] DFS из 0:", g_list.dfs(0))
    print("[Список] Кратчайший путь 0→2:", g_list.shortest_path(0, 2))

    print("\nМатрица смежности:")
    for row in g_mat.matrix:
        print(row)