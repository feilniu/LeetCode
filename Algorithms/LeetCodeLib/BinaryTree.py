# vim:fdm=marker:

class TreeNode(object):#{{{
    ''' Definition for binary tree node.
    '''
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
#}}}

def BuildTreeIntoList(vals):#{{{
    ''' Build tree with a values list, return a list of TreeNode.
    :type vals: List[T]
    :rtype: List[TreeNode]
    '''
    if vals:
        nodes = []
        for i in range(len(vals)):
            val = vals[i]
            if val:
                node = TreeNode(val)
                nodes.append(node)
                if i > 0:
                    a, b = divmod(i - 1, 2)
                    if nodes[a]:
                        if b == 0:
                            nodes[a].left = node
                        else:
                            nodes[a].right = node
                    else:
                        raise Exception('Bad input!')
            else:
                nodes.append(None)
        return nodes
    return None
#}}}
def BuildTree(vals):#{{{
    ''' Build tree with a values list, return the root TreeNode.
    :type vals: List[T]
    :rtype: TreeNode
    '''
    if vals:
        return BuildTreeIntoList(vals)[0]
    return None
#}}}

