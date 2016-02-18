import collections

class Solution(object):
    def countRangeSum1(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        Result = 0
        if nums:
            length = len(nums)
            for i in range(length):
                for j in range(i, length):
                    if lower <= sum(nums[i:j+1]) <= upper:
                        Result += 1
        return Result
    def countRangeSum2(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        pass

testCases = [
        [[], 0, 0, 0],
        [[1], -1, 1, 1],
        [[2], -1, 1, 0],
        [[-2, 5, -1], -2, 2, 3],
        [[5,-23,-5,-1,-21,13,15,7,18,4,7,26,29,-7,-28,11,-20,-29,19,22,15,25,17,-13,11,-15,19,-8,3,12,-1,2,-1,-21,-10,-7,14,-12,-14,-8,-1,-30,19,-27,16,2,-15,23,6,14,23,2,-4,4,-9,-8,10,20,-29,29], -19, 10, 362],
        ]
passedCount = 0
s = Solution()
for tc in testCases:
    result = s.countRangeSum(*tc[:-1])
    passed = result == tc[-1]
    if passed:
        passedCount += 1
    else:
        print(tc, result, passed)
print('{}/{} test cases passed.'.format(passedCount, len(testCases)))

