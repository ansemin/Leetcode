# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # Base case: if the tree is empty 
        if not root:
            return None
        # 1. Searching the node
        if key<root.val:
            root.left=self.deleteNode(root.left,key)
        elif key>root.val:
            root.right=self.deleteNode(root.right,key)
        else:
            # 2. Found the nonde to delete 
            # Case 1: Node has 0 or 1 child
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            # Case 2: Node has two children 
            # Find the in-order sucessor (smallest in the right subtree)
            temp=root.right
            while temp.left:
                temp=temp.left
            # Copy the sucessor's value to this node 
            root.val=temp.val 
            # Recursively delete the sucessor from the right subtree
            root.right=self.deleteNode(root.right, root.val)
        return root