class Solution(object):
    def getMinDistance(self, nums, target, start):
        """
        :type nums: List[int]
        :type target: int
        :type start: int
        :rtype: int
        """
        min_dist = float('inf')
        
        for i, num in enumerate(nums):
            if num == target:
                # Calculate the distance for the current index
                current_dist = abs(i - start)
                
                # Update min_dist if the current one is smaller
                if current_dist < min_dist:
                    min_dist = current_dist
                    
                # Optimization: if distance is 0, we can't do better
                if min_dist == 0:
                    return 0
                    
        return min_dist