class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        frequency_s = {}
        for ch in s:
            frequency_s[ch] = frequency_s.get(ch,0)+1
        
        frequency_t = {}
        for ch in t:
            frequency_t[ch] = frequency_t.get(ch,0)+1
        
        return frequency_s == frequency_t
            
        