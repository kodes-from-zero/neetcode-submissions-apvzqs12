class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        i=0
        numset = set(nums)
        maxLen=0
        while i < len(nums):
            if nums[i]-1 not in numset:
                seqStart = nums[i]
                seqLen=1
                while seqStart + 1 in numset:
                    seqLen +=1
                    seqStart+=1
                maxLen = max(maxLen, seqLen)
            i=i+1
        return maxLen
                    


        