//Бинарная куча
#include <queue>
#include <vector>

std::priority_queue<int, std::vector<int>, std::greater<int>> minHeap;
minHeap.push(5);
minHeap.push(2);
minHeap.push(8);
std::cout << minHeap.top();  // 2 (минимум)
minHeap.pop();


//Биномиальная куча
#include <boost/heap/binomial_heap.hpp>
boost::heap::binomial_heap<int> heap;
heap.push(3); heap.push(1);
std::cout << heap.top(); heap.pop(); // 1


//Куча фибоначчи
#include <boost/heap/fibonacci_heap.hpp>
boost::heap::fibonacci_heap<int> heap;
heap.push(3); heap.push(1);
std::cout << heap.top(); heap.pop(); // 1


//Хэш-таблицы
#include <unordered_map>
std::unordered_map<std::string, std::string> hash_table;
hash_table["key"] = "value";
std::cout << hash_table["key"]; // value
