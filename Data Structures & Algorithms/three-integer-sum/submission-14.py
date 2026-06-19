class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        # print(nums)
        for i in range(len(nums)):
            start = i + 1
            end = len(nums) - 1
            while not(start >= end):
                # print(f"nums[i]={nums[i]}, nums[start]={nums[start]}, nums[end]={nums[end]}")
                curr_sum = nums[start] + nums[end] + nums[i]
                if curr_sum == 0:
                    triplet = [nums[start], nums[end], nums[i]]
                    # print(f"triplet={triplet}")
                    if triplet not in result:
                        result.append(triplet)
                    start += 1
                    end -= 1
                if curr_sum > 0:
                    end -= 1
                if curr_sum < 0:
                    start += 1

        return result