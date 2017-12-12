class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}
        for i in range(len(nums)):
            d[nums[i]] = i
        for i in range(len(nums)):
            j = target - nums[i]
            if j in d and i != d[j]:
                return [i, d[j]]
        return []


import unittest as ut


class Test(ut.TestCase):
    def test(self):
        s = Solution()
        self.assertEqual([0, 1], s.twoSum([2, 7, 11, 15], 9))
        self.assertEqual([1, 2], s.twoSum([3, 2, 4], 6))


if __name__ == '__main__':
    ut.main()
