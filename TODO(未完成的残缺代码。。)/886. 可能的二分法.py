#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/10/16 9:21
# @Author  : HuntingGame
# @FileName: 886. 可能的二分法.py
# @Software: PyCharm
# C'est la vie. Enjoy ur day ! :D
from typing import List


class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        g = [[] for _ in range(n)]
        for x,y in dislikes:
            g[x-1].append(y-1)
            g[y-1].append(x-1)
        color = [0] * n # color[x] = 0 表示未访问节点x

         def dfs(x:int,c:int) -> bool:
            color[x] = c
            return all(color[y] !=c and (color[y] or dfs(y,-c)) for y in g[x])

n = 3
dislikes = [[1,2],[1,3],[2,3]]

n = 5
dislikes = [[1,2],[2,3],[3,4],[4,5],[1,5]]
print(Solution().possibleBipartition(n,dislikes))
print(Solution().possibleBipartition(4,[[1,2],[1,3],[2,4]]))