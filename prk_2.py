import time


class SimpleDynamicArray:
    """Упрощенная реализация динамического массива"""

    def __init__(self, capacity=1):
        self._capacity = max(1, capacity)
        self._size = 0
        self._array = [None] * self._capacity

    def append(self, element):
        if self._size == self._capacity:
            self._resize(2 * self._capacity)
        self._array[self._size] = element
        self._size += 1

    def _resize(self, new_capacity):
        new_array = [None] * new_capacity
        for i in range(self._size):
            new_array[i] = self._array[i]
        self._array = new_array
        self._capacity = new_capacity

    def __len__(self):
        return self._size

    def __getitem__(self, index):
        return self._array[index]

    def __str__(self):
        return str(self._array[:self._size])


if __name__ == "__main__":

    n = 100000

    start = time.time()
    static = [None] * n
    for i in range(n):
        static[i] = i
    print(f"Статический: {time.time() - start:.4f} сек")

    start = time.time()
    dynamic = SimpleDynamicArray()
    for i in range(n):
        dynamic.append(i)
    print(f"Динамический: {time.time() - start:.4f} сек")

    start = time.time()
    py_list = []
    for i in range(n):
        py_list.append(i)
    print(f"Python list: {time.time() - start:.4f} сек")