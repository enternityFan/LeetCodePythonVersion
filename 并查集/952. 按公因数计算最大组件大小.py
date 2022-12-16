#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：952. 按公因数计算最大组件大小.py
@Author ：HuntingGame
@Date ：2022-12-16 12:21 
C'est la vie!!! enjoy ur day :D
'''
from typing import List


class Solution:
    def __init__(self):
        self.nodes = dict()
        self.parents = dict()
        self.sizeMap = dict()

    def largestComponentSize(self, nums: List[int]) -> int:

        n = len(nums)
        fatorMap = dict()
        for i in range(n):
            self.nodes[i] = i
            self.parents[i] = i
            self.sizeMap[i] = 1
        for i in range(n):
            num = nums[i]
            limit = int(num ** 0.5)
            for j in range(1,limit+1):
                if num % j == 0:
                    if j !=1:
                        if j not in fatorMap:
                            fatorMap[j] = i
                        else:
                            self.union(fatorMap[j],i)
                    other = num // j
                    if other !=1:
                        if other not in fatorMap:
                            fatorMap[other] = i
                        else:
                            self.union(fatorMap[other],i)


        return max(self.sizeMap.values())




    def isSameSet(self, a, b):
        if a not in self.nodes or b not in self.nodes:
            return
        return self.findFather(a) == self.findFather(b)

    def findFather(self, cur):
        path = []
        while cur != self.parents[cur]:
            path.append(cur)
            cur = self.parents[cur]

        while path:
            self.parents[path.pop()] = cur
        return cur

    def union(self, a, b):
        if a not in self.nodes or b not in self.nodes:
            return

        aHead = self.findFather(a)
        bHead = self.findFather(b)
        if aHead != bHead:
            aSize = self.sizeMap[aHead]
            bSize = self.sizeMap[bHead]
            big = aHead if aSize >= bSize else bHead
            small = bHead if aHead == big else aHead
            self.parents[small] = big
            self.sizeMap[big] = aSize + bSize
            self.sizeMap.pop(small)

