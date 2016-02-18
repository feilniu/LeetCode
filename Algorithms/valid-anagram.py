class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        Ls = [0] * 26
        Lt = [0] * 26
        for i in range(len(s)):
            Ls[ord(s[i]) - 97] += 1
            Lt[ord(t[i]) - 97] += 1
        return Ls == Lt


testCases = [
        ['anagram', 'nagaram', True],
        ['rat', 'car', False],
        ['', '', True],
        ['a', 'a', True],
        ['a', 'b', False],
        ['abc', 'bac', True],
        ['aab', 'bba', False]
        ]
s = Solution()
for tc in testCases:
    result = s.isAnagram(tc[0], tc[1])
    passed = result == tc[2]
    if not passed:
        print(tc, result, passed)

