class Solution:
    def climbStairs(self, n: int) -> int:
        # кеш 
        # номер ступеньки : количество способов
        memo = {}
        
        def stepper(step):
            # 1. Базовые случаи
            if step == 1:
                return 1
            if step == 2:
                return 2
            
            # 2. Проверяем кэш: если уже считали, возвращаем готовое
            if step in memo:
                return memo[step]
            
            # 3. Если в кэше нет, вычисляем рекурсивно
            result = stepper(step - 1) + stepper(step - 2)
            
            # 4. Обязательно сохраняем результат в кэш перед возвратом
            memo[step] = result
            return result
            
        # Запускаем рекурсию с самой верхней ступеньки
        return stepper(n)