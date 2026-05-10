class Solution(object):
    def maximumJumps(self, nums, target):
        n = len(nums)
        # Initialize dp array with -1 (unreachable)
        dp = [-1] * n
        # Base case: 0 jumps to reach the start
        dp[0] = 0
        
        # Iterate through every possible destination index
        for j in range(1, n):
            # Check every possible starting index before j
            for i in range(j):
                # If i is reachable and the jump condition is met
                if dp[i] != -1 and abs(nums[j] - nums[i]) <= target:
                    dp[j] = max(dp[j], dp[i] + 1)
        
        return dp[n - 1]
