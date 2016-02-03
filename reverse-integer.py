class Solution(object):
    def reverse1(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign, val = 1 if x >= 0 else -1, abs(x)
        rev = int(str(val)[::-1]) * sign
        return rev if -2147483648 <= rev <= 2147483647 else 0

    def reverse2(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign, val = 1 if x >= 0 else -1, abs(x)
        rev = 0
        while val > 0:
            val, digit = divmod(val, 10)
            rev = rev * 10 + digit
        rev *= sign
        return rev if -2147483648 <= rev <= 2147483647 else 0

    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign = 1 if x >= 0 else -1
        base = 10 * sign
        rev = 0
        while x != 0:
            x, digit = divmod(x, base)
            x *= sign
            rev = rev * 10 + digit
        return rev if -2147483648 <= rev <= 2147483647 else 0

testCases = [
        [0, 0],
        [123, 321],
        [-123, -321],
        [1, 1],
        [-1, -1],
        [10, 1],
        [-100, -1],
        [10001, 10001],
        [1000000022, 0],
        [-1000000512, 0]
        ]
s = Solution()
for tc in testCases:
    result = s.reverse(*tc[:-1])
    passed = result == tc[-1]
    if not passed:
        print(tc, result, passed)

