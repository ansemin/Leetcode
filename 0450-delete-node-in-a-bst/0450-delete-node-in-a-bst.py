# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        # Traversing
        if key<root.val:
            root.left=self.deleteNode(root.left,key)
        elif key>root.val:
            root.right=self.deleteNode(root.right,key)
        # found a match
        else:
            # Either has 1 or 0 node
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            # have two nodes 
            temp=root.right
            while temp.left:
                temp=temp.left
            # set this smallest value to the root value
            root.val=temp.val 
            # now delete the smallest node from the tree
            root.right=self.deleteNode(root.right,temp.val)
        return root