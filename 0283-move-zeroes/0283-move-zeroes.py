class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i=0
        j=0
        n=len(nums)
        while i+j < n:
            if abs(nums[i])>0:
                i+=1
            elif nums[i]==0:
                nums.pop(i)
                nums.append(0)
                j+=1
        # print(nums)
        return nums
