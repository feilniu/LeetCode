class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        j = 0
        length = len(nums)
        for i in range(length):
            if nums[i] != 0:
                if i > j:
                    nums[j] = nums[i]
                j += 1
        while j < length:
            nums[j] = 0
            j += 1

testCases = [
        [0, 1, 0, 3, 12],
        [0],
        [1],
        [1, 1],
        [0, 0]
        ]
s = Solution()
for tc in testCases:
    print('Input:', tc)
    s.moveZeroes(tc)
    print('Output:', tc)

