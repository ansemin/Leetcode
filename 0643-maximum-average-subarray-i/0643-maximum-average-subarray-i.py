class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        window=sum(nums[:k]) 
        max_a=float(window)/k # initialization of the first window 
        for i in range(k, len(nums)):
            window = window+nums[i]-nums[i-k]
            max_a=max(max_a,float(window)/k)
        return max_a