class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        # Запоминаем исходный цвет стартового пикселя
        original_color = image[sr][sc]
        
        # Если исходный цвет совпадает с новым, заливка не требуется
        if original_color == color:
            return image
        
        # Определяем размеры матрицы
        rows = len(image)
        cols = len(image[0])
        
        # Вложенная функция для поиска в глубину (DFS)
        def dfs(r, c):
            # Базовый случай: проверяем выход за границы матрицы 
            # и совпадает ли цвет текущего пикселя с исходным
            if r < 0 or r >= rows or c < 0 or c >= cols or image[r][c] != original_color:
                return
            
            # Закрашиваем текущий пиксель в новый цвет
            image[r][c] = color
            
            # Рекурсивно вызываем DFS для соседей (вверх, вниз, влево, вправо)
            dfs(r - 1, c) # Вверх
            dfs(r + 1, c) # Вниз
            dfs(r, c - 1) # Влево
            dfs(r, c + 1) # Вправо
            
        # Запускаем алгоритм со стартовых координат
        dfs(sr, sc)
        
        # Возвращаем измененную матрицу
        return image