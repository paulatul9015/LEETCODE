class Solution(object):
    def distance(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        res = [0] * n
        index_map = {}
        for i, val in enumerate(nums):
            if val not in index_map:
                index_map[val] = []
            index_map[val].append(i)
        for val in index_map:
            indices = index_map[val]
            k = len(indices)
            if k <= 1:
                continue
                
            total_sum = sum(indices)
            prefix_sum = 0
            
            for i, p_i in enumerate(indices):
                left_count = i
                left_sum = (left_count * p_i) - prefix_sum
                
                right_count = k - 1 - i
                right_sum = (total_sum - prefix_sum - p_i) - (right_count * p_i)
                
                res[p_i] = left_sum + right_sum
                prefix_sum += p_i
                
        return res