# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.path_p=[]
        self.path_q=[]

        def search(node, current_path):
            if not node:
                return 
            # 1. Add the current node to the path
            current_path.append(node) # p and q are nodes themselves, and we're not finding the node.val but the actual LCA node 

            # 2. If we find p or q, take a snapshot (a copy) of the path
            if node==p:
                self.path_p=current_path.copy()
            if node==q:
                self.path_q=current_path.copy()
            
            # 3. Explore children
            search(node.left,current_path)
            search(node.right,current_path)

            # 4. Backtrack: Remove the current node from the path before returning
            current_path.pop()

        # Start the traversal
        search(root,[])

        # make it into set for efficient look up 
        ancestor_p=set(self.path_p)

        lca=None
        # Iterate backwards through q's path. The first node we find that is also in p's path must be the deepest (lowest) one.
        # forward search also work though (remove reversed() and break)
        for node in reversed(self.path_q):
            if node in ancestor_p:
                lca=node
                break
    
        return lca 
