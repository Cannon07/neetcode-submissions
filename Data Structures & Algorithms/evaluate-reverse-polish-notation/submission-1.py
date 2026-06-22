class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ["+", "-", "*", "/"]
        for i in tokens:
            if i in operators:
                secondVal = int(stack.pop())
                firstVal = int(stack.pop())

                if i == "+":
                    result = firstVal + secondVal
                    stack.append(result)
                
                if i == "-":
                    result = firstVal - secondVal
                    stack.append(result)

                if i == "*":
                    result = firstVal * secondVal
                    stack.append(result)

                if i == "/":
                    result = firstVal / secondVal
                    stack.append(result)
            else:
                stack.append(i)

        return int(stack.pop())
        