from LeetCodeLib.BinaryTree import *

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        result = []
        if root:
            nodeStack = []
            nodeStack.append(root)
            visitedNode = root
            while nodeStack:
                if nodeStack[-1].left and visitedNode not in (nodeStack[-1].left, nodeStack[-1].right):
                    nodeStack.append(nodeStack[-1].left)
                elif nodeStack[-1].right and visitedNode != nodeStack[-1].right:
                    nodeStack.append(nodeStack[-1].right)
                elif nodeStack[-1].left == None and nodeStack[-1].right == None:
                    thisPath = list(str(n.val) for n in nodeStack)
                    result.append('->'.join(thisPath))
                    visitedNode = nodeStack.pop()
                else:
                    visitedNode = nodeStack.pop()
        return result

testCases = [
        [[], []],
        [[1], ['1']],
        [[1, 2], ['1->2']],
        [[1, None, 2], ['1->2']],
        [[1, 2, 3], ['1->2', '1->3']],
        [[1, 2, 3, 4, 5, None, 6, None, 7], ['1->2->4->7', '1->2->5', '1->3->6']]
        ]
s = Solution()
for tc in testCases:
    r = BuildTree(tc[0])
    result = s.binaryTreePaths(r)
    passed = result == tc[1]
    if not passed:
        print(tc, result, passed)

