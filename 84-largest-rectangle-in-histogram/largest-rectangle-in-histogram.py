class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        max_Area = 0
        stack = []
        for i ,h in enumerate(heights):
            start = i 
            while stack and stack[-1][1] > h:
                index , height = stack.pop()
                max_Area= max(max_Area , height * (i-index))
                start = index
            stack.append((start,h))
        for i , h in stack:
            max_Area = max(max_Area,h*(len(heights) - i))
        return max_Area

