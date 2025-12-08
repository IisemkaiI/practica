class StaticArray:

    def __init__(self, capacity: int):
        if capacity <= 0:
            raise ValueError("Capacity must be positive")
        self._capacity = capacity
        self._arr = [None] * capacity
        self._size = 0

    def is_full(self) -> bool:
        return self._size == self._capacity

    def is_empty(self) -> bool:
        return self._size == 0

    def __len__(self):
        return self._size

    def __str__(self):
        elements = self._arr[:self._size]
        return f"StaticArray({elements}, size={self._size}, capacity={self._capacity})"

    def pushBack(self, value) -> bool:
        """
        Добавляет элемент в конец массива.
        Трудоёмкость: O(1) — выполняется за постоянное время:
        одна запись + увеличение счётчика. Не зависит от размера.
        """
        if self.is_full():
            return False
        self._arr[self._size] = value
        self._size += 1
        return True

    def pushFront(self, value) -> bool:
        """
        Добавляет элемент в начало массива.
        Трудоёмкость: O(n) — требуется сдвинуть все n существующих элементов на 1 позицию вправо.
        В худшем случае (массив почти полный) — ~n операций копирования.
        """
        if self.is_full():
            return False
        for i in range(self._size - 1, -1, -1):
            self._arr[i + 1] = self._arr[i]
        self._arr[0] = value
        self._size += 1
        return True

    def insert(self, index: int, value) -> bool:
        """
        Вставляет элемент по указанному индексу.
        Трудоёмкость: O(n) — в худшем случае (вставка в начало) нужно сдвинуть все n элементов.
        В среднем — сдвиг (n - index) элементов → всё равно линейная зависимость от n.
        """
        if index < 0 or index > self._size:
            raise IndexError("Index out of bounds for insert")
        if self.is_full():
            return False

        for i in range(self._size - 1, index - 1, -1):
            self._arr[i + 1] = self._arr[i]
        self._arr[index] = value
        self._size += 1
        return True

    def remove(self, index: int):
        """
        Удаляет элемент по индексу и возвращает его.
        Трудоёмкость: O(n) — после удаления нужно сдвинуть все элементы справа от index на 1 влево.
        В худшем случае (удаление первого элемента) — сдвиг n-1 элементов.
        """
        if index < 0 or index >= self._size:
            raise IndexError("Index out of bounds for remove")

        removed_value = self._arr[index]

        for i in range(index, self._size - 1):
            self._arr[i] = self._arr[i + 1]

        self._arr[self._size - 1] = None
        self._size -= 1

        return removed_value

    def find(self, value) -> int:
        """
        Ищет первое вхождение значения и возвращает его индекс.
        Трудоёмкость: O(n) — линейный поиск: в худшем случае (элемента нет или он последний)
        просматриваем все n элементов.
        """
        for i in range(self._size):
            if self._arr[i] == value:
                return i
        return -1


if __name__ == "__main__":
    sa = StaticArray(5)

    print(" pushBack")
    sa.pushBack(10)
    sa.pushBack(20)
    sa.pushBack(30)
    print(sa)

    print("\n pushFront")
    sa.pushFront(5)
    print(sa)

    print("\n insert")
    sa.insert(2, 15)
    print(sa)

    print("\n find")
    print("Index of 15:", sa.find(15))
    print("Index of 99:", sa.find(99))

    print("\n remove")
    removed = sa.remove(0)  # удаляем первый (5)
    print(f"Removed: {removed}, array: {sa}")

    print("\n переполнение")
    print("PushBack 99:", sa.pushBack(99))
    print("PushBack 100:", sa.pushBack(100))