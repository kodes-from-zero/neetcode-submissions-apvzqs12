class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        lp=[1]* len(nums)
        rp=[1]* len(nums)
        product = [1]*len(nums)
        for i in (range(1,len(nums))):
            lp[i]=lp[i-1]*nums[i-1]
        for i in (range(len(nums)-2, -1, -1)):
            rp[i]=rp[i+1]*nums[i+1]
        for i in range(len(nums)):
            product[i] = lp[i]*rp[i]
        return product

             
        