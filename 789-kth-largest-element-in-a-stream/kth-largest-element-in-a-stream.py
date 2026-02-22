import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = nums
        heapq.heapify(self.heap)  # превращаем список в min-heap
        
        # если элементов больше k — удаляем лишние (минимальные)
        while len(self.heap) > k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        
        # если стало больше k — удаляем минимальный
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        
        # k-й по величине — это минимальный в куче
        return self.heap[0]