//Сортировка выбором (Selection Sort)
#include <iostream>
#include <vector>

// Функция сортировки выбором
void selection_sort(std::vector<int>& arr) {
    int n = arr.size();
    // Проходим по всем элементам массива
    for (int i = 0; i < n; ++i) {
        // Предполагаем, что текущий элемент - минимальный
        int min_index = i;

        // Ищем минимальный элемент в оставшейся части массива
        for (int j = i + 1; j < n; ++j) {
            if (arr[j] < arr[min_index]) {
                min_index = j;  // Обновляем индекс минимального элемента
            }
        }

        // Меняем местами текущий элемент с найденным минимальным
        std::swap(arr[i], arr[min_index]);
    }
}

int main() {
    // Соз тестовый массив
    std::vector<int> test_array = {64, 25, 12, 22, 11};

    // Вывод исходного массива
    std::cout << "Исходный массив: ";
    for (int num : test_array) {
        std::cout << num << " ";
    }
    std::cout << std::endl;

    // Сортируем массив
    selection_sort(test_array);

    // Вывод отсортированного массива
    std::cout << "Отсортированный массив: ";
    for (int num : test_array) {
        std::cout << num << " ";
    }
    std::cout << std::endl;

    return 0;
}
