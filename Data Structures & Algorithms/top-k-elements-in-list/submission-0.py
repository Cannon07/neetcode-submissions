class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []
        hash_map = {}
        for num in nums:
            if num not in hash_map:
                hash_map[num] = 0
            hash_map[num] += 1
        
        freq_arr = []
        for i in hash_map:
            freq_arr.append([hash_map[i], i])

        freq_arr.sort(reverse=True)
        print(freq_arr)
        for i in range(k):
            result.append(freq_arr[i][1])
        return result 
        