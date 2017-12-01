# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # return self.findBottomLeft([root], root.val)
        return self.fuck_simple(root)

    def findBottomLeft(self, nodes, max_left):
        min_v = -99999999
        next_level_nodes = []
        for n in nodes:
            if n is not None and (n.left is not None or n.right is not None):
                next_level_nodes.append(n.left)
                next_level_nodes.append(n.right)
        if len(next_level_nodes) > 0:
            max_v = min_v
            for i, n in enumerate(next_level_nodes):
                if n is not None and i % 2 == 0 and n.val > max_v:
                    max_v = n.val
            if max_v == min_v:
                return max_left
            else:
                return self.findBottomLeft(next_level_nodes, max_v)
        else:
            return max_left

    def fuck_simple(self, root):
        queue = [root]
        for node in queue:
            queue += filter(None, (node.right, node.left))
        return node.val


import unittest as ut


class Test(ut.TestCase):
    def test(self):
        s = Solution()
        # node = TreeNode(1)
        # node.right = TreeNode(1)
        # self.assertEqual(1, s.findBottomLeftValue(node))
        # node = TreeNode(0)
        # node.left = TreeNode(-1)
        # self.assertEqual(-1, s.findBottomLeftValue(node))
        node = TreeNode(0)
        node.right = TreeNode(-1)
        self.assertEqual(0, s.findBottomLeftValue(node))


if __name__ == '__main__':
    ut.main()
