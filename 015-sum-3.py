class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums=sorted(nums)
        d = {}
        for i in range(len(nums)):
            if nums[i] not in d:
                d[nums[i]]=[]
            d[nums[i]].append(i)
        r = []
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                neg = -nums[i] - nums[j]
                if neg in d and d[neg][-1] > j:
                    r.append([nums[i], nums[j], neg])
                    # a = sorted([nums[i], nums[j], neg])
                    # if a not in r:
                    #     r.append(a)
        return r


import unittest as ut


class Test(ut.TestCase):
    def test(self):
        s = Solution()
        self.assertEqual([
            [-1, 0, 1],
            [-1, -1, 2]
        ], s.threeSum([-1, 0, 1, 2, -1, -4]))


if __name__ == '__main__':
    ut.main()
