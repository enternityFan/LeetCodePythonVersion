#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：54. 螺旋矩阵.py
@Author ：HuntingGame
@Date ：2023-02-03 9:58 
C'est la vie!!! enjoy ur day :D
'''
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """
        还是整个框去把框里的打印对
        :param matrix:
        :return:
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return []
        a = 0
        b = 0
        c = len(matrix) - 1
        d = len(matrix[0]) - 1
        ans = []
        while a <=c and b <=d:
            self.addEdge(matrix,a,b,c,d,ans)
            a+=1
            b+=1
            c-=1
            d-=1

        return ans



    def addEdge(self,m,a,b,c,d,ans:List):

        if a == c: #单横线
            for i in range(b,d+1):
                ans.append(m[a][i])
        elif b == d:#单竖线
            for i in range(a,c+1):
                ans.append(m[i][b])
        else:
            #下面是四个框。上面俩都是最后的情况了。
            curC = b
            curR = a
            while curC !=d:
                ans.append(m[a][curC])
                curC +=1
            while curR !=c:
                ans.append(m[curR][d])
                curR +=1
            while curC !=b:
                ans.append(m[c][curC])
                curC -=1
            while curR !=a:
                ans.append(m[curR][b])
                curR -=1








