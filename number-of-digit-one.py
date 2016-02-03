class Solution(object):
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = 0
        i = 0
        num = n
        while n > 0:
            n, d = divmod(n, 10)
            if d > 0:
                prev = i * (10 ** (i - 1)) if i > 0 else 0
                if d == 1:
                    result += num % (10 ** i) + 1 + prev
                else:
                    result += 10 ** i + prev * d
            i += 1
        return result


testCases = [
        [-1, 0],
        [0, 0],
        [1, 1],
        [2, 1],
        [9, 1],
        [10, 2],
        [11, 4],
        [12, 5],
        [13, 6],
        [19, 12],
        [20, 12],
        [21, 13],
        [31, 14],
        [32, 14],
        [100, 21],
        [101, 23],
        [105, 27],
        [111, 36],
        [211, 144],
        [312, 165],
        [10105, 4133],
        [20105, 18027]
        ]
s = Solution()
for tc in testCases:
    result = s.countDigitOne(*tc[:-1])
    passed = result == tc[-1]
    if not passed:
        print(tc, result, passed)

