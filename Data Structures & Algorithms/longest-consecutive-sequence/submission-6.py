class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset=set(nums)
        longest = 0
        for n in numset:
            if (n-1) not in numset:
                len=1
                current=n
                while current+1 in numset:
                    len=len+1
                    current=current+1
                longest = max(len, longest)
        return longest
