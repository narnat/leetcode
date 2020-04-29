#!/usr/bin/env python3

class Node:

    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

class FirstUnique:

    def __init__(self, nums: List[int]):
        self.d = {}
        self.head = self.tail = None
        for i in nums:
            self.add(i)

    def showFirstUnique(self) -> int:
        if self.head:
            return self.head.val
        return -1

    def add(self, value: int) -> None:
        if value in self.d:
            if self.d[value]:
                self.delete(self.d[value])
                self.d[value] = None
        else:
            node = Node(value)
            self.d[value] = node
            if self.head == None:
                self.tail = self.head = node
            else:
                self.tail.next = node
                node.prev = self.tail
                self.tail = node

    def delete(self, node):
        if not node.prev:
            self.head = self.head.next
        else:
            node.prev.next = node.next

        if not node.next:
            self.tail = self.tail.prev
        else:
            node.next.prev = node.prev





# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)
