class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = []
        for i in range(len(temperatures)):
            count = 0
            result.append(count)
            for j in range(i, len(temperatures)):
                if temperatures[j] > temperatures[i]:
                    result[i] = count
                    break
                count += 1

        return result