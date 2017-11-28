

class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        brd = board.copy()
        ships = 0
        h = len(brd)
        w = len(brd[0])
        for i in range(h):
            for j in range(w):
                if brd[i][j] == 'X':
                    k = j
                    reach_end = True
                    for k in range(j + 1, w):
                        if brd[i][k] == '.':
                            reach_end = False
                            break
                    if reach_end:
                        k = w
                    if k > j + 1:
                        for m in range(j, k):
                            brd[i][m] = '.'
                        ships += 1

        for j in range(w):
            for i in range(h):
                if brd[i][j] == 'X':
                    k = i
                    reach_end = True
                    for k in range(i + 1, h):
                        if brd[k][j] == '.':
                            reach_end = False
                            break
                    if reach_end:
                        k = h
                    if k > i + 1:
                        for m in range(i, k):
                            brd[m][j] = '.'
                        ships += 1

        for i in range(h):
            for j in range(w):
                if brd[i][j] == 'X':
                    ships += 1
        return ships


import unittest as ut


class Test(ut.TestCase):
    def test(self):
        s = Solution()
        self.assertEqual(1, s.countBattleships([['X']]))
        self.assertEqual(1, s.countBattleships([['X', 'X']]))
        self.assertEqual(1, s.countBattleships([['X', '.'],['X','.']]))

if __name__ == '__main__':
    ut.main()
