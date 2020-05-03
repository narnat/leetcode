#!/usr/bin/env python3


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    """ Regular recursive solution"""
    def sortList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head

        mid = self.middleNode(head)
        middle = mid.next
        mid.next = None

        left = self.sortList(head)
        right = self.sortList(middle)

        return self.mergeTwoLists(left, right)

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode()
        cur = head
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        cur.next = l1 or l2
        return head.next

    def middleNode(self, head: ListNode) -> ListNode:
        slow = fast = prev = head
        while fast and fast.next:
            fast = fast.next.next
            prev = slow
            slow = slow.next

        return prev

class Solution_2:
    """ Bottom up, no recursion solution"""
    def sortList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head

        def length(head):
            count = 0
            while head:
                count += 1
                head = head.next
            return count

        def split(head, step):
            i = 1
            while i < step and head:
                head = head.next
                i += 1
            if not head: return None
            middle, head.next = head.next, None
            return middle

        def mergeTwoLists(l1: ListNode, l2: ListNode, root: ListNode) -> ListNode:
            head = root
            cur = head
            while l1 and l2:
                if l1.val < l2.val:
                    cur.next = l1
                    l1 = l1.next
                else:
                    cur.next = l2
                    l2 = l2.next
                cur = cur.next
            cur.next = l1 or l2
            while cur.next: cur = cur.next
            return cur # Returns the last node

        size = length(head)
        step = 1
        dummy = ListNode()
        dummy.next = head
        tail = l = r = None

        while step < size:
            cur = dummy.next
            print(cur.val)
            tail = dummy
            while cur:
                l = cur
                r = split(l, step)
                cur = split(r, step)
                tail = mergeTwoLists(l, r, tail)
            step *= 2

        return dummy.next
