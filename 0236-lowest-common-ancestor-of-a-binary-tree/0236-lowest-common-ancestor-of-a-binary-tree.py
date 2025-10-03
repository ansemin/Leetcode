# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root==q or root==p:
            return root
        left_anc=self.lowestCommonAncestor(root.left,p,q)
        right_anc=self.lowestCommonAncestor(root.right,p,q)

        if left_anc and right_anc:
            return root
        return left_anc if left_anc else right_anc