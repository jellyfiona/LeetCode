"""
1644. Lowest Common Ancestor of a Binary Tree II

https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-ii/

##############################

类似题型:


#################################
考点或思路:
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        time: 051922  
        [Approach_stack_dict] travese to find p and q, if any of them does not exist, return Null.
         during traverse, use a dict to record the parent-child relationship, and when we find p or q, we put the ancestors in to stack.
         then we compare the two stack ,to get LCA.
         time_O(2N+2H+H)---> (N), treavese twice make it 2*N, full up the stack make it 2*H, where H is the high of the tree, may be N at worst.
                      comparing the two stack make it H. so time_O would be 2N+2H+H.
        space_O(N+2H) parent-child relationship dict would need N , two stack will need 2*H.
        """
        pdict = {root:None}
        def preOrder(root,target,stack):
            if root.val == target.val:
                p = pdict[root]
                while p :
                    stack.insert(0,p)
                    p = pdict[p]
                stack.append(root)
                return
            if root.left:
                pdict[root.left] = root
                preOrder(root.left, target, stack)
            if root.right and stack == []:
                pdict[root.right] = root
                preOrder(root.right, target, stack)
        
        pstack = []
        qstack = []
        preOrder(root,p, pstack)
        preOrder(root,q, qstack)
        LCA = None
        # if not pstack or not qstack:
        #     return None
        for i in range(min(len(pstack), len(qstack))):
            if pstack[i] == qstack[i]:
                LCA = pstack[i]
            else:
                break
        return LCA
                
        