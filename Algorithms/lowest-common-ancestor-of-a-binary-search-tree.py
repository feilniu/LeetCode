from LeetCodeLib.BinaryTree import *

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        LCA = root
        while LCA:
            if p.val < LCA.val and q.val < LCA.val:
                LCA = LCA.left
            elif p.val > LCA.val and q.val > LCA.val:
                LCA = LCA.right
            else:
                return LCA
        return None

testCases = [
        [[6, 2, 8, 0, 4, 7, 9, None, None, 3, 5], 1, 2, 0],
        [[6, 2, 8, 0, 4, 7, 9, None, None, 3, 5], 1, 5, 0],
        [[6, 2, 8, 0, 4, 7, 9, None, None, 3, 5], 1, 4, 1],
        [[5], 0, 0, 0],
        [[5, 2], 0, 1, 0],
        [[5, None, 8], 0, 2, 0]
        ]
s = Solution()
for tc in testCases:
    TL = BuildTreeIntoList(tc[0])
    result_node = s.lowestCommonAncestor(TL[0], TL[tc[1]], TL[tc[2]])
    result = TL.index(result_node)
    passed = result == tc[3]
    if not passed:
        print(tc, result, passed)

