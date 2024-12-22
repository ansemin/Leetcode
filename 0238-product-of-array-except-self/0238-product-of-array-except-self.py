class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        answer=[1]*len(nums) #initializing 
        #left
        prefix=1
        for i in range(len(nums)):
            answer[i]=prefix
            prefix*=nums[i]
            # print('step={}: prefix={}, answer={}'.format(i,prefix, answer))
        #right
        suffix=1
        for i in range(len(nums)-1,-1,-1):
            answer[i]*=suffix
            suffix*=nums[i]
            # print('Step{}: suffix={}, answer={}'.format(i,suffix,answer))

        return answer