class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1 
        nums_min = float('inf')
        while left <= right:
            middle = (left + right) // 2
            nums_min = min(nums_min, nums[middle])
            if nums[left] <= nums[right]:
                return min(nums_min, nums[left])
            if nums[middle] >= nums[left]:
                left = middle + 1
            else:
                right = middle - 1
        return nums_min
            