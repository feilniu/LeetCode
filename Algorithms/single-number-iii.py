import operator
import functools

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        x = functools.reduce(operator.xor, nums)
        right_bit = x & -x
        ans = functools.reduce(operator.xor, (n for n in nums if n & right_bit))
        return [ans, ans ^ x]

testCases = [
        [[1, 2, 1, 3, 2, 5], [3, 5]],
        [[2, 3], [2, 3]],
        [[1, 2, 3, 4, 3, 2, 1, 0], [4, 0]],
        [[-1, -2, 1, 2, 0, -2, 1, 0], [-1, 2]]
        ]
s = Solution()
for tc in testCases:
    result = s.singleNumber(tc[0])
    passed = (result == tc[1] or result == tc[1][::-1])
    if not passed:
        print(tc[0], result, tc[1], passed)
