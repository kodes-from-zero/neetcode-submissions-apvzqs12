class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        new_nums = set(nums)
        print(new_nums)
        return len(nums) != len(new_nums)