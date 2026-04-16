class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Dictionary to store seen numbers and their indices
        hashmap = {}
        
        for i, num in enumerate(nums):
            complement = target - num
            
            # If we've seen the complement before, return the indices
            if complement in hashmap:
                return [hashmap[complement], i]
            
            # Otherwise, add current number to the dictionary
            hashmap[num] = i
            
        return []