class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        j=len(heights)-1
        i=0
        while i<j:
            w = j-i
            h=min(heights[i],heights[j])
            area = w * h
            if heights[i]>heights[j]:
                j=j-1
            else:
                    i=i+1
            max_area=max(area,max_area)

        return max_area
            
        