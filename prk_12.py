class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
        self.word_count = 0


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
            node.word_count += 1
        node.is_end = True

    def delete(self, word: str) -> bool:
        def _delete(node: TrieNode, word: str, depth: int) -> bool:
            if depth == len(word):
                if not node.is_end:
                    return False
                node.is_end = False
                node.word_count -= 1
                return len(node.children) == 0
            ch = word[depth]
            if ch not in node.children:
                return False
            child = node.children[ch]
            should_delete_child = _delete(child, word, depth + 1)
            if should_delete_child:
                del node.children[ch]
            node.word_count -= 1
            return node.word_count == 0 and not node.is_end
        return _delete(self.root, word, 0)

    def count_words_with_prefix(self, prefix: str) -> int:
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return 0
            node = node.children[ch]
        return node.word_count

    def search(self, word: str) -> bool:
        node = self.root
        for ch in word:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return node.is_end


if __name__ == "__main__":
    trie = Trie()
    words = ["apple", "app", "application", "apply", "banana", "band"]

    print("Вставляем слова:", words)
    for w in words:
        trie.insert(w)

    print("\nПоиск слов целиком:")
    for w in ["app", "apple", "appl", "xyz"]:
        print(f"  '{w}': {'есть' if trie.search(w) else 'нет'}")

    print("\nКоличество слов по префиксу:")
    for p in ["a", "ap", "app", "appl", "b", "ba", "x"]:
        cnt = trie.count_words_with_prefix(p)
        print(f"  '{p}': {cnt} слов")

    print("\nУдаляем слово 'app'...")
    trie.delete("app")
    print(f"  'app' после удаления: {'есть' if trie.search('app') else 'нет'}")
    print(f"  'apple' всё ещё: {'есть' if trie.search('apple') else 'нет'}")
    print(f"  Количество слов с префиксом 'app': {trie.count_words_with_prefix('app')}")