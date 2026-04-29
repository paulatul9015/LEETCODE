class Solution(object):
    def maximumScore(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        # Precompute column prefix sums for O(1) range queries [cite: 15, 81]
        pref = [[0] * (n + 1) for _ in range(n)]
        for j in range(n):
            for i in range(n):
                pref[j][i + 1] = pref[j][i] + grid[i][j]

        # dp[col][prev_h][is_greater]
        # Using a 3D array for faster access than a dictionary 
        dp = [[[-1] * 2 for _ in range(n + 1)] for _ in range(n + 1)]

        def solve(col, prev_h, is_greater):
            if col == n:
                return 0
            
            # Check memoization table [cite: 28, 83]
            if dp[col][prev_h][is_greater] != -1:
                return dp[col][prev_h][is_greater]

            max_score = 0
            # Try every possible height h for the current column [cite: 20, 39]
            for h in range(n + 1):
                current_score = 0
                next_is_greater = False
                
                if is_greater == 1: # Decreasing trend
                    if h < prev_h:
                        # Current col is white, adjacent to taller previous black column [cite: 22, 52]
                        current_score = pref[col][prev_h] - pref[col][h]
                        next_is_greater = True
                    # Transition to next column
                    res = current_score + solve(col + 1, h, 1 if next_is_greater else 0)
                else: # Increasing trend
                    if h > prev_h:
                        if col > 0:
                            # Previous col was white, adjacent to taller current black column [cite: 21, 53]
                            current_score = pref[col - 1][h] - pref[col - 1][prev_h]
                    
                    # We can transition to either trend from an increasing state 
                    res = current_score + max(solve(col + 1, h, 0), solve(col + 1, h, 1))

                if res > max_score:
                    max_score = res

            dp[col][prev_h][is_greater] = max_score
            return max_score

        return solve(0, 0, 0)