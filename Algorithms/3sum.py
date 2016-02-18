class Solution(object):
    def threeSum1(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        results = []
        length = len(nums)
        if length > 2:
            for i in range(length - 2):
                h = {}
                for j in range(i + 1, length):
                    key = 0 - nums[i] - nums[j]
                    if key in h:
                        result = [nums[i], nums[j], nums[h[key]]]
                        result.sort()
                        if result not in results:
                            results.append(result)
                        del h[key]
                    h[nums[j]] = j
        return results

    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        results = []
        length = len(nums)
        if length > 2:
            nums.sort()
            i, maxi = 0, length - 2
            while i < maxi:
                ni = nums[i]
                if ni > 0:
                    break
                j, k = i + 1, length - 1
                while j < k:
                    nj = nums[j]
                    nk = nums[k]
                    sum3 = ni + nj + nk
                    if sum3 > 0:
                        while nums[k] == nk and j < k:
                            k -= 1
                    elif sum3 < 0:
                        while nums[j] == nj and j < k:
                            j += 1
                    else:
                        result = [ni, nj, nk]
                        results.append(result)
                        while nums[k] == nk and j < k:
                            k -= 1
                        while nums[j] == nj and j < k:
                            j += 1
                while nums[i] == ni and i < maxi:
                    i += 1
        return results


testCases = [
        [[], []],
        [[0, 0, 0, 0], [[0, 0, 0]]],
        [[-1, 0, 1, 2, -1, -4], [[-1, 0, 1],[-1, -1, 2]]],
        [[0, 0, 0, 1, -1], [[0, 0, 0],[-1, 0, 1]]],
        [[0, 0, 0, 1, 1, 1, -2, -3, 2, 3], [[0, 0, 0],[-2, 1, 1],[-2, 0, 2],[-3, 1, 2],[-3, 0, 3]]]
        ]
s = Solution()
for tc in testCases:
    result = s.threeSum(*tc[:-1])
    passed = (sorted(result) == sorted(tc[-1]))
    if not passed:
        print(tc, result, passed)

