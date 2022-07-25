"""
98. Validate Binary Search Tree_M

https://leetcode.com/problems/validate-binary-search-tree/

##############################

类似题型:
297. Serialize and Deserialize Binary Tree_M

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
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        time: 07/24/2022 9:00--
        [Approach] Since this is a problem about BST, for the children of each node, there is a left limit and a right limit of these children. we can store the limits in the parent node, and we can check its children. 
        We can traverse the tree in preOrder, as we traverse, we check each node to see if it if out of limits, 
        meanwhile we update the limits for the children node.
        time_O(N) we need go through the once.
        space_O(N) for each node, we need to parameters for lowerlimit and upper limit
        """
        
        if root == None:
            return True
        
        root.lower = float("-inf")
        root.upper = float("inf")
        
        def isBST(node):
            if node == None:
                return True
            
            if node.lower >= node.val or node.val >= node.upper:
                return False
                
            if node.left:
                node.left.lower = node.lower
                node.left.upper = node.val
                if isBST(node.left)== False:
                    return False
            if node.right:
                node.right.lower = node.val
                node.right.upper = node.upper
                if isBST(node.right) == False:
                    return False
            return True
        
        return isBST(root)
        
        
        
        