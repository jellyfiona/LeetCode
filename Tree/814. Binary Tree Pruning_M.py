"""
814. Binary Tree Pruning_M

https://leetcode.com/problems/binary-tree-pruning/
##############################

类似题型:


#################################
考点或思路:

"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        time : 09062022 10:35---10:54
        [Approach][ postOrder Travise ]
        Since any subtree not containing a "1" will be delete, we should check child node first, then check parent node.
        So, we should travise the tree in postOrder.
        When we see a leave node whose val is "0", we delete it; after we check the children node, if there is(are) child(ren) node
        with "1" , the node will stay; so for the parent node, if it has child, it cannot be deleted; if it has no child, then we check its onw val.
        time_O(N) we travise the tree only once.
        space_O(1) for each node ,we need its parent to know , how many child this node has. so we need a record of number of children.
        """
        
        if root == None:
            return root
        
        def postOrder(root):
            root.childnum = 0
            
            if root.left:
                root.childnum += 1
                postOrder(root.left)
                if root.left.val == 0 and root.left.childnum == 0:
                    root.left = None
                    root.childnum -= 1
            if root.right:
                root.childnum += 1
                postOrder(root.right)
                if root.right.val == 0 and root.right.childnum == 0:
                    root.right = None
                    root.childnum -= 1
            
        postOrder(root)
        
        if root.val == 0 and root.childnum == 0:
            return None
        
        return root
            
        