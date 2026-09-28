# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self, head):
        prev = None
        curr = head

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev

    def addTwoNumbers(
        self, l1: ListNode | None, l2: ListNode | None
    ) -> ListNode | None:

        l1 = self.reverse(l1)
        l2 = self.reverse(l2)
        carry = 0
        ans = None
        while l1 or l2 or carry:
            a = l1.val if l1 else 0
            b = l2.val if l2 else 0
            total = a + b + carry
            carry = total // 10
            digit = total % 10

            new = ListNode(digit)
            new.next = ans
            ans = new
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return ans
