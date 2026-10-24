# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = deque([root])
        res = []
        while queue:
            level = []
            for i in range(len(queue)):
                n = queue.popleft()
                if n and n.left:
                    queue.append(n.left)
                if n and n.right:
                    queue.append(n.right)
                level.append(n.val)
            res.append(level)
        
        return res
            
                

        