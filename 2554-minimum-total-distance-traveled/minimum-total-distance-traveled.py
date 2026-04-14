from collections import deque

class Solution(object):
    def minimumTotalDistance(self, robot, factory):
        robot.sort()
        factory.sort()
        
        n, m = len(robot), len(factory)
        # We use a 1D DP array to save space, representing dp[i] for the previous factory
        dp = [0] + [float('inf')] * n
        
        for pos, limit in factory:
            # cur_dp will store the results for the current factory
            cur_dp = dp[:]
            # dq stores pairs of (index, value)
            dq = deque([(0, 0)])
            
            prefix_sum = 0
            for i in range(1, n + 1):
                # Calculate the prefix distance sum for robots assigned to this factory
                prefix_sum += abs(robot[i-1] - pos)
                
                # Remove indices from deque that are outside the current factory's limit
                if dq[0][0] < i - limit:
                    dq.popleft()
                
                # The value we store in the deque is dp[i-k] - prefix_sum_of_k_robots
                # This allows us to find the min cost efficiently
                val = dp[i] - prefix_sum
                while dq and dq[-1][1] >= val:
                    dq.pop()
                dq.append((i, val))
                
                # The min distance for cur_dp[i] is the best value in our window + current prefix_sum
                cur_dp[i] = dq[0][1] + prefix_sum
            
            dp = cur_dp
            
        return dp[n]