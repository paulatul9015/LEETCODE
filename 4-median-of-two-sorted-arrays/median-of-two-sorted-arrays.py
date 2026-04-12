class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        # Always perform binary search on the smaller array for O(log(min(m,n)))
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
            
        m, n = len(nums1), len(nums2)
        low, high = 0, m
        half_len = (m + n + 1) // 2
        
        while low <= high:
            i = (low + high) // 2  # Partition index for nums1
            j = half_len - i       # Partition index for nums2
            
            # Boundary values
            # If i is 0, nothing on the left side of nums1; use -infinity
            # If i is m, nothing on the right side of nums1; use +infinity
            left1 = nums1[i-1] if i > 0 else float('-inf')
            right1 = nums1[i] if i < m else float('inf')
            
            left2 = nums2[j-1]   if j > 0 else float('-inf')
            right2 = nums2[j] if j < n else float('inf')
            
            # Check if partition is correct
            if left1 <= right2 and left2 <= right1:
                # Correct partition found
                if (m + n) % 2 == 1:
                    return float(max(left1, left2))
                else:
                    return (max(left1, left2) + min(right1, right2)) / 2.0
            
            elif left1 > right2:
                # We are too far right in nums1, move left
                high = i - 1
            else:
                # We are too far left in nums1, move right
                low = i + 1