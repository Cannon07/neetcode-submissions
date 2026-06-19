class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0 
        start = 0
        end = len(heights) - 1
        while not(start >= end):
            tank_height = min(heights[start], heights[end]) 
            tank_area = tank_height * (end - start)
            if max_area < tank_area:
                max_area = tank_area
            if heights[start] <= heights[end]:
                start += 1
            else:
                end -= 1
        return max_area