from LeetCodeLib.LinkedList import *

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        p1 = l1
        p2 = l2
        carry, value = divmod(p1.val + p2.val, 10)
        result = ListNode(value)
        p1 = p1.next
        p2 = p2.next
        pr = result
        while p1 and p2:
            carry, value = divmod(p1.val + p2.val + carry, 10)
            pr.next = ListNode(value)
            pr = pr.next
            p1 = p1.next
            p2 = p2.next
        while p1:
            carry, value = divmod(p1.val + carry, 10)
            pr.next = ListNode(value)
            pr = pr.next
            p1 = p1.next
        while p2:
            carry, value = divmod(p2.val + carry, 10)
            pr.next = ListNode(value)
            pr = pr.next
            p2 = p2.next
        if carry > 0:
            pr.next = ListNode(carry)
        return result

testCases = [
        [[1], [1], [2]],
        [[2,4,3], [5,6,4], [7,0,8]],
        [[9,9,9], [1], [0,0,0,1]],
        [[0,9,8], [2,2], [2,1,9]],
        [[0,1], [0], [0,1]]
        ]
s = Solution()
for tc in testCases:
    l1 = BuildLinkedList(tc[0])
    l2 = BuildLinkedList(tc[1])
    r = s.addTwoNumbers(l1, l2)
    result = LinkedListToList(r)
    passed = result == tc[2]
    if not passed:
        print(tc, result, passed)

