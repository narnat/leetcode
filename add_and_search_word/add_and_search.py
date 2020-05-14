#!/usr/bin/env python3


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
        cur = self.root
        for c in word:
            idx = ord(c) - ord('a')
            if not cur.children[idx]:
                cur.children[idx] = Node()
            cur = cur.children[idx]
        cur.is_end = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        return self.search_rec(word, 0, self.root)

    def search_rec(self, word, n, node):
        if len(word) == n:
            return node.is_end
        if word[n] != '.':
            child = node.children[ord(word[n]) - ord('a')]
            return child and self.search_rec(word, n + 1, child)
        else:
            for child in node.children:
                if child:
                    if self.search_rec(word, n + 1, child):
                        return True

        return False


if __name__ == '__main__':
    trie = WordDictionary()
    w1, w2, w3 = "bad", "dad", "mad"
    trie.addWord("bcd")
    trie.addWord("bjk")
    trie.addWord(w3)
    print(trie.search("pad"))
    print(trie.search("bad"))
    print(trie.search(".ad"))
    print(trie.search("b.."))
    print(trie.search("b.k"))
