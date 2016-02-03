class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lower = 0
        upper = len(nums) - 1
        while lower < upper:
            middle = lower + (upper - lower) // 2
            count = sum((1 for n in nums if n <= middle))
            if count <= middle:
                lower = middle + 1
            else:
                upper = middle
        return lower

testCases = [
        [[1,2,3,3,4], 3],
        [[1,3,5,7,2,4,6,8,9,5], 5],
        [[1,1], 1],
        [[2,2,2,2,2], 2],
        [[1,2,3,3,3], 3],
        [[1,4,3,3,3], 3],
        [[1,3,2,3,4,3,5], 3]
        ]
s = Solution()
for tc in testCases:
    result = s.findDuplicate(tc[0])
    passed = result == tc[1]
    if not passed:
        print(tc, result, passed)

