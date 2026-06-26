class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_k = max(piles)
        k = max_k

        left = 1
        right = max_k
        while left <= right:
            middle = (left + right) // 2
            hours = 0
            for j in piles:
                hours += math.ceil(j/middle)
            if hours > h:
                left = middle + 1
            else: 
                right = middle - 1
            if hours <= h:
                k = min(middle, k)
        return k 