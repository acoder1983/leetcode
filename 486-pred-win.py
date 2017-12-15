class Solution:
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        pass


import unittest as ut


class Test(ut.TestCase):
    def test(self):
        s = Solution()
        self.assertEqual(False, s.PredictTheWinner([1, 5, 2]))
        self.assertEqual(True, s.PredictTheWinner([1, 5, 233, 7]))


if __name__ == '__main__':
    ut.main()
