class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        nums_set = set()
        for i in nums:
            nums_set.add(i);
        sorted_set = list(nums_set)
        sorted_set.sort()
        count = 0
        max_count = 0
        for i in range(1, len(sorted_set)):
            if (sorted_set[i] - sorted_set[i-1] == 1):
                count += 1
                if max_count < count:
                    max_count = count
            else:
                count = 0
        return max_count + 1