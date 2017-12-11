class Solution:
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        i = 0
        j = i + 1
        c = 0
        while j < len(A):
            diff = A[j] - A[i]
            while j + 1 < len(A) and A[j + 1] - A[j] == diff:
                j += 1
            l = j - i
            c += self._calc_cnt(l)
            i = j
            j += 1
        return c

    def _calc_cnt(self, l):
        if l < 2:
            return 0
        else:
            return sum(range(1, l))


import unittest as ut


class Test(ut.TestCase):
    def test(self):
        s = Solution()
        self.assertEqual(1, s.numberOfArithmeticSlices([1, 2, 3]))
        self.assertEqual(3, s.numberOfArithmeticSlices([1, 2, 3, 4]))
        self.assertEqual(10, s.numberOfArithmeticSlices([1, 2, 3, 4, 5, 6]))
        self.assertEqual(2, s.numberOfArithmeticSlices([1, 2, 3, 8, 9, 10]))


if __name__ == '__main__':
    ut.main()
