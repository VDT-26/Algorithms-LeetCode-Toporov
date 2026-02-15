class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Устанавливаем границы поиска
        left, right = 0, len(nums) - 1

        # Пока границы не пересеклись
        while left <= right:
            mid = (left + right) // 2  # середина массива

            if nums[mid] == target:
                return mid  # нашли элемент
            elif nums[mid] < target:
                left = mid + 1  # ищем справа
            else:
                right = mid - 1  # ищем слева

        return -1  # не нашли