import re


class Solution(object):
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        m = re.compile('.+\+')
        a1 = int(m.search(a).group(0)[:-1])
        a2 = int(m.search(b).group(0)[:-1])
        m = re.compile('\+.+i')
        b1 = int(m.search(a).group(0)[1:-1])
        b2 = int(m.search(b).group(0)[1:-1])
        return '%d+%di' % (a1 * a2 - b1 * b2, a1 * b2 + a2 * b1)


import unittest as ut


class Test(ut.TestCase):
    def test(self):
        s = Solution()
        self.assertEqual('0+2i', s.complexNumberMultiply('1+1i', '1+1i'))
        self.assertEqual('0+0i', s.complexNumberMultiply('0+0i', '1+1i'))
        self.assertEqual('1+-5i', s.complexNumberMultiply('3+-2i', '1+-1i'))

if __name__ == '__main__':
    ut.main()
