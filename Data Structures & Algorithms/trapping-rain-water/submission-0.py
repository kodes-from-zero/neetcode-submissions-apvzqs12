class Solution:
    def trap(self, height: List[int]) -> int:
        max_area = 0
        left_max =[0] * len(height)
        right_max = [0] * len(height)
        total_water = 0
        left_max[0] = 0
        right_max[len(height)-1] = 0
        for i in range(1,len(height)):
            left_max[i] = max(left_max[i-1], height[i-1])
        print(left_max)
        for i in range(len(height)-2, -1,-1):
            right_max[i] = max(right_max[i+1], height[i+1])
        print(right_max)
        for i in range(len(height)):
            water_level = min(left_max[i], right_max[i]) 
            if water_level > height[i]:
                total_water += water_level - height[i]
        return total_water