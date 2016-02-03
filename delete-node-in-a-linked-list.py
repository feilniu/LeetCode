from LeetCodeLib.LinkedList import *

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next

LL = BuildLinkedList([1, 2, 3, 4])
PrintLinkedList(LL)
pointer = LL.next.next
s = Solution()
s.deleteNode(pointer)
PrintLinkedList(LL)

