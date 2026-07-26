class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict1 = {}
        for index,num in enumerate(nums):
            res = target - num
            if res in dict1:
                return [dict1[res], index]
            dict1[num]=index
            