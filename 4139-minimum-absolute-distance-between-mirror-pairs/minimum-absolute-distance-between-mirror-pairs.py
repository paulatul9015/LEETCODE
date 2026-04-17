class Solution(object):
    def minMirrorPairDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def get_reverse(n):
            return int(str(n)[::-1])
        last_seen = {}
        min_dist = float('inf')
        
        for j in range(len(nums)):
            current_val = nums[j]
            
            target = current_val
            if target in last_seen:
                min_dist = min(min_dist, j - last_seen[target])
            reversed_val = get_reverse(current_val)
            last_seen[reversed_val] = j
            
        return min_dist if min_dist != float('inf') else -1
        