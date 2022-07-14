"""
105. Construct Binary Tree from Preorder and Inorder Traversal_M

https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

#################################
考点或思路:
[solution: tree:  treversal]
Similar problems:


"""

from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """
        time: 07/14/2022   11:05--11:25
        [Approach] 利用tree traverse 的规则去建立tree的结构，每个preOrder的第一个肯定都是root，然后在 inOrder中找到这个root，inOrder的root前边就是leftsubTree，
        后边就是rightSubTree，按照这个subtree的个数，再从preOrderlist中分离出leftSubtree，和rightSubTree，然后递归。最终可以建立起整个tree。
        TIme-O(N)  we go through the tree once.
        space_O(H) we use recursion, so the stack space would be the height of the tree.  
        """
        if preorder == [] or inorder == []:
            return None
        
        if preorder == inorder and len(preorder) == 1:
            return TreeNode(preorder[0])
        
        root = TreeNode(preorder[0])
        
        # seperate the left subtree from inorder list
        rootidx = inorder.index(preorder[0])
        leftsubInorder = inorder[:rootidx]
        rightsubInorder = inorder[rootidx+1:]
        leftsubPreOrder = preorder[1:len(leftsubInorder)+1]
        rightsubPreOrder = preorder[len(leftsubInorder)+1:]
        
        root.left  = self.buildTree(leftsubPreOrder,leftsubInorder)
        root.right = self.buildTree(rightsubPreOrder,rightsubInorder)
        
        return root
        