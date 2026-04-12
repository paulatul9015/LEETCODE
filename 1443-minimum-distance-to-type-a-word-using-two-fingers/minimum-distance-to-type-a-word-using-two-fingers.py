class Solution(object):
    def minimumDistance(self, word):
        """
        :type word: str
        :rtype: int
        """
        def get_dist(char1, char2):
            if char1 is None or char2 is None:
                return 0
            # Convert characters to 0-25 range
            c1, c2 = ord(char1) - ord('A'), ord(char2) - ord('A')
            # Manhattan distance on a 6-column grid
            return abs(c1 // 6 - c2 // 6) + abs(c1 % 6 - c2 % 6)

        # dp[other_finger] stores the min distance. 
        # We use a dictionary to represent the position of the 'other' finger.
        # None represents the finger hasn't been placed yet (cost 0).
        dp = {None: 0}
        
        for i in range(len(word) - 1):
            curr_char = word[i]
            next_char = word[i+1]
            new_dp = {}
            
            for other_f, dist in dp.items():
                # Option 1: Move the finger that is currently at curr_char to next_char
                move_f1 = dist + get_dist(curr_char, next_char)
                if other_f not in new_dp or move_f1 < new_dp[other_f]:
                    new_dp[other_f] = move_f1
                
                # Option 2: Move the 'other' finger to next_char
                # The finger that was at curr_char now becomes the 'other' finger
                move_f2 = dist + get_dist(other_f, next_char)
                if curr_char not in new_dp or move_f2 < new_dp[curr_char]:
                    new_dp[curr_char] = move_f2
            
            dp = new_dp
            
        return min(dp.values())