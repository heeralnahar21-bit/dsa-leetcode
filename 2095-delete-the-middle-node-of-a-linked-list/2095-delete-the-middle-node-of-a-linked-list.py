# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: ListNode | None) -> ListNode | None:
        if head.next is None:
            return None
        temp = head
        n = 0
        while temp:
            n += 1
            temp = temp.next
        temp = head
        for i in range(n // 2 - 1):
            temp = temp.next
        temp.next = temp.next.next
        return head
