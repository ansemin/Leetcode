class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        #10 = 2x5 -> 2! is a lot more common than 5! --> determining 0 will by the number of 5!
        count=0 
        while n>0:
            n//=5
            count+=n
            # print('n: {} total count {}'.format(n, count))
        return count