class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def list_new(arr):
    next = head = ListNode(0)
    for a in arr:
        next.next = ListNode(a)
        next = next.next

    return head.next


def list_equal(lst1, lst2):
    while lst1 is not None and lst2 is not None:
        if lst1.val != lst2.val:
            return False
        lst1 = lst1.next
        lst2 = lst2.next

    return lst1 is None and lst2 is None


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def tree_from_seq(seq):
    if len(seq) == 0:
        return None

    root = TreeNode(seq.pop(0))
    node_q = [root]
    while len(seq) > 0:
        n = node_q.pop(0)

        v = seq.pop(0)
        if v is not None:
            n.left = TreeNode(v)
            node_q.append(n.left)

        if len(seq) > 0:
            v = seq.pop(0)
            if v is not None:
                n.right = TreeNode(v)
                node_q.append(n.right)

    return root


import unittest as ut


class Test(ut.TestCase):
    def testList(self):
        head = ListNode(1)
        head.next = ListNode(2)
        head.next.next = ListNode(3)
        head.next.next.next = ListNode(4)
        list1 = list_new([1, 2, 3, 4])
        assert list_equal(head, list1)

    def testTree(self):

        def preorder(root, seq):
            if root is None:
                return
            seq.append(root.val)
            preorder(root.left, seq)
            preorder(root.right, seq)

        root = tree_from_seq([1, 2, 3, None, 4, 5])
        seq = []
        preorder(root, seq)
        self.assertEqual([1, 2, 4, 3, 5], seq)

        root = tree_from_seq([3, 5, 1, 6, 2, 9, 8, None, None, 7, 4])
        seq = []
        preorder(root, seq)
        self.assertEqual([3, 5, 6, 2, 7, 4, 1, 9, 8], seq)

        root = tree_from_seq(
            [3, 5, 1, 6, 7, 4, 2, None, None, None, None, None, None, 9, 8])
        seq = []
        preorder(root, seq)
        self.assertEqual([3, 5, 6, 7, 1, 4, 2, 9, 8], seq)


if __name__ == '__main__':
    ut.main()
