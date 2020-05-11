#!/usr/bin/env python3


from collections import deque


def floodFill_bfs(image, sr, sc, newColor):

    color = image[sr][sc]
    l_r = len(image)
    l_c = len(image[0])

    if color == newColor:
        return image
    q = deque([(sr, sc)])
    while q:
        i, j = q.popleft()
        image[i][j] = newColor
        for k, l in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            if 0 <= i + k < l_r and 0 <= j + l < l_c and image[i + k][j + l] == color:
                q.append((i + k, j + l))
    return image


def floodFill_dfs(image, sr, sc, newColor):
    color = image[sr][sc]
    l_r = len(image)
    l_c = len(image[0])

    def fill(x, y):
        if 0 <= x < l_c and 0 <= y < l_r and image[y][x] == color:
            image[y][x] = newColor
            fill(x + 1, y)
            fill(x, y + 1)
            fill(x - 1, y)
            fill(x, y - 1)
    if color != newColor:
        fill(sc, sr)
    return image


if __name__ == '__main__':
    image = [[0, 0, 0], [0, 1, 1]]
    image = floodFill_bfs(image, 1, 1, 1)
    assert image == [[0, 0, 0], [0, 1, 1]]

    image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
    image = floodFill_bfs(image, 1, 1, 2)
    assert image == [[2, 2, 2], [2, 2, 0], [2, 0, 1]]
    print("All good!!!")
