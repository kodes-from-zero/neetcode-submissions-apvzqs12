class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pSum = [1] * len(nums)
        sSum = [1] * len(nums)
        output = [1] * len(nums)
        for i in range(1,len(nums)):
            pSum[i] = pSum[i-1]*nums[i-1]
        for i in range(len(nums)-2,-1,-1):
            sSum[i]= sSum[i+1]*nums[i+1]
        for i in range(len(nums)):
            output[i] = pSum[i]*sSum[i]
        return output
            