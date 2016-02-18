class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows < 2:
            return s
        result = []
        s_length = len(s)
        step = numRows - 1
        for k in range(numRows):
            i = 0
            while True:
                pos = step * 2 * i + k
                if pos < s_length:
                    result.append(s[pos])
                    i += 1
                else:
                    break
                if k not in (0, step):
                    pos = step * 2 * i - k
                    if pos < s_length:
                        result.append(s[pos])
                    else:
                        break
        return ''.join(result)


testCases = [
        ['', 1, ''],
        ['', 2, ''],
        ['', 3, ''],
        ['a', 1, 'a'],
        ['a', 2, 'a'],
        ['a', 3, 'a'],
        ['ab', 1, 'ab'],
        ['ab', 2, 'ab'],
        ['ab', 3, 'ab'],
        ['abcdefghijklmnopqrstuvwxy', 1, 'abcdefghijklmnopqrstuvwxy'],
        ['abcdefghijklmnopqrstuvwxy', 2, 'acegikmoqsuwybdfhjlnprtvx'],
        ['abcdefghijklmnopqrstuvwxy', 3, 'aeimquybdfhjlnprtvxcgkosw'],
        ['abcdefghijklmnopqrstuvwxy', 4, 'agmsybfhlnrtxceikoquwdjpv'],
        ['PAYPALISHIRING', 3, 'PAHNAPLSIIGYIR'],
        ]
s = Solution()
for tc in testCases:
    result = s.convert(*tc[:-1])
    passed = result == tc[-1]
    if not passed:
        print(tc, result, passed)

