class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = []
        for i in range(len(temperatures)):
            result.append(0)
        
        stack = []
        for tempIndex, temp in enumerate(temperatures):
            while stack and stack[-1][0] < temp:
                topTemp, topTempIndex = stack.pop()
                result[topTempIndex] = tempIndex - topTempIndex
            stack.append([temp, tempIndex])
        return result
             

        