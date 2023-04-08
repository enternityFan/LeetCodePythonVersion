#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：多多施工队.py
@Author ：HuntingGame
@Date ：2023-03-30 16:08 
C'est la vie!!! enjoy ur day :D

多多国有n座城市，编号从1到n，多多国的首都设置在1号城市，城市间由n-1条道路连接，每条道路连接两座城市，保证城市之间可以互相联通。现在由于台风侵袭，多多国有一些道路毁坏了，多多国国王准备派出一些施工队，每只施工队都从首都出发，
并选定一个终点城市xi，施工队会按照最短路线到达城市xi，并修复沿途被毁坏的道路。为了节约成本，国王希望派出尽可能少的施工队，修复好全部的被毁道路。
'''


def isSameSet( a, b):
    if a not in nodes or b not in nodes:
        return
    return findFather(a) == findFather(b)


def findFather( cur):
    path = []
    while cur != parents[cur]:
        path.append(cur)
        cur = parents[cur]

    while path:
        parents[path.pop()] = cur
    return cur


def union( a, b):
    if a not in nodes or b not in nodes:
        return

    aHead = findFather(a)
    bHead = findFather(b)
    if aHead != bHead:
        aSize = sizeMap[aHead]
        bSize = sizeMap[bHead]
        big = aHead if aSize >= bSize else bHead
        small = bHead if aHead == big else aHead
        parents[small] = big
        sizeMap[big] = aSize + bSize
        sizeMap.pop(small)

n = eval(input())
nodes = dict()
parents = dict()
sizeMap = dict()
#初始化并查集
for i in range(1,n+1):
    nodes[i] = i
    parents[i] = i
    sizeMap[i] = 1

# 输入数据
for _ in range(n-1):
    nums = list(map(int, input().split()))
    if nums[2] == 0:
        union(nodes[nums[0]],nodes[nums[1]])
print(len(sizeMap) - 1)

# print(nodes)
# print(parents)
# print(sizeMap)


"""

4
1 2 0
2 3 1
2 4 1

"""
