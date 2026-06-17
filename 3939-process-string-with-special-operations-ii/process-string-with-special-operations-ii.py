class Solution(object):
    def processStr(self, s, k):
        n = len(s)
        length = [0] * (n + 1)

        # Compute lengths after each operation
        for i, ch in enumerate(s):
            if ch.isalpha():
                length[i + 1] = length[i] + 1
            elif ch == '*':
                length[i + 1] = max(0, length[i] - 1)
            elif ch == '#':
                length[i + 1] = length[i] * 2
            elif ch == '%':
                length[i + 1] = length[i]

        # If k is out of bounds
        if k >= length[n]:
            return '.'

        # Work backwards
        for i in range(n - 1, -1, -1):
            ch = s[i]

            if ch.isalpha():
                if k == length[i]:
                    return ch

            elif ch == '*':
                # deletion restores previous length
                pass

            elif ch == '#':
                k %= length[i]

            elif ch == '%':
                k = length[i] - 1 - k

        return '.'