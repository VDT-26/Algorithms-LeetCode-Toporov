def selection_sort(arr):
    """
    Сортировка выбором (Selection Sort).
    Алгоритм ищет минимальный элемент в неотсортированной части списка
    и ставит его на текущую позицию.
    """
    # Проходим по всем позициям списка
    for i in range(len(arr)):
        min_index = i  # считаем текущий элемент минимальным
        # Ищем минимальный элемент в оставшейся части массива
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        # Меняем местами текущий элемент и найденный минимум
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr
# --- Взаимодействие с пользователем ---
print("Сортировка выбором (Selection Sort)")
print("Введите числа через пробел:")
# Получаем строку от пользователя
user_input = input("> ")
# Преобразуем строку в список чисел
numbers = list(map(int, user_input.split()))
print("\nИсходный список:", numbers)
# Сортируем
sorted_numbers = selection_sort(numbers)
print("Отсортированный список:", sorted_numbers)
