class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        start = 0
        substringchar = {}
        for i in range(len(s)):
            if s[i] in substringchar and start <= substringchar[s[i]]:
                start = substringchar[s[i]] + 1
            else:
                if i - start + 1 > result:
                    result = i - start + 1
            substringchar[s[i]] = i
        return result


testCases = [
        ['', 0],
        ['a', 1],
        ['ab', 2],
        ['abcdefghijklmnopqrstuvwxyz', 26],
        ['abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz', 26],
        ['abcabcbb', 3],
        ['abcad', 4],
        ['abcc', 3],
        ['abbcbca', 3],
        ['bbbbb', 1],
        ['abcdbcdcdd', 4],
        ['aababcabcdabcdebcdecdedee', 5]
        ]
s = Solution()
for tc in testCases:
    result = s.lengthOfLongestSubstring(tc[0])
    passed = result == tc[1]
    if not passed:
        print(tc, result, passed)

