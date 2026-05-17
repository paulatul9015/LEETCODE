from collections import deque

class Solution(object):
    def canReach(self, arr, start):
        """
        :type arr: List[int]
        :type start: int
        :rtype: bool
        """
        n = len(arr)
        queue = deque([start])
        visited = [False] * n
        visited[start] = True
        
        while queue:
            curr = queue.popleft()
            
            # Base Case: Found the target value
            if arr[curr] == 0:
                return True
            
            # Explore the two possible jumps
            for next_idx in (curr + arr[curr], curr - arr[curr]):
                if 0 <= next_idx < n and not visited[next_idx]:
                    visited[next_idx] = True
                    queue.append(next_idx)
                    
        return False