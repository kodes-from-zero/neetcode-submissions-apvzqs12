class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map1={}
        for num in nums:
            map1[num] = map1.get(num,0)+1
        sorted_list = sorted(map1.items(), key=lambda x :x[1], reverse=True)
        return [x[0] for x in sorted_list[:k]]
        
       
      