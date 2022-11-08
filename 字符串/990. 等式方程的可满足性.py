#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：990. 等式方程的可满足性.py
@Author ：HuntingGame
@Date ：2022-11-07 9:13 
C'est la vie!!! enjoy ur day :D
'''
from typing import List


class Solution:
    def __init__(self):
        self.nodes = dict()
        self.parents = dict()
        self.sizeMap = dict()
    def equationsPossible(self, equations: List[str]) -> bool:


        ans = True

        for i in range(len(equations)):

            self.nodes[equations[i][0]] = equations[i][0]
            self.parents[equations[i][0]] = equations[i][0]
            self.sizeMap[equations[i][0]] = 1

            self.nodes[equations[i][-1]] = equations[i][-1]
            self.parents[equations[i][-1]] = equations[i][-1]
            self.sizeMap[equations[i][-1]] = 1

        for i in range(len(equations)):
            if equations[i][1] == "=":
                self.union(equations[i][0],equations[i][-1])
        for i in range(len(equations)):
            if equations[i][1] == "!":
                if self.isSameSet(equations[i][0],equations[i][-1]):
                    return False

        return True


    def findFather(self, cur):
        path = []
        while cur != self.parents[cur]:
            path.append(cur)
            cur = self.parents[cur]

        # cur当前为头结点
        while path:
            self.parents[path.pop()] = cur  # 做了一个扁平的优化的操作

        return cur

    def isSameSet(self, a, b):
        if a not in self.nodes or b not in self.nodes:
            return False

        return self.findFather(self.nodes[a]) == self.findFather(self.nodes[b])

    def union(self, a, b):
        if a not in self.nodes or b not in self.nodes:
            return

        aHead = self.findFather(a)
        bHead = self.findFather(b)
        if aHead != bHead:
            aSetSize = self.sizeMap[aHead]
            bSetSize = self.sizeMap[bHead]
            big = aHead if aSetSize >= bSetSize else bHead
            small = bHead if big == aHead else aHead
            self.parents[small] = big
            self.sizeMap[big] = aSetSize + bSetSize
            self.sizeMap.pop(small)





print(Solution().equationsPossible(["a==b","b!=c","c==a"]))