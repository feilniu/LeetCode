class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        max_sliding_window = []
        if nums:
            if k == 1:
                return nums
            window_queue = nums[:k]
            max_sliding_window.append(max(window_queue))
            for i in range(k, len(nums)):
                del window_queue[0]
                window_queue.append(nums[i])
                max_sliding_window.append(max(window_queue))
        return max_sliding_window


testCases = [
        [[1,3,-1,-3,5,3,6,7], 2, [3,3,-1,5,5,6,7]],
        [[1,3,-1,-3,5,3,6,7], 3, [3,3,5,5,6,7]],
        [[1,3,-1,-3,5,3,6,7], 4, [3,5,5,6,7]],
        [[1,3,-1,-3,5,3,6,7], 5, [5,5,6,7]],
        [[1,3,-1,-3,5,3,6,7], 6, [5,6,7]],
        [[1,3,-1,-3,5,3,6,7], 7, [6,7]],
        [[1,3,-1,-3,5,3,6,7], 8, [7]],
        [[], 0, []],
        [[1], 1, [1]],
        [[1,3,2,4,5], 1, [1,3,2,4,5]],
        [[1,3,2,4,5], 2, [3,3,4,5]],
        [[1,1,5,5,6,6,5,4,4,3,3,2,2,1], 3, [5,5,6,6,6,6,5,4,4,3,3,2]]
        ]
s = Solution()
passed_count = 0
for tc in testCases:
    result = s.maxSlidingWindow(tc[0], tc[1])
    passed = result == tc[2]
    if passed:
        passed_count += 1
    else:
        print(tc, result, passed)
print('Passed: {}/{}'.format(passed_count, len(testCases)))

