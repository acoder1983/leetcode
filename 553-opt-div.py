
class Solution:
    def optimalDivision(self, nums):
        s = []
        if len(nums) == 1:
            s.append(str(nums[0]))
        else:
            s += [str(nums[0]), '/', str(nums[1])]
            i = 2
            while i < len(nums):
                beg = len(s) - 1
                j = i
                while i < len(nums) and nums[i] > 1:
                    s += ['/', str(nums[i])]
                    i += 1
                if j < i:
                    s.insert(beg, '(')
                    s.append(')')
                else:
                    s += ['/', str(nums[i])]
                i += 1
        r = ''
        for x in s:
            r += x
        return r

    # def optimalDivision(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: str
    #     """
    #     if len(nums) == 1:
    #         return nums[0]
    #     elif len(nums) == 2:
    #         return nums[0] / nums[1]
    #     else:
    #         results = [nums[0]]
    #         expr_sets = []
    #         for i in range(1, len(nums)):
    #             prd = [a for a in results]
    #             div = [a for a in results]

    #             prd_expr = [a.copy() for a in expr_sets]
    #             if len(prd_expr) == 0:
    #                 prd_expr.append(['/'])
    #             else:
    #                 tmp = []
    #                 for a in prd_expr:
    #                     a.append('*')
    #                     tmp.append(a)
    #                 prd_expr = tmp

    #             div_expr = [a.copy() for a in expr_sets]
    #             if len(div_expr) == 0:
    #                 div_expr.append(['/'])
    #             else:
    #                 tmp = []
    #                 for a in div_expr:
    #                     a.append('/')
    #                     tmp.append(a)
    #                 div_expr = tmp

    #             for j in range(len(results)):
    #                 if prd_expr[j][-1] == '*':
    #                     prd[j] = prd[j] * nums[i]
    #                 else:
    #                     prd[j] = prd[j] / nums[i]

    #                 if div_expr[j][-1] == '*':
    #                     div[j] = div[j] * nums[i]
    #                 else:
    #                     div[j] = div[j] / nums[i]

    #             results = prd + div
    #             expr_sets = prd_expr + div_expr
    #         max_v = -1
    #         max_i = -1
    #         for i, r in enumerate(results):
    #             if r > max_v:
    #                 max_v = r
    #                 max_i = i
    #         print(expr_sets[max_i])
    #         return max_v


import unittest as ut


class Test(ut.TestCase):
    def test(self):
        s = Solution()
        self.assertEqual('1', s.optimalDivision([1]))
        self.assertEqual('10/2', s.optimalDivision([10, 2]))
        self.assertEqual('1000/(100/10/2)',
                         s.optimalDivision([1000, 100, 10, 2]))


if __name__ == '__main__':
    ut.main()
