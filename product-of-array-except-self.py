import functools
import operator

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = [1]
        temp = 1
        for i in range(1, len(nums)):
            temp *= nums[i - 1]
            result.append(temp)
        temp = 1
        for i in range(len(nums) - 2, -1, -1):
            temp *= nums[i + 1]
            result[i] *= temp
        return result


testCases = [
        [[1,2,3,4], [24,12,8,6]],
        [[1,2], [2,1]],
        [[3,5,7], [35,21,15]]
        ]
s = Solution()
for tc in testCases:
    result = s.productExceptSelf(tc[0])
    passed = result == tc[1]
    if not passed:
        print(tc, result, passed)

