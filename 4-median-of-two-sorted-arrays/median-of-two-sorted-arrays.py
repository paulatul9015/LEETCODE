class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        A, B = nums1, nums2
        total = len(A) + len(B)
        half = (total + 1) // 2
        
        # Always binary search on the smaller array for O(log(min(m, n)))
        if len(B) < len(A):
            A, B = B, A
            
        l, r = 0, len(A)
        while l <= r:
            i = (l + r) // 2  # Partition for A
            j = half - i      # Partition for B
            
            # Boundary values (handling edge cases with infinity)
            Aleft = A[i - 1] if i > 0 else float("-infinity")
            Aright = A[i] if i < len(A) else float("infinity")
            Bleft = B[j - 1] if j > 0 else float("-infinity")
            Bright = B[j] if j < len(B) else float("infinity")
            
            # Valid partition found
            if Aleft <= Bright and Bleft <= Aright:
                # Odd total
                if total % 2:
                    return max(Aleft, Bleft)
                # Even total
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2.0
            
            elif Aleft > Bright:
                r = i - 1
            else:
                l = i + 1