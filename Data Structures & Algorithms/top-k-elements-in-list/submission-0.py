class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = [[] for _ in range(len(nums)+1)]
        hashmap = {}
        ans =[]
        for n in nums:
            hashmap[n] = 1 + hashmap.get(n,0)

        for key,values in hashmap.items():
            res[values].append(key)
        
        for i in range(len(res)-1,-1,-1):

            for j in res[i]:
                ans.append(j)
                if len(ans) == k:
                    return ans




        