#Бинарная куча
import heapq

heap = []
heapq.heappush(heap, 5)
heapq.heappush(heap, 2)
heapq.heappush(heap, 8)
print(heapq.heappop(heap))


#Биномиальная куча
class BinomialHeap:
    def __init__(self):
        self.trees = []
        self.min_node = None
    
    def insert(self, value):
        pass
    
    def merge(self, other_heap):
        pass
    
    def extract_min(self):
        pass

#Куча фибоначчи
# Требуется установка: pip install fibheap
import fibheap

fh = fibheap.makefheap()
fibheap.fheappush(fh, 5)
fibheap.fheappush(fh, 2)
fibheap.fheappush(fh, 8)
min_val = fibheap.fheappop(fh)  # 2


#Хэш-таблицы
hash_table = {}
hash_table["key1"] = "value1"
hash_table["key2"] = "value2"

value = hash_table.get("key1")

if "key1" in hash_table:
    print("Key exists")

del hash_table["key1"]

from collections import defaultdict
dd = defaultdict(int)
dd["count"] += 1
