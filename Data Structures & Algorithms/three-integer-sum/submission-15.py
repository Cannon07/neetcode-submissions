class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        for i in range(len(nums)):
            start = i + 1
            end = len(nums) - 1
            while not(start >= end):
                curr_sum = nums[start] + nums[end] + nums[i]
                if curr_sum == 0:
                    triplet = [nums[start], nums[end], nums[i]]
                    if triplet not in result:
                        result.append(triplet)
                    start += 1
                    end -= 1
                if curr_sum > 0:
                    end -= 1
                if curr_sum < 0:
                    start += 1

        return result