class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operands = ['+', "-", "*", "/"]
        for i in tokens:
            if i not in operands:
                stack.append(int(i))
            else:
                if i == "+":
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(b+a)
                elif i == "-":
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(b-a)
                elif i == "*":
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(b*a)
                elif i == "/":
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(int(b/a))
        return stack.pop()
