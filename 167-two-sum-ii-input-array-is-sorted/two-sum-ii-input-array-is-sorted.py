class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Initialize two pointers: one at the start, one at the end
        left = 0
        right = len(numbers) - 1
        
        while left < right:
            current_sum = numbers[left] + numbers[right]
            
            if current_sum == target:
                # The problem is 1-indexed, so add 1 to both indices
                return [left + 1, right + 1]
            
            elif current_sum < target:
                # If the sum is too small, move the left pointer to the right
                left += 1
            else:
                # If the sum is too large, move the right pointer to the left
                right -= 1
        
        # Based on constraints, a solution is guaranteed to exist.
        return -1