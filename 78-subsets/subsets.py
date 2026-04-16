class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        
        def backtrack(start, path):
            # Append a copy of the current path to result
            result.append(list(path))
            
            for i in range(start, len(nums)):
                # Include nums[i] in the subset
                path.append(nums[i])
                
                # Move onto the next element
                backtrack(i + 1, path)
                
                # Backtrack: Remove nums[i] to explore subsets without it
                path.pop()
        
        backtrack(0, [])
        return result