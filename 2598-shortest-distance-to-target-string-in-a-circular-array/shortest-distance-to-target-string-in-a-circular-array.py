class Solution(object):
    def closestTarget(self, words, target, startIndex):
        n = len(words)
        min_dist = float('inf')
        
        for i in range(n):
            if words[i] == target:
                # Calculate absolute distance between current index and start
                d = abs(i - startIndex)
                
                # The distance can be direct (d) or circular (n - d)
                # Take the minimum of the two, then update global min_dist
                min_dist = min(min_dist, d, n - d)
        
        # If min_dist is still infinity, target was never found
        return min_dist if min_dist != float('inf') else -1