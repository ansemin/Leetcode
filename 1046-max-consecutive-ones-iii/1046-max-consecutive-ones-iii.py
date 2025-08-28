# solution 1, solving in June's way
class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # Let's save the original length before padding
        original_length = len(nums)
        
        # Your padding and index finding logic
        nums = [0] + nums + [0]
        zero_indices = [i for i, num in enumerate(nums) if num == 0]

        # Handle the edge case: if we can flip all zeros
        # The number of real zeros is len(zero_indices) - 2
        if len(zero_indices) - 2 <= k:
            return original_length

        # Now, find the maximum length by iterating through the "sandwiches"
        max_length = 0
        # We loop up to the last possible starting point of a sandwich
        for i in range(len(zero_indices) - (k + 1)):
            # The left boundary of the sandwich
            left_boundary_idx = zero_indices[i]
            # The right boundary of the sandwich
            right_boundary_idx = zero_indices[i + k + 1]
            
            # Calculate the length between these boundaries
            current_length = right_boundary_idx - left_boundary_idx - 1
            
            # Update our max_length if this one is bigger
            if current_length > max_length:
                max_length = current_length
                
        return max_length
            

