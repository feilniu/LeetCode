class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
        if n > 0:
            codes = [[0]]
            for i in range(1, n):
                new_codes = []
                for code in codes:
                    for j in range(code[-1], i + 1):
                        new_codes.append(code + [j])
                codes = new_codes
            for code in codes:
                parenthesis = []
                left, right = 0, 0
                for k in code:
                    while k > right:
                        parenthesis.append(')')
                        right += 1
                    parenthesis.append('(')
                    left += 1
                while left > right:
                    parenthesis.append(')')
                    right += 1
                result.append(''.join(parenthesis))
        return result


testCases = [
        [0, []],
        [1, ['()']],
        [2, ['(())','()()']],
        [3, ["((()))", "(()())", "(())()", "()(())", "()()()"]]
        ]
s = Solution()
for tc in testCases:
    result = s.generateParenthesis(*tc[:-1])
    passed = result == tc[-1]
    if not passed:
        print(tc, result, passed)

