import math

class Solution(object):
    def numSquares_DP(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 4:
            return n
        counts = list(range(n + 1))
        for i in range(n):
            j = 1
            while True:
                temp = i + j * j
                if temp > n:
                    break
                if counts[temp] > counts[i] + 1:
                    counts[temp] = counts[i] + 1
                j += 1
        return counts[n]
    def numSquares_Math(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 4:
            return n
        sqrt_n = int(math.sqrt(n))
        if n == sqrt_n ** 2:
            return 1
        while n % 4 == 0:
            n //= 4
        if n % 8 == 7:
            return 4
        sqrt_n = int(math.sqrt(n))
        for i in range(1, sqrt_n + 1):
            nii = n - i ** 2
            sqrt_nii = int(math.sqrt(nii))
            if nii == sqrt_nii ** 2:
                return 2
        return 3


# 1 4 9 16 25 36 49 64 81 100 ...
testCases = [
        [0, 0], # 0
        [1, 1], # 1
        [2, 2], # 2
        [3, 3], # 3
        [4, 1], # 10
        [5, 2], # 11
        [6, 3], # 12
        [7, 4], # 13
        [8, 2], # 20
        [9, 1], # 100
        [10, 2], # 101
        [11, 3], # 102
        [12, 3], # 30
        [13, 2], # 110
        [14, 3], # 111
        [15, 4], # 112
        [16, 1], # 1000
        [17, 2], # 1001
        [18, 2], # 200
        [19, 3], # 201
        [20, 2], # 1010
        [21, 3], # 1011
        [22, 3], # 210
        [23, 4], # 211
        [24, 3], # 1020
        [25, 1], # 10000
        [35, 3], # 10101
        [36, 1], # 100000
        [43, 3], # 10200
        [45, 2], # 100010
        [46, 3], # 100011
        [47, 4], # 100012
        [48, 3], # 3000
        [49, 1], # 1000000
        [50, 2]  # 1000001
        ]
s = Solution()
for tc in testCases:
    result = s.numSquares_Math(tc[0])
    if result != tc[1]:
        print(tc[0], result, result == tc[1])

