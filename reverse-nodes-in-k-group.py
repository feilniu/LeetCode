from LeetCodeLib.LinkedList import *

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        tail = head
        if tail and tail.next:
            for i in range(k):
                if not tail:
                    return head
                tail = tail.next
            tail = self.reverseKGroup(tail, k)
            for i in range(k):
                p = head.next
                head.next = tail
                tail = head
                head = p
        return tail

l = [1,2,3,4,5,6,7,8,9]
s = Solution()
for i in range(2,12):
    head = BuildLinkedList(l)
    head = s.reverseKGroup(head, i)
    print(i)
    PrintLinkedList(head)

