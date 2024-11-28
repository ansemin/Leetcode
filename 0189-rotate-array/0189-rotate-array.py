class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        k=k%len(nums) #[1,2,3,4,5,6,7] k=3
        nums.reverse() # [7,6,5,4,3,2,1]
        nums[:k]=reversed(nums[:k]) # [5,6,7,4,3,2,1]
        nums[k:]=reversed(nums[k:]) # [5,6,7,1,2,3,4]