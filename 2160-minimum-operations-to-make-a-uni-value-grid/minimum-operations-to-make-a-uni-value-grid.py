class Solution(object):
    def minOperations(self, grid, x):
        """
        :type grid: List[List[int]]
        :type x: int
        :rtype: int
        """
        # Flatten the grid into a single list
        nums = []
        for row in grid:
            nums.extend(row)
        
        # Sort to find the median
        nums.sort()
        
        n = len(nums)
        median = nums[n // 2]
        operations = 0
        
        # Check feasibility and calculate operations
        first_rem = nums[0] % x
        for num in nums:
            if num % x != first_rem:
                return -1
            # Calculate distance to median in steps of x
            operations += abs(num - median) // x
            
        return operations