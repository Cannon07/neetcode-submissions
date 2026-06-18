class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start = 0
        end = len(numbers) - 1 
        while not(start >= end):
            start_num = numbers[start]
            end_num = numbers[end]
            if (start_num + end_num == target):
                return [start + 1, end + 1]
            if (start_num + end_num > target):
                end -= 1 
            if (start_num + end_num < target):
                start += 1
        return []