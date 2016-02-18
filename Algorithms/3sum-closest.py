class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        result = None
        length = len(nums)
        if length > 2:
            nums.sort()
            if target <= sum(nums[:3]):
                return sum(nums[:3])
            if target >= sum(nums[-3:]):
                return sum(nums[-3:])
            i, maxi = 0, length - 2
            while i < maxi:
                ni = nums[i]
                if result != None and ni - target > result:
                    break
                j, k = i + 1, length - 1
                while j < k:
                    nj = nums[j]
                    nk = nums[k]
                    sum3 = ni + nj + nk
                    diff = sum3 - target
                    if result == None or abs(diff) < abs(result - target):
                        result = sum3
                    if diff > 0:
                        while nums[k] == nk and j < k:
                            k -= 1
                    elif diff < 0:
                        while nums[j] == nj and j < k:
                            j += 1
                    else:
                        return result
                while nums[i] == ni and i < maxi:
                    i += 1
        return result


testCases = [
        [[-1,2,1,-4], 1, 2],
        [[-1,2,1,-4], 0, -1],
        [[-1,2,1,-4], -10, -4],
        [[-1,2,1,-4], 10, 2]
        ]
s = Solution()
for tc in testCases:
    result = s.threeSumClosest(*tc[:-1])
    passed = result == tc[-1]
    if not passed:
        print(tc, result, passed)

