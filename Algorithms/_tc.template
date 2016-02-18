testCases = [
        ]
passedCount = 0
s = Solution()
for tc in testCases:
    result = s.testMethod(*tc[:-1])
    passed = result == tc[-1]
    if passed:
        passedCount += 1
    else:
        print(tc, result, passed)
print('{}/{} test cases passed.'.format(passedCount, len(testCases)))

