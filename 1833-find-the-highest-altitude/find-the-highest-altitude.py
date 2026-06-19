class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        
        currentAlt = 0
        maxAlt = 0 
        for g in gain :
            currentAlt += g

            maxAlt = max(maxAlt, currentAlt)
        return maxAlt

