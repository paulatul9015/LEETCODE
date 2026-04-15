class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # Dictionary to store the Next Greater Element for each number in nums2
        nge_map = {}
        stack = []

        # Step 1: Traverse nums2 to find NGE for all its elements
        for num in nums2:
            # While stack is not empty and current num is greater than stack top
            while stack and num > stack[-1]:
                # The current num is the Next Greater Element for the popped element
                popped_num = stack.pop()
                nge_map[popped_num] = num
            
            # Push current number onto stack
            stack.append(num)

        # Step 2: Build the result for nums1 using the map
        # If a number wasn't in the map, it has no next greater element (-1)
        result = []
        for num in nums1:
            result.append(nge_map.get(num, -1))
            
        return result
        