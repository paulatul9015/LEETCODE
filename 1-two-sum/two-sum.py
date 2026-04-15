class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Dictionary to store seen numbers and their indices
        seen = {}
        
        for i, num in enumerate(nums):
            complement = target - num
            
            # If we've seen the complement before, return the indices
            if complement in seen:
                return [seen[complement], i]
            
            # Otherwise, add current number to the dictionary
            seen[num] = i
            
        return []