class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        # Проверка на пустую сетку
        if not grid:
            return 0
        
        rows = len(grid)
        cols = len(grid[0])
        islands_count = 0
        
        # Функция для обхода и "затопления" острова
        def dfs(r, c):
            # Базовый случай: выход за границы или попадание на воду ('0')
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == '0':
                return
            
            # "Топим" текущий участок суши, чтобы не посчитать его дважды
            grid[r][c] = '0'
            
            # Идем исследовать соседей
            dfs(r - 1, c) # Вверх
            dfs(r + 1, c) # Вниз
            dfs(r, c - 1) # Влево
            dfs(r, c + 1) # Вправо

        # Проходим по каждой клетке матрицы
        for r in range(rows):
            for c in range(cols):
                # Если нашли кусок суши
                if grid[r][c] == '1':
                    islands_count += 1 # Увеличиваем счетчик островов
                    dfs(r, c)          # Запускаем обход, который "уничтожит" весь этот остров
                    
        return islands_count