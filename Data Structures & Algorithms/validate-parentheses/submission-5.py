class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {"{":"}", "[": "]", "(":")"}
        stack = []
      
        for ch in s:
            if ch in mapping:
                stack.append(ch)
            if ch in ['}', ')', ']']:
                if stack and mapping[stack[-1]] == ch:
                    stack.pop()
                else:
                    return False
        return len(stack)==0

        