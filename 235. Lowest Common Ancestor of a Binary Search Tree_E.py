"""
235. Lowest Common Ancestor of a Binary Search Tree_E

https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

##############################

类似题型:


#################################
考点或思路:

"""
from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        time: 051822  10:50--
        [Approach] I will first use Dict to record the parent-child relationship between nodes.
        And I search for p and q, and get their ancestors into stacks backwords. 
        Then compare the ancestors in two stacks, find the latest common node in both stacks.
        time_O(N+N+ H)-->O(N) search for p and q will cost 2H, compare the ancestors cost H , where H may be N at worst.
        space_O(N+2H) -->O(N) use Dict to record the parent-child relationship will cost N, stacks for p and q will cost 2H.
        [NOTES] This is not a very effective method, we can make it more efficient because it is aa BST.
        """
        parentDict = {root:None}
        
        def biSearch(root, target, stack):
            if root.val == target.val:
                p = parentDict[root]
                while p:
                    stack.insert(0,p)
                    p = parentDict[p]
                stack.append(root)
                return 
            elif root.val > target.val:
                if root.left:
                    parentDict[root.left] = root
                    biSearch(root.left,target, stack)
            else:
                if root.right:
                    parentDict[root.right] = root
                    biSearch(root.right,target, stack)
        
        stackp = []
        stackq = []
        biSearch(root, p , stackp)
        biSearch(root,q, stackq)
        
        LCA = root
        for i in range(min(len(stackp), len(stackq))):
            if stackp[i] == stackq[i]:
                LCA = stackp[i]
            else:
                break
                
        return LCA
        
    def lowestCommonAncestor_V1(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        [Approach] Since this is a BST, the node are in increasing order if we see them in inorder traversal.
        each time we go down to a branch of the tree, if p and q both smaller than the root of subtree, they both go to the left, 
        the LCA must be also in the left subtree, or if p and q both bigger than a root of a subtree, p,q, LCA must all go to the rightside.
        if p and q, one is bigger or equel to the root, the ather one is smaller , then they need to go to different side of the root.
        then this root of the subtree is the LCA of p and q.
        Time_O(N) wo go though the tree only once.
        space_O(1) 
        """

        def inorderT(root, p, q):
            if p.val < root.val and q.val < root.val:
                return inorderT(root.left,p, q)
            elif p.val > root.val and q.val > root.val:
                return inorderT(root.right, p ,q)
            else:
                return root
            
        return inorderT(root,p,q)


    def lowestCommonAncestor_V2(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        [Approach] we do preorder traversal to find the p node and qNode in the Tree, 
        if a node is in the left subtree, we mark left== theNode, else we mark right = the Node.
        for the LCA, it must has one node in the leftsubtree , one node in the right, so the current node should be the LCA.
        [NOTE] This approach can be used for 236. 
        There is a condition for this approach, p,q must be exist in the tree. if p or q may not exist , this mathod would be wrong.(1644)
        """
        def findNode(root, p,q):
            if root == None:
                return None
            if root.val == p.val or root.val == q.val:
                return root
            
            left = findNode(root.left,p,q)
            right = findNode(root.right,p,q)
            # if left has one and right has one ,then this root is the LCA
            if left and right:
                return root
            return left if left else right
                
        return findNode(root, p, q)

import unittest
class TestcaseS(unittest.TestCase):
    def setUp(self):
        self.obj = Solution()
        self.f = self.obj.lowestCommonAncestor

    def testcase_1(self):
        node1 = TreeNode(6)
        node1.left = TreeNode(2)
        node1.left.left = TreeNode(0)
        node1.left.right = TreeNode(4) 
        node1.left.right.left = TreeNode(3)
        node1.left.right.right = TreeNode(5)

        node1.right = TreeNode(8)
        node1.right.left = TreeNode(7)
        node1.right.right = TreeNode(9)
        ret = self.f(node1, TreeNode(5), TreeNode(0))
        self.assertEqual(ret,node1.left)

        # a node can be considered as its own ancestor.
        ret = self.f(node1, TreeNode(2), TreeNode(4))
        self.assertEqual(ret,node1.left)

    def testcase_V1(self):
        print("****************************V1****************************")
        self.f = self.obj.lowestCommonAncestor_V1
        self.testcase_1()
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)