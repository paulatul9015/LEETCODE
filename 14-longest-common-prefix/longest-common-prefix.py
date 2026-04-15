class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        
        # Start by assuming the first word is the common prefix
        prefix = strs[0]
        
        # Compare the prefix with every other string in the list
        for i in range(1, len(strs)):
            # find() returns 0 if the prefix is at the very start
            while strs[i].find(prefix) != 0:
                # Shorten the prefix by one character from the end
                prefix = prefix[:-1]
                
                # If no prefix remains, there is no common prefix
                if not prefix:
                    return ""
                    
        return prefix