class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, node, key):
        if not node:
            return Node(key)
        if key < node.key:
            node.left = self._insert(node.left, key)
        elif key > node.key:
            node.right = self._insert(node.right, key)
        return node  # дубликаты не вставляем

    def search(self, key):
        return self._search(self.root, key) is not None

    def _search(self, node, key):
        if not node or node.key == key:
            return node
        if key < node.key:
            return self._search(node.left, key)
        return self._search(node.right, key)

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):
        if not node:
            return node
        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            # Нашли узел → удаляем
            if not node.left:
                return node.right
            if not node.right:
                return node.left
            # Два ребёнка → заменяем на min из правого поддерева
            min_node = self._min_node(node.right)
            node.key = min_node.key
            node.right = self._delete(node.right, min_node.key)
        return node

    def _min_node(self, node):
        while node.left:
            node = node.left
        return node

    def in_order(self):
        return self._in_order(self.root)

    def pre_order(self):
        return self._pre_order(self.root)

    def post_order(self):
        return self._post_order(self.root)

    def _in_order(self, node):
        return self._in_order(node.left) + [node.key] + self._in_order(node.right) if node else []

    def _pre_order(self, node):
        return [node.key] + self._pre_order(node.left) + self._pre_order(node.right) if node else []

    def _post_order(self, node):
        return self._post_order(node.left) + self._post_order(node.right) + [node.key] if node else []

    def is_balanced(self):
        return self._height(self.root) != -1

    def _height(self, node):
        if not node:
            return 0
        left_h = self._height(node.left)
        if left_h == -1:
            return -1
        right_h = self._height(node.right)
        if right_h == -1 or abs(left_h - right_h) > 1:
            return -1
        return max(left_h, right_h) + 1


if __name__ == "__main__":
    bst = BST()
    values = [50, 30, 70, 20, 40, 60, 80, 10]
    for v in values:
        bst.insert(v)

    print("Дерево построено из:", values)
    print("Поиск 40:", bst.search(40))
    print("Поиск 99:", bst.search(99))

    print("\nОбходы:")
    print("In-order:   ", bst.in_order())    # отсортировано!
    print("Pre-order:  ", bst.pre_order())
    print("Post-order: ", bst.post_order())

    print("\nУдаляем 30...")
    bst.delete(30)
    print("In-order после удаления:", bst.in_order())

    print("\nСбалансировано?", bst.is_balanced())  # True (высота ≤ 1 на всех узлах)

    unbalanced = BST()
    for v in [1, 2, 3, 4, 5]:
        unbalanced.insert(v)
    print("Цепочка 1→2→3→4→5 сбалансирована?", unbalanced.is_balanced())  # False