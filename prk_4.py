class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __len__(self):
        return self.length

    def __iter__(self):
        current = self.head
        while current:
            yield current.data
            current = current.next

    def __repr__(self):
        items = []
        current = self.head
        while current:
            items.append(str(current.data))
            current = current.next
        return " <-> ".join(items) if items else "Empty"

    def append(self, data):
        node = Node(data)
        if not self.head:
            self.head = self.tail = node
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
        self.length += 1
        return node

    def insert_front(self, data):
        node = Node(data)
        if not self.head:
            self.head = self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
        self.length += 1
        return node

    def insert_after(self, node, data):
        if not node: return

        new_node = Node(data)
        new_node.prev = node
        new_node.next = node.next

        if node.next:
            node.next.prev = new_node
        node.next = new_node

        if node == self.tail:
            self.tail = new_node

        self.length += 1
        return new_node

    def remove_node(self, node):
        if not node: return

        if node.prev:
            node.prev.next = node.next
        else:
            self.head = node.next

        if node.next:
            node.next.prev = node.prev
        else:
            self.tail = node.prev

        node.next = node.prev = None
        self.length -= 1
        return node.data

    def find(self, data):
        current = self.head
        while current:
            if current.data == data:
                return current
            current = current.next
        return None

    def remove(self, data):
        node = self.find(data)
        return self.remove_node(node) if node else None

    class Iterator:
        def __init__(self, start, reverse=False):
            self.current = start
            self.reverse = reverse

        def __iter__(self):
            return self

        def __next__(self):
            if not self.current:
                raise StopIteration
            data = self.current.data
            self.current = self.current.prev if self.reverse else self.current.next
            return data

    def reverse_iter(self):
        return self.Iterator(self.tail, reverse=True)

def test():
    print("Тест двусвязного списка")
    print("=" * 40)

    dll = DoublyLinkedList()

    dll.append(10)
    dll.append(20)
    dll.append(30)
    print(f"1. После append: {dll}")

    dll.insert_front(5)
    print(f"2. После insert_front: {dll}")

    node20 = dll.find(20)
    if node20:
        dll.insert_after(node20, 25)
        print(f"3. После insert_after(20, 25): {dll}")

    if node20:
        dll.remove_node(node20)
        print(f"4. После remove_node(20): {dll}")

    print(f"5. Прямой обход: {list(dll)}")
    print(f"6. Обратный обход: {list(dll.reverse_iter())}")

    print(f"Длина: {len(dll)}")
    print(f"Head: {dll.head.data if dll.head else 'None'}")
    print(f"Tail: {dll.tail.data if dll.tail else 'None'}")


def compare():
    import time
    dll = DoublyLinkedList()

    start = time.time()
    nodes = []
    for i in range(10000):
        nodes.append(dll.append(i))
    print(f"Вставка 10000 элементов: {time.time() - start:.4f} сек")

    import random
    start = time.time()
    for _ in range(1000):
        node = random.choice(nodes)
        dll.insert_after(node, "new")
    print(f"1000 вставок после случайных узлов: {time.time() - start:.4f} сек")

    start = time.time()
    for _ in range(1000):
        if nodes:
            node = random.choice(nodes)
            dll.remove_node(node)
            nodes.remove(node)
    print(f"1000 удалений случайных узлов: {time.time() - start:.4f} сек")


if __name__ == "__main__":
    test()
    print("\n" + "=" * 40)
    print("Сравнение производительности:")
    compare()