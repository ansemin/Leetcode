# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[float]
        """

        if not root:
            return []

        averages=[]
        queue=[root]

        while queue:
            level_sum=0
            level_count=len(queue)

            for _ in range(level_count):
                current=queue.pop(0)
                level_sum+=current.val

                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
            average=level_sum/float(level_count)

            averages.append(average)

        return averages