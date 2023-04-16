#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：好树.py
@Author ：HuntingGame
@Date ：2023-04-12 10:35 
C'est la vie!!! enjoy ur day :D


我们定义，一棵树是好树当且仅当它的红色节点数量大于蓝色节点的数量。
现在给定一棵好树，你需要删除一条边，使得形成的两个子树均为好树。请你求出有多少种删边的方案。
输入描述
第一行输入一个正整数n，代表节点的数量。
第二行输入一个长度为n的，仅包含'R'和'B'两种字符的字符串，第;个字符为'R'代表第;个节点被染成红色，'B'代表被染成蓝色。保证'R'的数量大于'B'的数量。
接下来的n- 1行，每行输入两个正整数u和v，代表节点au和节点v有一条边连接。
1 ≤n ≤105

'''
import collections

from collections import defaultdict


def dfs(node, parent, reds, blues, graph, count):
    # 如果当前节点是红色的，红色节点数量加1，否则蓝色节点数量加1
    if colors[node] == 'R':
        reds += 1
    else:
        blues += 1

    # 更新当前节点子树中红色节点数量大于蓝色节点数量的方案数
    count[node] = reds - blues

    # 遍历当前节点的子节点
    for child in graph[node]:
        if child != parent:
            dfs(child, node, reds, blues, graph, count)


def countGoodSubtrees(n, colors, edges):
    # 构建图
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    # 计算每个节点子树中红色节点数量大于蓝色节点数量的方案数
    count = [0] * n
    dfs(0, -1, 0, 0, graph, count)

    # 统计删边的方案数
    result = 0
    for u, v in edges:
        if count[u] == count[v] == 0:
            # 如果删去这条边不影响任何节点子树的红蓝节点数量关系，方案数加1
            result += 1
        elif count[u] + count[v] == 0:
            # 如果删去这条边会使得连接的两个子树均为好树，方案数加1
            result += 1

    return result


# 测试代码
n = int(input())
colors = input().strip()
edges = []
for i in range(n - 1):
    u, v = map(int, input().split())
    edges.append((u - 1, v - 1))
print(countGoodSubtrees(n, colors, edges))

"""
3
RBR
1 2
2 3
"""


