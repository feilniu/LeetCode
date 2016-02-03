class Solution(object):
    MAX_INT = 0x7fffffff
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if divisor == 0:
            return self.MAX_INT
        if dividend == 0:
            return 0
        positive = (dividend > 0) == (divisor > 0)
        dividend = abs(dividend)
        divisor = abs(divisor)
        result = 0
        if divisor == 1:
            result = dividend
        elif divisor == 2:
            result = dividend >> 1
        else:
            while dividend >= divisor:
                x = divisor
                i = 1
                while dividend >= x + x:
                    x += x
                    i += i
                dividend -= x
                result += i
        if not positive:
            result = -result
        if result > self.MAX_INT:
            result = self.MAX_INT
        return result


testCases = [
        [0,1,0],
        [1,1,1],
        [2,1,2],
        [6,2,3],
        [7,2,3],
        [-6,2,-3],
        [6,-2,-3],
        [-6,-2,3],
        [2147483647,2,1073741823],
        [-2147483648,-1,2147483647]
        ]
s = Solution()
for tc in testCases:
    result = s.divide(*tc[:-1])
    passed = result == tc[-1]
    if not passed:
        print(tc, result, passed)

