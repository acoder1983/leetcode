class Solution:
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        s = [1 for i in range(len(pairs))]
        for i in range(len(pairs) - 1, -1, -1):
            for j in range(i + 1, len(pairs)):
                if pairs[i][1] < pairs[j][0] and s[j] + 1 > s[i]:
                    s[i] = s[j] + 1
        return s[0]


import unittest as ut


class Test(ut.TestCase):
    def test(self):
        s = Solution()
        self.assertEqual(2, s.findLongestChain([[1, 2], [2, 3], [3, 4]]))


if __name__ == '__main__':
    ut.main()
