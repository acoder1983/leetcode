class Solution:
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        searched = [0 for i in range(len(M))]
        circles = 0
        for i in range(len(M)):
            if searched[i] == 0:
                circles += 1
                self.find_friends(i, M, searched)

        return circles

    def find_friends(self, i, M, searched):
        searched[i] = 1
        for j in range(len(M)):
            if i != j and M[i][j] == 1 and searched[j] == 0:
                self.find_friends(j, M, searched)


import unittest as ut


class Test(ut.TestCase):
    def test(self):
        s = Solution()
        self.assertEqual(1, s.findCircleNum([[1, 1, 0], [1, 1, 1], [0, 1, 1]]))
        self.assertEqual(2, s.findCircleNum([[1, 1, 0], [1, 1, 0], [0, 0, 1]]))


if __name__ == '__main__':
    ut.main()
