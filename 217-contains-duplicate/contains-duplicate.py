class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        seen = set() #Как словарь, только хранит ключи без повторений.
        for x in nums:
            if x in seen:
                return True
            seen.add(x)
        return False