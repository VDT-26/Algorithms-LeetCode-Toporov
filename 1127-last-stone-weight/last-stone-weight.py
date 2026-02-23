import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # превращаем в max-heap через отрицательные числа
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            y = -heapq.heappop(stones)  # самый тяжёлый
            x = -heapq.heappop(stones)  # второй по тяжести

            if y != x:
                heapq.heappush(stones, -(y - x))

        return -stones[0] if stones else 0