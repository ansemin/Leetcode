class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # nums: [1,2,3,4]
        ans=[1]*len(nums) #[1,1,1,1]
        right=1
        for i in range(len(nums)-1,-1,-1): #[3,-1,-1] stops at 0
            ans[i]=right # ans[-3]=1, ans[-2]=4, ans[-1]=12, ans[0]=24
            right=right*nums[i] #right update: 1*4=4, 4*3=12, 12*2=24
        # ans=[24,12,4,1]
        left=1
        for i in range(len(nums)):
            ans[i]*=left #ans[0]=1*24,ans[1]=12*1,ans[2]=2*4,ans[3]=1*6
            left*=nums[i] #1*1=1, 1*2=2, 2*3=6, 6*1=6
        # ans=[24,12,8,6]
        return ans


        