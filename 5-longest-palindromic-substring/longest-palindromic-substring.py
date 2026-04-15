class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ""
        resLen = 0  # Initialize the length tracker
        
        for i in range(len(s)):
            # --- ODD LENGTH ---
            # Center is at a single character (e.g., "aba")
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    res = s[l:r+1]
                    resLen = r - l + 1
                l -= 1
                r += 1
            
            # --- EVEN LENGTH ---
            # Center is between two characters (e.g., "abba")
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    res = s[l:r+1]
                    resLen = r - l + 1
                l -= 1
                r += 1
                
        return res  # Moved outside the for-loop