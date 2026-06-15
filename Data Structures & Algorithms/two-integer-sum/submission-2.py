class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        enumerate_nums = []
        for i, num in enumerate(nums):
            enumerate_nums.append([num, i])

        enumerate_nums.sort()
        result = []
        first = 0
        last = len(enumerate_nums) - 1
        while first < last:
            if enumerate_nums[first][0] + enumerate_nums[last][0] > target:
                last -= 1
                continue
            if enumerate_nums[first][0] + enumerate_nums[last][0] < target:
                first += 1
                continue
            if enumerate_nums[first][0] + enumerate_nums[last][0] == target:
                result.append(enumerate_nums[first][1])
                result.append(enumerate_nums[last][1])
                return [min(result), max(result)]
        return []
