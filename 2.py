#Бинарная куча
import heapq

heap = []
heapq.heappush(heap, 5)
heapq.heappush(heap, 2)
heapq.heappush(heap, 8)
print(heapq.heappop(heap))


#Биномиальная куча
class BinomialNode:
    def __init__(self, key):
        self.key = key
        self.degree = 0
        self.parent = None
        self.child = None
        self.sibling = None

class BinomialHeap:
    def __init__(self):
        self.head = None
    
    def merge(self, h2):
        # Объединение двух куч
        pass
    
    def insert(self, key):
        new_heap = BinomialHeap()
        new_heap.head = BinomialNode(key)
        self.merge(new_heap)
    
    def extract_min(self):
        # Извлечение минимального элемента
        pass


#
