from LeetCodeLib.LinkedList import *

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head:
            p1 = p2 = head
            while p1.next and p2.next and p2.next.next:
                p1 = p1.next
                p2 = p2.next.next
                if p1 == p2:
                    return True
        return False

s = Solution()
nodes = BuildLinkedListIntoList(range(10))
print(s.hasCycle(nodes[0]))
PrintLinkedListWithList(nodes)
nodes[-1].next = nodes[0]
print(s.hasCycle(nodes[0]))
PrintLinkedListWithList(nodes)
nodes[-1].next = nodes[1]
print(s.hasCycle(nodes[0]))
PrintLinkedListWithList(nodes)
nodes[-1].next = nodes[2]
print(s.hasCycle(nodes[0]))
PrintLinkedListWithList(nodes)
nodes[-1].next = nodes[5]
print(s.hasCycle(nodes[0]))
PrintLinkedListWithList(nodes)
nodes[-1].next = nodes[9]
print(s.hasCycle(nodes[0]))
PrintLinkedListWithList(nodes)
