class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        total_sum = sum(nums)
        
        # 1. Если общая сумма нечетная, поделить пополам нельзя
        if total_sum % 2 != 0:
            return False
            
        target = total_sum // 2
        
        # 2. Множество для хранения всех достижимых сумм.
        # Изначально мы можем собрать сумму 0 (не взяв ни одного числа)
        dp = set([0])
        
        # 3. Проходим по каждому числу в массиве
        for num in nums:
            next_dp = set() # Временное множество для следующего шага
            
            for t in dp:
                # Если текущая сумма + новое число дает нашу цель - мы победили!
                if t + num == target:
                    return True
                
                # Добавляем в копилку новый вариант (взяли число)
                next_dp.add(t + num)
                # Переносим старый вариант (не взяли число)
                next_dp.add(t)
                
            # Обновляем наше главное множество
            dp = next_dp
            
        return target in dp