from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)      # Тут не как в с++, можно просто импортировать библиотеку, которая сама считает частоты.
        heap = []                 # 2. Создаём min-heap

        for num, count in freq.items():
            heapq.heappush(heap, (count, num))  # кладём (частота, число)
            if len(heap) > k:                   # если куча > k → удаляем минимум
                heapq.heappop(heap)

        return [num for count, num in heap]     # возвращаем числа