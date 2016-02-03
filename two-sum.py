class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        length = len(nums)
        if length >= 2:
            h = {}
            for i in range(length):
                if target - nums[i] in h:
                    return [h[target - nums[i]], i + 1]
                h[nums[i]] = i + 1
        return []

testCases = [
        [[2, 7, 11, 15], 9, [1, 2]],
        [[2, 7, 11, 15], 22, [2, 4]],
        [[1, 2], 2, []],
        [[1, 2], 3, [1, 2]],
        [[1, 2, 4, 8, 16, 32], 24, [4, 5]],
        [[0, 2, 4, 0], 0, [1, 4]]
        ]
s = Solution()
for tc in testCases:
    result = s.twoSum(tc[0], tc[1])
    passed = result == tc[2]
    if not passed:
        print(tc, result, passed)

