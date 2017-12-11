class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        buckets = {}
        for n in nums:
            if n not in buckets:
                buckets[n] = 0
            buckets[n] += 1
        freq = [i[0] for i in (sorted([(b[0], b[1]) for b in buckets.items()], key=lambda x:x[1], reverse=True)[:k])]
        return freq


import unittest as ut


class Test(ut.TestCase):
    def test(self):
        s = Solution()
        self.assertEqual([1, 2], s.topKFrequent([1, 1, 1, 2, 2, 3], 2))


if __name__ == '__main__':
    ut.main()
