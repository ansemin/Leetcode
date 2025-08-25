class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        left=0
        right=len(nums)-1
        count=0

        while left<right:
            c_sum=nums[left]+nums[right]
            if c_sum==k:
                left+=1
                right-=1
                count+=1
            elif c_sum>k:
                right-=1
            else:
                left+=1
        return count
