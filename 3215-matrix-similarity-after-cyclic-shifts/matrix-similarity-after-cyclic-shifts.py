class Solution(object):
    def areSimilar(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: bool
        """
        m = len(mat)
        n = len(mat[0])
        
        # A shift of k is equivalent to a shift of k % n
        k %= n
        
        # If k % n is 0, no change occurs, so it's always true
        if k == 0:
            return True
            
        for row in mat:
            for j in range(n):
                # Check if the current element matches the element 
                # k positions away (cyclically)
                if row[j] != row[(j + k) % n]:
                    return False
                    
        return True
        