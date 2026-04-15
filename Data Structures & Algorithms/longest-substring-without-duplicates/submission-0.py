class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len =0
        for i in range(len(s)):
            for j in range(i+1, len(s)+1):
                substr = s[i:j]
                if len(substr) == len(set(substr)):
                    max_len = max(max_len, j-i)
        return max_len

        