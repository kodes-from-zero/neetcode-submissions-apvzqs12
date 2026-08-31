class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #create buckets for each count 
        frequency = {}
        for num in nums:
            frequency[num] = frequency.get(num,0)+1
        b = [[] for _ in range(len(nums)+1)]
        for num, count in frequency.items():
            b[count].append(num)
        res = []
        for i in range(len(b)-1, 0, -1):
            for j in b[i]:
                res.append(j)
                if len(res)==k:
                    return res


        

    

        