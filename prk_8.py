from typing import Any, List, Optional, Tuple


class HashTable:
    def __init__(self, initial_capacity: int = 8):
        self._capacity = initial_capacity
        self._size = 0

        self._buckets: List[List[Tuple[str, Any]]] = [[] for _ in range(self._capacity)]

    def _hash(self, key: str) -> int:
        """
        Полиномиальный хэш: h = (s₀·p⁰ + s₁·p¹ + ... + sₙ₋₁·pⁿ⁻¹) mod m
        p = 31 (простое), m = capacity
        """
        p = 31
        m = self._capacity
        hash_val = 0
        for i, char in enumerate(key):
            hash_val = (hash_val + ord(char) * (p ** i)) % m
        return hash_val

    def _find_in_bucket(self, bucket: List[Tuple[str, Any]], key: str) -> Optional[int]:
        """Возвращает индекс пары с данным ключом, или None"""
        for i, (k, _) in enumerate(bucket):
            if k == key:
                return i
        return None


    def put(self, key: str, value: Any) -> None:

        if self._size >= self._capacity * 0.75:
            self._resize()

        index = self._hash(key)
        bucket = self._buckets[index]

        pos = self._find_in_bucket(bucket, key)
        if pos is not None:

            bucket[pos] = (key, value)
        else:

            bucket.append((key, value))
            self._size += 1

    def get(self, key: str) -> Any:
        index = self._hash(key)
        bucket = self._buckets[index]
        pos = self._find_in_bucket(bucket, key)
        if pos is not None:
            return bucket[pos][1]
        raise KeyError(f"Key '{key}' not found")

    def remove(self, key: str) -> None:
        index = self._hash(key)
        bucket = self._buckets[index]
        pos = self._find_in_bucket(bucket, key)
        if pos is not None:
            bucket.pop(pos)
            self._size -= 1
        else:
            raise KeyError(f"Key '{key}' not found")

    def _resize(self) -> None:
        old_buckets = self._buckets
        old_capacity = self._capacity

        self._capacity *= 2
        self._buckets = [[] for _ in range(self._capacity)]
        self._size = 0

        for bucket in old_buckets:
            for key, value in bucket:
                self.put(key, value)

    def visualize(self) -> None:
        print(f"\n Хэш-таблица (размер = {self._size}, ёмкость = {self._capacity})")
        print("=" * 60)
        for i, bucket in enumerate(self._buckets):
            if bucket:
                entries = ", ".join([f"'{k}': {v}" for k, v in bucket])
                print(f"[{i:2}] → {{ {entries} }}")
            else:
                print(f"[{i:2}] → ∅")
        print("=" * 60)

    def __len__(self):
        return self._size

    def __contains__(self, key: str):
        try:
            self.get(key)
            return True
        except KeyError:
            return False

if __name__ == "__main__":
    ht = HashTable(initial_capacity=4)

    print(" Вставляем пары...")
    data = [
        ("apple", 10),
        ("banana", 20),
        ("cherry", 30),
        ("date", 40),
        ("elderberry", 50),
        ("fig", 60),
        ("grape", 70),
    ]

    for key, value in data:
        ht.put(key, value)
        print(f"  Добавлено: {key} → {value}")

    ht.visualize()

    print(f"\n get('banana') = {ht.get('banana')}")
    print(f"   'fig' in table? { 'fig' in ht }")

    ht.put("apple", 100)
    print(f" apple обновлён: apple → {ht.get('apple')}")

    ht.remove("date")
    print(f"🗑 'date' удалён. Осталось элементов: {len(ht)}")

    ht.visualize()

    try:
        ht.remove("kiwi")
    except KeyError as e:
        print(f"\n⚠Ошибка: {e}")