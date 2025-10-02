# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.max=0
        def search(root, count=0, state='central'):
            if not root:
                return 
            self.max=max(self.max,count)
            if state=='central':
                search(root.right,1,'right')
                search(root.left,1,'left')
            if state =="left" :
                count+=1
                search(root.right,count,'right')
                search(root.left,1,'left')
            if state =="right":
                count+=1
                search(root.left,count,'left')
                search(root.right,1,'right')
        

        search(root,0,'central')
        return self.max 
        

