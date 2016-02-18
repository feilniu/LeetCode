class Solution(object):
    def findKth(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int], len(nums1) <= len(nums2)
        :type k: int, k >= len(nums1)
        :rtype: int
        """
        len1 = len(nums1)
        len2 = len(nums2)
        if len1 > len2:
            return self.findKth(nums2, nums1, k)
        if len1 == 0:
            return nums2[k - 1]
        # choose x from nums1, k - x from nums2
        lower = 0 if k <= len2 else k - len2
        upper = len1 + 1
        while lower < upper:
            middle = (lower + upper) // 2
            if middle == 0:
                if nums1[middle] >= nums2[k - middle - 1]:
                    lower = middle
                    break
                else:
                    lower = middle + 1
            elif middle == len1:
                if k - middle == len2 or nums1[middle - 1] <= nums2[k - middle]:
                    lower = middle
                    break
                else:
                    upper = middle
            elif nums1[middle] < nums2[k - middle - 1]:
                lower = middle + 1
            elif k - middle == len2 or nums1[middle - 1] > nums2[k - middle]:
                upper = middle
            else:
                lower = middle
                break
        if lower == 0:
            return nums2[k - 1]
        if lower == k:
            return nums1[k - 1]
        return max(nums1[lower - 1], nums2[k - lower - 1])
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)
        length = len(nums1) + len(nums2)
        if length % 2 == 1:
            return self.findKth(nums1, nums2, length // 2 + 1)
        return (self.findKth(nums1, nums2, length // 2) + self.findKth(nums1, nums2, length // 2 + 1)) / 2.0

    def findMedianSortedArrays_slow(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums_all = nums1 + nums2
        nums_all.sort()
        length = len(nums_all)
        if length == 0:
            return None
        if length % 2 == 1:
            return nums_all[length // 2]
        return (nums_all[length // 2] + nums_all[length // 2 - 1]) / 2.0


testCases = [
        [[1], [], 1],
        [[], [2], 2],
        [[1], [2], 1.5],
        [[1,2,3], [], 2],
        [[], [1,2], 1.5],
        [[], [2,3], 2.5],
        [[1,2,3,4], [2,5], 2.5],
        [[1,2,3,4], [2,5,6], 3],
        [[1,2,2,6,8], [2,2,5], 2],
        [[1,2,3,4,9], [7,8,9,10], 7],
        [[1,2,3,4], [6,7,8,9], 5],
        [[1,1], [1,1], 1]
        ]
s = Solution()
for tc in testCases:
    result = s.findMedianSortedArrays(tc[0], tc[1])
    passed = abs(result - tc[2]) < 0.000001
    if not passed:
        print(tc, result, passed)

