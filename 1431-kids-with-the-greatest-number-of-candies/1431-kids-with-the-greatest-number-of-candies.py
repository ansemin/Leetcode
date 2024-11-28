class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]"""
        candymax=max(candies)
        result=[]
        for candy in candies:
            if candy + extraCandies >= candymax:
                result.append(True)
            else:
                result.append(False)
        return result