class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i == "[" or i == "(" or i == "{":
                stack.append(i)
                continue
            if len(stack) != 0:
                if i == ")":
                    if stack[-1] == "(":
                        stack.pop()
                        continue
                if i == "}":
                    if stack[-1] == "{":
                        stack.pop()
                        continue
                if i == "]":
                    if stack[-1] == "[":
                        stack.pop()
                        continue
            return False
        
        if len(stack) != 0:
            return False
        return True
                
            
        