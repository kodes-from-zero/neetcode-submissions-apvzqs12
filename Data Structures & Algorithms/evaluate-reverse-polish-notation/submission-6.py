class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operands = ['+','-','*','/']
        res=0
        for t in tokens:
            if t not in operands:
                stack.append(int(t))
            else:
                if t == '+':
                    a = stack.pop()
                    b = stack.pop()
                    res=a+b
                    stack.append(res)
                elif t == '*':
                    a = stack.pop()
                    b = stack.pop()
                    res=a*b
                    stack.append(res)
                elif t == '-':
                    a = stack.pop()
                    b = stack.pop()
                    res=(b-a)
                    stack.append(res)
                else:
                    a=stack.pop()
                    b=stack.pop()
                    res = int(b/a)
                    stack.append(res)
        return stack[-1]



            
        