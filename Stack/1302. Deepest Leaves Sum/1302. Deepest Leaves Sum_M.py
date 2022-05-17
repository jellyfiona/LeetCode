"""
1302. Deepest Leaves Sum_M
https://leetcode.com/problems/deepest-leaves-sum/

##############################

类似题型:


#################################
考点或思路:

"""
from typing import List

from collections import defaultdict

#Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def deepestLeavesSum_V1(self, root) -> int:
        """
        time: 051522 
        [Approach——DFS]因为刚刚做过给一个普通二叉树tree的各个节点找右侧node（117），
        这个题有点像那个题，找到所有节点的右侧node之后，再找最左侧leef，然后一个一个向右取值。
        ---这个解法感觉不够优化，因为你不知道最后的level的第一个叶子节点在哪里，就算给每个节点都搞了一个next，
        还是需要找到最后的level，的第一个节点。如果一定要这样，就在遍历的时候，还需要标记一下每个node的level，
        只要遇到更底层的点，就记录下来
        time_O(N) 找出nextNode的时候，要每个节点过一遍。
        space_O(N) 每个节点增加一个next指针。
        """
        if root == None:
            return root
        
        self.firstLeaf = root
        parentDi = {root:None,}
        def setNext(root,level):
            # set a next pointer for each input node, pointing to the node right to the input node on the same level
            root.next = None # None is default
            root.level = level
            # 因为同一行，先访问右孩子，所以遇到同level的，就要更新，
            if  root.level >= self.firstLeaf.level :
                self.firstLeaf = root
            p = parentDi[root]
            if p:
                if root == p.left and p.right:
                    root.next = p.right
                else:
                    # find the one on the right side of it
                    while p and p.next == None:
                        p = parentDi[p]
                    # if not p:# 找到头了也没有，只能结束了
                    #     break
                    if p and p.next:
                        while p.next and p.next.left==None and p.next.right == None:
                            p = p.next
                        if p.next and (p.next.left or p.next.right):
                            root.next = p.next.left if p.next.left else p.next.right
            
            # 递归时先找右孩子，因为左孩子的next依赖右孩子的next。
            if root.right:
                parentDi[root.right] = root
                setNext(root.right,level+1)
            if root.left:
                parentDi[root.left] = root
                setNext(root.left,level+1)
                
        setNext(root,0)
        
        cur = self.firstLeaf
        output = 0
        while cur:
            output += cur.val
            cur = cur.next
            
        return output


    def deepestLeavesSum_V2(self, root) -> int:
        """
        [Approach_2--Dict] We can go through the tree in any order, and record the level and the val for each node in Dict or in stack.
        Then we find the highest level in Dict or Stack, sum up the vals.
        Time_O(N)： Go through the tree once, it is O(N); check the record in Dict or stack for highest level, it is O(N) at most.
        space_O(N): store level and val for each node, so it will cost space_O(N).
        """
        nodeDict = defaultdict(list)
        
        def dfsTree(root,level):
            nodeDict[level].append(root.val)
            if root.left:
                dfsTree(root.left,level+1)
            if root.right:
                dfsTree(root.right, level+1)
            return

        dfsTree(root,0)
        
        level = max(nodeDict.keys())
        return sum(nodeDict[level])
        