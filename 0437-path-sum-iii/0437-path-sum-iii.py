# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.path=0
        self.memory=defaultdict(int)
        self.memory[0]=1
        
        def dfs(node, cs):
            if not node:
                return 
            # print(f'nodevalue is {node.val}')
            cs+=node.val
            self.path+=self.memory[cs-targetSum]
            self.memory[cs]+=1
            # print(f' current sum is {cs}')
            # print(f'The memory is {self.memory}')
            if node.left:
                # print(f'Going into left Node of {node.left.val}')
                dfs(node.left,cs)
            if node.right:
                # print(f'Going into right Node of {node.right.val}')
                dfs(node.right, cs)
            self.memory[cs]-=1
            # print(f'path is {self.path}')
        dfs(root,0)
        return self.path 