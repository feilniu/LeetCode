from LeetCodeLib.BinaryTree import *

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root:
            path_p = path_q = None
            nodeStack = []
            nodeStack.append(root)
            visitedNode = root
            while nodeStack:
                node = nodeStack[-1]
                if node == p and path_p == None:
                    path_p = list(nodeStack)
                if node == q and path_q == None:
                    path_q = list(nodeStack)
                if path_p and path_q:
                    i = 0
                    len_p = len(path_p)
                    len_q = len(path_q)
                    while i < len_p and i < len_q and path_p[i] == path_q[i]:
                        i += 1
                    return path_p[i - 1]
                if node.left and visitedNode not in (node.left, node.right):
                    nodeStack.append(node.left)
                elif node.right and visitedNode != node.right:
                    nodeStack.append(node.right)
                else:
                    visitedNode = nodeStack.pop()
        return None


testCases = [
        [[6, 2, 8, 0, 4, 7, 9, None, None, 3, 5], 1, 2, 0],
        [[6, 2, 8, 0, 4, 7, 9, None, None, 3, 5], 1, 5, 0],
        [[6, 2, 8, 0, 4, 7, 9, None, None, 3, 5], 1, 4, 1],
        [[5], 0, 0, 0],
        [[5, 2], 0, 1, 0],
        [[5, None, 8], 0, 2, 0],
        [[3, 5, 1, 6, 2, 0, 8, None, None, 7, 4], 1, 2, 0],
        [[3, 5, 1, 6, 2, 0, 8, None, None, 7, 4], 1, 4, 1],
        [[3, 5, 1, 6, 2, 0, 8, None, None, 7, 4], 1, 6, 0]
        ]
s = Solution()
for tc in testCases:
    TL = BuildTreeIntoList(tc[0])
    result_node = s.lowestCommonAncestor(TL[0], TL[tc[1]], TL[tc[2]])
    result = TL.index(result_node)
    passed = result == tc[3]
    if not passed:
        print(tc, result, passed)
TL = BuildTreeIntoList([5, 2, 1])
result_node = s.lowestCommonAncestor(TL[0], TL[1], TreeNode(0))
print(result_node)

