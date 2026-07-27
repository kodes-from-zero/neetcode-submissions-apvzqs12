class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #brute force:
        # dict1={}
        # res=[]
        # for num in nums:
        #     dict1[num] = dict1.get(num,0)+1
        # sorted_list = sorted(dict1.items(), key=lambda x:x[1], reverse=True)
        # for x in sorted_list[:k]:
        #     res.append(x[0])
        # return res
        #optimal approach:
        res = []
        dict1={}
        for num in nums:
            dict1[num] = dict1.get(num,0)+1
        bucket = [[] for i in range(len(nums)+1)]
        for num, count in dict1.items():
            bucket[count].append(num)
        for i in range(len(bucket)-1, 0, -1):
            for num in bucket[i]:
                res.append(num)
                if len(res)==k:
                    return res
            




        