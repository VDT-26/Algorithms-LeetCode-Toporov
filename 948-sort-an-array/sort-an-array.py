class Solution:
    def sortArray(self, nums):
        def merge_sort(arr):
            if len(arr) <= 1:
                return arr
            
            mid = len(arr) // 2
            left = merge_sort(arr[:mid]) #Вот тут вообще забавно. В с++: vector<int> left(arr.begin(), arr.begin() + mid);
            right = merge_sort(arr[mid:]) #vector<int> right(arr.begin() + mid, arr.end());
            
            return merge(left, right)
        
        def merge(left, right):
            merged = []
            i = j = 0
            
            # Соединяем две отсортированные половины
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    merged.append(left[i])
                    i += 1
                else:
                    merged.append(right[j])
                    j += 1
            
            # Добавляем оставшиеся элементы
            while i < len(left):
                merged.append(left[i])
                i += 1
            
            while j < len(right):
                merged.append(right[j])
                j += 1
            
            return merged
        
        return merge_sort(nums)