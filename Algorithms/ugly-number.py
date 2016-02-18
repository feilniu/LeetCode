class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:
            return False
        if num <= 6:
            return True
        for factor in (2, 3, 5):
            while num % factor == 0:
                num //= factor
        return num == 1

testCases = [
        [6, True],
        [7, False],
        [8, True],
        [11, False],
        [14, False]
        ]
s = Solution()
for tc in testCases:
    result = s.isUgly(tc[0])
    if result != tc[1]:
        print(tc[0], result, result == tc[1])

