class StackArray:
    def __init__(self):
        self._data = []

    def push(self, item):
        self._data.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self._data.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self._data[-1]

    def is_empty(self):
        return len(self._data) == 0

    def size(self):
        return len(self._data)

    def __str__(self):
        return f"StackArray: {self._data}"


class ListNode:
    def __init__(self, val, next_node=None):
        self.val = val
        self.next = next_node


class StackLinkedList:
    def __init__(self):
        self.head = None
        self._size = 0

    def push(self, item):
        new_node = ListNode(item, self.head)
        self.head = new_node
        self._size += 1  # O(1)

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        val = self.head.val
        self.head = self.head.next
        self._size -= 1
        return val  # O(1)

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self.head.val  # O(1)

    def is_empty(self):
        return self.head is None

    def size(self):
        return self._size

    def __str__(self):
        vals = []
        cur = self.head
        while cur:
            vals.append(cur.val)
            cur = cur.next
        return f"StackLinkedList: {vals[::-1]}"


def is_balanced_brackets(s: str) -> bool:
    stack = StackArray()
    pairs = {')': '(', ']': '[', '}': '{'}

    for ch in s:
        if ch in '([{':
            stack.push(ch)
        elif ch in ')]}':
            if stack.is_empty():
                return False
            if stack.pop() != pairs[ch]:
                return False

    return stack.is_empty()


if __name__ == "__main__":
    print("=" * 40)
    print("Тестирование Стека на массиве")
    print("=" * 40)

    stack_arr = StackArray()
    stack_arr.push(1)
    stack_arr.push(2)
    stack_arr.push(3)
    print(stack_arr)
    print(f"Верхний элемент: {stack_arr.peek()}")
    print(f"Извлечено: {stack_arr.pop()}")
    print(f"Размер: {stack_arr.size()}")
    print(stack_arr)

    print("\n" + "=" * 40)
    print("Тестирование Стека на связном списке")
    print("=" * 40)

    stack_ll = StackLinkedList()
    stack_ll.push('A')
    stack_ll.push('B')
    stack_ll.push('C')
    print(stack_ll)
    print(f"Верхний элемент: {stack_ll.peek()}")
    print(f"Извлечено: {stack_ll.pop()}")
    print(f"Размер: {stack_ll.size()}")
    print(stack_ll)

    print("\n" + "=" * 40)
    print("Тестирование проверки скобок")
    print("=" * 40)

    test_cases = [
        ("", True),
        ("()", True),
        ("[({})]", True),
        ("([)]", False),
        ("{[()]}", True),
        ("(((", False),
        (")))", False),
        ("()[]{}", True),
        ("{[(])}", False),
        ("{[()]}[{}]", True),
    ]

    for expr, expected in test_cases:
        result = is_balanced_brackets(expr)
        status = "робит" if result == expected else "не робит"
        print(f"'{expr}' → {result} (ожидалось {expected}) {status}")

