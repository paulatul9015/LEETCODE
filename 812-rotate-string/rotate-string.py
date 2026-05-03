class Solution(object):
    def rotateString(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        # Step 1: Check if lengths are equal
        if len(s) != len(goal):
            return False
        
        # Step 2: Check if goal is a substring of s + s
        return goal in (s + s)
        