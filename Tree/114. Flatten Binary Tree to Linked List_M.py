
"""
114. Flatten Binary Tree to Linked List_M

https://leetcode.com/problems/flatten-binary-tree-to-linked-list/

##############################

类似题型:


#################################
考点或思路:
[Tree][DFS]

"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        """
        time: 07/27/2022 10:10--10:36
        [Approach][DFS] This is more of a logic thinking problem.
        for each node, there a 4 different situations need to be dicuss, for all node are the same.
        So we can use DFS to do it recursively.
        and when we straight a subtree out into a linkedlist, we need to return the lastnode if the list,
        for later use, we may need add linkedlist to the tailnode of it.
        Time_O(N) we visit each node once.
        space_O(1) no extra space is needed, since we modify the node in-place.
        """
        
        # this func return a non-none tailnode as the last node in the linkedlist
        def flattenNode(root):
            if root.left == None and root.right == None:
                return root
            elif root.left and root.right == None:
                root.right = root.left
                root.left = None
                return flattenNode(root.right)
            elif root.left == None and root.right:
                return flattenNode(root.right)
            else:
                lefttail = flattenNode(root.left)
                righttail = flattenNode(root.right)
                
                lefttail.right = root.right
                root.right = root.left
                root.left = None
                return righttail
        if root == None:
            return None
        
        flattenNode(root)
        