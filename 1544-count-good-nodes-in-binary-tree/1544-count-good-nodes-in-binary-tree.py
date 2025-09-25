# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # for a single root case 
        if not root:
            return 0
        
        def CountMax(root, max_value=float('-inf')):
            count=0
            if not root:
                return 0
            if root.val >=max_value:
                print('Identified the new count')
                max_value=root.val
                count+=1
            count+=CountMax(root.left,max_value)
            count+=CountMax(root.right,max_value)
            return count
        return CountMax(root,max_value=float('-inf'))
       


        