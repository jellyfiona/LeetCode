"""
449. Serialize and Deserialize BST_M

https://leetcode.com/problems/serialize-and-deserialize-bst/

##############################

类似题型:
297. Serialize and Deserialize Binary Tree_M

#################################
考点或思路:

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
import json
class Codec:
    """
    time: 07/23/2022 2:35--3:10
    [Approach] The easiest way is to make the BST into a list by PreOrder traverse, 
    and then make the list into a string.
    time_O(N)
    space_O(1) No extra space needed.
    """
    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """
        if root== None:
            return "[]"
        res = []
        def preOrder(root,lst):
            lst.append(root.val)
            if root.left:
                preOrder(root.left,lst)
            if root.right:
                preOrder(root.right,lst)
        
        preOrder(root,res)
        s = json.dumps(res)
        print(s)
        return s
        

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        lst = json.loads(data)
        print(lst)
        
        
        def maketree(lst):
            if lst == []:
                return None
            rootval = lst[0]
            rightstart = len(lst)
            for i in range(1,len(lst)):
                if lst[i]>rootval:
                    rightstart = i
                    break
            root = TreeNode(rootval)
            root.left = maketree(lst[1:rightstart])
            root.right = maketree(lst[rightstart:])
            return root
        
                
        tree = maketree(lst)
        return tree
            
# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans