class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Track the top 3 maximums and top 2 minimums
        max1 = max2 = max3 = float('-inf')
        min1 = min2 = float('inf')

        for n in nums:
            # Update the 3 maximum values
            if n > max1:
                max3 = max2
                max2 = max1
                max1 = n
            elif n > max2:
                max3 = max2
                max2 = n
            elif n > max3:
                max3 = n

            # Update the 2 minimum values
            if n < min1:
                min2 = min1
                min1 = n
            elif n < min2:
                min2 = n

        # Compare: 3 largest vs. 2 smallest (negative) * 1 largest
        return max(max1 * max2 * max3, min1 * min2 * max1)