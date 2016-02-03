class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if not citations:
            return 0
        citations.sort(reverse = True)
        min_value = citations[0]
        count = 0
        length = len(citations)
        while min_value > count:
            count += 1
            if count == length:
                break
            if min_value > citations[count]:
                min_value = citations[count]
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
    print(tc, s.hIndex(tc))

