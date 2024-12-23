class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        n=len(triangle)
        for i in range(n-2,-1,-1):
            # print('starting row {}: {}'.format(i, triangle[i]))
            for j in range(len(triangle[i])):
                triangle[i][j]+=min(triangle[i+1][j],triangle[i+1][j+1])
            # print(triangle[0][0])
        return triangle[0][0]