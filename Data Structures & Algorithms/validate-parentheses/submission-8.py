class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        opening_braces = ['{', '[','(']
        closing_braces = [')',']','}']
        mappings={'(':')', '{':'}', '[':']'}
        for ch in s:
            if ch in closing_braces and len(stack)==0:
                return False
            if ch in opening_braces:
                stack.append(ch)
            elif ch==mappings[stack[-1]]:
                stack.pop()
            else:
                return False
        return len(stack)==0

