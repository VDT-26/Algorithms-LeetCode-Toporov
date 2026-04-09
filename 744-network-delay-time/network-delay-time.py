import collections
import heapq

class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        # Строим граф в виде списка смежности
        graph = collections.defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))
            
        # min-heap хранит кортежи: (накопленное_время, узел)
        min_heap = [(0, k)] 
        visited = set()
        max_time = 0
        
        while min_heap:
            # Берем узел, до которого можно добраться быстрее всего
            time, node = heapq.heappop(min_heap)
            
            if node in visited:
                continue
                
            visited.add(node)
            max_time = max(max_time, time) # Обновляем общее время
            
            # Добавляем соседей в кучу
            for neighbor, weight in graph[node]:
                if neighbor not in visited:
                    heapq.heappush(min_heap, (time + weight, neighbor))
                    
        # Проверяем, все ли узлы были посещены
        return max_time if len(visited) == n else -1