import random

def partition(arr, low, high):
    pivot = arr[high]          # опорный элемент (уже рандомизирован)
    i = low - 1                # граница элементов < pivot

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    # ставим pivot на место
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quick_sort(arr, low, high):
    if low < high:
        # рандомизация опорного элемента
        rand_index = random.randint(low, high)
        arr[rand_index], arr[high] = arr[high], arr[rand_index]

        # разделение
        p = partition(arr, low, high)

        # рекурсивные вызовы
        quick_sort(arr, low, p - 1)
        quick_sort(arr, p + 1, high)
arr = [9, 3, 7, 1, 8, 2, 5]
quick_sort(arr, 0, len(arr) - 1)
print(arr)
