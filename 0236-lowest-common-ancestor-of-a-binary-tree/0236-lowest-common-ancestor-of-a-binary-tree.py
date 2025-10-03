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
        def search(node, current_path=[]):
            if not node:
                return 
            current_path.append(node)
            if node==p:
                self.path_p=current_path.copy()
            if node==q:
                self.path_q=current_path.copy()
            search(node.left,current_path)
            search(node.right,current_path)
            current_path.pop()
        search(root,[])
        # print(f'p path{self.path_p}')
        # print(f'q path {self.path_q}')

        pnode=set(self.path_p)
        lca=None
        for node in reversed(self.path_q):
            if node in pnode:
              lca=node  
              break
        return lca