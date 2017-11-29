
import math
class Solution:
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        dups=[]
        for i in range(len(nums)):
            idx=int(math.fabs(nums[i]))-1
            if nums[idx]<0:
                dups.append(nums[i])
            else:
                nums[idx]=-nums[idx]
        return dups

import unittest as ut


class Test(ut.TestCase):
    def test(self):
        s = Solution()
        self.assertEqual([], s.findDuplicates([1]))
        self.assertEqual([1], s.findDuplicates([1,2,1]))
        self.assertEqual([1,2], s.findDuplicates([1,2,1,2,0]))
        self.assertEqual([2,3], s.findDuplicates([4,3,2,7,8,2,3,1]))


if __name__ == '__main__':
    ut.main()
