class SimpleLinkedList:
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None

    def __init__(self):
        self.head = None

    def insert_front(self, data):
        new_node = self.Node(data)
        new_node.next = self.head
        self.head = new_node

    def append(self, data):
        new_node = self.Node(data)

        if not self.head:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def remove(self, data):
        if not self.head:
            return False

        if self.head.data == data:
            self.head = self.head.next
            return True

        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return True
            current = current.next

        return False

    def search(self, data):
        current = self.head
        index = 0

        while current:
            if current.data == data:
                return index
            current = current.next
            index += 1

        return -1

    def reverse(self):
        prev = None
        current = self.head

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        self.head = prev

    def __str__(self):
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        return " -> ".join(elements)


if __name__ == "__main__":
    lst = SimpleLinkedList()
    lst.append(1)
    lst.append(2)
    lst.append(3)
    lst.insert_front(0)
    print(f"Список: {lst}")
    print(f"Поиск 2: {lst.search(2)}")
    lst.reverse()
    print(f"После разворота: {lst}")