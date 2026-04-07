class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        hashmap = {i:[] for i in range(n)}
        for key ,value in edges:
            hashmap[key].append(value)
            hashmap[value].append(key)
        visit = set()
        def dfs(i):
            if i in visit:
                return 0
            visit.add(i)
            for j in hashmap[i]:
                dfs(j)
            return 1
        count = 0
        for i in range(n):
            count += dfs(i)
        
        return count