# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or  not head.next:
            return head
        n = 1
        tail = head
        while tail.next:
            tail = tail.next
            n += 1
        k = k % n
        if k == 0:
            return head

        tail.next = head
        newtail = head
        for i in range(n - k - 1):
            newtail = newtail.next
        newhead = newtail.next
        newtail.next = None
        return newhead
