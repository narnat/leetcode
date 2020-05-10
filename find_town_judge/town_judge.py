#!/usr/bin/env python3


def findJudge(N, trust):
    """ Naive way"""
    d = {}
    if not trust:
        return 1 if N == 1 else -1
    for i in trust:
        d.setdefault(i[1], 0)
        d[i[1]] += 1
    key = -1
    for k in d:
        if d[k] == N - 1:
            key = k
            break
    for i in trust:
        if key == i[0]:
            return -1

    return key


def findJudge_2(N, trust):
    """ Using two arrays """
    votes = [0] * (N + 1)
    voted = [0] * (N + 1)

    for i in trust:
        votes[i[1]] += 1
        voted[i[0]] += 1

    for i in range(1, N + 1):
        if votes[i] == N - 1 and voted[i] == 0:
            return i

    return -1


def findJudge_3(N, trust):
    """ One array which stores the vote balance"""
    vote_balance = [0] * (N + 1)

    for i in trust:
        vote_balance[i[1]] += 1
        vote_balance[i[0]] -= 1

    for i in range(1, N + 1):
        if vote_balance[i] == N - 1:
            return i

    return -1


if __name__ == '__main__':
    assert findJudge_3(4, [[1, 3], [1, 4], [2, 3], [2, 4], [4, 3]]) == 3
    assert findJudge_3(3, [[1, 2], [2, 3]]) == -1
