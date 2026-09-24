
class Solution(object):
    def findMaxLength(self, nums):
        seen = {0: -1}
        max_len = count = 0
        
        for i, val in enumerate(nums):
            count += 1 if val else -1
            max_len = max(max_len, i - seen.setdefault(count, i))
            
        return max_len