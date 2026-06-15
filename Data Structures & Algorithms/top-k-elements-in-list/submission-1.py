class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []
        bucket_map = {} 
        hash_map = {}
        for i in range(len(nums)):
            if nums[i] not in hash_map:
                hash_map[nums[i]] = 0
            hash_map[nums[i]] += 1
            bucket_map[i] = []
        
        for i in hash_map:
            freq = hash_map[i]
            bucket_map[freq - 1].append(i)
        
        hits = 0
        for i in range(len(nums))[::-1]:
            if len(bucket_map[i]) != 0:
                for j in range(len(bucket_map[i]))[::-1]:
                    result.append(bucket_map[i][j])
                    hits += 1
                    if (hits == k):
                        return result
        return []
        