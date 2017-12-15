class Solution:
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        ins_p = {}
        most_freq = 0
        for row in wall:
            p = 0
            for i in range(len(row) - 1):
                p += row[i]
                if p not in ins_p:
                    ins_p[p] = 0
                ins_p[p] += 1
                if ins_p[p] > most_freq:
                    most_freq = ins_p[p]
        return len(wall) - most_freq


import unittest as ut


class Test(ut.TestCase):
    def test(self):
        s = Solution()
        self.assertEqual(0, s.leastBricks([[1, 2, 2, 1],
                                           [3, 1, 2]]))
        self.assertEqual(2, s.leastBricks([[1, 2, 2, 1],
                                           [3, 1, 2],
                                           [1, 3, 2],
                                           [2, 4],
                                           [3, 1, 2],
                                           [1, 3, 1, 1]]))


if __name__ == '__main__':
    ut.main()
