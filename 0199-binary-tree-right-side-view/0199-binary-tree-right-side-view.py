# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        que=deque([root])
        result=[]
        while que:
            level=len(que)
            for i in range(level):
                cl=que.popleft()
                if i==level-1:
                    result.append(cl.val)
                if cl.left:
                    que.append(cl.left)
                if cl.right:
                    que.append(cl.right)
        return result 