"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        cur = root
        def dfs(cur,parent):
            if not cur:
                return None
            if p == cur or q == cur:
                return cur
            
            l = dfs(cur.left,cur)
            r = dfs(cur.right,cur)
            if l and r:
                return cur
            
            return r or l
            
            


            
        return dfs(cur,root)
        