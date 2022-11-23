#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/11/18 20:04
# @Author  : HuntingGame
# @FileName: 407. 接雨水 II.py
# @Software: PyCharm
# C'est la vie. Enjoy ur day ! :D
import heapq
from typing import List


class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:

        N = len(heightMap)
        M = len(heightMap[0])

        isEnter = [[False] * M for i in range(N)]
        heap = []
        heapq.heapify(heap)
        # 首先让四周的进堆
        for i in range(M):
            isEnter[0][i] = True
            heapq.heappush(heap,info(heightMap[0][i],0,i))


class info:
    def __init__(self,val,x,y):
        self.val = val
        self.x = x
        self.y = y

