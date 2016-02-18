class Solution(object):
    UglyNumbers = [1]
    Factors = (2, 3, 5)
    LN = [0, 0, 0]
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 6:
            return n
        length = len(Solution.UglyNumbers)
        if n <= length:
            return Solution.UglyNumbers[n - 1]
        while n > length:
            un = list(Solution.Factors[i] * Solution.UglyNumbers[Solution.LN[i]] for i in range(3))
            umin = min(un)
            for i in range(3):
                if un[i] == umin:
                    Solution.LN[i] += 1
            Solution.UglyNumbers.append(umin)
            n -= 1
        return Solution.UglyNumbers[-1]


testCases = [
        [1, 1],
        [2, 2],
        [3, 3],
        [10, 12],
        [11, 15],
        [12, 16],
        [13, 18],
        [14, 20],
        [4, 4],
        [5, 5],
        [6, 6],
        [7, 8],
        [8, 9],
        [9, 10],
        [15, 24],
        [16, 25],
        [17, 27]
        ]
s = Solution()
for tc in testCases:
    result = s.nthUglyNumber(tc[0])
    if result != tc[1]:
        print(tc[0], result, result == tc[1])

