"""
314. Binary Tree Vertical Order Traversal_M

https://leetcode.com/problems/binary-tree-vertical-order-traversal/

##############################

类似题型:


#################################
考点或思路:

"""
from types import List
import heapq
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        time: 052022 10:30---11:27
        [Approach] I think we need to go through the tree in preOrder, 
        And wo need to keep a heap, each element of the heap would be like (col, level, no.Of preOrder, cur.val)
        So the heap will help us to sort the node by their col. and then by their level, and then by their sequence in preOrder 
        Since we traverse the tree in preOrder, the element with same col and same level, their seq no. show  their order from left to right.
        After travarsal the tree, we pop from the heap, 
        Time_O(N) traversal the tree will need O(N), pop each element and operate on it, will need O(N).
        space_O(N) each node ,will need to add some info, and we need a heap with size of N to help us sort.
        """
        
        if root == None:
            return []
        
        heap = []
        self.seq = 0
        def preOrder(root, heap, col , level):
            heapq.heappush(heap, (col, level,self.seq, root.val))
            self.seq += 1
            if root.left:
                
                preOrder(root.left, heap, col-1,level+1)
                
            if root.right:
                preOrder(root.right , heap, col+1, level+1)
                
        preOrder(root, heap, 0,0)
        output = []
        while heap:
            curcol = heap[0][0]
            col = []
            while heap and heap[0][0] == curcol:
                col.append(heapq.heappop(heap)[-1])
            output.append(col)
            
        return output
            
        
                
            