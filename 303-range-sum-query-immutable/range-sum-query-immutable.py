class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        if not nums:
            self.prefix_sums = []
            return
        
        # Create a prefix sum array where each element at index i 
        # stores the sum of nums[0...i]
        self.prefix_sums = [0] * len(nums)
        self.prefix_sums[0] = nums[0]
        for i in range(1, len(nums)):
            self.prefix_sums[i] = self.prefix_sums[i-1] + nums[i]

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        # Formula: Sum(L, R) = Prefix[R] - Prefix[L-1]
        if left == 0:
            return self.prefix_sums[right]
        
        return self.prefix_sums[right] - self.prefix_sums[left - 1]