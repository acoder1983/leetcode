class Solution:
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return 0
        s = [1 for i in range(n)]
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                if i == 0 and s[0] < s[j]:
                    s[0] = s[j]
                if nums[i] < nums[j] and s[j] + 1 > s[i]:
                    s[i] = s[j] + 1
        return s[0]


import unittest as ut


class Test(ut.TestCase):
    def test(self):
        s = Solution()
        self.assertEqual(1, s.lengthOfLIS([1]))
        self.assertEqual(2, s.lengthOfLIS([1, 2]))
        self.assertEqual(2, s.lengthOfLIS([3, 1, 2]))
        self.assertEqual(4, s.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))
        self.assertEqual(3, s.lengthOfLIS([4, 10, 4, 3, 8, 9]))


if __name__ == '__main__':
    ut.main()
