#!/usr/bin/env python3
from typing import List
from collections import deque


class Trie_Node:
    '''
    Trie node
    '''
    def __init__(self):
        self.children = [None] * 26
        self.end = False


class Trie:
    '''
    Trie class
    '''
    def __init__(self):
        self.root = Trie_Node()

    def add(self, word):
        node = self.root
        for c in word:
            idx = ord(c) - ord('a')
            if node.children[idx] is None:
                node.children[idx] = Trie_Node()
            node = node.children[idx]
        node.end = True


class StreamChecker:
    '''
    Stream checker, puts words in reverse order in Trie
    and stores the whole stream in reverse
    '''
    def __init__(self, words: List[str]):
        self.trie = Trie()
        self.stream = deque()
        for word in words:
            self.trie.add(word[::-1])

    def query(self, letter: str) -> bool:
        self.stream.appendleft(letter)
        trie = self.trie.root
        for c in self.stream:
            idx = ord(c) - ord('a')
            if trie.children[idx]:
                trie = trie.children[idx]
                if trie.end:
                    return True
            else:
                break
        return False
