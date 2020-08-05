#!/usr/bin/env python


class Node:
    def __init__(self):
        """
        Prefix tree node
        @children: child nodes
        """
        self.children = 26 * [None]
        self.is_end = False


class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node()

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        root = self.root

        for c in word:
            idx = ord(c) - ord('a')
            if root.children[idx] is None:
                root.children[idx] = Node()
            root = root.children[idx]
        root.is_end = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        return self.search_rec(word, 0, self.root)

    def search_rec(self, word, n, node):
        if node is None:
            return False
        if n == len(word):
            return node.is_end

        if word[n] == '.':
            for child in node.children:
                if self.search_rec(word, n + 1, child):
                    return True
        else:
            idx = ord(word[n]) - ord('a')
            if self.search_rec(word, n + 1, node.children[idx]):
                return True
        return False
