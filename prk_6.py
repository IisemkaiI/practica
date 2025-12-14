class CircularQueue:
    def __init__(self, capacity=10):
        self._capacity = capacity
        self._data = [None] * capacity
        self._front = 0
        self._rear = -1
        self._size = 0

    def enqueue(self, value):
        if self._size == self._capacity:
            raise OverflowError("Queue is full")
        self._rear = (self._rear + 1) % self._capacity
        self._data[self._rear] = value
        self._size += 1
        # Трудоёмкость: O(1)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        value = self._data[self._front]
        self._front = (self._front + 1) % self._capacity
        self._size -= 1
        return value
        # Трудоёмкость: O(1)

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty queue")
        return self._data[self._front]
        # Трудоёмкость: O(1)

    def is_empty(self):
        return self._size == 0
        # Трудоёмкость: O(1)

    def size(self):
        return self._size

    def __str__(self):
        if self.is_empty():
            return "CircularQueue: []"
        items = []
        i = self._front
        for _ in range(self._size):
            items.append(self._data[i])
            i = (i + 1) % self._capacity
        return f"CircularQueue: {items}"



class Stack:
    """Вспомогательный стек (на обычном списке — O(1) амортизированно)"""
    def __init__(self):
        self._items = []

    def push(self, item):
        self._items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self._items.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self._items[-1]

    def is_empty(self):
        return len(self._items) == 0


class QueueTwoStacks:
    """
    Очередь на двух стеках: 
    - in_stack — для enqueue
    - out_stack — для dequeue
    """
    def __init__(self):
        self.in_stack = Stack()
        self.out_stack = Stack()

    def _transfer(self):
        """Переносим элементы из in_stack в out_stack (если out_stack пуст)"""
        if self.out_stack.is_empty():
            while not self.in_stack.is_empty():
                self.out_stack.push(self.in_stack.pop())

    def enqueue(self, value):
        self.in_stack.push(value)
        # Трудоёмкость: O(1) всегда

    def dequeue(self):
        self._transfer()
        if self.out_stack.is_empty():
            raise IndexError("dequeue from empty queue")
        return self.out_stack.pop()
        # Амортизированная трудоёмкость: O(1)

    def peek(self):
        self._transfer()
        if self.out_stack.is_empty():
            raise IndexError("peek from empty queue")
        return self.out_stack.peek()
        # Амортизированная трудоёмкость: O(1)

    def is_empty(self):
        return self.in_stack.is_empty() and self.out_stack.is_empty()

    def size(self):
        return len(self.in_stack._items) + len(self.out_stack._items)

def test_queue(QueueClass, *args, **kwargs):
    q = QueueClass(*args, **kwargs)
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    assert q.peek() == 1, "peek() должен возвращать первый элемент"
    assert q.dequeue() == 1, "dequeue() должен удалять первый элемент"
    assert q.dequeue() == 2
    q.enqueue(4)
    assert q.dequeue() == 3
    assert q.dequeue() == 4
    assert q.is_empty(), "Очередь должна быть пуста"
    print(f"{QueueClass.__name__} — прошёл все тесты")


if __name__ == "__main__":
    print("  Тестирование очередей:\n")

    test_queue(CircularQueue, capacity=5)

    test_queue(QueueTwoStacks)

    print("\n Пример работы CircularQueue:")
    cq = CircularQueue(capacity=4)
    for x in [10, 20, 30]:
        cq.enqueue(x)
        print(f"Добавили {x} → {cq}")
    print("Извлекаем:", cq.dequeue())
    cq.enqueue(40)
    print("После добавления 40:", cq)

    print("\n  Пример работы QueueTwoStacks:")
    qs = QueueTwoStacks()
    for x in ['A', 'B', 'C']:
        qs.enqueue(x)
        print(f"Добавили {x}")
    print("Вершина:", qs.peek())
    print("Извлекаем:", qs.dequeue(), qs.dequeue(), qs.dequeue())