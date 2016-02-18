from LeetCodeLib.LinkedList import *

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        return False

testCases = [
        [[], True],
        [[1], True],
        [[1,2], False],
        [[1,2,1], True],
        [[1,2,3,4,5,4,3,2,1], True],
        [[1,2,3,4,4,3,2,1], True]
        ]
s = Solution()
for tc in testCases:
    head = BuildLinkedList(tc[0])
    result = s.isPalindrome(head)
    passed = result == tc[1]
    if not passed:
        print(tc, result, passed)

