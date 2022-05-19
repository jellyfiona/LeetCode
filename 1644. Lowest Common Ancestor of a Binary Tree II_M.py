"""
235. Lowest Common Ancestor of a Binary Search Tree_E

https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-iii/

##############################

类似题型:


#################################
考点或思路:

"""


# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None


class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        """
        [Approach] Notice that we dont have the tree ,we have the two node, and we could backtrace their ancestors by using the parentPointer.
        So we can back trace the ancestors and put them in stack. and compare the two stacks.
        time_O(2H)  Back trace to the root of the tree twice, will need 2H where H is the high of the tree. and Compare the two stacks, need (H)
        space_O(2H) store the ancestors for each node.
        """
        pstack = [p]
        qstack = [q]
        cur = p
        while cur.parent:
            pstack.insert(0,cur.parent)
            cur = cur.parent
        cur = q
        while cur.parent:
            qstack.insert(0,cur.parent)
            cur = cur.parent      
        LCA = None
        for i in range(min(len(pstack), len(qstack))):
            if pstack[i] == qstack[i]:
                LCA = pstack[i]
            else:
                break
        
        return LCA
    
    def lowestCommonAncestor_V2(self, p: 'Node', q: 'Node') -> 'Node':
        """
        [Approach] we move p or q up towards the root of the tree. and we keep a record of what node we have visited.
        If we go to a node, this node is new to us, add it in visited set. else if this node is already in the visited set,
        that means this node is LCA.
        time_O(H) we go up the tree, the maximum step is the height of the tree. In this case ,the worst would be N/2.
        space_O(N) the worst case is store all the node in this tree and finally get the root as LCA.
        """
        visited = set()
        while p or q:
            if p :
                if p in visited:
                    return p
                visited.add(p)
                p = p.parent
            if q:
                if q in visited:
                    return q
                visited.add(q)
                q = q.parent
                
        