import bisect

class Solution(object):
    def maxDistance(self, side, points, k):
        # 1. Map 2D to 1D (Perimeter)
        # Sequence: (0,0)->(side,0)->(side,side)->(0,side)
        arr = []
        for x, y in points:
            if y == 0:   p = x
            elif x == side: p = side + y
            elif y == side: p = 2 * side + (side - x)
            else:           p = 3 * side + (side - y)
            arr.append(p)
        
        arr.sort()
        n = len(arr)
        perimeter = 4 * side
        
        # Helper to get Manhattan distance between two 1D perimeter points
        def get_dist(p1, p2):
            def coords(p):
                p %= perimeter
                if p <= side: return p, 0
                if p <= 2 * side: return side, p - side
                if p <= 3 * side: return 3 * side - p, side
                return 0, 4 * side - p
            x1, y1 = coords(p1)
            x2, y2 = coords(p2)
            return abs(x1 - x2) + abs(y1 - y2)

        def check(mid):
            # We only need to try starting points within the first possible gap.
            # If we can't find a solution starting in the first 'mid' distance,
            # no solution exists because a point MUST fall in that range.
            for i in range(n):
                if arr[i] - arr[0] > mid: 
                    break
                
                count = 1
                curr_pos = arr[i]
                start_pos = arr[i]
                
                # Greedy pick the next k-1 points
                for _ in range(k - 1):
                    # Use binary search to find the first point at least 'mid' away 
                    # in terms of perimeter (as a lower bound)
                    idx = bisect.bisect_left(arr, curr_pos + mid)
                    
                    found = False
                    # Check points from idx onwards to satisfy Manhattan dist
                    for j in range(idx, n):
                        if get_dist(curr_pos, arr[j]) >= mid:
                            curr_pos = arr[j]
                            count += 1
                            found = True
                            break
                    if not found: break
                
                # Check if the last point and first point satisfy the distance
                if count == k and get_dist(curr_pos, start_pos) >= mid:
                    return True
            return False

        # Binary search for the maximum minimum distance
        low, high = 0, 2 * side
        ans = 0
        while low <= high:
            mid = (low + high) // 2
            if mid == 0: # Distance 0 is always possible
                ans = max(ans, mid)
                low = mid + 1
                continue
                
            if check(mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
        return ans