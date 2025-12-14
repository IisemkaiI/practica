import time
import re
from typing import List, Tuple, Any



def good_hash(key: str, capacity: int) -> int:
    """Полиномиальный хэш"""
    p = 31
    h = 0
    for i, ch in enumerate(key):
        h = (h + ord(ch) * (p ** i)) % capacity
    return h

def bad_hash(key: str, capacity: int) -> int:
    """Плохая хэш-функция — всегда 0"""
    return 0



class FrequencyHashMap:
    def __init__(self, capacity: int = 16, hash_func=good_hash):
        self._capacity = capacity
        self._size = 0
        self._buckets: List[List[Tuple[str, int]]] = [[] for _ in range(self._capacity)]
        self._hash_func = hash_func  # теперь это функция, принимающая key и capacity

    def _find_in_bucket(self, bucket, key: str):
        for i, (k, _) in enumerate(bucket):
            if k == key:
                return i
        return None

    def put(self, key: str, value: int) -> None:
        index = self._hash_func(key, self._capacity)  # передаём capacity
        bucket = self._buckets[index]
        pos = self._find_in_bucket(bucket, key)
        if pos is not None:
            bucket[pos] = (key, value)
        else:
            bucket.append((key, value))
            self._size += 1

    def get(self, key: str) -> int:
        index = self._hash_func(key, self._capacity)
        bucket = self._buckets[index]
        pos = self._find_in_bucket(bucket, key)
        if pos is not None:
            return bucket[pos][1]
        return 0

    def increment(self, key: str) -> None:
        self.put(key, self.get(key) + 1)

    def items(self) -> List[Tuple[str, int]]:
        result = []
        for bucket in self._buckets:
            result.extend(bucket)
        return result



def preprocess_text(text: str) -> List[str]:
    text = text.lower()
    words = re.findall(r'[а-яёa-z]+', text)
    return words



def build_frequency_dict(words: List[str], use_bad_hash: bool = False) -> Tuple[FrequencyHashMap, float]:
    start = time.perf_counter()

    hash_func = bad_hash if use_bad_hash else good_hash
    freq_map = FrequencyHashMap(capacity=256, hash_func=hash_func)

    for word in words:
        freq_map.increment(word)

    duration = time.perf_counter() - start
    return freq_map, duration



def print_top_n(freq_map: FrequencyHashMap, n: int = 10):
    items = freq_map.items()
    items.sort(key=lambda x: x[1], reverse=True)
    print(f"\n Топ-{n} самых частых слов:")
    print("-" * 30)
    for i, (word, count) in enumerate(items[:n], 1):
        print(f"{i:2}. {word:<15} — {count} раз")



SAMPLE_TEXT = """
В некотором царстве, в некотором государстве жил-был царь. У царя был сын — Иван-царевич. 
Царь очень любил сына, и сын любил отца. Однажды царь заболел, и никто не мог его вылечить. 
Иван-царевич отправился за чудодейственным зельем. По дороге он встретил лису, волка и медведя. 
Лиса была хитрой, волк — сильным, медведь — добрым. Все они помогли Ивану-царевичу. 
Царь выздоровел, и все зажили счастливо.
"""

if __name__ == "__main__":
    words = preprocess_text(SAMPLE_TEXT)
    print(f" Обработано слов: {len(words)}")


    print("\n️  Используем хорошую хэш-функцию...")
    good_map, good_time = build_frequency_dict(words, use_bad_hash=False)


    print("️  Используем плохую хэш-функцию (все ключи в одну ячейку)...")
    bad_map, bad_time = build_frequency_dict(words, use_bad_hash=True)


    print_top_n(good_map, n=10)

    print("\n Сравнение времени построения:")
    print(f"  Хорошая хэш-функция: {good_time:.6f} сек")
    print(f"  Плохая хэш-функция:  {bad_time:.6f} сек")
    if good_time > 0:
        ratio = bad_time / good_time
        print(f"  Ускорение: в {ratio:.1f} раз быстрее с хорошей хэш-функцией!")


    good_top = set(word for word, _ in sorted(good_map.items(), key=lambda x: x[1], reverse=True)[:5])
    bad_top = set(word for word, _ in sorted(bad_map.items(), key=lambda x: x[1], reverse=True)[:5])
    print(f"\n Проверка: одинаковые ли топ-5? {' Да' if good_top == bad_top else ' Нет'}")