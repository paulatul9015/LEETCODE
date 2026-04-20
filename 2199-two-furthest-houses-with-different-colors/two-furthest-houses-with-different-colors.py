class Solution(object):
    def maxDistance(self, colors):
        """
        :type colors: List[int]
        :rtype: int
        """
        n = len(colors)
        max_dist = 0
        
        # Scenario 1: Compare the first house with others starting from the end
        for j in range(n - 1, 0, -1):
            if colors[0] != colors[j]:
                max_dist = max(max_dist, j)
                break
                
        # Scenario 2: Compare the last house with others starting from the beginning
        for i in range(n - 1):
            if colors[n - 1] != colors[i]:
                max_dist = max(max_dist, (n - 1) - i)
                break
                
        return max_dist