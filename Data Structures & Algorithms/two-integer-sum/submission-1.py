class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map1 = {}
        for i in range(len(nums)):
            num = target - nums[i]
            if map1 and num in map1:
                return [map1[num], i]
            map1[nums[i]] = i
         

        