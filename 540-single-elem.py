

class Solution:
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.o_logn(nums, 0, len(nums))
        # return self.o_n(nums)

    def o_n(self, nums):
        if len(nums) == 1:
            return nums[0]
        i = 0
        while i < len(nums) - 1:
            if nums[i] == nums[i + 1]:
                i += 2
            else:
                return nums[i]
        return nums[len(nums) - 1]

    def o_logn(self, nums, beg, end):
        mid = int((beg + end) / 2)
        if end - beg < 3 or \
                (mid > beg and (mid + 1) < end and nums[mid] != nums[mid - 1] and nums[mid] != nums[mid + 1]):
            return nums[mid]
        else:
            pair = int((end - beg - 1) / 2) % 2
            if nums[mid] == nums[mid + 1] and pair == 1:
                return self.o_logn(nums, beg, mid)
            if nums[mid] == nums[mid - 1] and pair == 0:
                return self.o_logn(nums, beg, mid - 1)
            if nums[mid] == nums[mid + 1] and pair == 0:
                return self.o_logn(nums, mid, end)
            if nums[mid] == nums[mid - 1] and pair == 1:
                if end - beg == 3:
                    return self.o_logn(nums, mid, end)
                else:
                    return self.o_logn(nums, mid - 1, end)


import unittest as ut


class Test(ut.TestCase):
    def test(self):
        s = Solution()
        self.assertEqual(1, s.singleNonDuplicate([1]))
        self.assertEqual(3, s.singleNonDuplicate([2, 2, 3]))
        self.assertEqual(10, s.singleNonDuplicate([3, 3, 7, 7, 10, 11, 11]))
        self.assertEqual(9, s.singleNonDuplicate([1, 1, 2, 2, 4, 4, 5, 5, 9]))
        self.assertEqual(2, s.singleNonDuplicate([1, 1, 2, 3, 3, 4, 4, 8, 8]))


if __name__ == '__main__':
    ut.main()
