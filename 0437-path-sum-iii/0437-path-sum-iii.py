# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.paths=0 #counter of the total number of valid path 
        self.pathSums=defaultdict(int) # running sum we've seen so far
        self.pathSums[0]=1 # if we come across targetSum in the root, we count this 

        def dfs(r,currSum):
            # base condition
            if not r:
                return 
            currSum+=r.val #current running sum
            self.paths+=self.pathSums[currSum-targetSum] # all the valid path from previous 
            # if the key didn't exist, because we're using defaultdict, it would return 0 so it'd just be path+=0
            self.pathSums[currSum]+=1 # we've now  seen sum 
            #continuing the traversal
            if r.right:
                dfs(r.right,currSum)
            if r.left:
                dfs(r.left,currSum)
            # After we process both nodes, we subtract the count
            self.pathSums[currSum]-=1
        dfs(root,0)
        return self.paths