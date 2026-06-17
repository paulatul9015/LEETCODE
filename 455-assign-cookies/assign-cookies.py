class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
       # Step 1: Sort both arrays to align smallest needs with smallest assets
        g.sort()
        s.sort()
        
        child_ptr = 0
        cookie_ptr = 0
        
        # Step 2: Iterate through both arrays simultaneously using two pointers
        while child_ptr < len(g) and cookie_ptr < len(s):
            # If the cookie size satisfies the child's greed requirement
            if s[cookie_ptr] >= g[child_ptr]:
                # The child is satisfied, move to the next child
                child_ptr += 1
                
            
            # Greedily move to the next cookie in all cases
            cookie_ptr += 1
            
        # The number of children advanced matches the total satisfied count
        return child_ptr 