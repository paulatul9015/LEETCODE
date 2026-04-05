class Solution(object):
    def judgeCircle(self, moves):
        # A robot returns home if horizontal moves cancel out 
        # and vertical moves cancel out.
        return moves.count('U') == moves.count('D') and moves.count('L') == moves.count('R')