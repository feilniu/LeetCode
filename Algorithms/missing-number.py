class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(range(len(nums) + 1)) - sum(nums)
    def missingNumber2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum_nums = 0
        sum_all = 0
        k = 0
        for i in nums:
            k += 1
            sum_all += k
            sum_nums += i
        return sum_all - sum_nums

testCases = [
        [[0, 1, 3], 2],
        [[1, 2, 0], 3],
        [[], 0],
        [[0], 1],
        [[1], 0],
        [[1, 2], 0],
        [[1, 3, 5, 4, 0], 2]
        ]
s = Solution()
for tc in testCases:
    result = s.missingNumber2(tc[0])
    if result != tc[1]:
        print(tc[0], result, result == tc[1])

