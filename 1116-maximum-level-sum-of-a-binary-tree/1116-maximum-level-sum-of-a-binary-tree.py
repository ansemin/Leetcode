# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        queue=deque([root])
        max_sum=float('-inf')
        max_level=0
        current_level=1
        while queue:
            level_size=len(queue)
            current_sum=0
            for i in range(level_size):
                node=queue.popleft()
                current_sum+=node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if current_sum>max_sum:
                max_sum=current_sum
                max_level=current_level
            current_level+=1
        return max_level