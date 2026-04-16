import bisect
from collections import defaultdict

class Solution(object):
    def solveQueries(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        # Step 1: Group all indices by their value
        val_to_indices = defaultdict(list)
        for i, val in enumerate(nums):
            val_to_indices[val].append(i)
        
        answer = []
        
        # Step 2: Process each query
        for q_idx in queries:
            val = nums[q_idx]
            indices = val_to_indices[val]
            
            # If the list only contains the query index itself, no other exists
            if len(indices) == 1:
                answer.append(-1)
                continue
            
            # Find where q_idx is in the sorted list of indices for this value
            pos = bisect.bisect_left(indices, q_idx)
            
            # The closest neighbors in a circular array are the ones 
            # immediately to the left and right in the sorted list.
            # We use modulo to handle circular wrap-around (0 becomes last, last becomes 0).
            idx_left = indices[(pos - 1) % len(indices)]
            idx_right = indices[(pos + 1) % len(indices)]
            
            # Helper function for circular distance: min(|i-j|, n - |i-j|)
            def get_circ_dist(i, j):
                direct_dist = abs(i - j)
                return min(direct_dist, n - direct_dist)
            
            # Calculate distances to both potential closest neighbors
            res = min(get_circ_dist(q_idx, idx_left), get_circ_dist(q_idx, idx_right))
            answer.append(res)
            
        return answer