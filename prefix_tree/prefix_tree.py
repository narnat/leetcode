#!/usr/bin/env python3


class Node:
    def __init__(self):
        """
        Node for prefix tree
        """
        self.children = [None] * 26
        self.is_end = False


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        cur = self.root
        for c in word:
            idx = ord(c) - ord('a')
            if not cur.children[idx]:
                cur.children[idx] = Node()
            cur = cur.children[idx]
        cur.is_end = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        cur = self.root
        for c in word:
            idx = ord(c) - ord('a')
            if not cur.children[idx]:
                return False
            cur = cur.children[idx]
        return cur and cur.is_end

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        cur = self.root
        for c in prefix:
            idx = ord(c) - ord('a')
            if not cur.children[idx]:
                return False
            cur = cur.children[idx]
        return True


if __name__ == '__main__':
    word = "apple"
    word1 = "app"
    trie = Trie()
    trie.insert(word)
    print(trie.search(word))
    print(trie.search(word1))
    print(trie.startsWith(word1))
    trie.insert(word1)
    print(trie.search(word1))
