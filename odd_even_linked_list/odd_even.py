#!/usr/bin/env python3


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head):

        if not head or not head.next:
            return head
        odd = head
        even_head = even = head.next

        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        odd.next = even_head
        return head

    def oddEvenList_1(self, head):

        if not head or not head.next:
            return head

        odd = head
        even_head = even = head.next
        cur = head.next.next

        while cur:
            odd.next = cur
            odd = cur
            even.next = cur.next
            even = cur.next
            cur = cur.next and cur.next.next or None
        odd.next = even_head
        return head
