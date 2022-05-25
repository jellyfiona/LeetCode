"""
1448. Count Good Nodes in Binary Tree_M

https://leetcode.com/problems/count-good-nodes-in-binary-tree/

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
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        """
        time: 052422 4:30--4:57
        [Appraoch] In the question it was partate to be four parts, root + left boundary+leaves + right boundary.
        So we should get left and right boundary and leave , then put them together.
        Time_O(2H+N) get left or right boundary need O(H), where H is the height of the tree.
                    get leaves will need O(N), so O(2H+N)
        space_O(N) it is possible that all the node will be eligible to in the boundary.
        """
        
        left = []
        cur = root.left
        # if cur has child, then it is not leave, it can be in left boundary.
        while cur:
            if cur.left or cur.right:
                left.append(cur.val)
                cur = cur.left if cur.left else cur.right
            else:
                break
                
        right = []
        cur = root.right
        while cur:
            if cur.right or cur.left:
                right.insert(0,cur.val)
                cur = cur.right if cur.right else cur.left
            else:
                break
        
        leaves = []
        
        def preOrder(root):
            if root.left== None and root.right == None:
                leaves.append(root.val)
                return
            if root.left:
                preOrder(root.left)
            if root.right:
                preOrder(root.right)
        
        if root.left or root.right:        
            preOrder(root)
        
        return [root.val] + left +leaves + right