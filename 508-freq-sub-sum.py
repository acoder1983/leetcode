
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        freq = {}
        self.find_freq(root, freq)
        freq = [(k, v) for k, v in freq.items()]
        freq = sorted(freq, key=lambda x: x[1], reverse=True)
        i = 0
        while i + 1 < len(freq) and freq[i][1] == freq[i + 1][1]:
            i += 1
        return [f[0] for f in freq[:i + 1]]

    def find_freq(self, node, freq):
        l = r = 0
        if node.right is not None:
            r = self.find_freq(node.right, freq)
        if node.left is not None:
            l = self.find_freq(node.left, freq)
        s = node.val + l + r
        if s not in freq:
            freq[s] = 0
        freq[s] += 1
        return s


import unittest as ut


class Test(ut.TestCase):
    def test(self):
        s = Solution()
        tr = TreeNode(5)
        tr.left = TreeNode(2)
        tr.right = TreeNode(-3)
        # self.assertEqual([2, -3, 4], s.findFrequentTreeSum(tr))

        tr.right = TreeNode(-5)
        self.assertEqual([2], s.findFrequentTreeSum(tr))


if __name__ == '__main__':
    ut.main()
