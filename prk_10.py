from collections import defaultdict
from typing import List, Dict, Tuple



class TrieNode:
    def __init__(self):
        self.children: Dict[str, 'TrieNode'] = {}
        self.is_end_of_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_end_of_word = True

    def _dfs_collect(self, node: TrieNode, prefix: str, results: List[str]) -> None:
        if node.is_end_of_word:
            results.append(prefix)
        for ch, child in node.children.items():
            self._dfs_collect(child, prefix + ch, results)

    def autocomplete(self, prefix: str) -> List[str]:
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return []
            node = node.children[ch]
        results = []
        self._dfs_collect(node, prefix, results)
        return results



class TrieWithFrequency:
    def __init__(self):
        self.trie = Trie()
        self.freq_map: Dict[str, int] = {}  # слово → частота

    def insert(self, word: str) -> None:
        word = word.lower()
        self.freq_map[word] = self.freq_map.get(word, 0) + 1
        self.trie.insert(word)

    def remove(self, word: str) -> bool:
        word = word.lower()
        if word in self.freq_map:
            del self.freq_map[word]
            return True
        return False

    def autocomplete(self, prefix: str, top_n: int = 10) -> List[Tuple[str, int]]:
        """
        Возвращает список (слово, частота), отсортированный:
        - по убыванию частоты,
        -- при равных — по возрастанию слова (лексикографически).
        """
        candidates = self.trie.autocomplete(prefix.lower())
        filtered = [(w, self.freq_map[w]) for w in candidates if w in self.freq_map]

        filtered.sort(key=lambda x: (-x[1], x[0]))
        return filtered[:top_n]



if __name__ == "__main__":

    print("🔍 Часть 1: Базовый Trie")
    trie = Trie()
    words = ["apple", "app", "application", "banana", "band", "bandana"]
    for w in words:
        trie.insert(w)

    print("autocomplete('app') →", trie.autocomplete("app"))
    print("autocomplete('ban') →", trie.autocomplete("ban"))
    print("autocomplete('xyz') →", trie.autocomplete("xyz"))


    print("\n Часть 2: Trie + HashMap (частоты)")
    tf = TrieWithFrequency()


    corpus = [
        "apple", "banana", "apple", "application", "banana",
        "app", "banana", "band", "apple", "bandana"
    ]
    for w in corpus:
        tf.insert(w)

    print("\n Частотный словарь:")
    for word, freq in sorted(tf.freq_map.items()):
        print(f"  '{word}': {freq}")

    # Автодополнение с сортировкой по частоте
    print("\n autocomplete('app', top_n=5):")
    suggestions = tf.autocomplete("app", top_n=5)
    for i, (word, freq) in enumerate(suggestions, 1):
        print(f"{i}. {word:<12} — частота: {freq}")

    print("\n autocomplete('ban', top_n=5):")
    suggestions = tf.autocomplete("ban", top_n=5)
    for i, (word, freq) in enumerate(suggestions, 1):
        print(f"{i}. {word:<12} — частота: {freq}")

    # Удаление слова
    print(f"\n🗑 Удаляем слово 'app'...")
    tf.remove("app")
    print("autocomplete('app') после удаления:")
    for word, freq in tf.autocomplete("app"):
        print(f"  {word} — {freq}")

    print("\n🇷🇺 Поддержка русского:")
    russian_words = ["мама", "мыла", "раму", "мамонт", "мышка"]
    for w in russian_words:
        tf.insert(w)
    print("autocomplete('ма') →", [w for w, _ in tf.autocomplete("ма")])
    print("autocomplete('мы') →", [w for w, _ in tf.autocomplete("мы")])