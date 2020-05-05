#!/usr/bin/env


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def insertionSortList(self, head):
        """ Creating dummy node and discarding it, this code cannot insert a node to the beginning"""
        if not head:
            return head

        prev = new_list = ListNode()
        cur = head
        while cur:
            saved_next = cur.next
            while prev.next and prev.next.val < cur.val:
                prev = prev.next
            cur.next = prev.next
            prev.next = cur
            prev = new_list
            cur = saved_next

        return new_list.next



class Solution_2:
    """ Simple approach, can insert to the beginning, middle and end"""
    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head: return head

        newList = head
        cur = head.next
        newList.next = None

        while cur:
            node = cur
            cur = cur.next
            node.next = None
            temp = newList
            prev = temp
            while temp:
                if temp.val > node.val:
                    if temp is prev:
                        node.next = temp
                        newList = node
                    else:
                        prev.next = node
                        node.next = temp
                    break
                if not temp.next:
                    temp.next = node
                    break
                prev = temp
                temp = temp.next

        return newList
