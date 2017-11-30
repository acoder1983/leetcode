import time


class Solution:
    # def reconstructQueue(self, people):
    #     """
    #     :type people: List[List[int]]
    #     :rtype: List[List[int]]
    #     """
    #     i = 0
    #     while i < len(people):
    #         next_i = self.setInQueue(i, people)
    #         # print(people, i, next_i)
    #         i = next_i
    #         # time.sleep(1)
    #     return people

    # def setInQueue(self, i, people):
    #     taller_n = people[i][1]
    #     height = people[i][0]
    #     taller_c = 0
    #     next_i = i + 1
    #     new_i = -1
    #     p_i = people[i]
    #     for x, p in enumerate(people):
    #         if taller_n == 0:
    #             if x < i and p[0] >= height:
    #                 new_i = x
    #                 del people[i]
    #                 people.insert(new_i, p_i)
    #                 next_i = new_i + 1
    #                 break
    #         else:
    #             if p[0] >= height and x != i:
    #                 taller_c += 1

    #             if taller_c == taller_n and x == i:
    #                 break

    #             if taller_c == taller_n + 1:
    #                 new_i = x
    #                 if new_i != i:
    #                     if new_i < i:
    #                         del people[i]
    #                         people.insert(new_i, p_i)
    #                         next_i = new_i + 1
    #                     else:
    #                         people.insert(new_i, p_i)
    #                         del people[i]
    #                         next_i = i
    #                     break

    #             if x == len(people) - 1:
    #                 people.append(p_i)
    #                 del people[i]
    #                 next_i = i
    #     return next_i

    def reconstructQueue(self, people):
        people=sorted(people, key=lambda p: (-p[0],p[1]))
        print(people)
        queue = []
        for p in people:
            queue.insert(p[1], p)
        return queue

import unittest as ut


class Test(ut.TestCase):
    def test(self):
        s = Solution()
        self.assertEqual([[2, 0], [1, 1]],
                         s.reconstructQueue([[1, 1], [2, 0]]))

        self.assertEqual([[5, 0], [7, 0], [5, 2], [6, 1], [4, 4], [7, 1]],
                         s.reconstructQueue([[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]))


if __name__ == '__main__':
    ut.main()
