class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        length = len(citations)
        lower, upper = 0, length
        count = 0
        while lower < upper:
            index = (upper - lower) // 2 + lower
            count = length - index
            value = citations[index]
            if value == count:
                break
            elif value > count:
                upper = index
            else:
                lower = index + 1
                count -= 1
        return count


testCases = [
        [3, 0, 6, 1, 5],
        [],
        [0],
        [1],
        [2],
        [1, 1],
        [2, 2],
        [2, 2, 2],
        [0, 1, 2],
        [9, 5, 7, 8],
        [9, 9, 5, 4, 4]
        ]
s = Solution()
for tc in testCases:
    tc.sort()
    print(tc, s.hIndex(tc))

