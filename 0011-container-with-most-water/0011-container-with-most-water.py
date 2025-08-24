class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left=0
        right=len(height)-1
        x=right-left 
        output=[]
        while x>0:
            if height[left]>height[right]:
                area=x*height[right]
                output.append(area)
                right-=1
            elif height[left]<=height[right]:
                area=x*height[left]
                output.append(area)
                left+=1
            x=right-left 
        return max(output)

