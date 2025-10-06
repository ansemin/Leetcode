# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # BST so take advantage of the fact that 
        # if val < current.val -> go left 
        # if val > current.val -> go right 
        current=root
        while current:
            if val < current.val:
                current=current.left
            elif val > current.val:
                current=current.right
            else:
                # found the node with target value 
                return current 
        # If the loop finished nothing's been found 
        return None
