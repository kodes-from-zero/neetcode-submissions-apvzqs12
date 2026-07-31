class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        i=0
        res=[]
        nums.sort()
        for i in range(len(nums)-2):
            if i >0 and nums[i]==nums[i-1]:
                print(i)
                i=i+1
                continue
            j=i+1
            k=len(nums)-1
            while j<k:
                if nums[i]+nums[j]+nums[k] == 0:
                    res.append([nums[i],nums[j],nums[k]])
                    j=j+1
                    k=k-1
                    
                    while j <k and nums[j]==nums[j-1] and nums[k]==nums[k+1]:
                        j=j+1
                        k=k-1
                        continue
                elif nums[i]+nums[j]+nums[k] < 0:
                    j=j+1
                else:
                    k=k-1
        return res

           

