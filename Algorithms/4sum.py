class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        length = len(nums)
        if length >= 4:
            nums.sort()
            a = 0
            while a + 3 < length:
                na = nums[a]
                if na * 4 > target:
                    break
                b = a + 1
                while b + 2 < length:
                    nb = nums[b]
                    if na + nb * 3 > target:
                        break
                    c, d = b + 1, length - 1
                    while c < d:
                        nc, nd = nums[c], nums[d]
                        sum4 = na + nb + nc + nd
                        if sum4 < target:
                            while nums[c] == nc and c < d:
                                c += 1
                        elif sum4 > target:
                            while nums[d] == nd and c < d:
                                d -= 1
                        else:
                            result.append([na, nb, nc, nd])
                            while nums[c] == nc and c < d:
                                c += 1
                            while nums[d] == nd and c < d:
                                d -= 1
                    while nums[b] == nb and b + 2 < length:
                        b += 1
                while nums[a] == na and a + 3 < length:
                    a += 1
        return result


testCases = [
        [[], 0, []],
        [[1,2,3,4], 0, []],
        [[1,2,3,4], 10, [[1,2,3,4]]],
        [[1,0,1,0,1,0,1,0], 0, [[0,0,0,0]]],
        [[1,0,1,0,1,0,1,0], 2, [[0,0,1,1]]],
        [[1,0,1,0,1,0,1,0], 4, [[1,1,1,1]]],
        [[1,0,-1,0,-2,2], 0, [[-1,0,0,1],[-2,-1,1,2],[-2,0,0,2]]],
        [[1,0,-1,0,-2,2], 1, [[-2,0,1,2],[-1,0,0,2]]],
        [[-3,-2,-1,0,0,1,2,3], 0, [[-3,-2,2,3],[-3,-1,1,3],[-3,0,0,3],[-3,0,1,2],[-2,-1,0,3],[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]],
        [[-5,-4,-3,-2,-1,0,0,1,2,3,4,5], 0, [[-5,-4,4,5],[-5,-3,3,5],[-5,-2,2,5],[-5,-2,3,4],[-5,-1,1,5],[-5,-1,2,4],[-5,0,0,5],[-5,0,1,4],[-5,0,2,3],[-4,-3,2,5],[-4,-3,3,4],[-4,-2,1,5],[-4,-2,2,4],[-4,-1,0,5],[-4,-1,1,4],[-4,-1,2,3],[-4,0,0,4],[-4,0,1,3],[-3,-2,0,5],[-3,-2,1,4],[-3,-2,2,3],[-3,-1,0,4],[-3,-1,1,3],[-3,0,0,3],[-3,0,1,2],[-2,-1,0,3],[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]]
        ]
s = Solution()
for tc in testCases:
    result = s.fourSum(*tc[:-1])
    passed = sorted(result) == sorted(tc[-1])
    if not passed:
        print(tc, result, passed)

