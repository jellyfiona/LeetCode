"""
297. Serialize and Deserialize Binary Tree_M

https://leetcode.com/problems/serialize-and-deserialize-binary-tree/

##############################

类似题型:
449. Serialize and Deserialize BST_M

#################################
考点或思路:

"""
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

import json
class Codec:
    """
    time: 07/23/2022 3:15---
    [Approach] 
    this does not like BST, BST can be sort as it go with proOrder, 
    As a BT, it will has to be like the problem's input, give the data in level traversal order, and make sure None is included.
    So we can serialize a BT in level traversal.
    And we can deserialize it accordingly.
    Time_O(N)
    space_O(M) M是一个level最大多少个节点，应该是N/2
    """
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if root== None:
            return "[]"
        res = []
        # here we need a FIFO pipe, not a stack
        stack = [root]
        nextlevel = []
        while stack:
            curNode = stack[0]
            del stack[0]
            if curNode :
                res.append(curNode.val)
                stack.append(curNode.left)
                stack.append(curNode.right)
            else:
                res.append(None)
                    
        return json.dumps(res)


    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        lst = json.loads(data)
        if lst == []:
            return None
        
        root = TreeNode(lst[0])
        stack = [root]
        stackidx = 0
        for i in range((len(lst) -1 -1) //2):
            
            left = lst[i*2+1]
            right = lst[i*2+2]
            
            # [Notice!!] here , it has to be == None, we could be sure that the leftchild is none.
            # if left: In this condition, if left  is a node with val= 0, then we may wrongfully make it a None.
            if left == None:
                leftnode = None
            else:
                leftnode = TreeNode(left)
                stack.append(leftnode)
            if right==None :
                rightnode = None
            else:
                rightnode = TreeNode(right)
                stack.append(rightnode)
                
            if stackidx >= len(stack):
                print("Wrong!!!")
                break
            stack[stackidx].left = leftnode
            stack[stackidx].right = rightnode
            stackidx += 1
            
        return root
            
            

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))