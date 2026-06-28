class TimeMap:

    def __init__(self):
        self.timeMap = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timeMap:
            self.timeMap[key] = {}
        self.timeMap[key][timestamp] = value

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timeMap:
            return ""
        if timestamp in self.timeMap[key]:
            return self.timeMap[key][timestamp]
        
        maxTimestamp = float('-inf')
        for i in self.timeMap[key]:
            if i <= timestamp:
                maxTimestamp = max(maxTimestamp, i)
        if maxTimestamp <= timestamp and maxTimestamp != float('-inf'):
            return self.timeMap[key][maxTimestamp]
        return ""