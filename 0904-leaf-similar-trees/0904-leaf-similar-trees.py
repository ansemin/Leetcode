# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def GetLeaf(root, numbers):
            if not root:
                return 
            if not root.left and not root.right:
                numbers.append(root.val)
            GetLeaf(root.left,numbers)
            GetLeaf(root.right,numbers)
        root1_list=[]
        root2_list=[]
        GetLeaf(root1,root1_list)
        GetLeaf(root2,root2_list)
        return root1_list==root2_list