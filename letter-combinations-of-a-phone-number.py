class Solution(object):
    Mapping = {
            '2' : 'abc',
            '3' : 'def',
            '4' : 'ghi',
            '5' : 'jkl',
            '6' : 'mno',
            '7' : 'pqrs',
            '8' : 'tuv',
            '9' : 'wxyz',
            '0' : ' '}
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        result = []
        length = len(digits)
        if length > 0:
            d = digits[0]
            if d in Solution.Mapping:
                result = list(Solution.Mapping[d])
            for i in range(1, length):
                d = digits[i]
                if d in Solution.Mapping:
                    temp = list(Solution.Mapping[d])
                    new_result = []
                    for x in result:
                        for y in temp:
                            new_result.append(x + y)
                    result = new_result
        return result


testCases = [
        ['23', ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]],
        ['', []],
        ['1', []],
        ['2', ['a','b','c']],
        ['203', ["a d", "a e", "a f", "b d", "b e", "b f", "c d", "c e", "c f"]]
        ]
s = Solution()
for tc in testCases:
    result = s.letterCombinations(*tc[:-1])
    passed = sorted(result) == sorted(tc[-1])
    if not passed:
        print(tc, result, passed)

