from collections import deque

class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        queue = deque()
        fresh_count = 0
        
        # Шаг 1: Сканируем сетку. Считаем свежие, гнилые добавляем в очередь
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c)) # Гнилой апельсин — это стартовая точка
                elif grid[r][c] == 1:
                    fresh_count += 1     # Свежий апельсин
                    
        # Если свежих апельсинов изначально нет, время равно 0
        if fresh_count == 0:
            return 0
            
        minutes = 0
        # Возможные направления (вверх, вниз, влево, вправо)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        # Шаг 2: Поиск в ширину (BFS)
        # Работаем, пока есть гнилые апельсины в очереди И остались свежие
        while queue and fresh_count > 0:
            minutes += 1
            
            # Обрабатываем строго один "слой" (одну минуту времени)
            for _ in range(len(queue)):
                r, c = queue.popleft() # Достаем гнилой апельсин
                
                # Проверяем 4 соседние клетки
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    
                    # Если сосед находится в пределах сетки и это свежий апельсин
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2          # Он заражается и становится гнилым
                        fresh_count -= 1          # Уменьшаем счетчик свежих
                        queue.append((nr, nc))    # Добавляем его в очередь для следующей минуты
                        
        # Если после завершения процесса остались свежие апельсины, возвращаем -1
        return minutes if fresh_count == 0 else -1