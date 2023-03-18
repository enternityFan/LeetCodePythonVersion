#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：小妹刷怪2.py
@Author ：HuntingGame
@Date ：2023-03-18 11:05 
C'est la vie!!! enjoy ur day :D
'''

inp = input().split()
n, A, B = int(inp[0]), int(inp[1]), int(inp[2])

a = [[0 for j in range(1001)] for i in range(1001)]
s = [[0 for j in range(1001)] for i in range(1001)]

for i in range(n):
    inp = input().split()
    for j in range(m):
        a[i + 1][j + 1] = int(inp[j])
        s[i + 1][j + 1] = s[i][j + 1] + s[i + 1][j] - s[i][j] + a[i + 1][j + 1]

for n in range(q):
    inp = input().split()
    x1, y1, x2, y2 = int(inp[0]), int(inp[1]), int(inp[2]), int(inp[3])
    print(s[x2][y2] - s[x1 - 1][y2] - s[x2][y1 - 1] + s[x1 - 1][y1 - 1])