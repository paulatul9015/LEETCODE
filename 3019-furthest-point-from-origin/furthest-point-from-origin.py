class Solution(object):
    def furthestDistanceFromOrigin(self, moves):
        """
        :type moves: str
        :rtype: int
        """
        # Count the occurrences of each move type
        count_L = moves.count('L')
        count_R = moves.count('R')
        count_underscore = moves.count('_')
        
        # The furthest distance is the absolute net fixed moves 
        # plus all the flexible wildcard moves.
        return abs(count_R - count_L) + count_underscore
        