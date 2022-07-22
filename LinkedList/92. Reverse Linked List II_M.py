"""
92. Reverse Linked List II——M

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
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        """
        time: 07/21/2022 4:22--
        [Approach] we can use hash to help us.
        time_O(N) we go through the linkedlist for one time.
        space_O(M) M = right - left.  We need space for a dict for the node and the index.
        """
        
        if left == right:
            return head
        
        i = 0
        p = head
        mid = (right +left )/2
        di = {}
        
        while p:
            i += 1
            if i >right:
                break
                
            if  left <= i <= right:
                di[i] = p
            
            if i > mid :
                # swap
                di[mid-(i-mid)].val, p.val = p.val , di[mid-(i-mid)].val
            p = p.next
            
        return head
        