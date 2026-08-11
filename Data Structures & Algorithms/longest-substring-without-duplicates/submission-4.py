class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        str_set = set()
        max_len=0
        leng=0
        j=0
        for i in range(len(s)):
            while  s[i] in str_set:
                str_set.remove(s[j])
                j=j+1
                leng=leng-1
            str_set.add(s[i])
            leng=leng+1
            max_len= max(max_len, leng)
        return max_len

