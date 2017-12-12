class Solution:
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        results = []
        p=[]
        i = 0
        while i < len(nums):
            if i+1<len(nums) and a[i+1]>a[i]
            j = i + 1
            while i != j:
                if j == len(nums):
                    j = 0
                    continue
                if nums[j] > nums[i]:
                    n = len(nums)
                    if j > i:
                        n = j
                    for k in range(i, n):
                        results.append(nums[j])
                    i = n - 1
                    break
                else:
                    j += 1
            if i == j:
                results.append(-1)
            i += 1
        return results


import unittest as ut


class Test(ut.TestCase):
    def test(self):
        s = Solution()
        # self.assertEqual([-1], s.nextGreaterElements([1]))
        # self.assertEqual([2, -1, 2], s.nextGreaterElements([1, 2, 1]))
        # self.assertEqual([-1, 3, 3], s.nextGreaterElements([3, 2, 1]))
        self.assertEqual([2, 3, -1, 3, 2],
                         s.nextGreaterElements([1, 2, 3, 2, 1]))


if __name__ == '__main__':
    ut.main()
