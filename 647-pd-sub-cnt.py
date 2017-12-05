
class Solution:
    def countSubstrings(self, s):
        c = 0
        for i in range(len(s)):
            b = e = i
            while b > -1 and e < len(s):
                if s[b] == s[e]:
                    c += 1
                    b -= 1
                    e += 1
                else:
                    break
            b = i
            e = i + 1
            while b > -1 and e < len(s):
                if s[b] == s[e]:
                    c += 1
                    b -= 1
                    e += 1
                else:
                    break
        return c
    # def countSubstrings(self, s):
    #     """
    #     :type s: str
    #     :rtype: int
    #     """
    #     c = 0
    #     for i in range(len(s)):
    #         for j in range(i + 1, len(s) + 1):
    #             if self.is_pd(s, i, j - 1):
    #                 c += 1
    #     return c

    # def is_pd(self, s, i, j):
    #     while i < j:
    #         if s[i] == s[j]:
    #             i += 1
    #             j -= 1
    #         else:
    #             return False
    #     return True


import unittest as ut


class Test(ut.TestCase):
    def test(self):
        s = Solution()
        self.assertEqual(3, s.countSubstrings('abc'))
        self.assertEqual(6, s.countSubstrings('aaa'))


if __name__ == '__main__':
    ut.main()
