class Solution:
    def trap(self, height: List[int]) -> int:
        left_max= [0]*len(height)
        right_max=[0]*len(height)
        max_height =0
        for i in range(1,len(height)-1):
            left_max[i]=max(left_max[i-1], height[i-1])
        for i in range(len(height)-2,-1,-1):
            right_max[i]=max(right_max[i+1],height[i+1])
        for i in range(1,len(height)-1):
            max_height += max(min(right_max[i],left_max[i])-height[i],0)
        return max_height


        
        