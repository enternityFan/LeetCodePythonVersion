#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：6378. 最小化旅行的价格总和.py
@Author ：HuntingGame
@Date ：2023-04-16 10:56 
C'est la vie!!! enjoy ur day :D
'''
from collections import defaultdict
from typing import List


class Solution:
    def minimumTotalPrice(self, n: int, edges: List[List[int]], price: List[int], trips: List[List[int]]) -> int:
        # 构建树的邻接表
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # DFS 找到所有的路径
        paths = []
        def dfs(node, path, cost):
            if node == path[-1]:
                paths.append((path, cost))
                return
            if len(path) == n:
                return
            for child in graph[node]:
                if child not in path:
                    dfs(child, path + [child], cost + price[child])

        for start, end in trips:
            dfs(start, [start], price[start])

        # DP 计算所有旅行的最小价格总和
        memo = [[float('inf')] * 2 for _ in range(n)]
        for i in range(n):
            memo[i][0] = price[i]
        for path, cost in paths:
            for i in range(1, len(path)):
                u, v = path[i-1], path[i]
                for j in range(2):
                    memo[v][j] = min(memo[v][j], memo[u][j] + cost)
                    if j == 0:
                        memo[v][1] = min(memo[v][1], memo[u][0] + cost // 2)

        return memo[trips[-1][1]][1]


n = 4
edges = [[0,1],[1,2],[1,3]]
price = [2,2,10,6]
trips = [[0,3],[2,1],[2,3]]
print(Solution().minimumTotalPrice(4,edges,price,trips))