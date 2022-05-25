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
    def goodNodes(self, root: TreeNode) -> int:
        """
        time: 052422  2:05--2:35
        [Approach] Apparently we need to traverse the entire tree, to check for all the nodes.
        And since we need to know the val of the root sooner than the val of the child, 
        we need to traverse in preorder.
        And we need a stack to store the val in the path. 
        ---stack: what to push in? the val on the path and the maxval so far
                  when to push in? preOrder to a new node, we push in the (cur.val ,maxval )
                  when to pop out? after visit the childnodes of this node, we do not need this node's val, 
                                    so  we pop it out.
        Time_O(N) where N is the number of node.
        Space_O(H) where H is the height of the tree.
        """
        
        self.stack = []
        self.cnt = 1 # root will always be a good node
        
        def preOrder(root):
            if self.stack and self.stack[-1][1] <= root.val:
                self.cnt += 1
            self.stack.append( (root.val, max(root.val, self.stack[-1][1]) if self.stack else root.val   )   )
        
            if root.left:
                preOrder(root.left)
            if root.right:
                preOrder(root.right)
            self.stack.pop()
            
        preOrder(root)
        return self.cnt