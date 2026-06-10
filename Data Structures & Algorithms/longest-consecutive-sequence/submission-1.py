class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        seq_len = 0
        for x in nums_set:
            if x-1 not in nums_set:
                seq_len_start = 1
                k=x+1
                while k in nums_set:
                    seq_len_start += 1
                    k= k+1
                if seq_len_start > seq_len:
                    seq_len = seq_len_start
        return seq_len