class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left=0
        right=len(height)-1
        max_area=0

        while left<right:
            current_height=min(height[left],height[right])
            current_width=right-left
            current_area=current_height*current_width
            # print('for height {} * width {} =area {}'.format(current_height, current_width, current_area))
            max_area=max(max_area, current_area)
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
            # print('left {}, right {}'.format(left, right))
            # print(max_area)
        return max_area