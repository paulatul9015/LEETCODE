class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # 1. Count frequencies
        count = {}
        for n in nums:
            count[n] = 1 + count.get(n, 0)
            
        # 2. Bucket Sort: Index is the frequency, value is list of numbers
        # bucket[i] stores all numbers that appear exactly 'i' times
        buckets = [[] for _ in range(len(nums) + 1)]
        for n, c in count.items():
            buckets[c].append(n)
            
        # 3. Collect the top k results from right to left
        result = []
        for i in range(len(buckets) - 1, 0, -1):
            for n in buckets[i]:
                result.append(n)
                if len(result) == k:
                    return result