class Solution(object):
    def maxJumps(self, arr, d):
        """
        :type arr: List[int]
        :type d: int
        :rtype: int
        """
        n = len(arr)
        dp = [0] * n  # Memoization table to store max jumps from each index
        
        def dfs(i):
            # If already computed, return the memoized result
            if dp[i] != 0:
                return dp[i]
            
            res = 1  # Base case: we visit at least the current index
            
            # Jump Right
            for j in range(i + 1, min(i + d + 1, n)):
                if arr[j] >= arr[i]:
                    break  # Blocked by an equal or taller element
                res = max(res, 1 + dfs(j))
                
            # Jump Left
            for j in range(i - 1, max(i - d - 1, -1), -1):
                if arr[j] >= arr[i]:
                    break  # Blocked by an equal or taller element
                res = max(res, 1 + dfs(j))
                
            dp[i] = res
            return res
            
        # Compute the max jumps starting from every possible index
        return max(dfs(i) for i in range(n))