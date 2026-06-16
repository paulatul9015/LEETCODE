class Solution(object):
    def subarraySum(self, nums, k):

        result = 0
        curSum = 0
        prefix = {0 : 1}
        for n in nums:
            curSum += n
            diff = curSum - k 
            

            result += prefix.get(diff, 0)
            
            prefix[curSum] = 1 + prefix.get(curSum,0)
        

        return result