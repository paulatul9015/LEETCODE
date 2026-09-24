class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum_indices = {0: -1}
        
        max_len = 0
        current_sum = 0
        
        for i, num in enumerate(nums):
            # Treat 1 as +1 and 0 as -1
            current_sum += 1 if num == 1 else -1
            
            # If current_sum was seen before, the subarray between sum_indices[current_sum] 
            # and i has an equal number of 0s and 1s
            if current_sum in sum_indices:
                max_len = max(max_len, i - sum_indices[current_sum])
            else:
                # Store only the first occurrence to maximize the subarray length
                sum_indices[current_sum] = i
                
        return max_len