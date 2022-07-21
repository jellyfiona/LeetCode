

"""
445. Add Two Numbers II——M

https://leetcode.com/problems/add-two-numbers-ii/
#################################
考点或思路:
[solution: ]
Similar problems:
2. Add Two Numbers

"""
from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        time: 0721/2022 10:35--11:00
        [Approach] Since the last index of the linkedlist would be the ones place of a number, we can go through 
        it twce to solve the problem.
        First, we go throught each linkedlist, for each node in it, we add a attribute for it, we add a prePointer, which pointing to the pre node of it. meanwhile, we can get the last node of the linkedlist, which is also the once place of the number.
        Then, we start from the last node of each linkedlist, we add them and we track the carry of it.
        we can use the prePointer to get the next place node.and we continue do so till the hightes place.
        time_O(N+M) we go through each node twce. N= len(l1) M = len(l2)
        space_O(N+M) we need a new pointer for each node.
        """
        
        p1 = l1
        p1.pre = None
        
        while p1.next:
            p1.next.pre = p1
            p1 = p1.next
        
        p2 = l2
        p2.pre = None
        while p2.next:
            p2.next.pre = p2
            p2 = p2.next
        
        dummy = ListNode("d")
        carry = 0
        while p1 and p2:
            curVal = (p1.val + p2.val + carry) % 10
            carry = (p1.val + p2.val + carry) // 10
            node = ListNode(curVal,dummy.next)
            dummy.next = node
            p1 = p1.pre
            p2 = p2.pre
            
        while p1:
            curVal = (p1.val + carry) % 10
            carry = (p1.val + carry) // 10
            node = ListNode(curVal,dummy.next)
            dummy.next = node
            p1 = p1.pre
            
        while p2:
            curVal = (p2.val + carry) % 10
            carry = (p2.val + carry) // 10
            node = ListNode(curVal,dummy.next)
            dummy.next = node
            p2 = p2.pre
        if carry:
            node = ListNode(carry,dummy.next)
            dummy.next = node
        
        return dummy.next
            
            

            