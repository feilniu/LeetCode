import sys

TotalVersion = int(sys.argv[1])

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
BadVersion = 0
CallCount = 0
def isBadVersion(version):
    global BadVersion, CallCount
    CallCount += 1
    return version >= BadVersion

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if not isBadVersion(n):
            return None
        if n == 1:
            return 1
        lower, upper = 1, n
        while lower < upper:
            v = (upper - lower) // 2 + lower
            if isBadVersion(v):
                upper = v
            else:
                lower = v + 1
        return upper

s = Solution()
ccl = []
for BadVersion in range(1, TotalVersion + 1):
    CallCount = 0
    print(TotalVersion, BadVersion, s.firstBadVersion(TotalVersion), CallCount)
    ccl.append(CallCount)
print(sum(ccl) / len(ccl))
