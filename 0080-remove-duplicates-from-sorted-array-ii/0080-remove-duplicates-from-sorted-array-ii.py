class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        write_index=1
        count=1
        # print(nums)

        for i in range(1, len(nums)):
            if nums[i]==nums[i-1]:
                count+=1
            else:
                count=1
            if count<=2:
                nums[write_index]=nums[i]
                write_index+=1
                print(nums[:write_index])
        return write_index 