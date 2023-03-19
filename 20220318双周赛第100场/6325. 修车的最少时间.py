#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：6325. 修车的最少时间.py
@Author ：HuntingGame
@Date ：2023-03-18 23:33 
C'est la vie!!! enjoy ur day :D
'''
import heapq
import math
from typing import List


class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        n = len(ranks)
        if n == 1:
            return ranks[0] * cars * cars

        ans = 0 #当前的最大耗时
        ranks.sort()
        i = 0
        deal = [0] * n
        mydeal = [[ranks[i],ranks[i],0] for i in range(len(deal))]
        mini = 0 #当前的最小索引
        heapq.heapify(mydeal)
        while cars>0:
            val,rank,idx = heapq.heappop(mydeal)
            print(val, rank)
            tmp = rank * (idx+1) ** 2

            ans = max(ans,val)
            heapq.heappush(mydeal,[tmp,rank,idx+1])
            #heapq.heapify(mydeal)
            cars -=1
        print(mydeal)
        return ans

print(Solution().repairCars([4,2,3,1],10))