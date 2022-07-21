"""
21. Merge Two Sorted Lists_E

https://leetcode.com/problems/merge-two-sorted-lists/
#################################
考点或思路:
[solution: two pointers ]
Similar problems:


"""



# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        time: 07212022  11:10--11:22
        [Approach][TwoPointer]
        Since the two lists has been sorted, it is easy for us to just go thourght them.
        time_O(N+M)
        Space_O(1) we do not need extra space.
        """
        if list1 == None:
            return list2
        elif list2 == None:
            return list1
        
        p1 = list1
        p2 = list2
        dummy = ListNode("d")
        cur = dummy
        while p1 and p2:
            if p1.val <= p2.val:
                cur.next = p1
                cur = cur.next
                p1 = p1.next
            else:
                cur.next = p2
                cur = cur.next
                p2 = p2.next
        if p1:
            cur.next = p1
        if p2:
            cur.next = p2
        return dummy.next
        