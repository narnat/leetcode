#!/usr/bin/env python3


def floodFill(image, sr, sc, newColor):
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
    image = floodFill(image, 1, 1, 1)
    assert image == [[0, 0, 0], [0, 1, 1]]

    image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
    image = floodFill(image, 1, 1, 2)
    assert image == [[2, 2, 2], [2, 2, 0], [2, 0, 1]]
    print("All good!!!")
