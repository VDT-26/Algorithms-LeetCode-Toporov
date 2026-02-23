class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        import heapq
        
        # max-heap: храним отрицательные расстояния
        heap = []
        
        for x, y in points:
            dist = -(x*x + y*y)  # отрицательное, чтобы куча была max-heap
            
            if len(heap) < k:
                heapq.heappush(heap, (dist, x, y))
            else:
                # если текущая точка ближе, чем самая дальняя в куче
                if dist > heap[0][0]:
                    heapq.heapreplace(heap, (dist, x, y))
        
        return [[x, y] for (_, x, y) in heap]