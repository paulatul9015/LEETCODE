class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height:
            return 0
            
        n = len(height)
        # 1. Initialize lists with zeros
        lmax = [0] * n
        rmax = [0] * n
        
        # 2. Fill lmax (Max height to the left of i, including i)
        lmax[0] = height[0]
        for i in range(1, n):
            lmax[i] = max(lmax[i-1], height[i])
            
        # 3. Fill rmax (Max height to the right of i, including i)
        rmax[n-1] = height[n-1]
        for i in range(n-2, -1, -1):
            rmax[i] = max(rmax[i+1], height[i])
            
        # 4. Calculate total water
        ans = 0
        for i in range(n):
            # Water at index i is min(left_wall, right_wall) - height[i]
            ans += min(lmax[i], rmax[i]) - height[i]
            
        return ans