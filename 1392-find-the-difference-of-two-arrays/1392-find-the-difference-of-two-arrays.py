from collections import defaultdict
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums1_set=set(nums1)
        nums2_set=set(nums2)
        
        result=[[],[]]
        for num in nums1_set: 
            if not num in nums2_set:
                result[0].append(num)        
        for num in nums2_set:
            if not num in nums1_set:
                result[1].append(num)
        return result
