def quick_sort(array, low, high):
    if low < high:
        # pi — индекс разбиения, элемент на своём месте
        pi = partition(array, low, high)
        # Рекурсивная сортировка элементов до и после разбиения
        quick_sort(array, low, pi - 1)
        quick_sort(array, pi + 1, high)

def partition(array, low, high):
    pivot = array[high]  # выбираем последний элемент в качестве опорного
    i = low - 1  # индекс меньшего элемента
    for j in range(low, high):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]
    # перемещаем опорный элемент на его правильную позицию
    array[i + 1], array[high] = array[high], array[i + 1]
    return i + 1

def print_array(array):
    for value in array:
        print(value, end=' ')
    print()

if __name__ == "__main__":
    array = [10, 7, 8, 9, 1, 5]
    print("Исходный массив:")
    print_array(array)

    quick_sort(array, 0, len(array) - 1)

    print("\nОтсортированный массив:")
    print_array(array)
