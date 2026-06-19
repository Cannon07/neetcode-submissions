class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0 
        for i in range(len(heights)):
            for j in range(len(heights)):
                min_height = min(heights[i], heights[j])
                distance = abs(i - j)
                area = min_height * distance
                if max_area < area:
                    max_area = area
        return max_area