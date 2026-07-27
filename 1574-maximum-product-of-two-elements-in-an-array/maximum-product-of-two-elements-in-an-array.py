class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        maximum = 0

        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                calc = (nums[i] - 1) * (nums[j] - 1)
                if calc > maximum:
                    maximum = calc
        
        return maximum