#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：剑指 Offer 29. 顺时针打印矩阵.py
@Author ：HuntingGame
@Date ：2023-03-07 13:17 
C'est la vie!!! enjoy ur day :D
'''
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        a = 0
        b = 0
        c = len(matrix) - 1
        d = len(matrix[0]) -1
        ans = []
        while a <=c and b <=d:
            self.addEdge(matrix,a,b,c,d,ans)
            a+=1
            b+=1
            c-=1
            d-=1
        return ans


    def addEdge(self,matrix,a,b,c,d,ans):
        if a == c:
            # 单横线
            for i in range(b,d+1):
                ans.append(matrix[a][i])
        elif b ==d:
            #单竖线
            for i in range(a,c+1):
                ans.append(matrix[i][b])
        else:
            #一般情况
            #下面是四个框。上面俩都是最后的情况了。
            curC = b
            curR = a
            while curC !=d:
                ans.append(matrix[a][curC])
                curC +=1
            while curR !=c:
                ans.append(matrix[curR][d])
                curR +=1
            while curC !=b:
                ans.append(matrix[c][curC])
                curC -=1
            while curR !=a:
                ans.append(matrix[curR][b])
                curR -=1

