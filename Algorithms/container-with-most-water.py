class Solution(object):
    def maxArea1(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        length = len(height)
        max_area = 0
        for i in range(length - 1):
            for j in range(i, length):
                area = (j - i) * min(height[i], height[j])
                if area > max_area:
                    max_area = area
        return max_area

    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        lower, upper = 0, len(height) - 1
        max_area = 0
        while lower < upper:
            if height[lower] < height[upper]:
                area = (upper - lower) * height[lower]
                lower += 1
            else:
                area = (upper - lower) * height[upper]
                upper -= 1
            if area > max_area:
                max_area = area
        return max_area


testCases = [
        [[], 0],
        [[1], 0],
        [[1,0,0], 0],
        [[1,0,1,0,1], 4],
        [[1,2], 1],
        [[1,2,3], 2],
        [[1,2,3,4], 4],
        [[1,2,3,2,5,3], 9],
        [[3,0,5,3], 9],
        [[3,5,0,3], 9]
        ]
s = Solution()
for tc in testCases:
    result = s.maxArea(*tc[:-1])
    passed = result == tc[-1]
    if not passed:
        print(tc, result, passed)

