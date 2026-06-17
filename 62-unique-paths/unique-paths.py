class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        row = [1] * n
    
        for i in range(1, m):
            new_row = [1] * n
            for j in range(1, n):
                new_row[j] = new_row[j-1] + row[j]
            row = new_row
        
        return row[n-1]