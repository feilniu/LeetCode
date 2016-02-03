class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        if preorder:
            InputList = preorder.split(',')
            Stack = [] # number in stack means next expected value: 1:left 2:right 3:upper
            ch = InputList[0]
            if ch != '#':
                Stack.append(1)
            for ch in InputList[1:]:
                if not Stack:
                    return False
                Stack[-1] += 1
                if ch != '#':
                    Stack.append(1)
                else:
                    while Stack and Stack[-1] == 3:
                        Stack.pop()
            return Stack == []
        return False

testCases = [
        ["", False],
        ["#", True],
        ["1", False],
        ["1,#,#", True],
        ["9,3,4,#,#,1,#,#,2,#,6,#,#", True],
        ["1,#", False],
        ["#,1", False],
        ["9,#,#,1", False],
        ["9,3,4,#,#,#,#", True],
        ]
passedCount = 0
s = Solution()
for tc in testCases:
    result = s.isValidSerialization(*tc[:-1])
    passed = result == tc[-1]
    if passed:
        passedCount += 1
    else:
        print(tc, result, passed)
print('{}/{} test cases passed.'.format(passedCount, len(testCases)))

