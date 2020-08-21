#!/usr/bin/env python3

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    '''
    Use 3 steps:
    a) Get the middle of the list
    b) Disconnect middle from first half and reverse second half
    c) Merge two lists
    '''
    def reorderList(self, head: ListNode) -> None:
        if not (head and head.next and head.next.next):
            return head

        def reverse(head: ListNode) -> None:
            prev = None
            while head:
                tmp = head
                head = head.next
                tmp.next = prev
                prev = tmp
            return prev

        prev, slow, fast = head, head, head
        count = 0
        while fast and fast.next:
            count += 1
            prev = slow
            slow = slow.next
            fast = fast.next.next
        prev.next = None
        rev = reverse(slow)

        while count:
            count -= 1
            tmp = head
            head = head.next
            tmp.next = rev
            tmp = rev
            rev = rev.next
            tmp.next = head
        if rev:
            tmp.next = rev
