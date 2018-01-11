class Solution:
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        if len(word1)<len(word2):
            short_w=word1
            long_w=word2
        else:
            short_w=word2
            long_w=word1
        ch_seqs=[]
        for c in short_w:
            pos=[]
            for i,c_i in enumerate(long_w):
                if c == c_i:
                    pos.append(i)
            ch_seqs.append(pos)

        max_l=max_inc_len(ch_seqs)

        return len(word1) + len(word2) - 2 * max_l

    def max_inc_len(self,ch_seqs):
        

import unittest as ut


class Test(ut.TestCase):
    def test(self):
        s = Solution()
        self.assertEqual(2, s.minDistance('sea', 'eat'))
        self.assertEqual(0, s.minDistance('a', 'a'))
        self.assertEqual(3, s.minDistance('park', 'spake'))


if __name__ == '__main__':
    ut.main()
