class Solution(object):
    def twoEditWords(self, queries, dictionary):
        """
        :type queries: List[str]
        :type dictionary: List[str]
        :rtype: List[str]
        """
        answer = []
        
        for q in queries:
            # Check this query against every word in the dictionary
            for d in dictionary:
                diffs = 0
                # Compare characters at each position
                for i in range(len(q)):
                    if q[i] != d[i]:
                        diffs += 1
                    
                    # Optimization: if we exceed 2 edits, this d won't work
                    if diffs > 2:
                        break
                
                # If we found a word with 2 or fewer edits, keep it and move to next query
                if diffs <= 2:
                    answer.append(q)
                    break
                    
        return answer