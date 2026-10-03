# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(
        self, list1: ListNode | None, list2: ListNode | None
    ) -> ListNode | None:
        t1 = list1
        t2 = list2
        dnode = ListNode(-1)
        temp = dnode
        while t1 != None and t2 != None:
            if t1.val <= t2.val:
                temp.next = t1
                t1 = t1.next
            else:
                temp.next = t2
                t2 = t2.next
            temp = temp.next
        temp.next = t1 if t1 else t2
        return dnode.next
