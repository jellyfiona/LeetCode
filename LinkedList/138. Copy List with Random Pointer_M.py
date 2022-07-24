
"""
138. Copy List with Random Pointer_M

https://leetcode.com/problems/copy-list-with-random-pointer/
#################################
考点或思路:
[solution: hashtable ]
Similar problems:


"""


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        """
        time: 07/22/2022 10:15---10:36
        [Approach][hash] Since the random pointer could point to any node in the list, 
        when wo do copy one by one, the random pointer may point to a node after the cur node,which have not been created yet. So we need to go through the list twce. The first time is to make copy of the list of nodes with val and next. Meanwhile keep a record of the random pointers of each node. The second time we go through the list, we add the random pointer to each node.
        time_O(N)
        space_O(N) need extra space for record the ramdom pointers.
        """
        if head == None:
            return None
                
        # key is the oreginal node, val is the copy node
        di = {}
        dummy= Node(100000)
        cur = dummy
        p = head
        while p :
            cur.next = Node(p.val)
            di[p] = cur.next
            cur = cur.next
            p = p.next
            
        p = head
        cur = dummy.next
        while p:
            if p.random:
                cur.random = di[p.random]
            else:
                cur.random = None
            cur = cur.next
            p = p.next
        return dummy.next
            
