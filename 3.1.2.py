# Функция для сортировки массива методом пузырька
def bubble_sort(arr):
    n = len(arr)
    # Проходим по всем элементам массива
    for i in range(n - 1):
        # На каждой итерации последний элемент уже на своем месте
        for j in range(n - i - 1):
            # Сравниваем соседние элементы
            if arr[j] > arr[j + 1]:
                # Меняем местами, если они стоят в неправильном порядке
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Функция для вывода массива
def print_array(arr):
    for num in arr:
        print(num, end=' ')
    print()

# Основной блок программы
if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    print("Исходный массив:")
    print_array(arr)

    # Сортируем массив
    bubble_sort(arr)

    print("Отсортированный массив:")
    print_array(arr)
