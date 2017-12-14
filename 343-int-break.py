from math import sqrt


class Solution:
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 2:
            return 1

        a = int(sqrt(n))
        max_v = 0
        for i in range(2, a + 2):
            j = self.prod(n, i)
            if j > max_v:
                max_v = j
        return max_v

    def prod(self, n, a):
        s = 1
        while n > 0:
            if n - a < 2 and s != 1:
                a = n
            s *= a
            n -= a
        return s


import unittest as ut


class Test(ut.TestCase):
    def test(self):
        s = Solution()
        self.assertEqual(1, s.integerBreak(2))
        self.assertEqual(2, s.integerBreak(3))
        self.assertEqual(6, s.integerBreak(5))
        self.assertEqual(9, s.integerBreak(6))
        self.assertEqual(36, s.integerBreak(10))
        self.assertEqual(324, s.integerBreak(16))
        self.assertEqual(8748, s.integerBreak(25))


if __name__ == '__main__':
    ut.main()
