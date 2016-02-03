class Solution(object):
    def minPatches1(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: int
        """
        patches, maxRange = 0, 0
        nums.append(n + 1)
        for i in nums:
            num = min(i, n + 1)
            while maxRange + 1 < num:
                maxRange += maxRange + 1
                patches += 1
            maxRange += num
        return patches
    def minPatches(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: int
        """
        patches, maxRange = 0, 0
        nums.append(n + 1)
        for num in nums:
            num = min(num, n + 1)
            while maxRange + 1 < num:
                maxRange += maxRange + 1
                patches += 1
            maxRange += num
            if maxRange >= n:
                break
        return patches


testCases = [
        [[], 0, 0],
        [[], 1, 1],
        [[], 2, 2],
        [[], 3, 2],
        [[], 4, 3],
        [[], 5, 3],
        [[], 6, 3],
        [[], 7, 3],
        [[], 8, 4],
        [[], 9, 4],
        [[], 10, 4],
        [[], 15, 4],
        [[], 16, 5],
        [[1], 1, 0],
        [[1, 1, 1], 3, 0],
        [[1, 1, 1], 4, 1],
        [[1, 1, 1], 5, 1],
        [[1, 1, 1], 6, 1],
        [[1, 1, 1], 7, 1],
        [[1, 1, 1], 8, 2],
        [[1, 1, 1], 9, 2],
        [[1, 1, 1], 10, 2],
        [[1, 1, 1], 11, 2],
        [[1, 1, 1], 15, 2],
        [[1, 1, 1], 16, 3],
        [[1, 1, 1], 31, 3],
        [[1, 3], 6, 1],
        [[1, 5, 10], 20, 2],
        [[1, 2, 2], 5, 0],
        [[2, 2, 2], 2, 1],
        [[2, 2, 2], 7, 1],
        [[2, 2, 2], 8, 2],
        [[2, 2, 2], 15, 2],
        [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 10, 0],
        [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 18, 1],
        [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 34, 2],
        [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 20, 0],
        [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 55, 0],
        [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 87, 1],
        [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 151, 2],
        [[1, 1, 1, 3, 4, 6, 7, 8, 9, 10, 20], 63, 0],
        [[1, 1, 1, 3, 4, 6, 7, 8, 9, 10, 20], 70, 0],
        [[1, 1, 1, 3, 4, 6, 7, 8, 9, 10, 20], 71, 1],
        [[1, 1, 1, 3, 4, 6, 7, 8, 9, 10, 20], 127, 1],
        [[1, 1, 1, 1, 3, 3, 5, 50, 100], 15, 0],
        [[1, 1, 1, 1, 3, 3, 5, 50, 100], 16, 1],
        [[1, 1, 1, 1, 3, 3, 5, 50, 100], 31, 1],
        [[1, 1, 1, 1, 3, 3, 5, 50, 100], 49, 2],
        [[1, 1, 1, 1, 3, 3, 5, 50, 100], 213, 2],
        ]
passedCount = 0
s = Solution()
for tc in testCases:
    result = s.minPatches(*tc[:-1])
    passed = result == tc[-1]
    if passed:
        passedCount += 1
    else:
        print(tc, result, passed)
print('{}/{} test cases passed.'.format(passedCount, len(testCases)))

