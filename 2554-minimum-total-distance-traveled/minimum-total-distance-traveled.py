class Solution(object):
    def minimumTotalDistance(self, robot, factory):
        # Sort positions to enable contiguous DP transitions
        robot.sort()
        factory.sort()
        
        n = len(robot)
        m = len(factory)
        
        # dp[i][j] represents min distance for first i robots using first j factories
        # Initialize with a very large value (float('inf'))
        dp = [[float('inf')] * (m + 1) for _ in range(n + 1)]
        
        # Base case: 0 robots always cost 0 distance
        for j in range(m + 1):
            dp[0][j] = 0
            
        for j in range(1, m + 1):
            f_pos, f_limit = factory[j-1]
            for i in range(n + 1):
                # Option 1: Don't use the current factory at all for any new robots
                dp[i][j] = dp[i][j-1]
                
                # Option 2: Use current factory j to repair 'k' robots
                current_dist = 0
                for k in range(1, min(i, f_limit) + 1):
                    # Robot indices are 0-based, so the k-th robot back is robot[i-k]
                    current_dist += abs(robot[i-k] - f_pos)
                    
                    if dp[i-k][j-1] != float('inf'):
                        dp[i][j] = min(dp[i][j], dp[i-k][j-1] + current_dist)
                        
        return dp[n][m]
        