class Solution:
    def productExceptSelf(self, nums):
        ans=[1]*len(nums)
        right=1
        for i in range(len(nums)-1,-1,-1):
            ans[i]=right
            right*=nums[i]# num[i]=4
            # print(f'Right : {right}')
        # print(f'Result: {ans}')
        left=1
        for i in range(len(nums)):
            ans[i]*=left
            left*=nums[i]
        return ans
            
