import numpy as np
from timeit import default_timer as timer


# Реализация алгоритма пузырьковой сортировки
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return


# Реализация алгоритма сортировки выбором
def selection_sort(array, size):
    for s in range(size):
        min_idx = s
        for i in range(s + 1, size):
            if array[i] < array[min_idx]:
                min_idx = i
            (array[s], array[min_idx]) = (array[min_idx], array[s])
    return


# Реализация алгоритма сортировки вставками
def insertion_sort(list1):
    for i in range(1, len(list1)):
        a = list1[i]
        j = i - 1
        while j >= 0 and a < list1[j]:
            list1[j + 1] = list1[j]
            j -= 1
        list1[j + 1] = a
    return


# Реализация алгоритма сортировки Шелла
def shell_sort(datta: list[int]) -> list[int]:
    last_index = len(datta)
    step = len(datta)//2
    while step > 0:
        for i in range(step, last_index, 1):
            j = i
            delta = j - step
            while delta >= 0 and data[delta] > data[j]:
                datta[delta], data[j] = datta[j], datta[delta]
                j = delta
                delta = j - step
        step //= 2
    return


# Реализация алгоритма сортировки расческой
def comb_sort(alist):
    alen = len(alist)
    gap = (alen * 10 // 13) if alen > 1 else 0
    while gap:
        if 8 < gap < 11:
            gap = 11
        swapped = False
        for i in range(alen - gap):
            if alist[i + gap] < alist[i]:
                alist[i], alist[i + gap] = alist[i + gap], alist[i]
                swapped = True
        gap = (gap * 10 // 13) or swapped
    return


# Создаем массив
data = np.arange(1000)
# Получаем размер массива data
size = len(data)
# Примешиваем массив
np.random.shuffle(data)

# Засекаем время начала работы алгоритма
start = timer()

# bubble_sort(data)
# selection_sort(data, size)
# insertion_sort(data)
shell_sort(data)
# comb_sort(data)

# Засекаем время окончания работы алгоритма
end = timer()

# Выводим время работы алгоритма
print("Время работы алгоритма -> ", end - start, " ms")
