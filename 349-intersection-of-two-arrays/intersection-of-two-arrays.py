class Solution:
    def intersection(self, nums1, nums2):
        set1 = set(nums1)
        set2 = set(nums2)
        return list(set1 & set2) #автоматом выбираем пересечения ._.

"""
Я бы так сделал, но неэффективно. Надо ззапомнить первый вариант
class Solution:
    def intersection(self, nums1, nums2):
        seen = set()
        duplicates = []

        for x in nums1:
            if x in seen:
                duplicates.append(x)   # повтор — отправляем в список
            else:
                seen.add(x)

        result = []
        set2 = set(nums2)

        for x in seen:
            if x in set2:
                result.append(x)

        return result
"""