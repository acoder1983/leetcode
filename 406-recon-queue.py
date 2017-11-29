

class Solution:
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        for i in range(len(people)):
            next_i = self.setInQueue(i, people)
            if next_i == len(people):
                break
            else:
                i = next_i - 1
        return people

    def setInQueue(self, i, people):
        taller_n = people[i][1]
        height = people[i][0]
        taller_c = 0
        next_i = i + 1
        new_i = -1
        for x, p in enumerate(people):
            if taller_n == 0:
                if x < i and p[0] >= height:
                    new_i = x
                    tmp = people[i]
                    people[i] = people[new_i]
                    people[new_i] = tmp
                    next_i = new_i
                    break
            else:
                if p[0] >= height and x != i:
                    taller_c += 1
                
                if taller_c == taller_n:
                    new_i = x + 1
                    if new_i != i:
                        if new_i == len(people):
                            people.append(people[i])
                            del people[i]
                        else:
                            tmp = people[i]
                            people[i] = people[new_i]
                            people[new_i] = tmp

                        if new_i < i:
                            next_i = new_i
                        else:
                            next_i = i
                        break

        return next_i


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
