"""
102. Binary Tree Level Order Traversal_M

https://leetcode.com/problems/binary-tree-level-order-traversal/

#################################
考点或思路:
[solution: tree: level treversal]
Similar problems:
1029. Binary Tree Level Order Traversal_M

"""

from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        time: 07/11/2022 10:30---
        [Approach][DFS][PreOrder] we can use DFS to traverse this tree,  meanwhile we keep a record of what we see.
        Time_O(N) we go through the tree only once.
        space_O(N)  we need to store the values of each node.
         """
        
        self.levelLst = []
        
        def rec(root, level):
            if root == None:
                return
            
            while level > len(self.levelLst) - 1:
                self.levelLst.append([])
            self.levelLst[level].append(root.val)
            
            rec(root.left, level+1)
            rec(root.right, level+1)
            
        rec(root,0)
        return self.levelLst

        
    def levelOrder_V1(self, root: Optional[TreeNode]) -> List[List[int]]:   
        """
        [DFS][PreOrder][stack] we can implement it with out recursion.
        """
        
        if root == None:
            return []
        
        self.levelLst = []
        # each stack stores all the node in the same level from left to right
        stack = [(root,0),]
        nextlevel = []
        while stack:
            for curNode, level in  stack:
                while level > len(self.levelLst) -1 :
                    self.levelLst.append([])

                self.levelLst[level].append(curNode.val)
                if curNode.left:
                    nextlevel.append((curNode.left, level+1))
                if curNode.right:
                    nextlevel.append((curNode.right, level+1))
            stack = nextlevel
            nextlevel = []
        
        return self.levelLst