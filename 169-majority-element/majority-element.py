class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        candidate = None
        count = 0
    
        for num in nums:

            if count == 0:
                candidate = num
        
            if num == candidate:
                count = count + 1
            else:
                count = count - 1
            
        return candidate