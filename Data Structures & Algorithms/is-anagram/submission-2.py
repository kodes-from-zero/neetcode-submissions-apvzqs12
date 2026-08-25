class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s1 = {}
        t1={}
        for ch in s:
            s1[ch]=s1.get(ch,0)+1
        for ch in t:
            t1[ch] = t1.get(ch,0)+1
        return s1 == t1
        
