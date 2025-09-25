# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        # Base case 
        def GetLeaf(root, leave_list):
            if not root:
                return 
            if not root.left and not root.right:
                leave_list.append(root.val)
            GetLeaf(root.left,leave_list)
            GetLeaf(root.right,leave_list)
        root1_list=[]
        GetLeaf(root1,root1_list)
        root2_list=[]
        GetLeaf(root2,root2_list)
        return root1_list==root2_list
       
        