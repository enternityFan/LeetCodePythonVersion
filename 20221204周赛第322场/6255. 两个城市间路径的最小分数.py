#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：6255. 两个城市间路径的最小分数.py
@Author ：HuntingGame
@Date ：2022-12-04 10:59 
C'est la vie!!! enjoy ur day :D
'''
from typing import List


class Solution:
    def __init__(self):
        self.nodes = dict()
        self.parents = dict()
        self.sizeMap = dict()
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        # mydict = {}
        # for each in roads:
        #     if each[0] not in mydict:
        #         mydict[each[0]] = []
        #     mydict[each[0]].append(each[1])
        #     if each[1] not in mydict:
        #         mydict[each[1]] = []
        #     mydict[each[1]].append(each[0])
        #
        # #print(mydict)
        #
        # # 从n到1的推吧
        # ans = 1000000

        #并查集的做法，我只需要找与1，n连通的所有节点中最小的路径就行了

        # 初始化先
        for each in roads:
            self.nodes[each[0]] = each[0]
            self.parents[each[0]] = each[0]
            self.sizeMap[each[0]] = each[0]
            self.nodes[each[1]] = each[1]
            self.parents[each[1]] = each[1]
            self.sizeMap[each[1]] = each[1]

        # 开始合并，如果两个之间有，连接，那么就合并在一起
        for each in roads:
            self.union(each[0],each[1])
            self.union(each[1],each[0])
        print(self.parents)
        # 更新一下每个人的父节点
        for each in self.parents.keys():
            newfather = self.parents[each]
            while newfather in self.parents and self.parents[newfather] !=self.parents[each]:
                self.parents[each] = newfather
                newfather = self.parents[newfather]



        print(self.parents)

        ans = 10000000
        for each in roads:
            if self.parents[each[0]] ==self.parents[n] or self.parents[each[0]] ==self.parents[n] :
                ans = min(ans,each[2])

        return ans




    def isSameSet(self,a,b):
        if a not in self.nodes or b not in self.nodes:
            return
        return self.findFather(a) == self.findFather(b)

    def findFather(self,cur):
        path = []
        while cur !=self.parents[cur]:
            path.append(cur)
            cur = self.parents[cur]

        while path:
            self.parents[path.pop()] = cur
        return cur



    def union(self,a,b):
        if a not in self.nodes or b not in self.nodes:
            return

        aHead = self.findFather(a)
        bHead = self.findFather(b)
        if aHead != bHead:
            aSize = self.sizeMap[aHead]
            bSize = self.sizeMap[bHead]
            big = aHead if aSize >=bSize else bHead
            small = bHead if aHead == big else aHead
            self.parents[small] = big
            self.sizeMap[big] = aSize + bSize
            self.sizeMap.pop(small)





n = 20
roads =[[18,20,9207],[14,12,1024],[11,9,3056],[8,19,416],[3,18,5898],[17,3,6779],[13,15,3539],[15,11,1451],[19,2,3805],[9,8,2238],[1,16,618],[16,14,55],[17,7,6903],[12,13,1559],[2,17,3693]]
print(Solution().minScore(n,roads))