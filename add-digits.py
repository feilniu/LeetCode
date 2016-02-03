class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num > 0:
            result = num % 9
            return 9 if result == 0 else result
        return 0

testCases = [
        [0, 0],
        [1, 1],
        [9, 9],
        [10, 1],
        [18, 9],
        [19, 1],
        [20, 2],
        [27, 9],
        [28, 1],
        [99, 9],
        [100, 1],
        [123, 6],
        [1000, 1],
        [1234, 1],
        [9999, 9]
        ]
s = Solution()
for tc in testCases:
    result = s.addDigits(tc[0])
    passed = result == tc[1]
    if not passed:
        print(tc, result, passed)
