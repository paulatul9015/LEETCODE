class Solution(object):
    def maxFrequency(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        left = 0
        total = 0
        max_freq = 0
        
        for right in range(len(nums)):
            total += nums[right]
            
            # Current window length: (right - left + 1)
            # Target value for all elements in window: nums[right]
            # While the needed operations exceed k, shrink the window
            while nums[right] * (right - left + 1) - total > k:
                total -= nums[left]
                left += 1
            
            # Update the maximum frequency found so far
            max_freq = max(max_freq, right - left + 1)
            
        return max_freq