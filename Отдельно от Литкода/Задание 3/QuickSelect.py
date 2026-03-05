import random

# partition по Ломуто — тот же, что в QuickSort
def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quick_select(arr, k):
    low, high = 0, len(arr) - 1

    while low <= high:
        # рандомизация pivot
        rand_index = random.randint(low, high)
        arr[rand_index], arr[high] = arr[high], arr[rand_index]

        # разделение массива
        p = partition(arr, low, high)

        if p == k:
            return arr[p]          # нашли k-й наименьший
        elif k < p:
            high = p - 1           # ищем в левой части
        else:
            low = p + 1            # ищем в правой части
arr = [1,3,6,1,2,7,8,12]
result = quick_select(arr, k=5-1) # Так как индексы с 0
print("5-й наименьший элемент:", result)
