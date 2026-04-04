class Solution(object):
    def decodeCiphertext(self, encodedText, rows):
        """
        :type encodedText: str
        :type rows: int
        :rtype: str
        """
        if not encodedText:
            return ""
        
        n = len(encodedText)
        cols = n // rows
        res = []
        for i in range(cols):
            r, c = 0, i
            while r < rows and c < cols:
                # Calculate the linear index in encodedText
                index = r * cols + c
                res.append(encodedText[index])
                # Increment both to move diagonally
                r += 1
                c += 1
        return "".join(res).rstrip()