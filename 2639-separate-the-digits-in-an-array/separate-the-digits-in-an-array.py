class Solution(object):
    def separateDigits(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        ans = []
        for n in nums :
            for digit in str(n):
                # Convert back to integer and add to result
                ans.append(int(digit))
        return ans