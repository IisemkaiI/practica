from typing import List


class MinHeap:
    def __init__(self):
        self.heap: List[int] = []

    def _parent(self, i): return (i - 1) // 2
    def _left(self, i):   return 2 * i + 1
    def _right(self, i):  return 2 * i + 2

    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def _is_heap(self) -> bool:
        for i in range(len(self.heap)):
            l, r = self._left(i), self._right(i)
            if l < len(self.heap) and self.heap[i] > self.heap[l]:
                return False
            if r < len(self.heap) and self.heap[i] > self.heap[r]:
                return False
        return True

    def push(self, val: int) -> None:
        self.heap.append(val)
        self._sift_up(len(self.heap) - 1)
        assert self._is_heap(), "Нарушено свойство кучи после push!"

    def _sift_up(self, i: int) -> None:
        while i > 0 and self.heap[self._parent(i)] > self.heap[i]:
            self._swap(i, self._parent(i))
            i = self._parent(i)

    def pop(self) -> int:
        if not self.heap:
            raise IndexError("pop from empty heap")
        if len(self.heap) == 1:
            return self.heap.pop()
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._sift_down(0)
        assert self._is_heap(), "Нарушено свойство кучи после pop!"
        return root

    def _sift_down(self, i: int) -> None:
        n = len(self.heap)
        while True:
            smallest = i
            l, r = self._left(i), self._right(i)
            if l < n and self.heap[l] < self.heap[smallest]:
                smallest = l
            if r < n and self.heap[r] < self.heap[smallest]:
                smallest = r
            if smallest == i:
                break
            self._swap(i, smallest)
            i = smallest

    def heapify(self, arr: List[int]) -> None:
        self.heap = arr[:]
        n = len(self.heap)
        for i in range(n // 2 - 1, -1, -1):
            self._sift_down(i)
        assert self._is_heap(), "Нарушено свойство кучи после heapify!"

    def peek(self) -> int:
        if not self.heap:
            raise IndexError("peek from empty heap")
        return self.heap[0]

    def size(self) -> int:
        return len(self.heap)

    def is_empty(self) -> bool:
        return len(self.heap) == 0

    def __str__(self):
        return f"MinHeap: {self.heap}"


if __name__ == "__main__":
    print("Тест: вставка")
    h = MinHeap()
    for x in [10, 5, 15, 3, 7, 12]:
        h.push(x)
        print(f"push({x}) → {h}")

    print(f"\nМинимум: {h.peek()}")
    print(f"pop() → {h.pop()}")
    print(f"pop() → {h.pop()}")
    print(f"Текущее состояние: {h}")

    print("\nТест: heapify из [3, 9, 2, 1, 4, 5]")
    h.heapify([3, 9, 2, 1, 4, 5])
    print(h)
    print(f"Минимум: {h.peek()}")

    print("\nИзвлекаем все элементы:")
    res = []
    while not h.is_empty():
        res.append(h.pop())
    print("Результат:", res)
    print("Отсортировано?", res == sorted(res))