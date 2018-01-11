class Solution:
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        s1 = [0]
        s2 = [0]
        players = [s1, s2]
        self.choose(players, 0, nums, 0, len(nums) - 1)
        print(players)
        return max(players[0]) >= max(players[1])

    def choose(self, players, idx, nums, i, j):
        if i > j:
            return
        this_p=players[idx].copy()
        that_p=players[1-idx].copy()
        p_h = this_p.copy()
        p_t = this_p.copy()
        k = 0
        n = len(p_h)
        while k < n:
            p_h[k] += nums[i]
            p_t[k] += nums[j]
            k += 1
        players[idx]=p_h
        self.choose(players, 1 - idx, nums, i + 1, j)
        print(players)
        players[idx]=p_t
        players[1-idx]=that_p
        self.choose(players, 1 - idx, nums, i, j - 1)
        print(players)
        players[idx] = p_h + p_t
        print(players)


import unittest as ut


class Test(ut.TestCase):
    def test(self):
        s = Solution()
        self.assertEqual(True, s.PredictTheWinner([1, 2]))
        # self.assertEqual(False, s.PredictTheWinner([1, 5, 2]))
        # self.assertEqual(True, s.PredictTheWinner([1, 5, 233, 7]))


if __name__ == '__main__':
    ut.main()
