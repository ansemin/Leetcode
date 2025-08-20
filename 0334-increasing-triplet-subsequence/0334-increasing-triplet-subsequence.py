class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # nums=[3,3,3,2,0,1,1]
        fn=sn=float('inf')
        for i in nums:
            if i<=fn:
                fn=i
            elif i<=sn:
                sn=i
            else:
                return True
        return False 
