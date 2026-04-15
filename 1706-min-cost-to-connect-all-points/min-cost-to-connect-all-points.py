import heapq

class Solution:
    def minCostConnectPoints(self, points: list[list[int]]) -> int:
        n = len(points)
        # min-heap хранит кортежи: (стоимость_ребра, индекс_точки)
        # Начинаем с точки 0, стоимость подключения 0
        min_heap = [(0, 0)] 
        visited = set()
        total_cost = 0
        
        # Работаем, пока не посетим все n точек
        while len(visited) < n:
            cost, current_point = heapq.heappop(min_heap)
            
            # Если точка уже в остове, пропускаем
            if current_point in visited:
                continue
                
            # Добавляем точку в остов и плюсуем стоимость ребра
            visited.add(current_point)
            total_cost += cost
            
            # Проверяем все остальные точки (так как граф полный, каждая соединена с каждой)
            for next_point in range(n):
                if next_point not in visited:
                    # Вычисляем Манхэттенское расстояние
                    x1, y1 = points[current_point]
                    x2, y2 = points[next_point]
                    dist = abs(x1 - x2) + abs(y1 - y2)
                    
                    # Добавляем потенциальное ребро в кучу
                    heapq.heappush(min_heap, (dist, next_point))
                    
        return total_cost