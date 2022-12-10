#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：6262. 图中最大星和.py
@Author ：HuntingGame
@Date ：2022-12-10 22:41 
C'est la vie!!! enjoy ur day :D
'''
import collections
from typing import List


class Solution:
    def maxStarSum(self, vals: List[int], edges: List[List[int]], k: int) -> int:
        if k == 0 or edges == []:
            return max(vals)
        # 首先排序，让edges里面ai < bi
        edges = [[each[0],each[1]] if each[0] < each[1] else [each[1],each[0]] for each in edges ]
        # 然后再排序
        edges.sort(key=lambda x:x[0])
        mycnts = collections.defaultdict(int)
        myedges = collections.defaultdict(list)
        for each in edges:
            mycnts[each[0]] +=1
            myedges[each[0]].append(each[1])
            myedges[each[1]].append(each[0])


        myprefix = [] # 第i个节点他的前缀和
        ans = 0
        i = 0
        for node in myedges.keys():
            # 每次看一个节点
            res = vals[node]
            step = len(myedges[node])
            idx = -1 # 非负坐标的位置
            tmp = []
            for j in range(step):
                if vals[myedges[node][j]] >=0:
                    idx +=1
                tmp.append(vals[myedges[node][j]])
            tmp.sort(reverse=True)
            if idx !=-1:
                if len(tmp) <=k:

                    res = max(res,res+sum(tmp[:idx+1]))
                else:

                    res = max(res,res+sum(tmp[:idx+1])) if idx <=k else max(res,res+sum(tmp[:k]))
            ans = max(ans,res)


        return ans

vals = [0,-36,4,35,27,-13]
edges = [[5,3],[4,3],[0,4],[2,4],[0,2]]
k = 1
print(Solution().maxStarSum(vals,edges,k))