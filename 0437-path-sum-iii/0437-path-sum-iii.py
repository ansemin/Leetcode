# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.count=0
        self.countDict=defaultdict(int)
        self.countDict[0]=1
        
        def dfs(node, currSum):
            if not node:
                return 
            currSum+=node.val
            self.count+=self.countDict[currSum-targetSum]
            self.countDict[currSum]+=1
            if node.left:
                dfs(node.left,currSum)
            if node.right:
                dfs(node.right,currSum)
            self.countDict[currSum]-=1
        
        dfs(root,0)
        return self.count