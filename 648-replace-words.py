class Solution:
    def replaceWords(self, dict, sentence):
        """
        :type dict: List[str]
        :type sentence: str
        :rtype: str
        """
        words = sentence.split()
        for i in range(len(words)):
            wd = words[i]
            root = wd
            for r in dict:
                if wd.startswith(r) and len(r) < len(root):
                    root = r
            words[i] = root

        return ' '.join(words)


import unittest as ut


class Test(ut.TestCase):
    def test(self):
        s = Solution()
        self.assertEqual("the cattle was rattled by the battery", s.replaceWords(
            [], "the cattle was rattled by the battery"))
        self.assertEqual("the cat was rat by the bat", s.replaceWords(
            ["cat", "bat", "rat"], "the cattle was rattled by the battery"))


if __name__ == '__main__':
    ut.main()
