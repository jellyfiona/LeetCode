"""
23. Merge k Sorted Lists
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
Merge all the linked-lists into one sorted linked-list and return it.
##############################

类似题型：


#################################
考点或思路：

"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


import heapq
class Solution:
    def mergeKLists(self, lists) -> ListNode:
        """
        input:lists: List[ListNode]
        output:-> -> ListNode
        【思路】[heapq]
        这里有k个list，已经排序好了，那么我们可以每次从这些list中各取一个，放入到heapq中，heapq自动帮我们排序，
        然后再pop出来，链接到ret的LList上。
        每次pop出的node在哪个原Llist上，就从这个Llist上再取一个（也就是这个node的next）放入到heapq中。
        
        """
        # 这里是给LinkedList打个补丁，因为本身LinkedList已经被定义好了，我这里不能重新定义，
        # 不能直接在class定义的地方加__lt__，所以这里打补丁。
        def com_list_node(a,b):
            return a.val < b.val
        ListNode.__lt__ = com_list_node
        
        
        retlistDummy = ListNode()
        cur = retlistDummy
        heap = []
        # 起始，把每个list的第一个node放进去，heapq自动排序
        for node in lists:
            if node:
                heapq.heappush(heap,node)

        while heap:
            cur.next = heapq.heappop(heap)
            cur = cur.next
            # 如果这个node后边还有node，则pushin，
            if cur and cur.next:
                heapq.heappush(heap, cur.next)
        
        n = retlistDummy.next
        while n :
            print(n.val, end=" / ")
            n = n.next  

        return retlistDummy.next



import unittest
class TestcaseS(unittest.TestCase):
    def setUp(self):
        self.obj = Solution()
        self.f = self.obj.mergeKLists

    def testcase_1(self):
        alist = ListNode(1)
        alist.next = ListNode(4)
        alist.next.next = ListNode(5)

        blist = ListNode(1)
        blist.next = ListNode(3)
        blist.next.next = ListNode(4)
        clist = ListNode(2)
        clist.next = ListNode(6)

        ret = self.f([alist, blist,clist])
        # self.assertEqual(ret,8)

    def testcase_2(self):
        ret = self.f([[], []])

    # def testcase_V1(self):
    #     self.f = self.obj.f
    #     self.testcase_1()
    #     self.testcase_2()

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)