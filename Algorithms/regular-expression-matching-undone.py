class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        s_length = len(s)
        p_length = len(p)
        pi = 0
        matches = [False] * (s_length + 1)
        matches[0] = True
        while pi < p_length:
            if pi + 1 < p_length and p[pi + 1] == '*':
                for i in range(s_length + 1):
                    if not matches[i] and i != 0 and matches[i - 1] and (s[i - 1] == p[pi] or p[pi] == '.'):
                        matches[i] = True
                pi += 2
            else:
                for i in range(s_length, -1, -1):
                    matches[i] = (i != 0 and matches[i - 1] and (s[i - 1] == p[pi] or p[pi] == '.'))
                pi += 1
        return matches[s_length]


testCases = [
        ["aa", "a", False],
        ["aa", "aa", True],
        ["aaa", "aa", False],
        ["aa", "a*", True],
        ["aa", ".*", True],
        ["ab", ".*", True],
        ["aab", "c*a*b", True],
        ['', 'a*', True],
        ['', '', True],
        ['a', 'a', True],
        ['b', 'a', False],
        ['a', '.', True],
        ['b', '.', True],
        ['ab', '.', False],
        ['a', 'a*', True],
        ['aaaaaa', 'a*', True],
        ['', '.*', True],
        ['abcdefg', '.*', True],
        ['ab', '..', True],
        ['acd', 'ab*c*d', True],
        ['az', 'a.*z', True],
        ['abcdefgz', 'a.*z', True],
        ['aa', 'a.*a', True],
        ['a', 'a.*a', False],
        ['aaaaba', 'a.*a', True],
        ['abcdefgh', 'abc*d.fg.*h', True],
        ['abdffggggghijklmnh', 'abc*d.fg.*h', True],
        ['abcccccdffggggghijklmnh', 'abc*d.fg.*h', True],
        ['abcccccdffggggghijklmn', 'abc*d.fg.*h', False],
        ['ahz', 'a.*h.*z', True],
        ['abcdefghijkmlnz', 'a.*h.*z', True],
        ['aaaaaahhhhhhz', 'a.*h.*z', True],
        ["caaabbacbabccabaacb", "a*b*.*c*c*.*b*abbc", False]
        ]
s = Solution()
for tc in testCases:
    result = s.isMatch(*tc[:-1])
    passed = result == tc[-1]
    if not passed:
        print(tc, result, passed)

