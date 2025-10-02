# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.max=0
        def dfs(root,count=0, state='central'):
            if not root:
                return 
            self.max=max(self.max,count)
            if state=='central':
                dfs(root.right,1,'right')
                dfs(root.left,1,'left')
            if state=='right':
                count+=1
                dfs(root.left,count,'left')
                dfs(root.right,1,'right')
            if state=='left':
                count+=1
                dfs(root.right,count,'right')
                dfs(root.left,1,'left')

        dfs(root,0,'central')
        return self.max