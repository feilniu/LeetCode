from LeetCodeLib.LinkedList import *

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head and head.next:
            p = head
            head = head.next
            p.next = head.next
            head.next = p
            while p.next and p.next.next:
                a, b = p.next, p.next.next
                p.next = b
                a.next = b.next
                b.next = a
                p = a
        return head


testCases = [
        [],
        [0],
        [0,1],
        [0,1,2],
        [0,1,2,3],
        [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
        ]
s = Solution()
for tc in testCases:
    print(tc)
    head = BuildLinkedList(tc)
    PrintLinkedList(head)
    result = s.swapPairs(head)
    PrintLinkedList(result)

