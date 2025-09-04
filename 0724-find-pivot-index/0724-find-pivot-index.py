class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        leftsum=0
        rightsum=0
        total=sum(nums)
        for i in range(len(nums)):
            rightsum=total-(leftsum+nums[i])
            if leftsum==rightsum:
                return i
            leftsum+=nums[i]
        return -1