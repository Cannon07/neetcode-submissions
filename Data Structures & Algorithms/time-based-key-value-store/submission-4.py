class TimeMap:

    def __init__(self):
        self.timeMap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timeMap:
            self.timeMap[key] = []
        self.timeMap[key].append([timestamp, value]) 
        
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timeMap:
            return ""
        
        valueList = self.timeMap[key]
        left = 0
        right = len(valueList) - 1
        maxTimestamp = float('-inf')
        maxTimestampValue = ""
        while left <= right:
            middle = (left + right) // 2
            if valueList[middle][0] <= timestamp:
                if valueList[middle][0] == timestamp:
                    return valueList[middle][1]
                if maxTimestamp < valueList[middle][0]:
                    maxTimestamp = valueList[middle][0]
                    maxTimestampValue = valueList[middle][1]
            if valueList[middle][0] < timestamp:
                left = middle + 1
            else:
                right = middle - 1
        
        if maxTimestamp == float('-inf'):
            return ""
        return maxTimestampValue