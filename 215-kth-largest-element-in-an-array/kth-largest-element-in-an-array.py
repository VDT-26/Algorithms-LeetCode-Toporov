class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        import heapq #стандартная библиотека Python, реализующая минимальную кучу
        
        heap = [] #пустая куча
        for n in nums:
            heapq.heappush(heap, n) #Добавление элемента в конец и "всплывание"
            if len(heap) > k: #Если элементов больше К, то удаляем наименьший
                heapq.heappop(heap) #Как раз удаление минимального элемента
        return heap[0]