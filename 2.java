//Бинарная куча
import java.util.PriorityQueue;
PriorityQueue<Integer> heap = new PriorityQueue<>();
heap.add(3); heap.add(1);
System.out.println(heap.poll()); // 1


//Биномиальная куча
BinomialHeap heap = new BinomialHeap();
heap.insert(5);
heap.insert(2);
heap.insert(8);
System.out.println(heap.findMin());


//Куча фибоначчи
FibonacciHeap fibHeap = new FibonacciHeap();
fibHeap.insert(3);
fibHeap.insert(1);
fibHeap.insert(4);
System.out.println(fibHeap.extractMin());


//Хэш-таблицы
import java.util.HashMap;
HashMap<String, String> hashTable = new HashMap<>();
hashTable.put("key", "value");
System.out.println(hashTable.get("key")); // value
