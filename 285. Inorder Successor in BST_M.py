"""
285. Inorder Successor in BST

https://leetcode.com/problems/inorder-successor-in-bst/

##############################

类似题型:


#################################
考点或思路:
[DFS][BST]
"""
from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        """
        time: 052522  9:20--10:14
        [approach] First we need to traverse the tree to find the p node,
        if p has a right child, the inorder successor would be the left most node of the rightsubtree;
        if p is a left child, the inorder successor of it would be its parentnode.
        if p is a right child, we should look for its parent, if the parent is a right child ;
        keep looking up for a parentnode who itself is a leftchild, this parent's parent should be the inorder succesor.
        time_O(H) traverse to find p, since it is a BST, we go with DFS,  we need O(H) to find p,
                    meanwhile keep a dict for the parent-child relationship.
                    when we find p, we trace back in the dict to find the inorder successor. 
                    The trace may take O(H) where H is the height of the tree.
        space_O(H):  keep a dict for the parent-child relationship.
        """
        parentDict = {root: None}
        
        cur = root
        while cur:
            if cur.val == p.val:
                break
            elif cur.val < p.val and cur.right:
                parentDict[cur.right] = cur
                cur = cur.right
            elif cur.val > p.val and cur.left:
                parentDict[cur.left] = cur
                cur = cur.left
            else:
                cur = None
        
        # we could not find p 
        if cur == None:
            return None
        
        # if p has a right child, find the left most node in right subtree
        if cur.right:
            sub = cur.right
            while sub.left:
                sub = sub.left
            return sub
        
        # if p is the root, and it has no right child, return None
        if parentDict[p] == None:
            return None
        
        # if p is a left child, the inorder successor of it would be its parentnode.
        if parentDict[p].left == p:
            return parentDict[p]
        
        # if p is a right child,looking up for a parentnode who itself is a leftchild, this parent's parent should be the inorder succesor.
        while parentDict[p] and parentDict[p].right == p:
            p = parentDict[p]
        # out of the while loop, maybe p reach to root, maybe p is a leftchild , either way we could return parentDict[p]
        return parentDict[p]
        
                