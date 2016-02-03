class Solution(object):
    def longestPalindrome1(self, s):
        """
        :type s: str
        :rtype: str
        """
        s_length = len(s)
        if s_length < 2:
            return s
        result_start, result_length = 0, 1
        center1, center2 = 0, 1
        i = 1
        while i < s_length:
            start = center1 - (i - center2)
            if s[i] == s[start]:
                length = i - start + 1
                if length > result_length:
                    result_start, result_length = start, length
                if start > 0:
                    i += 1
                    continue
            if center1 < center2:
                center1 += 1
            elif s[center1] == s[center1 + 1]:
                center2 += 1
            else:
                center1 += 1
                center2 += 1
            if s_length * 2 - center1 - center2 - 1 <= result_length:
                break
            i = center2 + 1
        return s[result_start : result_start + result_length]

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        s_length = len(s)
        if s_length < 2:
            return s
        result_start, result_length = 0, 1
        for i in range(s_length - 1):
            i1, i2 = i, i
            while i1 >= 0 and i2 < s_length and s[i1] == s[i2]:
                i1 -= 1
                i2 += 1
            p_length = i2 - i1 - 1
            if result_length < p_length:
                result_start = i1 + 1
                result_length = p_length
            i1, i2 = i, i + 1
            while i1 >= 0 and i2 < s_length and s[i1] == s[i2]:
                i1 -= 1
                i2 += 1
            p_length = i2 - i1 - 1
            if result_length < p_length:
                result_start = i1 + 1
                result_length = p_length
        return s[result_start : result_start + result_length]


testCases = [
        ['', ''],
        ['a', 'a'],
        ['ab', 'a'],
        ['aa', 'aa'],
        ['aaa', 'aaa'],
        ['aaaa', 'aaaa'],
        ['aab', 'aa'],
        ['abab', 'aba'],
        ['abcb', 'bcb'],
        ['abcbc', 'bcb'],
        ['aaab', 'aaa'],
        ['aaaab', 'aaaa'],
        ['abbbbb', 'bbbbb'],
        ['abccbaab', 'abccba'],
        ['abccbaabcc', 'ccbaabcc'],
        ['abcdcbbcaca', 'bcdcb'],
        ['abbaa', 'abba'],
        ['abbaabbaa', 'abbaabba'],
        ['aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabcaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa', 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'],
        ['aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab', 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'],
        ['baaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab', 'baaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab']
        ]
s = Solution()
for tc in testCases:
    result = s.longestPalindrome(*tc[:-1])
    passed = result == tc[-1]
    if not passed:
        print(tc, result, passed)

