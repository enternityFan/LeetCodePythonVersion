#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：1971. 寻找图中是否存在路径.py
@Author ：HuntingGame
@Date ：2023-02-13 10:58 
C'est la vie!!! enjoy ur day :D
'''
import collections
from typing import List


class Solution:

    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        def dfs(i):
            if i == destination:
                return True
            vis.add(i)
            for j in g[i]:
                if j not in vis and dfs(j):
                    return True
            return False

        g = collections.defaultdict(list)
        for a,b in edges:
            g[a].append(b)
            g[b].append(a)
        vis = set()
        return dfs(source)



print(Solution().validPath(3,[[0,1],[1,2],[2,0]],0,2))