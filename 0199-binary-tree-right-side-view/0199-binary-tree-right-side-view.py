# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque 
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        queue=deque([root])
        result=[]
        while queue:
            level=len(queue)
            for i in range(level):
                current_level=queue.popleft()
                if i==level-1:
                    result.append(current_level.val)
                if current_level.left:
                    queue.append(current_level.left)
                if current_level.right:
                    queue.append(current_level.right)
        return result
                
        
        