#!/usr/bin/env python3
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        return self.dfs(s, wordDict, {})

    def dfs(self, s, wordDict, memo):
        if not s:
            return []
        if s in memo:
            return memo[s]
        res = []
        for word in wordDict:
            print(s, memo)
            if s.startswith(word):
                if len(s) == len(word):
                    res.append(s)
                else:
                    ret = self.dfs(s[len(word):], wordDict, memo)
                    for el in ret:
                        res.append(word + ' ' + el)
        memo[s] = res
        return res


class Solution_2:
    ''' Regular backtracking, results in TLE '''

    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        words = set(wordDict)
        output = []
        n = len(s)

        def dfs(s, i, ans):
            if i == n - 1:
                output.append(ans[:])
                return
            for j in range(i + 1, n):
                if s[i + 1: j + 1] in words:
                    ans.append(s[i+1:j+1])
#                     print(s[i + 1 : j + 1])
                    dfs(s, j, ans)
                    ans.pop()

        dfs(s, -1, [])
        return [" ".join(i) for i in output]
