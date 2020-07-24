#!/usr/bin/env python3


class Node:
    def __init__(self, val=0, min_val=float('inf')):
        self.val = val
        self.next = None
        self.min = min_val


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.head = None

    def push(self, x: int) -> None:
        if self.head is None:
            self.head = Node(x, x)
        else:
            node = Node(x, min(x, self.head.min))
            node.next = self.head
            self.head = node

    def pop(self) -> None:
        if self.head:
            self.head = self.head.next

    def top(self) -> int:
        if self.head:
            return self.head.val

    def getMin(self) -> int:
        if self.head:
            return self.head.min
