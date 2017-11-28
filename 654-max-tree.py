# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        root = self.buildBT(nums,0,len(nums))
        result = []
        self.breadthSearch([root],result)
        return result

    def breadthSearch(self,nodes,result):
        next_level_nodes=[]
        not_null_nodes=[]
        last_not_null_idx=-1
        next_level_node_not_null=False
        for i,n in enumerate(nodes):
            if n is not None:
                not_null_nodes.append(n)
                next_level_nodes.append(n.left)
                next_level_nodes.append(n.right)
                if n.left is not None or n.right is not None:
                    next_level_node_not_null=True
                last_not_null_idx=i

        if len(not_null_nodes)>0:
            if next_level_node_not_null:
                result+=[None if n is None else n.val for n in nodes]
            else:
                result+=[None if n is None else n.val for n in nodes[:last_not_null_idx+1]]
            self.breadthSearch(next_level_nodes,result)

    
    def buildBT(self,nums,beg,end):
        if beg < end:
            idx=beg
            for i in range(beg+1,end):
                if nums[i]>nums[idx]:
                    idx=i
            n = TreeNode(nums[idx])
            
            n.left=self.buildBT(nums,beg,idx)
            n.right=self.buildBT(nums,idx+1,end)
            
            return n
            
import unittest as ut

class Test(ut.TestCase):
    def test(self):
        # s=Solution()
        # tn=TreeNode(6)
        # tn.left=TreeNode(3)
        # tn.right=TreeNode(5)
        # tn.left.right=TreeNode(2)
        # tn.right.left=TreeNode(0)
        # tn.left.right.right=TreeNode(1)
        # a=[]
        # s.breadthSearch([tn],a)
        # print(a)
        
        s=Solution()
        # self.assertEqual([3,2,None,1],s.constructMaximumBinaryTree([1,2,3]))
        self.assertEqual([],s.constructMaximumBinaryTree([]))
        self.assertEqual([3],s.constructMaximumBinaryTree([3]))
        self.assertEqual([3,2],s.constructMaximumBinaryTree([2,3]))
        self.assertEqual([3,2,None,1],s.constructMaximumBinaryTree([1,2,3]))
        self.assertEqual([6,3,5,None,None,0],s.constructMaximumBinaryTree([3,6,0,5]))
        self.assertEqual([6,3,5,None,2,0,None,None,1],s.constructMaximumBinaryTree([3,2,1,6,0,5]))

if __name__ == '__main__':
    ut.main()