"""
1485. Clone Binary Tree With Random Pointer_M

https://leetcode.com/problems/clone-binary-tree-with-random-pointer/
#################################
考点或思路:
[solution: hashtable ]
Similar problems:
138. Copy List with Random Pointer_M   https://leetcode.com/problems/copy-list-with-random-pointer/

"""

# Definition for Node.
class NodeCopy:
    def __init__(self, val=0, left=None, right=None, random=None):
        self.val = val
        self.left = left
        self.right = right
        self.random = random

""" 看这里，其实系统中有一个而这样命名的Node，但是leetcode给我的也是 class Node, 这导致我跟本没法debug，没有得到正确的信息，也没法debug，浪费太多时间。其实我的逻辑是对的
from lib2to3.pytree import Node
"""

class Solution:
    def copyRandomBinaryTree(self, root: 'Optional[NodeCopy]') -> 'Optional[NodeCopy]':
        """
        time: 07/22/2022 10:51--
        [Approach][hashtable] we traverse the tree with preorder, and we keep a record of the connection between each node and each copynode.
        After the entire tree been built, we traverse again, this time we add the random pointer to each node.
        time_O(N) traverse twice.
        space_O(N) extra space for the connection between each node and each copynode.
        """

        if root == None:
            return None
        
        di = {}
        
        def copynode(oldNode):
            newNode = NodeCopy(oldNode.val)
            di[oldNode] = newNode
            if oldNode.left:
                newNode.left = copynode(oldNode.left)
            if oldNode.right:
                newNode.right = copynode(oldNode.right)
            return newNode
        
        newroot = copynode(root)
        
        # second traverse, add random pointer
        def addRandom(oldNode, newNode):
            if oldNode.random:
                newNode.random = di[oldNode.random]
            if oldNode.left:
                addRandom(oldNode.left, newNode.left)
            if oldNode.right:
                addRandom(oldNode.right, newNode.right)
        
        addRandom(root,newroot)
        return newroot


# import unittest
# class TestcaseS(unittest.TestCase):
#     def setUp(self):
#         self.obj = Solution()
#         self.f = self.obj.copyRandomBinaryTree

#     def testcase_1(self):
#         # alist = NodeCopy(1)
#         # alist.left = None
#         # alist.right = NodeCopy(4)

#         # alist.right.left = NodeCopy(7,random = alist)
#         # alist.right.random = alist.right.left

#         # ret = self.f(alist)
#         # print(ret.val)


# if __name__ == '__main__':
#     unittest.main(argv=['first-arg-is-ignored'], exit=False)