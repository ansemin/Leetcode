class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count={}
        operations=0

        for num in nums:
            complement=k-num # nums =[1,2,3,4], num=1, complement=4
            if complement in count and count[complement]>0:
                operations+=1
                count[complement]-=1 #because the number can be only used once 
            else:
                count[num]=count.get(num,0)+1
            print('num: {}, complement: {}, count: {}, operation": {}'.format(num, complement, count, operations))
        return operations 