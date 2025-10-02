# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.path=0
        from collections import defaultdict
        self.pathSum=defaultdict(int)
        self.pathSum[0]=1
        
        def dfs(root,currSum):
            if not root:
                return 
            currSum+=root.val
            self.path+=self.pathSum[currSum-targetSum]
            self.pathSum[currSum]+=1
            if root.right:
                dfs(root.right,currSum)
            if root.left:
                dfs(root.left,currSum)
            self.pathSum[currSum]-=1
        dfs(root,0)
        return self.path 