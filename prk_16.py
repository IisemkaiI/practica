import heapq
from typing import Any, List, Tuple


class PriorityQueue:
    def __init__(self):
        self._heap: List[Tuple[int, int, Any]] = []
        self._counter = 0

    def push(self, value: Any, priority: int) -> None:
        heapq.heappush(self._heap, (priority, self._counter, value))
        self._counter += 1

    def pop(self) -> Any:
        if self.is_empty():
            raise IndexError("pop from empty priority queue")
        _, _, value = heapq.heappop(self._heap)
        return value

    def is_empty(self) -> bool:
        return len(self._heap) == 0

    def size(self) -> int:
        return len(self._heap)


class TaskScheduler:
    def __init__(self):
        self.pq = PriorityQueue()

    def add_task(self, task: str, priority: int) -> None:
        """Чем ниже приоритет → тем раньше выполнится (0 = highest)"""
        self.pq.push(task, priority)

    def next_task(self) -> str:
        return self.pq.pop()

    def run_all(self) -> List[str]:
        tasks = []
        while not self.pq.is_empty():
            tasks.append(self.next_task())
        return tasks


def k_smallest(arr: List[int], k: int) -> List[int]:
    """Возвращает k наименьших элементов в порядке возрастания"""
    if k <= 0:
        return []
    if k >= len(arr):
        return sorted(arr)
    heap = []
    for x in arr:
        if len(heap) < k:
            heapq.heappush(heap, -x)
        elif x < -heap[0]:
            heapq.heapreplace(heap, -x)
    return sorted(-x for x in heap)


if __name__ == "__main__":
    print("ест приоритетной очереди:")
    pq = PriorityQueue()
    pq.push("выпить кофе", 2)
    pq.push("срочно доделать отчёт", 0)
    pq.push("проверить почту", 1)
    pq.push("погулять", 3)

    print("Очередь задач (по приоритету):")
    while not pq.is_empty():
        print(f"  → {pq.pop()}")

    print("\nПланировщик задач:")
    scheduler = TaskScheduler()
    scheduler.add_task("Позвонить клиенту", 1)
    scheduler.add_task("Срочный багфикс", 0)
    scheduler.add_task("Собрание", 1)
    scheduler.add_task("Отдых", 5)
    print("Порядок выполнения:", scheduler.run_all())

    arr = [4, 1, 7, 3, 8, 2, 6, 5]
    k = 3
    print(f"\nМассив: {arr}")
    print(f"Топ-{k} самых маленьких: {k_smallest(arr, k)}")