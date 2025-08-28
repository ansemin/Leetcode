class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        original= [0]+nums+[0]
        print('orginal {}'.format(original))
        zeros=[i for i, num in enumerate(original) if num==0] # define the 
        print('zeros {}'.format(zeros))
        if len(zeros) <= k+2:
            return len(nums)
        current_value=0
        max_value=0
        for zp in range(len(zeros)-(k+1)):
            left_boundary=zeros[zp]
            right_boundary=zeros[zp+k+1]
            print('left boundary {}, right boundary {}'.format(left_boundary, right_boundary))
            current_value = right_boundary-left_boundary-1
            print('current value is {}'.format(current_value))
            if current_value>max_value:
                max_value=current_value
        print('final value {}'.format(max_value))
        return max_value 