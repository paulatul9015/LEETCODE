class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        res = 0
        curSum = 0
        prefix = {0 : 1}
        for n in nums:
            curSum += n
            dif = curSum - k 
            

            res += prefix.get(dif,0)
            prefix[curSum] = 1 + prefix.get(curSum,0)
        

        return res