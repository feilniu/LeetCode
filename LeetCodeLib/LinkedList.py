# vim:fdm=marker:

class ListNode(object):#{{{
    ''' Definition for singly-linked list.
    '''
    def __init__(self, x):
        self.val = x
        self.next = None
#}}}

def BuildLinkedListIntoList(vals):#{{{
    ''' Build linked list with a values list, return a list of ListNode.
    :type vals: List[T]
    :rtype: List[ListNode]
    '''
    if vals:
        nodes = []
        for i in range(len(vals)):
            node = ListNode(vals[i])
            nodes.append(node)
            if i > 0:
                nodes[i - 1].next = node
        return nodes
    return None
#}}}
def PrintLinkedListWithList(nodes):#{{{
    '''
    :type nodes: List[ListNode]
    :rtype: void
    '''
    vals = list(str(node.val) for node in nodes)
    i = -1
    if nodes[-1].next:
        for i in range(len(nodes)):
            if nodes[-1].next == nodes[i]:
                break
        else:
            i = -1
            vals.append('?')
    if i == -1:
        print(' -> '.join(vals))
    else:
        width = max(len(val) for val in vals)
        valfmt = ''.join(('{:', str(width), '}'))
        print(' -> '.join(valfmt.format(val) for val in vals), '-')
        length = len(nodes)
        step1 = (4 + width) * i
        step2 = (4 + width) * (length - i) - 3
        print(''.join((' ' * step1, '^', ' ' * step2, '|')))
        print(''.join((' ' * step1, '+', '-' * step2)))

#}}}
def BuildLinkedList(vals):#{{{
    ''' Build linked list with a values list, return the head node.
    :type vals: List[T]
    :rtype: ListNode
    '''
    if vals:
        head = ListNode(vals[0])
        pointer = head
        for i in range(1, len(vals)):
            pointer.next = ListNode(vals[i])
            pointer = pointer.next
        return head
    return None
#}}}
def PrintLinkedList(head):#{{{
    '''
    :type head: ListNode
    :rtype: void
    '''
    vals = []
    if head:
        vals.append(head.val)
        pointer = head
        while pointer.next:
            pointer = pointer.next
            vals.append(pointer.val)
    print(' -> '.join(str(v) for v in vals))
#}}}

def LinkedListToList(head):#{{{
    '''
    :type head: ListNode
    :rtype: List[T]
    '''
    vals = []
    if head:
        vals.append(head.val)
        pointer = head
        while pointer.next:
            pointer = pointer.next
            vals.append(pointer.val)
    return vals
#}}}
